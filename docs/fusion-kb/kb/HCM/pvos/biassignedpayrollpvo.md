---
id: DOC-HCM-PVO-BIAssignedPayrollPVO
doc_type: system-doc
title: "BIAssignedPayrollPVO — PVO Human Capital Management"
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
  - BIAssignedPayrollPVO
  - biassignedpayrollpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIAssignedPayrollPVO

## 📌 Visão Geral

Disponibiliza payrolls atribuidos (versao denormalizada) para extracao BICC. Base para identificacao do vinculo entre colaborador e folha de pagamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmPayRegsBiccExtractAM.BIAssignedPayrollPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_assigned_payrolls_dn|PAY_ASSIGNED_PAYROLLS_DN]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[pay_assigned_payrolls_dn|PAY_ASSIGNED_PAYROLLS_DN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayrollUsagePEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | 🔑 | ✅ |
| 2 | PayrollUsagePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PayrollUsagePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PayrollUsagePEOEndDate | END_DATE | — | ✅ |
| 5 | PayrollUsagePEOFinc | FINC | — | ✅ |
| 6 | PayrollUsagePEOFsed | FSED | — | ✅ |
| 7 | PayrollUsagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PayrollUsagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PayrollUsagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PayrollUsagePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 11 | PayrollUsagePEOLsed | LSED | — | ✅ |
| 12 | PayrollUsagePEOLspd | LSPD | — | ✅ |
| 13 | PayrollUsagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PayrollUsagePEOPayrollId | PAYROLL_ID | — | ✅ |
| 15 | PayrollUsagePEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 16 | PayrollUsagePEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
