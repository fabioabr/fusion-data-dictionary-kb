---
id: DOC-PO-PVO-NegotiationRequirementExtractPVO
doc_type: system-doc
title: "NegotiationRequirementExtractPVO — PVO Purchasing"
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
  - NegotiationRequirementExtractPVO
  - negotiationrequirementextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationRequirementExtractPVO

## 📌 Visão Geral

Extrai requisitos de negociações para carga BICC, incluindo especificações técnicas e comerciais exigidas. Alimenta análises de complexidade e padronização dos processos de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationRequirementExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 2 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_requirements|PON_REQUIREMENTS]] — 45 atributos (2 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[pon_requirements|PON_REQUIREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsoluteSectionSequence | ABSOLUTE_SECTION_SEQUENCE | — | ✅ |
| 2 | AllowAttachmentCode | ALLOW_ATTACHMENT_CODE | — | ✅ |
| 3 | AllowComments | ALLOW_COMMENTS | — | ✅ |
| 4 | AuctionHeaderId | AUCTION_HEADER_ID | 🔑 | ✅ |
| 5 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | Datatype | DATATYPE | — | ✅ |
| 9 | DateValue | DATE_VALUE | — | ✅ |
| 10 | DatetimeValue | DATETIME_VALUE | — | ✅ |
| 11 | DispSeqNumber | DISP_SEQ_NUMBER | — | ✅ |
| 12 | DisplayTargetFlag | DISPLAY_TARGET_FLAG | — | ✅ |
| 13 | Hint | HINT | — | ✅ |
| 14 | IsQuestionBranch | IS_QUESTION_BRANCH | — | ✅ |
| 15 | KnockoutScore | KNOCKOUT_SCORE | — | ✅ |
| 16 | LastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 17 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | MaxScore | MAX_SCORE | — | ✅ |
| 21 | ModifiedDate | MODIFIED_DATE | — | ✅ |
| 22 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 23 | NumberValue | NUMBER_VALUE | — | ✅ |
| 24 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | ParentLevel | PARENT_LEVEL | — | ✅ |
| 26 | ParentRequirementId | PARENT_REQUIREMENT_ID | — | ✅ |
| 27 | PreviousRequirementId | PREVIOUS_REQUIREMENT_ID | — | ✅ |
| 28 | QuestionId | QUESTION_ID | — | ✅ |
| 29 | ReqDisplayNumber | REQ_DISPLAY_NUMBER | — | ✅ |
| 30 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 31 | RequirementName | REQUIREMENT_NAME | — | ✅ |
| 32 | RequirementText | REQUIREMENT_TEXT | — | ✅ |
| 33 | RequirementTreeLevel | REQUIREMENT_TREE_LEVEL | — | ✅ |
| 34 | RequirementType | REQUIREMENT_TYPE | — | ✅ |
| 35 | ResponseType | RESPONSE_TYPE | — | ✅ |
| 36 | RevisionNumber | REVISION_NUMBER | — | ✅ |
| 37 | RootRequirementId | ROOT_REQUIREMENT_ID | — | ✅ |
| 38 | ScoreId | SCORE_ID | — | ✅ |
| 39 | ScoringMethod | SCORING_METHOD | — | ✅ |
| 40 | ScoringType | SCORING_TYPE | — | ✅ |
| 41 | SectionId | SECTION_ID | — | ✅ |
| 42 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 43 | SupplierLevel | SUPPLIER_LEVEL | — | ✅ |
| 44 | TextValue | TEXT_VALUE | — | ✅ |
| 45 | Weight | WEIGHT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
