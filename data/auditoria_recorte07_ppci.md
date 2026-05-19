# Auditoria Capitulo 10 - Recorte 07

Fonte analisada: `data/Referencias de banco de dados/SS-NIG-ESCOLASESI-EX-ORC-DOC-001-R02.docx`

Texto extraido para consulta: `data/Referencias de banco de dados/roteiro_tecnico_extraido.txt`

Recorte analisado nesta etapa:

- `QUALIFICACAO TECNICA EXIGIDA` (linhas aprox. 3891-3894)
- `NORMAS APLICAVEIS` (linhas aprox. 3895-3912)
- `EXTINTORES` (linhas aprox. 3913-3947)
- `SINALIZACAO DE EMERGENCIA` (linhas aprox. 3948-4047)
- `ILUMINACAO DE EMERGENCIA` (linhas aprox. 4048-4346)
- `CANALIZACAO PREVENTIVA` (linhas aprox. 4347-4429)
- `SISTEMA DE ALARME DE INCENDIO` (linhas aprox. 4430-4477)
- `ESPECIFICACAO TECNICA – ALARME` (linhas aprox. 4478-4560)
- `ACIONADOR MANUAL ENDERECAVEL` (linhas aprox. 4509-4530)
- `ALARME AUDIO VISUAL` (linhas aprox. 4531-4560)
- `PLANO DE EMERGENCIA` (linhas aprox. 4561-4566)
- `HIDRANTE URBANO` (linhas aprox. 4567-4574) — acao burocrática, sem conteudo tecnico de banco

## 1. Criterio De Curadoria

O roteiro tecnico deve ser usado como fonte de tecnicas, requisitos, servicos, materiais e normas. Nao deve ser transcrito como memorial especifico do projeto.

Devem ser mantidos:

- metodos executivos genericos de PPCI;
- requisitos de qualidade e criterios de desempenho (pressao, vazao, autonomia, iluminancia);
- criterios de seguranca e protecao contra incendio;
- materiais-tipo com especificacoes tecnicas reprodutiveis;
- normas tecnicas ABNT e instrucoes tecnicas do corpo de bombeiros local aplicaveis;
- atividades auxiliares necessarias para instalacao dos sistemas.

Devem ser removidos ou generalizados:

- nome da unidade, escola ou cliente;
- referencias a ambientes especificos como ginasio, vestiarios, secretaria escolar, cozinha;
- quantitativos absolutos especificos do projeto (numero de unidades, comprimentos totais, area total);
- referencias contratuais como CONTRATADA, CONTRATANTE, FISCALIZACAO, certame, planilha orcamentaria;
- restricoes de aproveitamento de materiais existentes ligadas a condicoes especificas de projeto;
- localizacoes geograficas especificas que nao sejam de norma tecnica.

Sobre o CBMERJ especificamente:

- Referencias tecnicas ao CBMERJ devem ser mantidas nas `normas_de_referencia` como `Instrucao Tecnica CBMERJ` ou `Normas Tecnicas do Corpo de Bombeiros local`, com nota `(verificar equivalente estadual)`;
- Os numeros do Decreto 42/2018 e das Notas Tecnicas (NT 2-05, NT 2-06, NT 2-10, NT 2-20) sao do Rio de Janeiro e devem ser listados com a nota `(verificar equivalente estadual)`;
- Nao citar o nome CBMERJ junto a unidade especifica, apenas como referencia normativa generica.

## 2. Estrutura Fonte Identificada No Word

### 2.1 Qualificacao Tecnica Exigida

Linhas aproximadas: 3891 a 3894.

Conteudo tecnico:

- exigencia de atestado de capacidade tecnica em execucao de PPCI;
- area minima de experiencia: 4.500 m² em sistema completo.

Uso recomendado no banco:

- nao criar item isolado de servico para habilitacao;
- aproveitar como criterio de qualificacao do executante no descritivo dos itens de PPCI.

### 2.2 Normas Aplicaveis

Linhas aproximadas: 3895 a 3912.

Normas identificadas no bloco:

- Decreto 42/2018 (CBMERJ) e Notas Tecnicas – Codigo de Seguranca Contra Incendio e Panico;
- ABNT NBR 13434 – Sinalizacao de seguranca contra incendio e panico;
- ABNT NBR 13714 – Sistema de hidrantes e mangotinhos;
- ABNT NBR 17240 – Sistemas de alarme de incendio;
- ABNT NBR 10898 – Sistema de iluminacao de emergencia;
- ABNT NBR 12693 – Sistemas de protecao por extintores.

Uso recomendado no banco:

- essas normas devem estar distribuidas pelos itens especificos de cada subsistema;
- nao criar item de normas generais como entrada propria no banco.

### 2.3 Extintores

Linhas aproximadas: 3913 a 3947.

Subtemas tecnicos identificados:

- **Extintor tipo AP (Agua Pressurizada):** uso em areas de circulacao;
- **Extintor tipo CO2:** uso em areas com equipamentos eletricos;
- **Extintor tipo PQS (Po Quimico Seco):** uso em subestacao e central de GLP;
- Criterio de dimensionamento: area maxima de 150 m² por unidade extintora (risco medio), distancia maxima de 15 m ate o operador;
- Altura de instalacao: maximo 1,60 m do piso acabado;
- Lacre e selo de conformidade ABNT exigidos;
- Instalacao em locais de menor probabilidade de fogo, visiveis e desobstruidos.

