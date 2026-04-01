---
id: DOC-OTHER-PVO-AwardCFDAPVO
doc_type: system-doc
title: "AwardCFDAPVO — PVO Cross-Module"
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
  - AwardCFDAPVO
  - awardcfdapvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardCFDAPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award CFDA. Acessa as tabelas: GMS_AWARD_CFDAS, GMS_CFDAS_VL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardCFDAPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 2 | 1 | 8 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_cfdas|GMS_AWARD_CFDAS]] — 9 atributos (1 PKs, 2 BICC)
- [[gms_cfdas_vl|GMS_CFDAS_VL]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[gms_award_cfdas|GMS_AWARD_CFDAS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCFDAPEOAwardId | AWARD_ID | — | — |
| 2 | AwardCFDAPEOCfda | CFDA | — | — |
| 3 | AwardCFDAPEOCreatedBy | CREATED_BY | — | — |
| 4 | AwardCFDAPEOCreationDate | CREATION_DATE | — | — |
| 5 | AwardCFDAPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AwardCFDAPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AwardCFDAPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AwardCFDAPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | Id | ID | 🔑 | ✅ |

### [[gms_cfdas_vl|GMS_CFDAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CFDAPEOAgency | AGENCY | — | ✅ |
| 2 | CFDAPEOAssistanceType | ASSISTANCE_TYPE | — | ✅ |
| 3 | CFDAPEOCfda | CFDA | — | ✅ |
| 4 | CFDAPEOModifiedDate | MODIFIED_DATE | — | ✅ |
| 5 | CFDAPEOProgramTitle | PROGRAM_TITLE | — | ✅ |
| 6 | CFDAPEOPublishedDate | PUBLISHED_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
