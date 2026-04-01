---
id: DOC-OTHER-PVO-SubledgerTransactionLineReversalExtractPVO
doc_type: system-doc
title: "SubledgerTransactionLineReversalExtractPVO — PVO Cross-Module"
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
  - SubledgerTransactionLineReversalExtractPVO
  - subledgertransactionlinereversalextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerTransactionLineReversalExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Transaction Line Reversal Extract. Acessa as tabelas: XLA_TRANSACTION_HEADERS, XLA_TRANSACTION_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerTransactionLineReversalExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 161 | 2 | 3 | 161 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_transaction_headers|XLA_TRANSACTION_HEADERS]] — 6 atributos (6 BICC)
- [[xla_transaction_lines|XLA_TRANSACTION_LINES]] — 155 atributos (3 PKs, 155 BICC)

---

## ⚙️ Atributos

### [[xla_transaction_headers|XLA_TRANSACTION_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxRevHeaderCreationDate | CREATION_DATE | — | ✅ |
| 2 | TrxRevHeaderEventId | EVENT_ID | — | ✅ |
| 3 | TrxRevHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | TrxRevHeaderTransactionDate | TRANSACTION_DATE | — | ✅ |
| 5 | TrxRevHeaderTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 6 | TrxRevHeaderTransactionReversalFlag | TRANSACTION_REVERSAL_FLAG | — | ✅ |