Conteudo a ser excluido por ser especifico do projeto:

- "posicionados nas areas de circulacao" (referencia a ambientes);
- instrucoes de relocalizacao de extintores existentes para novas posicoes de projeto;
- referencias a ART/CREA/credenciamento junto ao CBMERJ por serem obrigacoes contratuais e nao tecnicas de banco.

### 2.4 Sinalizacao de Emergencia

Linhas aproximadas: 3948 a 4047.

Subtemas tecnicos identificados:

- **Classificacao da sinalizacao:** proibicao, alerta, orientacao, equipamentos e complementar;
- **Implantacao por tipo:**
  - Proibicao e alerta: no minimo a 1,80 m do piso, distanciadas no maximo 15 m entre si;
  - Orientacao em portas: imediatamente acima, no maximo 10 cm da verga, ou na folha a 1,80 m do piso;
  - Orientacao em rotas: distancia maxima de percurso de 7,5 m, base a no minimo 1,80 m do piso;
  - Identificacao de pavimento em escada: 1,80 m do piso acabado;
  - Identificacao de pavimento em antecamaras: 1,50 m do piso acabado;
  - Indicacao continuada de rotas: entre a sinalizacao basica, a no maximo 60 cm do piso;
  - Obstaculos: faixas amarelas e pretas a 45° do piso ate 1 m de altura;
  - Sinalizacao de equipamentos: no minimo 1,80 m do piso acabado.
- **Material das placas:** PVC expandido (nao reciclado), 3 mm de espessura, impressao em serigrafia (silk-screen), suportabilidade a intemperies;
- **Garantia minima:** 36 meses a partir do recebimento;
- **Dimensionamento:** placas dimensionadas para visualizacao a 6 m de distancia.

Conteudo a ser excluido por ser especifico do projeto:

- obrigacao de retirar e entregar sinalização existente a FISCALIZACAO;
- obrigacao de aprovacao previa das placas pela FISCALIZACAO;
- referencia a prazo de garantia como obrigacao contratual em vez de requisito tecnico do material;
- referencia ao Senai como destinatario da garantia.

### 2.5 Iluminacao de Emergencia

Linhas aproximadas: 4048 a 4346.

Subtemas tecnicos identificados:

- **Tipo de equipamento:** blocos autonomos (aparelhos de iluminacao de emergencia em unico involucro);
- **Funcao:** garantir nivel minimo de iluminancia em rotas de saida na falta de energia da concessionaria;
- **Niveis minimos de iluminancia:** 5 lux em locais com desnivel (escadas, passagens com obstaculos); 3 lux em locais planos (corredores, halls, areas de refugio);
- **Autonomia:** minimo de 2 (duas) horas de funcionamento com perda menor que 10% da luminosidade inicial (conforme Decreto 35.671);
- **Tempo de comutacao:** maximo de 12 segundos entre interrupcao da rede e funcionamento pleno;
- **Fluxo luminoso nominal:** medido apos 2 minutos de funcionamento;
- **Fluxo luminoso residual:** medido apos o tempo de autonomia garantido pelo fabricante;
- **Ofuscamento:** variacao de intensidade nao superior a 20:1; limites por altura de ponto de luz (Tabela 1 da NBR 10898);
- **Grau de protecao do involucro:** minimo IP23 ou IP40 conforme NBR 6146;
- **Material:** deve impedir propagacao de chama; gases toxicos em combustao nao podem ultrapassar 1% da carga combustivel do ambiente; partes metalicas protegidas contra corrosao;
- **Fixacao:** rigida, impedindo queda acidental, sem remocao sem ferramenta;
- **Instalacao:** em eletroduto flexivel aparente, fixado em alvenaria;
- **Manutenção – primeiro nivel:** verificacao de lampadas, fusíveis ou disjuntores, nivel de eletrolito, data de fabricacao e inicio de garantia das baterias;
- **Manutencao – segundo nivel:** reparos e substituicoes de componentes; responsabilidade do tecnico especializado;
- **Prazo de registro de defeitos:** anotacao no caderno de controle e reparo em ate 24 horas;
- **Adaptacao apos reformas:** iluminacao deve ser adaptada em no maximo dois meses apos conclusao de alteracoes nas areas iluminadas;
- **Dados necessarios para projeto:** tipo de lampada, potencia, tensao, fluxo luminoso nominal, angulo de dispersao, vida util.

Conteudo a ser excluido:

- instrucoes de retirada e entrega de luminárias existentes à FISCALIZACAO;
- referencias a circuitos de projeto executivo especifico;
- referencias a ART/CREA/credenciamento contratual.

Observacao importante sobre tecnologia:

O Word menciona apenas blocos autonomos. O banco nao possui item separado para sistemas centralizados de iluminacao de emergencia (central + circuitos). Essa segunda tecnologia e reconhecida pela NBR 10898 e deve ser considerada como item adicional ao banco.

### 2.6 Canalizacao Preventiva

Linhas aproximadas: 4347 a 4429.

Subtemas tecnicos identificados:

