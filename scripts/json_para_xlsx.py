#!/usr/bin/env python3
"""Converte memorial_servicos.json -> BANCO_ESPECIFICACOES.xlsx.

Formato esperado pelo frontend (SheetJS, range: 2):
  Linha 1: título da aba
  Linha 2: subtítulo
  Linha 3: cabeçalhos CHAVE | TIPO_SERVICO | NOME_SERVICO | NORMAS_ABNT | TEXTO_TECNICO
  Linha 4+: dados
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
JSON_IN = ROOT / "data" / "memorial_servicos.json"
XLSX_OUT = ROOT / "BANCO_ESPECIFICACOES.xlsx"

DISC_MAP = {
    "Obras Civis": ("civil", "Obras Civis"),
    "Instalações Elétricas": ("eletrica", "Instalações Elétricas"),
    "Instalações Hidrossanitárias": ("hidrossanitaria", "Instalações Hidrossanitárias"),
    "PPCI": ("ppci", "PPCI"),
    "Instalações Mecânicas": ("mecanica", "Instalações Mecânicas"),
    "Lógica e Telefonia": ("dados", "Dados, Voz e CFTV"),
    "Paisagismo": ("paisagismo", "Paisagismo"),
}

HEADERS = ["CHAVE", "TIPO_SERVICO", "NOME_SERVICO", "NORMAS_ABNT", "TEXTO_TECNICO"]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40]


def col_ref(index: int) -> str:
    letters = ""
    while index:
        index, remainder = divmod(index - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters


def cell_xml(row: int, col: int, value: str) -> str:
    ref = f"{col_ref(col)}{row}"
    return f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}</t></is></c>'


def row_xml(row_num: int, values: list[str]) -> str:
    return (
        f'<row r="{row_num}">'
        + "".join(cell_xml(row_num, idx, v) for idx, v in enumerate(values, 1))
        + "</row>"
    )


def worksheet_xml(disc_name: str, rows: list[list[str]]) -> str:
    data_rows = [
        row_xml(1, [f"BANCO_ESPECIFICACOES - {disc_name}"]),
        row_xml(2, ["Gerado a partir de memorial_servicos.json"]),
        row_xml(3, HEADERS),
    ]
    data_rows.extend(row_xml(i, r) for i, r in enumerate(rows, 4))
    last_row = max(3, len(rows) + 3)
    last_col = col_ref(len(HEADERS))
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<dimension ref="A1:{last_col}{last_row}"/>'
        '<sheetViews><sheetView workbookViewId="0"/></sheetViews>'
        '<sheetFormatPr defaultRowHeight="15"/>'
        f'<sheetData>{"".join(data_rows)}</sheetData>'
        "</worksheet>"
    )


def build_workbook(sheets: list[tuple[str, list[list[str]]]]) -> None:
    with ZipFile(XLSX_OUT, "w", ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            + "".join(
                f'<Override PartName="/xl/worksheets/sheet{i}.xml" '
                f'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                for i in range(1, len(sheets) + 1)
            )
            + "</Types>",
        )
        zf.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
            'Target="xl/workbook.xml"/>'
            "</Relationships>",
        )
        zf.writestr(
            "xl/workbook.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            "<sheets>"
            + "".join(
                f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
                for i, (name, _) in enumerate(sheets, 1)
            )
            + "</sheets></workbook>",
        )
        zf.writestr(
            "xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(
                f'<Relationship Id="rId{i}" '
                f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
                f'Target="worksheets/sheet{i}.xml"/>'
                for i in range(1, len(sheets) + 1)
            )
            + "</Relationships>",
        )
        for i, (name, rows) in enumerate(sheets, 1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", worksheet_xml(name, rows))


def main() -> None:
    items = json.loads(JSON_IN.read_text(encoding="utf-8"))

    # Agrupar por disciplina mantendo ordem de inserção
    por_disc: dict[str, list[list[str]]] = {}
    counters: dict[str, int] = {}

    for item in items:
        disc_raw = item.get("disciplina", "Obras Civis")
        disc_key, disc_name = DISC_MAP.get(disc_raw, ("civil", "Obras Civis"))

        if disc_name not in por_disc:
            por_disc[disc_name] = []
            counters[disc_name] = 0

        counters[disc_name] += 1
        seq = counters[disc_name]

        nome = item.get("servico_item", "")
        chave = f"{disc_key}|{seq:03d}-{slugify(nome)}"
        tipo = item.get("categoria_principal", "")
        normas = "; ".join(item.get("normas_de_referencia") or [])
        texto = item.get("descritivo_integral", "")

        por_disc[disc_name].append([chave, tipo, nome, normas, texto])

    sheets = list(por_disc.items())
    build_workbook(sheets)

    total = sum(len(v) for v in por_disc.values())
    print(f"Gerado {XLSX_OUT} com {total} serviços em {len(sheets)} abas:")
    for name, rows in sheets:
        print(f"  {name}: {len(rows)}")


if __name__ == "__main__":
    main()
