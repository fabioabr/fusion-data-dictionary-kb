---
id: DOC-HCM-PVO-BIEntryUsagePVO
doc_type: system-doc
title: "BIEntryUsagePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BIEntryUsagePVO
  - bientryusagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIEntryUsagePVO

## 📌 Visão Geral

Relaciona usos de lancamentos (entry usages) com payrolls atribuidos. Controla a aplicacao de element entries em contextos especificos de folha.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmElementSetupBiccExtractAM.BIEntryUsagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_entry_usages|PAY_ENTRY_USAGES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[pay_entry_usages|PAY_ENTRY_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EntryUsagePEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | — | ✅ |
| 2 | EntryUsagePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | EntryUsagePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EntryUsagePEODateFrom | DATE_FROM | — | ✅ |
| 5 | EntryUsagePEODateTo | DATE_TO | — | ✅ |
| 6 | EntryUsagePEOElementEntryId | ELEMENT_ENTRY_ID | — | ✅ |
| 7 | EntryUsagePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | EntryUsagePEOEntryUsageId | ENTRY_USAGE_ID | 🔑 | ✅ |
| 9 | EntryUsagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EntryUsagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | EntryUsagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | EntryUsagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | EntryUsagePEOPayrollAssignmentId | PAYROLL_ASSIGNMENT_ID | — | ✅ |
| 14 | EntryUsagePEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | ✅ |
| 15 | EntryUsagePEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 16 | EntryUsagePEOUsageLevel | USAGE_LEVEL | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