- **Tubulacao:** ferro galvanizado (FG) diametro 65 mm, resistencia minima 180 kgf/cm², saindo da Casa de Maquinas de Incendio;
- **Conexoes, registros e valvulas:** resistencia igual ou superior a exigida para os tubos, tipo apropriado;
- **Pintura:** tinta esmalte sintetico vermelho (referencia cromatica compativel com Ypiranga n. 217 ou similar); tubulacoes subterraneas com betume;
- **Tubulacao subterranea:** instalada a 30 cm de profundidade;
- **Fixacao aparente:** bracadeiras economicas com vergalhao rosqueado 3/8" galvanizadas, chumbador CB 3/8", espacamento medio de 3,00 m;
- **Fixacao vertical:** cantoneiras em forma de grampos tipo U;
- **Bombeamento:** 2 eletrobombas (principal + reserva), 44,50 mca, 12 m³/h;
- **Sistema de pressurização constante:** manômetro, pressostato e tanque hidropneumatico 12 L com acionamento automatico;
- **Ligacao eletrica independente** da rede geral da edificacao;
- **Registros:** tipo gaveta ou globo em bronze ou latao;
- **Condutores eletricos:** cobre eletrolítico, isolamento PIRASTIC ou similar, 600 V;
- **Eletrodutos:** PVC rigido ou ferro preto esmaltado, estrutura uniforme, sem costura;
- **Alarme de acionamento da bomba:** campainha sincrona de 9", 220 ou 110 V, na portaria;
- **Instalacao eletrica:** conforme NR 5410 da ABNT.

Conteudo a ser excluido:

- instrucoes de reaproveitamento ou descarte de tubulacoes existentes mediante aprovacao de FISCALIZACAO;
- referencias a canaleta de projeto de ARQUITETURA especifico;
- referencias a ART/CREA/credenciamento contratual.

### 2.7 Hidrantes Internos (Caixas de Incendio)

Linhas aproximadas: 4369 a 4408.

Subtemas tecnicos identificados:

- **Caixa de incendio:** 75 x 45 x 17 cm com vidro, hidrante simples;
- **Registro:** tipo globo angular 2½" x 45°;
- **Mangueiras:** 2 lances de 15 m cada, 1½" de diametro, tipo II, fibra resistente a umidade com revestimento interno de borracha vulcanizada; pressao de teste de 20 kgf/cm²; juntas tipo STORZ;
- **Esguichos:** jato regulavel 1½";
- **Adaptador:** 2½" x 2½" com junta STORZ;
- **Chave Storz:** 2½";
- **Boca de expulsao:** a 1,20 m do piso acabado;
- **Alcance maximo de mangueira:** 30 m de percurso do hidrante ao ponto mais desfavoravel;
- **Limite por abrigo:** maximo 2 secoes de mangueira por abrigo;
- **Secagem de mangueiras:** secagem na posicao vertical esticada; nunca enrolar ou guardar umidas.

### 2.8 Hidrante de Recalque (Registro de Passeio ou Fachada)

Linhas aproximadas: 4410 a 4429.

Subtemas tecnicos identificados:

- **Caixa:** ferro fundido 40 x 30 cm, com inscricao "INCENDIO" na tampa;
- **Registro:** tipo globo angular 2½" x 45°;
- **Adaptador:** 2½" x 2½" com junta STORZ;
- **Tampao cego com corrente:** diametro 2½";
- **Profundidade:** caixa com 40 cm de profundidade;
- **Rebordo:** nao abaixo de 15 cm do nivel do solo;
- **Fundo:** nao concretado para drenagem de aguas pluviais;
- **Posicao:** frente da edificacao, interligado a canalizacao de incendio.

### 2.9 Sistema de Alarme de Incendio

Linhas aproximadas: 4430 a 4560.

Subtemas tecnicos identificados:

- **Central de alarme:** Classe B, 2 lacos; tipo convencional com sinalizacao individual por acionador/sirene;
- **Acionadores manuais:** distribuidos nos acessos e circulacoes principais; distancia maxima de 30 m de percurso;
- **Sirenes audiovisuais:** distribuidas nas circulacoes principais;
- **Registro de final de linha:** instalado ao final de cada laco;
- **Tecnologia dos dispositivos:** microprocessador, auto-diagnostico on-line, pré-alarme, auto-calibracao, LED bicolor de status no corpo do dispositivo, imunidade a ruidos, operacao em modo degradado por falha da central;
- **Protocolo:** aberto;
- **Acionador manual endereçavel:** caixa PVC auto-extinguivel na cor vermelha; LED bicolor (verde = interrogacao, vermelho = alarme); tipo quebra-vidro ou aperta-botao; uso interno em ambientes nao corrosivos;
- **Sirene audiovisual:** pressao sonora 100 dB (a 1 m); sinalizacao visual por 20 LEDs de alto brilho; frequencia de flash 100 por minuto; suporte em ABS vermelho; lente em acrilico; tensao 12/24 Vcc;
- **Cabos de cobre:** flexivel isolado PP 1,5 mm² anti-chama 0,6/1,0 kV para sirenes; PP 1,0 mm² anti-chama para acionadores.

Conteudo a ser excluido:

- localizacao especifica da central (Secretaria Escolar);
- referencias a ART/CREA/credenciamento contratual;
- instrucoes a CONTRATADA sobre projeto executivo.

