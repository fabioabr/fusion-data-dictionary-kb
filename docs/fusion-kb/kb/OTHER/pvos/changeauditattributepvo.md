---
id: DOC-OTHER-PVO-ChangeAuditAttributePVO
doc_type: system-doc
title: "ChangeAuditAttributePVO — PVO Cross-Module"
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
  - ChangeAuditAttributePVO
  - changeauditattributepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeAuditAttributePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Audit Attribute. Acessa as tabelas: HWM_TM_ATRB_FLDS_VL, HWM_TM_AUDITS, HWM_TM_AUDIT_ATRBS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.ChangeAuditAttributePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 3 | 1 | 29 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 2 atributos (1 BICC)
- [[hwm_tm_audits|HWM_TM_AUDITS]] — 18 atributos (11 BICC)
- [[hwm_tm_audit_atrbs|HWM_TM_AUDIT_ATRBS]] — 28 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TmAtrbFieldVLPEOName | NAME | — | ✅ |
| 2 | TmAtrbFieldVLPEOTmAtrbFldId1 | TM_ATRB_FLD_ID | — | — |

### [[hwm_tm_audits|HWM_TM_AUDITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeAuditPEOActionType1 | ACTION_TYPE | — | ✅ |
| 2 | ChangeAuditPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 3 | ChangeAuditPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 4 | ChangeAuditPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 5 | ChangeAuditPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | ChangeAuditPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ChangeAuditPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 8 | ChangeAuditPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 9 | ChangeAuditPEOOrigAuditId | ORIG_AUDIT_ID | — | — |
| 10 | ChangeAuditPEOReasonCode1 | REASON_CODE | — | ✅ |
| 11 | ChangeAuditPEORefDate | REF_DATE | — | ✅ |
| 12 | ChangeAuditPEOTmAuditId1 | TM_AUDIT_ID | — | ✅ |
| 13 | ChangeAuditPEOTmBlkId | TM_BLK_ID | — | ✅ |
| 14 | ChangeAuditPEOTmBlkVersion | TM_BLK_VERSION | — | — |
| 15 | ChangeAuditPEOTmNewBlkId | TM_NEW_BLK_ID | — | — |
| 16 | ChangeAuditPEOTmNewBlkVersion | TM_NEW_BLK_VERSION | — | — |
| 17 | ChangeAuditPEOTmRecordGrpId | TM_RECORD_GRP_ID | — | ✅ |
| 18 | ChangeAuditPEOUsagesType | USAGES_TYPE | — | — |

### [[hwm_tm_audit_atrbs|HWM_TM_AUDIT_ATRBS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeAuditAttributePEOActionType | ACTION_TYPE | — | ✅ |
| 2 | ChangeAuditAttributePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ChangeAuditAttributePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ChangeAuditAttributePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ChangeAuditAttributePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ChangeAuditAttributePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ChangeAuditAttributePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ChangeAuditAttributePEONewDate | NEW_DATE | — | ✅ |
| 9 | ChangeAuditAttributePEONewGmtOffset | NEW_GMT_OFFSET | — | — |
| 10 | ChangeAuditAttributePEONewNumber | NEW_NUMBER | — | ✅ |
| 11 | ChangeAuditAttributePEONewTimestamp | NEW_TIMESTAMP | — | ✅ |
| 12 | ChangeAuditAttributePEONewTimezoneCode | NEW_TIMEZONE_CODE | — | — |
| 13 | ChangeAuditAttributePEONewVarchar | NEW_VARCHAR | — | ✅ |
| 14 | ChangeAuditAttributePEONewZoneType | NEW_ZONE_TYPE | — | — |
| 15 | ChangeAuditAttributePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ChangeAuditAttributePEOOldDate | OLD_DATE | — | ✅ |
| 17 | ChangeAuditAttributePEOOldGmtOffset | OLD_GMT_OFFSET | — | — |
| 18 | ChangeAuditAttributePEOOldNumber | OLD_NUMBER | — | ✅ |
| 19 | ChangeAuditAttributePEOOldTimestamp | OLD_TIMESTAMP | — | ✅ |
| 20 | ChangeAuditAttributePEOOldTimezoneCode | OLD_TIMEZONE_CODE | — | — |
| 21 | ChangeAuditAttributePEOOldVarchar | OLD_VARCHAR | — | ✅ |
| 22 | ChangeAuditAttributePEOOldZoneType | OLD_ZONE_TYPE | — | — |
| 23 | ChangeAuditAttributePEOOrigAuditAtrbId | ORIG_AUDIT_ATRB_ID | — | — |
| 24 | ChangeAuditAttributePEOReasonCode | REASON_CODE | — | ✅ |
| 25 | ChangeAuditAttributePEOTmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 26 | ChangeAuditAttributePEOTmAttributeType | TM_ATTRIBUTE_TYPE | — | — |
| 27 | ChangeAuditAttributePEOTmAuditAtrbId | TM_AUDIT_ATRB_ID | 🔑 | ✅ |
| 28 | ChangeAuditAttributePEOTmAuditId | TM_AUDIT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
