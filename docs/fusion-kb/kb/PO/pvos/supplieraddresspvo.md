---
id: DOC-PO-PVO-SupplierAddressPVO
doc_type: system-doc
title: "SupplierAddressPVO — PVO Purchasing"
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
  - SupplierAddressPVO
  - supplieraddresspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierAddressPVO

## 📌 Visão Geral

Extrai os endereços dos fornecedores, incluindo logradouro, cidade, estado, país e finalidade (comercial, entrega, faturamento). Permite análise geográfica da base e validação de dados cadastrais.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierAddressPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 154 | 4 | 1 | 102 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_languages_vl|FND_LANGUAGES_VL]] — 18 atributos (3 BICC)
- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 20 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 2 atributos (2 BICC)
- [[poz_supplier_address_v|POZ_SUPPLIER_ADDRESS_V]] — 114 atributos (1 PKs, 94 BICC)

---

## ⚙️ Atributos

### [[fnd_languages_vl|FND_LANGUAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LanguageCreatedBy | CREATED_BY | — | — |
| 2 | LanguageCreationDate | CREATION_DATE | — | — |
| 3 | LanguageDescription | DESCRIPTION | — | ✅ |
| 4 | LanguageInstalledFlag | INSTALLED_FLAG | — | — |
| 5 | LanguageIsoLanguage | ISO_LANGUAGE | — | — |
| 6 | LanguageIsoLanguage3 | ISO_LANGUAGE_3 | — | — |
| 7 | LanguageIsoTerritory | ISO_TERRITORY | — | — |
| 8 | LanguageLangDb2 | LANG_DB2 | — | — |
| 9 | LanguageLangSqlserver | LANG_SQLSERVER | — | — |
| 10 | LanguageLanguageCode | LANGUAGE_CODE | — | ✅ |
| 11 | LanguageLanguageId | LANGUAGE_ID | — | — |
| 12 | LanguageLanguageTag | LANGUAGE_TAG | — | — |
| 13 | LanguageLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LanguageLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LanguageLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | LanguageNlsCodeset | NLS_CODESET | — | — |
| 17 | LanguageNlsLanguage | NLS_LANGUAGE | — | — |
| 18 | LanguageNlsTerritory | NLS_TERRITORY | — | — |

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryAddressStyle | ADDRESS_STYLE | — | — |
| 2 | TerritoryAddressValidation | ADDRESS_VALIDATION | — | — |
| 3 | TerritoryAlternateTerritoryCode | ALTERNATE_TERRITORY_CODE | — | — |
| 4 | TerritoryBankInfoStyle | BANK_INFO_STYLE | — | — |
| 5 | TerritoryBankInfoValidation | BANK_INFO_VALIDATION | — | — |
| 6 | TerritoryCreatedBy | CREATED_BY | — | — |
| 7 | TerritoryCreationDate | CREATION_DATE | — | — |
| 8 | TerritoryCurrencyCode | CURRENCY_CODE | — | — |
| 9 | TerritoryDescription | DESCRIPTION | — | — |
| 10 | TerritoryEnabledFlag | ENABLED_FLAG | — | — |
| 11 | TerritoryEuCode | EU_CODE | — | — |
| 12 | TerritoryIsoNumericCode | ISO_NUMERIC_CODE | — | — |
| 13 | TerritoryIsoTerritoryCode | ISO_TERRITORY_CODE | — | — |
| 14 | TerritoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | TerritoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | TerritoryLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | TerritoryNlsTerritory | NLS_TERRITORY | — | — |
| 18 | TerritoryObsoleteFlag | OBSOLETE_FLAG | — | — |
| 19 | TerritoryTerritoryCode | TERRITORY_CODE | — | ✅ |
| 20 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPartyId | PARTY_ID | — | ✅ |
| 2 | PartyPartyName | PARTY_NAME | — | ✅ |

