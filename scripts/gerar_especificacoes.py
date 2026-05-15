#!/usr/bin/env python3
"""Gera um banco inicial de especificacoes a partir de um roteiro modelo.

O sistema le cada aba a partir da terceira linha (range: 2 no SheetJS).
Cada servico precisa ter uma CHAVE iniciada pelo id da disciplina, no formato:
disciplina|codigo.
"""
from __future__ import annotations

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "especificacoes.xlsx"
ACCDOCS = Path(r"C:\Users\email\DC\ACCDocs")
MODELO_NOME = "SS-NIG-ESCOLASESI-EX-ORC-DOC-001-R02.docx"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

DISCIPLINAS = {
    "civil": "Obras Civis",
    "eletrica": "Instalações Elétricas",
    "hidrossanitaria": "Instalações Hidrossanitárias",
    "ppci": "PPCI - Prevenção e Combate a Incêndio",
    "climatizacao": "Climatização, Mecânica e Elevadores",
    "dados": "Dados, Voz e CFTV",
    "paisagismo": "Paisagismo e Obras Externas",
}

HEADERS = ["CHAVE", "TIPO_SERVICO", "NOME_SERVICO", "NORMAS_ABNT", "TEXTO_TECNICO"]

ACAO_RE = re.compile(
    r"^(A\s+CONTRATADA\s+dever[aá]|"
    r"Dever[aã]o?|"
    r"Execu[cç][aã]o|"
    r"Instala[cç][aã]o|"
    r"Fornecimento|"
    r"Constru[cç][aã]o|"
    r"Demoli[cç][aã]o|"
    r"Retirada|"
    r"Reforma|"
    r"Substitui[cç][aã]o|"
    r"Pintura|"
    r"Impermeabiliza[cç][aã]o|"
    r"Plantio|"
    r"Emiss[aã]o|"
    r"Apresenta[cç][aã]o|"
    r"Adequa[cç][aã]o)",
    re.IGNORECASE,
)

DESCARTAR_RE = re.compile(
    r"^(REV\\.|DATA|ELABORADO|VERIFICADO|APROVADO|ROTEIRO T[ÉE]CNICO|"
    r"FISCAL DO CONTRATO|GESTOR DO CONTRATO|PRAZO DE ENTREGA|QUALIFICA[CÇ][AÃ]O|"
    r"JUSTIFICATIVA|ESCOPO DOS PRINCIPAIS|Normas T[ée]cnicas Aplic[aá]veis)$",
    re.IGNORECASE,
)


def achar_modelo() -> Path:
    candidatos: list[Path] = []
    if ACCDOCS.exists():
        for dirpath, _, filenames in os.walk(ACCDOCS):
            if MODELO_NOME in filenames:
                candidatos.append(Path(dirpath) / MODELO_NOME)
    if not candidatos:
        raise FileNotFoundError(f"Roteiro modelo não encontrado: {MODELO_NOME}")
    return sorted(candidatos, key=lambda p: p.stat().st_mtime)[-1]


def paragrafos_docx(path: Path) -> list[str]:
    with ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
    paragrafos: list[str] = []
    for p in root.findall(".//w:p", NS):
        texto = "".join(t.text or "" for t in p.findall(".//w:t", NS))
        texto = re.sub(r"\s+", " ", texto).strip()
        if texto:
            paragrafos.append(texto)
    return paragrafos


def normalizar_nome(texto: str) -> str:
    texto = texto.strip(" ;,.-")
    texto = re.sub(r"\s+", " ", texto)
    if len(texto) <= 110:
        return texto
    corte = texto[:110].rsplit(" ", 1)[0]
    return corte + "..."


