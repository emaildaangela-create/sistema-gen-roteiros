# Auditoria Capitulo 10 - Recorte 05

Fonte analisada: `data/Referencias de banco de dados/SS-NIG-ESCOLASESI-EX-ORC-DOC-001-R02.docx`

Texto extraido para consulta: `data/Referencias de banco de dados/roteiro_tecnico_extraido.txt`

Recorte analisado nesta etapa:

- `INSTALACOES ELETRICAS` — cabecalho e abertura (linhas 2863-2864)
- `NORMAS DE REFERENCIA` — lista normativa completa (linhas 2865-2964)
- `SERVICOS A EXECUTAR` — escopo geral (linhas 2965-3010)
- `DETALHAMENTO DOS SERVICOS — SUBESTACAO` (linhas 3013-3030)
- `NOVA INFRAESTRUTURA DE ENCAMINHAMENTO DE CIRCUITOS ELETRICOS` (linhas 3031-3075)
- `ESCAVACAO DE VALAS` — critérios de profundidade e caixas de inspeção (linhas 3077-3092)
- `CONDUTORES — CIRCUITOS TERMINAIS E ALIMENTADORES` (linhas 3093-3156)
- `CONDUTOS — ELETRODUTOS, ELETROCALHAS E PERFILADOS` (linhas 3157-3190)
- `CONSIDERACOES GERAIS SOBRE PAINEIS ELETRICOS` (linhas 3191-3254)
- `CONSIDERACOES PARA CARGAS ESPECIFICAS — GABINETES DE VENTILACAO, VENTILADORES INLINE E EXAUSTORES` (linhas 3235-3291)
- `SENSORES DE PRESENCA E INTERFACE PCD` (linhas 3293-3348)
- `DESCRICOES DOS MATERIAIS A UTILIZAR — BOTOEIRAS, ALARMES, TOMADAS` (linhas 3349-3408)
- `CAIXAS DE TOMADAS EMBUTIDAS NO PISO` (linhas 3409-3412)
- `SISTEMA DE ATERRAMENTO E SPDA` (linhas 3413-3531)

---

## 1. Criterio De Curadoria

O roteiro tecnico deve ser usado como fonte de tecnicas, requisitos, servicos, materiais e normas. Nao deve ser transcrito como memorial especifico do projeto.

Devem ser mantidos:

- metodos executivos genericos;
- requisitos de qualidade;
- criterios de seguranca;
- materiais-tipo e especificacoes tecnicas de condutores, condutos, quadros e dispositivos;
- normas tecnicas e regulamentadoras aplicaveis;
- atividades auxiliares necessarias para execucao do servico.

Devem ser removidos ou generalizados:

- nome da unidade ou escola especifica;
- referencias a ambientes especificos como salas de aula, biblioteca, refeitorio, ginasio;
- quantitativos especificos de equipamentos ou circuitos;
- referencias a projetos por numero de documento (ex: SN-ITAG-AMPLIACAO-EX-ELE-DIAG-001-R00);
- referencias contratuais como CONTRATANTE, CONTRATADA, FISCALIZACAO, certame;
- material removido e devolvido a CONTRATANTE (redacao contratual);
- pareceres tecnicos de orgaos especificos quando vinculados ao projeto (ex: parecer CBMERJ n° 14/2023).

---

## 2. Estrutura Fonte Identificada No Word

### 2.1 Lista Normativa — Linhas 2865 a 2964

O Word apresenta uma lista normativa extensa e heterogenea, cobrindo: seguranca do trabalho, baixa tensao, locais especiais, media tensao, combate a incendio, iluminacao de emergencia, cabos de potencia, dispositivos de protecao, conjuntos de manobra, condutos e acessorios, tomadas e interruptores, conectores e emendas, e protecao contra descargas atmosfericas.

A lista deve ser DISTRIBUIDA pelos itens especificos do banco — nao concentrada toda em um unico item geral.

Normas identificadas e sua classificacao recomendada:

**Normas-mae (item geral de instalacoes eletricas BT):**

- `NR-10` — seguranca em instalacoes e servicos com eletricidade; pertence a todos os itens eletricos
- `ABNT NBR 5410:2004` — instalacoes eletricas de baixa tensao; norma estruturante geral
- `ABNT NBR 13570:2021` — locais de afluencia de publico; pertence ao item principal BT e ao item de circuitos terminais
- `ABNT NBR 13534:2008` — estabelecimentos assistenciais de saude; pertence ao item principal quando aplicavel

**Normas especificas por item:**

