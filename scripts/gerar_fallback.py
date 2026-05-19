#!/usr/bin/env python3
"""Regenera a variável ESPECIFICACOES_FALLBACK embutida no index.html
a partir de data/memorial_servicos.json."""
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_IN = ROOT / "data" / "memorial_servicos.json"
INDEX = ROOT / "index.html"

DISC_MAP = {
    "Obras Civis":                    "civil",
    "Instalações Elétricas":          "eletrica",
    "Instalações Hidrossanitárias":   "hidrossanitaria",
    "PPCI":                           "ppci",
    "Instalações Mecânicas":          "climatizacao",
    "Lógica e Telefonia":             "dados",
    "Paisagismo":                     "paisagismo",
}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:40]


with open(JSON_IN, encoding="utf-8") as f:
    items = json.load(f)

por_disciplina: dict[str, list] = {}
for s in sorted(items, key=lambda x: (x.get("ordem_planilha", 99), x["id"])):
    disc_nome = s["disciplina"]
    did = DISC_MAP.get(disc_nome)
    if not did:
        print(f"  AVISO: disciplina desconhecida '{disc_nome}' (id {s['id']})")
        continue

    chave = f"{did}|{s['id']}"
    normas = "; ".join(s.get("normas_de_referencia") or [])
    obj = {
        "CHAVE":          chave,
        "GRUPO":          s.get("categoria_principal", ""),
        "SUBCATEGORIA":   s.get("subcategoria", ""),
        "NOME_SERVICO":   s.get("servico_item", ""),
        "NORMAS_ABNT":    normas,
        "TEXTO_TECNICO":  s.get("descritivo_integral", ""),
        "MATERIAIS":      s.get("materiais_especificados") or [],
        "SERVICOS_VINCULADOS": s.get("servicos_vinculados") or [],
    }
    por_disciplina.setdefault(did, []).append(obj)

fallback_obj = {"por_disciplina": por_disciplina}
js_value = json.dumps(fallback_obj, ensure_ascii=False, separators=(",", ":"))
new_line = f"var ESPECIFICACOES_FALLBACK = {js_value};\n"

html = INDEX.read_text(encoding="utf-8")

# Replace the line that starts with "var ESPECIFICACOES_FALLBACK ="
pattern = r"var ESPECIFICACOES_FALLBACK = \{.*?\};\n"
replaced = re.sub(pattern, new_line, html, count=1)

if replaced == html:
    print("ERRO: padrão não encontrado no index.html — nada foi alterado.")
else:
    INDEX.write_text(replaced, encoding="utf-8")
    total = sum(len(v) for v in por_disciplina.values())
    print(f"Fallback atualizado: {len(por_disciplina)} disciplinas, {total} serviços.")
    for did, lst in por_disciplina.items():
        print(f"  {did}: {len(lst)}")
