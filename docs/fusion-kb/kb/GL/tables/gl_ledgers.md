---
id: DOC-GL-027
doc_type: system-doc
title: "GL_LEDGERS — Ledgers (Livros Contábeis)"
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
  - ledger
  - livro-contabil
  - configuracao
aliases:
  - GL_LEDGERS
  - gl_ledgers
  - ledgers
  - livros-contabeis
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEDGERS

## 📌 Visão Geral

Armazena a definição dos **ledgers (livros contábeis)** do General Ledger. É a tabela central de configuração do GL — define o plano de contas, moeda funcional, calendário contábil e método de subledger accounting para cada livro. Praticamente toda tabela transacional do GL referencia `LEDGER_ID` desta tabela. Suporta Primary Ledger, Secondary Ledger e Reporting Currency.

> [!note] Tabela central do GL
> Esta é a tabela mais referenciada do módulo GL. O `LEDGER_ID` é FK em [[gl_balances]], [[gl_je_headers]], [[gl_je_lines]], [[gl_periods]] e dezenas de outras tabelas do ERP.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração do GL:** Definição dos livros contábeis da organização (primary, secondary, reporting).
- **Multi-book accounting:** Suporte a múltiplos livros contábeis com diferentes planos de contas e moedas.
- **Consolidação:** Identificação dos ledgers para consolidação financeira.
- **Relatórios financeiros:** Filtro obrigatório por ledger em todas as consultas contábeis.
- **Subledger Accounting:** Configuração do método de contabilização (Standard Accrual, Cash etc.).
- **Compliance regulatório:** Ledgers separados para IFRS vs BRGAAP quando necessário.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ledger | — | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do ledger (ex: "Patria Primary Ledger") | — | 🟢 100% |
| 3 | SHORT_NAME | VARCHAR2(20) | NOT NULL | Identificação | Nome curto/código do ledger | — | 🟢 100% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual do ledger | — | 🟢 100% |
| 5 | LEDGER_CATEGORY_CODE | VARCHAR2(30) | NOT NULL | Classificação | Categoria: PRIMARY, SECONDARY, ALC (Reporting Currency), NONE | — | 🟢 100% |
| 6 | OBJECT_TYPE_CODE | VARCHAR2(1) | NOT NULL | Classificação | Tipo de objeto: L (Ledger), S (Ledger Set) | — | 🟢 95% |
| 7 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NOT NULL | FK | ID da estrutura do plano de contas (Key Flexfield) | — | 🟢 100% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Classificação | Moeda funcional do ledger (ex: BRL, USD) | — | 🟢 100% |
| 9 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do calendário contábil (period set) | — | 🟢 100% |
| 10 | ACCOUNTED_PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo de período contábil (Month, Quarter, Year) | — | 🟢 100% |
| 11 | FIRST_LEDGER_PERIOD_NAME | VARCHAR2(15) | NULL | Período | Primeiro período contábil do ledger | — | 🟢 90% |
| 12 | RET_EARN_CODE_COMBINATION_ID | NUMBER(18) | NULL | FK | CCID da conta de lucros/prejuízos acumulados (retained earnings) | [[gl_code_combinations]] | 🟢 95% |
| 13 | SLA_ACCOUNTING_METHOD_CODE | VARCHAR2(30) | NULL | Classificação | Método de contabilização SLA (Standard Accrual, Cash etc.) | — | 🟢 95% |
| 14 | SLA_ACCOUNTING_METHOD_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do método SLA | — | 🟢 90% |
| 15 | SUSPENSE_ALLOWED_FLAG | VARCHAR2(1) | NULL | Controle | Permite lançamentos em conta suspense quando desbalanceado (Y/N) | — | 🟢 95% |
| 16 | ALLOW_INTERCOMPANY_POST_FLAG | VARCHAR2(1) | NULL | Controle | Permite lançamentos intercompany (Y/N) | — | 🟢 90% |
| 17 | ENABLE_AVERAGE_BALANCES_FLAG | VARCHAR2(1) | NULL | Controle | Habilita saldos médios diários (Y/N) | — | 🟢 90% |
| 18 | ENABLE_BUDGETARY_CONTROL_FLAG | VARCHAR2(1) | NULL | Controle | Habilita controle orçamentário (Y/N) | — | 🟢 95% |
| 19 | REQUIRE_BUDGET_JOURNALS_FLAG | VARCHAR2(1) | NULL | Controle | Requer journals de budget (Y/N) | — | 🟡 80% |
| 20 | ENABLE_JE_APPROVAL_FLAG | VARCHAR2(1) | NULL | Controle | Habilita workflow de aprovação de journals (Y/N) | — | 🟢 90% |
| 21 | ENABLE_AUTOMATIC_TAX_FLAG | VARCHAR2(1) | NULL | Controle | Habilita cálculo automático de imposto (Y/N) | — | 🟡 80% |
| 22 | CONSOLIDATION_LEDGER_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é ledger de consolidação (Y/N) | — | 🟢 90% |
| 23 | TRANSLATE_INTERCOMPANY_FLAG | VARCHAR2(1) | NULL | Controle | Traduzir transações intercompany (Y/N) | — | 🟡 75% |
| 24 | BAL_SEG_VALUE_OPTION_CODE | VARCHAR2(25) | NULL | Classificação | Opção de balancing segment: A (All Values), I (Selected Values) | — | 🟢 90% |
| 25 | BAL_SEG_COLUMN_NAME | VARCHAR2(25) | NULL | Classificação | Nome da coluna do balancing segment (ex: SEGMENT1) | — | 🟢 90% |
| 26 | MGT_SEG_COLUMN_NAME | VARCHAR2(25) | NULL | Classificação | Nome da coluna do management segment (ex: SEGMENT3) | — | 🟢 90% |
| 27 | COMPLETION_STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status de completude da configuração do ledger | — | 🟡 75% |
| 28 | CONFIGURATION_ID | NUMBER(18) | NULL | FK | ID da configuração do ledger | [[gl_ledger_config_details]] | 🟡 80% |
| 29 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 30 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 31 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 32 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `RET_EARN_CODE_COMBINATION_ID` (conta de lucros acumulados)
- [[gl_ledger_config_details]] — via `CONFIGURATION_ID` (configuração do ledger)

### Tabelas-filha (FK de saída)
- [[gl_balances]] — via `LEDGER_ID` (saldos contábeis)
- [[gl_je_headers]] — via `LEDGER_ID` (headers de journals)
- [[gl_je_lines]] — via `LEDGER_ID` (linhas de journals)
- [[gl_ledger_segment_values]] — via `LEDGER_ID` (valores de segmento do ledger)
- [[gl_ledger_set_assignments]] — via `LEDGER_ID` (atribuições de ledger sets)
- [[gl_legal_entities_bsvs]] — via `LEDGER_ID` (BSVs por entidade legal)
- [[gl_periods]] — via `PERIOD_SET_NAME` (períodos contábeis)

---

## 📎 Uso Típico

### Listar todos os ledgers da organização
```sql
SELECT gl.LEDGER_ID,
       gl.NAME,
       gl.SHORT_NAME,
       gl.LEDGER_CATEGORY_CODE,
       gl.CURRENCY_CODE,
       gl.PERIOD_SET_NAME,
       gl.SLA_ACCOUNTING_METHOD_CODE
FROM   GL_LEDGERS gl
WHERE  gl.OBJECT_TYPE_CODE = 'L'
ORDER BY gl.LEDGER_CATEGORY_CODE, gl.NAME;
```

### Identificar o primary ledger e seus secondary ledgers
```sql
SELECT gl.LEDGER_ID,
       gl.NAME,
       gl.LEDGER_CATEGORY_CODE,
       gl.CURRENCY_CODE,
       gl.CHART_OF_ACCOUNTS_ID
FROM   GL_LEDGERS gl
WHERE  gl.LEDGER_CATEGORY_CODE IN ('PRIMARY', 'SECONDARY')
  AND  gl.OBJECT_TYPE_CODE = 'L'
ORDER BY gl.LEDGER_CATEGORY_CODE;
```

