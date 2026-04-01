---
id: DOC-OTHER-PVO-FosProcessMessageExtractPVO
doc_type: system-doc
title: "FosProcessMessageExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - FosProcessMessageExtractPVO
  - fosprocessmessageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosProcessMessageExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Process Message Extract. Acessa as tabelas: FOS_PROCESS_MESSAGES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosProcessMessageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_process_messages|FOS_PROCESS_MESSAGES]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[fos_process_messages|FOS_PROCESS_MESSAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessMessagePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProcessMessagePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProcessMessagePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | ProcessMessagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProcessMessagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ProcessMessagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ProcessMessagePEOMessageAdditionalText | MESSAGE_ADDITIONAL_TEXT | — | ✅ |
| 8 | ProcessMessagePEOMessageCategory1 | MESSAGE_CATEGORY1 | — | ✅ |
| 9 | ProcessMessagePEOMessageCategory2 | MESSAGE_CATEGORY2 | — | ✅ |
| 10 | ProcessMessagePEOMessageEntityId1 | MESSAGE_ENTITY_ID1 | — | ✅ |
| 11 | ProcessMessagePEOMessageEntityId2 | MESSAGE_ENTITY_ID2 | — | ✅ |
| 12 | ProcessMessagePEOMessageGroupNumber | MESSAGE_GROUP_NUMBER | — | ✅ |
| 13 | ProcessMessagePEOMessageId | MESSAGE_ID | 🔑 | ✅ |
| 14 | ProcessMessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 15 | ProcessMessagePEOMessageTokens | MESSAGE_TOKENS | — | ✅ |
| 16 | ProcessMessagePEOMessageType | MESSAGE_TYPE | — | ✅ |
| 17 | ProcessMessagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ProcessMessagePEOReferenceEntityId | REFERENCE_ENTITY_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
