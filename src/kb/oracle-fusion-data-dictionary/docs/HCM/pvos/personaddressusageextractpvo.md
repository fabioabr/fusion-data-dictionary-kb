---
id: DOC-HCM-PVO-PersonAddressUsageExtractPVO
doc_type: system-doc
title: "PersonAddressUsageExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonAddressUsageExtractPVO
  - personaddressusageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAddressUsageExtractPVO

## 📌 Visão Geral

Extrai os usos de endereço das pessoas (residencial, correspondência, etc.) com vigência e business group. Suporta extração BICC para analytics de localização geográfica da força de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PersonBiccExtractAM.PersonAddressUsageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 3 | 13 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_addr_usages_f|PER_PERSON_ADDR_USAGES_F]] — 79 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[per_person_addr_usages_f|PER_PERSON_ADDR_USAGES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressId | ADDRESS_ID | — | ✅ |
| 2 | AddressType | ADDRESS_TYPE | — | ✅ |
| 3 | Attribute1 | ATTRIBUTE1 | — | — |
| 4 | Attribute10 | ATTRIBUTE10 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute16 | ATTRIBUTE16 | — | — |
| 11 | Attribute17 | ATTRIBUTE17 | — | — |
| 12 | Attribute18 | ATTRIBUTE18 | — | — |
| 13 | Attribute19 | ATTRIBUTE19 | — | — |
| 14 | Attribute2 | ATTRIBUTE2 | — | — |
| 15 | Attribute20 | ATTRIBUTE20 | — | — |
| 16 | Attribute21 | ATTRIBUTE21 | — | — |
| 17 | Attribute22 | ATTRIBUTE22 | — | — |
| 18 | Attribute23 | ATTRIBUTE23 | — | — |
| 19 | Attribute24 | ATTRIBUTE24 | — | — |
| 20 | Attribute25 | ATTRIBUTE25 | — | — |
| 21 | Attribute26 | ATTRIBUTE26 | — | — |
| 22 | Attribute27 | ATTRIBUTE27 | — | — |
| 23 | Attribute28 | ATTRIBUTE28 | — | — |
| 24 | Attribute29 | ATTRIBUTE29 | — | — |
| 25 | Attribute3 | ATTRIBUTE3 | — | — |
| 26 | Attribute30 | ATTRIBUTE30 | — | — |
| 27 | Attribute4 | ATTRIBUTE4 | — | — |
| 28 | Attribute5 | ATTRIBUTE5 | — | — |
| 29 | Attribute6 | ATTRIBUTE6 | — | — |
| 30 | Attribute7 | ATTRIBUTE7 | — | — |
| 31 | Attribute8 | ATTRIBUTE8 | — | — |
| 32 | Attribute9 | ATTRIBUTE9 | — | — |
| 33 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 36 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 37 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 38 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 39 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 40 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 41 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 54 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 55 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 56 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 57 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 58 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 59 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 60 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 61 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 62 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 63 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 64 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 65 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 66 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 67 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 68 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 69 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 70 | CreatedBy | CREATED_BY | — | ✅ |
| 71 | CreationDate | CREATION_DATE | — | ✅ |
| 72 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 73 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 74 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 76 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 77 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 78 | PersonAddrUsageId | PERSON_ADDR_USAGE_ID | 🔑 | ✅ |
| 79 | PersonId | PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
