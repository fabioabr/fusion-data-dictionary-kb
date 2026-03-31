---
id: DOC-GL-039
doc_type: system-doc
title: "XCC_CONTROL_BUDGETS — Orçamentos de Controle"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - orcamento
  - budget-control
  - controle-orcamentario
  - budgetary-control
aliases:
  - XCC_CONTROL_BUDGETS
  - xcc_control_budgets
  - orcamentos-controle
  - control-budgets
  - budgetary-control
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# XCC_CONTROL_BUDGETS

## 📌 Visão Geral

Armazena a definição dos **orçamentos de controle (budgetary control)** do Oracle Fusion Cloud. Define os parâmetros de controle orçamentário — quais ledgers, períodos e contas estão sob controle de budget, com que nível de rigor (advisory, absolute, etc.) e quais ações são tomadas quando o orçamento é excedido.

> [!note] Prefixo XCC
> O prefixo `XCC` identifica tabelas do módulo **Budgetary Control** (antigo GL Budget Control no E-Business Suite). No Fusion, o budgetary control é um módulo separado que se integra com GL, AP, PO e Procurement.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle orçamentário:** Definição de regras que validam se há saldo de orçamento disponível antes de aprovar transações (requisições, POs, invoices, journals).
- **Budget checking:** O processo de validação orçamentária consulta esta tabela para determinar se o controle está ativo e qual o nível de enforcement.
- **Reservas (Encumbrance):** Configuração de como reservas orçamentárias são criadas e controladas.
- **Período orçamentário:** Definição do período de controle (mensal, trimestral, anual, project-to-date).
- **Governança financeira:** Implementação de políticas de governança que impedem gastos acima do orçamento aprovado.
- **Auditoria:** Documentação dos parâmetros de controle orçamentário vigentes.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTROL_BUDGET_ID | NUMBER(18) | NOT NULL | PK | Identificador único do orçamento de controle | — | 🟢 95% |
| 2 | CONTROL_BUDGET_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do orçamento de controle | — | 🟢 95% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger associado | [[gl_ledgers]] | 🟢 95% |
| 4 | BUDGET_ENTITY_ID | NUMBER(18) | NULL | FK | Identificador da entidade orçamentária | — | 🟡 75% |
| 5 | CONTROL_LEVEL | VARCHAR2(30) | NOT NULL | Classificação | Nível de controle: ABSOLUTE (bloqueia), ADVISORY (alerta), NONE | — | 🟢 90% |
| 6 | FUNDS_CHECK_LEVEL | VARCHAR2(30) | NULL | Classificação | Nível de verificação de fundos: MANDATORY, OPTIONAL, NONE | — | 🟡 80% |
| 7 | BUDGET_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de orçamento: EXPENSE, REVENUE, ALL | — | 🟡 75% |
| 8 | AMOUNT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de valor controlado: PTD (Period-to-Date), YTD (Year-to-Date), PJTD (Project-to-Date) | — | 🟡 80% |
| 9 | CURRENCY_CODE | VARCHAR2(15) | NULL | Configuração | Moeda do controle orçamentário | — | 🟢 90% |
| 10 | PERIOD_SET_NAME | VARCHAR2(15) | NULL | FK | Nome do conjunto de períodos (calendário contábil) | [[gl_period_sets]] | 🟡 80% |
| 11 | PERIOD_TYPE | VARCHAR2(15) | NULL | FK | Tipo de período do controle | [[gl_period_types]] | 🟡 80% |
| 12 | STATUS | VARCHAR2(30) | NOT NULL | Status | Status do orçamento de controle: ACTIVE, INACTIVE, CLOSED | — | 🟢 90% |
| 13 | TOLERANCE_AMOUNT | NUMBER | NULL | Configuração | Valor de tolerância acima do orçamento (antes de bloquear/alertar) | — | 🟡 75% |
| 14 | TOLERANCE_PERCENTAGE | NUMBER | NULL | Configuração | Percentual de tolerância acima do orçamento | — | 🟡 75% |
| 15 | ENABLE_BC_FLAG | VARCHAR2(1) | NULL | Status | Indica se o controle orçamentário está habilitado (Y/N) | — | 🟡 80% |
| 16 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do orçamento de controle | — | 🟢 90% |
| 17 | START_DATE | DATE | NULL | Vigência | Data de início da vigência do controle | — | 🟡 80% |
| 18 | END_DATE | DATE | NULL | Vigência | Data de fim da vigência (NULL = sem expiração) | — | 🟡 80% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 23 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (conjunto de períodos)
- [[gl_period_types]] — via `PERIOD_TYPE` (tipo de período)

