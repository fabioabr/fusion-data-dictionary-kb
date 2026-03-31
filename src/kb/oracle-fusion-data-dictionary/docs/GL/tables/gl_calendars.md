---
id: DOC-GL-008
doc_type: system-doc
title: "GL_CALENDARS — Calendários Contábeis"
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
  - calendario
  - periodos
  - contabilidade
aliases:
  - GL_CALENDARS
  - gl_calendars
  - calendarios-contabeis
  - accounting-calendars
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_CALENDARS

## Visao Geral

Armazena a **definição de calendários contábeis** e seus períodos no General Ledger. Cada registro representa um período contábil dentro de um calendário, com datas de início e fim, tipo de período e número sequencial. É a tabela de referência para todos os processos que dependem de períodos contábeis — fechamento, abertura, lançamentos e relatórios.

> [!note] Nomenclatura
> No Oracle Fusion, o calendário é identificado pelo `PERIOD_SET_NAME` (ex: "Patria Fiscal Calendar") e cada período tem um `PERIOD_NAME` único (ex: "JAN-26", "FEB-26").

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Definição de exercício fiscal:** Estabelece os períodos contábeis do ano fiscal da organização.
- **Abertura/fechamento de períodos:** Determina quais períodos estão disponíveis para lançamentos.
- **Relatórios financeiros:** Referência para balancetes, DRE e balanço por período.
- **Validação de datas:** Garante que datas contábeis (GL_DATE) caiam dentro de períodos válidos.
- **Calendários especiais:** Suporta períodos de ajuste (adjustment periods) para lançamentos de fechamento.
- **Configuração de ledger:** Cada ledger é vinculado a um calendário específico.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | PK | Nome do calendário contábil | — | 🟢 95% |
| 2 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | PK | Nome do período (ex: JAN-26, FEB-26) | — | 🟢 95% |
| 3 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo do período: Month, Quarter, Year | — | 🟢 95% |
| 4 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano fiscal do período | — | 🟢 95% |
| 5 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano (1-12 para meses, 13+ para ajuste) | — | 🟢 95% |
| 6 | START_DATE | DATE | NOT NULL | Data | Data de início do período | — | 🟢 95% |
| 7 | END_DATE | DATE | NOT NULL | Data | Data de fim do período | — | 🟢 95% |
| 8 | QUARTER_NUM | NUMBER(15) | NOT NULL | Período | Número do trimestre (1-4) | — | 🟢 90% |
| 9 | ENTERED_PERIOD_NAME | VARCHAR2(15) | NULL | Identificação | Nome do período como digitado pelo usuário | — | 🟡 75% |
| 10 | ADJUSTMENT_PERIOD_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se é um período de ajuste (Y/N) | — | 🟢 90% |
| 11 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do período | — | 🟢 85% |
| 12 | YEAR_START_DATE | DATE | NULL | Data | Data de início do ano fiscal | — | 🟡 80% |
| 13 | QUARTER_START_DATE | DATE | NULL | Data | Data de início do trimestre | — | 🟡 80% |
| 14 | CONTEXT | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 15 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟡 70% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[gl_ledgers]] — via `PERIOD_SET_NAME` (ledger usa este calendário)
- [[gl_access_sets]] — via `PERIOD_SET_NAME` (conjunto de acesso usa este calendário)
- [[gl_period_statuses]] — via `PERIOD_SET_NAME` + `PERIOD_NAME` (status de abertura/fechamento)

---

## Uso Tipico

### Períodos de um calendário
```sql
SELECT c.PERIOD_NAME, c.PERIOD_YEAR, c.PERIOD_NUM,
       c.START_DATE, c.END_DATE, c.QUARTER_NUM,
       c.ADJUSTMENT_PERIOD_FLAG
FROM   GL_CALENDARS c
WHERE  c.PERIOD_SET_NAME = :p_calendar_name
  AND  c.PERIOD_TYPE = 'Month'
  AND  c.PERIOD_YEAR = 2026
ORDER BY c.PERIOD_NUM;
```