### [[xla_transaction_lines|XLA_TRANSACTION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrxRevLineApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | TrxRevLineChar1 | CHAR1 | — | ✅ |
| 3 | TrxRevLineChar10 | CHAR10 | — | ✅ |
| 4 | TrxRevLineChar100 | CHAR100 | — | ✅ |
| 5 | TrxRevLineChar11 | CHAR11 | — | ✅ |
| 6 | TrxRevLineChar12 | CHAR12 | — | ✅ |
| 7 | TrxRevLineChar13 | CHAR13 | — | ✅ |
| 8 | TrxRevLineChar14 | CHAR14 | — | ✅ |
| 9 | TrxRevLineChar15 | CHAR15 | — | ✅ |
| 10 | TrxRevLineChar16 | CHAR16 | — | ✅ |
| 11 | TrxRevLineChar17 | CHAR17 | — | ✅ |
| 12 | TrxRevLineChar18 | CHAR18 | — | ✅ |
| 13 | TrxRevLineChar19 | CHAR19 | — | ✅ |
| 14 | TrxRevLineChar2 | CHAR2 | — | ✅ |
| 15 | TrxRevLineChar20 | CHAR20 | — | ✅ |
| 16 | TrxRevLineChar21 | CHAR21 | — | ✅ |
| 17 | TrxRevLineChar22 | CHAR22 | — | ✅ |
| 18 | TrxRevLineChar23 | CHAR23 | — | ✅ |
| 19 | TrxRevLineChar24 | CHAR24 | — | ✅ |
| 20 | TrxRevLineChar25 | CHAR25 | — | ✅ |
| 21 | TrxRevLineChar26 | CHAR26 | — | ✅ |
| 22 | TrxRevLineChar27 | CHAR27 | — | ✅ |
| 23 | TrxRevLineChar28 | CHAR28 | — | ✅ |
| 24 | TrxRevLineChar29 | CHAR29 | — | ✅ |
| 25 | TrxRevLineChar3 | CHAR3 | — | ✅ |
| 26 | TrxRevLineChar30 | CHAR30 | — | ✅ |
| 27 | TrxRevLineChar31 | CHAR31 | — | ✅ |
| 28 | TrxRevLineChar32 | CHAR32 | — | ✅ |
| 29 | TrxRevLineChar33 | CHAR33 | — | ✅ |
| 30 | TrxRevLineChar34 | CHAR34 | — | ✅ |
| 31 | TrxRevLineChar35 | CHAR35 | — | ✅ |
| 32 | TrxRevLineChar36 | CHAR36 | — | ✅ |
| 33 | TrxRevLineChar37 | CHAR37 | — | ✅ |
| 34 | TrxRevLineChar38 | CHAR38 | — | ✅ |
| 35 | TrxRevLineChar39 | CHAR39 | — | ✅ |
| 36 | TrxRevLineChar4 | CHAR4 | — | ✅ |
| 37 | TrxRevLineChar40 | CHAR40 | — | ✅ |
| 38 | TrxRevLineChar41 | CHAR41 | — | ✅ |
| 39 | TrxRevLineChar42 | CHAR42 | — | ✅ |
| 40 | TrxRevLineChar43 | CHAR43 | — | ✅ |
| 41 | TrxRevLineChar44 | CHAR44 | — | ✅ |
| 42 | TrxRevLineChar45 | CHAR45 | — | ✅ |
| 43 | TrxRevLineChar46 | CHAR46 | — | ✅ |
| 44 | TrxRevLineChar47 | CHAR47 | — | ✅ |
| 45 | TrxRevLineChar48 | CHAR48 | — | ✅ |
| 46 | TrxRevLineChar49 | CHAR49 | — | ✅ |
| 47 | TrxRevLineChar5 | CHAR5 | — | ✅ |
| 48 | TrxRevLineChar50 | CHAR50 | — | ✅ |
| 49 | TrxRevLineChar51 | CHAR51 | — | ✅ |
| 50 | TrxRevLineChar52 | CHAR52 | — | ✅ |
| 51 | TrxRevLineChar53 | CHAR53 | — | ✅ |
| 52 | TrxRevLineChar54 | CHAR54 | — | ✅ |
| 53 | TrxRevLineChar55 | CHAR55 | — | ✅ |
| 54 | TrxRevLineChar56 | CHAR56 | — | ✅ |
| 55 | TrxRevLineChar57 | CHAR57 | — | ✅ |
| 56 | TrxRevLineChar58 | CHAR58 | — | ✅ |
| 57 | TrxRevLineChar59 | CHAR59 | — | ✅ |
| 58 | TrxRevLineChar6 | CHAR6 | — | ✅ |
| 59 | TrxRevLineChar60 | CHAR60 | — | ✅ |
| 60 | TrxRevLineChar61 | CHAR61 | — | ✅ |
| 61 | TrxRevLineChar62 | CHAR62 | — | ✅ |
| 62 | TrxRevLineChar63 | CHAR63 | — | ✅ |
| 63 | TrxRevLineChar64 | CHAR64 | — | ✅ |
| 64 | TrxRevLineChar65 | CHAR65 | — | ✅ |
| 65 | TrxRevLineChar66 | CHAR66 | — | ✅ |
| 66 | TrxRevLineChar67 | CHAR67 | — | ✅ |
| 67 | TrxRevLineChar68 | CHAR68 | — | ✅ |
| 68 | TrxRevLineChar69 | CHAR69 | — | ✅ |
| 69 | TrxRevLineChar7 | CHAR7 | — | ✅ |
| 70 | TrxRevLineChar70 | CHAR70 | — | ✅ |
| 71 | TrxRevLineChar71 | CHAR71 | — | ✅ |
| 72 | TrxRevLineChar72 | CHAR72 | — | ✅ |
| 73 | TrxRevLineChar73 | CHAR73 | — | ✅ |
| 74 | TrxRevLineChar74 | CHAR74 | — | ✅ |
| 75 | TrxRevLineChar75 | CHAR75 | — | ✅ |
| 76 | TrxRevLineChar76 | CHAR76 | — | ✅ |
| 77 | TrxRevLineChar77 | CHAR77 | — | ✅ |
| 78 | TrxRevLineChar78 | CHAR78 | — | ✅ |
| 79 | TrxRevLineChar79 | CHAR79 | — | ✅ |
| 80 | TrxRevLineChar8 | CHAR8 | — | ✅ |
| 81 | TrxRevLineChar80 | CHAR80 | — | ✅ |
| 82 | TrxRevLineChar81 | CHAR81 | — | ✅ |
| 83 | TrxRevLineChar82 | CHAR82 | — | ✅ |
| 84 | TrxRevLineChar83 | CHAR83 | — | ✅ |
| 85 | TrxRevLineChar84 | CHAR84 | — | ✅ |
| 86 | TrxRevLineChar85 | CHAR85 | — | ✅ |
| 87 | TrxRevLineChar86 | CHAR86 | — | ✅ |
| 88 | TrxRevLineChar87 | CHAR87 | — | ✅ |
| 89 | TrxRevLineChar88 | CHAR88 | — | ✅ |
| 90 | TrxRevLineChar89 | CHAR89 | — | ✅ |
| 91 | TrxRevLineChar9 | CHAR9 | — | ✅ |
| 92 | TrxRevLineChar90 | CHAR90 | — | ✅ |
| 93 | TrxRevLineChar91 | CHAR91 | — | ✅ |
| 94 | TrxRevLineChar92 | CHAR92 | — | ✅ |
| 95 | TrxRevLineChar93 | CHAR93 | — | ✅ |
| 96 | TrxRevLineChar94 | CHAR94 | — | ✅ |
| 97 | TrxRevLineChar95 | CHAR95 | — | ✅ |
| 98 | TrxRevLineChar96 | CHAR96 | — | ✅ |
| 99 | TrxRevLineChar97 | CHAR97 | — | ✅ |
| 100 | TrxRevLineChar98 | CHAR98 | — | ✅ |
| 101 | TrxRevLineChar99 | CHAR99 | — | ✅ |
| 102 | TrxRevLineCreatedBy | CREATED_BY | — | ✅ |
| 103 | TrxRevLineDate1 | DATE1 | — | ✅ |
| 104 | TrxRevLineDate10 | DATE10 | — | ✅ |
| 105 | TrxRevLineDate2 | DATE2 | — | ✅ |
| 106 | TrxRevLineDate3 | DATE3 | — | ✅ |
| 107 | TrxRevLineDate4 | DATE4 | — | ✅ |
| 108 | TrxRevLineDate5 | DATE5 | — | ✅ |
| 109 | TrxRevLineDate6 | DATE6 | — | ✅ |
| 110 | TrxRevLineDate7 | DATE7 | — | ✅ |
| 111 | TrxRevLineDate8 | DATE8 | — | ✅ |
| 112 | TrxRevLineDate9 | DATE9 | — | ✅ |
| 113 | TrxRevLineEventId | EVENT_ID | 🔑 | ✅ |
| 114 | TrxRevLineJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 115 | TrxRevLineJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 116 | TrxRevLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 117 | TrxRevLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 118 | TrxRevLineLineNumber | LINE_NUMBER | 🔑 | ✅ |
| 119 | TrxRevLineLongChar1 | LONG_CHAR1 | — | ✅ |
| 120 | TrxRevLineLongChar2 | LONG_CHAR2 | — | ✅ |
| 121 | TrxRevLineLongChar3 | LONG_CHAR3 | — | ✅ |
| 122 | TrxRevLineLongChar4 | LONG_CHAR4 | — | ✅ |
| 123 | TrxRevLineLongChar5 | LONG_CHAR5 | — | ✅ |
| 124 | TrxRevLineNumber1 | NUMBER1 | — | ✅ |
| 125 | TrxRevLineNumber10 | NUMBER10 | — | ✅ |
| 126 | TrxRevLineNumber11 | NUMBER11 | — | ✅ |
| 127 | TrxRevLineNumber12 | NUMBER12 | — | ✅ |
| 128 | TrxRevLineNumber13 | NUMBER13 | — | ✅ |
| 129 | TrxRevLineNumber14 | NUMBER14 | — | ✅ |
| 130 | TrxRevLineNumber15 | NUMBER15 | — | ✅ |
| 131 | TrxRevLineNumber16 | NUMBER16 | — | ✅ |
| 132 | TrxRevLineNumber17 | NUMBER17 | — | ✅ |
| 133 | TrxRevLineNumber18 | NUMBER18 | — | ✅ |
| 134 | TrxRevLineNumber19 | NUMBER19 | — | ✅ |
| 135 | TrxRevLineNumber2 | NUMBER2 | — | ✅ |
| 136 | TrxRevLineNumber20 | NUMBER20 | — | ✅ |
| 137 | TrxRevLineNumber21 | NUMBER21 | — | ✅ |
| 138 | TrxRevLineNumber22 | NUMBER22 | — | ✅ |
| 139 | TrxRevLineNumber23 | NUMBER23 | — | ✅ |
| 140 | TrxRevLineNumber24 | NUMBER24 | — | ✅ |
| 141 | TrxRevLineNumber25 | NUMBER25 | — | ✅ |
| 142 | TrxRevLineNumber26 | NUMBER26 | — | ✅ |
| 143 | TrxRevLineNumber27 | NUMBER27 | — | ✅ |
| 144 | TrxRevLineNumber28 | NUMBER28 | — | ✅ |
| 145 | TrxRevLineNumber29 | NUMBER29 | — | ✅ |
| 146 | TrxRevLineNumber3 | NUMBER3 | — | ✅ |
| 147 | TrxRevLineNumber30 | NUMBER30 | — | ✅ |
| 148 | TrxRevLineNumber4 | NUMBER4 | — | ✅ |
| 149 | TrxRevLineNumber5 | NUMBER5 | — | ✅ |
| 150 | TrxRevLineNumber6 | NUMBER6 | — | ✅ |
| 151 | TrxRevLineNumber7 | NUMBER7 | — | ✅ |
| 152 | TrxRevLineNumber8 | NUMBER8 | — | ✅ |
| 153 | TrxRevLineNumber9 | NUMBER9 | — | ✅ |
| 154 | TrxRevLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 155 | TrxRevLineRequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
