#!/usr/bin/env python3
"""Audita o banco de dados `memorial_servicos.json` usando regras extraídas dos recortes de auditoria."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "memorial_servicos.json"

LUMINARIA_PATTERN = re.compile(r"lumin[aá]ria", re.IGNORECASE)
ELEVATOR_PROJECT_DATA = re.compile(r"\b\d+\s*paradas?\b", re.IGNORECASE)


def load_db() -> list[dict[str, Any]]:
    with DB_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_db(db: list[dict[str, Any]]) -> None:
    with DB_PATH.open("w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        f.write("\n")


def normalize_text(value: Any) -> str:
    return str(value or "").strip()


def contains_luminaria(item: dict[str, Any]) -> bool:
    text = " ".join(
        normalize_text(item.get(k))
        for k in ["disciplina", "categoria_principal", "subcategoria", "servico_item", "descritivo_integral"]
    )
    return bool(LUMINARIA_PATTERN.search(text))


def check_luminaria_rule(db: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    for item in db:
        if contains_luminaria(item) and item.get("disciplina") != "Obras Civis":
            issues.append(
                f"ID {item.get('id')} contém luminária, mas disciplina é '{item.get('disciplina')}'. Deve ser Obras Civis."
            )
    return issues


def check_ppci_items(db: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    ppci = [item for item in db if item.get("disciplina") == "PPCI"]
    if not ppci:
        issues.append("Nenhum item com disciplina PPCI encontrado.")
        return issues

    expected_categories = {
        "Extintores": 1,
        "Sinalizacao de Emergencia": 1,
        "Iluminacao de Emergencia": 1,
        "Sistema de Pressurizacao": 1,
        "LGE": 1,
        "Sistema de CO2": 1,
        "Canalizacao Preventiva": 1,
        "Hidrantes Internos": 1,
        "Hidrante de Recalque": 1,
        "Sistema de Alarme": 1,
    }
    found = {cat: 0 for cat in expected_categories}
    for item in ppci:
        sub = normalize_text(item.get("subcategoria"))
        for cat in expected_categories:
            if cat.lower() in sub.lower() or cat.lower() in normalize_text(item.get("servico_item")).lower():
                found[cat] += 1
    for cat, count in found.items():
        if count == 0:
            issues.append(f"PPCI: falta item relacionado a '{cat}'.")
    if len(ppci) != len([c for c in expected_categories if found[c] > 0]):
        issues.append(
            f"PPCI: há {len(ppci)} itens em PPCI, mas {sum(1 for c in found if found[c] == 0)} categorias esperadas estão ausentes ou agrupadas."
        )
    return issues


def check_elevador_project_data(db: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    for item in db:
        if item.get("disciplina") == "Instalações Mecânicas" and "Elevador" in normalize_text(item.get("servico_item")):
            if ELEVATOR_PROJECT_DATA.search(normalize_text(item.get("servico_item"))):
                issues.append(
                    f"ID {item.get('id')} com elevador contém dado de projeto em título: '{item.get('servico_item')}'."
                )
    return issues


def check_paisagismo_exists(db: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    if not any(item.get("disciplina") == "Paisagismo" or item.get("disciplina") == "Paisagismo e Obras Externas" for item in db):
        issues.append("Nenhum item de Paisagismo encontrado no banco.")
    return issues


def check_servicos_finais(db: list[dict[str, Any]]) -> list[str]:
    issues: list[str] = []
    finais = [item for item in db if item.get("categoria_principal") == "Servicos Finais" or item.get("categoria_principal") == "Serviços Finais"]
    if len(finais) < 3:
        issues.append(
            f"Serviços Finais: apenas {len(finais)} item(ns) encontrados. O recorte identifica pelo menos limpeza final, as-built, manual do usuário e comissionamento/testes."
        )
    return issues


def apply_luminaria_fix(db: list[dict[str, Any]]) -> int:
    fixed = 0
    for item in db:
        if contains_luminaria(item) and item.get("disciplina") != "Obras Civis":
            item["disciplina"] = "Obras Civis"
            fixed += 1
    return fixed


def main() -> None:
    db = load_db()
    issues: list[str] = []
    issues.extend(check_luminaria_rule(db))
    issues.extend(check_ppci_items(db))
    issues.extend(check_elevador_project_data(db))
    issues.extend(check_paisagismo_exists(db))
    issues.extend(check_servicos_finais(db))

    print("AUDITORIA DO BANCO DE DADOS")
    print("=========================")
    print(f"Total de itens no banco: {len(db)}")
    print(f"Total de itens PPCI: {len([i for i in db if i.get('disciplina') == 'PPCI'])}")
    print(f"Total de itens Paisagismo: {len([i for i in db if i.get('disciplina') in ['Paisagismo', 'Paisagismo e Obras Externas']])}")
    print("")
    if issues:
        print("Regras violadas / pontos de atenção:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("Nenhuma inconsistência detectada pelo auditor.")

    if "--fix-luminarias" in sys.argv:
        fixed = apply_luminaria_fix(db)
        if fixed:
            save_db(db)
            print(f"\nCorrigido(s) {fixed} item(ns) de luminária para disciplina 'Obras Civis'.")
        else:
            print("\nNenhum item de luminária precisava de correção.")


if __name__ == "__main__":
    import sys
    main()
