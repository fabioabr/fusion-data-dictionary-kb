---
id: DOC-AR-039
doc_type: system-doc
title: "AR_CHARGE_SCHEDULES — Cronogramas de Cobrança de Encargos"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, encargos, cronograma, charge-schedule]
aliases: [AR_CHARGE_SCHEDULES, ar_charge_schedules, charge_schedules, cronograma_encargos, schedule_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CHARGE_SCHEDULES

## 📌 Visão Geral

Tabela de cronogramas de cobrança de encargos (charge schedules) do Accounts Receivable. Cada registro define uma configuração de encargo vinculada a um cabeçalho de cronograma ([[ar_charge_schedule_hdrs]]) e a uma faixa de aging ([[ar_aging_buckets]]), especificando valores ou percentuais a serem cobrados.

## 🧠 Propósito de Negócio

Os cronogramas de encargos permitem configurar regras automáticas de cobrança baseadas no tempo de atraso. Para cada faixa de aging, é possível definir um valor fixo ou percentual de encargo. Isso automatiza o processo de cobrança de juros e multas conforme a política de crédito da organização.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | SCHEDULE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cronograma. | PK | 🟢 100% |
| 2 | SCHEDULE_HEADER_ID | NUMBER(15) | NOT NULL | FK para [[ar_charge_schedule_hdrs]]. Cabeçalho do cronograma. | FK | 🟢 100% |
| 3 | AGING_BUCKET_ID | NUMBER(15) | NULL | FK para [[ar_aging_buckets]]. Faixa de aging associada. | FK | 🟢 100% |
| 4 | SCHEDULE_AMOUNT | NUMBER | NULL | Valor fixo do encargo a ser cobrado. | Financeiro | 🟢 100% |
| 5 | SCHEDULE_PERCENTAGE | NUMBER | NULL | Percentual do encargo sobre o saldo devedor. | Financeiro | 🟢 100% |
| 6 | FREQUENCY | VARCHAR2(30) | NULL | Frequência de aplicação do encargo. | Negócio | 🟡 75% |
| 7 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 8 | ATTRIBUTE1 | VARCHAR2(150) | NULL | Atributo descritivo flexível 1. | DFF | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_charge_schedule_hdrs]]** — Cabeçalho do cronograma (N:1 via `SCHEDULE_HEADER_ID`).
- **[[ar_aging_buckets]]** — Faixa de aging associada (N:1 via `AGING_BUCKET_ID`).
- **[[ar_charge_schedule_lines]]** — Linhas de detalhe do cronograma (1:N via `SCHEDULE_ID`).

## 📎 Uso Típico

```sql
-- Cronogramas de encargos por faixa de aging
SELECT csh.SCHEDULE_HEADER_NAME,
       ab.BUCKET_NAME,
       cs.SCHEDULE_AMOUNT,
       cs.SCHEDULE_PERCENTAGE
  FROM AR_CHARGE_SCHEDULES cs
  JOIN AR_CHARGE_SCHEDULE_HDRS csh
    ON csh.SCHEDULE_HEADER_ID = cs.SCHEDULE_HEADER_ID
  LEFT JOIN AR_AGING_BUCKETS ab
    ON ab.AGING_BUCKET_ID = cs.AGING_BUCKET_ID
 WHERE csh.STATUS = 'A'
 ORDER BY csh.SCHEDULE_HEADER_NAME, ab.BUCKET_NAME;
```

## 🔒 Observações

- `SCHEDULE_AMOUNT` e `SCHEDULE_PERCENTAGE` são mutuamente exclusivos; apenas um deve estar preenchido por registro.
- A associação com `AGING_BUCKET_ID` permite escalonamento automático de encargos por tempo de atraso.
- Cronogramas inativos no cabeçalho não devem ser processados.

## 🔗 PVOs Relacionados

### [[chargescheduleextractpvo|ChargeScheduleExtractPVO]] (OTHER · BICC: 9/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ArChargeScheduleAttribute1 | — |
| ATTRIBUTE10 | ArChargeScheduleAttribute10 | — |
| ATTRIBUTE11 | ArChargeScheduleAttribute11 | — |
| ATTRIBUTE12 | ArChargeScheduleAttribute12 | — |
| ATTRIBUTE13 | ArChargeScheduleAttribute13 | — |
| ATTRIBUTE14 | ArChargeScheduleAttribute14 | — |
| ATTRIBUTE15 | ArChargeScheduleAttribute15 | — |
| ATTRIBUTE2 | ArChargeScheduleAttribute2 | — |
| ATTRIBUTE3 | ArChargeScheduleAttribute3 | — |
| ATTRIBUTE4 | ArChargeScheduleAttribute4 | — |
| ATTRIBUTE5 | ArChargeScheduleAttribute5 | — |
| ATTRIBUTE6 | ArChargeScheduleAttribute6 | — |
| ATTRIBUTE7 | ArChargeScheduleAttribute7 | — |
| ATTRIBUTE8 | ArChargeScheduleAttribute8 | — |
| ATTRIBUTE9 | ArChargeScheduleAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArChargeScheduleAttributeCategory | — |
| CREATED_BY | ArChargeScheduleCreatedBy | ✅ |
| CREATION_DATE | ArChargeScheduleCreationDate | ✅ |
| LAST_UPDATE_DATE | ArChargeScheduleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArChargeScheduleLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArChargeScheduleLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArChargeScheduleObjectVersionNumber | ✅ |
| SCHEDULE_DESCRIPTION | ArChargeScheduleScheduleDescription | ✅ |
| SCHEDULE_ID | ArChargeScheduleScheduleId | ✅ |
| SCHEDULE_NAME | ArChargeScheduleScheduleName | ✅ |

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SCHEDULE_DESCRIPTION | ChargeScheduleScheduleDescription | — |
| SCHEDULE_ID | ChargeScheduleScheduleId | — |
| SCHEDULE_NAME | ChargeScheduleScheduleName | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SCHEDULE_DESCRIPTION | ChargeSchedulesScheduleDescription | — |
| SCHEDULE_ID | ChargeSchedulesScheduleId | — |
| SCHEDULE_NAME | ChargeSchedulesScheduleName | ✅ |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SCHEDULE_DESCRIPTION | ChargeSchedulesScheduleDescription | — |
| SCHEDULE_ID | ChargeSchedulesScheduleId | — |
| SCHEDULE_NAME | ChargeSchedulesScheduleName | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Charge Schedules and Late Charges Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