- `ABNT NBR 14039:2021` — media tensao; pertence ao item de subestacao/autotransformador; nao ao item de infraestrutura geral de BT
- `ABNT NBR 5356-1:2007` — transformadores de potencia; pertence exclusivamente ao item de subestacao/autotransformador
- `ABNT NBR 5419-1:2015` — protecao contra descargas atmosfericas; pertence ao item SPDA
- `NF C 17-102:2011`, `UNE 21-186:2011`, `NP 4426:2013`, `IEC 62561`, `IEC 62305` — normas europeias/internacionais de SPDA PDI; pertencem ao item SPDA com captor PDI
- `ABNT NBR 13248:2014` — cabos nao halogenados ate 1 kV; pertence ao item de condutores/alimentadores
- `ABNT NBR NM 247-3:2002` — cabos PVC ate 450/750 V; pertence ao item de condutores terminais
- `ABNT NBR 8661:1997` — cabos planos PVC ate 750 V; pertence ao item de condutores terminais (uso em multipolar PP)
- `ABNT NBR 7286:2022` — cabos EPR/HEPR 1 kV a 35 kV; pertence ao item de alimentadores HEPR
- `ABNT NBR 7288:2018` — cabos PVC/PE 1 kV a 6 kV; pertence ao item de alimentadores
- `ABNT NBR IEC 60947-2:2013` — disjuntores BT; pertence ao item de quadros de distribuicao
- `ABNT NBR NM 60898:2004` — disjuntores residenciais/similares; pertence ao item de quadros de distribuicao
- `ABNT NBR IEC 60269-1:2003` — dispositivos fusiveis BT; pertence ao item de quadros de distribuicao
- `IEC 61009-1:2010` — RCBO (DR com sobrecorrente); pertence ao item de quadros de distribuicao
- `ABNT NBR IEC 62423:2020` — dispositivo corrente diferencial tipo B e F; pertence ao item de quadros
- `IEC 61643-1:2005` — DPS baixa tensao; pertence ao item de quadros/surtos
- `ABNT NBR IEC 60439-1:2003` — conjuntos de manobra PTTA/TTA; pertence ao item de quadros de distribuicao
- `ABNT NBR IEC 62208:2013` — involucros para conjuntos de manobra; pertence ao item de quadros de distribuicao
- `ABNT NBR 13057:2011` — eletroduto rigido aco-carbono zincado eletroliticamente; pertence ao item de eletrodutos
- `ABNT NBR 5624:2011` — eletroduto rigido aco-carbono galvanizado a fogo; pertence ao item de eletrodutos
- `ABNT NBR IEC 61537:2013` — eletrocalhas e leitos de cabos; pertence ao item de eletrocalhas e leitos
- `ABNT NBR IEC 61084:2022` — perfilados e canaletas nao circulares; pertence ao item de perfilados
- `ABNT NBR 15465:2020` — eletrodutos plasticos BT; pertence ao item de eletrodutos PVC
- `ABNT NBR 15701:2016` — conduletes metalicos; pertence ao item de condutores terminais e caixas de passagem
- `ABNT NBR 14136:2012` — tomadas e plugues domesticos ate 20 A; pertence ao item de tomadas e interruptores TUG
- `ABNT NBR NM 60884-1:2010` — plugues e tomadas; pertence ao item de tomadas e interruptores
- `ABNT NBR NM 60669-1:2004` — interruptores fixos domesticos; pertence ao item de tomadas e interruptores
- `ABNT NBR IEC 60309-1:2015` — plugues e tomadas industriais; pertence ao item de tomadas TUE/industrial
- `ABNT NBR 9326:2014` — conectores para cabos de potencia; pertence ao item de condutores/emendas
- `ABNT NBR 9513:2010` — emendas para cabos ate 750 V; pertence ao item de condutores terminais e alimentadores
- `CBMERJ Nota Tecnica 2-04:2019` — pressurização combate a incendio; pertence ao item de alarmes/incendio, nao ao item geral de eletrica
- `CBMERJ Nota Tecnica 2-06:2019` — iluminacao de emergencia; pertence ao item especifico de iluminacao de emergencia
- `CBMERJ Nota Tecnica 2-07:2019` — deteccao e alarme de incendio; pertence ao item de alarmes PCD e integracoes

### 2.2 Servicos a Executar — Linhas 2965 a 3010

Escopo geral identificado no Word:

- remoção completa de infraestrutura de BT obsoleta (paineis, cabos, eletrocalhas, eletrodutos, leitos, perfilados, suportes, caixas de passagem, tomadas, interruptores);
- fornecimento e instalacao de nova infraestrutura BT;
- instalacao de dutos PEAD corrugado flexivel no subterraneo para circuitos de distribuicao e terminais;
- envelopamento em concreto com camada superior minima de 5 cm em trechos especificos;
- equipotencializacao de todos os elementos metalicos;
- fornecimento e instalacao de autotransformador trifasico a seco 300 kVA 220/380 V;
- quadros eletricos novos, comissionamento;
- botoeiras e sirene para banheiros PCD;
- alarmes visuais PCD;
- SPDA com dispositivo de ionizacao (Metodo Ionizante).

Conteudo aproveitavel para o banco (generalizando):

- metodo de remocao e reinstalacao de infraestrutura eletrica BT;
- criterios de instalacao de dutos subterraneos PEAD;
- equipotencializacao geral;
- subestacao com autotransformador a seco;
- quadros de distribuicao;
- alarmes acessibilidade PCD;
- SPDA.

Conteudo a descartar/generalizar:

- referencias a salas, laboratorios, biblioteca, refeitorio como ambientes especificos;
- quantidade fixada de autotransformadores;
- referencias a banheiros PCD como locais especificos — manter como criterio de projeto.

### 2.3 Subestacao / Autotransformador — Linhas 3013 a 3030

Especificacoes tecnicas identificadas:

- enrolamento em aluminio;
- classe de isolamento 1,1 kV;
- potencia nominal 300 kVA;
- tensao primaria 220 V, secundaria 380 V;
- grau de protecao IP23;
- elevacao de temperatura 105 °C;
- referencia Wise ou similar.

Conteudo aproveitavel: as especificacoes tecnicas sao genericas e reutilizaveis para qualquer projeto de adequacao de tensao com autotransformador de mesma faixa.

### 2.4 Nova Infraestrutura de Encaminhamento — Linhas 3031 a 3075

Subtemas identificados:

- remoção e reinstalacao de infraestrutura aparente e embutida;
- cabos de cobre flexivel antichama: PVC 70°C 450/750 V para terminais; HEPR 90°C 0,6/1 kV para alimentadores;
- padrao de cores de condutores: vermelho (fase R), branco (fase S), preto (fase T), verde (PE), azul claro (neutro), amarelo (retorno), verde-amarelo (equipotencializacao);
- identificacao por fita isolante colorida nos cabos HEPR nas duas extremidades;
- equipotencializacao de todos os elementos metalicos pertencentes e nao pertencentes a instalacao eletrica;
- condutor equipotencializacao elementos da instalacao: 4 mm² verde-amarelo, classe 5, PVC 450/750 V, conectado a barra PE do QD;
- condutor equipotencializacao elementos externos: 6 mm² verde-amarelo, classe 5, PVC 450/750 V, conectado a barra PE do QD;
- continuidade eletrica de eletrocalhas garantida por saida para perfilado com parafuso, porca e arruela;
- continuidade eletrica de eletrodutos garantida por saidas horizontais ou verticais nas eletrocalhas.

### 2.5 Escavacao de Valas — Linhas 3077 a 3092

Criterios tecnicos identificados:

- linhas eletricas no solo posicionadas no minimo 10 cm acima do fundo da caixa de passagem (prevencao de inundacao);
- circuitos terminais: profundidade minima 0,3 m;
- circuitos alimentadores: profundidade minima 0,7 m;
- largura da vala igual a largura da caixa de passagem;
- paredes internas das caixas em blocos de concreto;
- fundo coberto com concreto magro.

