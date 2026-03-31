---
id: DOC-OTHER-PVO-EntitlementPVO
doc_type: system-doc
title: "EntitlementPVO — PVO Cross-Module"
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
  - EntitlementPVO
  - entitlementpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EntitlementPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Entitlement. Acessa as tabelas: GRC_OTBI_CTRL_CCM_ENT, GRC_OTBI_ENT_ACCESS, PER_PERSON_NAMES_F_V (+1).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.EntitlementPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 4 | 2 | 20 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[grc_otbi_ctrl_ccm_ent|GRC_OTBI_CTRL_CCM_ENT]] — 10 atributos
- [[grc_otbi_ent_access|GRC_OTBI_ENT_ACCESS]] — 18 atributos (2 PKs, 18 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_otbi_ctrl_ccm_ent|GRC_OTBI_CTRL_CCM_ENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntitlementCtrlPEOAcsPnts | ACCESS_POINTS | — | — |
| 2 | EntitlementCtrlPEOControlId | CONTROL_ID | — | — |
| 3 | EntitlementCtrlPEOCreatedBy | CREATED_BY | — | — |
| 4 | EntitlementCtrlPEOCrtnDate | CREATION_DATE | — | — |
| 5 | EntitlementCtrlPEOEntDispName | ENTITLEMENT_DISPLAY_NAME | — | — |
| 6 | EntitlementCtrlPEOEntId | ENTITLEMENT_ID | — | — |
| 7 | EntitlementCtrlPEOEntName | ENTITLEMENT_NAME | — | — |
| 8 | EntitlementCtrlPEOLstUpdtDt | LAST_UPDATE_DATE | — | — |
| 9 | EntitlementCtrlPEOLstUpdtLgn | LAST_UPDATE_LOGIN | — | — |
| 10 | EntitlementCtrlPEOLstUpdtdBy | LAST_UPDATED_BY | — | — |

### [[grc_otbi_ent_access|GRC_OTBI_ENT_ACCESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntitlementBasePEOAccessDesc | ACCESS_DESC | — | ✅ |
| 2 | EntitlementBasePEOAccessDispName | ACCESS_DISP_NAME | — | ✅ |
| 3 | EntitlementBasePEOAccessId | ACCESS_ID | 🔑 | ✅ |
| 4 | EntitlementBasePEOAccessName | ACCESS_NAME | — | ✅ |
| 5 | EntitlementBasePEOAccessType | ACCESS_TYPE | — | ✅ |
| 6 | EntitlementBasePEOAccessTypeId | ACCESS_TYPE_ID | — | ✅ |
| 7 | EntitlementBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | EntitlementBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | EntitlementBasePEODatasourceId | DATASOURCE_ID | — | ✅ |
| 10 | EntitlementBasePEOEntDesc | ENT_DESC | — | ✅ |
| 11 | EntitlementBasePEOEntDispName | ENT_DISP_NAME | — | ✅ |
| 12 | EntitlementBasePEOEntName | ENT_NAME | — | ✅ |
| 13 | EntitlementBasePEOEntitlementId | ENTITLEMENT_ID | 🔑 | ✅ |
| 14 | EntitlementBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | EntitlementBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | EntitlementBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | EntitlementBasePEORowNum | ROW_NUM | — | ✅ |
| 18 | EntitlementBasePEOStatus | STATUS | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | EntPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | EntPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | EntPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | EntPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | EntPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | EntPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | EntPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | EntPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | EntPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | EntCreatedByPersonId | PERSON_ID | — | — |
| 3 | EntCreatedByUserGuid | USER_GUID | — | — |
| 4 | EntCreatedByUserId | USER_ID | — | — |
| 5 | EntCreatedByUsername | USERNAME | — | — |
| 6 | EntUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | EntUpdatedByPersonId | PERSON_ID | — | — |
| 8 | EntUpdatedByUserGuid | USER_GUID | — | — |
| 9 | EntUpdatedByUserId | USER_ID | — | — |
| 10 | EntUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
