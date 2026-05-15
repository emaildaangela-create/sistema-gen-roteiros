import pandas as pd
from docx import Document
import re
import unicodedata

# Dictionary mapping keywords to Macro Items from the Cost Spreadsheet
MACRO_ITEMS = {
    1: "1 - Serviços preliminares",
    2: "2 - Administração de obra",
    3: "3 - Demolições e retiradas",
    4: "4 - Movimento de terra",
    5: "5 - Fundação e estrutura convencional",
    6: "6 - Estrutura Metálica",
    7: "7 - Impermeabilizações",
    8: "8 - Telhados e coberturas",
    9: "9 - Alvenarias e vedações",
    10: "10 - Revestimentos e argamassas",
    11: "11 - Pisos e Pavimentações",
    12: "12 - Esquadrias",
    13: "13 - Forros e divisórias",
    14: "14 - Rodapés, Soleiras, Peitoris,Testeira, Bancadas e Prateleiras",
    15: "15 - Acessórios, louças e metais",
    16: "16 - Luminárias",
    17: "17 - Diversos",
    18: "18 - Pinturas",
    19: "19 - Marcenaria",
    20: "20 - Instalações elétricas",
    21: "21 - INSTALAÇÕES HIDRÁULICAS ÁGUA FRIA",
    22: "22 - INSTALAÇÕES DE ESGOTO SANITÁRIO / ÁGUAS PLUVIAIS",
    23: "23 - Instalações especiais",
    24: "24 - INSTALAÇÕES DE GASES",
    25: "25 - INSTALAÇÕES MECÂNICAS",
    26: "26 - ELEVADOR",
    27: "27 - INSTALAÇÕES DE INCÊNDIO",
    28: "28 - SUSTENTABILIDADE",
    29: "29 - URBANIZAÇÃO E PAISAGISMO",
    30: "30 - SERVIÇOS FINAIS"
}

# Mapping macro_id to the Frontend Tabs (Disciplines)
DISCIPLINAS_MAP = {
    20: ("eletrica", "Instalações Elétricas"),
    16: ("eletrica", "Instalações Elétricas"), # luminárias usually go to eletrica
    21: ("hidrossanitaria", "Instalações Hidrossanitárias"),
    22: ("hidrossanitaria", "Instalações Hidrossanitárias"),
    27: ("ppci", "PPCI - Prevenção e Combate a Incêndio"),
    24: ("climatizacao", "Climatização, Mecânica e Elevadores"),
    25: ("climatizacao", "Climatização, Mecânica e Elevadores"),
    26: ("climatizacao", "Climatização, Mecânica e Elevadores"),
    23: ("dados", "Dados, Voz e CFTV"),
    29: ("paisagismo", "Paisagismo e Obras Externas"),
}

def clean_text(text):
    return " ".join(text.split()).strip()

def create_key(disc_key, nome_servico, prefix_num):
    slug = str(nome_servico).lower()
    slug = unicodedata.normalize('NFKD', slug).encode('ASCII', 'ignore').decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    return f"{disc_key}|{prefix_num:03d}-{slug[:40]}"

def assign_macro_item(text, h2, h3):
    t_lower = (h2 + " " + h3 + " " + text).lower()
    if "demolição" in t_lower or "remoção" in t_lower or "retirada" in t_lower or "demolir" in t_lower:
        return 3
    if "ar-condicionado" in t_lower or "climatização" in t_lower or "exaustão" in t_lower or "splits" in t_lower:
        return 25
    if "elevador" in t_lower:
        return 26
    if "incêndio" in t_lower or "extintor" in t_lower or "hidrante" in t_lower or "lge" in t_lower or "alarme" in t_lower:
        return 27
    if "piso" in t_lower or "porcelanato" in t_lower or "pavimentação" in t_lower or "contrapiso" in t_lower or "calçamento" in t_lower or "intertravado" in t_lower or "degrau" in t_lower or "arquibancada" in t_lower:
        return 11
    if "pintura" in t_lower or "repintura" in t_lower or "esmalte" in t_lower:
        return 18
    if "esquadria" in t_lower or "vidro" in t_lower or "portão" in t_lower or "porta" in t_lower or "janela" in t_lower:
        return 12
    if "luminária" in t_lower or "refletor" in t_lower or "iluminação" in t_lower or "poste" in t_lower:
        return 16
    if "elétrica" in t_lower or "energia" in t_lower or "gerador" in t_lower:
        return 20
    if "hidráulica" in t_lower or "água" in t_lower or "chuveiro" in t_lower:
        return 21
    if "esgoto" in t_lower or "drenagem" in t_lower or "pluvial" in t_lower or "ete" in t_lower or "ralo" in t_lower:
        return 22
    if "impermeabilização" in t_lower or "manta" in t_lower:
        return 7
    if "telhado" in t_lower or "calha" in t_lower or "rufo" in t_lower or "cobertura" in t_lower or "platibanda" in t_lower:
        return 8
    if "bancada" in t_lower or "peitoril" in t_lower or "soleira" in t_lower or "prateleira" in t_lower:
        return 14
    if "louça" in t_lower or "metal" in t_lower or "acessório sanitário" in t_lower or "cuba" in t_lower or "lavatório" in t_lower:
        return 15
    if "metálica" in t_lower or "steel deck" in t_lower or "guarda-corpo" in t_lower or "corrimão" in t_lower or "alambrado" in t_lower or "escada" in t_lower:
        return 6
    if "alvenaria" in t_lower or "bloco cerâmico" in t_lower or "divisória" in t_lower or "drywall" in t_lower or "chapa cimentícia" in t_lower or "elemento vazado" in t_lower:
        return 9
    if "forro" in t_lower or "rebaixo" in t_lower or "isopor" in t_lower:
        return 13
    if "concreto" in t_lower or "laje" in t_lower or "pilar" in t_lower or "viga" in t_lower or "fundação" in t_lower or "sapata" in t_lower or "cinta" in t_lower or "mureta" in t_lower:
        return 5
    if "escavação" in t_lower or "reaterro" in t_lower or "terra" in t_lower or "movimentação" in t_lower:
        return 4
    if "árvore" in t_lower or "vegetação" in t_lower or "jardim" in t_lower or "paisagismo" in t_lower or "quadra de areia" in t_lower:
        return 29
    if "catraca" in t_lower or "voz" in t_lower or "dados" in t_lower or "cftv" in t_lower:
        return 23
    if "mdf" in t_lower or "marcenaria" in t_lower or "armário" in t_lower:
        return 19
    if "gás" in t_lower:
        return 24
    if "mobilização" in t_lower or "canteiro" in t_lower or "cronograma" in t_lower or "tapume" in t_lower or "provisória" in t_lower:
        return 1
    if "reunião" in t_lower or "art " in t_lower or "responsável" in t_lower or "fiscalização" in t_lower or "segurança do trabalho" in t_lower or "laudo" in t_lower:
        return 2
    if "limpeza final" in t_lower or "as built" in t_lower or "desmobilização" in t_lower:
        return 30
    
    return 17

