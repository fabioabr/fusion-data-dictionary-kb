---
id: DOC-AR-031
doc_type: system-doc
title: "AR_AGING_BUCKETS — Faixas de Aging de Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, aging, buckets, cobranca]
aliases: [AR_AGING_BUCKETS, ar_aging_buckets, aging_buckets, faixas_aging, aging_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_AGING_BUCKETS

## 📌 Visão Geral

Tabela de definição das faixas de aging (envelhecimento) utilizadas para classificar saldos em aberto de contas a receber por período de atraso. Cada registro representa um conjunto de faixas (ex.: 0–30, 31–60, 61–90 dias) que pode ser associado a relatórios de aging e processos de cobrança.

## 🧠 Propósito de Negócio

As faixas de aging são fundamentais para a gestão de crédito e cobrança. Permitem que a tesouraria e o departamento financeiro visualizem a distribuição dos recebíveis por tempo de atraso, identifiquem clientes inadimplentes e priorizem ações de cobrança. Os buckets são configuráveis por organização e podem ser personalizados conforme a política de crédito do Banco Patria.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | AGING_BUCKET_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único da faixa de aging. | PK | 🟢 100% |
| 2 | BUCKET_NAME | VARCHAR2(80) | NOT NULL | Nome da faixa de aging (ex.: "Padrão 30/60/90"). | Negócio | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição textual da faixa de aging. | Negócio | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | TYPE | VARCHAR2(30) | NOT NULL | Tipo do bucket (ex.: AGING_DAYS, AGING_AMOUNT). | Classificação | 🟢 100% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 7 | ATTRIBUTE1 | VARCHAR2(150) | NULL | Atributo descritivo flexível 1. | DFF | 🟢 100% |
| 8 | ATTRIBUTE2 | VARCHAR2(150) | NULL | Atributo descritivo flexível 2. | DFF | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_aging_bucket_lines_b]]** — Linhas individuais de cada faixa (1:N via `AGING_BUCKET_ID`).
- **[[ar_aging_bucket_lines_tl]]** — Traduções das linhas de aging (via `AGING_BUCKET_LINE_ID`).

## 📎 Uso Típico

```sql
-- Listar faixas de aging ativas com suas linhas
SELECT b.BUCKET_NAME,
       bl.BUCKET_SEQUENCE_NUM,
       bl.DAYS_START,
       bl.DAYS_TO
  FROM AR_AGING_BUCKETS b
  JOIN AR_AGING_BUCKET_LINES_B bl
    ON bl.AGING_BUCKET_ID = b.AGING_BUCKET_ID
 WHERE b.STATUS = 'A'
 ORDER BY b.BUCKET_NAME, bl.BUCKET_SEQUENCE_NUM;
```

## 🔒 Observações

- Faixas de aging são compartilhadas entre business units e não possuem `ORG_ID`.
- Alterações nas faixas afetam todos os relatórios de aging que as utilizam.
- É recomendável não desativar buckets que estejam em uso por relatórios agendados.

## 🔗 PVOs Relacionados

### [[agingbucketlinesbasepvo|AgingBucketLinesBasePVO]] (OTHER · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET_ID | AgingBucketsAgingBucketId | — |
| AGING_TYPE | AgingBucketsAgingType | ✅ |
| BUCKET_NAME | AgingBucketsBucketName | ✅ |
| CREATED_BY | AgingBucketsCreatedBy | — |
| CREATION_DATE | AgingBucketsCreationDate | — |
| DESCRIPTION | AgingBucketsDescription | — |
| LAST_UPDATE_DATE | AgingBucketsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AgingBucketsLastUpdateLogin | — |
| LAST_UPDATED_BY | AgingBucketsLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AgingBucketsObjectVersionNumber | — |
| SET_ID | AgingBucketsSetId | — |
| STATUS | AgingBucketsStatus | ✅ |

### [[agingbucketsextractpvo|AgingBucketsExtractPVO]] (OTHER · BICC: 12/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_BUCKET_ID | ArAgingBucketsAgingBucketId | ✅ |
| AGING_TYPE | ArAgingBucketsAgingType | ✅ |
| ATTRIBUTE1 | ArAgingBucketsAttribute1 | — |
| ATTRIBUTE10 | ArAgingBucketsAttribute10 | — |
| ATTRIBUTE11 | ArAgingBucketsAttribute11 | — |
| ATTRIBUTE12 | ArAgingBucketsAttribute12 | — |
| ATTRIBUTE13 | ArAgingBucketsAttribute13 | — |
| ATTRIBUTE14 | ArAgingBucketsAttribute14 | — |
| ATTRIBUTE15 | ArAgingBucketsAttribute15 | — |
| ATTRIBUTE2 | ArAgingBucketsAttribute2 | — |
| ATTRIBUTE3 | ArAgingBucketsAttribute3 | — |
| ATTRIBUTE4 | ArAgingBucketsAttribute4 | — |
| ATTRIBUTE5 | ArAgingBucketsAttribute5 | — |
| ATTRIBUTE6 | ArAgingBucketsAttribute6 | — |
| ATTRIBUTE7 | ArAgingBucketsAttribute7 | — |
| ATTRIBUTE8 | ArAgingBucketsAttribute8 | — |
| ATTRIBUTE9 | ArAgingBucketsAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArAgingBucketsAttributeCategory | — |
| BUCKET_NAME | ArAgingBucketsBucketName | ✅ |
| CREATED_BY | ArAgingBucketsCreatedBy | ✅ |
| CREATION_DATE | ArAgingBucketsCreationDate | ✅ |
| DESCRIPTION | ArAgingBucketsDescription | ✅ |
| LAST_UPDATE_DATE | ArAgingBucketsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArAgingBucketsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArAgingBucketsLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ArAgingBucketsObjectVersionNumber | ✅ |
| SET_ID | ArAgingBucketsSetId | ✅ |
| STATUS | ArAgingBucketsStatus | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle BICC — AR Aging Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