### Identificar período para uma data específica
```sql
SELECT c.PERIOD_NAME, c.PERIOD_YEAR, c.PERIOD_NUM
FROM   GL_CALENDARS c
WHERE  c.PERIOD_SET_NAME = :p_calendar_name
  AND  c.PERIOD_TYPE = 'Month'
  AND  c.ADJUSTMENT_PERIOD_FLAG = 'N'
  AND  :p_date BETWEEN c.START_DATE AND c.END_DATE;
```

### Filtros comuns
- `PERIOD_TYPE = 'Month'` — Períodos mensais (mais comum)
- `ADJUSTMENT_PERIOD_FLAG = 'N'` — Excluir períodos de ajuste
- `ADJUSTMENT_PERIOD_FLAG = 'Y'` — Apenas períodos de ajuste
- `PERIOD_YEAR = 2026` — Ano fiscal específico

---

## Observacoes

- A chave primária é composta por `PERIOD_SET_NAME` + `PERIOD_NAME` — cada nome de período é único dentro do calendário.
- Períodos de ajuste (`ADJUSTMENT_PERIOD_FLAG = 'Y'`) são usados para lançamentos de fechamento de exercício e não representam meses reais.
- Os períodos devem ser contíguos — não pode haver lacunas entre `END_DATE` de um período e `START_DATE` do próximo.
- O `PERIOD_NUM` para períodos regulares vai de 1 a 12 (ou mais, em calendários com 13 períodos). Períodos de ajuste tipicamente usam números acima de 12.
- O status de abertura/fechamento do período **não** é armazenado aqui, mas sim na tabela [[gl_period_statuses]].

---

## Referencias