Observacao: este subtema deve ser um criterio dentro do item de infraestrutura de encaminhamento subterraneo ou dentro do item geral de infraestrutura BT, nao um item isolado de escavacao de vala (que ja existe em Movimento de Terra).

### 2.6 Condutores — Circuitos Terminais e Alimentadores — Linhas 3093 a 3156

Circuitos terminais identificados (tipo 1.1.1):

- cabo de cobre, classe 5 (flexivel), isolacao PVC 70°C, 450/750 V, antichama, baixa emissao de gases toxicos (ATOX);
- valido para: circuitos de luz, tomadas, evaporadores, ventiladores, gabinetes de ventilacao e condensadoras split.

Circuitos terminais para cargas especiais (tipo 1.1.2):

- cabo de cobre, classe 5 (flexivel), isolacao HEPR 90°C, 0,6/1 kV, unipolar, antichama;
- valido para: condensadoras VRF, bombas de piscina, trocadores de calor.

Identificacao e encaminhamento de terminais:

- encaminhamento em eletrocalhas e perfilados em camada unica, justapostos;
- identificacao em ambas as extremidades por anilhas ou luvas (quadros) e fita adesiva (caixas, conduletes e pontos terminais);
- derivacoes (secao <= 4 mm²) com conector tipo guilhotina scotchlok ou similar nas caixas de passagem;
- cabos 380 V identificados com etiquetas adesivas "380 V" a cada 2 m.

Circuitos de distribuicao / alimentadores (tipo 2):

- cabo de cobre, classe 5 (flexivel), isolacao HEPR 90°C, 0,6/1 kV, unipolar, antichama;
- cor preta com fita isolante colorida para identificacao de fase; luva transparente para identificacao de circuito;
- encaminhamento em eletrodutos, bandejas e leitos em configuracao trifolia;
- fixacao a cada 1,5 m por abracadeira de nylon.

Cabos multipolares PP para rabichos de luminarias:

- cabo PP multipolar 3 condutores (fase, fase, terra), 2,5 mm², PVC 70°C, 450/750 V, antichama, ATOX;
- plugue femea na caixa de passagem; plugue macho nas luminarias.

Cabos PP para alimentacao de evaporadoras via condulete tipo E:

- cabo PP 3×2,5 mm², PVC 450/750 V, antichama, ATOX;
- condulete metalico tipo E com tampa com furo.

### 2.7 Condutos — Eletrodutos, Eletrocalhas e Perfilados — Linhas 3157 a 3190

Eletrodutos — criterios por ambiente:

- aparentes internos: aco-carbono zincado eletroliticamente, leve — ABNT NBR 13057:2011;
- externos ou ambientes agressivos: aco-carbono galvanizado a fogo pesado — ABNT NBR 5624:2011;
- exclusivos no entreforro sem trechos aparentes: PVC rigido cor preta — ABNT NBR 15465:2020;
- fixacao na laje: abraçadeira tipo D, tirante ou barra rosqueada 1/4", pino com rosca e porca longa a cada 1,5 m;
- aparentes sobre parede: abraçadeira tipo D.

Eletrocalhas perfuradas e leitos:

- internos: aco-carbono pre-galvanizado, sem tampa (eletrocalhas apenas) — ABNT NBR IEC 61537:2013;
- externos: aco-carbono galvanizado a fogo, com tampa (eletrocalhas apenas) — ABNT NBR IEC 61537:2013;
- fixacao em laje: suporte tipo balanco vertical, tirante 1/4", pino com rosca e porca longa a cada 1,5 m;
- prumadas de leito: fixacao sobre alvenaria com juncao L em ambas as extremidades.

Perfilados:

- material: aco-carbono pre-galvanizado — ABNT NBR IEC 61084:2022;
- fixacao em laje: suporte tipo grampo J, tirante 1/4", pino com rosca a cada 1,5 m;
- faceando paredes: suporte tipo mao francesa com base L = 75 mm a cada 1,5 m.

Condutos nao metalicos aparentes:

- todos devem ser nao-propagantes de chama e com baixa emissao de gases toxicos — ABNT NBR 5410, item 5.2.2.2.3.

### 2.8 Quadros de Distribuicao — Linhas 3191 a 3254

Especificacoes gerais dos paineis:

- tipo PTTA, com suportabilidade a esforcos termicos e dinamicos do nivel de curto presumido;
- tipo sobrepor;
- grau de protecao IP54;
- caixa pintura eletrostatica em po poliester cinza RAL 7032;
- placa de montagem em chapa de aco pintura alaranjada (2,5YR614 ou RAL 2000);
- fecho tipo lingueta reta triangulo;
- barreira de acrilico interna contra contato acidental com partes vivas;
- sinaleira LED vermelha Φ22 mm para indicacao de energizacao sobre porta;
- placa de advertencia contra risco de choque eletrico sobre porta;
- porta-documentos A3 na face interna da porta.

Conteudo a descartar: referencias a numeros de projeto de diagrama (SN-ITAG-AMPLIACAO-EX-ELE-DIAG-001 a 014); referencias a aprovacao pela CONTRATANTE; referencias a engenharia da CONTRADA (sic).

Layout recomendado: organizacao de placa de montagem com entrada e saida de alimentadores pela face superior, conforme layout tecnico generico.

### 2.9 Cargas Especificas — Gabinetes de Ventilacao — Linhas 3235 a 3255

Especificacoes tecnicamente aproveitaveis para o banco:

- partida direta com comando manual na porta do painel;
- chave seletora local/automatico;
- DPS Classe II com protecao backup;
- protecao contra sobrecorrentes e falta de fase;
- indicacao visual de energizacao individual e geral;
- diagrama de forca e comando como referencia de logica de comando.

Conteudo a descartar: referencias a casa de maquinas especifica; referencias a figuras numeradas do projeto.

### 2.10 Ventiladores Inline e Exaustores de Banheiro — Linhas 3257 a 3291

Subtemas tecnicos aproveitaveis:

- acionamento por contator monofasico (ex.: Finder Serie 22 ou similar);
- diagrama funcional de acionamento direto via circuito de iluminacao;
- comando por interruptor bipolar para exaustores de banheiro;
- protecao contra surtos (DPS Classe II) e sobrecorrentes.

Observacao: este subtema e especifico de instalacoes mecanicas/ventilacao; pode ser referenciado no item de instalacoes eletricas como servico vinculado, nao como item proprio.

### 2.11 Sensores de Presenca — Linhas 3293 a 3323

Especificacoes tecnicamente aproveitaveis:

- sensor de presenca para teto, altura aproximada 2,4 m;
- tensao 100 a 240 VCA bivolt automatico;
- alcance ate Ø 7 m a 25°C;
- angulo de cobertura ate 360°;
- regulagem de tempo: 1 s, 30 s, 1 min, 3 min, 7 min, 15 min;
- recontagem automatica a partir da ultima deteccao;
- fotocélula regulavel;
- material: corpo ABS cor branca;
- sobrepor e embutir no mesmo produto.

Conteudo a generalizar: eliminar referencias a banheiros especificos como locais de instalacao; manter como criterio de especificacao generico.

### 2.12 Alarmes e Botoeiras PCD — Linhas 3349 a 3388

Especificacoes aproveitaveis:

- alarme audiovisual sobre porta externa do banheiro PCD, altura 2,30 m;
- botoeira de emergencia tipo soco na caixa de passagem 4×2, embutida, a 40 cm do piso;
- alarme visual nas salas: cor amarela (sinal de aula) e cor vermelha (alarme de incendio);
- integracao do alarme vermelho com sistema de deteccao de incendio;
- botao com contraste de cor em relacao a parede;
- dimensao minima do botao: 2,5 cm;
- controle de acionamento por alavanca ou pressao;
- posicionamento obrigatorio proximo a bacia sanitaria.

Norma mencionada: NBR 9050:2020, item 4.6.7.

Conteudo a descartar: referencias a salas de aula, laboratorio, biblioteca, refeitorio como locais especificos.

### 2.13 Tomadas e Interruptores — Linhas 3391 a 3407

Especificacoes aproveitaveis:

- tomadas e interruptores embutidos ou aparentes em caixa 4×2 PVC ou condulete metalico de aluminio;
- alimentacoes especificas (condensadoras, bombas, boiler) em conduletes metalicos com tampa com furo;
- etiqueta nas tampas com indicacao de tensao e circuito;
- interruptores bipolares simples 10 A / 250 V em caixa 4×2 ou condulete;
- interruptores bipolares paralelos (three-way) quando indicado;
- espelhos conforme tipo de caixa e tecla utilizada;
- todas as tomadas polarizadas com condutor de protecao (terra) — ABNT NBR 14136:2012.

### 2.14 Caixas de Tomadas Embutidas no Piso — Linhas 3409 a 3411

Especificacoes aproveitaveis:

- corpo em plastico de engenharia;
- tamanho: 150×250×60 mm;
- 4 alojamentos para tomadas padrao brasileiro;
- 4 suportes para conectores RJ45;
- tampa basculante 190×190 mm em aco inox escovado;
- fornecimento com modulos de tomadas e conectores RJ45 instalados.

### 2.15 Sistema de Aterramento e SPDA — Linhas 3413 a 3490

Sistema SPDA com captor PDI:

- fornecimento e instalacao especializada de captacao, descida e aterramento;
- captor com dispositivo de ionizacao (metodo ionizante);
- antecipacao de descarga proporcionando raio de protecao maior;
- eficacia de atuacao ΔT = 60 μs;
- desvio padrao σ PDI < 0,53 σ PTS;
- teste de corrente onda 10/350 μs (Iimp): 100 kA (normativo);
- teste de corrente maxima Imax: 200 kA;
- deteccao do lider ascendente por monitoramento continuo de gradiente e variacao de campo eletrico (ΔE/Δt);
- dispositivo de ionizacao: centelhamento por impulso de alta tensao;
- ponta central do captor: continuidade eletrica, 200 m² cobre niquelado;
- caixa metalica: aco inoxidavel 316, blindagem CEM;
- referencia: Pevectron 3 S60 ou similar.

Sistema de aterramento do SPDA:

- cabos de cobre nu normatizado #50 mm² (7 fios) nas descidas;
- 3 hastes de terra copperweld alta camada (254 micras) de 5/8"×2,4 m por descida;
- hastes interligadas entre si;
- conjuntos de aterramento interligados entre si e conectados ao barramento do QDG para equipotencializacao;
- barramento de equipotencial principal (BEP) na subestacao, interligado a malha de aterramento existente;
- todas as conexoes cabo-cabo e cabo-haste por solda exotermica;
- cabos de aterramento #50 mm² em valas individuais; podem seguir paralelo a outras valas respeitando as alturas normativas.

### 2.16 Metodo de Execucao dos Servicos — Linhas 3492 a 3531

Condutores e acessorios — criterios de execucao:

- emendas somente no interior das caixas;
- vedado emenda de condutores no interior de eletrodutos;
- vedado uso de fita isolante como emenda nos casos indicados;
- cabos amarrados com abracadeiras plasticas em quadros, eletrocalhas e perfilados;
- terminais tipo ilhos (olhal) nos cabinhos conectados a disjuntores;
- abracadeiras e etiquetas de identificacao de circuitos em todos os paineis.

Eletrodutos — criterios de execucao:

- ligacao a caixas e eletrocalhas com bucha e arruela de diametro externo igual ao do eletroduto + bucha contra porca interna (instalacao aparente);
- conexao a caixas 4×2 embutidas em parede por eletroduto flexivel corrugado;
- sem angulos de curvatura inferiores a 90°;
- corte perpendicular ao eixo com retirada de rebarbas;
- eletrodutos nao podem ser inclinados no interior das caixas;
- arame guia #16 galvanizado, sobra minima de 20 cm em cada extremidade;
- extremidades livres obturadas com caps (vedado buchas de madeira ou papel);
- eletrodutos flexiveis: sem emendas, raio de curvatura minimo de 12× o diametro externo, fixacao por abracadeiras a no maximo 1,0 m.

Tomadas — criterio de execucao:

- todas as tomadas polarizadas e com condutor de protecao (terra).