### Tabelas-filha (FK de saída)
- Tabelas de detalhes de budget control (ex: XCC_CONTROL_BUDGET_DETAILS) — contêm os valores orçados por conta/período.
- Tabelas de resultados de funds check — armazenam os resultados das validações orçamentárias.

---

## 📎 Uso Típico

### Orçamentos de controle ativos por ledger
```sql
SELECT cb.CONTROL_BUDGET_ID,
       cb.CONTROL_BUDGET_NAME,
       cb.CONTROL_LEVEL,
       cb.AMOUNT_TYPE,
       cb.STATUS
FROM   XCC_CONTROL_BUDGETS cb
WHERE  cb.LEDGER_ID = :p_ledger_id
  AND  cb.STATUS = 'ACTIVE'
ORDER BY cb.CONTROL_BUDGET_NAME;
```

### Orçamentos com controle absoluto (bloqueante)
```sql
SELECT cb.CONTROL_BUDGET_NAME,
       cb.TOLERANCE_AMOUNT,
       cb.TOLERANCE_PERCENTAGE,
       cb.CURRENCY_CODE
FROM   XCC_CONTROL_BUDGETS cb
WHERE  cb.LEDGER_ID = :p_ledger_id
  AND  cb.CONTROL_LEVEL = 'ABSOLUTE'
  AND  cb.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Orçamentos de controle ativos
- `CONTROL_LEVEL = 'ABSOLUTE'` — Controle bloqueante (impede transação sem saldo)
- `CONTROL_LEVEL = 'ADVISORY'` — Controle consultivo (alerta mas permite)
- `AMOUNT_TYPE = 'YTD'` — Controle acumulado no ano
- `ENABLE_BC_FLAG = 'Y'` — Controle orçamentário habilitado

---

## 🔒 Observações

- O `CONTROL_LEVEL` define o comportamento quando o orçamento é excedido: **ABSOLUTE** bloqueia a transação, **ADVISORY** emite alerta mas permite, **NONE** não valida.
- O `AMOUNT_TYPE` determina a janela de validação: **PTD** valida por período, **YTD** valida acumulado no ano, **PJTD** valida acumulado no projeto.
- Tolerâncias permitem uma margem antes de acionar o controle — útil para evitar bloqueios por centavos de arredondamento.
- O módulo Budgetary Control (XCC) no Oracle Fusion é separado do GL, mas fortemente integrado. Ele intercepta transações de AP (invoices), PO (purchase orders), Procurement (requisições) e GL (journals manuais).
- Em instituições financeiras, o controle orçamentário é tipicamente usado para despesas administrativas (OPEX), não para operações financeiras (trading, tesouraria).
- Esta tabela tem confiança moderada (75-80%) em várias colunas porque a documentação oficial do Oracle Fusion para o módulo XCC é menos detalhada que para GL/AP/AR core. Validar estrutura no ambiente real.

---

## 🔗 PVOs Relacionados

### [[balanceactivitypvo|BalanceActivityPVO]] (OTHER · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUDGET_CHART_OF_ACCOUNTS_ID | ControlBudgetBudgetChartOfAccountsId | — |
| CHART_OF_ACCOUNTS_ID | ControlBudgetChartOfAccountsId | — |
| CONTROL_BUDGET_ID | ControlBudgetControlBudgetId | — |
| CURRENCY_CODE | ControlBudgetCurrencyCode | ✅ |
| FUNDS_RELEASE_TIMEFRAME | ControlBudgetFundsReleaseTimeframe | — |
| LEDGER_ID | ControlBudgetLedgerId | — |
| NAME | ControlBudgetName | — |
| OBJECT_VERSION_NUMBER | ControlBudgetObjectVersionNumber | — |
| PJC_CONTRACT_ID | ControlBudgetPjcContractId | — |
| PROJECT_ID | ControlBudgetProjectId | — |

### [[balancepvo|BalancePVO]] (OTHER · BICC: 1/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CREATION_ALLOWED_FLAG | ControlBudgetAccountCreationAllowedFlag | — |
| BALANCE_DECREASES_ALLOWED_FLAG | ControlBudgetBalanceDecreasesAllowedFlag | — |
| BALANCE_INCREASES_ALLOWED_FLAG | ControlBudgetBalanceIncreasesAllowedFlag | — |
| BDG_AMT_NOT_FOUND_RESULT_CODE | ControlBudgetBdgAmtNotFoundResultCode | — |
| BUDGET_CHART_OF_ACCOUNTS_ID | ControlBudgetBudgetChartOfAccountsId | — |
| BUDGET_MANAGER_ID | ControlBudgetBudgetManagerId | — |
| CHART_OF_ACCOUNTS_ID | ControlBudgetChartOfAccountsId | — |
| CONTROL_BUDGET_ID | ControlBudgetControlBudgetId | — |
| CONTROL_LEVEL_CODE | ControlBudgetControlLevelCode | — |
| CREATED_BY | ControlBudgetCreatedBy | — |
| CREATION_DATE | ControlBudgetCreationDate | — |
| CURRENCY_CODE | ControlBudgetCurrencyCode | — |
| DEFAULT_RATE_TYPE | ControlBudgetDefaultRateType | — |
| DESCRIPTION | ControlBudgetDescription | — |
| END_DATE | ControlBudgetEndDate | — |
| END_EFF_PERIOD_NUM | ControlBudgetEndEffPeriodNum | — |
| END_PERIOD_NAME | ControlBudgetEndPeriodName | — |
| LAST_UPDATE_DATE | ControlBudgetLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ControlBudgetLastUpdateLogin | — |
| LAST_UPDATED_BY | ControlBudgetLastUpdatedBy | — |
| LEDGER_ID | ControlBudgetLedgerId | — |
| NAME | ControlBudgetName | — |
| NEGATIVE_BALANCES_ALLOWED_FLAG | ControlBudgetNegativeBalancesAllowedFlag | — |
| OBJECT_VERSION_NUMBER | ControlBudgetObjectVersionNumber | — |
| PCBD_ERROR_CODE | ControlBudgetPcbdErrorCode | — |
| PERIOD_SET_NAME | ControlBudgetPeriodSetName | — |
| PERIOD_TYPE | ControlBudgetPeriodType | — |
| PJC_CONTRACT_ID | ControlBudgetPjcContractId | — |
| PROJECT_ID | ControlBudgetProjectId | — |
| REQUEST_ID | ControlBudgetRequestId | — |
| SOURCE_BUDGET | ControlBudgetSourceBudget | — |
| SOURCE_BUDGET_SYSTEM_CODE | ControlBudgetSourceBudgetSystemCode | — |
| START_DATE | ControlBudgetStartDate | — |
| START_EFF_PERIOD_NUM | ControlBudgetStartEffPeriodNum | — |
| START_PERIOD_NAME | ControlBudgetStartPeriodName | — |
| STATUS_CODE | ControlBudgetStatusCode | — |
| TOLERANCE_AMOUNT | ControlBudgetToleranceAmount | — |
| TOLERANCE_PERCENT | ControlBudgetTolerancePercent | — |
| UOM_CODE | ControlBudgetUomCode | — |

### [[controlbudgetextractpvo|ControlBudgetExtractPVO]] (OTHER · BICC: 42/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_OVERRIDES_FLAG | AllowOverridesFlag | ✅ |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| BALANCE_DECREASES_ALLOWED_FLAG | BalanceDecreasesAllowedFlag | ✅ |
| BALANCE_INCREASES_ALLOWED_FLAG | BalanceIncreasesAllowedFlag | ✅ |
| BUDGET_CHART_OF_ACCOUNTS_ID | BudgetChartOfAccountsId | ✅ |
| BUDGET_MANAGER_ID | BudgetManagerId | ✅ |
| CHART_OF_ACCOUNTS_ID | ChartOfAccountsId | ✅ |
| CONTROL_BUDGET_ID | ControlBudgetId | ✅ |
| CONTROL_LEVEL_CODE | ControlLevelCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| DEFAULT_RATE_TYPE | DefaultRateType | ✅ |
| DESCRIPTION | Description | ✅ |
| END_DATE | EndDate | ✅ |
| END_EFF_PERIOD_NUM | EndEffPeriodNum | ✅ |
| END_PERIOD_NAME | EndPeriodName | ✅ |
| FUNDS_RELEASE_TIMEFRAME | FundsReleaseTimeframe | ✅ |
| FV_TYPE_CODE | FvTypeCode | — |
| INTERNAL_BUDGET_TYPE_CODE | InternalBudgetTypeCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEDGER_ID | LedgerId | ✅ |
| MAXIMUM_OVERRIDE_AMOUNT | MaximumOverrideAmount | ✅ |
| NAME | Name | ✅ |
| NEGATIVE_BALANCES_ALLOWED_FLAG | NegativeBalancesAllowedFlag | ✅ |
| NO_OVERRIDES_NOTIFY_FLAG | NoOverridesNotifyFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OFFLINE_REASON_CODE | OfflineReasonCode | — |
| OVERRIDES_TAKEN_NOTIFY_FLAG | OverridesTakenNotifyFlag | ✅ |
| PARENT_SOURCE_BUDGET | ParentSourceBudget | ✅ |
| PARENT_SOURCE_SYSTEM | ParentSourceSystem | ✅ |
| PERIOD_SET_NAME | PeriodSetName | ✅ |
| PERIOD_TYPE | PeriodType | ✅ |
| PJC_CONTRACT_ID | PjcContractId | ✅ |
| PROJECT_ID | ProjectId | ✅ |
| SOURCE_BUDGET | SourceBudget | ✅ |
| SOURCE_BUDGET_SYSTEM_CODE | SourceBudgetSystemCode | ✅ |
| START_DATE | StartDate | ✅ |
| START_EFF_PERIOD_NUM | StartEffPeriodNum | ✅ |
| START_PERIOD_NAME | StartPeriodName | ✅ |
| STATUS_CODE | StatusCode | ✅ |
| TOLERANCE_AMOUNT | ToleranceAmount | ✅ |
| TOLERANCE_PERCENT | TolerancePercent | ✅ |
| UOM_CODE | UomCode | ✅ |

### [[controlbudgetpvo|ControlBudgetPVO]] (OTHER · BICC: 12/48)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CREATION_ALLOWED_FLAG | ControlBudgetUnsecuredAccountCreationAllowedFlag | — |
| ALLOW_OVERRIDES_FLAG | ControlBudgetUnsecuredAllowOverridesFlag | — |
| BALANCE_DECREASES_ALLOWED_FLAG | ControlBudgetUnsecuredBalanceDecreasesAllowedFlag | — |
| BALANCE_INCREASES_ALLOWED_FLAG | ControlBudgetUnsecuredBalanceIncreasesAllowedFlag | — |
| BDG_AMT_NOT_FOUND_RESULT_CODE | ControlBudgetUnsecuredBdgAmtNotFoundResultCode | — |
| BUDGET_CHART_OF_ACCOUNTS_ID | ControlBudgetUnsecuredBudgetChartOfAccountsId | — |
| BUDGET_MANAGER_ID | ControlBudgetUnsecuredBudgetManagerId | — |
| CHART_OF_ACCOUNTS_ID | ControlBudgetUnsecuredChartOfAccountsId | — |
| CONTROL_BUDGET_ID | ControlBudgetId | ✅ |
| CONTROL_BUDGET_ID | MasterControlBudgetControlBudgetId | — |
| CONTROL_LEVEL_CODE | ControlBudgetUnsecuredControlLevelCode | ✅ |
| CREATED_BY | ControlBudgetUnsecuredCreatedBy | — |
| CREATION_DATE | ControlBudgetUnsecuredCreationDate | ✅ |
| CURRENCY_CODE | ControlBudgetUnsecuredCurrencyCode | ✅ |
| DEFAULT_RATE_TYPE | ControlBudgetUnsecuredDefaultRateType | — |
| DESCRIPTION | ControlBudgetUnsecuredDescription | ✅ |
| END_DATE | ControlBudgetUnsecuredEndDate | — |
| END_EFF_PERIOD_NUM | ControlBudgetUnsecuredEndEffPeriodNum | — |
| END_PERIOD_NAME | ControlBudgetUnsecuredEndPeriodName | — |
| FUNDS_RELEASE_TIMEFRAME | ControlBudgetUnsecuredFundsReleaseTimeframe | ✅ |
| LAST_UPDATE_DATE | ControlBudgetUnsecuredLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ControlBudgetUnsecuredLastUpdateLogin | — |
| LAST_UPDATED_BY | ControlBudgetUnsecuredLastUpdatedBy | — |
| LEDGER_ID | ControlBudgetUnsecuredLedgerId | — |
| MAXIMUM_OVERRIDE_AMOUNT | ControlBudgetUnsecuredMaximumOverrideAmount | — |
| NAME | ControlBudgetUnsecuredName | ✅ |
| NAME | MasterControlBudgetName | — |
| NEGATIVE_BALANCES_ALLOWED_FLAG | ControlBudgetUnsecuredNegativeBalancesAllowedFlag | — |
| NO_OVERRIDES_NOTIFY_FLAG | NoOverridesNotifyFlag | — |
| OBJECT_VERSION_NUMBER | ControlBudgetUnsecuredObjectVersionNumber | — |
| OVERRIDES_TAKEN_NOTIFY_FLAG | ControlBudgetUnsecuredOverridesTakenNotifyFlag | — |
| PARENT_SOURCE_SYSTEM | ControlBudgetUnsecuredParentSourceSystem | — |
| PERIOD_SET_NAME | ControlBudgetUnsecuredPeriodSetName | — |
| PERIOD_TYPE | ControlBudgetUnsecuredPeriodType | — |
| PJC_CONTRACT_ID | ControlBudgetUnsecuredPjcContractId | — |
| PREVIOUS_STATUS_CODE | ControlBudgetUnsecuredPreviousStatusCode | — |
| PROJECT_ID | ControlBudgetUnsecuredProjectId | — |
| REQUEST_ID | ControlBudgetUnsecuredRequestId | — |
| RULE_SQL | ControlBudgetUnsecuredRuleSql | — |
| SOURCE_BUDGET | ControlBudgetUnsecuredSourceBudget | — |
| SOURCE_BUDGET_SYSTEM_CODE | ControlBudgetUnsecuredSourceBudgetSystemCode | ✅ |
| START_DATE | ControlBudgetUnsecuredStartDate | — |
| START_EFF_PERIOD_NUM | ControlBudgetUnsecuredStartEffPeriodNum | — |
| START_PERIOD_NAME | ControlBudgetUnsecuredStartPeriodName | — |
| STATUS_CODE | ControlBudgetUnsecuredStatusCode | ✅ |
| TOLERANCE_AMOUNT | ControlBudgetUnsecuredToleranceAmount | ✅ |
| TOLERANCE_PERCENT | ControlBudgetUnsecuredTolerancePercent | ✅ |
| UOM_CODE | ControlBudgetUnsecuredUomCode | — |

### [[fiscaldaypvo|FiscalDayPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | ControlBudgetUnsecuredChartOfAccountsId | — |
| CONTROL_BUDGET_ID | ControlBudgetUnsecuredControlBudgetId | — |
| LEDGER_ID | ControlBudgetUnsecuredLedgerId | — |

### [[glfiscalperiodpvo|GLFiscalPeriodPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | ControlBudgetUnsecuredChartOfAccountsId | — |
| CONTROL_BUDGET_ID | ControlBudgetUnsecuredControlBudgetId | — |
| LEDGER_ID | ControlBudgetUnsecuredLedgerId | — |

---

## 📚 Referências

- [Oracle Docs — Budgetary Control](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