### 2.10 Controle de Materiais de Acabamento e Plano de Emergencia

Linhas aproximadas: 4554 a 4566.

Conteudo tecnico aproveitavel:

- verificacao de materiais de acabamento conforme NT 2-20 (verificar equivalente estadual) e projeto legal aprovado;
- elaboracao de Plano de Emergencia conforme NT 2-10 (verificar equivalente estadual), sob responsabilidade tecnica com ART.

Uso recomendado no banco:

- podem ser criados como itens de servico "Plano de Emergencia" e "Laudo de Materiais de Acabamento" dentro da disciplina PPCI.

### 2.11 LGE e Sistema Fixo de CO2

Linhas aproximadas: 4276 a 4346.

Esses blocos aparecem dentro da secao de Canalizacao Preventiva/Pressurização no Word, mas constituem subsistemas tecnicamente distintos:

- **LGE AFFF:** concentracao 6%, compativel com equipamentos de combate existentes; carreta portatil em aco inox ou polietileno de alta resistencia; testes de comissionamento; FISPQ exigida;
- **Sistema fixo CO2 para dutos de cozinha:** cilindros aco Mannesmann SAE-1541 ou similar, detectores de temperatura fusivel 144°C, dampers corta-fogo, quadro de intertravamento, botoeira de acionamento manual, acionamento automatico por sensor termico; inundacao total por no minimo 60 segundos; tubulacao SCH40 ASTM A53 classe 300 psi.

## 3. Estado Atual Do Banco

Arquivo analisado: `data/memorial_servicos.json`

Itens atualmente com `disciplina` = "PPCI":

| ID | Subcategoria | Item atual |
|---:|---|---|
| 82 | Extintores | Extintores de Incendio – AP, CO2 e PQS |
| 83 | Sinalizacao de Emergencia | Sinalizacao de Emergencia em PVC Expandido 3 mm – Serigrafia – Garantia 36 meses |
| 84 | Iluminacao de Emergencia | Iluminacao de Emergencia – Blocos Autonomos IP23, 2h |
| 85 | Sistema de Pressurizacao | Sistema de Pressurizacao de Escada – 2 Eletrobombas 44,5 mca / 12 m³/h |
| 86 | LGE | LGE AFFF 6% e Carreta Proporcionadora |
| 87 | Sistema de CO2 | Sistema Fixo de Extincao por CO2 – Dutos de Cozinha |
| 88 | Canalizacao Preventiva | Canalizacao Preventiva em Ferro Galvanizado Ø 65 mm – 180 kgf/cm² |
| 89 | Hidrantes Internos | Hidrantes Internos – Caixas 75×45×17 cm com Mangueiras Tipo II |
| 90 | Hidrante de Recalque | Hidrante de Recalque – Registro de Passeio / Fachada |
| 91 | Sistema de Alarme | Sistema de Alarme de Incendio – Central 2 Lacos Classe B |

Total: 10 itens atualmente no banco para a disciplina PPCI.

## 4. Diagnostico Tecnico

### 4.1 Extintores (ID 82)

O banco possui um unico item que agrupa AP, CO2 e PQS.

Coberto:

- tipos AP, CO2 e PQS com usos distintos por ambiente-tipo;
- criterio de dimensionamento 150 m² / 15 m;
- mencao a INMETRO (selo de conformidade).

Problemas encontrados:

- O descritivo menciona "INMETRO" mas a norma de fabricacao e de carga e a ABNT NBR 12693 juntamente com o INMETRO; o correto e mencionar o Selo ABNT de Conformidade, nao genericamente INMETRO;
- O descritivo e excessivamente resumido para um item de banco — faltam: altura de instalacao (max 1,60 m), distancia maxima de alcance (15 m), obrigatoriedade do lacre e da data de recarga no corpo do aparelho, norma de fabricacao individual de cada tipo de extintor;
- Nao ha separacao entre os tres tipos de extintor como itens independentes; os criterios de uso (natureza do fogo, classe A, B, C) nao estao detalhados;
- A norma `ABNT NBR 13434` na lista de normas deste item esta incorreta — essa norma e de sinalizacao, nao de extintores. O correto seria `ABNT NBR 12693` somente;
- Faltam normas individuais por tipo: extintores CO2 seguem NBR 11715; extintores PQS seguem NBR 11716; extintores de agua pressurizada seguem NBR 11861.

### 4.2 Sinalizacao de Emergencia (ID 83)

O banco possui um item razoavelmente detalhado.

Coberto:

- material PVC expandido 3 mm;
- impressao em serigrafia;
- garantia 36 meses;
- funcao de rotas de fuga e localizacao de equipamentos.

Problemas encontrados:

- Falta mencao as alturas de instalacao por tipo de sinalizacao (1,80 m para proibicao/alerta/orientacao, 1,50 m para antecamaras, 60 cm para indicacao continuada de rotas);
- Falta mencao ao criterio de distancia de visualizacao (6 m) e espaçamento entre placas (max 15 m);
- Falta a classificacao tecnica completa: proibicao, alerta, orientacao, equipamentos, complementar;
- O item mistura requisito de material (PVC, serigrafia, garantia) com criterio de implantacao e classificacao; seria tecnicamente mais robusto ter os criterios de implantacao no descritivo integrado;
- A garantia de 36 meses pode ser mantida como criterio tecnico de durabilidade do material, desde que nao faca referencia ao cliente especifico.

