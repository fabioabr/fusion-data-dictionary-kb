---
id: DOC-HCM-490
doc_type: system-doc
title: "HZ_CUST_ACCT_SITES_ALL — (título a preencher)"
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
  - HZ_CUST_ACCT_SITES_ALL
  - hz_cust_acct_sites_all
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_CUST_ACCT_SITES_ALL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCT_SITE_LANGUAGE | — | — | — | — | — | — |
| 2 | BILL_TO_FLAG | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | CUSTOMER_CATEGORY_CODE | — | — | — | — | — | — |
| 7 | CUST_ACCOUNT_ID | — | — | — | — | — | — |
| 8 | CUST_ACCT_SITE_ID | — | — | — | — | — | — |
| 9 | ECE_TP_LOCATION_CODE | — | — | — | — | — | — |
| 10 | END_DATE | — | — | — | — | — | — |
| 11 | KEY_ACCOUNT_FLAG | — | — | — | — | — | — |
| 12 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 15 | MARKET_FLAG | — | — | — | — | — | — |
| 16 | ORIG_SYSTEM_REFERENCE | — | — | — | — | — | — |
| 17 | PARTY_SITE_ID | — | — | — | — | — | — |
| 18 | SET_ID | — | — | — | — | — | — |
| 19 | SHIP_TO_FLAG | — | — | — | — | — | — |
| 20 | START_DATE | — | — | — | — | — | — |
| 21 | STATUS | — | — | — | — | — | — |
| 22 | TP_HEADER_ID | — | — | — | — | — | — |
| 23 | TRANSLATED_CUSTOMER_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[custaccountsiteuse|CustAccountSiteUse]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | Language | — |
| BILL_TO_FLAG | BillToFlag | — |
| CUST_ACCT_SITE_ID | CustAccountSiteId | — |
| CUSTOMER_CATEGORY_CODE | CustomerCategoryCode | — |
| ECE_TP_LOCATION_CODE | EceTpLocationCode | — |
| END_DATE | AccountSiteEndDate | — |
| KEY_ACCOUNT_FLAG | KeyAccountFlag | — |
| MARKET_FLAG | MarketFlag | — |
| PARTY_SITE_ID | AccountSitePartySiteId | — |
| SET_ID | AccountSiteSetId | — |
| SHIP_TO_FLAG | ShipToFlag | — |
| START_DATE | AccountSiteStartDate | — |
| STATUS | AccountSiteStatus | — |
| TP_HEADER_ID | TpHeaderId | — |
| TRANSLATED_CUSTOMER_NAME | TranslatedCustomerName | — |

### [[custacctsiteuseloc|CustAcctSiteUseLoc]] (HCM · BICC: 13/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | CustomerAccountSiteLanguage | ✅ |
| BILL_TO_FLAG | CustomerAccountSiteBillToFlag | — |
| CREATED_BY | CustomerAccountSiteCreatedBy | ✅ |
| CREATED_BY_MODULE | CustomerAccountSiteCreatedByModule | — |
| CREATION_DATE | CustomerAccountSiteCreationDate | ✅ |
| CUST_ACCOUNT_ID | CustomerAccountSiteCustAccountId | — |
| CUST_ACCT_SITE_ID | CustomerAccountSiteCustAcctSiteId | ✅ |
| CUSTOMER_CATEGORY_CODE | CustomerAccountSiteCustomerCategoryCode | ✅ |
| ECE_TP_LOCATION_CODE | CustomerAccountSiteEceTpLocationCode | — |
| END_DATE | CustomerAccountSiteEndDate | ✅ |
| KEY_ACCOUNT_FLAG | CustomerAccountSiteKeyAccountFlag | — |
| LAST_UPDATE_DATE | CustomerAccountSiteLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CustomerAccountSiteLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CustomerAccountSiteLastUpdatedBy | ✅ |
| MARKET_FLAG | CustomerAccountSiteMarketFlag | — |
| ORIG_SYSTEM_REFERENCE | CustomerAccountSiteOrigSystemReference | ✅ |
| PARTY_SITE_ID | CustomerAccountSitePartySiteId | — |
| SET_ID | CustomerAccountSiteSetIdentifier | — |
| SHIP_TO_FLAG | CustomerAccountSiteShipToFlag | — |
| START_DATE | CustomerAccountSiteStartDate | ✅ |
| STATUS | CustomerAccountSiteStatus | ✅ |
| TP_HEADER_ID | CustomerAccountSiteTpHeaderId | — |
| TRANSLATED_CUSTOMER_NAME | CustomerAccountSiteTranslatedCustomerName | ✅ |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCT_SITE_LANGUAGE | PayingSiteLanguage | — |
| ACCT_SITE_LANGUAGE | RmtToAddrSiteLanguage | — |
| ACCT_SITE_LANGUAGE | ShipToSiteLanguage | — |
| ACCT_SITE_LANGUAGE | SoldToSiteLanguage | — |
| CUST_ACCT_SITE_ID | PayingSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | RmtToAddrSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | ShipToSiteCustAcctSiteId | — |
| CUST_ACCT_SITE_ID | SoldToSiteCustAcctSiteId | — |
| PARTY_SITE_ID | PayingSitePartySiteId | — |
| PARTY_SITE_ID | RmtToAddrSitePartySiteId | — |
| PARTY_SITE_ID | ShipToSitePartySiteId | — |
| PARTY_SITE_ID | SoldToSitePartySiteId | — |
