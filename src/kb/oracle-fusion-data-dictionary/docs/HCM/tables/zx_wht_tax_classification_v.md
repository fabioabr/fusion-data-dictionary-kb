---
id: DOC-HCM-915
doc_type: system-doc
title: "ZX_WHT_TAX_CLASSIFICATION_V — (título a preencher)"
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
  - ZX_WHT_TAX_CLASSIFICATION_V
  - zx_wht_tax_classification_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_WHT_TAX_CLASSIFICATION_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | GROUP_ID | — | — | — | — | — | — |
| 5 | INACTIVE_DATE | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | NAME | — | — | — | — | — | — |
| 10 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 3/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WithholdingTaxGrpExpCreatedBy | — |
| CREATED_BY | WithholdingTaxGrpExpRptCreatedBy | — |
| CREATED_BY | WithholdingTaxGrpInvCreatedBy | — |
| CREATION_DATE | WithholdingTaxGrpExpCreationDate | — |
| CREATION_DATE | WithholdingTaxGrpExpRptCreationDate | — |
| CREATION_DATE | WithholdingTaxGrpInvCreationDate | — |
| DESCRIPTION | WithholdingTaxGrpExpDescription | — |
| DESCRIPTION | WithholdingTaxGrpExpRptDescription | — |
| DESCRIPTION | WithholdingTaxGrpInvDescription | — |
| GROUP_ID | WithholdingTaxGrpExpGroupId | — |
| GROUP_ID | WithholdingTaxGrpExpRptGroupId | — |
| GROUP_ID | WithholdingTaxGrpInvGroupId | — |
| INACTIVE_DATE | WithholdingTaxGrpExpInactiveDate | — |
| INACTIVE_DATE | WithholdingTaxGrpExpRptInactiveDate | — |
| INACTIVE_DATE | WithholdingTaxGrpInvInactiveDate | — |
| LAST_UPDATE_DATE | WithholdingTaxGrpExpLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WithholdingTaxGrpExpRptLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WithholdingTaxGrpInvLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WithholdingTaxGrpExpLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | WithholdingTaxGrpExpRptLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | WithholdingTaxGrpInvLastUpdateLogin | — |
| LAST_UPDATED_BY | WithholdingTaxGrpExpLastUpdatedBy | — |
| LAST_UPDATED_BY | WithholdingTaxGrpExpRptLastUpdatedBy | — |
| LAST_UPDATED_BY | WithholdingTaxGrpInvLastUpdatedBy | — |
| NAME | WithholdingTaxGrpExpName | — |
| NAME | WithholdingTaxGrpExpRptName | — |
| NAME | WithholdingTaxGrpInvName | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGrpExpObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGrpExpRptObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGrpInvObjectVersionNumber | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WithholdingTaxGroupExpCreatedBy | — |
| CREATED_BY | WithholdingTaxGroupExpRptCreatedBy | — |
| CREATION_DATE | WithholdingTaxGroupExpCreationDate | — |
| CREATION_DATE | WithholdingTaxGroupExpRptCreationDate | — |
| DESCRIPTION | WithholdingTaxGroupExpDescription | — |
| DESCRIPTION | WithholdingTaxGroupExpRptDescription | — |
| GROUP_ID | WithholdingTaxGroupExpGroupId | — |
| GROUP_ID | WithholdingTaxGroupExpRptGroupId | — |
| INACTIVE_DATE | WithholdingTaxGroupExpInactiveDate | — |
| INACTIVE_DATE | WithholdingTaxGroupExpRptInactiveDate | — |
| LAST_UPDATE_DATE | WithholdingTaxGroupExpLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WithholdingTaxGroupExpRptLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WithholdingTaxGroupExpLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | WithholdingTaxGroupExpRptLastUpdateLogin | — |
| LAST_UPDATED_BY | WithholdingTaxGroupExpLastUpdatedBy | — |
| LAST_UPDATED_BY | WithholdingTaxGroupExpRptLastUpdatedBy | — |
| NAME | WithholdingTaxGroupExpName | — |
| NAME | WithholdingTaxGroupExpRptName | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGroupExpObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGroupExpRptObjectVersionNumber | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WithholdingTaxGroupCreatedBy | — |
| CREATION_DATE | WithholdingTaxGroupCreationDate | — |
| DESCRIPTION | WithholdingTaxGroupDescription | — |
| GROUP_ID | WithholdingTaxGroupGroupId | — |
| INACTIVE_DATE | WithholdingTaxGroupInactiveDate | — |
| LAST_UPDATE_DATE | WithholdingTaxGroupLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WithholdingTaxGroupLastUpdateLogin | — |
| LAST_UPDATED_BY | WithholdingTaxGroupLastUpdatedBy | — |
| NAME | WithholdingTaxGroupName | — |
| OBJECT_VERSION_NUMBER | WithholdingTaxGroupObjectVersionNumber | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| GROUP_ID | WithholdingTaxGroupGroupId | — |
| LAST_UPDATE_DATE | WithholdingTaxGroupLastUpdateDate | ✅ |

### [[supplierpvo|SupplierPVO]] (PO · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WithholdingTaxGroupsCreatedBy | — |
| CREATION_DATE | WithholdingTaxGroupsCreationDate | — |
| DESCRIPTION | WithholdingTaxGroupsDescription | — |
| GROUP_ID | WithholdingTaxGroupsGroupId | — |
| INACTIVE_DATE | WithholdingTaxGroupsInactiveDate | — |
| LAST_UPDATE_DATE | WithholdingTaxGroupsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WithholdingTaxGroupsLastUpdateLogin | — |
| LAST_UPDATED_BY | WithholdingTaxGroupsLastUpdatedBy | — |
| NAME | WithholdingTaxGroupsName | ✅ |
| OBJECT_VERSION_NUMBER | WithholdingTaxGroupsObjectVersionNumber | — |

### [[suppliersiteassignmentspvo|SupplierSiteAssignmentsPVO]] (PO · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ApAwtGroupsCreatedBy | ✅ |
| CREATION_DATE | ApAwtGroupsCreationDate | ✅ |
| DESCRIPTION | ApAwtGroupsDescription | ✅ |
| GROUP_ID | ApAwtGroupsGroupId | ✅ |
| INACTIVE_DATE | ApAwtGroupsInactiveDate | ✅ |
| LAST_UPDATE_DATE | ApAwtGroupsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApAwtGroupsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApAwtGroupsLastUpdatedBy | ✅ |
| NAME | ApAwtGroupsName | ✅ |
| OBJECT_VERSION_NUMBER | ApAwtGroupsObjectVersionNumber | ✅ |