### 4.3 Iluminacao de Emergencia (ID 84)

O banco possui um item com boa base tecnica.

Coberto:

- blocos autonomos IP23;
- autonomia 2h;
- niveis de iluminancia (5 lux escadas, 3 lux corredores);
- comutacao maxima 12 segundos;
- referencia NBR 10898.

Problemas encontrados:

- Ausente a perda maxima de luminosidade (10%) ao longo das 2 horas de autonomia;
- Ausente o criterio de fluxo luminoso nominal (medido apos 2 min) e residual;
- Ausente o limite de ofuscamento (relacao 20:1 entre intensidades maximo e minimo);
- Ausente a exigencia de material anti-chama no involucro;
- Ausente a classe de protecao IP40 como alternativa ao IP23;
- Nao ha item separado para sistema centralizado de iluminacao de emergencia (tecnologia distinta — central + circuitos), que e tecnicamente diferente do bloco autonomo e possui requisitos proprios na NBR 10898;
- A Nota Tecnica NT 2-06 do CBMERJ (verificar equivalente estadual) referencia definicoes adicionais relevantes — essa referencia deveria estar listada.

### 4.4 Sistema de Pressurizacao (ID 85)

O banco possui um item tecnicamente razoavel.

Coberto:

- 2 eletrobombas (principal + reserva);
- 44,5 mca / 12 m³/h;
- tanque hidropneumatico 12 L;
- manometro e pressostato.

Problemas encontrados:

- A subcategoria esta como "Sistema de Pressurização de Escada", mas o sistema descrito no Word e pressurização da rede de hidrantes (eletrobombas de combate a incendio), nao pressurização de escada (que e outro sistema de PPCI voltado a controlar fumaca e pressao diferencial em rotas de fuga). Essa nomenclatura e um erro tecnico grave e deve ser corrigida;
- A norma `ABNT NBR 17240` listada e de sistemas de alarme de incendio, nao de hidrantes; a norma correta para sistema de hidrantes e `ABNT NBR 13714`;
- Faltam criterios de conexao eletrica independente da rede geral da edificacao;
- Falta mencao ao alarme de acionamento da bomba (campainha sincrona na portaria, conforme descrito no Word);
- Falta especificacao dos registros (gaveta ou globo, bronze ou latao) como materiais do item.

### 4.5 LGE e Carreta Proporcionadora (ID 86)

O banco possui um item adequado.

Coberto:

- AFFF 6%;
- NFPA 11 e NBR 15511;
- carreta inox ou PEAD;
- FISPQ e certificados;
- treinamento.

Problemas encontrados:

- O item nao detalha os requisitos tecnicos da carreta (capacidade minima, tipo de bico proporcionador, material do tanque, tipo de rodas);
- O texto do Word indica que a quantidade total de LGE deve ser dimensionada conforme projeto executivo aprovado — esse criterio de dimensionamento pode ser generalizado no descritivo como "quantidade dimensionada pelo tempo de atuacao do sistema conforme norma aplicavel";
- A norma `ABNT NBR 15511` no banco esta correta; `NFPA 11` tambem; verificar se ha NBR nacional equivalente ao NFPA 11 para espumas.

### 4.6 Sistema Fixo de CO2 (ID 87)

O banco possui item tecnicamente razoavel.

Coberto:

- cilindros Mannesmann SAE-1541 ou similar;
- detectores fusivel 144°C;
- dampers corta-fogo;
- tubulacao SCH40 ASTM A53;
- acionamento automatico e manual;
- inundacao total 60 s.

Problemas encontrados:

- O descritivo cita "dutos de cozinha" — essa referencia a ambiente especifico deve ser generalizada para "dutos de exaustao em areas de preparo de alimentos ou ambientes com risco de incendio por gordura";
- A norma `ABNT NBR 12779` listada e de limpeza e manutencao de dutos de ar-condicionado, nao de sistemas de CO2; a norma correta para sistemas fixos de CO2 e `ABNT NBR 12232`;
- A norma `ABNT NBR 16401` listada e de instalacoes de ar-condicionado — nao pertence a este item de PPCI e deve ser removida;
- Falta o criterio de temperatura de atuacao dos detectores (144°C) como requisito de selecao de componente.

### 4.7 Canalizacao Preventiva (ID 88)

O banco possui item bem fundamentado.

Coberto:

- FG Ø 65 mm;
- 180 kgf/cm²;
- pintura vermelha;
- bracadeiras economicas;
- chumbadores CB 3/8";
- espacamento 3,00 m.

Problemas encontrados:

- Falta o criterio de instalacao subterranea a 30 cm de profundidade com pintura em betume;
- Falta mencao a conexoes, registros e valvulas com resistencia igual ou superior a exigida para os tubos;
- Falta criterio para tubulacao vertical (grampos tipo U);
- A cor de referencia "Ypiranga n. 217" deve ser mantida com a indicacao "ou similar de equivalência tecnica" — o banco ja faz isso corretamente;
- O banco atual omite o requisito de tubulacao partir diretamente da Casa de Maquinas de Incendio (CMI), que e um requisito tecnico relevante de topologia da rede.

### 4.8 Hidrantes Internos (ID 89)

