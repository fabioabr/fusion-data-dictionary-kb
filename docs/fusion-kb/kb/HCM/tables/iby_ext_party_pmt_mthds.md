---
id: DOC-HCM-514
doc_type: system-doc
title: "IBY_EXT_PARTY_PMT_MTHDS — (título a preencher)"
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
  - IBY_EXT_PARTY_PMT_MTHDS
  - iby_ext_party_pmt_mthds
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_EXT_PARTY_PMT_MTHDS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | END_DATE | — | — | — | — | — | — |
| 4 | EXT_PARTY_PMT_MTHD_ID | — | — | — | — | — | — |
| 5 | EXT_PMT_PARTY_ID | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 10 | PAYMENT_FLOW | — | — | — | — | — | — |
| 11 | PAYMENT_FUNCTION | — | — | — | — | — | — |
| 12 | PAYMENT_METHOD_CODE | — | — | — | — | — | — |
| 13 | PRIMARY_FLAG | — | — | — | — | — | — |
| 14 | START_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[supplieraddressbankaccountpvo|SupplierAddressBankAccountPVO]] (PO · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartyPayMethodCreatedBy | — |
| CREATION_DATE | PartyPayMethodCreationDate | — |
| END_DATE | PartyPayMethodEndDate | ✅ |
| EXT_PARTY_PMT_MTHD_ID | PartyPayMethodExtPartyPmtMthdId | — |
| EXT_PMT_PARTY_ID | PartyPayMethodExtPmtPartyId | — |
| LAST_UPDATE_DATE | PartyPayMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyPayMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyPayMethodLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartyPayMethodObjectVersionNumber | — |
| PAYMENT_FLOW | PartyPayMethodPaymentFlow | — |
| PAYMENT_FUNCTION | PartyPayMethodPaymentFunction | — |
| PAYMENT_METHOD_CODE | PartyPayMethodPaymentMethodCode | — |
| PRIMARY_FLAG | PartyPayMethodPrimaryFlag | — |
| START_DATE | PartyPayMethodStartDate | ✅ |

### [[supplierbankaccountpvo|SupplierBankAccountPVO]] (PO · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartyPayMethodCreatedBy | — |
| CREATION_DATE | PartyPayMethodCreationDate | — |
| END_DATE | PartyPayMethodEndDate | ✅ |
| EXT_PARTY_PMT_MTHD_ID | PartyPayMethodExtPartyPmtMthdId | — |
| EXT_PMT_PARTY_ID | PartyPayMethodExtPmtPartyId | — |
| LAST_UPDATE_DATE | PartyPayMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyPayMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyPayMethodLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartyPayMethodObjectVersionNumber | — |
| PAYMENT_FLOW | PartyPayMethodPaymentFlow | — |
| PAYMENT_FUNCTION | PartyPayMethodPaymentFunction | — |
| PAYMENT_METHOD_CODE | PartyPayMethodPaymentMethodCode | — |
| PRIMARY_FLAG | PartyPayMethodPrimaryFlag | — |
| START_DATE | PartyPayMethodStartDate | ✅ |

### [[suppliersitebankaccountpvo|SupplierSiteBankAccountPVO]] (PO · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PartyPayMethodCreatedBy | — |
| CREATION_DATE | PartyPayMethodCreationDate | — |
| END_DATE | PartyPayMethodEndDate | ✅ |
| EXT_PARTY_PMT_MTHD_ID | PartyPayMethodExtPartyPmtMthdId | — |
| EXT_PMT_PARTY_ID | PartyPayMethodExtPmtPartyId | — |
| LAST_UPDATE_DATE | PartyPayMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyPayMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyPayMethodLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartyPayMethodObjectVersionNumber | — |
| PAYMENT_FLOW | PartyPayMethodPaymentFlow | — |
| PAYMENT_FUNCTION | PartyPayMethodPaymentFunction | — |
| PAYMENT_METHOD_CODE | PartyPayMethodPaymentMethodCode | — |
| PRIMARY_FLAG | PartyPayMethodPrimaryFlag | — |
| START_DATE | PartyPayMethodStartDate | ✅ |
