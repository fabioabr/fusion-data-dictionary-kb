# Oracle Fusion — General Ledger (GL) — Database Tables

> Referencia de tabelas do modulo GL extraidas do BICC Database Mapping (Release 13/25A).
> Fonte: documentacao oficial Oracle Fusion Cloud ERP.

---

## Sumario

| Grupo | Tabelas |
|-------|---------|
| [Saldos e Balancetes](#saldos-e-balancetes) | GL_BALANCES, GL_BUDGET_BALANCES |
| [Lancamentos Contabeis (Journals)](#lancamentos-contabeis-journals) | GL_JE_BATCHES, GL_JE_HEADERS, GL_JE_LINES, GL_JE_LINES_RECON, GL_JE_CATEGORIES_B, GL_JE_CATEGORIES_TL, GL_JE_SOURCES_B, GL_JE_SOURCES_TL, GL_IMPORT_REFERENCES |
| [Plano de Contas e Combinacoes](#plano-de-contas-e-combinacoes) | GL_CODE_COMBINATIONS, GL_SEG_VAL_HIER_CF, GL_STAT_ACCOUNT_UOM |
| [Ledgers e Configuracao](#ledgers-e-configuracao) | GL_LEDGERS, GL_LEDGER_CONFIG_DETAILS, GL_LEDGER_SEGMENT_VALUES, GL_LEDGER_SET_ASSIGNMENTS, GL_LEGAL_ENTITIES_BSVS |
| [Controle de Acesso](#controle-de-acesso) | GL_ACCESS_SETS, GL_ACCESS_SET_ASSIGNMENTS, GL_ACCESS_SET_LEDGERS |
| [Calendario e Periodos](#calendario-e-periodos) | GL_CALENDARS, GL_PERIOD_STATUSES, GL_PERIOD_TYPES, GL_TRANSACTION_CALENDAR, GL_FISCAL_DAY_V, GL_FISCAL_PERIOD_V, GL_FISCAL_QUARTER_V, GL_FISCAL_YEAR_V |
| [Taxas de Cambio e Conversao](#taxas-de-cambio-e-conversao) | GL_DAILY_RATES, GL_DAILY_CONVERSION_TYPES |
| [Encumbrances (Reservas Orcamentarias)](#encumbrances-reservas-orcamentarias) | GL_ENCUMBRANCE_TYPES_B, GL_ENCUMBRANCE_TYPES_TL, GL_ENCUMBRANCE_TYPES_VL |
| [Configuracao e Regras](#configuracao-e-regras) | GL_AUTOREV_CRITERIA_SETS, GL_RECONCILIATION_RULES, GL_LOOKUPS |
| [Tabelas de Referencia Cruzada (Outros Modulos)](#tabelas-de-referencia-cruzada-outros-modulos) | AP_RECON_SUMMARY_CCID, AR_RECON_SUMMARY_CCID, FND_APPLICATION_VL, FND_CURRENCIES_VL, FND_DOCUMENT_SEQUENCES, FND_KF_STR_INSTANCES_VL, FND_VS_VALUE_SETS, FUN_SEQ_VERSIONS, PER_PERSON_NAMES_F_V, PER_USERS, XCC_CONTROL_BUDGETS, XLA_ACCTG_METHODS_B, XLA_ACCTG_METHODS_TL, XLE_ENTITY_PROFILES |

---

## Saldos e Balancetes

### GL_BALANCES
**Descricao:** Armazena os saldos contabeis para cada combinacao de conta, moeda e periodo. Contem os debitos e creditos liquidos do periodo (`PERIOD_NET_DR`, `PERIOD_NET_CR`) e os saldos iniciais (`BEGIN_BALANCE_DR`, `BEGIN_BALANCE_CR`). E a principal tabela de consulta de saldos do General Ledger.
**Modulo:** General Ledger
**Uso tipico:** Extracao de balancetes, relatorios de saldos por periodo, conciliacao contabil, alimentacao de cubos OLAP e dashboards financeiros.

---

### GL_BUDGET_BALANCES
**Descricao:** Armazena os saldos orcamentarios do General Ledger, em estrutura similar a GL_BALANCES. Os dados orcamentarios sao carregados para o cubo de balancetes a partir desta tabela e utilizados em relatorios de variacao (realizado vs. orcado). Caso o cubo precise ser reconstruido, os dados orcamentarios sao restaurados a partir desta tabela.
**Modulo:** General Ledger
**Uso tipico:** Relatorios de variacao orcamentaria, analise de budget vs. realizado, reconstrucao de cubos orcamentarios.

---

## Lancamentos Contabeis (Journals)

### GL_JE_BATCHES
**Descricao:** Armazena os lotes (batches) de lancamentos contabeis. Cada registro inclui o nome do lote, descricao, status de postagem e totais de debitos e creditos. Os status possiveis incluem: `U` (nao postado), `P` (postado), `S` (selecionado para postagem), `I` (em processo de postagem).
**Modulo:** General Ledger
**Uso tipico:** Consulta de lotes de lancamentos, monitoramento do pipeline de postagem, auditoria de lancamentos.

---

### GL_JE_HEADERS
**Descricao:** Armazena os cabecalhos dos lancamentos contabeis. Cada registro contem o ID do lote associado, o nome e descricao do lancamento, categoria, fonte, data contabil, moeda, ledger e outras informacoes de cabecalho.
**Modulo:** General Ledger
**Uso tipico:** Consulta de lancamentos por periodo, fonte ou categoria; rastreamento de lancamentos importados de subledgers; auditoria contabil.

---

### GL_JE_LINES
**Descricao:** Armazena as linhas individuais dos lancamentos contabeis. Cada registro contem o ID do cabecalho associado, o numero da linha, o ID da combinacao de contas (code combination), e os valores de debito e credito da linha.
**Modulo:** General Ledger
**Uso tipico:** Detalhamento de lancamentos contabeis, conciliacao linha a linha, extracao de movimentacoes por conta.

---

### GL_JE_LINES_RECON
**Descricao:** Armazena informacoes de conciliacao das linhas de lancamentos contabeis. Vincula linhas do journal a processos de conciliacao, permitindo rastrear quais lancamentos foram conciliados.
**Modulo:** General Ledger
**Uso tipico:** Processos de conciliacao contabil, identificacao de lancamentos nao conciliados, auditoria.

---

### GL_JE_CATEGORIES_B
**Descricao:** Tabela base que armazena as categorias de lancamentos contabeis (ex.: Adjustment, Accrual, Revaluation). Cada categoria classifica o tipo de lancamento no GL.
**Modulo:** General Ledger
**Uso tipico:** Configuracao e classificacao de lancamentos; filtros em relatorios por tipo de lancamento.

---

### GL_JE_CATEGORIES_TL
**Descricao:** Tabela de traducao (Translation) das categorias de lancamentos contabeis. Contem os nomes e descricoes das categorias em diferentes idiomas.
**Modulo:** General Ledger
**Uso tipico:** Suporte a ambientes multi-idioma; exibicao de nomes de categorias no idioma do usuario.

---

### GL_JE_SOURCES_B
**Descricao:** Tabela base que armazena as fontes (sources) dos lancamentos contabeis, identificando o sistema ou modulo de origem (ex.: Payables, Receivables, Assets, Manual).
**Modulo:** General Ledger
**Uso tipico:** Rastreamento de origem dos lancamentos; filtros por fonte em relatorios e consultas.

---

### GL_JE_SOURCES_TL
**Descricao:** Tabela de traducao (Translation) das fontes de lancamentos contabeis. Contem nomes e descricoes das fontes em diferentes idiomas.
**Modulo:** General Ledger
**Uso tipico:** Suporte a ambientes multi-idioma; exibicao de nomes de fontes no idioma do usuario.

---

### GL_IMPORT_REFERENCES
**Descricao:** Armazena as referencias individuais de transacoes de subledgers que foram sumarizadas em linhas de lancamentos do GL pelo processo de Journal Import. Para cada fonte configurada com "Import Journal References = Yes", o sistema popula esta tabela com um registro por transacao do sistema alimentador.
**Modulo:** General Ledger
**Uso tipico:** Rastreabilidade de lancamentos ate a transacao original no subledger (drill-down); auditoria de origem de lancamentos importados.

---

## Plano de Contas e Combinacoes

### GL_CODE_COMBINATIONS
**Descricao:** Contem as combinacoes validas de contas contabeis (segmentos do flexfield contabil) para cada estrutura de plano de contas do General Ledger. Cada registro representa uma combinacao unica de segmentos (empresa, centro de custo, conta natural, etc.) com seus atributos de habilitacao e permissao de postagem.
**Modulo:** General Ledger
**Uso tipico:** Validacao de contas, consulta de combinacoes contabeis, juncao com tabelas de saldos e lancamentos para obter a descricao completa da conta.

---

### GL_SEG_VAL_HIER_CF
**Descricao:** Armazena a hierarquia de valores de segmentos contabeis em formato "flattened" (achatado). Permite consultar relacoes pai-filho entre valores de segmentos para fins de consolidacao e roll-up.
**Modulo:** General Ledger
**Uso tipico:** Navegacao hierarquica de contas, consolidacao de saldos por nivel de hierarquia, relatorios de roll-up.

---

### GL_STAT_ACCOUNT_UOM
**Descricao:** Armazena as unidades de medida (UOM) associadas a contas estatisticas. Cada registro vincula uma conta estatistica a sua unidade de medida correspondente (ex.: horas, headcount, metros quadrados).
**Modulo:** General Ledger
**Uso tipico:** Configuracao de contas estatisticas, relatorios com metricas nao-monetarias.

---

## Ledgers e Configuracao

### GL_LEDGERS
**Descricao:** Contem informacoes sobre os ledgers (razoes contabeis) e ledger sets definidos no Accounting Setup Manager. Cada registro inclui nome do ledger, nome curto, descricao, moeda funcional, calendario, tipo de periodo, plano de contas (chart of accounts) e metodo contabil associado.
**Modulo:** General Ledger
**Uso tipico:** Consulta da configuracao de ledgers, identificacao de moeda funcional e calendario por ledger, base para juncoes com praticamente todas as tabelas do GL.

---

### GL_LEDGER_CONFIG_DETAILS
**Descricao:** Armazena os detalhes de configuracao dos ledgers, incluindo parametros de setup como opcoes de lancamento, tratamento de moeda e outras configuracoes granulares definidas durante a implantacao do ledger.
**Modulo:** General Ledger
**Uso tipico:** Consulta de parametros de configuracao de ledgers, auditoria de setup contabil.

---

### GL_LEDGER_SEGMENT_VALUES
**Descricao:** Armazena os valores de segmentos de balanceamento (Balancing Segment Values — BSV) atribuidos a cada ledger. Define quais valores de empresa/entidade sao validos para postagem em cada ledger.
**Modulo:** General Ledger
**Uso tipico:** Controle de quais entidades podem postar em cada ledger, validacao de lancamentos.

---

### GL_LEDGER_SET_ASSIGNMENTS
**Descricao:** Armazena as atribuicoes de ledgers a ledger sets (conjuntos de razoes). Permite agrupar multiplos ledgers sob um unico conjunto para fins de relatorios consolidados e processamento em lote.
**Modulo:** General Ledger
**Uso tipico:** Configuracao de ledger sets, relatorios consolidados multi-ledger.

---

### GL_LEGAL_ENTITIES_BSVS
**Descricao:** Armazena o mapeamento entre entidades legais (Legal Entities) e valores de segmento de balanceamento (BSV). Define quais BSVs pertencem a cada entidade legal para fins de relatorios legais e regulatorios.
**Modulo:** General Ledger
**Uso tipico:** Mapeamento de entidade legal para segmentos contabeis, relatorios por entidade legal, compliance regulatorio.

---

## Controle de Acesso

### GL_ACCESS_SETS
**Descricao:** Armazena a definicao dos conjuntos de acesso (Data Access Sets) do General Ledger. Cada access set define quais ledgers, segmentos de balanceamento e segmentos de gestao um usuario ou grupo de usuarios pode acessar.
**Modulo:** General Ledger
**Uso tipico:** Controle de acesso a dados contabeis, segregacao de funcoes, configuracao de seguranca.

---

### GL_ACCESS_SET_ASSIGNMENTS
**Descricao:** Armazena as atribuicoes detalhadas de um access set, incluindo os segmentos de balanceamento e gestao especificos permitidos.
**Modulo:** General Ledger
**Uso tipico:** Detalhamento granular de permissoes de acesso a dados por segmento.

---

### GL_ACCESS_SET_LEDGERS
**Descricao:** Armazena a relacao entre access sets e os ledgers aos quais concedem acesso. Define quais ledgers estao incluidos em cada conjunto de acesso.
**Modulo:** General Ledger
**Uso tipico:** Controle de acesso por ledger, configuracao de seguranca multi-ledger.

---

## Calendario e Periodos

### GL_CALENDARS
**Descricao:** Armazena a definicao dos calendarios contabeis (Accounting Calendars), incluindo nome e descricao. Cada calendario define a estrutura de periodos utilizada por um ou mais ledgers.
**Modulo:** General Ledger
**Uso tipico:** Configuracao de calendarios contabeis, consulta de estrutura de periodos.

---

### GL_PERIOD_STATUSES
**Descricao:** Armazena o status de cada periodo contabil por ledger e aplicacao. Os status possiveis incluem: Open (aberto para postagem), Closed (fechado), Never Opened, Future Entry, e Permanently Closed.
**Modulo:** General Ledger
**Uso tipico:** Controle de abertura e fechamento de periodos, validacao de datas de lancamento, processos de fechamento contabil.

---

### GL_PERIOD_TYPES
**Descricao:** Armazena os tipos de periodo contabil disponiveis no sistema (ex.: Month, Quarter, Year). Define a granularidade dos periodos nos calendarios.
**Modulo:** General Ledger
**Uso tipico:** Configuracao de calendarios, classificacao de periodos.

---

### GL_TRANSACTION_CALENDAR
**Descricao:** Armazena o calendario de transacoes, que define quais dias sao uteis para fins de contabilizacao. Utilizado para determinar datas validas de lancamento em cada periodo.
**Modulo:** General Ledger
**Uso tipico:** Determinacao de dias uteis para lancamento, controle de datas validas.

---

### GL_FISCAL_DAY_V
**Descricao:** View que fornece a dimensao de dia fiscal do calendario contabil. Cada registro representa um dia, com referencia ao periodo, trimestre e ano fiscal correspondente. Nivel mais granular da hierarquia de calendario.
**Modulo:** General Ledger
**Uso tipico:** Analise por data contabil, drill-down temporal em relatorios, determinacao do periodo contabil de uma transacao.

---

### GL_FISCAL_PERIOD_V
**Descricao:** View que fornece a dimensao de periodo fiscal do calendario contabil. Consolida os dias em periodos (tipicamente meses), com datas de inicio e fim.
**Modulo:** General Ledger
**Uso tipico:** Relatorios por periodo contabil, analise de tendencias mensais.

---

### GL_FISCAL_QUARTER_V
**Descricao:** View que fornece a dimensao de trimestre fiscal do calendario contabil. Consolida os periodos em trimestres.
**Modulo:** General Ledger
**Uso tipico:** Relatorios trimestrais, analise de performance por trimestre fiscal.

---

### GL_FISCAL_YEAR_V
**Descricao:** View que fornece a dimensao de ano fiscal do calendario contabil. Nivel mais alto da hierarquia temporal.
**Modulo:** General Ledger
**Uso tipico:** Relatorios anuais, comparativos year-over-year.

---

## Taxas de Cambio e Conversao

### GL_DAILY_RATES
**Descricao:** Armazena as taxas de conversao diarias entre moedas. Cada registro contem a moeda de origem, moeda de destino, data da taxa, tipo de conversao e o valor da taxa. Substitui a antiga tabela GL_DAILY_CONVERSION_RATES.
**Modulo:** General Ledger
**Uso tipico:** Conversao de moedas em transacoes diarias, revalorizacao de saldos em moeda estrangeira, relatorios multi-moeda.

---

### GL_DAILY_CONVERSION_TYPES
**Descricao:** Armazena os tipos de conversao de moeda disponiveis (ex.: Corporate, Spot, User). Cada tipo define uma politica de taxa de cambio para conversao de valores entre moedas.
**Modulo:** General Ledger
**Uso tipico:** Configuracao de politicas de conversao cambial, selecao de tipo de taxa em processos de traducao e revalorizacao.

---

## Encumbrances (Reservas Orcamentarias)

### GL_ENCUMBRANCE_TYPES_B
**Descricao:** Tabela base que armazena os tipos de encumbrance (reserva orcamentaria), incluindo Commitment e Obligation. Utilizada em processos de controle orcamentario para reservar valores antes da efetivacao da despesa.
**Modulo:** General Ledger
**Uso tipico:** Configuracao de tipos de reserva orcamentaria, controle de comprometimento de budget.

---

### GL_ENCUMBRANCE_TYPES_TL
**Descricao:** Tabela de traducao (Translation) dos tipos de encumbrance. Contem nomes e descricoes em multiplos idiomas.
**Modulo:** General Ledger
**Uso tipico:** Suporte a ambientes multi-idioma para exibicao dos tipos de encumbrance.

---

### GL_ENCUMBRANCE_TYPES_VL
**Descricao:** View combinada (Base + Translation) dos tipos de encumbrance. Apresenta os dados da tabela base junto com as traducoes no idioma da sessao do usuario.
**Modulo:** General Ledger
**Uso tipico:** Consulta simplificada de tipos de encumbrance com traducao automatica; utilizada na maioria dos relatorios e interfaces.

---

## Configuracao e Regras

### GL_AUTOREV_CRITERIA_SETS
**Descricao:** Armazena os conjuntos de criterios para reversao automatica de lancamentos contabeis (AutoReverse). Define quais categorias de lancamentos devem ser revertidos automaticamente no periodo seguinte (ex.: accruals).
**Modulo:** General Ledger
**Uso tipico:** Configuracao de reversao automatica de accruals, controle de lancamentos provisorios.

---

### GL_RECONCILIATION_RULES
**Descricao:** Armazena as regras de conciliacao contabil do General Ledger. Define criterios para match automatico entre lancamentos de debito e credito em contas de conciliacao (ex.: contas de clearing).
**Modulo:** General Ledger
**Uso tipico:** Conciliacao automatica de contas, identificacao de itens em aberto.

---

### GL_LOOKUPS
**Descricao:** Armazena os valores de lookup (listas de valores) especificos do modulo General Ledger. Contem codigos e significados utilizados em diversos campos de configuracao e validacao do GL.
**Modulo:** General Ledger
**Uso tipico:** Decodificacao de campos codificados em relatorios, validacao de valores em interfaces.

---

## Tabelas de Referencia Cruzada (Outros Modulos)

> As tabelas abaixo pertencem a outros modulos do Oracle Fusion (AP, AR, FND, FUN, PER, XCC, XLA, XLE) mas aparecem no contexto do GL por serem referenciadas em processos de conciliacao, configuracao ou integracao com o General Ledger.

### AP_RECON_SUMMARY_CCID
**Descricao:** Armazena os CCIDs (Code Combination IDs) do Accounts Payable utilizados nos processos de conciliacao AP-to-GL. Os CCIDs sao derivados dos segmentos de balanceamento e contas naturais informados como parametros de conciliacao, ou das contas de payables definidas no GL.
**Modulo:** Accounts Payable (AP) — referencia cruzada com GL
**Uso tipico:** Conciliacao entre subledger de AP e General Ledger, relatorios de reconciliacao AP-GL.

---

### AR_RECON_SUMMARY_CCID
**Descricao:** Armazena os CCIDs do Accounts Receivable utilizados nos processos de conciliacao AR-to-GL. Estrutura analoga a AP_RECON_SUMMARY_CCID, permitindo a reconciliacao entre dados de Receivables, Subledger Accounting (SLA) e General Ledger.
**Modulo:** Accounts Receivable (AR) — referencia cruzada com GL
**Uso tipico:** Conciliacao entre subledger de AR e General Ledger, relatorios de reconciliacao AR-GL.

---

### FND_APPLICATION_VL
**Descricao:** View que contem informacoes sobre as aplicacoes registradas no Oracle Fusion, incluindo nome curto, nome de exibicao e descricao. Sufixo `_VL` indica que e uma view combinada com traducao.
**Modulo:** Foundation (FND) — referencia cruzada com GL
**Uso tipico:** Identificacao de aplicacoes em joins com tabelas que referenciam application_id (ex.: GL_PERIOD_STATUSES).

---

### FND_CURRENCIES_VL
**Descricao:** View que contem a definicao de todas as moedas disponiveis no sistema, incluindo codigo ISO, nome, simbolo, precisao decimal e status (ativa/inativa).
**Modulo:** Foundation (FND) — referencia cruzada com GL
**Uso tipico:** Decodificacao de codigos de moeda em relatorios, validacao de moedas em transacoes.

---

### FND_DOCUMENT_SEQUENCES
**Descricao:** Armazena as definicoes de sequencias de numeracao de documentos (Document Sequencing). Cada registro define uma sequencia com seu tipo (automatica, manual ou sem gaps), aplicacao associada e regras de numeracao.
**Modulo:** Foundation (FND) — referencia cruzada com GL
**Uso tipico:** Numeracao sequencial de lancamentos contabeis, conformidade com requisitos fiscais de sequenciamento.

---

### FND_KF_STR_INSTANCES_VL
**Descricao:** View que contem instancias de estruturas de Key Flexfield (KFF). No contexto do GL, armazena as instancias do flexfield contabil (Accounting Flexfield), vinculando a estrutura de segmentos ao plano de contas utilizado em cada ledger.
**Modulo:** Foundation (FND) — referencia cruzada com GL
**Uso tipico:** Identificacao da estrutura do plano de contas, mapeamento de segmentos do flexfield contabil.

---

### FND_VS_VALUE_SETS
**Descricao:** Armazena as definicoes de conjuntos de valores (Value Sets) em nivel de cabecalho. Cada value set define as regras de validacao (formato, tipo, tabela de validacao) aplicadas a segmentos de flexfields e parametros de relatorios.
**Modulo:** Foundation (FND) — referencia cruzada com GL
**Uso tipico:** Configuracao de segmentos do plano de contas, validacao de valores de segmento, administracao de flexfields.

---

### FUN_SEQ_VERSIONS
**Descricao:** Armazena as versoes de sequencias de numeracao do modulo Subledger Accounting / Financials Common. Cada versao define um intervalo de datas de vigencia e regras de sequenciamento para numeracao de documentos contabeis.
**Modulo:** Financials Common (FUN) — referencia cruzada com GL
**Uso tipico:** Controle de versoes de sequencias de numeracao, rastreamento de numeracao por periodo.

---

### PER_PERSON_NAMES_F_V
**Descricao:** View que contem os nomes das pessoas cadastradas no modulo HCM (Human Capital Management), com efetividade por data. Inclui nome completo, nome de exibicao (display name) e nome de lista.
**Modulo:** Human Resources (PER) — referencia cruzada com GL
**Uso tipico:** Exibicao do nome do usuario responsavel por lancamentos, relatorios com identificacao de aprovadores.

---

### PER_USERS
**Descricao:** Armazena informacoes dos usuarios do sistema Oracle Fusion, incluindo username, user_guid e vinculacao com a pessoa (person_id) do modulo HCM.
**Modulo:** Human Resources (PER) — referencia cruzada com GL
**Uso tipico:** Identificacao de usuarios que criaram ou aprovaram lancamentos, auditoria de acoes por usuario.

---

### XCC_CONTROL_BUDGETS
**Descricao:** Armazena as informacoes de cabecalho dos orcamentos de controle (Control Budgets) do modulo Budgetary Control. Define os orcamentos utilizados para controle de disponibilidade de fundos antes da aprovacao de despesas.
**Modulo:** Budgetary Control (XCC) — referencia cruzada com GL
**Uso tipico:** Controle orcamentario, verificacao de disponibilidade de fundos, relatorios de comprometimento.

---

### XLA_ACCTG_METHODS_B
**Descricao:** Tabela base que armazena os metodos contabeis (Accounting Methods) do Subledger Accounting (SLA/XLA). Cada metodo contabil define as regras de como transacoes de subledgers sao contabilizadas no GL.
**Modulo:** Subledger Accounting (XLA) — referencia cruzada com GL
**Uso tipico:** Configuracao de metodos contabeis atribuidos a ledgers, definicao de regras de contabilizacao.

---

### XLA_ACCTG_METHODS_TL
**Descricao:** Tabela de traducao (Translation) dos metodos contabeis do Subledger Accounting. Contem nomes e descricoes em multiplos idiomas.
**Modulo:** Subledger Accounting (XLA) — referencia cruzada com GL
**Uso tipico:** Suporte a ambientes multi-idioma para exibicao dos metodos contabeis.

---

### XLE_ENTITY_PROFILES
**Descricao:** Armazena os perfis das entidades legais (Legal Entities) do Oracle Fusion. Contem informacoes como nome da entidade legal, pais de registro, identificador fiscal e dados cadastrais. E a tabela central do modulo Legal Entity (XLE).
**Modulo:** Legal Entity (XLE) — referencia cruzada com GL
**Uso tipico:** Identificacao de entidades legais associadas a ledgers, relatorios fiscais e regulatorios, compliance.

---

## Notas Tecnicas

### Convencoes de sufixo nas tabelas Oracle Fusion

| Sufixo | Significado |
|--------|-------------|
| `_B` | Tabela base (Base) — dados independentes de idioma |
| `_TL` | Tabela de traducao (Translation) — dados traduzidos por idioma |
| `_VL` | View combinada (View Language) — juncao de `_B` + `_TL` no idioma da sessao |
| `_V` | View — consulta pre-definida sobre uma ou mais tabelas |
| `_F` | Tabela com efetividade por data (Date-effective) |

### Relacoes principais entre tabelas GL

```
GL_JE_BATCHES (1) ──→ (N) GL_JE_HEADERS (1) ──→ (N) GL_JE_LINES
                                                          │
                                                          ▼
                                                   GL_CODE_COMBINATIONS
                                                          │
                                                          ▼
                                                     GL_BALANCES
                                                          │
                                                          ▼
                                                     GL_LEDGERS ──→ GL_CALENDARS
                                                                 ──→ GL_PERIOD_STATUSES
```

### Fontes de referencia

- [Oracle Fusion Cloud Financials — Tables and Views (OEDMF)](https://docs.oracle.com/en/cloud/saas/financials/25d/oedmf/)
- [GL Tables in Oracle Fusion — RPForOracle](https://rpforacle.blogspot.com/2020/05/gl-tables-in-oracle-fusion.html)
- [Oracle General Ledger — Overview of Table Structure](http://oracleapps88.blogspot.com/2016/08/oracle-general-ledger-overview-of-table.html)
- [GL_CODE_COMBINATIONS — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/23d/oedmf/glcodecombinations-19917.html)
- [GL_LEDGERS — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/25d/oedmf/glledgers-28219.html)
- [GL_BUDGET_BALANCES — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/glbudgetbalances-20078.html)
- [XCC_CONTROL_BUDGETS — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/xcccontrolbudgets-8259.html)
- [GL_STAT_ACCOUNT_UOM — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/22c/oedmf/glstataccountuom-15692.html)
- [GL_FISCAL_DAY_V — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/21d/oedmf/glfiscaldayv-6732.html)
- [GL_FISCAL_PERIOD_V — Oracle Docs](https://docs.oracle.com/en/cloud/saas/financials/21d/oedmf/glfiscalperiodv-6414.html)