O banco possui item razoavelmente detalhado.

Coberto:

- caixa 75×45×17 cm;
- registro globo angular 2½";
- mangueira 1½" tipo II com 15 m;
- adaptador Storz 2½";
- esguicho jato regulavel;
- boca a 1,20 m;
- alcance 30 m.

Problemas encontrados:

- Falta o criterio de resistencia das mangueiras (pressao de teste de 20 kgf/cm², junta tipo STORZ, secoes permanentemente unicas de 15 m);
- Falta o criterio operacional de secagem: mangueiras usadas devem secar na posicao vertical, nunca enroladas umidas;
- Falta o limite de 2 secoes por abrigo como criterio tecnico de dimensionamento;
- A `ABNT NBR 13434` listada como norma de referencia esta incorreta para este item especifico (e de sinalizacao); as normas corretas sao `ABNT NBR 13714` para o sistema de hidrantes e `ABNT NBR 11861` / `ABNT NBR 11861` para as mangueiras; `NBR 13434` deve ser removida deste item.

### 4.9 Hidrante de Recalque (ID 90)

O banco possui item adequado para a funcao.

Coberto:

- caixa FF 40×30 cm;
- registro globo angular 2½";
- adaptador Storz;
- tampao cego com corrente;
- profundidade 40 cm.

Problemas encontrados:

- Falta o criterio de rebordo minimo de 15 cm acima do nivel do solo;
- Falta o criterio tecnico de nao concretar o fundo da caixa para drenagem;
- O item nao menciona a conexao direta com a rede preventiva existente como requisito;
- A localizacao "frente da edificacao" e especifica de projeto; genericamente deve ser "em ponto de facil acesso para as viaturas do corpo de bombeiros, na fachada ou passeio externo".

### 4.10 Sistema de Alarme de Incendio (ID 91)

O banco possui item razoavel mas compacto para a complexidade do subsistema.

Coberto:

- central 2 lacos Classe B;
- acionadores manuais PVC vermelho;
- sirenes audiovisuais 100 dB;
- cabos PP 1,0 e 1,5 mm²;
- protocolo aberto.

Problemas encontrados:

- Um unico item agrupa central de alarme, acionadores manuais, sirenes e cabos — sao componentes com criterios tecnicos proprios e podem justificar itens separados;
- Faltam as especificacoes tecnicas completas da sirene: 20 LEDs de alto brilho, frequencia de flash 100 por minuto, suporte ABS vermelho, lente acrilico, tensao 12/24 Vcc;
- Faltam as especificacoes tecnicas do acionador: LED bicolor (verde = interrogacao / vermelho = alarme), tipo quebra-vidro ou aperta-botao, uso interno nao corrosivo;
- Falta o criterio de distancia maxima de percurso para instalacao de acionadores e sirenes (30 m);
- Falta o registro de final de linha ao fim de cada laco como requisito tecnico;
- Falta o criterio de operacao em modo degradado em caso de falha na central;
- Nao ha item especifico para detectores de fumaca, que o Word descreve genericamente como dispositivos inteligentes com auto-diagnostico — o banco nao tem nenhum item de detector de fumaca ou calor.

### 4.11 Itens Ausentes no Banco

Os seguintes subsistemas ou servicos estao presentes no Word mas nao possuem item dedicado no banco:

| Subsistema / Servico | Justificativa de item separado |
|---|---|
| Detector de Fumaca/Calor Endereçavel | Componente tecnico distinto dos acionadores, com criterios de microprocessador, auto-diagnostico, auto-calibracao, pre-alarme e imunidade a ruido |
| Iluminacao de Emergencia – Sistema Centralizado | Tecnologia distinta do bloco autonomo; a NBR 10898 trata ambos como sistemas proprios |
| Plano de Emergencia | Servico tecnico com norma propria (NT 2-10), ART obrigatoria e conteudo especifico |
| Controle de Materiais de Acabamento (Laudo NT 2-20) | Servico de verificacao e documentacao com norma propria, tecnicamente separado da instalacao |

## 5. Proposta De Itens Para Inserir Ou Revisar

### 5.1 Revisoes em Itens Existentes

