---
id: DOC-OTHER-PVO-TimeAttributeFieldMasterReferenceTranslationPVO
doc_type: system-doc
title: "TimeAttributeFieldMasterReferenceTranslationPVO — PVO Cross-Module"
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
  - TimeAttributeFieldMasterReferenceTranslationPVO
  - timeattributefieldmasterreferencetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeAttributeFieldMasterReferenceTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Attribute Field Master Reference Translation. Acessa as tabelas: HWM_TM_ATRB_FLD_MSTR_REF_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DataDictionaryAM.TimeAttributeFieldMasterReferenceTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_atrb_fld_mstr_ref_tl|HWM_TM_ATRB_FLD_MSTR_REF_TL]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_atrb_fld_mstr_ref_tl|HWM_TM_ATRB_FLD_MSTR_REF_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DetailInstanceDisplayName | DET_INS_DISPLAY_NAME | — | — |
| 4 | EnterpriseId | ENTERPRISE_ID | — | — |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |
| 11 | TimeAttributeFieldMasterReferenceId | TM_ATRB_FLD_MSTR_REF_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
