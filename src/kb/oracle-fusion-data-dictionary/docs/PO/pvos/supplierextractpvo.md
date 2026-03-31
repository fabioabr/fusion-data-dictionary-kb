---
id: DOC-PO-PVO-SupplierExtractPVO
doc_type: system-doc
title: "SupplierExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierExtractPVO
  - supplierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierExtractPVO

## 📌 Visão Geral

Extrai dados de fornecedores para carga BICC, incluindo razão social, nomes alternativos e informações PII. Alimenta o data warehouse para análises de base de fornecedores e relatórios gerenciais.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 143 | 3 | 1 | 42 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]] — 4 atributos (4 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 136 atributos (1 PKs, 35 BICC)
- [[poz_suppliers_pii|POZ_SUPPLIERS_PII]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AliasPartyName | PARTY_NAME | — | ✅ |
| 2 | AliasPartyNameId | PARTY_NAME_ID | — | ✅ |
| 3 | AlternateNamePartyName | PARTY_NAME | — | ✅ |
| 4 | AlternateNamePartyNameId | PARTY_NAME_ID | — | ✅ |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute12 | ATTRIBUTE12 | — | — |
| 6 | Attribute13 | ATTRIBUTE13 | — | ✅ |
| 7 | Attribute14 | ATTRIBUTE14 | — | — |
| 8 | Attribute15 | ATTRIBUTE15 | — | — |
| 9 | Attribute16 | ATTRIBUTE16 | — | — |
| 10 | Attribute17 | ATTRIBUTE17 | — | — |
| 11 | Attribute18 | ATTRIBUTE18 | — | — |
| 12 | Attribute19 | ATTRIBUTE19 | — | — |
| 13 | Attribute2 | ATTRIBUTE2 | — | — |
| 14 | Attribute20 | ATTRIBUTE20 | — | — |
| 15 | Attribute3 | ATTRIBUTE3 | — | — |
| 16 | Attribute4 | ATTRIBUTE4 | — | — |
| 17 | Attribute5 | ATTRIBUTE5 | — | — |
| 18 | Attribute6 | ATTRIBUTE6 | — | — |
| 19 | Attribute7 | ATTRIBUTE7 | — | — |
| 20 | Attribute8 | ATTRIBUTE8 | — | — |
| 21 | Attribute9 | ATTRIBUTE9 | — | — |
| 22 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | AwtGroupId | AWT_GROUP_ID | — | ✅ |
| 54 | BcNotApplicableFlag | BC_NOT_APPLICABLE_FLAG | — | ✅ |
| 55 | BusinessRelationship | BUSINESS_RELATIONSHIP | — | ✅ |
| 56 | CorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 57 | CreatedBy | CREATED_BY | — | ✅ |
| 58 | CreationDate | CREATION_DATE | — | ✅ |
| 59 | CreationSource | CREATION_SOURCE | — | ✅ |
| 60 | CustomerNum | CUSTOMER_NUM | — | ✅ |
| 61 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 62 | FederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | ✅ |
| 63 | GlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 64 | GlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 65 | GlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 66 | GlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 67 | GlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 68 | GlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 69 | GlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 70 | GlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 71 | GlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 72 | GlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 73 | GlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 74 | GlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 75 | GlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 76 | GlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 77 | GlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 78 | GlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 79 | GlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 80 | GlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 81 | GlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 82 | GlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 83 | GlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 84 | GlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 85 | GlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | — |
| 86 | GlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 87 | GlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 88 | GlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 89 | GlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 90 | GlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | — |
| 91 | GlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | — |
| 92 | GlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | — |
| 93 | GlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | — |
| 94 | GlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 95 | GlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 96 | GlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 97 | GlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 98 | GlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 99 | GlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 100 | GlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 101 | GlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 102 | GlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 103 | GlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 104 | GlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | — |
| 105 | GlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | — |
| 106 | GlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | — |
| 107 | GlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | — |
| 108 | GlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | — |
| 109 | GlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | — |
| 110 | GlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | — |
| 111 | GlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | — |
| 112 | GlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | — |
| 113 | GlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | — |
| 114 | IncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | ✅ |
| 115 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 116 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 117 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 118 | NameControl | NAME_CONTROL | — | ✅ |
| 119 | NiNumberFlag | NI_NUMBER_FLAG | — | ✅ |
| 120 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 121 | OneTimeFlag | ONE_TIME_FLAG | — | ✅ |
| 122 | OrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | ✅ |
| 123 | ParentPartyId | PARENT_PARTY_ID | — | ✅ |
| 124 | ParentVendorId | PARENT_VENDOR_ID | — | ✅ |
| 125 | PartyId | PARTY_ID | — | ✅ |
| 126 | Segment1 | SEGMENT1 | — | ✅ |
| 127 | SpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | ✅ |
| 128 | StandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | ✅ |
| 129 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 130 | StateReportableFlag | STATE_REPORTABLE_FLAG | — | ✅ |
| 131 | TaxReportingName | TAX_REPORTING_NAME | — | ✅ |
| 132 | TaxVerificationDate | TAX_VERIFICATION_DATE | — | ✅ |
| 133 | TaxpayerCountry | TAXPAYER_COUNTRY | — | ✅ |
| 134 | Type1099 | TYPE_1099 | — | ✅ |
| 135 | VendorId | VENDOR_ID | 🔑 | ✅ |
| 136 | VendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |

### [[poz_suppliers_pii|POZ_SUPPLIERS_PII]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncomeTaxId | INCOME_TAX_ID | — | ✅ |
| 2 | NiNumber | NI_NUMBER | — | ✅ |
| 3 | VendorId1 | VENDOR_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
