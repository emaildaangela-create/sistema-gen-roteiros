# Auditoria Capitulo 10 - Recorte 01

Fonte analisada: `data/Referencias de banco de dados/SS-NIG-ESCOLASESI-EX-ORC-DOC-001-R02.docx`

Texto extraido para consulta: `data/Referencias de banco de dados/roteiro_tecnico_extraido.txt`

Recorte analisado nesta etapa:

- `SERVICOS A EXECUTAR`
- `SERVICOS PRELIMINARES`
- `MOVIMENTO DE TERRA`
- `INSTALACOES PROVISORIAS`
- Inicio de `Instalacoes Eletricas Provisorias`

## 1. Criterio De Curadoria

O roteiro tecnico deve ser usado como fonte de tecnicas, requisitos, servicos, materiais e normas. Nao deve ser transcrito como memorial especifico do projeto.

Devem ser mantidos:

- metodos executivos genericos;
- requisitos de qualidade;
- criterios de seguranca;
- materiais-tipo;
- normas tecnicas e regulamentadoras aplicaveis;
- atividades auxiliares necessarias para execucao do servico.

Devem ser removidos ou generalizados:

- nome da unidade ou escola;
- referencias a ambientes especificos, como ginasio e sala multiuso;
- quantitativos especificos;
- horarios, logistica ou restricoes exclusivas daquele projeto;
- cores, modelos ou padroes que tenham sido definidos apenas para aquele projeto;
- referencias contratuais como CONTRATANTE, CONTRATADA, certame, planilha orcamentaria e fiscalizacao, salvo quando convertidas para redacao generica.

## 2. Estrutura Fonte Identificada No Word

### 2.1 Orientacoes Gerais

Linhas aproximadas: 460 a 468.

Conteudo tecnico aproveitavel:

- seguir normas tecnicas brasileiras;
- executar servicos conforme metodologias construtivas e preparos de superficie;
- incluir servicos secundarios necessarios;
- fornecer materiais, equipamentos, mao de obra, alugueis, retiradas, instalacoes provisorias e logistica;
- admitir similaridade tecnica apenas se comprovada;
- atualizar memorial/manual ao termino da obra.

Uso recomendado no banco:

- nao criar item isolado de servico;
- aproveitar como criterio geral de redacao e validacao dos itens.

### 2.2 Servicos Preliminares

Linhas aproximadas: 469 a 522.

Subtemas identificados:

- servicos de escritorio, laboratorio e campo;
- instalacao, manutencao, conservacao e operacao do canteiro;
- tapume estruturado e isolamento fisico;
- limpeza, vigilancia e protecao contra terceiros;
- protecao de elementos e estruturas existentes;
- administracao local;
- placas de obra;
- locacao da obra e execucao de gabarito;
- andaimes tubulares, passarelas e equipamentos de acesso;
- guindastes, icamentos e levantamento de cargas;
- transportes vertical e horizontal.

### 2.3 Movimento De Terra

Linhas aproximadas: 523 a 539.

Subtemas identificados:

- limpeza do terreno;
- retirada e destinacao de residuos;
- escavacoes para fundacoes, blocos, cintas, valas e interferencias;
- escoramento e esgotamento;
- reaterros e aterros com material selecionado;
- remocao de material excedente;
- compactacao mecanica e conformacao de plataformas.

### 2.4 Instalacoes Provisorias

Linhas aproximadas: 540 a 571.

Subtemas identificados:

- salas provisorias;
- divisorias em drywall;
- vao para portas e passagem de instalacoes;
- reforcos metalicos;
- tratamento de juntas;
- pintura;
- reaproveitamento/reinstalacao de portas;
- forro em EPS/isopor;
- iluminacao aparente;
- isolamento da area por tapume;
- desmontagem e recomposicao ao final.

### 2.5 Instalacoes Eletricas Provisorias

Linhas aproximadas: 572 a 620 neste recorte, continuando depois.

Subtemas identificados:

- cabos para pontos de forca, tomadas, iluminacao e equipamentos;
- eletrodutos, eletrocalhas e acessorios;
- quadro eletrico de distribuicao provisoria;
- detalhamento de componentes necessarios;
- lista normativa extensa.

Observacao:

Este bloco pertence melhor a disciplina `Instalacoes Eletricas`, categoria `Instalacoes Provisorias`, nao a `Obras Civis`.

## 3. Estado Atual Do Banco

Arquivo analisado: `data/memorial_servicos.json`

Itens atualmente relacionados ao recorte:

| ID | Disciplina | Categoria | Subcategoria | Item atual |
|---:|---|---|---|---|
| 1 | Obras Civis | Servicos Preliminares | Canteiro de Obra | Administracao Local do Canteiro de Obras |
| 2 | Obras Civis | Servicos Preliminares | Canteiro de Obra | Fornecimento e Instalacao de Placa de Obra |
| 3 | Obras Civis | Servicos Preliminares | Canteiro de Obra | Locacao e Nivelamento da Obra |
| 4 | Obras Civis | Servicos Preliminares | Equipamentos de Obra | Andaimes Fachadeiros e Equipamentos de Acesso em Altura |
| 5 | Obras Civis | Movimento de Terra | Terraplenagem | Limpeza e Preparo do Terreno |
| 6 | Obras Civis | Movimento de Terra | Terraplenagem | Escavacao Manual e Mecanizada |
| 7 | Obras Civis | Movimento de Terra | Terraplenagem | Reaterro e Aterro Compactado |
| 8 | Obras Civis | Instalacoes Provisorias | Salas Provisorias | Salas Provisorias em Drywall |
| 9 | Instalacoes Eletricas | Instalacoes Provisorias | Instalacoes Eletricas Provisorias | Infraestrutura Eletrica Provisoria do Canteiro |
| 10 | Logica e Telefonia | Instalacoes Provisorias | Instalacoes Especiais Provisorias | Infraestrutura de Dados Provisoria do Canteiro |

## 4. Diagnostico Tecnico

### 4.1 Servicos Preliminares

O banco atual cobre parcialmente o bloco.

Coberto:

- administracao local;
- placa de obra;
- locacao e nivelamento;
- andaimes/equipamentos de acesso.

Faltante ou excessivamente agrupado:

- instalacao, manutencao e desmobilizacao do canteiro;
- tapume e isolamento fisico;
- limpeza, vigilancia e protecao contra terceiros;
- protecao de elementos/estruturas existentes;
- guindastes, icamentos e levantamento de cargas;
- transportes vertical e horizontal.

Problema de itemizacao:

- `Administracao Local do Canteiro de Obras` mistura equipe tecnica, gestao documental, diario de obra, controle de qualidade e obrigacoes de comunicacao.
- `Andaimes Fachadeiros e Equipamentos de Acesso em Altura` nao cobre bem passarelas, plataformas e equipamentos de acesso em geral.

### 4.2 Movimento De Terra

O banco atual cobre o nucleo, mas ainda esta compacto.

Coberto:

- limpeza/preparo do terreno;
- escavacao;
- reaterro/aterro.

Faltante ou recomendavel separar:

- escoramento e esgotamento de cavas/valas;
- escavacao de valas para instalacoes;
- remocao, carga, transporte e destinacao de material excedente;
- compactacao mecanica e regularizacao de plataformas.

Problema encontrado:

- `Escavacao Manual e Mecanizada` recebeu `ABNT NBR 16401` por regra automatica indevida. Essa norma e de ar-condicionado e deve ser removida desse item.

### 4.3 Instalacoes Provisorias

O banco atual possui apenas um item para salas provisorias em drywall, mas o Word descreve varias frentes tecnicamente distintas.

Faltante ou recomendavel separar:

- divisorias provisorias em drywall;
- reforcos para vaos, portas e passagem de instalacoes;
- reaproveitamento/reinstalacao de portas;
- forro provisorio em EPS;
- iluminacao aparente provisoria;
- isolamento de area operacional por tapume;
- desmontagem de instalacoes provisorias e recomposicao.

