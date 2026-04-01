---
id: DOC-HCM-601
doc_type: system-doc
title: "PAY_TIME_PERIOD_TYPES — Tipos de Períodos de Tempo de Pagamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - periodos-pagamento
  - time-period-types
aliases:
  - PAY_TIME_PERIOD_TYPES
  - pay_time_period_types
  - pay-time-period-types
  - tipos-de-períodos-de-tempo-de-pagamento
  - pay-time-period-type
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_TIME_PERIOD_TYPES

## 📌 Visão Geral

Armazena os **tipos de períodos de tempo** utilizados nos ciclos de folha de pagamento (payroll). Define as frequências de processamento disponíveis (mensal, quinzenal, semanal, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de frequência de pagamento** — define os ciclos disponíveis para processamento de folha.
- **Associação com folha de pagamento** — cada payroll referencia um tipo de período.
- **Geração de períodos** — base para criação automática de períodos de tempo.
- **Relatórios financeiros** — agrupamento de dados por frequência de pagamento.
- **Compliance trabalhista** — conformidade com frequências legais de pagamento.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERIOD_TYPE | VARCHAR2(30) | NOT NULL | PK | Código do tipo de período (CALENDAR_MONTH, BI_WEEK, etc.) | — | 🟢 90% |
| 2 | NUMBER_PER_FISCAL_YEAR | NUMBER(5) | NOT NULL | Configuração | Quantidade de períodos por ano fiscal | — | 🟢 85% |
| 3 | YEAR_TYPE_IN_NAME | VARCHAR2(1) | NULL | Configuração | Tipo de ano usado na nomenclatura (C=calendário, F=fiscal) | — | 🟡 70% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição legível do tipo de período | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] — via `PERIOD_TYPE` (payrolls que usam este tipo de período)

### Tabelas-filha (FK de saída)
- [[pay_time_periods]] — via `PERIOD_TYPE` (períodos gerados com base neste tipo)

---

## 📎 Uso Típico

### Tipos de período disponíveis
```sql
SELECT ptp.PERIOD_TYPE, ptp.NUMBER_PER_FISCAL_YEAR, ptp.DESCRIPTION
FROM   PAY_TIME_PERIOD_TYPES ptp
ORDER BY ptp.NUMBER_PER_FISCAL_YEAR;
```

### Filtros comuns
- `PERIOD_TYPE = 'CALENDAR_MONTH'` — Período mensal
- `NUMBER_PER_FISCAL_YEAR = 12` — Periodicidade mensal
---

## 🔒 Observações

- Tabela de referência (lookup) — registros raramente alterados.
- Os valores de `PERIOD_TYPE` são padronizados pelo Oracle e incluem: CALENDAR_MONTH, BI_WEEK, WEEK, SEMI_MONTH, LUNAR_MONTH.
- A coluna `NUMBER_PER_FISCAL_YEAR` determina quantos períodos serão gerados automaticamente para cada payroll associado.
---

## 🔗 PVOs Relacionados

### [[timeperiodtypepvo|TimePeriodTypePVO]] (HCM · BICC: 3/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TimePeriodTypePEOCreatedBy | — |
| CREATION_DATE | TimePeriodTypePEOCreationDate | — |
| DESCRIPTION | TimePeriodTypePEODescription | — |
| DISPLAY_PERIOD_TYPE | TimePeriodTypePEODisplayPeriodType | — |
| LAST_UPDATE_DATE | TimePeriodTypePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimePeriodTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TimePeriodTypePEOLastUpdatedBy | — |
| NUMBER_PER_FISCAL_YEAR | NumberPerFiscalYear | ✅ |
| OBJECT_VERSION_NUMBER | TimePeriodTypePEOObjectVersionNumber | — |
| PERIOD_TYPE | PeriodType | ✅ |
| PROGRAM_APPLICATION_ID | TimePeriodTypePEOProgramApplicationId | — |
| PROGRAM_ID | TimePeriodTypePEOProgramId | — |
| PROGRAM_UPDATE_DATE | TimePeriodTypePEOProgramUpdateDate | — |
| REQUEST_ID | TimePeriodTypePEORequestId | — |
| SYSTEM_FLAG | TimePeriodTypePEOSystemFlag | — |
| YEAR_TYPE_IN_NAME | TimePeriodTypePEOYearTypeInName | — |

---

## 📚 Referências

- [Oracle Docs — PAY_TIME_PERIOD_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paytimeperiodtypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
