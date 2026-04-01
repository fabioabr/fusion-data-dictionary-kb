---
id: DOC-HCM-130
doc_type: system-doc
title: "FND_DOC_SEQUENCE_CATEGORIES — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_DOC_SEQUENCE_CATEGORIES
  - fnd_doc_sequence_categories
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DOC_SEQUENCE_CATEGORIES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLICATION_ID | — | — | — | — | — | — |
| 2 | CODE | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DESCRIPTION | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | MODULE_ID | — | — | — | — | — | — |
| 10 | NAME | — | — | — | — | — | — |
| 11 | TABLE_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | DocSeqCatApplicationId | — |
| CODE | DocSeqCatCode | — |
| DESCRIPTION | DocSeqCatDescription | ✅ |
| NAME | DocSeqCatName | ✅ |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | DocSeqCatApplicationId | — |
| CODE | DocSeqCatCode | — |
| DESCRIPTION | DocSeqCatDescription | ✅ |
| NAME | DocSeqCatName | ✅ |

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | DocSeqCategApplicationId | — |
| CODE | DocSeqCategCode | — |
| CREATED_BY | DocSeqCategCreatedBy | — |
| CREATION_DATE | DocSeqCategCreationDate | — |
| DESCRIPTION | DocSeqCategDescription | — |
| LAST_UPDATE_DATE | DocSeqCategLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DocSeqCategLastUpdateLogin | — |
| LAST_UPDATED_BY | DocSeqCategLastUpdatedBy | — |
| MODULE_ID | DocSeqCategModuleId | — |
| NAME | DocSeqCategName | ✅ |
| TABLE_NAME | DocSeqCategTableName | — |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | DocSeqCategApplicationId | — |
| CODE | DocSeqCategCode | — |
| CREATED_BY | DocSeqCategCreatedBy | — |
| CREATION_DATE | DocSeqCategCreationDate | — |
| DESCRIPTION | DocSeqCategDescription | — |
| LAST_UPDATE_DATE | DocSeqCategLastUpdateDate | — |
| LAST_UPDATE_LOGIN | DocSeqCategLastUpdateLogin | — |
| LAST_UPDATED_BY | DocSeqCategLastUpdatedBy | — |
| MODULE_ID | DocSeqCategModuleId | — |
| NAME | DocSeqCategName | — |
| TABLE_NAME | DocSeqCategTableName | — |
