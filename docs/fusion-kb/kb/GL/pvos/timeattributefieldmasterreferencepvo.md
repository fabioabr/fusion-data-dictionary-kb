---
id: DOC-GL-PVO-TimeAttributeFieldMasterReferencePVO
doc_type: system-doc
title: "TimeAttributeFieldMasterReferencePVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TimeAttributeFieldMasterReferencePVO
  - timeattributefieldmasterreferencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeAttributeFieldMasterReferencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Attribute Field Master Reference. Acessa as tabelas: HWM_TM_ATRB_FLD_MSTR_REF_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DataDictionaryAM.TimeAttributeFieldMasterReferencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_atrb_fld_mstr_ref_b|HWM_TM_ATRB_FLD_MSTR_REF_B]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_atrb_fld_mstr_ref_b|HWM_TM_ATRB_FLD_MSTR_REF_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DetailInstanceAttributeType | DET_INS_ATTRIBUTE_TYPE | — | ✅ |
| 4 | DetailInstanceValueLocation | DET_INS_VALUE_LOCATION | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 12 | MasterInstanceIdentifier | MASTER_INSTANCE_IDENTIFIER | — | ✅ |
| 13 | ModuleId | MODULE_ID | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | StartDate | START_DATE | — | ✅ |
| 16 | TimeAttributeFieldEssProcessId | TM_ATRB_FLD_ESS_PROCESS_ID | — | ✅ |
| 17 | TimeAttributeFieldId | TM_ATRB_FLD_ID | — | ✅ |
| 18 | TimeAttributeFieldMasterReferenceCode | TM_ATRB_FLD_MSTR_REF_CODE | — | ✅ |
| 19 | TimeAttributeFieldMasterReferenceId | TM_ATRB_FLD_MSTR_REF_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
