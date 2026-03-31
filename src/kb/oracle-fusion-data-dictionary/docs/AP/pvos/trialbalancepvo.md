---
id: DOC-AP-PVO-TrialBalancePVO
doc_type: system-doc
title: "TrialBalancePVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TrialBalancePVO
  - trialbalancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TrialBalancePVO

## 📌 Visão Geral

Extrai o balancete de verificação do contas a pagar, incluindo débitos e créditos contabilizados por fornecedor, conta contábil e fatura. Fundamental para fechamento contábil, conciliação de saldos de fornecedores e validação dos lançamentos de contas a pagar.

**Caminho:** `FscmTopModelAM.FinApSharedCoreAM.TrialBalancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 6 | 4 | 15 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 2 atributos
- [[ap_trial_balances|AP_TRIAL_BALANCES]] — 28 atributos (4 PKs, 12 BICC)
- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvHdrInvoiceId | INVOICE_ID | — | — |
| 2 | InvHdrLegalEntityId | LEGAL_ENTITY_ID | — | — |

### [[ap_trial_balances|AP_TRIAL_BALANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | AeHeaderId | AE_HEADER_ID | 🔑 | ✅ |
| 3 | InvoiceId | INVOICE_ID | 🔑 | ✅ |
| 4 | TrialBalanceAccountedCr | ACCOUNTED_CR | — | ✅ |
| 5 | TrialBalanceAccountedDr | ACCOUNTED_DR | — | ✅ |
| 6 | TrialBalanceAccountingClassCode | ACCOUNTING_CLASS_CODE | 🔑 | ✅ |
| 7 | TrialBalanceBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 8 | TrialBalanceCodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 9 | TrialBalanceCreatedBy | CREATED_BY | — | ✅ |
| 10 | TrialBalanceCreationDate | CREATION_DATE | — | ✅ |
| 11 | TrialBalanceEnteredCr | ENTERED_CR | — | ✅ |
| 12 | TrialBalanceEnteredDr | ENTERED_DR | — | ✅ |
| 13 | TrialBalanceJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 14 | TrialBalanceJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 15 | TrialBalanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | TrialBalanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | TrialBalanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | TrialBalanceLedgerId | LEDGER_ID | — | — |
| 19 | TrialBalanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | TrialBalancePartyId | PARTY_ID | — | — |
| 21 | TrialBalancePartySiteId | PARTY_SITE_ID | — | — |
| 22 | TrialBalanceProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 23 | TrialBalanceProgramId | PROGRAM_ID | — | — |
| 24 | TrialBalanceProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 25 | TrialBalanceRequestId | REQUEST_ID | — | — |
| 26 | TrialBalanceTrxCurrencyCode | TRX_CURRENCY_CODE | — | — |
| 27 | TrialBalanceVendorId | VENDOR_ID | — | — |
| 28 | TrialBalanceVendorSiteId | VENDOR_SITE_ID | — | — |

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPartyId | PARTY_ID | — | — |
| 2 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 2 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName1 | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