def classificar(texto: str) -> str:
    t = texto.lower()
    if re.search(r"cftv|voz|dados|rede lógica|telefonia|telecom|cabeamento estruturado", t):
        return "dados"
    if re.search(r"inc[êe]ndio|hidrante|extintor|alarme|detec[cç][aã]o|sprinkler|bombeiro|cbmerj|emerg[êe]ncia", t):
        return "ppci"
    if re.search(r"ar-condicionado|climatiza|split|exaust[aã]o|ventila[cç][aã]o|elevador|transporte vertical|mec[âa]nic", t):
        return "climatizacao"
    if re.search(r"el[eé]tric|quadro|cabo|eletrocalha|perfilado|lumin[áa]ria|tomada|spda|energia", t):
        return "eletrica"
    if re.search(r"hidr[áa]ul|sanit[áa]ri|esgoto|[áa]gua|pluvial|tubula[cç][aã]o|ralo|lou[cç]a|metal sanit", t):
        return "hidrossanitaria"
    if re.search(r"paisag|plantio|jardim|grama|muda|[áa]rvore|cal[cç]ada|pavimenta|intertravado|estacionamento|extern", t):
        return "paisagismo"
    return "civil"


def tipo_servico(texto: str, disc: str) -> str:
    t = texto.lower()
    if disc == "eletrica":
        if re.search(r"quadro|circuito|alimentador|disjuntor|energia", t):
            return "Quadros, circuitos e alimentação"
        if re.search(r"lumin[áa]ria|ilumina[cç][aã]o", t):
            return "Iluminação"
        return "Instalações elétricas gerais"
    if disc == "hidrossanitaria":
        if re.search(r"esgoto|sanit[áa]ri|ralo|lou[cç]a|metal", t):
            return "Esgoto sanitário, louças e metais"
        if re.search(r"[áa]gua|hidr[áa]ul|tubula[cç][aã]o|reservat", t):
            return "Água fria e instalações hidráulicas"
        if re.search(r"pluvial|drenagem|calha", t):
            return "Águas pluviais e drenagem"
        return "Instalações hidrossanitárias gerais"
    if disc == "ppci":
        if re.search(r"hidrante|mangueira|bomba|recalque", t):
            return "Hidrantes e rede de incêndio"
        if re.search(r"alarme|detec[cç][aã]o|sirene|acionador", t):
            return "Alarme e detecção de incêndio"
        if re.search(r"extintor|sinaliza[cç][aã]o|emerg[êe]ncia", t):
            return "Extintores, sinalização e emergência"
        return "Prevenção e combate a incêndio"
    if disc == "climatizacao":
        if re.search(r"elevador|transporte vertical", t):
            return "Elevadores e transporte vertical"
        if re.search(r"split|ar-condicionado|climatiza", t):
            return "Climatização"
        if re.search(r"exaust[aã]o|ventila[cç][aã]o|renova[cç][aã]o de ar", t):
            return "Exaustão e ventilação"
        return "Mecânica geral"
    if disc == "dados":
        if re.search(r"cftv|c[âa]mera", t):
            return "CFTV"
        if re.search(r"dados|voz|cabeamento|rede", t):
            return "Dados, voz e cabeamento"
        return "Sistemas de comunicação"
    if disc == "paisagismo":
        if re.search(r"plantio|jardim|grama|muda|[áa]rvore", t):
            return "Paisagismo"
        return "Áreas externas e pavimentação"
    if re.search(r"demoli|retirada|desmontagem|remo[cç][aã]o", t):
        return "Demolições e retiradas"
    if re.search(r"parede|veda[cç][aã]o|alvenaria|divis[óo]ria|drywall|gesso acartonado|chapa ciment", t):
        return "Paredes e vedações"
    if re.search(r"esquadria|porta|janela|vidro|guarda-corpo|brise|pele de vidro", t):
        return "Esquadrias, vidros e guarda-corpos"
    if re.search(r"piso|revestimento|cer[âa]mic|porcelanato|granito|soleira|peitoril|bancada|rodap", t):
        return "Pisos e revestimentos"
    if re.search(r"forro|teto|rebaixo", t):
        return "Forros e tetos"
    if re.search(r"pintura|textura|selador|massa corrida", t):
        return "Pintura e acabamento"
    if re.search(r"estrutura|funda[cç][aã]o|pilar|viga|laje|steel deck|met[áa]lic", t):
        return "Estruturas e fundações"
    if re.search(r"impermeabiliza|cobertura|telha|calha|rufo|dreno", t):
        return "Coberturas e impermeabilização"
    if re.search(r"canteiro|tapume|mobiliza|instala[cç][oõ]es provis[óo]rias|limpeza|res[ií]duo|entulho", t):
        return "Canteiro, logística e serviços preliminares"
    return "Serviços civis gerais"