def generate_specs():
    word_path = r"C:\Users\email\OneDrive\Documentos\GitHub\sistema-gen-roteiros\data\Referencias de banco de dados\SS-NIG-ESCOLASESI-EX-ORC-DOC-001-R02.docx"
    doc = Document(word_path)
    
    items = []
    
    in_escopo = False
    current_h2 = ""
    current_h3 = ""
    
    for para in doc.paragraphs:
        style = para.style.name
        text = clean_text(para.text)
        
        if not text:
            continue
            
        if "ESCOPO DOS PRINCIPAIS SERVIÇOS" in text:
            in_escopo = True
            
        if "QUALIFICAÇÃO TÉCNICA EXIGIDA" in text or "JUSTIFICATIVA PARA CONTRATAÇÃO" in text:
            in_escopo = False
            
        if in_escopo:
            if style.startswith("Heading 2") or (style == "Normal" and text.isupper()):
                current_h2 = text
                current_h3 = ""
            elif style.startswith("Heading 3") or (style == "Normal" and "–" in text and len(text) < 50):
                current_h3 = text
            elif style == "List Paragraph" and len(text) > 10:
                title = ""
                if current_h2 and current_h2.lower() != "escopo de intervenção":
                    title += current_h2 + " - "
                if current_h3:
                    title += current_h3 + " - "
                
                # Get the first short part of the paragraph as the core title
                core_title = text.split('.')[0]
                if len(core_title) > 80:
                    core_title = text.split(';')[0]
                if len(core_title) > 80:
                    core_title = core_title[:80] + "..."
                
                title += core_title.strip(';').strip('.')
                
                macro_id = assign_macro_item(text, current_h2, current_h3)
                
                items.append({
                    'macro_id': macro_id,
                    'TIPO_SERVICO': MACRO_ITEMS[macro_id],
                    'NOME_SERVICO': title,
                    'TEXTO_TECNICO': text + ('.' if not text.endswith(('.', ';')) else '')
                })

    # Deduplicate
    unique_items = []
    seen = set()
    for item in items:
        if item['TEXTO_TECNICO'] not in seen:
            seen.add(item['TEXTO_TECNICO'])
            unique_items.append(item)
            
    unique_items.sort(key=lambda x: x['macro_id'])
    
    # Split by disciplines for the frontend sheets
    sheets_data = {}
    
    for idx, item in enumerate(unique_items, 1):
        macro_id = item['macro_id']
        disc_key, disc_name = DISCIPLINAS_MAP.get(macro_id, ("civil", "Obras Civis"))
        
        if disc_name not in sheets_data:
            sheets_data[disc_name] = []
            
        sheets_data[disc_name].append({
            'CHAVE': create_key(disc_key, item['NOME_SERVICO'], len(sheets_data[disc_name]) + 1),
            'TIPO_SERVICO': item['TIPO_SERVICO'],
            'NOME_SERVICO': item['NOME_SERVICO'],
            'NORMAS_ABNT': 'ABNT NBR 15575; ABNT NBR 16280', # can be customized later if needed
            'TEXTO_TECNICO': item['TEXTO_TECNICO']
        })
        
    output_path = r"C:\Users\email\OneDrive\Documentos\GitHub\sistema-gen-roteiros\BANCO_ESPECIFICACOES.xlsx"
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, records in sheets_data.items():
            df = pd.DataFrame(records)
            
            # The frontend expects 2 rows of headers before the actual headers
            header1 = [f"BANCO_ESPECIFICACOES - {sheet_name}"] + [""] * (len(df.columns) - 1)
            header2 = ["Base inicial extraída do roteiro modelo"] + [""] * (len(df.columns) - 1)
            header3 = df.columns.tolist()
            
            # Create a new dataframe with the custom headers at the top
            top_rows = pd.DataFrame([header1, header2, header3], columns=df.columns)
            
            # Concatenate custom headers with data
            final_df = pd.concat([top_rows, df], ignore_index=True)
            
            # Write to excel without index and without default pandas header
            final_df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
            
    print(f"Generated {len(unique_items)} specifications across {len(sheets_data)} sheets in {output_path}")

if __name__ == "__main__":
    generate_specs()