| ID | Acao | Descricao da revisao |
|---:|---|---|
| 82 | Revisar | Corrigir descritivo com altura de instalacao (max 1,60 m), distancia de alcance (max 15 m), obrigatoriedade do lacre e da data de recarga; remover `ABNT NBR 13434` da lista de normas deste item; adicionar NBR 11715 (CO2), NBR 11716 (PQS), NBR 11861 (agua pressurizada) |
| 83 | Revisar | Complementar descritivo com criterios de altura de instalacao por tipo, distancia de visualizacao (6 m), espaçamento maximo entre placas (15 m) e classificacao da sinalizacao (proibicao, alerta, orientacao, equipamentos, complementar) |
| 84 | Revisar | Complementar descritivo com: perda maxima de luminosidade (10% em 2h), fluxo luminoso nominal/residual, criterio de ofuscamento (20:1), material anti-chama do involucro, IP40 como alternativa ao IP23; adicionar NT 2-06 do CBMERJ (verificar equivalente estadual) |
| 85 | Revisar | Corrigir subcategoria de "Sistema de Pressurizacao de Escada" para "Sistema de Pressurizacao de Rede de Hidrantes"; trocar norma `ABNT NBR 17240` por `ABNT NBR 13714`; adicionar criterio de ligacao eletrica independente da rede geral e alarme de acionamento da bomba |
| 87 | Revisar | Corrigir norma de referencia: remover `ABNT NBR 12779` (limpeza de dutos) e `ABNT NBR 16401` (ar-condicionado); adicionar `ABNT NBR 12232` (sistemas fixos de CO2); generalizar "dutos de cozinha" para "dutos de exaustao em areas com risco de incendio por gordura" |
| 88 | Revisar | Complementar com: criterio de instalacao subterranea (30 cm de profundidade, betume); conexoes e valvulas com resistencia equivalente aos tubos; tubulacao vertical em grampos tipo U; requisito de partir da CMI |
| 89 | Revisar | Remover `ABNT NBR 13434` da lista de normas; adicionar criterio de pressao de teste das mangueiras (20 kgf/cm²), junta STORZ, limite de 2 secoes por abrigo, criterio de secagem de mangueiras |
| 90 | Revisar | Complementar com: rebordo minimo 15 cm; fundo nao concretado; posicionamento generico acessivel a viaturas do corpo de bombeiros |
| 91 | Revisar | Complementar especificacoes tecnicas completas da sirene (20 LEDs, flash 100 por min, ABS vermelho, acrilico, 12/24 Vcc) e do acionador (LED bicolor, tipo quebra-vidro ou aperta-botao, uso interno); adicionar criterio de distancia maxima de percurso (30 m); adicionar registro de final de linha; adicionar criterio de operacao em modo degradado |

### 5.2 Itens Novos a Inserir

| Acao | Subcategoria proposta | Item proposto | Motivo |
|---|---|---|---|
| Adicionar | Sistema de Alarme | Detector de Fumaca e Calor Endereçavel | O Word descreve componente tecnico distinto com criterios de microprocessador, auto-diagnostico, auto-calibracao, pre-alarme, LED bicolor de status e imunidade a ruido |
| Adicionar | Iluminacao de Emergencia | Iluminacao de Emergencia – Sistema Centralizado (Central + Circuitos) | Tecnologia tecnica distinta dos blocos autonomos; a NBR 10898 as trata como categorias independentes |
| Adicionar | Plano de Emergencia | Elaboracao de Plano de Emergencia | Servico tecnico com norma propria (NT 2-10, verificar equivalente estadual), ART obrigatoria; conteudo especifico e distinto da instalacao fisica dos sistemas |
| Adicionar | Controle de Materiais | Laudo Tecnico de Materiais de Acabamento (NT 2-20) | Servico de verificacao e documentacao tecnica com norma propria (NT 2-20, verificar equivalente estadual) |

### 5.3 Descritivos Sugeridos para Itens Novos

#### Detector de Fumaca e Calor Endereçavel

Servico_item: `Detector de Fumaca e Calor Endereçavel – Sistema de Alarme de Incendio`

Descritivo_integral sugerido:

> Detectores endereçaveis de fumaca optica e/ou calor, de tecnologia baseada em microprocessador, com recursos de auto-diagnostico on-line para deteccao de falhas, verificacao de alarmes espurios por atraso de tempo na confirmacao, deteccao de po ou sujeira (emitindo alerta de manutencao), pre-alarme, auto-calibracao e ajuste remoto de sensibilidade. Devem possuir LED de sinalizacao de status no proprio corpo, operando via rede de comunicacao com imunidade a ruidos. Devem manter operacao em modo degradado em caso de falha na central. Protocolo aberto, compativel com central de alarme conforme ABNT NBR 17240. Instalacao conforme instrucoes tecnicas do Corpo de Bombeiros local (verificar equivalente estadual).

Normas_de_referencia sugeridas:

- ABNT NBR 17240
- ABNT NBR 9441 (verificar substituicao pela NBR 17240 atual)
- Instrucao Tecnica CBMERJ (verificar equivalente estadual)

#### Iluminacao de Emergencia – Sistema Centralizado

Servico_item: `Iluminacao de Emergencia – Sistema Centralizado com Central e Circuitos Dedicados`

Descritivo_integral sugerido:

> Sistema de iluminacao de emergencia do tipo centralizado, constituido por central de emergencia com banco de baterias e carregador, ligada a circuitos eletricos dedicados que alimentam os pontos de luz. A central deve garantir autonomia minima de 2 horas com perda menor que 10% da luminosidade inicial. Tempo de comutacao maximo de 12 segundos. Niveis minimos de iluminancia: 5 lux em locais com desnivel (escadas, passagens com obstaculos) e 3 lux em locais planos (corredores, halls). Cabos resistentes ao fogo (RF) para os circuitos da central. Grau de protecao dos pontos de luz minimo IP23 ou IP40 conforme NBR 6146. Material dos involucos: anti-chama. Fixacao rigida impedindo queda acidental. Manual de manutencao com descricao de primeiro e segundo nivel obrigatorio. Conforme ABNT NBR 10898 e instrucoes tecnicas do Corpo de Bombeiros local (verificar equivalente estadual).

Normas_de_referencia sugeridas:

- ABNT NBR 10898
- ABNT NBR 5410
- ABNT NBR 6146
- Instrucao Tecnica CBMERJ NT 2-06 (verificar equivalente estadual)

