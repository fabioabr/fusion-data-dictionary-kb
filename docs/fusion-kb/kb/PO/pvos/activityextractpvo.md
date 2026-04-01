---
id: DOC-PO-PVO-ActivityExtractPVO
doc_type: system-doc
title: "ActivityExtractPVO — PVO Purchasing"
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
  - ActivityExtractPVO
  - activityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActivityExtractPVO

## 📌 Visão Geral

Extrai as atividades de procurement rastreadas para fins de sustentabilidade, com tipo, período e unidade de negócio. Suporta métricas ambientais e monitoramento da pegada ecológica da cadeia de suprimentos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.ActivityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 111 | 1 | 1 | 111 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_activities|SUS_ACTIVITIES]] — 111 atributos (1 PKs, 111 BICC)

---

## ⚙️ Atributos

### [[sus_activities|SUS_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityDate | ACTIVITY_DATE | — | ✅ |
| 2 | ActivityId | ACTIVITY_ID | 🔑 | ✅ |
| 3 | ActivityNumber | ACTIVITY_NUMBER | — | ✅ |
| 4 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 5 | Attribute1 | ATTRIBUTE1 | — | ✅ |
| 6 | Attribute10 | ATTRIBUTE10 | — | ✅ |
| 7 | Attribute11 | ATTRIBUTE11 | — | ✅ |
| 8 | Attribute12 | ATTRIBUTE12 | — | ✅ |
| 9 | Attribute13 | ATTRIBUTE13 | — | ✅ |
| 10 | Attribute14 | ATTRIBUTE14 | — | ✅ |
| 11 | Attribute15 | ATTRIBUTE15 | — | ✅ |
| 12 | Attribute16 | ATTRIBUTE16 | — | ✅ |
| 13 | Attribute17 | ATTRIBUTE17 | — | ✅ |
| 14 | Attribute18 | ATTRIBUTE18 | — | ✅ |
| 15 | Attribute19 | ATTRIBUTE19 | — | ✅ |
| 16 | Attribute2 | ATTRIBUTE2 | — | ✅ |
| 17 | Attribute20 | ATTRIBUTE20 | — | ✅ |
| 18 | Attribute3 | ATTRIBUTE3 | — | ✅ |
| 19 | Attribute4 | ATTRIBUTE4 | — | ✅ |
| 20 | Attribute5 | ATTRIBUTE5 | — | ✅ |
| 21 | Attribute6 | ATTRIBUTE6 | — | ✅ |
| 22 | Attribute7 | ATTRIBUTE7 | — | ✅ |
| 23 | Attribute8 | ATTRIBUTE8 | — | ✅ |
| 24 | Attribute9 | ATTRIBUTE9 | — | ✅ |
| 25 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 26 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 27 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 28 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 29 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 30 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 31 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 32 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 33 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 34 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 35 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 36 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 37 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 38 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 39 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 40 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 41 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 42 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 43 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 44 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 45 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 46 | CalculationOverrideCode | CALCULATION_OVERRIDE_CODE | — | ✅ |
| 47 | Comments | COMMENTS | — | ✅ |
| 48 | ConsumptionEndDate | CONSUMPTION_END_DATE | — | ✅ |
| 49 | ConsumptionStartDate | CONSUMPTION_START_DATE | — | ✅ |
| 50 | CountryCode | COUNTRY_CODE | — | ✅ |
| 51 | CreatedBy | CREATED_BY | — | ✅ |
| 52 | CreationDate | CREATION_DATE | — | ✅ |
| 53 | DataQualityCode | DATA_QUALITY_CODE | — | ✅ |
| 54 | Description | DESCRIPTION | — | ✅ |
| 55 | EfmAttribute1 | EFM_ATTRIBUTE1 | — | ✅ |
| 56 | EfmAttribute10 | EFM_ATTRIBUTE10 | — | ✅ |
| 57 | EfmAttribute11 | EFM_ATTRIBUTE11 | — | ✅ |
| 58 | EfmAttribute12 | EFM_ATTRIBUTE12 | — | ✅ |
| 59 | EfmAttribute13 | EFM_ATTRIBUTE13 | — | ✅ |
| 60 | EfmAttribute14 | EFM_ATTRIBUTE14 | — | ✅ |
| 61 | EfmAttribute15 | EFM_ATTRIBUTE15 | — | ✅ |
| 62 | EfmAttribute16 | EFM_ATTRIBUTE16 | — | ✅ |
| 63 | EfmAttribute17 | EFM_ATTRIBUTE17 | — | ✅ |
| 64 | EfmAttribute18 | EFM_ATTRIBUTE18 | — | ✅ |
| 65 | EfmAttribute19 | EFM_ATTRIBUTE19 | — | ✅ |
| 66 | EfmAttribute2 | EFM_ATTRIBUTE2 | — | ✅ |
| 67 | EfmAttribute20 | EFM_ATTRIBUTE20 | — | ✅ |
| 68 | EfmAttribute3 | EFM_ATTRIBUTE3 | — | ✅ |
| 69 | EfmAttribute4 | EFM_ATTRIBUTE4 | — | ✅ |
| 70 | EfmAttribute5 | EFM_ATTRIBUTE5 | — | ✅ |
| 71 | EfmAttribute6 | EFM_ATTRIBUTE6 | — | ✅ |
| 72 | EfmAttribute7 | EFM_ATTRIBUTE7 | — | ✅ |
| 73 | EfmAttribute8 | EFM_ATTRIBUTE8 | — | ✅ |
| 74 | EfmAttribute9 | EFM_ATTRIBUTE9 | — | ✅ |
| 75 | EfmAttributeDate1 | EFM_ATTRIBUTE_DATE1 | — | ✅ |
| 76 | EfmAttributeDate2 | EFM_ATTRIBUTE_DATE2 | — | ✅ |
| 77 | EfmAttributeDate3 | EFM_ATTRIBUTE_DATE3 | — | ✅ |
| 78 | EfmAttributeDate4 | EFM_ATTRIBUTE_DATE4 | — | ✅ |
| 79 | EfmAttributeDate5 | EFM_ATTRIBUTE_DATE5 | — | ✅ |
| 80 | EfmAttributeNumber1 | EFM_ATTRIBUTE_NUMBER1 | — | ✅ |
| 81 | EfmAttributeNumber10 | EFM_ATTRIBUTE_NUMBER10 | — | ✅ |
| 82 | EfmAttributeNumber2 | EFM_ATTRIBUTE_NUMBER2 | — | ✅ |
| 83 | EfmAttributeNumber3 | EFM_ATTRIBUTE_NUMBER3 | — | ✅ |
| 84 | EfmAttributeNumber4 | EFM_ATTRIBUTE_NUMBER4 | — | ✅ |
| 85 | EfmAttributeNumber5 | EFM_ATTRIBUTE_NUMBER5 | — | ✅ |
| 86 | EfmAttributeNumber6 | EFM_ATTRIBUTE_NUMBER6 | — | ✅ |
| 87 | EfmAttributeNumber7 | EFM_ATTRIBUTE_NUMBER7 | — | ✅ |
| 88 | EfmAttributeNumber8 | EFM_ATTRIBUTE_NUMBER8 | — | ✅ |
| 89 | EfmAttributeNumber9 | EFM_ATTRIBUTE_NUMBER9 | — | ✅ |
| 90 | EntryTypeCode | ENTRY_TYPE_CODE | — | ✅ |
| 91 | EsgLedgerId | ESG_LEDGER_ID | — | ✅ |
| 92 | ExternalReferenceNumber | EXTERNAL_REF_NUM | — | ✅ |
| 93 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 94 | InvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | ✅ |
| 95 | InvoiceId | INVOICE_ID | — | ✅ |
| 96 | InvoiceLineNumber | INVOICE_LINE_NUMBER | — | ✅ |
| 97 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 98 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 99 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 100 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 101 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 102 | OriginalActivityId | ORIGINAL_ACTIVITY_ID | — | ✅ |
| 103 | PeriodId | PERIOD_ID | — | ✅ |
| 104 | PostingDate | POSTING_DATE | — | ✅ |
| 105 | ScopeCategoryCode | SCOPE_CATEGORY_CODE | — | ✅ |
| 106 | ScopeCode | SCOPE_CODE | — | ✅ |
| 107 | SourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |
| 108 | StatusCode | STATUS_CODE | — | ✅ |
| 109 | SupplierId | SUPPLIER_ID | — | ✅ |
| 110 | TotalCo2e | TOTAL_CO2E | — | ✅ |
| 111 | TotalCo2eUom | TOTAL_CO2E_UOM | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
