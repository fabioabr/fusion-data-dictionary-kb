---
id: DOC-HCM-138
doc_type: system-doc
title: "FND_SETID_SETS_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_SETID_SETS_VL
  - fnd_setid_sets_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_SETID_SETS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESCRIPTION | — | — | — | — | — | — |
| 2 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 3 | SET_CODE | — | — | — | — | — | — |
| 4 | SET_ID | — | — | — | — | — | — |
| 5 | SET_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[businessunitpvo|BusinessUnitPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[costelementpvo|CostElementPVO]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | ✅ |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[custacctsiteuseloc|CustAcctSiteUseLoc]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SET_CODE | SetIdSetSetCode | — |
| SET_ID | SetIdSetSetId | ✅ |
| SET_NAME | CustomerAccountSiteSetId | ✅ |

### [[departmentpvo|DepartmentPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[departmentpvoviewall|DepartmentPVOViewAll]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[enterprisepvo|EnterprisePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[gradeladderpvo|GradeLadderPVO]] (GL · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[gradepvo|GradePVO]] (GL · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 5/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | ✅ |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | ✅ |
| SET_ID | SetIdSetPEOSetId | ✅ |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[jobpvo|JobPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[jobpvoviewall|JobPVOViewAll]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[legalemployerpvo|LegalEmployerPVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | ✅ |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[locationpvo|LocationPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | ✅ |
| SET_CODE | SetIdSetPEOSetCode | ✅ |
| SET_ID | SetIdSetPEOSetId | ✅ |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | ✅ |
| SET_CODE | SetIdSetsSetCode | ✅ |
| SET_ID | SetIdSetsSetId | ✅ |
| SET_NAME | SetIdSetsSetName | ✅ |

### [[organizationpvo|OrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[orgunitclassificationpvo|OrgUnitClassificationPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | ✅ |
| SET_CODE | SetIdSetPEOSetCode | ✅ |
| SET_ID | SetIdSetPEOSetId | ✅ |
| SET_NAME | SetIdSetPEOSetName | ✅ |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[payrollstatutoryunitpvo|PayrollStatutoryUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[project|Project]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[projectexec|ProjectExec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectexpenditureorganizationpvo|ProjectExpenditureOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[projecttaskowningorganizationpvo|ProjectTaskOwningOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectunitclassificationpvo|ProjectUnitClassificationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[projectview|ProjectView]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetsDescription | — |
| SET_CODE | SetIdSetsSetCode | — |
| SET_ID | SetIdSetsSetId | — |
| SET_NAME | SetIdSetsSetName | — |

### [[reportingestablishmentpvo|ReportingEstablishmentPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[reportingestablishmentpvoviewall|ReportingEstablishmentPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[taxreportingunitpvo|TaxReportingUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | — |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |

### [[unionpvo|UnionPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | SetIdSetPEODescription | — |
| LAST_UPDATE_DATE | SetIdSetPEOLastUpdateDate | ✅ |
| SET_CODE | SetIdSetPEOSetCode | — |
| SET_ID | SetIdSetPEOSetId | — |
| SET_NAME | SetIdSetPEOSetName | — |
