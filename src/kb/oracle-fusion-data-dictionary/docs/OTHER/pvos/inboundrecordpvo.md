---
id: DOC-OTHER-PVO-InboundRecordPVO
doc_type: system-doc
title: "InboundRecordPVO — PVO Cross-Module"
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
  - InboundRecordPVO
  - inboundrecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InboundRecordPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inbound Record. Acessa as tabelas: HRY_PI_INBD_RECORDS, PAY_PAY_RELATIONSHIPS_DN.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayInboundRecordAM.InboundRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 2 | 29 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[hry_pi_inbd_records|HRY_PI_INBD_RECORDS]] — 26 atributos (1 PKs, 25 BICC)
- [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]] — 4 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hry_pi_inbd_records|HRY_PI_INBD_RECORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InbdRecordId | INBD_RECORD_ID | 🔑 | ✅ |
| 2 | InboundRecordPEOBatchCode | BATCH_CODE | — | ✅ |
| 3 | InboundRecordPEOBatchDate | BATCH_DATE | — | ✅ |
| 4 | InboundRecordPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 5 | InboundRecordPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InboundRecordPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InboundRecordPEODocumentsOfRecordId | DOCUMENTS_OF_RECORD_ID | — | ✅ |
| 8 | InboundRecordPEOEndDate | END_DATE | — | ✅ |
| 9 | InboundRecordPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 10 | InboundRecordPEOEntityIdentifier | ENTITY_IDENTIFIER | — | ✅ |
| 11 | InboundRecordPEOFunctionalCategory | FUNCTIONAL_CATEGORY | — | ✅ |
| 12 | InboundRecordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | InboundRecordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | InboundRecordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | InboundRecordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | InboundRecordPEOPayrollAssignmentId | PAYROLL_ASSIGNMENT_ID | — | ✅ |
| 17 | InboundRecordPEOPayrollId | PAYROLL_ID | — | ✅ |
| 18 | InboundRecordPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | — |
| 19 | InboundRecordPEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 20 | InboundRecordPEOPersonId | PERSON_ID | — | ✅ |
| 21 | InboundRecordPEORecordType | RECORD_TYPE | — | ✅ |
| 22 | InboundRecordPEOSourceId | SOURCE_ID | — | ✅ |
| 23 | InboundRecordPEOSourceType | SOURCE_TYPE | — | ✅ |
| 24 | InboundRecordPEOStartDate | START_DATE | — | ✅ |
| 25 | InboundRecordPEOTimePeriodId | TIME_PERIOD_ID | — | ✅ |
| 26 | InboundRecordPEOVendorCode | VENDOR_CODE | — | ✅ |

### [[pay_pay_relationships_dn|PAY_PAY_RELATIONSHIPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 2 | PayrollRelationshipPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | PayrollRelationshipPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | 🔑 | ✅ |
| 4 | PayrollRelationshipPEOPayrollStatUnitId | PAYROLL_STAT_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
