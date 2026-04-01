---
id: DOC-OTHER-PVO-AwardCFDAExtractPVO
doc_type: system-doc
title: "AwardCFDAExtractPVO — PVO Cross-Module"
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
  - AwardCFDAExtractPVO
  - awardcfdaextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardCFDAExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award CFDAExtract. Acessa as tabelas: GMS_AWARD_CFDAS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardCFDAExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_cfdas|GMS_AWARD_CFDAS]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[gms_award_cfdas|GMS_AWARD_CFDAS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardCFDAPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardCFDAPEOCfda | CFDA | — | ✅ |
| 3 | AwardCFDAPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardCFDAPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardCFDAPEOId | ID | 🔑 | ✅ |
| 6 | AwardCFDAPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardCFDAPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardCFDAPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardCFDAPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
