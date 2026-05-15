#!/usr/bin/env python3
"""Gera o arquivo cadastros.xlsx usado como consulta pelo sistema.

O projeto carrega as abas a partir da terceira linha (range: 2 no SheetJS),
por isso cada planilha mantém duas linhas introdutórias antes dos cabeçalhos.
"""
from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "cadastros.xlsx"
PRIMARY_UNIDADES_CSV = ROOT / "data" / "CNPJs_Enderecos.csv"
LEGACY_UNIDADES_CSV = ROOT / "data" / "unidades.csv"

RESPONSAVEIS = [
    ["Warren dos Santos Bastos", "WSB", "GER ENGENHARIA SEGURANCA", "", "GERENTE"],
    ["Luis Felipe Omena Viana De Vasconcellos", "LFOV", "COORD PROJETOS ENGENHARIA", "", "COORDENADOR"],
    ["Marcelo Derzie De Jesus Belache", "MDJB", "COORD OBRAS E MANUTENCAO", "", "COORDENADOR"],
    ["Angela Maria Lourenco", "AML", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Anna Carolina Dias Goncalves Pereira", "ACDGP", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Balu - Maria Lúcia Americano Freire", "MLAF", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Fabianne Manssour", "FM", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Gabriel Kreischer Tavares", "GKT", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Igor Freitas Dos Santos", "IFDS", "ENGENHEIRO(A) ELETRICISTA", "", "ENGENHEIRO"],
    ["Jorge Lucas Mendonca Dos Santos", "JLMDS", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Larissa Reis Ferreira Da Silva", "LRFS", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Luiz Henrique F Dos S Brandao Da Silva", "LHFBS", "ENGENHEIRO(A) MECANICO", "", "ENGENHEIRO"],
    ["Maisa Bastos da Silva Ligeiro", "MBSL", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Natasha Attalah F Fernandes", "NAFF", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Ana Paula Dos S Silva Ferreira Da Silva", "APSSFS", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Carlos Eduardo Corrêa", "CEC", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Daniele Haffner Marques De Oliveira Bran", "DHMOB", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Marcio Piza do Nascimento", "MPN", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Ribamar Dallaruvera", "RD", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
    ["Vladimir Gomes de Assis", "VGA", "ARQUITETO(A)", "", "ARQUITETO"],
    ["Wladimir Da Silva Costa", "WDSC", "ENGENHEIRO(A) CIVIL", "", "ENGENHEIRO"],
]

MODALIDADES = [
    ["Empreitada Global", "Contratação por valor global para execução completa do objeto."],
    ["Empreitada por Preço Unitário", "Contratação com medição por quantidades executadas e preços unitários."],
    ["Ata de Registro de Preços", "Contratação baseada em ata vigente para fornecimento ou serviços registrados."],
    ["Empreitada Integral", "Contratação integral do empreendimento, incluindo etapas necessárias à entrega final."],
    ["Contratação por Tarefa", "Contratação para mão de obra ou pequenas tarefas por preço certo."],
    ["Contratação Integrada", "Contratação que inclui elaboração de projeto básico/executivo e execução."],
    ["Contratação Semi-integrada", "Contratação que inclui projeto executivo e execução, a partir de projeto básico."],
    ["Fornecimento e Prestação de Serviço Associado", "Contratação combinada de fornecimento de bens e serviços vinculados."],
]

UNIDADE_HEADERS = [
    "SIGLA",
    "NOME_COMPLETO",
    "ENDERECO",
    "MUNICIPIO",
    "UF",
    "CNPJ",
    "TITULO",
    "INSC_MUNICIPAL",
    "INSC_ESTADUAL",
    "ANEXOS",
]


def separar_municipio_uf(valor: str) -> tuple[str, str]:
    partes = [p.strip() for p in valor.split("/")]
    if len(partes) >= 2:
        return partes[0], partes[-1]
    return valor.strip(), ""


def sigla_unidade(titulo: str, cnpj: str) -> str:
    titulo_limpo = re.sub(r"[^A-Z0-9]+", "-", titulo.upper()).strip("-")
    digitos = re.sub(r"\D", "", cnpj)
    filial = digitos[-6:-2] if len(digitos) >= 6 else digitos[-4:]
    return f"{titulo_limpo}-{filial}" if filial else titulo_limpo


def normalize_header_value(value: str) -> str:
    normalized = value.strip().replace("\ufeff", "").replace("\xa0", " ")
    normalized = unicodedata.normalize("NFKD", normalized)
    normalized = "".join(
        ch for ch in normalized
        if not unicodedata.combining(ch) and unicodedata.category(ch) != "Cf"
    )
    return normalized.upper()


def carregar_unidades() -> list[list[str]]:
    csv_path = PRIMARY_UNIDADES_CSV if PRIMARY_UNIDADES_CSV.exists() else LEGACY_UNIDADES_CSV
    with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
        linhas = csv.DictReader(csv_file)
        unidades = []
        for linha in linhas:
            normalized = {normalize_header_value(k): (v or "") for k, v in linha.items()}
            municipio, uf = separar_municipio_uf(normalized["MUNICIPIO / UF"])
            unidades.append([
                sigla_unidade(normalized["TITULO"], normalized["CNPJ"]),
                normalized["UNIDADE"].strip(),
                normalized["ENDERECO"].strip(),
                municipio,
                uf,
                normalized["CNPJ"].strip(),
                normalized["TITULO"].strip(),
                normalized["INSC. MUNICIPAL"].strip(),
                normalized["INSC. ESTADUAL"].strip(),
                normalized["ANEXOS"].strip(),
            ])
        return unidades


SHEETS = [
    ("UNIDADES", UNIDADE_HEADERS, carregar_unidades()),
    ("RESPONSAVEIS", ["NOME", "INICIAIS", "CARGO", "CREA_CAU", "PAPEL"], RESPONSAVEIS),
    ("MODALIDADES", ["MODALIDADE", "DESCRICAO"], MODALIDADES),
    ("TIPOS_SERVICO", ["NOME_SERVICO", "DESCRICAO_RESUMIDA"], []),
]


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
    cells = "".join(cell_xml(row_num, idx, value) for idx, value in enumerate(values, 1))
    return f'<row r="{row_num}">{cells}</row>'


def worksheet_xml(title: str, headers: list[str], rows: list[list[str]]) -> str:
    data_rows = [
        row_xml(1, [f"BANCO_CADASTROS - {title}"]),
        row_xml(2, ["Dados de consulta do sistema"]),
        row_xml(3, headers),
    ]
    data_rows.extend(row_xml(idx, row) for idx, row in enumerate(rows, 4))
    last_row = max(3, len(rows) + 3)
    last_col = col_ref(max(1, len(headers)))
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


def build_workbook() -> None:
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
                for i in range(1, len(SHEETS) + 1)
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
                for i, (name, _, _) in enumerate(SHEETS, 1)
            )
            + '</sheets></workbook>',
        )
        zf.writestr(
            "xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            + "".join(
                f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
                for i in range(1, len(SHEETS) + 1)
            )
            + '</Relationships>',
        )
        for i, (name, headers, rows) in enumerate(SHEETS, 1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", worksheet_xml(name, headers, rows))


if __name__ == "__main__":
    build_workbook()
    print(f"Gerado {OUTPUT} com {len(carregar_unidades())} unidades e {len(RESPONSAVEIS)} responsáveis.")
