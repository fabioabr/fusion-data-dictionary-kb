---
id: DOC-AR-040
doc_type: system-doc
title: "AR_CHARGE_SCHEDULE_HDRS — Cabeçalhos dos Cronogramas de Encargos"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, encargos, cabecalho, charge-schedule]
aliases: [AR_CHARGE_SCHEDULE_HDRS, ar_charge_schedule_hdrs, charge_schedule_hdrs, cabecalho_cronograma, schedule_hdrs]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_CHARGE_SCHEDULE_HDRS

## 📌 Visão Geral

Tabela de cabeçalhos dos cronogramas de encargos (charge schedule headers) do Accounts Receivable. Define o nome, tipo e vigência de cada cronograma, que é detalhado nas tabelas [[ar_charge_schedules]] e [[ar_charge_schedule_lines]].

## 🧠 Propósito de Negócio

Os cabeçalhos de cronograma centralizam a configuração das políticas de cobrança de encargos. Cada cabeçalho representa uma política nomeada (ex.: "Juros Padrão", "Multa Premium") que pode ser atribuída a perfis de clientes. A vigência por datas permite versionar políticas sem perder histórico.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | SCHEDULE_HEADER_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cabeçalho. | PK | 🟢 100% |
| 2 | SCHEDULE_HEADER_NAME | VARCHAR2(30) | NOT NULL | Nome do cronograma de encargos. | Negócio | 🟢 100% |
| 3 | SCHEDULE_HEADER_TYPE | VARCHAR2(30) | NOT NULL | Tipo do cronograma (ex.: PERCENTAGE, AMOUNT, FIXED). | Classificação | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | START_DATE | DATE | NULL | Data de início de vigência do cronograma. | Temporal | 🟢 100% |
| 6 | END_DATE | DATE | NULL | Data de fim de vigência do cronograma. | Temporal | 🟢 100% |
| 7 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição textual do cronograma. | Negócio | 🟢 100% |
| 8 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_charge_schedules]]** — Cronogramas associados a este cabeçalho (1:N via `SCHEDULE_HEADER_ID`).
- **[[ar_charge_schedule_lines]]** — Linhas de detalhe dos cronogramas (1:N via `SCHEDULE_HEADER_ID`).
- **HZ_CUSTOMER_PROFILES** — Perfis de clientes que utilizam este cronograma.

## 📎 Uso Típico

```sql
-- Listar cronogramas de encargos ativos e vigentes
SELECT csh.SCHEDULE_HEADER_ID,
       csh.SCHEDULE_HEADER_NAME,
       csh.SCHEDULE_HEADER_TYPE,
       csh.START_DATE,
       csh.END_DATE
  FROM AR_CHARGE_SCHEDULE_HDRS csh
 WHERE csh.STATUS = 'A'
   AND NVL(csh.END_DATE, SYSDATE + 1) > SYSDATE
 ORDER BY csh.SCHEDULE_HEADER_NAME;
```

## 🔒 Observações

- Cronogramas com `END_DATE` preenchida e anterior à data atual são considerados expirados.
- O `SCHEDULE_HEADER_TYPE` determina como os valores nas linhas devem ser interpretados (percentual vs. valor fixo).
- Não é recomendável excluir cabeçalhos que já foram utilizados em cálculos históricos; prefira inativar.

## 🔗 PVOs Relacionados

### [[chargeschedulehdrextractpvo|ChargeScheduleHDRExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET_ID | ArChargeScheduleHDRAgingBucketId | ✅ |
| ATTRIBUTE1 | ArChargeScheduleHDRAttribute1 | — |
| ATTRIBUTE10 | ArChargeScheduleHDRAttribute10 | — |
| ATTRIBUTE11 | ArChargeScheduleHDRAttribute11 | — |
| ATTRIBUTE12 | ArChargeScheduleHDRAttribute12 | — |
| ATTRIBUTE13 | ArChargeScheduleHDRAttribute13 | — |
| ATTRIBUTE14 | ArChargeScheduleHDRAttribute14 | — |
| ATTRIBUTE15 | ArChargeScheduleHDRAttribute15 | — |
| ATTRIBUTE2 | ArChargeScheduleHDRAttribute2 | — |
| ATTRIBUTE3 | ArChargeScheduleHDRAttribute3 | — |
| ATTRIBUTE4 | ArChargeScheduleHDRAttribute4 | — |
| ATTRIBUTE5 | ArChargeScheduleHDRAttribute5 | — |
| ATTRIBUTE6 | ArChargeScheduleHDRAttribute6 | — |
| ATTRIBUTE7 | ArChargeScheduleHDRAttribute7 | — |
| ATTRIBUTE8 | ArChargeScheduleHDRAttribute8 | — |
| ATTRIBUTE9 | ArChargeScheduleHDRAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArChargeScheduleHDRAttributeCategory | — |
| CREATED_BY | ArChargeScheduleHDRCreatedBy | ✅ |
| CREATION_DATE | ArChargeScheduleHDRCreationDate | ✅ |
| END_DATE | ArChargeScheduleHDREndDate | ✅ |
| LAST_UPDATE_DATE | ArChargeScheduleHDRLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArChargeScheduleHDRLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArChargeScheduleHDRLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArChargeScheduleHDRObjectVersionNumber | ✅ |
| SCHEDULE_HEADER_ID | ArChargeScheduleHDRScheduleHeaderId | ✅ |
| SCHEDULE_HEADER_TYPE | ArChargeScheduleHDRScheduleHeaderType | ✅ |
| SCHEDULE_ID | ArChargeScheduleHDRScheduleId | ✅ |
| START_DATE | ArChargeScheduleHDRStartDate | ✅ |
| STATUS | ArChargeScheduleHDRStatus | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Charge Schedules Configuration Guide.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