def normas(texto: str, disc: str) -> str:
    achadas: list[str] = []
    for padrao in [
        r"ABNT\s+NBR\s*[A-Z]*\s*[\d\.\-:]+",
        r"NBR\s*[A-Z]*\s*[\d\.\-:]+",
        r"NR\s*[- ]?\s*\d+",
        r"NFPA\s*\d+",
        r"CBMERJ",
    ]:
        for item in re.findall(padrao, texto, re.IGNORECASE):
            item = re.sub(r"\s+", " ", item.upper()).strip()
            if item not in achadas:
                achadas.append(item)
    padroes = {
        "civil": ["ABNT NBR 15575", "ABNT NBR 16280"],
        "eletrica": ["ABNT NBR 5410", "NR 10"],
        "hidrossanitaria": ["ABNT NBR 5626", "ABNT NBR 8160"],
        "ppci": ["Normas CBMERJ", "ABNT NBR 9077"],
        "climatizacao": ["ABNT NBR 16401"],
        "dados": ["ABNT NBR 14565"],
        "paisagismo": ["ABNT NBR 16246"],
    }
    for item in padroes.get(disc, []):
        if item not in achadas:
            achadas.append(item)
    return "; ".join(achadas[:6])


def extrair_servicos(paragrafos: list[str]) -> dict[str, list[list[str]]]:
    inicio = next((i for i, p in enumerate(paragrafos) if "Relação dos principais serviços" in p), 0)
    fim = next((i for i, p in enumerate(paragrafos) if p.startswith("PRAZO DE ENTREGA")), len(paragrafos))
    candidatos = paragrafos[inicio:fim]
    por_disc = {k: [] for k in DISCIPLINAS}
    vistos: set[str] = set()
    for texto in candidatos:
        if DESCARTAR_RE.match(texto) or len(texto) < 25:
            continue
        if not ACAO_RE.match(texto):
            continue
        chave_base = re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")[:48]
        if chave_base in vistos:
            continue
        vistos.add(chave_base)
        disc = classificar(texto)
        seq = len(por_disc[disc]) + 1
        chave = f"{disc}|{seq:03d}-{chave_base or 'servico'}"
        por_disc[disc].append([chave, tipo_servico(texto, disc), normalizar_nome(texto), normas(texto, disc), texto])
    return por_disc


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
    return f'<row r="{row_num}">{"".join(cell_xml(row_num, idx, value) for idx, value in enumerate(values, 1))}</row>'


def worksheet_xml(title: str, rows: list[list[str]]) -> str:
    data_rows = [
        row_xml(1, [f"BANCO_ESPECIFICACOES - {title}"]),
        row_xml(2, ["Base inicial extraída do roteiro modelo"]),
        row_xml(3, HEADERS),
    ]
    data_rows.extend(row_xml(idx, row) for idx, row in enumerate(rows, 4))
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
        '</worksheet>'
    )


def build_workbook(sheets: list[tuple[str, list[list[str]]]]) -> None:
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            + "".join(
                f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                for i in range(1, len(sheets) + 1)
            )
            + '</Types>',
        )
        zf.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '</Relationships>',
        )
        zf.writestr(
            "xl/workbook.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<sheets>'
            + "".join(
                f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
                for i, (name, _) in enumerate(sheets, 1)
            )
            + '</sheets></workbook>',
        )
        zf.writestr(
            "xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(
                f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
                for i in range(1, len(sheets) + 1)
            )
            + '</Relationships>',
        )
        for i, (name, rows) in enumerate(sheets, 1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", worksheet_xml(name, rows))


def main() -> None:
    modelo = achar_modelo()
    por_disc = extrair_servicos(paragrafos_docx(modelo))
    sheets = [(DISCIPLINAS[did], rows) for did, rows in por_disc.items()]
    build_workbook(sheets)
    total = sum(len(rows) for rows in por_disc.values())
    print(f"Gerado {OUTPUT} com {total} serviços a partir de {modelo}")
    for did, rows in por_disc.items():
        print(f"- {did}: {len(rows)}")


if __name__ == "__main__":
    main()
