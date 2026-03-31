---
id: DOC-OTHER-PVO-BIPayrollRelationshipGroupPVO
doc_type: system-doc
title: "BIPayrollRelationshipGroupPVO — PVO Cross-Module"
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
  - BIPayrollRelationshipGroupPVO
  - bipayrollrelationshipgrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIPayrollRelationshipGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de BIPayroll Relationship Group. Acessa as tabelas: PAY_REL_GROUPS_DN.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmPayRegsBiccExtractAM.BIPayrollRelationshipGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_rel_groups_dn|PAY_REL_GROUPS_DN]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[pay_rel_groups_dn|PAY_REL_GROUPS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollRelationshipGroupPEOAcTriggerFlag | AC_TRIGGER_FLAG | — | ✅ |
| 2 | PayrollRelationshipGroupPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | PayrollRelationshipGroupPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 4 | PayrollRelationshipGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PayrollRelationshipGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PayrollRelationshipGroupPEOEndDate | END_DATE | — | ✅ |
| 7 | PayrollRelationshipGroupPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | PayrollRelationshipGroupPEOGroupType | GROUP_TYPE | — | ✅ |
| 9 | PayrollRelationshipGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PayrollRelationshipGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | PayrollRelationshipGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | PayrollRelationshipGroupPEOLegalEmployerId | LEGAL_EMPLOYER_ID | — | ✅ |
| 13 | PayrollRelationshipGroupPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 14 | PayrollRelationshipGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | PayrollRelationshipGroupPEOParentRelGroupId | PARENT_REL_GROUP_ID | — | ✅ |
| 16 | PayrollRelationshipGroupPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | ✅ |
| 17 | PayrollRelationshipGroupPEORelationshipGroupId | RELATIONSHIP_GROUP_ID | 🔑 | ✅ |
| 18 | PayrollRelationshipGroupPEOStartDate | START_DATE | — | ✅ |
| 19 | PayrollRelationshipGroupPEOTaxReportingUnitId | TAX_REPORTING_UNIT_ID | — | ✅ |
| 20 | PayrollRelationshipGroupPEOTermId | TERM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