### [[poz_supplier_address_v|POZ_SUPPLIER_ADDRESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | ✅ |
| 2 | AddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | ✅ |
| 3 | AddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | ✅ |
| 4 | AddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | ✅ |
| 5 | AddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | ✅ |
| 6 | AddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | ✅ |
| 7 | Building | BUILDING | — | ✅ |
| 8 | FloorNumber | FLOOR_NUMBER | — | ✅ |
| 9 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 10 | PostalPlus4Code | POSTAL_PLUS4_CODE | — | ✅ |
| 11 | SupplierAddressAddress1 | ADDRESS1 | — | ✅ |
| 12 | SupplierAddressAddress2 | ADDRESS2 | — | ✅ |
| 13 | SupplierAddressAddress3 | ADDRESS3 | — | ✅ |
| 14 | SupplierAddressAddress4 | ADDRESS4 | — | ✅ |
| 15 | SupplierAddressAddressPurposeOrdering | ADDRESS_PURPOSE_ORDERING | — | ✅ |
| 16 | SupplierAddressAddressPurposeRemitTo | ADDRESS_PURPOSE_REMIT_TO | — | ✅ |
| 17 | SupplierAddressAddressPurposeRfqOrBidding | ADDRESS_PURPOSE_RFQ_OR_BIDDING | — | ✅ |
| 18 | SupplierAddressAddressee | ADDRESSEE | — | ✅ |
| 19 | SupplierAddressAttribute1 | ATTRIBUTE1 | — | ✅ |
| 20 | SupplierAddressAttribute10 | ATTRIBUTE10 | — | ✅ |
| 21 | SupplierAddressAttribute11 | ATTRIBUTE11 | — | ✅ |
| 22 | SupplierAddressAttribute12 | ATTRIBUTE12 | — | ✅ |
| 23 | SupplierAddressAttribute13 | ATTRIBUTE13 | — | ✅ |
| 24 | SupplierAddressAttribute14 | ATTRIBUTE14 | — | ✅ |
| 25 | SupplierAddressAttribute15 | ATTRIBUTE15 | — | ✅ |
| 26 | SupplierAddressAttribute16 | ATTRIBUTE16 | — | ✅ |
| 27 | SupplierAddressAttribute17 | ATTRIBUTE17 | — | ✅ |
| 28 | SupplierAddressAttribute18 | ATTRIBUTE18 | — | ✅ |
| 29 | SupplierAddressAttribute19 | ATTRIBUTE19 | — | ✅ |
| 30 | SupplierAddressAttribute2 | ATTRIBUTE2 | — | ✅ |
| 31 | SupplierAddressAttribute20 | ATTRIBUTE20 | — | ✅ |
| 32 | SupplierAddressAttribute21 | ATTRIBUTE21 | — | ✅ |
| 33 | SupplierAddressAttribute22 | ATTRIBUTE22 | — | ✅ |
| 34 | SupplierAddressAttribute23 | ATTRIBUTE23 | — | ✅ |
| 35 | SupplierAddressAttribute24 | ATTRIBUTE24 | — | ✅ |
| 36 | SupplierAddressAttribute25 | ATTRIBUTE25 | — | ✅ |
| 37 | SupplierAddressAttribute26 | ATTRIBUTE26 | — | ✅ |
| 38 | SupplierAddressAttribute27 | ATTRIBUTE27 | — | ✅ |
| 39 | SupplierAddressAttribute28 | ATTRIBUTE28 | — | ✅ |
| 40 | SupplierAddressAttribute29 | ATTRIBUTE29 | — | ✅ |
| 41 | SupplierAddressAttribute3 | ATTRIBUTE3 | — | ✅ |
| 42 | SupplierAddressAttribute30 | ATTRIBUTE30 | — | ✅ |
| 43 | SupplierAddressAttribute4 | ATTRIBUTE4 | — | ✅ |
| 44 | SupplierAddressAttribute5 | ATTRIBUTE5 | — | ✅ |
| 45 | SupplierAddressAttribute6 | ATTRIBUTE6 | — | ✅ |
| 46 | SupplierAddressAttribute7 | ATTRIBUTE7 | — | ✅ |
| 47 | SupplierAddressAttribute8 | ATTRIBUTE8 | — | ✅ |
| 48 | SupplierAddressAttribute9 | ATTRIBUTE9 | — | ✅ |
| 49 | SupplierAddressAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 50 | SupplierAddressAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 51 | SupplierAddressAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 52 | SupplierAddressAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 53 | SupplierAddressAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 54 | SupplierAddressAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 55 | SupplierAddressAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 56 | SupplierAddressAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 57 | SupplierAddressAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 58 | SupplierAddressAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 59 | SupplierAddressAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 60 | SupplierAddressAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 61 | SupplierAddressAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 62 | SupplierAddressAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 63 | SupplierAddressAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 64 | SupplierAddressAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 65 | SupplierAddressAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 66 | SupplierAddressAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 67 | SupplierAddressAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 68 | SupplierAddressAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 69 | SupplierAddressAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 70 | SupplierAddressAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 71 | SupplierAddressAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 72 | SupplierAddressAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 73 | SupplierAddressAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 74 | SupplierAddressCity | CITY | — | ✅ |
| 75 | SupplierAddressCounty | COUNTY | — | ✅ |
| 76 | SupplierAddressCreatedBy | CREATED_BY | — | ✅ |
| 77 | SupplierAddressCreationDate | CREATION_DATE | — | ✅ |
| 78 | SupplierAddressEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 79 | SupplierAddressEmailContactPointId | EMAIL_CONTACT_POINT_ID | — | — |
| 80 | SupplierAddressEmailContactPointType | EMAIL_CONTACT_POINT_TYPE | — | — |
| 81 | SupplierAddressEmailOverallPrimaryFlag | EMAIL_OVERALL_PRIMARY_FLAG | — | — |
| 82 | SupplierAddressEmailPrimaryFlag | EMAIL_PRIMARY_FLAG | — | — |
| 83 | SupplierAddressFaxContactPointId | FAX_CONTACT_POINT_ID | — | — |
| 84 | SupplierAddressFaxContactPointType | FAX_CONTACT_POINT_TYPE | — | — |
| 85 | SupplierAddressFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 86 | SupplierAddressFaxOverallPrimaryFlag | FAX_OVERALL_PRIMARY_FLAG | — | — |
| 87 | SupplierAddressFaxPhoneAreaCode | FAX_PHONE_AREA_CODE | — | ✅ |
| 88 | SupplierAddressFaxPhoneNumber | FAX_PHONE_NUMBER | — | ✅ |
| 89 | SupplierAddressFaxPrimaryFlag | FAX_PRIMARY_FLAG | — | — |
| 90 | SupplierAddressGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | ✅ |
| 91 | SupplierAddressInactiveDate | INACTIVE_DATE | — | ✅ |
| 92 | SupplierAddressLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 93 | SupplierAddressLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 94 | SupplierAddressLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 95 | SupplierAddressLocationId | LOCATION_ID | — | — |
| 96 | SupplierAddressLocationLanguage | LOCATION_LANGUAGE | — | — |
| 97 | SupplierAddressObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 98 | SupplierAddressPEOCountry | COUNTRY | — | — |
| 99 | SupplierAddressPartyId | PARTY_ID | — | — |
| 100 | SupplierAddressPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 101 | SupplierAddressPayPartySiteUseId | PAY_PARTY_SITE_USE_ID | — | — |
| 102 | SupplierAddressPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 103 | SupplierAddressPhoneContactPointId | PHONE_CONTACT_POINT_ID | — | — |
| 104 | SupplierAddressPhoneContactPointType | PHONE_CONTACT_POINT_TYPE | — | — |
| 105 | SupplierAddressPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 106 | SupplierAddressPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 107 | SupplierAddressPhoneNumber | PHONE_NUMBER | — | ✅ |
| 108 | SupplierAddressPhoneOverallPrimaryFlag | PHONE_OVERALL_PRIMARY_FLAG | — | — |
| 109 | SupplierAddressPhonePrimaryFlag | PHONE_PRIMARY_FLAG | — | — |
| 110 | SupplierAddressPostalCode | POSTAL_CODE | — | ✅ |
| 111 | SupplierAddressProvince | PROVINCE | — | ✅ |
| 112 | SupplierAddressPurPartySiteUseId | PUR_PARTY_SITE_USE_ID | — | — |
| 113 | SupplierAddressState | STATE | — | ✅ |
| 114 | SupplierAddressStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
