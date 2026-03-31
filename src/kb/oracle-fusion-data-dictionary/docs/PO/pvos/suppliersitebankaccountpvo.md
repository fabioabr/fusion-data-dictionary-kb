---
id: DOC-PO-PVO-SupplierSiteBankAccountPVO
doc_type: system-doc
title: "SupplierSiteBankAccountPVO — PVO Purchasing"
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
  - SupplierSiteBankAccountPVO
  - suppliersitebankaccountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSiteBankAccountPVO

## 📌 Visão Geral

Extrai as contas bancárias associadas a sites específicos de fornecedores, com dados completos de banco, agência e validação. Permite pagamentos direcionados ao estabelecimento correto.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierSiteBankAccountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 582 | 10 | 2 | 50 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 246 atributos (3 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 30 atributos (1 BICC)
- [[iby_external_payees_all|IBY_EXTERNAL_PAYEES_ALL]] — 36 atributos (1 PKs, 18 BICC)
- [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]] — 45 atributos (1 PKs, 10 BICC)
- [[iby_ext_party_pmt_mthds|IBY_EXT_PARTY_PMT_MTHDS]] — 14 atributos (3 BICC)
- [[iby_payment_methods_vl|IBY_PAYMENT_METHODS_VL]] — 31 atributos (3 BICC)
- [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]] — 15 atributos (4 BICC)
- [[poz_ext_bank_accounts_v|POZ_EXT_BANK_ACCOUNTS_V]] — 12 atributos (5 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 49 atributos (1 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 104 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAddress1 | ADDRESS1 | — | — |
| 2 | BankAddress2 | ADDRESS2 | — | — |
| 3 | BankAddress3 | ADDRESS3 | — | — |
| 4 | BankAddress4 | ADDRESS4 | — | — |
| 5 | BankAnalysisFy | ANALYSIS_FY | — | — |
| 6 | BankCategoryCode | CATEGORY_CODE | — | — |
| 7 | BankCeoName | CEO_NAME | — | — |
| 8 | BankCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | BankCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | BankCity | CITY | — | — |
| 11 | BankComments | COMMENTS | — | — |
| 12 | BankCountry | COUNTRY | — | — |
| 13 | BankCounty | COUNTY | — | — |
| 14 | BankCreatedBy | CREATED_BY | — | — |
| 15 | BankCreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | BankCreationDate | CREATION_DATE | — | — |
| 17 | BankCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 18 | BankDateOfBirth | DATE_OF_BIRTH | — | — |
| 19 | BankDunsNumberC | DUNS_NUMBER_C | — | — |
| 20 | BankEmailAddress | EMAIL_ADDRESS | — | — |
| 21 | BankEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 22 | BankFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 23 | BankGender | GENDER | — | — |
| 24 | BankGroupType | GROUP_TYPE | — | — |
| 25 | BankGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 26 | BankHomeCountry | HOME_COUNTRY | — | — |
| 27 | BankHqBranchInd | HQ_BRANCH_IND | — | — |
| 28 | BankIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 29 | BankIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 30 | BankInternalFlag | INTERNAL_FLAG | — | — |
| 31 | BankJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 32 | BankLanguageName | LANGUAGE_NAME | — | — |
| 33 | BankLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | BankLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | BankLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | BankMaritalStatus | MARITAL_STATUS | — | — |
| 37 | BankMissionStatement | MISSION_STATEMENT | — | — |
| 38 | BankNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 39 | BankObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | BankOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 41 | BankPartyId | PARTY_ID | — | — |
| 42 | BankPartyName | PARTY_NAME | — | — |
| 43 | BankPartyNumber | PARTY_NUMBER | — | — |
| 44 | BankPartyType | PARTY_TYPE | — | — |
| 45 | BankPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | BankPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | BankPersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | BankPersonLastName | PERSON_LAST_NAME | — | — |
| 49 | BankPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | BankPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | BankPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | BankPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | BankPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | BankPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | BankPersonTitle | PERSON_TITLE | — | — |
| 56 | BankPostalCode | POSTAL_CODE | — | — |
| 57 | BankPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | BankPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | BankPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | BankPreferredName | PREFERRED_NAME | — | — |
| 61 | BankPreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | BankPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | BankPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | BankPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | BankPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | BankPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | BankPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | BankPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 69 | BankPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | BankPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | BankProvince | PROVINCE | — | — |
| 72 | BankSalutation | SALUTATION | — | — |
| 73 | BankSicCode | SIC_CODE | — | — |
| 74 | BankSicCodeType | SIC_CODE_TYPE | — | — |
| 75 | BankState | STATE | — | — |
| 76 | BankStatus | STATUS | — | — |
| 77 | BankThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | BankTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | BankUrl | URL | — | — |
| 80 | BankUserGuid | USER_GUID | — | — |
| 81 | BankValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | BankYearEstablished | YEAR_ESTABLISHED | — | — |
| 83 | BranchAddress1 | ADDRESS1 | — | — |
| 84 | BranchAddress2 | ADDRESS2 | — | — |
| 85 | BranchAddress3 | ADDRESS3 | — | — |
| 86 | BranchAddress4 | ADDRESS4 | — | — |
| 87 | BranchAnalysisFy | ANALYSIS_FY | — | — |
| 88 | BranchCategoryCode | CATEGORY_CODE | — | — |
| 89 | BranchCeoName | CEO_NAME | — | — |
| 90 | BranchCertReasonCode | CERT_REASON_CODE | — | — |
| 91 | BranchCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 92 | BranchCity | CITY | — | — |
| 93 | BranchComments | COMMENTS | — | — |
| 94 | BranchCountry | COUNTRY | — | — |
| 95 | BranchCounty | COUNTY | — | — |
| 96 | BranchCreatedBy | CREATED_BY | — | — |
| 97 | BranchCreatedByModule | CREATED_BY_MODULE | — | — |
| 98 | BranchCreationDate | CREATION_DATE | — | — |
| 99 | BranchCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 100 | BranchDateOfBirth | DATE_OF_BIRTH | — | — |
| 101 | BranchDunsNumberC | DUNS_NUMBER_C | — | — |
| 102 | BranchEmailAddress | EMAIL_ADDRESS | — | — |
| 103 | BranchEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 104 | BranchFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 105 | BranchGender | GENDER | — | — |
| 106 | BranchGroupType | GROUP_TYPE | — | — |
| 107 | BranchGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 108 | BranchHomeCountry | HOME_COUNTRY | — | — |
| 109 | BranchHqBranchInd | HQ_BRANCH_IND | — | — |
| 110 | BranchIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 111 | BranchIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 112 | BranchInternalFlag | INTERNAL_FLAG | — | — |
| 113 | BranchJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 114 | BranchLanguageName | LANGUAGE_NAME | — | — |
| 115 | BranchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 116 | BranchLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 117 | BranchLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 118 | BranchMaritalStatus | MARITAL_STATUS | — | — |
| 119 | BranchMissionStatement | MISSION_STATEMENT | — | — |
| 120 | BranchNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 121 | BranchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | BranchOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 123 | BranchPartyId | PARTY_ID | — | — |
| 124 | BranchPartyName | PARTY_NAME | — | — |
| 125 | BranchPartyNumber | PARTY_NUMBER | — | — |
| 126 | BranchPartyType | PARTY_TYPE | — | — |
| 127 | BranchPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 128 | BranchPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 129 | BranchPersonFirstName | PERSON_FIRST_NAME | — | — |
| 130 | BranchPersonLastName | PERSON_LAST_NAME | — | — |
| 131 | BranchPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 132 | BranchPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 133 | BranchPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 134 | BranchPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 135 | BranchPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 136 | BranchPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 137 | BranchPersonTitle | PERSON_TITLE | — | — |
| 138 | BranchPostalCode | POSTAL_CODE | — | — |
| 139 | BranchPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 140 | BranchPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 141 | BranchPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 142 | BranchPreferredName | PREFERRED_NAME | — | — |
| 143 | BranchPreferredNameId | PREFERRED_NAME_ID | — | — |
| 144 | BranchPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 145 | BranchPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 146 | BranchPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 147 | BranchPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 148 | BranchPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 149 | BranchPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 150 | BranchPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 151 | BranchPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 152 | BranchPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 153 | BranchProvince | PROVINCE | — | — |
| 154 | BranchSalutation | SALUTATION | — | — |
| 155 | BranchSicCode | SIC_CODE | — | — |
| 156 | BranchSicCodeType | SIC_CODE_TYPE | — | — |
| 157 | BranchState | STATE | — | — |
| 158 | BranchStatus | STATUS | — | — |
| 159 | BranchThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 160 | BranchTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 161 | BranchUrl | URL | — | — |
| 162 | BranchUserGuid | USER_GUID | — | — |
| 163 | BranchValidatedFlag | VALIDATED_FLAG | — | — |
| 164 | BranchYearEstablished | YEAR_ESTABLISHED | — | — |
| 165 | SupplierPartyAddress1 | ADDRESS1 | — | — |
| 166 | SupplierPartyAddress2 | ADDRESS2 | — | — |
| 167 | SupplierPartyAddress3 | ADDRESS3 | — | — |
| 168 | SupplierPartyAddress4 | ADDRESS4 | — | — |
| 169 | SupplierPartyAnalysisFy | ANALYSIS_FY | — | — |
| 170 | SupplierPartyCategoryCode | CATEGORY_CODE | — | — |
| 171 | SupplierPartyCeoName | CEO_NAME | — | — |
| 172 | SupplierPartyCertReasonCode | CERT_REASON_CODE | — | — |
| 173 | SupplierPartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 174 | SupplierPartyCity | CITY | — | — |
| 175 | SupplierPartyComments | COMMENTS | — | — |
| 176 | SupplierPartyCountry | COUNTRY | — | — |
| 177 | SupplierPartyCounty | COUNTY | — | — |
| 178 | SupplierPartyCreatedBy | CREATED_BY | — | — |
| 179 | SupplierPartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 180 | SupplierPartyCreationDate | CREATION_DATE | — | — |
| 181 | SupplierPartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 182 | SupplierPartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 183 | SupplierPartyDunsNumberC | DUNS_NUMBER_C | — | — |
| 184 | SupplierPartyEmailAddress | EMAIL_ADDRESS | — | — |
| 185 | SupplierPartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 186 | SupplierPartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 187 | SupplierPartyGender | GENDER | — | — |
| 188 | SupplierPartyGroupType | GROUP_TYPE | — | — |
| 189 | SupplierPartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 190 | SupplierPartyHomeCountry | HOME_COUNTRY | — | — |
| 191 | SupplierPartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 192 | SupplierPartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 193 | SupplierPartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 194 | SupplierPartyInternalFlag | INTERNAL_FLAG | — | — |
| 195 | SupplierPartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 196 | SupplierPartyLanguageName | LANGUAGE_NAME | — | — |
| 197 | SupplierPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 198 | SupplierPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 199 | SupplierPartyLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 200 | SupplierPartyMaritalStatus | MARITAL_STATUS | — | — |
| 201 | SupplierPartyMissionStatement | MISSION_STATEMENT | — | — |
| 202 | SupplierPartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 203 | SupplierPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 204 | SupplierPartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 205 | SupplierPartyPartyId | PARTY_ID | — | — |
| 206 | SupplierPartyPartyName | PARTY_NAME | — | — |
| 207 | SupplierPartyPartyNumber | PARTY_NUMBER | — | — |
| 208 | SupplierPartyPartyType | PARTY_TYPE | — | — |
| 209 | SupplierPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 210 | SupplierPartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 211 | SupplierPartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 212 | SupplierPartyPersonLastName | PERSON_LAST_NAME | — | — |
| 213 | SupplierPartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 214 | SupplierPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 215 | SupplierPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 216 | SupplierPartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 217 | SupplierPartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 218 | SupplierPartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 219 | SupplierPartyPersonTitle | PERSON_TITLE | — | — |
| 220 | SupplierPartyPostalCode | POSTAL_CODE | — | — |
| 221 | SupplierPartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 222 | SupplierPartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 223 | SupplierPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 224 | SupplierPartyPreferredName | PREFERRED_NAME | — | — |
| 225 | SupplierPartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 226 | SupplierPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 227 | SupplierPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 228 | SupplierPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 229 | SupplierPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 230 | SupplierPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 231 | SupplierPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 232 | SupplierPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 233 | SupplierPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 234 | SupplierPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 235 | SupplierPartyProvince | PROVINCE | — | — |
| 236 | SupplierPartySalutation | SALUTATION | — | — |
| 237 | SupplierPartySicCode | SIC_CODE | — | — |
| 238 | SupplierPartySicCodeType | SIC_CODE_TYPE | — | — |
| 239 | SupplierPartyState | STATE | — | — |
| 240 | SupplierPartyStatus | STATUS | — | — |
| 241 | SupplierPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 242 | SupplierPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 243 | SupplierPartyUrl | URL | — | — |
| 244 | SupplierPartyUserGuid | USER_GUID | — | — |
| 245 | SupplierPartyValidatedFlag | VALIDATED_FLAG | — | — |
| 246 | SupplierPartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySiteAddressee | ADDRESSEE | — | — |
| 3 | PartySiteComments | COMMENTS | — | — |
| 4 | PartySiteCreatedBy | CREATED_BY | — | — |
| 5 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | PartySiteCreationDate | CREATION_DATE | — | — |
| 7 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 8 | PartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 10 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 11 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 12 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PartySiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PartySiteLocationId | LOCATION_ID | — | — |
| 16 | PartySiteMailstop | MAILSTOP | — | — |
| 17 | PartySiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 19 | PartySitePartyId | PARTY_ID | — | — |
| 20 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 21 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 22 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 23 | PartySitePartySiteId | PARTY_SITE_ID | — | — |
| 24 | PartySitePartySiteName | PARTY_SITE_NAME | — | — |
| 25 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 26 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 27 | PartySitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 28 | PartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 29 | PartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 30 | PartySiteStatus | STATUS | — | — |

### [[iby_external_payees_all|IBY_EXTERNAL_PAYEES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExtPayeeId | EXT_PAYEE_ID | 🔑 | ✅ |
| 2 | PayeeBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 3 | PayeeBankInstruction1Code | BANK_INSTRUCTION1_CODE | — | ✅ |
| 4 | PayeeBankInstruction2Code | BANK_INSTRUCTION2_CODE | — | ✅ |
| 5 | PayeeBankInstructionDetails | BANK_INSTRUCTION_DETAILS | — | ✅ |
| 6 | PayeeCreatedBy | CREATED_BY | — | — |
| 7 | PayeeCreationDate | CREATION_DATE | — | — |
| 8 | PayeeDefaultPaymentMethodCode | DEFAULT_PAYMENT_METHOD_CODE | — | — |
| 9 | PayeeDeliveryChannelCode | DELIVERY_CHANNEL_CODE | — | ✅ |
| 10 | PayeeEceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 11 | PayeeEndDate | END_DATE | — | — |
| 12 | PayeeExclusivePaymentFlag | EXCLUSIVE_PAYMENT_FLAG | — | ✅ |
| 13 | PayeeInactiveDate | INACTIVE_DATE | — | — |
| 14 | PayeeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | PayeeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | PayeeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | PayeeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PayeeOrgId | ORG_ID | — | — |
| 19 | PayeeOrgType | ORG_TYPE | — | — |
| 20 | PayeePartySiteId | PARTY_SITE_ID | — | — |
| 21 | PayeePayeePartyId | PAYEE_PARTY_ID | — | — |
| 22 | PayeePaymentFormatCode | PAYMENT_FORMAT_CODE | — | — |
| 23 | PayeePaymentFunction | PAYMENT_FUNCTION | — | — |
| 24 | PayeePaymentReasonCode | PAYMENT_REASON_CODE | — | ✅ |
| 25 | PayeePaymentReasonComments | PAYMENT_REASON_COMMENTS | — | ✅ |
| 26 | PayeePaymentTextMessage1 | PAYMENT_TEXT_MESSAGE1 | — | ✅ |
| 27 | PayeePaymentTextMessage2 | PAYMENT_TEXT_MESSAGE2 | — | ✅ |
| 28 | PayeePaymentTextMessage3 | PAYMENT_TEXT_MESSAGE3 | — | ✅ |
| 29 | PayeeRemitAdviceDeliveryMethod | REMIT_ADVICE_DELIVERY_METHOD | — | ✅ |
| 30 | PayeeRemitAdviceEmail | REMIT_ADVICE_EMAIL | — | ✅ |
| 31 | PayeeRemitAdviceFax | REMIT_ADVICE_FAX | — | ✅ |
| 32 | PayeeSettlementPriority | SETTLEMENT_PRIORITY | — | ✅ |
| 33 | PayeeStartDate | START_DATE | — | — |
| 34 | PayeeSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 35 | ServiceLevelCode | SERVICE_LEVEL_CODE | — | ✅ |
| 36 | SupplierPayeeExtPayeeId | EXT_PAYEE_ID | — | — |

### [[iby_ext_bank_accounts|IBY_EXT_BANK_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountAccountClassification | ACCOUNT_CLASSIFICATION | — | — |
| 2 | BankAccountAccountSuffix | ACCOUNT_SUFFIX | — | — |
| 3 | BankAccountAgencyLocationCode | AGENCY_LOCATION_CODE | — | — |
| 4 | BankAccountBaMaskSetting | BA_MASK_SETTING | — | — |
| 5 | BankAccountBaNumElecSecSegmentId | BA_NUM_ELEC_SEC_SEGMENT_ID | — | — |
| 6 | BankAccountBaNumSecSegmentId | BA_NUM_SEC_SEGMENT_ID | — | — |
| 7 | BankAccountBaUnmaskLength | BA_UNMASK_LENGTH | — | — |
| 8 | BankAccountBankAccountName | BANK_ACCOUNT_NAME | — | ✅ |
| 9 | BankAccountBankAccountNameAlt | BANK_ACCOUNT_NAME_ALT | — | — |
| 10 | BankAccountBankAccountType | BANK_ACCOUNT_TYPE | — | ✅ |
| 11 | BankAccountBankId | BANK_ID | — | — |
| 12 | BankAccountBranchId | BRANCH_ID | — | — |
| 13 | BankAccountCheckDigits | CHECK_DIGITS | — | — |
| 14 | BankAccountCountryCode | COUNTRY_CODE | — | — |
| 15 | BankAccountCreatedBy | CREATED_BY | — | ✅ |
| 16 | BankAccountCreationDate | CREATION_DATE | — | ✅ |
| 17 | BankAccountCurrencyCode | CURRENCY_CODE | — | ✅ |
| 18 | BankAccountDescription | DESCRIPTION | — | — |
| 19 | BankAccountEncrypted | ENCRYPTED | — | — |
| 20 | BankAccountEndDate | END_DATE | — | — |
| 21 | BankAccountExchangeRate | EXCHANGE_RATE | — | — |
| 22 | BankAccountExchangeRateAgreementNum | EXCHANGE_RATE_AGREEMENT_NUM | — | — |
| 23 | BankAccountExchangeRateAgreementType | EXCHANGE_RATE_AGREEMENT_TYPE | — | — |
| 24 | BankAccountForeignPaymentUseFlag | FOREIGN_PAYMENT_USE_FLAG | — | — |
| 25 | BankAccountHedgingContractReference | HEDGING_CONTRACT_REFERENCE | — | — |
| 26 | BankAccountIban | IBAN | — | — |
| 27 | BankAccountIbanHash1 | IBAN_HASH1 | — | — |
| 28 | BankAccountIbanHash2 | IBAN_HASH2 | — | — |
| 29 | BankAccountIbanSecSegmentId | IBAN_SEC_SEGMENT_ID | — | — |
| 30 | BankAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | BankAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 32 | BankAccountLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | BankAccountMaskedBankAccountNum | MASKED_BANK_ACCOUNT_NUM | — | ✅ |
| 34 | BankAccountMaskedIban | MASKED_IBAN | — | ✅ |
| 35 | BankAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | BankAccountPaymentFactorFlag | PAYMENT_FACTOR_FLAG | — | — |
| 37 | BankAccountProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 38 | BankAccountProgramId | PROGRAM_ID | — | — |
| 39 | BankAccountProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 40 | BankAccountRequestId | REQUEST_ID | — | — |
| 41 | BankAccountSaltVersion | SALT_VERSION | — | — |
| 42 | BankAccountSecondaryAccountReference | SECONDARY_ACCOUNT_REFERENCE | — | — |
| 43 | BankAccountShortAcctName | SHORT_ACCT_NAME | — | — |
| 44 | BankAccountStartDate | START_DATE | — | — |
| 45 | ExtBankAccountId | EXT_BANK_ACCOUNT_ID | 🔑 | ✅ |

### [[iby_ext_party_pmt_mthds|IBY_EXT_PARTY_PMT_MTHDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPayMethodCreatedBy | CREATED_BY | — | — |
| 2 | PartyPayMethodCreationDate | CREATION_DATE | — | — |
| 3 | PartyPayMethodEndDate | END_DATE | — | ✅ |
| 4 | PartyPayMethodExtPartyPmtMthdId | EXT_PARTY_PMT_MTHD_ID | — | — |
| 5 | PartyPayMethodExtPmtPartyId | EXT_PMT_PARTY_ID | — | — |
| 6 | PartyPayMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PartyPayMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PartyPayMethodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PartyPayMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PartyPayMethodPaymentFlow | PAYMENT_FLOW | — | — |
| 11 | PartyPayMethodPaymentFunction | PAYMENT_FUNCTION | — | — |
| 12 | PartyPayMethodPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 13 | PartyPayMethodPrimaryFlag | PRIMARY_FLAG | — | — |
| 14 | PartyPayMethodStartDate | START_DATE | — | ✅ |

### [[iby_payment_methods_vl|IBY_PAYMENT_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayMethodAnticipatedFloat | ANTICIPATED_FLOAT | — | — |
| 2 | PayMethodBankChargeBearerAplFlag | BANK_CHARGE_BEARER_APL_FLAG | — | — |
| 3 | PayMethodCreatedBy | CREATED_BY | — | — |
| 4 | PayMethodCreationDate | CREATION_DATE | — | — |
| 5 | PayMethodDeliveryChannelAplFlag | DELIVERY_CHANNEL_APL_FLAG | — | — |
| 6 | PayMethodDescription | DESCRIPTION | — | — |
| 7 | PayMethodDocumentCategoryCode | DOCUMENT_CATEGORY_CODE | — | — |
| 8 | PayMethodEndDate | END_DATE | — | — |
| 9 | PayMethodExclusivePmtAplFlag | EXCLUSIVE_PMT_APL_FLAG | — | — |
| 10 | PayMethodExternalBankAcctAplFlag | EXTERNAL_BANK_ACCT_APL_FLAG | — | — |
| 11 | PayMethodFormatValue | FORMAT_VALUE | — | — |
| 12 | PayMethodInactiveDate | INACTIVE_DATE | — | — |
| 13 | PayMethodLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PayMethodLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | PayMethodLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PayMethodMaturityDateOffsetDays | MATURITY_DATE_OFFSET_DAYS | — | — |
| 17 | PayMethodObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PayMethodPaymentFormatAplFlag | PAYMENT_FORMAT_APL_FLAG | — | — |
| 19 | PayMethodPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 20 | PayMethodPaymentMethodName | PAYMENT_METHOD_NAME | — | ✅ |
| 21 | PayMethodPaymentReasonAplFlag | PAYMENT_REASON_APL_FLAG | — | — |
| 22 | PayMethodPaymentReasonComntAplFlag | PAYMENT_REASON_COMNT_APL_FLAG | — | — |
| 23 | PayMethodRemittanceMessage1AplFlag | REMITTANCE_MESSAGE1_APL_FLAG | — | — |
| 24 | PayMethodRemittanceMessage2AplFlag | REMITTANCE_MESSAGE2_APL_FLAG | — | — |
| 25 | PayMethodRemittanceMessage3AplFlag | REMITTANCE_MESSAGE3_APL_FLAG | — | — |
| 26 | PayMethodSeededFlag | SEEDED_FLAG | — | — |
| 27 | PayMethodSettlementPriorityAplFlag | SETTLEMENT_PRIORITY_APL_FLAG | — | — |
| 28 | PayMethodStartDate | START_DATE | — | — |
| 29 | PayMethodSupportBillsPayableFlag | SUPPORT_BILLS_PAYABLE_FLAG | — | — |
| 30 | PayMethodUniqueRemittanceIdAplFlag | UNIQUE_REMITTANCE_ID_APL_FLAG | — | — |
| 31 | PayMethodUriCheckDigitAplFlag | URI_CHECK_DIGIT_APL_FLAG | — | — |

### [[iby_pmt_instr_uses_all|IBY_PMT_INSTR_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UseCreatedBy | CREATED_BY | — | — |
| 2 | UseCreationDate | CREATION_DATE | — | — |
| 3 | UseEndDate | END_DATE | — | ✅ |
| 4 | UseExtPmtPartyId | EXT_PMT_PARTY_ID | — | — |
| 5 | UseInstrumentId | INSTRUMENT_ID | — | — |
| 6 | UseInstrumentPaymentUseId | INSTRUMENT_PAYMENT_USE_ID | — | — |
| 7 | UseInstrumentType | INSTRUMENT_TYPE | — | — |
| 8 | UseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | UseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | UseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | UseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UsePaymentFlow | PAYMENT_FLOW | — | — |
| 13 | UsePaymentFunction | PAYMENT_FUNCTION | — | — |
| 14 | UsePrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 15 | UseStartDate | START_DATE | — | ✅ |

### [[poz_ext_bank_accounts_v|POZ_EXT_BANK_ACCOUNTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountInfoBankAccountName | BANK_ACCOUNT_NAME | — | — |
| 2 | BankAccountInfoBankAccountType | BANK_ACCOUNT_TYPE | — | — |
| 3 | BankAccountInfoBankId | BANK_ID | — | — |
| 4 | BankAccountInfoBankName | BANK_NAME | — | ✅ |
| 5 | BankAccountInfoBankNumber | BANK_NUMBER | — | ✅ |
| 6 | BankAccountInfoBranchId | BRANCH_ID | — | — |
| 7 | BankAccountInfoBranchName | BRANCH_NAME | — | ✅ |
| 8 | BankAccountInfoBranchNumber | BRANCH_NUMBER | — | ✅ |
| 9 | BankAccountInfoEftSwiftCode | EFT_SWIFT_CODE | — | ✅ |
| 10 | BankAccountInfoEndDate | END_DATE | — | — |
| 11 | BankAccountInfoExtBankAccountId | EXT_BANK_ACCOUNT_ID | — | — |
| 12 | BankAccountInfoStartDate | START_DATE | — | — |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierAllowAwtFlag | ALLOW_AWT_FLAG | — | — |
| 2 | SupplierAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 3 | SupplierApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 4 | SupplierAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 5 | SupplierAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 6 | SupplierAwtGroupId | AWT_GROUP_ID | — | — |
| 7 | SupplierBusinessRelationship | BUSINESS_RELATIONSHIP | — | — |
| 8 | SupplierCorporateWebsite | CORPORATE_WEBSITE | — | — |
| 9 | SupplierCreatedBy | CREATED_BY | — | — |
| 10 | SupplierCreationDate | CREATION_DATE | — | — |
| 11 | SupplierCreationSource | CREATION_SOURCE | — | — |
| 12 | SupplierCustomerNum | CUSTOMER_NUM | — | — |
| 13 | SupplierEmployeeId | EMPLOYEE_ID | — | — |
| 14 | SupplierEndDateActive | END_DATE_ACTIVE | — | — |
| 15 | SupplierFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | — |
| 16 | SupplierIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 17 | SupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | SupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | SupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | SupplierMinOrderAmount | MIN_ORDER_AMOUNT | — | — |
| 21 | SupplierNameControl | NAME_CONTROL | — | — |
| 22 | SupplierNiNumber | NI_NUMBER | — | — |
| 23 | SupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | SupplierOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 25 | SupplierOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 26 | SupplierOneTimeFlag | ONE_TIME_FLAG | — | — |
| 27 | SupplierOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | — |
| 28 | SupplierParentPartyId | PARENT_PARTY_ID | — | — |
| 29 | SupplierParentVendorId | PARENT_VENDOR_ID | — | — |
| 30 | SupplierPartyId | PARTY_ID | — | — |
| 31 | SupplierProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 32 | SupplierProgramId | PROGRAM_ID | — | — |
| 33 | SupplierProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 34 | SupplierRequestId | REQUEST_ID | — | — |
| 35 | SupplierReviewType | REVIEW_TYPE | — | — |
| 36 | SupplierSegment1 | SEGMENT1 | — | — |
| 37 | SupplierSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | — |
| 38 | SupplierStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | — |
| 39 | SupplierStartDateActive | START_DATE_ACTIVE | — | — |
| 40 | SupplierStateReportableFlag | STATE_REPORTABLE_FLAG | — | — |
| 41 | SupplierTaxReportingName | TAX_REPORTING_NAME | — | — |
| 42 | SupplierTaxVerificationDate | TAX_VERIFICATION_DATE | — | — |
| 43 | SupplierTaxpayerCountry | TAXPAYER_COUNTRY | — | — |
| 44 | SupplierType1099 | TYPE_1099 | — | — |
| 45 | SupplierVatCode | VAT_CODE | — | — |
| 46 | SupplierVendorId | VENDOR_ID | — | — |
| 47 | SupplierVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | — |
| 48 | SupplierWithholdingStartDate | WITHHOLDING_START_DATE | — | — |
| 49 | SupplierWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | — |
| 2 | SupplierSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | — |
| 3 | SupplierSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | — |
| 4 | SupplierSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 5 | SupplierSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 6 | SupplierSiteAreaCode | AREA_CODE | — | — |
| 7 | SupplierSiteAttentionArFlag | ATTENTION_AR_FLAG | — | — |
| 8 | SupplierSiteAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | — |
| 9 | SupplierSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 10 | SupplierSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | — |
| 11 | SupplierSiteB2bSiteCode | B2B_SITE_CODE | — | — |
| 12 | SupplierSiteBankChargeBearer | BANK_CHARGE_BEARER | — | — |
| 13 | SupplierSiteCarrierId | CARRIER_ID | — | — |
| 14 | SupplierSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 15 | SupplierSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | — |
| 16 | SupplierSiteCreatedBy | CREATED_BY | — | — |
| 17 | SupplierSiteCreationDate | CREATION_DATE | — | — |
| 18 | SupplierSiteCustomerNum | CUSTOMER_NUM | — | — |
| 19 | SupplierSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | — |
| 20 | SupplierSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | — |
| 21 | SupplierSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | — |
| 22 | SupplierSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | — |
| 23 | SupplierSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 24 | SupplierSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 25 | SupplierSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | SupplierSiteEmailAddress | EMAIL_ADDRESS | — | — |
| 27 | SupplierSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | — |
| 28 | SupplierSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | — |
| 29 | SupplierSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | — |
| 30 | SupplierSiteFax | FAX | — | — |
| 31 | SupplierSiteFaxAreaCode | FAX_AREA_CODE | — | — |
| 32 | SupplierSiteFaxCountryCode | FAX_COUNTRY_CODE | — | — |
| 33 | SupplierSiteFobLookupCode | FOB_LOOKUP_CODE | — | — |
| 34 | SupplierSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | — |
| 35 | SupplierSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | — |
| 36 | SupplierSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | — |
| 37 | SupplierSiteHoldBy | HOLD_BY | — | — |
| 38 | SupplierSiteHoldDate | HOLD_DATE | — | — |
| 39 | SupplierSiteHoldFlag | HOLD_FLAG | — | — |
| 40 | SupplierSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | — |
| 41 | SupplierSiteHoldReason | HOLD_REASON | — | — |
| 42 | SupplierSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | — |
| 43 | SupplierSiteInactiveDate | INACTIVE_DATE | — | — |
| 44 | SupplierSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | — |
| 45 | SupplierSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | — |
| 46 | SupplierSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | — |
| 47 | SupplierSiteJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 48 | SupplierSiteJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 49 | SupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | SupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 51 | SupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 52 | SupplierSiteLocationId | LOCATION_ID | — | — |
| 53 | SupplierSiteMatchOption | MATCH_OPTION | — | — |
| 54 | SupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | SupplierSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 56 | SupplierSiteOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 57 | SupplierSitePartySiteId | PARTY_SITE_ID | — | — |
| 58 | SupplierSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | — |
| 59 | SupplierSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | — |
| 60 | SupplierSitePayOnCode | PAY_ON_CODE | — | — |
| 61 | SupplierSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | — |
| 62 | SupplierSitePaySiteFlag | PAY_SITE_FLAG | — | — |
| 63 | SupplierSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | — |
| 64 | SupplierSitePaymentHoldDate | PAYMENT_HOLD_DATE | — | — |
| 65 | SupplierSitePaymentPriority | PAYMENT_PRIORITY | — | — |
| 66 | SupplierSitePcardSiteFlag | PCARD_SITE_FLAG | — | — |
| 67 | SupplierSitePhone | PHONE | — | — |
| 68 | SupplierSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 69 | SupplierSitePhoneExtension | PHONE_EXTENSION | — | — |
| 70 | SupplierSitePrcBuId | PRC_BU_ID | — | — |
| 71 | SupplierSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | — |
| 72 | SupplierSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 73 | SupplierSiteProgramId | PROGRAM_ID | — | — |
| 74 | SupplierSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 75 | SupplierSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | — |
| 76 | SupplierSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | — |
| 77 | SupplierSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | — |
| 78 | SupplierSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | — |
| 79 | SupplierSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | — |
| 80 | SupplierSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 81 | SupplierSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | — |
| 82 | SupplierSiteRequestId | REQUEST_ID | — | — |
| 83 | SupplierSiteRetainageRate | RETAINAGE_RATE | — | — |
| 84 | SupplierSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | — |
| 85 | SupplierSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | — |
| 86 | SupplierSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | — |
| 87 | SupplierSiteShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | — |
| 88 | SupplierSiteShippingControl | SHIPPING_CONTROL | — | — |
| 89 | SupplierSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | — |
| 90 | SupplierSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | — |
| 91 | SupplierSiteTaxCountryCode | TAX_COUNTRY_CODE | — | — |
| 92 | SupplierSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | — |
| 93 | SupplierSiteTelex | TELEX | — | — |
| 94 | SupplierSiteTermsDateBasis | TERMS_DATE_BASIS | — | — |
| 95 | SupplierSiteTermsId | TERMS_ID | — | — |
| 96 | SupplierSiteToleranceId | TOLERANCE_ID | — | — |
| 97 | SupplierSiteTpHeaderId | TP_HEADER_ID | — | — |
| 98 | SupplierSiteVatCode | VAT_CODE | — | — |
| 99 | SupplierSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 100 | SupplierSiteVendorId | VENDOR_ID | — | — |
| 101 | SupplierSiteVendorSiteCode | VENDOR_SITE_CODE | — | — |
| 102 | SupplierSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | — |
| 103 | SupplierSiteVendorSiteId | VENDOR_SITE_ID | — | — |
| 104 | SupplierSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