---

## 3. Estado Atual Do Banco

Arquivo analisado: `data/memorial_servicos.json`

Itens atualmente relacionados ao recorte (disciplina `Instalacoes Eletricas` ou subcategoria de mesma disciplina):

| ID | Disciplina | Categoria | Subcategoria | Item atual |
|---:|---|---|---|---|
| 9 | Instalações Elétricas | Instalações Provisórias | Instalações Elétricas Provisórias | Infraestrutura Elétrica Provisória do Canteiro |
| 112 | Instalações Elétricas | Instalações Provisórias | Instalações Elétricas Provisórias | Iluminação Aparente Provisória em Canaleta ou Eletrocalha |
| 58 | Instalações Elétricas | Instalações Elétricas | Infraestrutura Elétrica | Infraestrutura Elétrica de Baixa Tensão – Remoção e Nova Instalação |
| 59 | Instalações Elétricas | Instalações Elétricas | Quadros Elétricos | Quadros de Distribuição BT – IP54 RAL 7032 |
| 60 | Instalações Elétricas | Instalações Elétricas | Autotransformador | Autotransformador Trifásico 300 kVA 220/380V a Seco IP23 |
| 61 | Instalações Elétricas | SPDA | Para-Raios PDI | SPDA com Captores PDI Pevectron 3 S60 – ΔT=60 μs |
| 62 | Instalações Elétricas | Instalações Elétricas | Sensores e Alarmes PCD | Sensores de Presença 360° e Alarmes Visuais PCD MINI-CSL |
| 63 | Instalações Elétricas | Instalações Elétricas | Tomadas Especiais | Tomadas de Piso em Inox Escovado 150×250 mm – NBR 14136 |

Total atual: 8 itens (2 provisorios, 6 definitivos).

---

## 4. Diagnostico Tecnico

### 4.1 Item 9 — Infraestrutura Eletrica Provisoria do Canteiro

Estado: resumido.

Coberto adequadamente:

- condutores PVC 70°C 2,5 mm² para iluminacao;
- cabos HEPR 90°C 0,6/1 kV para alimentadores;
- quadro provisorio;
- NR-10 e NBR 5410.

Faltante ou insuficiente:

- sem descritivo de eletrodutos ou eletrocalhas provisorias;
- sem criterios de aterramento provisorio;
- sem mencao a identificacao de circuitos provisorios;
- materiais especificados simplificados demais para um item reutilizavel;
- nao menciona criterios de desligamento e retirada ao final da obra.

### 4.2 Item 112 — Iluminacao Aparente Provisoria

Estado: adequado como item separado, mas descritivo ainda generico.

Coberto adequadamente:

- canaleta PVC ou eletrocalha;
- condutores PVC 2,5 mm²;
- NR-10, NBR 5410, NR-18.

Faltante:

- sem mencao a interruptores bipolares para controle de iluminacao provisoria;
- sem criterio de protecao (disjuntor no quadro provisorio);
- sem criterio de desmontagem.

### 4.3 Item 58 — Infraestrutura Eletrica BT

Estado: muito compacto para o volume de informacao tecnica disponivel.

Coberto adequadamente:

- remoção e nova instalacao;
- eletrodutos por tipo de ambiente (interno/externo/entreforro);
- eletrocalhas perfuradas;
- cabos HEPR e PVC com diferenciacoes;
- valas com profundidades corretas;
- equipotencializacao mencionada;
- NBR 13534, NBR 13570, NBR 5410, NR-10.

Faltante ou excessivamente agrupado:

- padrão de cores de condutores (vermelho/branco/preto/verde/azul/amarelo/verde-amarelo) nao consta no descritivo;
- criterios de identificacao de circuitos (anilhas, luvas, fita adesiva, etiquetas 380 V) ausentes;
- criterios de execucao de eletrodutos (bucha e arruela, arame guia, caps, angulo minimo, corte perpendicular) ausentes;
- conector tipo guilhotina scotchlok para derivacoes ate 4 mm² nao consta;
- PEAD corrugado flexivel subterraneo e envelopamento em concreto nao constam;
- continuidade de equipotencializacao em eletrocalhas/perfilados ausente;
- conduletes metalicos tipo E para alimentacao de evaporadoras ausentes;
- cabos PP multipolares para rabichos de luminarias ausentes;
- criterios de execucao de perfilados ausentes;
- fixacao de alimentadores em trifolia ausente;
- normas de cabos (NBR 13248, NBR NM 247-3, NBR 7286, NBR 7288) ausentes;
- normas de condutos (NBR 13057, NBR 5624, NBR 15465, NBR IEC 61537, NBR IEC 61084, NBR 15701) ausentes.

Problema de agrupamento: este item une remoção, nova instalacao, eletrodutos, eletrocalhas, perfilados, cabos terminais e alimentadores em um unico item. O resultado e um descritivo com pouca profundidade em cada subtema.

### 4.4 Item 59 — Quadros de Distribuicao BT

Estado: compacto e tecnicamente razoavel para um item de banco, mas com lacunas.

Coberto adequadamente:

- IP54 RAL 7032;
- placa RAL 2000;
- fecho lingueta triangulo;
- disjuntores, DR, DPS;
- sinaleira LED vermelha;
- porta-documentos A3;
- ABNT NBR IEC 60439-1 (via IEC 61439 no campo normas — divergencia de codigo);
- NR-10, NBR 5410, NBR 14039.

Problemas identificados:

- `ABNT NBR 14039` no item de quadros de distribuicao BT e incorreto; essa norma e de media tensao (1,0 kV a 36,2 kV); deve ser removida ou justificada se o quadro for de media tensao;
- `IEC 61439` esta referenciado informalmente; o correto e `ABNT NBR IEC 60439-1:2003`;
- barreira de acrilico interno contra contato acidental nao consta no descritivo;
- sem criterios de commissioning e testes de isolamento e continuidade;
- sem mencao a PTTA (conjuntos com ensaio de tipo parcialmente testados);
- sem mencao ao layout de placa de montagem (entrada e saida de alimentadores pela face superior).

### 4.5 Item 60 — Autotransformador

Estado: adequado em especificacoes tecnicas principais.

