#!/usr/bin/env python3
import json
from pathlib import Path

JSON_IN = Path(__file__).resolve().parents[1] / "data" / "memorial_servicos.json"

with open(JSON_IN, encoding="utf-8") as f:
    data = json.load(f)

novos = [
    {
        "id": 189,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Captação em Cobertura",
        "servico_item": "Calhas, Rufos e Condutores Verticais de Águas Pluviais",
        "descritivo_integral": "Fornecimento e instalação de calhas (em chapa galvanizada, alumínio ou PVC), rufos de arremate e condutores verticais para captação e condução das águas pluviais provenientes da cobertura. Inclui fixação, caimento mínimo de 0,5% nas calhas, bocais, grelhas de proteção contra folhas, conexões e ligação ao ramal enterrado ou caixa de captação. Deve atender ao projeto hidráulico predial e às prescrições da ABNT NBR 10844.",
        "normas_de_referencia": ["ABNT NBR 10844", "ABNT NBR 5626"],
        "servicos_vinculados": [
            "Instalação de rufos e arremates de cobertura",
            "Execução de ramal enterrado",
            "Ligação à caixa de captação ou sarjeta",
        ],
        "materiais_especificados": [
            "Calhas em chapa galvanizada ou alumínio conforme projeto",
            "Condutores verticais em PVC ou chapa galvanizada",
            "Rufos em chapa galvanizada ou alumínio",
            "Grelhas de proteção anti-entupimento",
            "Conexões, abraçadeiras e bocais",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 190,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Rede Enterrada",
        "servico_item": "Rede Enterrada de Águas Pluviais — Tubulações e Caixas de Passagem",
        "descritivo_integral": "Execução da rede enterrada de coleta e condução de águas pluviais, compreendendo escavação de valas, assentamento de tubulações (PVC rígido reforçado ou concreto conforme diâmetro), caixas de passagem com grelha ou tampa, reaterro compactado e recomposição de pavimento. O sistema deve atender ao projeto hidráulico, com declividade mínima de 0,5%, seções calculadas para chuvas de projeto e ligação ao lançamento final (rede pública, valeta ou corpo receptor).",
        "normas_de_referencia": ["ABNT NBR 10844", "ABNT NBR 9648", "ABNT NBR 8160"],
        "servicos_vinculados": [
            "Escavação e reaterro de valas",
            "Execução de caixas de passagem",
            "Recomposição de pavimento",
            "Ligação à rede pública ou corpo receptor",
        ],
        "materiais_especificados": [
            "Tubos PVC rígido reforçado série R ou tubos de concreto conforme diâmetro",
            "Conexões e peças especiais PVC",
            "Caixas de passagem em alvenaria ou pré-moldadas com tampa/grelha em ferro fundido",
            "Areia, brita e compactante para berço e reaterro",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 191,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Drenagem Superficial",
        "servico_item": "Canaletas, Valetas e Sarjetas de Drenagem Superficial",
        "descritivo_integral": "Execução de sistema de drenagem superficial para coleta e condução das águas pluviais em áreas externas, pátios, estacionamentos e vias internas. Compreende valetas em concreto moldado in loco ou pré-moldadas, canaletas em polímero com grelha, sarjetas e caixas coletoras, implantadas conforme declividade de projeto e conectadas ao sistema de coleta. Inclui escavação, regularização do fundo, assentamento, rejuntamento e ligação ao coletor ou corpo receptor.",
        "normas_de_referencia": ["ABNT NBR 10844", "ABNT NBR 9050", "DNIT 018/2004-PRO"],
        "servicos_vinculados": [
            "Terraplanagem e conformação do terreno",
            "Execução de meio-fio e guias",
            "Ligação ao sistema de coleta enterrado",
        ],
        "materiais_especificados": [
            "Canaletas poliméricas com grelha (aço galvanizado ou fundido) conforme classe de carga",
            "Valetas em concreto pré-moldado ou moldado in loco",
            "Concreto estrutural para sarjetas",
            "Argamassa de assentamento e rejunte",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 192,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Drenagem Profunda",
        "servico_item": "Drenos Franceses e Drenos Subterrâneos Perfurados",
        "descritivo_integral": "Execução de sistema de drenagem profunda para rebaixamento do lençol freático e controle de umidade em fundações, subsolos e muros de arrimo. Compreende escavação de valas, camadas de brita grossa, tubo perfurado corrugado em PEAD envolto em manta geotêxtil, reaterro com material drenante e saída para coletor ou poço de visita. O projeto deve ser elaborado com base em ensaios de permeabilidade do solo.",
        "normas_de_referencia": ["ABNT NBR 6118", "ABNT NBR 9800", "ABNT NBR 15875"],
        "servicos_vinculados": [
            "Impermeabilização de fundações e muros de arrimo",
            "Escavação de subsolos",
            "Execução de poço de visita ou bombeamento",
        ],
        "materiais_especificados": [
            "Tubo corrugado perfurado em PEAD com manta geotêxtil",
            "Brita nº 4 para camada drenante",
            "Manta geotêxtil não tecido (Bidim OP-30 ou equivalente)",
            "Caixas de inspeção e saída para coletor",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 193,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Tratamento e Controle",
        "servico_item": "Caixa Separadora de Areia e Sedimentação Pluvial",
        "descritivo_integral": "Fornecimento e instalação de caixas separadoras de areia e sedimentos provenientes das áreas de coleta de águas pluviais, antes do lançamento na rede pública ou corpo hídrico receptor. As caixas devem ser dimensionadas para a vazão de pico calculada, com tampa removível para limpeza periódica, câmara de sedimentação com volume adequado e estrutura em concreto armado ou PEAD conforme porte.",
        "normas_de_referencia": ["ABNT NBR 10844", "Resolução CONAMA 430/2011", "ABNT NBR 9800"],
        "servicos_vinculados": [
            "Rede enterrada de águas pluviais",
            "Caixas de passagem e grelhas",
            "Ligação ao lançamento final",
        ],
        "materiais_especificados": [
            "Caixa separadora em concreto armado ou PEAD conforme dimensionamento",
            "Tampa removível em ferro fundido ou concreto",
            "Tubos e conexões de entrada e saída",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 194,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Retenção e Amortecimento",
        "servico_item": "Reservatório de Detenção e Amortecimento de Cheias",
        "descritivo_integral": "Execução de reservatório de detenção (enterrado ou semienterrado) para amortecimento de picos de cheias, atendendo a exigências de legislação municipal ou estudo hidrológico. O volume deve ser calculado por método hidrológico compatível com o tempo de recorrência exigido. Compreende escavação, execução em concreto armado ou estrutura pré-moldada, dispositivo de saída controlada (orifício calibrado), extravasor e acesso para manutenção.",
        "normas_de_referencia": [
            "ABNT NBR 10844",
            "Legislação municipal de drenagem urbana aplicável",
            "ABNT NBR 6118",
        ],
        "servicos_vinculados": [
            "Rede enterrada de águas pluviais",
            "Estudo hidrológico e dimensionamento",
            "Sistema de controle de saída (orifício ou comporta)",
        ],
        "materiais_especificados": [
            "Concreto estrutural para estrutura do reservatório",
            "Impermeabilizante rígido ou flexível para face interna",
            "Dispositivo de saída em aço inox ou PEAD",
            "Tampa de acesso e grade de proteção",
        ],
        "ordem_planilha": 22,
    },
    {
        "id": 195,
        "disciplina": "Instalações Hidrossanitárias",
        "categoria_principal": "Águas Pluviais e Drenagem",
        "subcategoria": "Reúso",
        "servico_item": "Sistema de Captação e Reúso de Águas Pluviais",
        "descritivo_integral": "Implantação de sistema para captação, armazenamento, tratamento primário e distribuição de águas pluviais para fins não potáveis (irrigação, lavagem de pisos, descarga de bacias sanitárias). Inclui filtro de descarte de primeiras águas (first flush), cisterna de armazenamento, bombeamento, desinfecção e rede de distribuição segregada identificada em roxo. Deve atender à ABNT NBR 15527 e à legislação local.",
        "normas_de_referencia": [
            "ABNT NBR 15527",
            "ABNT NBR 5626",
            "Resolução CONAMA 357/2005",
        ],
        "servicos_vinculados": [
            "Instalação de calhas e condutores de captação",
            "Execução de cisterna ou reservatório de reúso",
            "Rede de distribuição não potável",
            "Sistema de bombeamento e tratamento",
        ],
        "materiais_especificados": [
            "Filtro de descarte de primeiras águas (first flush) conforme área de captação",
            "Cisterna em PEAD, fibra ou concreto conforme volume de projeto",
            "Bomba de recalque para distribuição",
            "Equipamento de desinfecção (UV ou dosador de cloro)",
            "Tubulação e acessórios em PVC cor roxa para rede não potável",
            "Identificação e sinalização de rede não potável",
        ],
        "ordem_planilha": 22,
    },
]

# Check for duplicate IDs
existing_ids = {d["id"] for d in data}
for n in novos:
    if n["id"] in existing_ids:
        print(f"AVISO: ID {n['id']} já existe, pulando.")
    else:
        data.append(n)

with open(JSON_IN, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total: {len(data)} serviços")
print("IDs adicionados:", [n["id"] for n in novos])
