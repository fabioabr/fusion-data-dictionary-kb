---
id: DOC-AR-PVO-ReferenceAccount
doc_type: system-doc
title: "ReferenceAccount — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ReferenceAccount
  - referenceaccount
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceAccount

## 📌 Visão Geral

Extrai as contas de referência de Contas a Receber, mapeando combinações contábeis (code combinations) por unidade de negócio e vendedor. Define o plano de contas padrão para contabilização automática das transações de recebíveis.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ReferenceAccount`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 6 | 3 | 5 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[ar_ref_accounts_all|AR_REF_ACCOUNTS_ALL]] — 11 atributos (3 PKs, 3 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 3 atributos (1 BICC)
- [[gl_code_combinations|GL_CODE_COMBINATIONS]] — 7 atributos
- [[gl_ledgers|GL_LEDGERS]] — 4 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[jtf_rs_salesreps|JTF_RS_SALESREPS]] — 3 atributos

---

## ⚙️ Atributos

### [[ar_ref_accounts_all|AR_REF_ACCOUNTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuId | BU_ID | 🔑 | ✅ |
| 2 | FreightCcid | FREIGHT_CCID | — | — |
| 3 | LedgerId | LEDGER_ID | — | — |
| 4 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | RecCcid | REC_CCID | — | — |
| 6 | RevCcid | REV_CCID | — | — |
| 7 | SourceRefAccountId | SOURCE_REF_ACCOUNT_ID | 🔑 | ✅ |
| 8 | SourceRefTable | SOURCE_REF_TABLE | 🔑 | ✅ |
| 9 | TaxCcid | TAX_CCID | — | — |
| 10 | UnbilledCcid | UNBILLED_CCID | — | — |
| 11 | UnearnedCcid | UNEARNED_CCID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitName | BU_NAME | — | ✅ |
| 3 | BusinessUnitStatus | STATUS | — | — |

### [[gl_code_combinations|GL_CODE_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeCombinationClearingCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 2 | CodeCombinationFreightCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 3 | CodeCombinationRecCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | CodeCombinationRevCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | CodeCombinationTaxCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 6 | CodeCombinationUnbilledCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | CodeCombinationUnearnedCodeCombinationId | CODE_COMBINATION_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 3 | GlLedgersName | NAME | — | ✅ |
| 4 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[jtf_rs_salesreps|JTF_RS_SALESREPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceSalesrepResourceId | RESOURCE_ID | — | — |
| 2 | ResourceSalesrepResourceSalesrepId | RESOURCE_SALESREP_ID | — | — |
| 3 | ResourceSalesrepStatus | STATUS | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