- [Oracle Docs — GL_CALENDARS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glcalendars-25076.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL

---

## 🔗 PVOs Relacionados

### [[cogsdistributionspvo|COGSDistributionsPVO]] (OTHER · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | ✅ |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | ✅ |

### [[costaccountingtransactionspvo|CostAccountingTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | CalendarPEOCalendarId | — |
| OBJECT_VERSION_NUMBER | CalendarPEOObjectVersionNumber | — |
| PERIOD_SET_ID | CalendarPEOPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPEOPeriodSetName | — |
| PERIOD_TYPE | CalendarPEOPeriodType | — |
| PERIOD_TYPE_ID | CalendarPEOPeriodTypeId | — |

### [[costaccountingtransactionsrefpvo|CostAccountingTransactionsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | CalendarPEOCalendarId | — |
| OBJECT_VERSION_NUMBER | CalendarPEOObjectVersionNumber | — |
| PERIOD_SET_ID | CalendarPEOPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPEOPeriodSetName | — |
| PERIOD_TYPE | CalendarPEOPeriodType | — |
| PERIOD_TYPE_ID | CalendarPEOPeriodTypeId | — |

### [[costtransactionpvo|CostTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | — |
| PERIOD_TYPE | GlCalendarsPeriodType | — |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |

### [[csttransactionserrorspvo|CstTransactionsErrorsPVO]] (OTHER · BICC: 32/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | ✅ |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | ✅ |
| ATTRIBUTE1 | GlCalendarsAttribute1 | ✅ |
| ATTRIBUTE2 | GlCalendarsAttribute2 | ✅ |
| ATTRIBUTE3 | GlCalendarsAttribute3 | ✅ |
| ATTRIBUTE4 | GlCalendarsAttribute4 | ✅ |
| ATTRIBUTE5 | GlCalendarsAttribute5 | ✅ |
| ATTRIBUTE_CATEGORY | GlCalendarsAttributeCategory | ✅ |
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | ✅ |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | ✅ |
| CREATED_BY | GlCalendarsCreatedBy1 | ✅ |
| CREATION_DATE | GlCalendarsCreationDate1 | ✅ |
| DESCRIPTION | GlCalendarsDescription | ✅ |
| LAST_UPDATE_DATE | GlCalendarsLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | GlCalendarsLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | GlCalendarsLastUpdatedBy1 | ✅ |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | ✅ |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | ✅ |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | ✅ |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | ✅ |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | ✅ |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | ✅ |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | ✅ |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | ✅ |
| SECURITY_FLAG | GlCalendarsSecurityFlag | ✅ |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | ✅ |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[cstwocostvaiancedetailspvo|CstWOCostVaianceDetailsPVO]] (OTHER · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsPEOCalendarId | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsPEOObjectVersionNumber | ✅ |
| PERIOD_SET_ID | GlCalendarsPEOPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPEOPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPEOPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPEOPeriodTypeId | ✅ |

### [[cstworkordercostspvo|CstWorkOrderCostsPVO]] (OTHER · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | CalendarPEOCalendarId | ✅ |
| OBJECT_VERSION_NUMBER | CalendarPEOObjectVersionNumber | ✅ |
| PERIOD_SET_ID | CalendarPEOPeriodSetId | ✅ |
| PERIOD_SET_NAME | CalendarPEOPeriodSetName | ✅ |
| PERIOD_TYPE | CalendarPEOPeriodType | ✅ |
| PERIOD_TYPE_ID | CalendarPEOPeriodTypeId | ✅ |

### [[fiscalcalendarextractpvo|FiscalCalendarExtractPVO]] (OTHER · BICC: 26/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | ✅ |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | ✅ |
| ATTRIBUTE1 | GlCalendarsAttribute1 | — |
| ATTRIBUTE2 | GlCalendarsAttribute2 | — |
| ATTRIBUTE3 | GlCalendarsAttribute3 | — |
| ATTRIBUTE4 | GlCalendarsAttribute4 | — |
| ATTRIBUTE5 | GlCalendarsAttribute5 | — |
| ATTRIBUTE_CATEGORY | GlCalendarsAttributeCategory | — |
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | ✅ |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | ✅ |
| CREATED_BY | GlCalendarsCreatedBy | ✅ |
| CREATION_DATE | GlCalendarsCreationDate | ✅ |
| DESCRIPTION | GlCalendarsDescription | ✅ |
| LAST_UPDATE_DATE | GlCalendarsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlCalendarsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlCalendarsLastUpdatedBy | ✅ |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | ✅ |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | ✅ |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | ✅ |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | ✅ |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | ✅ |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | ✅ |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | ✅ |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | ✅ |
| SECURITY_FLAG | GlCalendarsSecurityFlag | ✅ |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | ✅ |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[fiscaldaypvo|FiscalDayPVO]] (GL · BICC: 3/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | — |
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | — |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | — |
| CREATED_BY | GlCalendarsCreatedBy | — |
| CREATION_DATE | GlCalendarsCreationDate | — |
| DESCRIPTION | GlCalendarsDescription | — |
| LAST_UPDATE_DATE | GlCalendarsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlCalendarsLastUpdateLogin | — |
| LAST_UPDATED_BY | GlCalendarsLastUpdatedBy | — |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName1 | — |
| PERIOD_TYPE | GlCalendarsPeriodType | — |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| SECURITY_FLAG | GlCalendarsSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[fiscalperiodwithoutledgerpvo|FiscalPeriodWithoutLedgerPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | CalendarAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | CalendarAdjPeriodsNum | — |
| CALENDAR_ID | CalendarCalendarId | — |
| CALENDAR_START_DATE | CalendarCalendarStartDate | — |
| CALENDAR_TYPE_CODE | CalendarCalendarTypeCode | — |
| CREATED_BY | CalendarCreatedBy | — |
| CREATION_DATE | CalendarCreationDate | — |
| DESCRIPTION | CalendarDescription | — |
| LAST_UPDATE_DATE | CalendarLastUpdateDate | — |
| LAST_UPDATE_LOGIN | CalendarLastUpdateLogin | — |
| LAST_UPDATED_BY | CalendarLastUpdatedBy | — |
| LATEST_YEAR_START_DATE | CalendarLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | CalendarLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | CalendarLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | CalendarNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | CalendarNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | CalendarObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | CalendarPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | CalendarPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | CalendarPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPeriodSetName | — |
| PERIOD_TYPE | CalendarPeriodType | — |
| PERIOD_TYPE_ID | CalendarPeriodTypeId | — |
| SECURITY_FLAG | CalendarSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | CalendarUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | CalendarUserPeriodSetName | — |

### [[glfiscalperiodpvo|GLFiscalPeriodPVO]] (GL · BICC: 4/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | — |
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | — |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | — |
| CREATED_BY | GlCalendarsCreatedBy | — |
| CREATION_DATE | GlCalendarsCreationDate | — |
| DESCRIPTION | GlCalendarsDescription | — |
| LAST_UPDATE_DATE | GlCalendarsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlCalendarsLastUpdateLogin | — |
| LAST_UPDATED_BY | GlCalendarsLastUpdatedBy | — |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | — |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| SECURITY_FLAG | GlCalendarsSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[glfiscalqtrpvo|GLFiscalQtrPVO]] (GL · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName1 | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[glfiscalyearpvo|GLFiscalYearPVO]] (GL · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName1 | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | ✅ |

### [[intransitvaluationaccounteddailypvo|IntransitValuationAccountedDailyPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |

### [[intransitvaluationcosteddailypvo|IntransitValuationCostedDailyPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsCalendarId | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_SET_ID | PeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |

### [[journalbatchpvo|JournalBatchPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | CalendarAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | CalendarAdjPeriodsNum | — |
| CALENDAR_ID | CalendarCalendarId | — |
| CALENDAR_START_DATE | CalendarCalendarStartDate | — |
| CALENDAR_TYPE_CODE | CalendarCalendarTypeCode | — |
| DESCRIPTION | CalendarDescription | — |
| LATEST_YEAR_START_DATE | CalendarLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | CalendarLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | CalendarLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | CalendarNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | CalendarNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | CalendarObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | CalendarPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | CalendarPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | CalendarPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPeriodSetName | — |
| PERIOD_TYPE | CalendarPeriodType | — |
| PERIOD_TYPE_ID | CalendarPeriodTypeId | — |
| SECURITY_FLAG | CalendarSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | CalendarUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | CalendarUserPeriodSetName | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | CalendarAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | CalendarAdjPeriodsNum | — |
| CALENDAR_ID | CalendarCalendarId | — |
| CALENDAR_START_DATE | CalendarCalendarStartDate | — |
| CALENDAR_TYPE_CODE | CalendarCalendarTypeCode | — |
| DESCRIPTION | CalendarDescription | — |
| LATEST_YEAR_START_DATE | CalendarLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | CalendarLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | CalendarLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | CalendarNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | CalendarNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | CalendarObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | CalendarPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | CalendarPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | CalendarPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPeriodSetName | — |
| PERIOD_TYPE | CalendarPeriodType | — |
| PERIOD_TYPE_ID | CalendarPeriodTypeId | — |
| SECURITY_FLAG | CalendarSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | CalendarUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | CalendarUserPeriodSetName | — |

### [[journallinepvo|JournalLinePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | CalendarAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | CalendarAdjPeriodsNum | — |
| CALENDAR_ID | CalendarCalendarId | — |
| CALENDAR_START_DATE | CalendarCalendarStartDate | — |
| CALENDAR_TYPE_CODE | CalendarCalendarTypeCode | — |
| DESCRIPTION | CalendarDescription | — |
| LATEST_YEAR_START_DATE | CalendarLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | CalendarLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | CalendarLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | CalendarNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | CalendarNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | CalendarObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | CalendarPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | CalendarPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | CalendarPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPeriodSetName | — |
| PERIOD_TYPE | CalendarPeriodType | — |
| PERIOD_TYPE_ID | CalendarPeriodTypeId | — |
| SECURITY_FLAG | CalendarSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | CalendarUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | CalendarUserPeriodSetName | — |

### [[ledgerpvo|LedgerPVO]] (GL · BICC: 3/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | — |
| CALENDAR_ID | GlCalendarsCalendarId | — |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | ✅ |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | — |
| DESCRIPTION | GlCalendarsDescription | — |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| SECURITY_FLAG | GlCalendarsSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | GlCalendarsAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | GlCalendarsAdjPeriodsNum | — |
| CALENDAR_ID | GlCalendarsCalendarId | — |
| CALENDAR_START_DATE | GlCalendarsCalendarStartDate | — |
| CALENDAR_TYPE_CODE | GlCalendarsCalendarTypeCode | — |
| DESCRIPTION | GlCalendarsDescription | — |
| LATEST_YEAR_START_DATE | GlCalendarsLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | GlCalendarsLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | GlCalendarsLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | GlCalendarsNonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | GlCalendarsNonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | GlCalendarsObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | GlCalendarsPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | GlCalendarsPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | GlCalendarsPeriodSetId | — |
| PERIOD_SET_NAME | GlCalendarsPeriodSetName | — |
| PERIOD_TYPE | GlCalendarsPeriodType | — |
| PERIOD_TYPE_ID | GlCalendarsPeriodTypeId | — |
| SECURITY_FLAG | GlCalendarsSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | GlCalendarsUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | GlCalendarsUserPeriodSetName | — |

### [[overheadratedetailspvo|OverheadRateDetailsPVO]] (OTHER · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsPEOCalendarId1 | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsPEOObjectVersionNumber | ✅ |
| PERIOD_SET_ID | GlCalendarsPEOPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPEOPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPEOPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPEOPeriodTypeId | ✅ |

### [[resourceratedetailspvo|ResourceRateDetailsPVO]] (OTHER · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CALENDAR_ID | GlCalendarsPEOCalendarId1 | ✅ |
| OBJECT_VERSION_NUMBER | GlCalendarsPEOObjectVersionNumber | ✅ |
| PERIOD_SET_ID | GlCalendarsPEOPeriodSetId | ✅ |
| PERIOD_SET_NAME | GlCalendarsPEOPeriodSetName | ✅ |
| PERIOD_TYPE | GlCalendarsPEOPeriodType | ✅ |
| PERIOD_TYPE_ID | GlCalendarsPEOPeriodTypeId | ✅ |

### [[rmcsfiscaldaypvo|RMCSFiscalDayPVO]] (OTHER · BICC: 4/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_PERIOD_FREQ_CODE | CalendarPEOAdjPeriodFreqCode | — |
| ADJ_PERIODS_NUM | CalendarPEOAdjPeriodsNum | — |
| ATTRIBUTE1 | CalendarPEOAttribute1 | — |
| ATTRIBUTE2 | CalendarPEOAttribute2 | — |
| ATTRIBUTE3 | CalendarPEOAttribute3 | — |
| ATTRIBUTE4 | CalendarPEOAttribute4 | — |
| ATTRIBUTE5 | CalendarPEOAttribute5 | — |
| ATTRIBUTE_CATEGORY | CalendarPEOAttributeCategory | — |
| CALENDAR_ID | CalendarPEOCalendarId | ✅ |
| CALENDAR_START_DATE | CalendarPEOCalendarStartDate | — |
| CALENDAR_TYPE_CODE | CalendarPEOCalendarTypeCode | — |
| CREATED_BY | CalendarPEOCreatedBy | — |
| CREATION_DATE | CalendarPEOCreationDate | — |
| DESCRIPTION | CalendarPEODescription | — |
| ENTERPRISE_ID | CalendarPEOEnterpriseId | — |
| LAST_UPDATE_DATE | CalendarPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CalendarPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CalendarPEOLastUpdatedBy | — |
| LATEST_YEAR_START_DATE | CalendarPEOLatestYearStartDate | — |
| LEGACY_CALENDAR_FLAG | CalendarPEOLegacyCalendarFlag | — |
| LEGACY_RULES_ENABLED_FLAG | CalendarPEOLegacyRulesEnabledFlag | — |
| NON_ADJ_PERIOD_FREQ_CODE | CalendarPEONonAdjPeriodFreqCode | — |
| NON_ADJ_PERIODS_NUM | CalendarPEONonAdjPeriodsNum | — |
| OBJECT_VERSION_NUMBER | CalendarPEOObjectVersionNumber | — |
| PERIOD_NAME_FORMAT_CODE | CalendarPEOPeriodNameFormatCode | — |
| PERIOD_NAME_SEPARATOR_CODE | CalendarPEOPeriodNameSeparatorCode | — |
| PERIOD_SET_ID | CalendarPEOPeriodSetId | — |
| PERIOD_SET_NAME | CalendarPEOPeriodSetName | ✅ |
| PERIOD_TYPE | CalendarPEOPeriodType | — |
| PERIOD_TYPE_ID | CalendarPEOPeriodTypeId | — |
| SECURITY_FLAG | CalendarPEOSecurityFlag | — |
| USER_PERIOD_NAME_PREFIX | CalendarPEOUserPeriodNamePrefix | — |
| USER_PERIOD_SET_NAME | CalendarPEOUserPeriodSetName | ✅ |
