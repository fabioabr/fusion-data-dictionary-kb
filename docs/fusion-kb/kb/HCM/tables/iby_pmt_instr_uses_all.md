---
id: DOC-HCM-522
doc_type: system-doc
title: "IBY_PMT_INSTR_USES_ALL — (título a preencher)"
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
  - IBY_PMT_INSTR_USES_ALL
  - iby_pmt_instr_uses_all
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_PMT_INSTR_USES_ALL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | END_DATE | — | — | — | — | — | — |
| 4 | EXT_PMT_PARTY_ID | — | — | — | — | — | — |
| 5 | INSTRUMENT_ID | — | — | — | — | — | — |
| 6 | INSTRUMENT_PAYMENT_USE_ID | — | — | — | — | — | — |
| 7 | INSTRUMENT_TYPE | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 12 | PAYMENT_FLOW | — | — | — | — | — | — |
| 13 | PAYMENT_FUNCTION | — | — | — | — | — | — |
| 14 | PRIMARY_FLAG | — | — | — | — | — | — |
| 15 | START_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountbankaccount|AccountBankAccount]] (AR · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | — |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | InstrumentPaymentUseId | ✅ |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | — |

### [[accountcreditcard|AccountCreditCard]] (AR · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | — |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | InstrumentPaymentUseId | ✅ |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | ✅ |

### [[sitebankaccount|SiteBankAccount]] (AR · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | — |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | InstrumentPaymentUseId | ✅ |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | — |

### [[sitecreditcard|SiteCreditCard]] (AR · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | — |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | InstrumentPaymentUseId | ✅ |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | ✅ |

### [[supplieraddressbankaccountpvo|SupplierAddressBankAccountPVO]] (PO · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | ✅ |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | UseInstrumentPaymentUseId | — |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | ✅ |

### [[supplierbankaccountpvo|SupplierBankAccountPVO]] (PO · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | ✅ |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | UseInstrumentPaymentUseId | — |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | ✅ |

### [[suppliersitebankaccountpvo|SupplierSiteBankAccountPVO]] (PO · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UseCreatedBy | — |
| CREATION_DATE | UseCreationDate | — |
| END_DATE | UseEndDate | ✅ |
| EXT_PMT_PARTY_ID | UseExtPmtPartyId | — |
| INSTRUMENT_ID | UseInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | UseInstrumentPaymentUseId | — |
| INSTRUMENT_TYPE | UseInstrumentType | — |
| LAST_UPDATE_DATE | UseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UseLastUpdateLogin | — |
| LAST_UPDATED_BY | UseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UseObjectVersionNumber | — |
| PAYMENT_FLOW | UsePaymentFlow | — |
| PAYMENT_FUNCTION | UsePaymentFunction | — |
| PRIMARY_FLAG | UsePrimaryFlag | ✅ |
| START_DATE | UseStartDate | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INSTRUMENT_ID | DraweeToAccountInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | DraweeToAccountInstrumentPaymentUseId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INSTRUMENT_ID | DraweeToAccountInstrumentId | — |
| INSTRUMENT_PAYMENT_USE_ID | DraweeToAccountInstrumentPaymentUseId | — |
