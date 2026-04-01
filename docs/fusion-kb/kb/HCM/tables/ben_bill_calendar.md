---
id: DOC-HCM-027
doc_type: system-doc
title: "BEN_BILL_CALENDAR — Calendário de Cobrança de Benefícios"
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
  - benefits
  - calendario-cobranca
  - bill-calendar
aliases:
  - BEN_BILL_CALENDAR
  - ben_bill_calendar
  - calendario-cobranca-beneficios
  - bill-calendar
  - ben-bill-calendar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CALENDAR

## 📌 Visão Geral

Armazena os **calendários de cobrança** (billing) dos benefícios. Define os períodos e datas de cobrança para premiações e contribuições de benefícios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Calendário de Cobrança de Benefícios.
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_CALENDAR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do calendário | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do calendário de cobrança | — | 🟢 90% |
| 3 | BILLING_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência (MONTHLY, QUARTERLY, etc.) | — | 🟡 80% |
| 4 | START_DATE | DATE | NULL | Período | Data de início | — | 🟢 85% |
| 5 | END_DATE | DATE | NULL | Período | Data de fim | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charges]] — via `BILL_CALENDAR_ID` (cobrancas do calendario de faturamento)
- [[ben_bill_cycle]] — via `BILL_CALENDAR_ID` (ciclos do calendario de faturamento)

---

## 📎 Uso Típico

### Calendários de cobrança ativos
```sql
SELECT bc.BILL_CALENDAR_ID, bc.NAME, bc.BILLING_FREQUENCY
FROM   BEN_BILL_CALENDAR bc
WHERE  bc.END_DATE IS NULL OR bc.END_DATE > SYSDATE;
```

### Filtros comuns
- `END_DATE IS NULL OR END_DATE > SYSDATE` — Calendários ativos

---

## 🔒 Observações

- Define os períodos de cobrança para contribuições de benefícios.
- A frequência de cobrança pode ser mensal, trimestral, semestral ou anual.

---

## 🔗 PVOs Relacionados

### [[billcalendarpvo|BillCalendarPVO]] (HCM · BICC: 12/57)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BBC_ATTRIBUTE1 | BbcAttribute1 | — |
| BBC_ATTRIBUTE10 | BbcAttribute10 | — |
| BBC_ATTRIBUTE2 | BbcAttribute2 | — |
| BBC_ATTRIBUTE3 | BbcAttribute3 | — |
| BBC_ATTRIBUTE4 | BbcAttribute4 | — |
| BBC_ATTRIBUTE5 | BbcAttribute5 | — |
| BBC_ATTRIBUTE6 | BbcAttribute6 | — |
| BBC_ATTRIBUTE7 | BbcAttribute7 | — |
| BBC_ATTRIBUTE8 | BbcAttribute8 | — |
| BBC_ATTRIBUTE9 | BbcAttribute9 | — |
| BBC_ATTRIBUTE_CATEGORY | BbcAttributeCategory | — |
| BBC_ATTRIBUTE_DATE1 | BbcAttributeDate1 | — |
| BBC_ATTRIBUTE_DATE2 | BbcAttributeDate2 | — |
| BBC_ATTRIBUTE_DATE3 | BbcAttributeDate3 | — |
| BBC_ATTRIBUTE_DATE4 | BbcAttributeDate4 | — |
| BBC_ATTRIBUTE_DATE5 | BbcAttributeDate5 | — |
| BBC_ATTRIBUTE_NUMBER1 | BbcAttributeNumber1 | — |
| BBC_ATTRIBUTE_NUMBER2 | BbcAttributeNumber2 | — |
| BBC_ATTRIBUTE_NUMBER3 | BbcAttributeNumber3 | — |
| BBC_ATTRIBUTE_NUMBER4 | BbcAttributeNumber4 | — |
| BBC_ATTRIBUTE_NUMBER5 | BbcAttributeNumber5 | — |
| BILL_CAL_ID | BillCalId | ✅ |
| BILL_CAL_SOURCE | BillCalSource | ✅ |
| BILL_CALC_RUN | BillCalcRun | ✅ |
| BILL_CYCLE_ID | BillCalendarPEOBillCycleId | — |
| BILL_YEAR | BillYear | ✅ |
| BILLING_DATE | BillingDate | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| COMMENTS | Comments | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CONFIG_CHAR_2 | ConfigChar2 | — |
| CONFIG_CHAR_3 | ConfigChar3 | — |
| CONFIG_CHAR_4 | ConfigChar4 | — |
| CONFIG_CHAR_5 | ConfigChar5 | — |
| CONFIG_DATE_1 | ConfigDate1 | — |
| CONFIG_DATE_2 | ConfigDate2 | — |
| CONFIG_DATE_3 | ConfigDate3 | — |
| CONFIG_DATE_4 | ConfigDate4 | — |
| CONFIG_DATE_5 | ConfigDate5 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_2 | ConfigNum2 | — |
| CONFIG_NUM_3 | ConfigNum3 | — |
| CONFIG_NUM_4 | ConfigNum4 | — |
| CONFIG_NUM_5 | ConfigNum5 | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| END_DATE | EndDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PAY_TIME_PERIOD_ID | PayTimePeriodId | — |
| PAYROLL_ID | PayrollId | — |
| PERIOD_NAME | PeriodName | ✅ |
| PYMNT_DUE_DT | PymntDueDt | ✅ |
| PYMNT_OVERDUE_DT | PymntOverdueDt | ✅ |
| START_DATE | StartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CALENDAR](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcalendar.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