Coberto adequadamente:

- 300 kVA, 220/380 V, IP23, aluminio, 105°C;
- referencia Wise ou similar;
- base antivibrante;
- NBR 5356, NBR 5410, NR-10.

Faltante:

- classe de isolamento 1,1 kV nao consta;
- sem criterios de localizacao (sala eletrica / subestacao);
- sem mencao a comissionamento com medicao de tensao de saida.

### 4.6 Item 61 — SPDA com Captor PDI

Estado: tecnicamente detalhado e adequado.

Coberto adequadamente:

- captor PDI Pevectron 3 S60 ou similar;
- ΔT = 60 μs;
- NF C17-102 e NBR 5419-1;
- hastes copperweld 5/8"×2,4 m (3 por descida);
- descidas em cabo nu 50 mm²;
- solda exotermica;
- caixas de inspeção.

Faltante ou a revisar:

- normas europeias UNE 21-186:2011, NP 4426:2013 nao constam;
- normas IEC 62561 e IEC 62305 nao constam;
- caixa metalica aco inoxidavel 316 e ponta central cobre niquelado nao constam como especificacao do captor;
- barramento de equipotencial principal (BEP) na subestacao e sua integracao a malha de aterramento nao constam;
- criterio de solda exotermica para todas as conexoes cabo-cabo e cabo-haste nao esta suficientemente enfatizado no descritivo;
- medicao de resistencia de aterramento nao e citada como criterio de aceitacao.

### 4.7 Item 62 — Sensores de Presenca e Alarmes PCD

Estado: compacto porem com mistura de dois subtemas distintos (sensores de presenca e alarmes PCD).

Coberto adequadamente:

- sensores de presenca 360° bivolt, alcance Ø 7 m;
- alarmes MINI-CSL ou similar;
- botoeiras de emergencia a 40 cm do piso;
- NBR 9050:2020, NBR 5410, NR-10.

Faltante ou a revisar:

- regulagem de tempo (1 s a 15 min) e recontagem automatica ausentes;
- altura de instalacao do sensor (2,4 m) ausente;
- integracao do alarme vermelho ao sistema de deteccao de incendio ausente;
- mencao a NBR 9050 item 4.6.7 para dimensionamento do botao ausente;
- critério de contraste de cor do botao com a parede ausente;
- dimensao minima do botao (2,5 cm) ausente;
- alarme audiovisual na face externa da porta ausente no descritivo;
- instrucao tecnica CBMERJ referenciada genericamente, sem identificar qual nota tecnica e para qual servico.

Problema de agrupamento: sensor de presenca e alarme PCD tem logica de acionamento, cabeamento e normativa distintos; podem ser dois itens separados no banco.

### 4.8 Item 63 — Tomadas de Piso em Inox

Estado: adequado para o nivel de especificidade do item.

Coberto adequadamente:

- caixa 150×250×60 mm em plastico de engenharia;
- modulos NBR 14136 e suportes RJ45;
- tampa basculante 190×190 mm inox escovado;
- NBR 14136, NBR 5410, NR-10.

Faltante:

- criterio de montagem no piso (recorte, reforco de estrutura, nivel do acabamento) ausente;
- criterio de aterramento da tampa metalica ausente.

### 4.9 Itens Ausentes no Banco (nao cobertos por nenhum item atual)

Os seguintes subtemas tecnicos identificados no Word nao tem representacao no banco:

1. Condutores Terminais — PVC 70°C ATOX: especificacoes detalhadas de secoes, padrão de cores, identificacao por anilhas e etiquetas, encaminhamento justaposto em eletrocalha
2. Condutores Alimentadores — HEPR 90°C antichama: encaminhamento em trifolia, fixacao a cada 1,5 m, identificacao por fita colorida e luva transparente
3. Eletrodutos: diferenciacoes por ambiente (interno leve, externo pesado, entreforro PVC preto), criterios de execucao (arame guia, caps, angulo, bucha e arruela)
4. Eletrocalhas e Leitos: diferenciacoes por ambiente, fixacoes, continuidade de equipotencializacao
5. Perfilados: especificacoes de material e fixacao
6. Dutos PEAD Corrugados Flexiveis no Subterraneo: envelopamento em concreto, profundidades de circuitos
7. Quadros para Cargas Especificas — Gabinetes de Ventilacao e Ventiladores Inline: DPS Classe II, protecao contra falta de fase, chave seletora local/automatico
8. Tomadas e Interruptores Padrao: criterios de instalacao, polarizacao, condutor de terra, condulete metalico para cargas especificas
9. Conectores e Emendas: guilhotina scotchlok, terminais ilhos, vedacao de emendas com fita isolante
10. Medicao / Comissionamento / Testes: testes de continuidade, isolamento e equipotencializacao como criterio de entrega

---

## 5. Proposta De Itens Para Inserir Ou Revisar