#### Plano de Emergencia

Servico_item: `Elaboracao de Plano de Emergencia da Edificacao`

Descritivo_integral sugerido:

> Elaboracao do Plano de Emergencia da edificacao conforme instrucao tecnica do Corpo de Bombeiros local para planos de emergencia (verificar equivalente estadual). O plano deve contemplar procedimentos de evacuacao, identificacao das rotas de saida, atribuicao de responsabilidades, procedimentos de acionamento do socorro externo, instrucoes de uso dos equipamentos de combate a incendio instalados e plano de treinamento da brigada de incendio. Deve ser elaborado por profissional habilitado com emissao de ART. O plano deve ser revisado sempre que houver alteracao na planta da edificacao ou nos sistemas de PPCI instalados.

Normas_de_referencia sugeridas:

- Instrucao Tecnica CBMERJ NT 2-10 (verificar equivalente estadual)
- ABNT NBR 14276 (brigada de incendio)

## 6. Normas A Revisar Neste Recorte

### 6.1 Normas pertinentes confirmadas no recorte

Extintores:

- `ABNT NBR 12693` – sistemas de protecao por extintores;
- `ABNT NBR 11715` – extintores de incendio de agua pressurizada;
- `ABNT NBR 11716` – extintores de incendio de po quimico seco;
- `ABNT NBR 11861` – mangueiras de incendio;
- Instrucao Tecnica CBMERJ (verificar equivalente estadual).

Sinalizacao de emergencia:

- `ABNT NBR 13434` – partes 1, 2 e 3 (projeto, simbolos, especificacao);
- Instrucao Tecnica CBMERJ NT 2-05 (verificar equivalente estadual).

Iluminacao de emergencia:

- `ABNT NBR 10898`;
- `ABNT NBR 5461` (definicoes de luminotecnica);
- `ABNT NBR 9077` (saidas de emergencia);
- `ABNT NBR 6146` (graus de protecao IP);
- Instrucao Tecnica CBMERJ NT 2-06 (verificar equivalente estadual).

Hidrantes e canalizacao preventiva:

- `ABNT NBR 13714` – sistemas de hidrantes e mangotinhos;
- Instrucao Tecnica CBMERJ (verificar equivalente estadual).

Sistema de alarme de incendio:

- `ABNT NBR 17240`;
- Instrucao Tecnica CBMERJ (verificar equivalente estadual).

Sistema fixo de CO2:

- `ABNT NBR 12232` – sistemas fixos automaticos de extincao de incendio com dioxido de carbono (CO2).

LGE:

- `ABNT NBR 15511` – espumas para extincao de incendio;
- `NFPA 11` – standard for low-, medium-, and high-expansion foam (referencia internacional complementar).

Plano de emergencia:

- `ABNT NBR 14276` – brigada de incendio;
- Instrucao Tecnica CBMERJ NT 2-10 (verificar equivalente estadual).

Controle de materiais de acabamento:

- Instrucao Tecnica CBMERJ NT 2-20 (verificar equivalente estadual).

### 6.2 Inconsistencias de Normas Encontradas nos Itens Existentes

| ID | Norma incorreta presente | Motivo | Acao |
|---:|---|---|---|
| 82 | `ABNT NBR 13434` | Norma de sinalizacao; nao pertence ao item de extintores | Remover |
| 85 | `ABNT NBR 17240` | Norma de sistema de alarme; nao pertence ao item de eletrobombas/hidrantes | Trocar por `ABNT NBR 13714` |
| 87 | `ABNT NBR 12779` | Norma de limpeza de dutos de ar-condicionado; nao pertence a sistema de CO2 | Remover |
| 87 | `ABNT NBR 16401` | Norma de instalacoes de ar-condicionado; nao pertence a sistema de CO2 | Remover |
| 87 | — | Falta `ABNT NBR 12232` (sistema fixo de CO2) | Adicionar |
| 89 | `ABNT NBR 13434` | Norma de sinalizacao; nao pertence ao item de hidrantes internos | Remover |

## 7. Decisao Antes De Escrever No JSON

Para a proxima etapa, recomenda-se atualizar o banco em tres movimentos separados:

1. **Correcoes de normas incorretas:** remover as normas claramente erradas identificadas na Secao 6.2 — essas correcoes nao alteram os descritivos e sao de baixo risco.

2. **Revisoes de descritivos e subcategorias:** corrigir o erro tecnico grave da subcategoria do ID 85 (pressurização de escada x pressurização de rede de hidrantes) e complementar os descritivos dos IDs 82, 83, 84, 88, 89, 90 e 91 com os criterios tecnicos ausentes identificados na Secao 4.

3. **Adicao de novos itens:** inserir os quatro itens novos propostos na Secao 5.2 com novos IDs, após aprovacao da proposta de descritivos.

Essa sequencia evita misturar correcao estrutural com expansao do banco e permite validacao incremental.

Proximos IDs sugeridos para novos itens (partindo do ultimo ID PPCI = 91):

- ID 92: Detector de Fumaca e Calor Endereçavel
- ID 93: Iluminacao de Emergencia – Sistema Centralizado
- ID 94: Elaboracao de Plano de Emergencia
- ID 95: Laudo Tecnico de Materiais de Acabamento (NT 2-20)