Exemplo de melhoria de granularidade:

Em vez de apenas `Salas Provisorias em Drywall`, o banco deve ter itens reutilizaveis por situacao, como:

- `Divisorias Provisorias em Drywall ST`;
- `Parede de Drywall com Reforco para Vaos e Instalacoes`;
- `Reinstalacao de Portas Reaproveitadas`;
- `Forro Provisorio em Painel EPS`;
- `Iluminacao Aparente Provisoria em Canaleta ou Eletrocalha`;
- `Desmontagem de Instalacoes Provisorias e Recomposicao`.

### 4.4 Instalacoes Eletricas Provisorias

O banco atual possui item resumido.

O Word traz lista normativa longa. Nem toda norma deve ir automaticamente para o item principal; algumas devem ficar em itens especificos.

Exemplo de separacao recomendada:

- `Infraestrutura Eletrica Provisoria de Canteiro`;
- `Quadro de Distribuicao Provisorio`;
- `Circuitos Provisorios de Iluminacao`;
- `Circuitos Provisorios de Tomadas e Pontos de Forca`;
- `Eletrodutos, Eletrocalhas e Canaletas Provisorias`;
- `Testes e Comissionamento de Instalacao Eletrica Provisoria`.

## 5. Proposta De Itens Para Inserir Ou Revisar

### 5.1 Obras Civis > Servicos Preliminares

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Administracao Local | Administracao Local e Gestao Tecnica da Obra | Separar gestao tecnica de canteiro fisico. |
| Adicionar | Canteiro de Obra | Mobilizacao, Manutencao e Desmobilizacao do Canteiro | O Word descreve instalacao, conservacao e entrega limpa do canteiro. |
| Adicionar | Isolamento e Protecao | Tapume e Isolamento Fisico de Obra | Item tecnico proprio, com materiais e criterios de seguranca. |
| Adicionar | Isolamento e Protecao | Protecao de Elementos e Estruturas Existentes | Necessario para obras em edificacoes existentes. |
| Adicionar | Canteiro de Obra | Limpeza, Vigilancia e Guarda de Materiais no Canteiro | Hoje esta diluido no texto, mas e item recorrente. |
| Revisar | Placas de Obra | Placas de Obra e Identificacao Tecnica | Generalizar sem quantidade fixa. |
| Revisar | Locacao da Obra | Locacao Topografica, Nivelamento e Gabarito | Acrescentar marcos, cotas, eixos e controle. |
| Revisar | Equipamentos de Obra | Andaimes Tubulares, Passarelas e Plataformas de Trabalho | Ampliar alem de fachadeiro. |
| Adicionar | Equipamentos de Obra | Guindastes, Icamentos e Levantamento de Cargas | O Word tem bloco proprio. |
| Adicionar | Logistica de Obra | Transporte Vertical e Horizontal de Materiais, Equipamentos e Residuos | O Word tem bloco proprio. |

### 5.2 Obras Civis > Movimento de Terra

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Limpeza do Terreno | Limpeza, Preparo do Terreno e Remocao Inicial de Interferencias | Generalizar a limpeza externa. |
| Revisar | Escavacoes | Escavacao Manual e Mecanizada para Fundacoes e Valas | Tornar mais especifico. |
| Adicionar | Escavacoes | Escoramento e Esgotamento de Cavas e Valas | Condicao tecnica propria citada no Word. |
| Adicionar | Escavacoes | Escavacao de Valas para Instalacoes Enterradas | Diferente de escavacao de fundacao. |
| Revisar | Reaterros e Aterros | Reaterro e Aterro Compactado com Material Selecionado | Manter, mas melhorar criterios. |
| Adicionar | Terraplenagem | Remocao, Carga e Transporte de Material Excedente | Citado no Word e recorrente em obras. |
| Adicionar | Terraplenagem | Regularizacao e Compactacao de Plataformas | Item tecnico proprio. |