### 5.1 Instalacoes Eletricas > Infraestrutura Eletrica

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Infraestrutura Eletrica | Infraestrutura Elétrica de Baixa Tensão — Remoção, Encaminhamento e Nova Instalação | Ampliar descritivo com criterios de execucao, padrão de cores e identificacao de circuitos; adicionar normas de condutos |
| Adicionar | Condutores | Condutores de Cobre para Circuitos Terminais — PVC 70°C 450/750 V ATOX | Item proprio para especificacao de cabos terminais, padrão de cores e identificacao |
| Adicionar | Condutores | Condutores de Cobre para Circuitos Alimentadores — HEPR 90°C 0,6/1 kV Antichama | Item proprio para alimentadores, encaminhamento trifolia e identificacao |
| Adicionar | Condutos | Eletrodutos Metálicos e PVC por Tipo de Ambiente — Critérios de Instalação | Unir criterios de eletroduto rigido aco interno/externo/entreforro e de execucao (arame guia, caps, bucha, angulo) |
| Adicionar | Condutos | Eletrocalhas Perfuradas e Leitos de Cabos — Pré-galvanizados e Galvanizados a Fogo | Item proprio com diferenciacoes por ambiente e criterios de fixacao e equipotencializacao |
| Adicionar | Condutos | Perfilados de Aço-Carbono Pré-galvanizado para Encaminhamento de Circuitos | Item proprio com criterios de fixacao na laje e faceando paredes |
| Adicionar | Condutos | Dutos PEAD Corrugados Flexíveis Subterrâneos com Envelopamento em Concreto | Item proprio para circuitos enterrados, com profundidades e criterios de caixa de passagem |
| Revisar | Quadros Elétricos | Quadros de Distribuição BT PTTA — IP54 RAL 7032 com DPS Classe II | Remover NBR 14039, corrigir IEC 61439, acrescentar PTTA, barreira de acrilico e criterios de comissionamento |
| Adicionar | Quadros Elétricos | Quadros para Cargas Especiais — Ventilacao, Exaustao e Automacao | Item proprio com DPS Classe II, protecao contra falta de fase, chave local/automatico e diagrama funcional |
| Adicionar | Tomadas e Interruptores | Tomadas TUG e Interruptores Embutidos e Aparentes — NBR 14136 | Item proprio para tomadas e interruptores padrao com criterios de instalacao e identificacao |
| Adicionar | Sensores | Sensor de Presença para Teto 360° — Bivolt Temporizado | Item isolado de sensor de presenca (separar do alarme PCD) |
| Revisar | Sensores e Alarmes PCD | Alarmes Visuais e Sonoros PCD — Amarelo (Sinal de Aula) e Vermelho (Incendio) | Melhorar descritivo com integracao ao sistema de incendio e criterios NBR 9050 |
| Adicionar | Conectores e Emendas | Terminação e Emendas de Condutores — Conector Guilhotina, Terminal Ilhós e Proibicoes de Execucao | Item proprio para criterios de execucao de conexoes e emendas |
| Adicionar | Comissionamento | Testes de Continuidade, Isolamento e Equipotencialização — Criterios de Aceitacao | Item proprio de comissionamento eletrico antes da energizacao |

### 5.2 Instalacoes Eletricas > SPDA e Aterramento

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Para-Raios PDI | SPDA com Captores PDI — Método Ionizante, ΔT=60 μs | Acrescentar normas IEC 62561, IEC 62305, UNE 21-186, NP 4426; captor aco inox 316 e ponta cobre niquelado; medicao de resistencia |
| Adicionar | Aterramento | Sistema de Aterramento SPDA — Hastes Copperweld, Cabo Nu 50 mm² e Solda Exotérmica | Separar o aterramento do SPDA como item proprio com criterios tecnicos especificos |
| Adicionar | Aterramento | Barramento de Equipotencial Principal (BEP) e Malha de Aterramento Geral | Item proprio para BEP, integracao de malha e medicao de resistencia de aterramento |

### 5.3 Instalacoes Eletricas Provisorias

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Instalações Elétricas Provisórias | Infraestrutura Elétrica Provisória do Canteiro | Ampliar com eletrodutos provisorios, aterramento provisorio e criterios de desmontagem |
| Revisar | Instalações Elétricas Provisórias | Iluminação Aparente Provisória em Canaleta ou Eletrocalha | Acrescentar interruptores bipolares e protecao por disjuntor |

---

## 6. Normas A Revisar Neste Recorte

### 6.1 Normas pertinentes identificadas e sua distribuicao recomendada

**Item geral de instalacoes eletricas BT (normas-mae):**

- `NR-10` — seguranca em instalacoes e servicos; em todos os itens eletricos
- `ABNT NBR 5410:2004` — instalacoes eletricas de baixa tensao; em todos os itens eletricos
- `ABNT NBR 13570:2021` — locais de afluencia de publico
- `ABNT NBR 13534:2008` — estabelecimentos assistenciais de saude (quando aplicavel)

**Item de subestacao / autotransformador:**

- `ABNT NBR 5356-1:2007` — transformadores de potencia
- `ABNT NBR 14039:2021` — instalacoes de media tensao (1,0 kV a 36,2 kV)

**Item de condutores terminais:**

- `ABNT NBR NM 247-3:2002` — cabos PVC ate 450/750 V
- `ABNT NBR 8661:1997` — cabos planos PVC ate 750 V (PP multipolar)
- `ABNT NBR 9326:2014` — conectores para cabos de potencia
- `ABNT NBR 9513:2010` — emendas ate 750 V
- `ABNT NBR 15701:2016` — conduletes metalicos

**Item de condutores alimentadores:**

- `ABNT NBR 13248:2014` — cabos nao halogenados ate 1 kV
- `ABNT NBR 7286:2022` — cabos EPR/HEPR 1 kV a 35 kV
- `ABNT NBR 7288:2018` — cabos PVC/PE 1 kV a 6 kV
- `ABNT NBR 9326:2014` — conectores
- `ABNT NBR 9513:2010` — emendas

**Item de eletrodutos:**

- `ABNT NBR 13057:2011` — eletroduto aco-carbono zincado eletroliticamente leve
- `ABNT NBR 5624:2011` — eletroduto aco-carbono galvanizado a fogo pesado
- `ABNT NBR 15465:2020` — eletrodutos plasticos BT

**Item de eletrocalhas e leitos:**

- `ABNT NBR IEC 61537:2013` — eletrocalhas e leitos

**Item de perfilados:**

- `ABNT NBR IEC 61084:2022` — canaletas e eletrodutos nao circulares

**Item de quadros de distribuicao:**

- `ABNT NBR IEC 60439-1:2003` — conjuntos PTTA/TTA
- `ABNT NBR IEC 62208:2013` — involucros para conjuntos
- `ABNT NBR IEC 60947-2:2013` — disjuntores BT
- `ABNT NBR NM 60898:2004` — disjuntores residenciais
- `ABNT NBR IEC 60269-1:2003` — dispositivos fusiveis
- `IEC 61009-1:2010` — RCBO
- `ABNT NBR IEC 62423:2020` — dispositivo diferencial tipo B e F
- `IEC 61643-1:2005` — DPS BT

**Item de tomadas e interruptores:**

- `ABNT NBR 14136:2012` — tomadas e plugues domesticos ate 20 A
- `ABNT NBR NM 60884-1:2010` — plugues e tomadas gerais
- `ABNT NBR NM 60669-1:2004` — interruptores fixos
- `ABNT NBR IEC 60309-1:2015` — plugues e tomadas industriais

