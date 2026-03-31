---
id: DOC-PO-PVO-ResponseRepositoryValuesExtractPVO
doc_type: system-doc
title: "ResponseRepositoryValuesExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ResponseRepositoryValuesExtractPVO
  - responserepositoryvaluesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResponseRepositoryValuesExtractPVO

## 📌 Visão Geral

Extrai os valores do repositório de respostas de qualificação para carga BICC, incluindo dados cadastrais e certificações armazenados. Alimenta análises de completude de dados.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.ResponseRepositoryValuesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_resp_repository_values|POQ_RESP_REPOSITORY_VALUES]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[poq_resp_repository_values|POQ_RESP_REPOSITORY_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccResponseId | ACC_RESPONSE_ID | — | ✅ |
| 2 | AccResponseText | ACC_RESPONSE_TEXT | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RespRepositoryValueId | RESP_REPOSITORY_VALUE_ID | 🔑 | ✅ |
| 10 | ResponseRepositoryId | RESPONSE_REPOSITORY_ID | — | ✅ |
| 11 | ResponseValueDate | RESPONSE_VALUE_DATE | — | ✅ |
| 12 | ResponseValueDatetime | RESPONSE_VALUE_DATETIME | — | ✅ |
| 13 | ResponseValueNum | RESPONSE_VALUE_NUM | — | ✅ |
| 14 | ResponseValueTxt | RESPONSE_VALUE_TXT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