### 5.3 Obras Civis > Instalacoes Provisorias

| Acao | Subcategoria | Item proposto | Motivo |
|---|---|---|---|
| Revisar | Salas Provisorias | Salas Provisorias para Operacao Temporaria Durante Obra | Generalizar sem citar ambientes do projeto. |
| Adicionar | Divisorias Provisorias | Divisorias Provisorias em Drywall ST | Separar do conjunto sala. |
| Adicionar | Divisorias Provisorias | Reforcos em Drywall para Vaos, Portas e Passagem de Instalacoes | Situacao tecnica especifica. |
| Adicionar | Esquadrias Provisorias | Reaproveitamento, Reinstalacao e Ajuste de Portas | O Word descreve este servico. |
| Adicionar | Forros Provisorios | Forro Provisorio em Painel EPS | Item proprio. |
| Adicionar | Instalacoes Eletricas Provisorias | Iluminacao Aparente Provisoria em Canaleta ou Eletrocalha | Pode ficar em eletrica, mas precisa existir. |
| Adicionar | Desmobilizacao | Desmontagem de Instalacoes Provisorias e Recomposicao de Areas | O Word fecha o ciclo do servico. |

## 6. Normas A Revisar Neste Recorte

### 6.1 Normas pertinentes ja identificadas

Servicos preliminares e canteiro:

- `NR-18` - seguranca e saude no trabalho na industria da construcao;
- `NR-35` - trabalho em altura, quando houver andaimes/acesso;
- `NR-11` - transporte, movimentacao e manuseio de materiais, quando houver icamento/cargas;
- `NBR 6494` - seguranca nos andaimes;
- `CONAMA Resolucao 307/2002` - residuos da construcao civil;
- `Resolucao CONFEA 198/1971` - placa de obra.

Movimento de terra:

- `NBR 6122` - fundacoes, quando ligado a escavacoes de fundacao;
- `NBR 6457` - preparacao de amostras de solo;
- `NBR 7182` - ensaio de compactacao;
- `NR-18` - seguranca em escavacoes e obras;
- legislacao ambiental para destinacao de residuos/solo.

Instalacoes provisorias civis:

- `ABNT NBR 15758` - drywall;
- `ABNT NBR 14715` - chapas de gesso para drywall;
- `NR-18` - canteiro e condicoes de seguranca.

Instalacoes eletricas provisorias:

- `NR-10`;
- `ABNT NBR 5410`;
- `ABNT NBR 13570`, quando aplicavel a locais de afluencia de publico;
- `ABNT NBR 13534`, quando aplicavel a estabelecimentos assistenciais de saude;
- `ABNT NBR 5419-1`, quando houver SPDA/protecao contra descargas;
- `ABNT NBR 14039`, apenas para media tensao;
- normas de cabos, quadros e eletrodutos devem ser distribuidas para itens especificos, nao jogadas todas no item principal.

### 6.2 Inconsistencias encontradas

- Remover `ABNT NBR 16401` do item `Escavacao Manual e Mecanizada`; ela e de ar-condicionado e nao pertence a movimento de terra.
- Avaliar se `NR-18` e `NR-35` devem estar em todos os itens de canteiro ou apenas nos itens com risco correspondente.
- Avaliar se `ABNT NBR 15575` deve ser usada no banco. Ela nao aparece neste recorte e e norma de desempenho habitacional, podendo nao ser adequada para todos os servicos.

## 7. Decisao Antes De Escrever No JSON

Para a proxima etapa, recomenda-se atualizar o banco em dois movimentos separados:

1. Corrigir itens existentes e normas claramente inconsistentes.
2. Adicionar novos itens candidatos deste recorte.

Essa separacao evita misturar correcao estrutural com expansao do banco.

Proxima acao sugerida:

- aplicar no JSON apenas as revisoes seguras dos itens existentes IDs 1 a 10;
- depois adicionar os novos itens de `Servicos Preliminares`, `Movimento de Terra` e `Instalacoes Provisorias` com novos IDs.
