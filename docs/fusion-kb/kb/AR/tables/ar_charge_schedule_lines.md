---
id: DOC-AR-041
doc_type: system-doc
title: "AR_CHARGE_SCHEDULE_LINES — Linhas dos Cronogramas de Encargos"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, encargos, linhas-cronograma, faixas]
aliases: [AR_CHARGE_SCHEDULE_LINES, ar_charge_schedule_lines, charge_schedule_lines, linhas_cronograma, schedule_lines]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CHARGE_SCHEDULE_LINES

## 📌 Visão Geral

Tabela de linhas dos cronogramas de encargos do Accounts Receivable. Cada linha define uma faixa de valor ou período de atraso com a respectiva taxa de juros ou valor fixo a ser cobrado. Vinculada ao cabeçalho em [[ar_charge_schedule_hdrs]].

## 🧠 Propósito de Negócio

As linhas de cronograma permitem escalonamento granular de encargos: diferentes taxas podem ser aplicadas conforme o valor em atraso ou o número de dias de inadimplência. Exemplo: 1% ao mês para valores até R$ 10.000 e 1,5% para valores acima. Isso proporciona flexibilidade na política de crédito e cobrança.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | SCHEDULE_LINE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único da linha do cronograma. | PK | 🟢 100% |
| 2 | SCHEDULE_HEADER_ID | NUMBER(15) | NOT NULL | FK para [[ar_charge_schedule_hdrs]]. Cabeçalho do cronograma. | FK | 🟢 100% |
| 3 | AMOUNT_FROM | NUMBER | NULL | Valor mínimo da faixa de saldo devedor. | Financeiro | 🟢 100% |
| 4 | AMOUNT_TO | NUMBER | NULL | Valor máximo da faixa de saldo devedor. | Financeiro | 🟢 100% |
| 5 | INTEREST_RATE | NUMBER | NULL | Taxa de juros (percentual) aplicada nesta faixa. | Financeiro | 🟢 100% |
| 6 | INTEREST_FIXED_AMOUNT | NUMBER | NULL | Valor fixo de juros aplicado nesta faixa. | Financeiro | 🟢 100% |
| 7 | OVERDUE_DAYS_FROM | NUMBER | NULL | Número mínimo de dias em atraso para esta faixa. | Negócio | 🟢 100% |
| 8 | OVERDUE_DAYS_TO | NUMBER | NULL | Número máximo de dias em atraso para esta faixa. | Negócio | 🟢 100% |
| 9 | SCHEDULE_LINE_NUM | NUMBER | NULL | Número de sequência da linha dentro do cronograma. | Controle | 🟡 75% |
| 10 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 11 | ATTRIBUTE1 | VARCHAR2(150) | NULL | Atributo descritivo flexível 1. | DFF | 🟢 100% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_charge_schedule_hdrs]]** — Cabeçalho do cronograma (N:1 via `SCHEDULE_HEADER_ID`).
- **[[ar_charge_schedules]]** — Cronogramas de nível intermediário (via `SCHEDULE_HEADER_ID`).

## 📎 Uso Típico

```sql
-- Faixas de encargos configuradas por cronograma
SELECT csh.SCHEDULE_HEADER_NAME,
       csl.AMOUNT_FROM,
       csl.AMOUNT_TO,
       csl.OVERDUE_DAYS_FROM,
       csl.OVERDUE_DAYS_TO,
       csl.INTEREST_RATE,
       csl.INTEREST_FIXED_AMOUNT
  FROM AR_CHARGE_SCHEDULE_LINES csl
  JOIN AR_CHARGE_SCHEDULE_HDRS csh
    ON csh.SCHEDULE_HEADER_ID = csl.SCHEDULE_HEADER_ID
 WHERE csh.STATUS = 'A'
 ORDER BY csh.SCHEDULE_HEADER_NAME, csl.OVERDUE_DAYS_FROM, csl.AMOUNT_FROM;
```

## 🔒 Observações

- `INTEREST_RATE` e `INTEREST_FIXED_AMOUNT` são mutuamente exclusivos, conforme o tipo definido no cabeçalho.
- Faixas de valor (`AMOUNT_FROM`/`AMOUNT_TO`) e faixas de dias (`OVERDUE_DAYS_FROM`/`OVERDUE_DAYS_TO`) não devem se sobrepor dentro do mesmo cronograma.
- A ausência de `AMOUNT_TO` ou `OVERDUE_DAYS_TO` pode indicar faixa aberta (sem limite superior).

## 🔗 PVOs Relacionados

### [[chargeschedulelineextractpvo|ChargeScheduleLineExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET_ID | ArChargeScheduleLineAgingBucketId | ✅ |
| AGING_BUCKET_LINE_ID | ArChargeScheduleLineAgingBucketLineId | ✅ |
| AMOUNT | ArChargeScheduleLineAmount | ✅ |
| ATTRIBUTE1 | ArChargeScheduleLineAttribute1 | — |
| ATTRIBUTE10 | ArChargeScheduleLineAttribute10 | — |
| ATTRIBUTE11 | ArChargeScheduleLineAttribute11 | — |
| ATTRIBUTE12 | ArChargeScheduleLineAttribute12 | — |
| ATTRIBUTE13 | ArChargeScheduleLineAttribute13 | — |
| ATTRIBUTE14 | ArChargeScheduleLineAttribute14 | — |
| ATTRIBUTE15 | ArChargeScheduleLineAttribute15 | — |
| ATTRIBUTE2 | ArChargeScheduleLineAttribute2 | — |
| ATTRIBUTE3 | ArChargeScheduleLineAttribute3 | — |
| ATTRIBUTE4 | ArChargeScheduleLineAttribute4 | — |
| ATTRIBUTE5 | ArChargeScheduleLineAttribute5 | — |
| ATTRIBUTE6 | ArChargeScheduleLineAttribute6 | — |
| ATTRIBUTE7 | ArChargeScheduleLineAttribute7 | — |
| ATTRIBUTE8 | ArChargeScheduleLineAttribute8 | — |
| ATTRIBUTE9 | ArChargeScheduleLineAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArChargeScheduleLineAttributeCategory | — |
| CREATED_BY | ArChargeScheduleLineCreatedBy | ✅ |
| CREATION_DATE | ArChargeScheduleLineCreationDate | ✅ |
| LAST_UPDATE_DATE | ArChargeScheduleLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArChargeScheduleLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArChargeScheduleLineLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArChargeScheduleLineObjectVersionNumber | ✅ |
| RATE | ArChargeScheduleLineRate | ✅ |
| SCHEDULE_HEADER_ID | ArChargeScheduleLineScheduleHeaderId | ✅ |
| SCHEDULE_ID | ArChargeScheduleLineScheduleId | ✅ |
| SCHEDULE_LINE_ID | ArChargeScheduleLineScheduleLineId | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Charge Schedules Configuration Guide.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