**Item de alarmes PCD:**

- `ABNT NBR 9050:2020` — acessibilidade (item 4.6.7 especifico para botao de alarme)
- `CBMERJ Nota Tecnica 2-06:2019` — iluminacao de emergencia (quando associado)
- `CBMERJ Nota Tecnica 2-07:2019` — deteccao e alarme de incendio (para integracao)

**Item de SPDA:**

- `ABNT NBR 5419-1:2015` — protecao contra descargas atmosfericas, parte 1: principios gerais
- `NF C 17-102:2011` — SPDA com dispositivo de ionizacao (norma francesa, referencia do fabricante)
- `UNE 21-186:2011` — norma espanhola para SPDA PDI
- `NP 4426:2013` — norma portuguesa para SPDA PDI
- `IEC 62561` — componentes de sistemas de protecao contra descargas atmosfericas
- `IEC 62305` — protecao contra descargas atmosfericas

### 6.2 Inconsistencias de Normas Encontradas no Banco Atual

1. **ID 59 — Quadros de Distribuicao BT:** referencia `ABNT NBR 14039` (media tensao 1,0–36,2 kV). Esta norma nao pertence a um item de quadro de distribuicao de baixa tensao. Deve ser removida ou o item deve ter escopo explicitado como media tensao.

2. **ID 59 — Quadros de Distribuicao BT:** referencia `IEC 61439` como codigo informal. O correto e `ABNT NBR IEC 60439-1:2003`. Verificar se a versao mais recente IEC 61439 supera a NBR 60439-1 e atualizar conforme necessidade.

3. **ID 61 — SPDA:** normas `UNE 21-186`, `NP 4426`, `IEC 62561` e `IEC 62305` estao ausentes mesmo sendo citadas no Word como exigencia do fabricante de referencia. Devem ser acrescentadas ao item.

4. **ID 58 — Infraestrutura BT:** nenhuma norma de cabos (serie NBR NM 247-3, NBR 7286, NBR 7288, NBR 13248) e nenhuma norma de condutos (NBR 13057, NBR 5624, NBR IEC 61537, NBR IEC 61084, NBR 15465) esta presente. O item fica sem sustentacao normativa para os materiais que especifica.

5. **ID 62 — Sensores e Alarmes PCD:** `Instrucao Tecnica CBMERJ` referenciada de forma generica sem identificar a nota tecnica especifica. Deve ser substituida por `CBMERJ Nota Tecnica 2-06:2019` (iluminacao de emergencia) ou `CBMERJ Nota Tecnica 2-07:2019` (alarme de incendio) conforme o subtema.

---

## 7. Decisao Antes De Escrever No JSON

Para a proxima etapa, recomenda-se operar em tres movimentos distintos:

**Movimento 1 — Correcoes de normas nos itens existentes (seguras, sem mudanca estrutural):**

- ID 59: remover `ABNT NBR 14039`; substituir `IEC 61439` por `ABNT NBR IEC 60439-1:2003`; adicionar `ABNT NBR IEC 62208:2013`
- ID 61: acrescentar `UNE 21-186:2011`, `NP 4426:2013`, `IEC 62561`, `IEC 62305`
- ID 62: substituir `Instrucao Tecnica CBMERJ` por notas tecnicas especificas

**Movimento 2 — Revisao de descritivos e materiais nos itens existentes:**

- ID 58: ampliar descritivo com padrão de cores de condutores, criterios de identificacao (anilhas, etiquetas 380 V), criterios de execucao de eletrodutos (arame guia, caps, angulo), continuidade de equipotencializacao em eletrocalhas; adicionar normas de cabos e condutos
- ID 59: acrescentar barreira de acrilico, PTTA, layout de placa de montagem e criterios de comissionamento
- ID 60: acrescentar classe de isolamento 1,1 kV e criterio de comissionamento
- ID 62: separar em dois itens (sensor de presenca e alarme PCD)
- ID 63: acrescentar criterio de aterramento da tampa metalica

**Movimento 3 — Adicao de novos itens:**

Novos IDs propostos (proximos numericos apos o maior ID atual):

1. Condutores de Cobre para Circuitos Terminais — PVC 70°C 450/750 V ATOX
2. Condutores de Cobre para Circuitos Alimentadores — HEPR 90°C 0,6/1 kV Antichama
3. Eletrodutos Metálicos e PVC por Tipo de Ambiente — Criterios de Instalacao
4. Eletrocalhas Perfuradas e Leitos de Cabos — Pre-galvanizados e Galvanizados a Fogo
5. Perfilados de Aco-Carbono Pre-galvanizado para Encaminhamento de Circuitos
6. Dutos PEAD Corrugados Flexiveis Subterraneos com Envelopamento em Concreto
7. Quadros para Cargas Especiais — Ventilacao, Exaustao e Automacao
8. Tomadas TUG e Interruptores Embutidos e Aparentes — NBR 14136
9. Sensor de Presenca para Teto 360° — Bivolt Temporizado
10. Sistema de Aterramento SPDA — Hastes Copperweld, Cabo Nu 50 mm² e Solda Exotermica
11. Barramento de Equipotencial Principal (BEP) e Malha de Aterramento Geral
12. Terminacao e Emendas de Condutores — Conector Guilhotina, Terminal Ilhos e Criterios de Execucao
13. Testes de Continuidade, Isolamento e Equipotencializacao — Criterios de Aceitacao

**Observacao sobre o autotransformador (ID 60):**

O item existente tem especificacoes fortemente vinculadas ao projeto especifico (300 kVA, 220/380 V para condensadoras de ar-condicionado). Para banco reutilizavel, o item pode ser mantido com as especificacoes tecnicas como exemplo de projeto, mas o descritivo deve deixar claro que potencia e tensoes variam conforme dimensionamento. Nao deve ser alterado estruturalmente nesta etapa.

**Sequencia recomendada:**

1. Aplicar correcoes de normas (Movimento 1) — sem risco de perda de conteudo;
2. Revisar descritivos e materiais (Movimento 2) — expandindo sem apagar o existente;
3. Adicionar novos itens em IDs sequenciais (Movimento 3) — somente apos revisao dos itens existentes para evitar duplicidade.