### Filtros comuns
- `OBJECT_TYPE_CODE = 'L'` — Apenas ledgers (não ledger sets)
- `LEDGER_CATEGORY_CODE = 'PRIMARY'` — Primary ledger
- `LEDGER_CATEGORY_CODE = 'SECONDARY'` — Secondary ledger
- `LEDGER_CATEGORY_CODE = 'ALC'` — Reporting currency (Automatic Ledger Currency)
- `CURRENCY_CODE = 'BRL'` — Ledgers em Real

---

## 🔒 Observações

- `LEDGER_ID` é a FK mais comum do módulo GL — presente em praticamente todas as tabelas transacionais.
- `LEDGER_CATEGORY_CODE` distingue: **PRIMARY** (livro principal), **SECONDARY** (livro secundário com regras contábeis diferentes), **ALC** (moeda de reporte).
- `OBJECT_TYPE_CODE = 'S'` indica um Ledger Set (agrupamento lógico de ledgers) — não é um ledger real, mas uma abstração para simplificar atribuições.
- O `CHART_OF_ACCOUNTS_ID` define qual estrutura de plano de contas o ledger usa — pode variar entre primary e secondary ledgers.
- `RET_EARN_CODE_COMBINATION_ID` aponta para a conta de lucros/prejuízos acumulados — usada no fechamento anual para transferir o resultado.
- A configuração do ledger é feita uma única vez no setup inicial — alterações posteriores têm impacto significativo.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[balanceactivitypvo|BalanceActivityPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | ✅ |
| LEDGER_ID | LedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[balancepvo|BalancePVO]] (GL · BICC: 6/112)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgerAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgerApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgerArDocSequencingOptionFlag | — |
| ATTRIBUTE1 | GlLedgerAttribute1 | — |
| ATTRIBUTE10 | GlLedgerAttribute10 | — |
| ATTRIBUTE11 | GlLedgerAttribute11 | — |
| ATTRIBUTE12 | GlLedgerAttribute12 | — |
| ATTRIBUTE13 | GlLedgerAttribute13 | — |
| ATTRIBUTE14 | GlLedgerAttribute14 | — |
| ATTRIBUTE15 | GlLedgerAttribute15 | — |
| ATTRIBUTE2 | GlLedgerAttribute2 | — |
| ATTRIBUTE3 | GlLedgerAttribute3 | — |
| ATTRIBUTE4 | GlLedgerAttribute4 | — |
| ATTRIBUTE5 | GlLedgerAttribute5 | — |
| ATTRIBUTE6 | GlLedgerAttribute6 | — |
| ATTRIBUTE7 | GlLedgerAttribute7 | — |
| ATTRIBUTE8 | GlLedgerAttribute8 | — |
| ATTRIBUTE9 | GlLedgerAttribute9 | — |
| ATTRIBUTE_CATEGORY | GlLedgerAttributeCategory | — |
| ATTRIBUTE_DATE1 | GlLedgerAttributeDate1 | — |
| ATTRIBUTE_DATE2 | GlLedgerAttributeDate2 | — |
| ATTRIBUTE_DATE3 | GlLedgerAttributeDate3 | — |
| ATTRIBUTE_DATE4 | GlLedgerAttributeDate4 | — |
| ATTRIBUTE_DATE5 | GlLedgerAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | GlLedgerAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | GlLedgerAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | GlLedgerAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | GlLedgerAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | GlLedgerAttributeNumber5 | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgerAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgerBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgerBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgerBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | ChartOfAccountsId | ✅ |
| COMPLETE_FLAG | GlLedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgerCompletionStatusCode | — |
| CONFIGURATION_ID | GlLedgerConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgerCreateJeFlag | — |
| CREATED_BY | GlLedgerCreatedBy | — |
| CREATION_DATE | GlLedgerCreationDate | — |
| CRITERIA_SET_ID | GlLedgerCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgerCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerCurrencyCode | ✅ |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgerDailyTranslationRateType | — |
| DESCRIPTION | GlLedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgerEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgerEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgerFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgerImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgerImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgerIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgerJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LastUpdateDateSob | ✅ |
| LAST_UPDATE_LOGIN | GlLedgerLastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBySob | ✅ |
| LATEST_ENCUMBRANCE_YEAR | GlLedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerCategoryCode | ✅ |
| LEDGER_ID | GlLedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | GlLedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | GlLedgerMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | GlLedgerMgtSegValueSetId | — |
| NAME | GlLedgerName | — |
| NET_CLOSING_BAL_FLAG | GlLedgerNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgerNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | GlLedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgerPeriodSetName | ✅ |
| POP_UP_STAT_ACCOUNT_FLAG | GlLedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | GlLedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgerRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | GlLedgerResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | GlLedgerRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | GlLedgerRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | GlLedgerRoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | GlLedgerSequencingModeCode | — |
| SHORT_NAME | GlLedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | GlLedgerSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | GlLedgerSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | GlLedgerSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | GlLedgerSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | GlLedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | GlLedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | GlLedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | GlLedgerTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | GlLedgerTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | GlLedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | GlLedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | GlLedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | GlLedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | GlLedgerValidateJournalRefDate | — |

### [[bankaccountbalanceavailabilitypvo|BankAccountBalanceAvailabilityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[bankaccountbalancepvo|BankAccountBalancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[bankstatementlineavailabilitypvo|BankStatementLineAvailabilityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[bankstatementlinespvo|BankStatementLinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[billingplan|BillingPlan]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |

### [[costorgbookpvo|CostOrgBookPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_ID | GlLedgersPEOLedgerId | — |
| NAME | GlLedgersPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersPEOObjectVersionNumber | — |

### [[costorgbookrefpvo|CostOrgBookRefPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_ID | GlLedgersPEOLedgerId | — |
| NAME | GlLedgersPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersPEOObjectVersionNumber | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgersObjectVersionNumber | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |

### [[customercontractheaderspvo|CustomerContractHeadersPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[depreciationextractpvo|DepreciationExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| LEDGER_ID | LedgerId1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgersArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgersAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| COMPLETE_FLAG | GlLedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode | — |
| CONFIGURATION_ID | GlLedgersConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | GlLedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | — |
| DESCRIPTION | GlLedgersDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgersEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | GlLedgersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GlLedgersLastUpdateLogin | — |
| LAST_UPDATED_BY | GlLedgersLastUpdatedBy | — |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| MGT_SEG_COLUMN_NAME | GlLedgersMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | GlLedgersMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | GlLedgersMgtSegValueSetId | — |
| NAME | GlLedgersName | — |
| NET_CLOSING_BAL_FLAG | GlLedgersNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | GlLedgersPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | GlLedgersPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | GlLedgersResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | GlLedgersRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | GlLedgersRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | GlLedgersRoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | GlLedgersSequencingModeCode | — |
| SHORT_NAME | GlLedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | GlLedgersSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | GlLedgersSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | GlLedgersSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | GlLedgersSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | GlLedgersSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | GlLedgersSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | GlLedgersTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | GlLedgersTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | GlLedgersTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | GlLedgersTranslateYatdFlag | — |
| USSGL_OPTION_CODE | GlLedgersUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | GlLedgersValidateJournalRefDate | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER · BICC: 1/86)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgersArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgersAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| COMPLETE_FLAG | GlLedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode | — |
| CONFIGURATION_ID | GlLedgersConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | GlLedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | — |
| DESCRIPTION | GlLedgersDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgersEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | GlLedgersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlLedgersLastUpdateLogin | — |
| LAST_UPDATED_BY | GlLedgersLastUpdatedBy | — |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| MGT_SEG_COLUMN_NAME | GlLedgersMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | GlLedgersMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | GlLedgersMgtSegValueSetId | — |
| NAME | GlLedgersName | — |
| NET_CLOSING_BAL_FLAG | GlLedgersNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | GlLedgersPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | GlLedgersPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | GlLedgersResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | GlLedgersRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | GlLedgersRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | GlLedgersRoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | GlLedgersSequencingModeCode | — |
| SHORT_NAME | GlLedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | GlLedgersSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | GlLedgersSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | GlLedgersSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | GlLedgersSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | GlLedgersSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | GlLedgersSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | GlLedgersTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | GlLedgersTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | GlLedgersTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | GlLedgersTranslateYatdFlag | — |
| USSGL_OPTION_CODE | GlLedgersUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | GlLedgersValidateJournalRefDate | — |

