---
id: DOC-OTHER-PVO-SupplyMessagesExtractPVO
doc_type: system-doc
title: "SupplyMessagesExtractPVO — PVO Cross-Module"
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
  - SupplyMessagesExtractPVO
  - supplymessagesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyMessagesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Messages Extract. Acessa as tabelas: DOS_MESSAGES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyMessagesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_messages|DOS_MESSAGES]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[dos_messages|DOS_MESSAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosMessageExtractPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | DosMessageExtractPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | DosMessageExtractPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | DosMessageExtractPEOExceptionType | EXCEPTION_TYPE | — | ✅ |
| 5 | DosMessageExtractPEOFunctionalModule | FUNCTIONAL_MODULE | — | ✅ |
| 6 | DosMessageExtractPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DosMessageExtractPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | DosMessageExtractPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DosMessageExtractPEOMessageApplicationCode | MESSAGE_APPLICATION_CODE | — | ✅ |
| 10 | DosMessageExtractPEOMessageId | MESSAGE_ID | 🔑 | ✅ |
| 11 | DosMessageExtractPEOMessageName | MESSAGE_NAME | — | ✅ |
| 12 | DosMessageExtractPEOMessageSeverity | MESSAGE_SEVERITY | — | ✅ |
| 13 | DosMessageExtractPEOMessageText | MESSAGE_TEXT | — | ✅ |
| 14 | DosMessageExtractPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | DosMessageExtractPEOProcessingEntityId | PROCESSING_ENTITY_ID | — | ✅ |
| 16 | DosMessageExtractPEOProcessingEntityType | PROCESSING_ENTITY_TYPE | — | ✅ |
| 17 | DosMessageExtractPEORecoveryStatus | RECOVERY_STATUS | — | ✅ |
| 18 | DosMessageExtractPEOTokenNameA | TOKEN_NAME_A | — | ✅ |
| 19 | DosMessageExtractPEOTokenNameB | TOKEN_NAME_B | — | ✅ |
| 20 | DosMessageExtractPEOTokenNameC | TOKEN_NAME_C | — | ✅ |
| 21 | DosMessageExtractPEOTokenNameD | TOKEN_NAME_D | — | ✅ |
| 22 | DosMessageExtractPEOTokenNameE | TOKEN_NAME_E | — | ✅ |
| 23 | DosMessageExtractPEOTokenValueA | TOKEN_VALUE_A | — | ✅ |
| 24 | DosMessageExtractPEOTokenValueB | TOKEN_VALUE_B | — | ✅ |
| 25 | DosMessageExtractPEOTokenValueC | TOKEN_VALUE_C | — | ✅ |
| 26 | DosMessageExtractPEOTokenValueD | TOKEN_VALUE_D | — | ✅ |
| 27 | DosMessageExtractPEOTokenValueE | TOKEN_VALUE_E | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
