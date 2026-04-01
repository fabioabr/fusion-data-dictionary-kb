---
id: DOC-HCM-909
doc_type: system-doc
title: "ZX_STATUS_B — (título a preencher)"
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
  - ZX_STATUS_B
  - zx_status_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_STATUS_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOW_EXCEPTIONS_FLAG | — | — | — | — | — | — |
| 2 | ALLOW_EXEMPTIONS_FLAG | — | — | — | — | — | — |
| 3 | ALLOW_RATE_OVERRIDE_FLAG | — | — | — | — | — | — |
| 4 | ATTRIBUTE1 | — | — | — | — | — | — |
| 5 | ATTRIBUTE10 | — | — | — | — | — | — |
| 6 | ATTRIBUTE11 | — | — | — | — | — | — |
| 7 | ATTRIBUTE12 | — | — | — | — | — | — |
| 8 | ATTRIBUTE13 | — | — | — | — | — | — |
| 9 | ATTRIBUTE14 | — | — | — | — | — | — |
| 10 | ATTRIBUTE15 | — | — | — | — | — | — |
| 11 | ATTRIBUTE2 | — | — | — | — | — | — |
| 12 | ATTRIBUTE3 | — | — | — | — | — | — |
| 13 | ATTRIBUTE4 | — | — | — | — | — | — |
| 14 | ATTRIBUTE5 | — | — | — | — | — | — |
| 15 | ATTRIBUTE6 | — | — | — | — | — | — |
| 16 | ATTRIBUTE7 | — | — | — | — | — | — |
| 17 | ATTRIBUTE8 | — | — | — | — | — | — |
| 18 | ATTRIBUTE9 | — | — | — | — | — | — |
| 19 | ATTRIBUTE_CATEGORY | — | — | — | — | — | — |
| 20 | CONTENT_OWNER_ID | — | — | — | — | — | — |
| 21 | CREATED_BY | — | — | — | — | — | — |
| 22 | CREATION_DATE | — | — | — | — | — | — |
| 23 | DEFAULT_FLG_EFFECTIVE_FROM | — | — | — | — | — | — |
| 24 | DEFAULT_FLG_EFFECTIVE_TO | — | — | — | — | — | — |
| 25 | DEFAULT_STATUS_FLAG | — | — | — | — | — | — |
| 26 | DEF_REC_SETTLEMENT_OPTION_CODE | — | — | — | — | — | — |
| 27 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 28 | EFFECTIVE_TO | — | — | — | — | — | — |
| 29 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 30 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 31 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 32 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 33 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 34 | RULE_BASED_RATE_FLAG | — | — | — | — | — | — |
| 35 | TAX | — | — | — | — | — | — |
| 36 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 37 | TAX_STATUS_CODE | — | — | — | — | — | — |
| 38 | TAX_STATUS_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TAX_STATUS_ID | TaxStatusTaxStatusId | — |

### [[taxstatusextractpvo|TaxStatusExtractPVO]] (OTHER · BICC: 22/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_EXCEPTIONS_FLAG | TaxStatusBaseAllowExceptionsFlag | ✅ |
| ALLOW_EXEMPTIONS_FLAG | TaxStatusBaseAllowExemptionsFlag | ✅ |
| ALLOW_RATE_OVERRIDE_FLAG | TaxStatusBaseAllowRateOverrideFlag | ✅ |
| ATTRIBUTE1 | TaxStatusBaseAttribute1 | — |
| ATTRIBUTE10 | TaxStatusBaseAttribute10 | — |
| ATTRIBUTE11 | TaxStatusBaseAttribute11 | — |
| ATTRIBUTE12 | TaxStatusBaseAttribute12 | — |
| ATTRIBUTE13 | TaxStatusBaseAttribute13 | — |
| ATTRIBUTE14 | TaxStatusBaseAttribute14 | — |
| ATTRIBUTE15 | TaxStatusBaseAttribute15 | — |
| ATTRIBUTE2 | TaxStatusBaseAttribute2 | — |
| ATTRIBUTE3 | TaxStatusBaseAttribute3 | — |
| ATTRIBUTE4 | TaxStatusBaseAttribute4 | — |
| ATTRIBUTE5 | TaxStatusBaseAttribute5 | — |
| ATTRIBUTE6 | TaxStatusBaseAttribute6 | — |
| ATTRIBUTE7 | TaxStatusBaseAttribute7 | — |
| ATTRIBUTE8 | TaxStatusBaseAttribute8 | — |
| ATTRIBUTE9 | TaxStatusBaseAttribute9 | — |
| ATTRIBUTE_CATEGORY | TaxStatusBaseAttributeCategory | — |
| CONTENT_OWNER_ID | TaxStatusBaseContentOwnerId | ✅ |
| CREATED_BY | TaxStatusBaseCreatedBy | ✅ |
| CREATION_DATE | TaxStatusBaseCreationDate | ✅ |
| DEF_REC_SETTLEMENT_OPTION_CODE | TaxStatusBaseDefRecSettlementOptionCode | ✅ |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxStatusBaseDefaultFlgEffectiveFrom | ✅ |
| DEFAULT_FLG_EFFECTIVE_TO | TaxStatusBaseDefaultFlgEffectiveTo | ✅ |
| DEFAULT_STATUS_FLAG | TaxStatusBaseDefaultStatusFlag | ✅ |
| EFFECTIVE_FROM | TaxStatusBaseEffectiveFrom | ✅ |
| EFFECTIVE_TO | TaxStatusBaseEffectiveTo | ✅ |
| LAST_UPDATE_DATE | TaxStatusBaseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxStatusBaseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaxStatusBaseLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | TaxStatusBaseObjectVersionNumber | ✅ |
| RECORD_TYPE_CODE | TaxStatusBaseRecordTypeCode | ✅ |
| RULE_BASED_RATE_FLAG | TaxStatusBaseRuleBasedRateFlag | ✅ |
| TAX | TaxStatusBaseTax | ✅ |
| TAX_REGIME_CODE | TaxStatusBaseTaxRegimeCode | ✅ |
| TAX_STATUS_CODE | TaxStatusBaseTaxStatusCode | ✅ |
| TAX_STATUS_ID | TaxStatusBaseTaxStatusId | ✅ |
