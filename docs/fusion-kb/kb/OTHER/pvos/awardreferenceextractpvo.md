---
id: DOC-OTHER-PVO-AwardReferenceExtractPVO
doc_type: system-doc
title: "AwardReferenceExtractPVO — PVO Cross-Module"
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
  - AwardReferenceExtractPVO
  - awardreferenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardReferenceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Reference Extract. Acessa as tabelas: GMS_AWARD_REFERENCES_B, GMS_AWARD_REFERENCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_references_b|GMS_AWARD_REFERENCES_B]] — 11 atributos (1 PKs, 11 BICC)
- [[gms_award_references_tl|GMS_AWARD_REFERENCES_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[gms_award_references_b|GMS_AWARD_REFERENCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardReferenceBaseAwardId | AWARD_ID | — | ✅ |
| 2 | AwardReferenceBaseAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardReferenceBaseCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardReferenceBaseCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardReferenceBaseId | ID | 🔑 | ✅ |
| 6 | AwardReferenceBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardReferenceBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardReferenceBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardReferenceBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AwardReferenceBaseReferenceType | REFERENCE_TYPE | — | ✅ |
| 11 | AwardReferenceBaseReferenceValue | REFERENCE_VALUE | — | ✅ |

### [[gms_award_references_tl|GMS_AWARD_REFERENCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardReferenceTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardReferenceTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardReferenceTransLangId | ID | — | ✅ |
| 4 | AwardReferenceTransLangLanguage | LANGUAGE | — | ✅ |
| 5 | AwardReferenceTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AwardReferenceTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AwardReferenceTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AwardReferenceTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | AwardReferenceTransLangReferenceComment | REFERENCE_COMMENT | — | ✅ |
| 10 | AwardReferenceTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