### [[externaltransactionspvo|ExternalTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | AccountsSin | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[fabalancesextractpvo|FaBalancesExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber | — |

### [[fatransactionextractpvo|FaTransactionExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| LEDGER_ID | LedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[fiscaldaypvo|FiscalDayPVO]] (GL · BICC: 1/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | AccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | AlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | AllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | AutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | AutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | BalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | BalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | BalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | BudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | BudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | ChartOfAccountsId | — |
| COMPLETE_FLAG | CompleteFlag | — |
| COMPLETION_STATUS_CODE | CompletionStatusCode | — |
| CONFIGURATION_ID | ConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | ConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | CreateJeFlag | — |
| CREATED_BY | LedgerCreatedBy | — |
| CREATION_DATE | LedgerCreationDate | — |
| CRITERIA_SET_ID | CriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | CumTransCodeCombinationId | — |
| CURRENCY_CODE | CurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | DailyTranslationRateType | — |
| DESCRIPTION | Description | — |
| ENABLE_AUTOMATIC_TAX_FLAG | EnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | EnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | EnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | EnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | EnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | EnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | EnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | FirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | FutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | ImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | ImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | IntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | JrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LedgerLastUpdateLogin | — |
| LAST_UPDATED_BY | LedgerLastUpdatedBy | — |
| LATEST_ENCUMBRANCE_YEAR | LatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerCategoryCode | — |
| LEDGER_ID | LedgerId | — |
| MGT_SEG_COLUMN_NAME | MgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | MgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | MgtSegValueSetId | — |
| NAME | LedgerName | — |
| NET_INCOME_CODE_COMBINATION_ID | NetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | ObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | PeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | PeriodEndRateType | — |
| PERIOD_SET_NAME | PeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | PopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | PriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | RequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | ResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | RetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | RevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | RoundingCodeCombinationId | — |
| SHORT_NAME | ShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | SlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | SlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | SlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | SlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | SlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | SlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | SlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | SlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | SuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | ThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | TrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | TransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | TranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | TranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | TranslateYatdFlag | — |
| USSGL_OPTION_CODE | UssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | ValidateJournalRefDate | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerPEOAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerPEOAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerPEOAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | LedgerPEOAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerPEOAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerPEOAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerPEOBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerPEOBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerPEOBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerPEOBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerPEOBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerPEOCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerPEOCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerPEOConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerPEOConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerPEOCreateJeFlag | — |
| CREATED_BY | LedgerPEOCreatedBy11 | — |
| CREATION_DATE | LedgerPEOCreationDate11 | — |
| CRITERIA_SET_ID | LedgerPEOCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerPEOCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerPEOCurrencyCode2 | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerPEODailyTranslationRateType | — |
| DESCRIPTION | LedgerPEODescription2 | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerPEOEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerPEOEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerPEOEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerPEOEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerPEOEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerPEOEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerPEOEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | LedgerPEOEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerPEOFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerPEOFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerPEOImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerPEOImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerPEOIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerPEOJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerPEOLastUpdateDate11 | — |
| LAST_UPDATE_LOGIN | LedgerPEOLastUpdateLogin11 | — |
| LAST_UPDATED_BY | LedgerPEOLastUpdatedBy11 | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerPEOLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerPEOLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerPEOLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerPEOLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerPEOLedgerCategoryCode | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| LEDGER_ID | LedgerPEOLedgerId1 | — |
| MGT_SEG_COLUMN_NAME | LedgerPEOMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerPEOMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerPEOMgtSegValueSetId | — |
| NAME | LedgerPEOName1 | — |
| NET_CLOSING_BAL_FLAG | LedgerPEONetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerPEONetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerPEOObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber17 | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber18 | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPEOPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPEOPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPEOPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPEOPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPEOPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerPEORequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerPEOResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerPEORetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerPEORevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerPEORoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | LedgerPEOSequencingModeCode | — |
| SHORT_NAME | LedgerPEOShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerPEOSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerPEOSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerPEOSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerPEOSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerPEOSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerPEOSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerPEOSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerPEOSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerPEOSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerPEOThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerPEOTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerPEOTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerPEOTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerPEOTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerPEOTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerPEOUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerPEOValidateJournalRefDate | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerPEOAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerPEOAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerPEOAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOArDocSequencingOptionFlag | — |
| ATTRIBUTE_CATEGORY | LedgerPEOAttributeCategory8 | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | LedgerPEOAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerPEOAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerPEOAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerPEOBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerPEOBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerPEOBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerPEOBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerPEOBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerPEOCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerPEOCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerPEOConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerPEOConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerPEOCreateJeFlag | — |
| CREATED_BY | LedgerPEOCreatedBy9 | — |
| CREATION_DATE | LedgerPEOCreationDate9 | — |
| CRITERIA_SET_ID | LedgerPEOCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerPEOCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerPEOCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerPEODailyTranslationRateType | — |
| DESCRIPTION | LedgerPEODescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerPEOEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerPEOEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerPEOEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerPEOEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerPEOEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerPEOEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerPEOEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | LedgerPEOEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerPEOFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerPEOFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerPEOImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerPEOImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerPEOIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerPEOJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerPEOLastUpdateDate9 | — |
| LAST_UPDATE_LOGIN | LedgerPEOLastUpdateLogin9 | — |
| LAST_UPDATED_BY | LedgerPEOLastUpdatedBy9 | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerPEOLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerPEOLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerPEOLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerPEOLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerPEOLedgerCategoryCode | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerPEOMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerPEOMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerPEOMgtSegValueSetId | — |
| NAME | LedgerPEOName2 | — |
| NET_CLOSING_BAL_FLAG | LedgerPEONetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerPEONetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerPEOObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber8 | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPEOPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPEOPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPEOPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPEOPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPEOPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerPEORequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerPEOResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerPEORetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerPEORevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerPEORoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | LedgerPEOSequencingModeCode | — |
| SHORT_NAME | LedgerPEOShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerPEOSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerPEOSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerPEOSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerPEOSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerPEOSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerPEOSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerPEOSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerPEOSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerPEOSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerPEOThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerPEOTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerPEOTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerPEOTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerPEOTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerPEOTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerPEOUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerPEOValidateJournalRefDate | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerPEOAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerPEOAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerPEOAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOArDocSequencingOptionFlag | — |
| ATTRIBUTE_CATEGORY | LedgerPEOAttributeCategory | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | LedgerPEOAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerPEOAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerPEOAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerPEOBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerPEOBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerPEOBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerPEOBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerPEOBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerPEOCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerPEOCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerPEOConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerPEOConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerPEOCreateJeFlag | — |
| CREATED_BY | LedgerPEOCreatedBy | — |
| CREATION_DATE | LedgerPEOCreationDate | — |
| CRITERIA_SET_ID | LedgerPEOCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerPEOCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerPEOCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerPEODailyTranslationRateType | — |
| DESCRIPTION | LedgerPEODescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerPEOEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerPEOEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerPEOEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerPEOEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerPEOEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerPEOEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerPEOEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | LedgerPEOEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerPEOFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerPEOFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerPEOImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerPEOImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerPEOIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerPEOJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | LedgerPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LedgerPEOLastUpdatedBy | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerPEOLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerPEOLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerPEOLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerPEOLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerPEOLedgerCategoryCode | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerPEOMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerPEOMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerPEOMgtSegValueSetId | — |
| NAME | LedgerPEOName | — |
| NET_CLOSING_BAL_FLAG | LedgerPEONetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerPEONetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerPEOObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPEOPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPEOPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPEOPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPEOPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPEOPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerPEORequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerPEOResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerPEORetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerPEORevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerPEORoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | LedgerPEOSequencingModeCode | — |
| SHORT_NAME | LedgerPEOShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerPEOSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerPEOSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerPEOSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerPEOSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerPEOSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerPEOSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerPEOSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerPEOSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerPEOSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerPEOThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerPEOTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerPEOTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerPEOTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerPEOTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerPEOTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerPEOUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerPEOValidateJournalRefDate | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgersArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgersAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| COMPLETE_FLAG | GlLedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode | — |
| CONFIGURATION_ID | GlLedgersConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | GlLedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | — |
| DESCRIPTION | GlLedgersDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgersEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | GlLedgersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GlLedgersLastUpdateLogin | — |
| LAST_UPDATED_BY | GlLedgersLastUpdatedBy | — |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| MGT_SEG_COLUMN_NAME | GlLedgersMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | GlLedgersMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | GlLedgersMgtSegValueSetId | — |
| NAME | GlLedgersName | — |
| NET_CLOSING_BAL_FLAG | GlLedgersNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | GlLedgersPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | GlLedgersPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | GlLedgersResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | GlLedgersRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | GlLedgersRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | GlLedgersRoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | GlLedgersSequencingModeCode | — |
| SHORT_NAME | GlLedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | GlLedgersSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | GlLedgersSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | GlLedgersSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | GlLedgersSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | GlLedgersSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | GlLedgersSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | GlLedgersTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | GlLedgersTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | GlLedgersTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | GlLedgersTranslateYatdFlag | — |
| USSGL_OPTION_CODE | GlLedgersUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | GlLedgersValidateJournalRefDate | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerPEOAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerPEOAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerPEOAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | LedgerPEOArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | LedgerPEOAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerPEOAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerPEOAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerPEOBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerPEOBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerPEOBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerPEOBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerPEOBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerPEOChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerPEOCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerPEOCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerPEOConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerPEOConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerPEOCreateJeFlag | — |
| CREATED_BY | LedgerPEOCreatedBy16 | — |
| CREATION_DATE | LedgerPEOCreationDate16 | — |
| CRITERIA_SET_ID | LedgerPEOCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerPEOCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerPEOCurrencyCode2 | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerPEODailyTranslationRateType | — |
| DESCRIPTION | LedgerPEODescription1 | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerPEOEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerPEOEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerPEOEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerPEOEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerPEOEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerPEOEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerPEOEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | LedgerPEOEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerPEOFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerPEOFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerPEOImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerPEOImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerPEOIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerPEOJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerPEOLastUpdateDate16 | — |
| LAST_UPDATE_LOGIN | LedgerPEOLastUpdateLogin16 | — |
| LAST_UPDATED_BY | LedgerPEOLastUpdatedBy16 | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerPEOLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerPEOLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerPEOLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerPEOLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerPEOLedgerCategoryCode | — |
| LEDGER_ID | LedgerPEOLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerPEOMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerPEOMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerPEOMgtSegValueSetId | — |
| NAME | LedgerPEOName1 | — |
| NET_CLOSING_BAL_FLAG | LedgerPEONetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerPEONetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerPEOObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerPEOObjectVersionNumber15 | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPEOPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPEOPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPEOPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPEOPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPEOPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerPEORequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerPEOResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerPEORetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerPEORevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerPEORoundingCodeCombinationId | — |
| SEQUENCING_MODE_CODE | LedgerPEOSequencingModeCode | — |
| SHORT_NAME | LedgerPEOShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerPEOSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerPEOSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerPEOSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerPEOSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerPEOSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerPEOSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerPEOSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerPEOSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerPEOSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerPEOThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerPEOTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerPEOTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerPEOTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerPEOTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerPEOTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerPEOUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerPEOValidateJournalRefDate | — |

### [[fulfillline|FulfillLine]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[fulfilllineref|FulfillLineRef]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[glfiscalperiodpvo|GLFiscalPeriodPVO]] (GL · BICC: 1/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CRITERIA_SET_ID | LedgerCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | ✅ |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerMgtSegValueSetId | — |
| NAME | LedgerName | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerRoundingCodeCombinationId | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName1 | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[header|Header]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[invoiceselfassessedtaxdistributionpvo|InvoiceSelfAssessedTaxDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| CURRENCY_CODE | LedgersCurrencyCode | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgersObjectVersionNumber | — |

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[journallinepvo|JournalLinePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerChartOfAccountsId | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DESCRIPTION | LedgerDescription | — |
| LEDGER_ID | LedgerLedgerId | — |
| NAME | LedgerName | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| SHORT_NAME | LedgerShortName | — |

### [[ledgerextractpvo|LedgerExtractPVO]] (OTHER · BICC: 73/99)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | ✅ |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | ✅ |
| AP_DOC_SEQUENCING_OPTION_FLAG | LedgerApDocSequencingOptionFlag | ✅ |
| AR_DOC_SEQUENCING_OPTION_FLAG | LedgerArDocSequencingOptionFlag | ✅ |
| ATTRIBUTE1 | LedgerAttribute1 | — |
| ATTRIBUTE10 | LedgerAttribute10 | — |
| ATTRIBUTE11 | LedgerAttribute11 | — |
| ATTRIBUTE12 | LedgerAttribute12 | — |
| ATTRIBUTE13 | LedgerAttribute13 | — |
| ATTRIBUTE14 | LedgerAttribute14 | — |
| ATTRIBUTE15 | LedgerAttribute15 | — |
| ATTRIBUTE2 | LedgerAttribute2 | — |
| ATTRIBUTE3 | LedgerAttribute3 | — |
| ATTRIBUTE4 | LedgerAttribute4 | — |
| ATTRIBUTE5 | LedgerAttribute5 | — |
| ATTRIBUTE6 | LedgerAttribute6 | — |
| ATTRIBUTE7 | LedgerAttribute7 | — |
| ATTRIBUTE8 | LedgerAttribute8 | — |
| ATTRIBUTE9 | LedgerAttribute9 | — |
| ATTRIBUTE_CATEGORY | LedgerAttributeCategory | — |
| ATTRIBUTE_DATE1 | LedgerAttributeDate1 | — |
| ATTRIBUTE_DATE2 | LedgerAttributeDate2 | — |
| ATTRIBUTE_DATE3 | LedgerAttributeDate3 | — |
| ATTRIBUTE_DATE4 | LedgerAttributeDate4 | — |
| ATTRIBUTE_DATE5 | LedgerAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | LedgerAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | LedgerAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | LedgerAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | LedgerAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | LedgerAttributeNumber5 | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | LedgerAutomateSecJrnlRevFlag | ✅ |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | ✅ |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | ✅ |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | ✅ |
| BAL_SEG_VALUE_SET_ID | LedgerBalSegValueSetId | ✅ |
| CHART_OF_ACCOUNTS_ID | LedgerChartOfAccountsId | ✅ |
| COMPLETE_FLAG | LedgerCompleteFlag | ✅ |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | ✅ |
| CONFIGURATION_ID | LedgerConfigurationId | ✅ |
| CREATED_BY | LedgerCreatedBy | ✅ |
| CREATION_DATE | LedgerCreationDate | ✅ |
| CRITERIA_SET_ID | LedgerCriteriaSetId | ✅ |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerCumTransCodeCombinationId | ✅ |
| CURRENCY_CODE | LedgerCurrencyCode | ✅ |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | ✅ |
| DESCRIPTION | LedgerDescription | ✅ |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | ✅ |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | ✅ |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | ✅ |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | ✅ |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | ✅ |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | ✅ |
| ENF_SEQ_DATE_CORRELATION_CODE | LedgerEnfSeqDateCorrelationCode | ✅ |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | ✅ |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | ✅ |
| IMPLICIT_ACCESS_SET_ID | LedgerImplicitAccessSetId | ✅ |
| INTERCO_GAIN_LOSS_CCID | LedgerIntercoGainLossCcid | ✅ |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | ✅ |
| LAST_UPDATE_DATE | LedgerLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LedgerLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LedgerLastUpdatedBy | ✅ |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | ✅ |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | ✅ |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | ✅ |
| LEDGER_ID | LedgerLedgerId | ✅ |
| MINIMUM_THRESHOLD_AMOUNT | LedgerMinimumThresholdAmount | ✅ |
| NAME | LedgerName | ✅ |
| NET_CLOSING_BAL_FLAG | LedgerNetClosingBalFlag | ✅ |
| NET_INCOME_CODE_COMBINATION_ID | LedgerNetIncomeCodeCombinationId | ✅ |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | ✅ |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | ✅ |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | ✅ |
| PERIOD_SET_NAME | LedgerPeriodSetName | ✅ |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | ✅ |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | ✅ |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | ✅ |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerResEncumbCodeCombinationId | ✅ |
| RET_EARN_CODE_COMBINATION_ID | LedgerRetEarnCodeCombinationId | ✅ |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | ✅ |
| ROUNDING_CODE_COMBINATION_ID | LedgerRoundingCodeCombinationId | ✅ |
| SEQUENCING_MODE_CODE | LedgerSequencingModeCode | ✅ |
| SHORT_NAME | LedgerShortName | ✅ |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | ✅ |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | ✅ |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | ✅ |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | ✅ |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerSlaEnteredCurBalSusCcid | ✅ |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | ✅ |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerSlaLedgerCurBalSusCcid | ✅ |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | ✅ |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | ✅ |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | ✅ |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | ✅ |
| TRANSACTION_CALENDAR_ID | LedgerTransactionCalendarId | ✅ |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | ✅ |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | ✅ |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | ✅ |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | ✅ |

### [[ledgerpvo|LedgerPVO]] (GL · BICC: 18/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | ✅ |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | ✅ |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | ✅ |
| BAL_SEG_VALUE_SET_ID | LedgerBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerChartOfAccountsId | ✅ |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CREATED_BY | LedgerCreatedBy | ✅ |
| CREATION_DATE | LedgerCreationDate | ✅ |
| CRITERIA_SET_ID | LedgerCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerCurrencyCode | ✅ |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | ✅ |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | LedgerIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LedgerLastUpdateLogin | — |
| LAST_UPDATED_BY | LedgerLastUpdatedBy | ✅ |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | ✅ |
| LEDGER_ID | LedgerId | ✅ |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerMgtSegValueSetId | — |
| NAME | LedgerName | ✅ |
| NET_INCOME_CODE_COMBINATION_ID | LedgerNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | ✅ |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerRoundingCodeCombinationId | — |
| SHORT_NAME | LedgerShortName | ✅ |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | ✅ |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | ✅ |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | ✅ |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL · BICC: 8/158)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerSetAccountedPeriodType | — |
| ACCOUNTED_PERIOD_TYPE | LedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerSetAlcLedgerTypeCode | — |
| ALC_LEDGER_TYPE_CODE | LedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerSetAllowIntercompanyPostFlag | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgersAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerSetAutomaticallyCreatedFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerSetAutorevAfterOpenPrdFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerSetBalSegColumnName | — |
| BAL_SEG_COLUMN_NAME | LedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerSetBalSegValueOptionCode | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | LedgerSetBalSegValueSetId | — |
| BAL_SEG_VALUE_SET_ID | LedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerSetBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerSetBudgetPeriodEndRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | LedgerSetChartOfAccountsId | — |
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| COMPLETE_FLAG | LedgerSetCompleteFlag | — |
| COMPLETE_FLAG | LedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerSetCompletionStatusCode | — |
| COMPLETION_STATUS_CODE | LedgersCompletionStatusCode | — |
| CONFIGURATION_ID | LedgerSetConfigurationId | — |
| CONFIGURATION_ID | LedgersConfigurationId | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerSetConsolidationLedgerFlag | — |
| CONSOLIDATION_LEDGER_FLAG | LedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerSetCreateJeFlag | — |
| CREATE_JE_FLAG | LedgersCreateJeFlag | — |
| CREATED_BY | LedgerSetCreatedBy | — |
| CREATED_BY | LedgersCreatedBy | ✅ |
| CREATION_DATE | LedgerSetCreationDate | ✅ |
| CREATION_DATE | LedgersCreationDate | — |
| CRITERIA_SET_ID | LedgerSetCriteriaSetId | — |
| CRITERIA_SET_ID | LedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgerSetCumTransCodeCombinationId | — |
| CUM_TRANS_CODE_COMBINATION_ID | LedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | LedgerSetCurrencyCode | — |
| CURRENCY_CODE | LedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerSetDailyTranslationRateType | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgersDailyTranslationRateType | — |
| DESCRIPTION | LedgerSetDescription | — |
| DESCRIPTION | LedgersDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerSetEnableAutomaticTaxFlag | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerSetEnableAverageBalancesFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerSetEnableBudgetaryControlFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerSetEnableJeApprovalFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerSetEnableReconciliationFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerSetEnableRevalSsTrackFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerSetEnableSecondaryTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgersEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerSetFirstLedgerPeriodName | — |
| FIRST_LEDGER_PERIOD_NAME | LedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerSetFutureEnterablePeriodsLimit | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | LedgerSetImplicitAccessSetId | — |
| IMPLICIT_ACCESS_SET_ID | LedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgerSetImplicitLedgerSetId | — |
| IMPLICIT_LEDGER_SET_ID | LedgersImplicitLedgerSetId | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerSetJrnlsGroupByDateFlag | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgersJrnlsGroupByDateFlag | — |
| LAST_UPDATE_DATE | LedgerSetLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | LedgersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LedgerSetLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | LedgersLastUpdateLogin | — |
| LAST_UPDATED_BY | LedgerSetLastUpdatedBy | — |
| LAST_UPDATED_BY | LedgersLastUpdatedBy | ✅ |
| LATEST_ENCUMBRANCE_YEAR | LedgerSetLatestEncumbranceYear | — |
| LATEST_ENCUMBRANCE_YEAR | LedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerSetLatestOpenedPeriodName | — |
| LATEST_OPENED_PERIOD_NAME | LedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerSetLeLedgerTypeCode | — |
| LE_LEDGER_TYPE_CODE | LedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerSetLedgerAttributes | — |
| LEDGER_ATTRIBUTES | LedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerSetLedgerCategoryCode | — |
| LEDGER_CATEGORY_CODE | LedgersLedgerCategoryCode | — |
| LEDGER_ID | LedgerId | ✅ |
| LEDGER_ID | LedgerSetLedgerId | ✅ |
| MGT_SEG_COLUMN_NAME | LedgerSetMgtSegColumnName | — |
| MGT_SEG_COLUMN_NAME | LedgersMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerSetMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgersMgtSegValueOptionCode | — |
| MGT_SEG_VALUE_SET_ID | LedgerSetMgtSegValueSetId | — |
| MGT_SEG_VALUE_SET_ID | LedgersMgtSegValueSetId | — |
| NAME | LedgerSetName | ✅ |
| NAME | LedgersName | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgerSetNetIncomeCodeCombinationId | — |
| NET_INCOME_CODE_COMBINATION_ID | LedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | LedgerSetObjectTypeCode | — |
| OBJECT_TYPE_CODE | LedgersObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerSetObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | LedgersObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerSetPeriodAverageRateType | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerSetPeriodEndRateType | — |
| PERIOD_END_RATE_TYPE | LedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerSetPeriodSetName | — |
| PERIOD_SET_NAME | LedgersPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerSetPopUpStatAccountFlag | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgersPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerSetPriorPrdNotificationFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgersPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerSetRequireBudgetJournalsFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgersRequireBudgetJournalsFlag | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgerSetResEncumbCodeCombinationId | — |
| RES_ENCUMB_CODE_COMBINATION_ID | LedgersResEncumbCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgerSetRetEarnCodeCombinationId | — |
| RET_EARN_CODE_COMBINATION_ID | LedgersRetEarnCodeCombinationId | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerSetRevalFromPriLgrCurr | — |
| REVAL_FROM_PRI_LGR_CURR | LedgersRevalFromPriLgrCurr | — |
| ROUNDING_CODE_COMBINATION_ID | LedgerSetRoundingCodeCombinationId | — |
| ROUNDING_CODE_COMBINATION_ID | LedgersRoundingCodeCombinationId | — |
| SHORT_NAME | LedgerSetShortName | — |
| SHORT_NAME | LedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSetSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSetSlaAccountingMethodType | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSetSlaBalByLedgerCurrFlag | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgersSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSetSlaDescriptionLanguage | — |
| SLA_DESCRIPTION_LANGUAGE | LedgersSlaDescriptionLanguage | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgerSetSlaEnteredCurBalSusCcid | — |
| SLA_ENTERED_CUR_BAL_SUS_CCID | LedgersSlaEnteredCurBalSusCcid | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSetSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgersSlaLedgerCashBasisFlag | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgerSetSlaLedgerCurBalSusCcid | — |
| SLA_LEDGER_CUR_BAL_SUS_CCID | LedgersSlaLedgerCurBalSusCcid | — |
| SLA_SEQUENCING_FLAG | LedgerSetSlaSequencingFlag | — |
| SLA_SEQUENCING_FLAG | LedgersSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSetSuspenseAllowedFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgersSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerSetThresholdAmount | — |
| THRESHOLD_AMOUNT | LedgersThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerSetTrackRoundingImbalanceFlag | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgersTrackRoundingImbalanceFlag | — |
| TRANSACTION_CALENDAR_ID | LedgerSetTransactionCalendarId | — |
| TRANSACTION_CALENDAR_ID | LedgersTransactionCalendarId | — |
| TRANSLATE_EOD_FLAG | LedgerSetTranslateEodFlag | — |
| TRANSLATE_EOD_FLAG | LedgersTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerSetTranslateQatdFlag | — |
| TRANSLATE_QATD_FLAG | LedgersTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerSetTranslateYatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgersTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerSetUssglOptionCode | — |
| USSGL_OPTION_CODE | LedgersUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerSetValidateJournalRefDate | — |
| VALIDATE_JOURNAL_REF_DATE | LedgersValidateJournalRefDate | — |

### [[legalentityprimaryledgerpvo|LegalEntityPrimaryLedgerPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgersArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgersAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| COMPLETE_FLAG | GlLedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode1 | — |
| CONFIGURATION_ID | GlLedgersConfigurationId2 | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | — |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | GlLedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | — |
| DESCRIPTION | GlLedgersDescription1 | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgersEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | — |
| LEDGER_ID | LedgerId | — |
| NAME | GlLedgersName | — |
| NET_CLOSING_BAL_FLAG | GlLedgersNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | — |
| SHORT_NAME | GlLedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | — |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | — |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | — |

### [[legalentitypvo|LegalEntityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | — |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | — |
| AR_DOC_SEQUENCING_OPTION_FLAG | GlLedgersArDocSequencingOptionFlag | — |
| AUTOMATE_SEC_JRNL_REV_FLAG | GlLedgersAutomateSecJrnlRevFlag | — |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | — |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | — |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| COMPLETE_FLAG | GlLedgersCompleteFlag | — |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode1 | — |
| CONFIGURATION_ID | GlLedgersConfigurationId2 | — |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | — |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | — |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | — |
| CURRENCY_CODE | GlLedgersCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | — |
| DESCRIPTION | GlLedgersDescription1 | — |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | — |
| ENF_SEQ_DATE_CORRELATION_CODE | GlLedgersEnfSeqDateCorrelationCode | — |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | — |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | — |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | — |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | — |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | — |
| LEDGER_ID | LedgerId | — |
| NAME | GlLedgersName | — |
| NET_CLOSING_BAL_FLAG | GlLedgersNetClosingBalFlag | — |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | — |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | — |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | — |
| SHORT_NAME | GlLedgersShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | — |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | — |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | — |

### [[manualpriceadjustment|ManualPriceAdjustment]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 59/59)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | ✅ |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | ✅ |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | ✅ |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | ✅ |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | ✅ |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | ✅ |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | ✅ |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | ✅ |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | ✅ |
| COMPLETE_FLAG | LedgerCompleteFlag | ✅ |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | ✅ |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | ✅ |
| CREATE_JE_FLAG | LedgerCreateJeFlag | ✅ |
| CURRENCY_CODE | LedgerCurrencyCode | ✅ |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | ✅ |
| DESCRIPTION | LedgerDescription | ✅ |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | ✅ |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | ✅ |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | ✅ |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | ✅ |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | ✅ |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | ✅ |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | ✅ |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | ✅ |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | ✅ |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | ✅ |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | ✅ |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | ✅ |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | ✅ |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | ✅ |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | ✅ |
| LEDGER_ID | LedgerLedgerId | ✅ |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | ✅ |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | ✅ |
| NAME | LedgerName | ✅ |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | ✅ |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | ✅ |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | ✅ |
| PERIOD_SET_NAME | LedgerPeriodSetName | ✅ |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | ✅ |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | ✅ |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | ✅ |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | ✅ |
| SHORT_NAME | LedgerShortName | ✅ |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | ✅ |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | ✅ |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | ✅ |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | ✅ |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | ✅ |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | ✅ |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | ✅ |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | ✅ |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | ✅ |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | ✅ |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | ✅ |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | ✅ |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | ✅ |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | ✅ |

### [[orderchargecomponent|OrderChargeComponent]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotal|OrderTotal]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotaldiscount|OrderTotalDiscount]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotalforcredit|OrderTotalForCredit]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotallistprice|OrderTotalListPrice]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotalnetprice|OrderTotalNetPrice]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotalpaynow|OrderTotalPayNow]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotalshipcharge|OrderTotalShipCharge]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[ordertotaltax|OrderTotalTax]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENCY_CODE | LedgerCurrencyCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| NAME | LedgersName | ✅ |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[payablesreconciliationsummarypvo|PayablesReconciliationSummaryPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| NAME | LedgersName | ✅ |

### [[perfobligationlindistspvo|PerfObligationLinDistsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[perfobligationlinespvo|PerfObligationLinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[perfobligationspvo|PerfObligationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| CREATED_BY | GlLedgersCreatedBy | — |
| CREATION_DATE | GlLedgersCreationDate | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName | — |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[pjsactualcostsp1|PjsActualCostsP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersPEOAccPeriodType | — |
| LEDGER_ID | GlLedgersPEOLedgerId | — |
| OBJECT_VERSION_NUMBER | GlLedgersPEOObjVerNumber | — |
| PERIOD_SET_NAME | GlLedgersPEOPeriodSetName | — |

### [[pjscommitmentcostsp1|PjsCommitmentCostsP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgerPEOAccPeriodType | — |
| LEDGER_ID | GlLedgerPEOLedgerId | — |
| OBJECT_VERSION_NUMBER | GlLedgerPEOObjectVersionNumber | — |
| PERIOD_SET_NAME | GlLedgerPEOPeriodSetName | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgerInvDistChartOfAccountsId | — |
| LEDGER_ID | LedgerInvDistLedgerId | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgersObjectVersionNumber | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | LedgerAccountedPeriodType | — |
| ALC_LEDGER_TYPE_CODE | LedgerAlcLedgerTypeCode | — |
| ALLOW_INTERCOMPANY_POST_FLAG | LedgerAllowIntercompanyPostFlag | — |
| AUTOMATICALLY_CREATED_FLAG | LedgerAutomaticallyCreatedFlag | — |
| AUTOREV_AFTER_OPEN_PRD_FLAG | LedgerAutorevAfterOpenPrdFlag | — |
| BAL_SEG_COLUMN_NAME | LedgerBalSegColumnName | — |
| BAL_SEG_VALUE_OPTION_CODE | LedgerBalSegValueOptionCode | — |
| BUDGET_PERIOD_AVG_RATE_TYPE | LedgerBudgetPeriodAvgRateType | — |
| BUDGET_PERIOD_END_RATE_TYPE | LedgerBudgetPeriodEndRateType | — |
| COMPLETE_FLAG | LedgerCompleteFlag | — |
| COMPLETION_STATUS_CODE | LedgerCompletionStatusCode | — |
| CONSOLIDATION_LEDGER_FLAG | LedgerConsolidationLedgerFlag | — |
| CREATE_JE_FLAG | LedgerCreateJeFlag | — |
| CURRENCY_CODE | LedgerCurrencyCode | — |
| DAILY_TRANSLATION_RATE_TYPE | LedgerDailyTranslationRateType | — |
| DESCRIPTION | LedgerDescription | — |
| ENABLE_AUTOMATIC_TAX_FLAG | LedgerEnableAutomaticTaxFlag | — |
| ENABLE_AVERAGE_BALANCES_FLAG | LedgerEnableAverageBalancesFlag | — |
| ENABLE_BUDGETARY_CONTROL_FLAG | LedgerEnableBudgetaryControlFlag | — |
| ENABLE_JE_APPROVAL_FLAG | LedgerEnableJeApprovalFlag | — |
| ENABLE_RECONCILIATION_FLAG | LedgerEnableReconciliationFlag | — |
| ENABLE_REVAL_SS_TRACK_FLAG | LedgerEnableRevalSsTrackFlag | — |
| ENABLE_SECONDARY_TRACK_FLAG | LedgerEnableSecondaryTrackFlag | — |
| FIRST_LEDGER_PERIOD_NAME | LedgerFirstLedgerPeriodName | — |
| FUTURE_ENTERABLE_PERIODS_LIMIT | LedgerFutureEnterablePeriodsLimit | — |
| JRNLS_GROUP_BY_DATE_FLAG | LedgerJrnlsGroupByDateFlag | — |
| LATEST_ENCUMBRANCE_YEAR | LedgerLatestEncumbranceYear | — |
| LATEST_OPENED_PERIOD_NAME | LedgerLatestOpenedPeriodName | — |
| LE_LEDGER_TYPE_CODE | LedgerLeLedgerTypeCode | — |
| LEDGER_ATTRIBUTES | LedgerLedgerAttributes | — |
| LEDGER_CATEGORY_CODE | LedgerLedgerCategoryCode | — |
| LEDGER_ID | LedgerLedgerId | — |
| MGT_SEG_COLUMN_NAME | LedgerMgtSegColumnName | — |
| MGT_SEG_VALUE_OPTION_CODE | LedgerMgtSegValueOptionCode | — |
| NAME | LedgerName | — |
| OBJECT_TYPE_CODE | LedgerObjectTypeCode | — |
| OBJECT_VERSION_NUMBER | LedgerObjectVersionNumber | — |
| PERIOD_AVERAGE_RATE_TYPE | LedgerPeriodAverageRateType | — |
| PERIOD_END_RATE_TYPE | LedgerPeriodEndRateType | — |
| PERIOD_SET_NAME | LedgerPeriodSetName | — |
| POP_UP_STAT_ACCOUNT_FLAG | LedgerPopUpStatAccountFlag | — |
| PRIOR_PRD_NOTIFICATION_FLAG | LedgerPriorPrdNotificationFlag | — |
| REQUIRE_BUDGET_JOURNALS_FLAG | LedgerRequireBudgetJournalsFlag | — |
| REVAL_FROM_PRI_LGR_CURR | LedgerRevalFromPriLgrCurr | — |
| SHORT_NAME | LedgerShortName | — |
| SLA_ACCOUNTING_METHOD_CODE | LedgerSlaAccountingMethodCode | — |
| SLA_ACCOUNTING_METHOD_TYPE | LedgerSlaAccountingMethodType | — |
| SLA_BAL_BY_LEDGER_CURR_FLAG | LedgerSlaBalByLedgerCurrFlag | — |
| SLA_DESCRIPTION_LANGUAGE | LedgerSlaDescriptionLanguage | — |
| SLA_LEDGER_CASH_BASIS_FLAG | LedgerSlaLedgerCashBasisFlag | — |
| SLA_SEQUENCING_FLAG | LedgerSlaSequencingFlag | — |
| SUSPENSE_ALLOWED_FLAG | LedgerSuspenseAllowedFlag | — |
| THRESHOLD_AMOUNT | LedgerThresholdAmount | — |
| TRACK_ROUNDING_IMBALANCE_FLAG | LedgerTrackRoundingImbalanceFlag | — |
| TRANSLATE_EOD_FLAG | LedgerTranslateEodFlag | — |
| TRANSLATE_QATD_FLAG | LedgerTranslateQatdFlag | — |
| TRANSLATE_YATD_FLAG | LedgerTranslateYatdFlag | — |
| USSGL_OPTION_CODE | LedgerUssglOptionCode | — |
| VALIDATE_JOURNAL_REF_DATE | LedgerValidateJournalRefDate | — |

### [[receivablesreconciliationsummarypvo|ReceivablesReconciliationSummaryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[referenceaccount|ReferenceAccount]] (AR · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | — |
| LEDGER_ID | GlLedgersLedgerId | — |
| NAME | GlLedgersName | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | — |

### [[revenueadjustmentdistributionpvo|RevenueAdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[subledgercontrolbalancepvo|SubledgerControlBalancePVO]] (GL · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | ✅ |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | ✅ |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | ✅ |
| AP_DOC_SEQUENCING_OPTION_FLAG | GlLedgersApDocSequencingOptionFlag | ✅ |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | ✅ |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | ✅ |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | ✅ |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | ✅ |
| CONFIGURATION_ID | GlLedgersConfigurationId | ✅ |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | ✅ |
| CURRENCY_CODE | GlLedgersCurrencyCode | ✅ |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | ✅ |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | ✅ |
| LEDGER_ID | GlLedgersLedgerId | ✅ |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | ✅ |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | ✅ |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| CURRENCY_CODE | LedgersCurrencyCode | — |
| LEDGER_ID | LedgersLedgerId | ✅ |
| NAME | LedgersName | — |

### [[suppliersiteassignmentspvo|SupplierSiteAssignmentsPVO]] (PO · BICC: 80/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlLedgersAccountedPeriodType | ✅ |
| ALC_LEDGER_TYPE_CODE | GlLedgersAlcLedgerTypeCode | ✅ |
| ALLOW_INTERCOMPANY_POST_FLAG | GlLedgersAllowIntercompanyPostFlag | ✅ |
| AUTOMATICALLY_CREATED_FLAG | GlLedgersAutomaticallyCreatedFlag | ✅ |
| AUTOREV_AFTER_OPEN_PRD_FLAG | GlLedgersAutorevAfterOpenPrdFlag | ✅ |
| BAL_SEG_COLUMN_NAME | GlLedgersBalSegColumnName | ✅ |
| BAL_SEG_VALUE_OPTION_CODE | GlLedgersBalSegValueOptionCode | ✅ |
| BAL_SEG_VALUE_SET_ID | GlLedgersBalSegValueSetId | ✅ |
| BUDGET_PERIOD_AVG_RATE_TYPE | GlLedgersBudgetPeriodAvgRateType | ✅ |
| BUDGET_PERIOD_END_RATE_TYPE | GlLedgersBudgetPeriodEndRateType | ✅ |
| CHART_OF_ACCOUNTS_ID | GlLedgersChartOfAccountsId | ✅ |
| COMPLETE_FLAG | GlLedgersCompleteFlag | ✅ |
| COMPLETION_STATUS_CODE | GlLedgersCompletionStatusCode | ✅ |
| CONFIGURATION_ID | GlLedgersConfigurationId | ✅ |
| CONSOLIDATION_LEDGER_FLAG | GlLedgersConsolidationLedgerFlag | ✅ |
| CREATE_JE_FLAG | GlLedgersCreateJeFlag | ✅ |
| CREATED_BY | GlLedgersCreatedBy | ✅ |
| CREATION_DATE | GlLedgersCreationDate | ✅ |
| CRITERIA_SET_ID | GlLedgersCriteriaSetId | ✅ |
| CUM_TRANS_CODE_COMBINATION_ID | GlLedgersCumTransCodeCombinationId | ✅ |
| CURRENCY_CODE | GlLedgersCurrencyCode | ✅ |
| DAILY_TRANSLATION_RATE_TYPE | GlLedgersDailyTranslationRateType | ✅ |
| DESCRIPTION | GlLedgersDescription | ✅ |
| ENABLE_AUTOMATIC_TAX_FLAG | GlLedgersEnableAutomaticTaxFlag | ✅ |
| ENABLE_AVERAGE_BALANCES_FLAG | GlLedgersEnableAverageBalancesFlag | ✅ |
| ENABLE_BUDGETARY_CONTROL_FLAG | GlLedgersEnableBudgetaryControlFlag | ✅ |
| ENABLE_JE_APPROVAL_FLAG | GlLedgersEnableJeApprovalFlag | ✅ |
| ENABLE_RECONCILIATION_FLAG | GlLedgersEnableReconciliationFlag | ✅ |
| ENABLE_REVAL_SS_TRACK_FLAG | GlLedgersEnableRevalSsTrackFlag | ✅ |
| ENABLE_SECONDARY_TRACK_FLAG | GlLedgersEnableSecondaryTrackFlag | ✅ |
| FIRST_LEDGER_PERIOD_NAME | GlLedgersFirstLedgerPeriodName | ✅ |
| FUTURE_ENTERABLE_PERIODS_LIMIT | GlLedgersFutureEnterablePeriodsLimit | ✅ |
| IMPLICIT_ACCESS_SET_ID | GlLedgersImplicitAccessSetId | ✅ |
| IMPLICIT_LEDGER_SET_ID | GlLedgersImplicitLedgerSetId | ✅ |
| INTERCO_GAIN_LOSS_CCID | GlLedgersIntercoGainLossCcid | ✅ |
| JRNLS_GROUP_BY_DATE_FLAG | GlLedgersJrnlsGroupByDateFlag | ✅ |
| LAST_UPDATE_DATE | GlLedgersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlLedgersLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlLedgersLastUpdatedBy | ✅ |
| LATEST_ENCUMBRANCE_YEAR | GlLedgersLatestEncumbranceYear | ✅ |
| LATEST_OPENED_PERIOD_NAME | GlLedgersLatestOpenedPeriodName | ✅ |
| LE_LEDGER_TYPE_CODE | GlLedgersLeLedgerTypeCode | ✅ |
| LEDGER_ATTRIBUTES | GlLedgersLedgerAttributes | ✅ |
| LEDGER_CATEGORY_CODE | GlLedgersLedgerCategoryCode | ✅ |
| LEDGER_ID | GlLedgersLedgerId | ✅ |
| MGT_SEG_COLUMN_NAME | GlLedgersMgtSegColumnName | ✅ |
| MGT_SEG_VALUE_OPTION_CODE | GlLedgersMgtSegValueOptionCode | ✅ |
| MGT_SEG_VALUE_SET_ID | GlLedgersMgtSegValueSetId | ✅ |
| NAME | GlLedgersName | ✅ |
| NET_INCOME_CODE_COMBINATION_ID | GlLedgersNetIncomeCodeCombinationId | ✅ |
| OBJECT_TYPE_CODE | GlLedgersObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | GlLedgersObjectVersionNumber | ✅ |
| PERIOD_AVERAGE_RATE_TYPE | GlLedgersPeriodAverageRateType | ✅ |
| PERIOD_END_RATE_TYPE | GlLedgersPeriodEndRateType | ✅ |
| PERIOD_SET_NAME | GlLedgersPeriodSetName | ✅ |
| POP_UP_STAT_ACCOUNT_FLAG | GlLedgersPopUpStatAccountFlag | ✅ |
| PRIOR_PRD_NOTIFICATION_FLAG | GlLedgersPriorPrdNotificationFlag | ✅ |
| REQUIRE_BUDGET_JOURNALS_FLAG | GlLedgersRequireBudgetJournalsFlag | ✅ |
| RES_ENCUMB_CODE_COMBINATION_ID | GlLedgersResEncumbCodeCombinationId | ✅ |
| RET_EARN_CODE_COMBINATION_ID | GlLedgersRetEarnCodeCombinationId | ✅ |
| REVAL_FROM_PRI_LGR_CURR | GlLedgersRevalFromPriLgrCurr | ✅ |
| ROUNDING_CODE_COMBINATION_ID | GlLedgersRoundingCodeCombinationId | ✅ |
| SHORT_NAME | GlLedgersShortName | ✅ |
| SLA_ACCOUNTING_METHOD_CODE | GlLedgersSlaAccountingMethodCode | ✅ |
| SLA_ACCOUNTING_METHOD_TYPE | GlLedgersSlaAccountingMethodType | ✅ |
| SLA_BAL_BY_LEDGER_CURR_FLAG | GlLedgersSlaBalByLedgerCurrFlag | ✅ |
| SLA_DESCRIPTION_LANGUAGE | GlLedgersSlaDescriptionLanguage | ✅ |
| SLA_ENTERED_CUR_BAL_SUS_CCID | GlLedgersSlaEnteredCurBalSusCcid | ✅ |
| SLA_LEDGER_CASH_BASIS_FLAG | GlLedgersSlaLedgerCashBasisFlag | ✅ |
| SLA_LEDGER_CUR_BAL_SUS_CCID | GlLedgersSlaLedgerCurBalSusCcid | ✅ |
| SLA_SEQUENCING_FLAG | GlLedgersSlaSequencingFlag | ✅ |
| SUSPENSE_ALLOWED_FLAG | GlLedgersSuspenseAllowedFlag | ✅ |
| THRESHOLD_AMOUNT | GlLedgersThresholdAmount | ✅ |
| TRACK_ROUNDING_IMBALANCE_FLAG | GlLedgersTrackRoundingImbalanceFlag | ✅ |
| TRANSACTION_CALENDAR_ID | GlLedgersTransactionCalendarId | ✅ |
| TRANSLATE_EOD_FLAG | GlLedgersTranslateEodFlag | ✅ |
| TRANSLATE_QATD_FLAG | GlLedgersTranslateQatdFlag | ✅ |
| TRANSLATE_YATD_FLAG | GlLedgersTranslateYatdFlag | ✅ |
| USSGL_OPTION_CODE | GlLedgersUssglOptionCode | ✅ |
| VALIDATE_JOURNAL_REF_DATE | GlLedgersValidateJournalRefDate | ✅ |

### [[supportingreferencebalancepvo|SupportingReferenceBalancePVO]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | ✅ |
| LEDGER_ID | LedgersLedgerId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHART_OF_ACCOUNTS_ID | LedgersChartOfAccountsId | — |
| LEDGER_ID | LedgersLedgerId | — |
| OBJECT_VERSION_NUMBER | LedgersObjectVersionNumber2 | — |

---

## 📚 Referências

- [Oracle Docs — GL_LEDGERS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glledgers-25358.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
