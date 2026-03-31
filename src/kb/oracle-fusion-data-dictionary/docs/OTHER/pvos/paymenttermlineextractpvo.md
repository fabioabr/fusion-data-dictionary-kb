---
id: DOC-OTHER-PVO-PaymentTermLineExtractPVO
doc_type: system-doc
title: "PaymentTermLineExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PaymentTermLineExtractPVO
  - paymenttermlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Term Line Extract. Acessa as tabelas: RA_TERMS_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.PaymentTermLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 2 | 15 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_lines|RA_TERMS_LINES]] — 31 atributos (2 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[ra_terms_lines|RA_TERMS_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermsLineAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RaTermsLineAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RaTermsLineAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RaTermsLineAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RaTermsLineAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RaTermsLineAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RaTermsLineAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RaTermsLineAttribute2 | ATTRIBUTE2 | — | — |
| 9 | RaTermsLineAttribute3 | ATTRIBUTE3 | — | — |
| 10 | RaTermsLineAttribute4 | ATTRIBUTE4 | — | — |
| 11 | RaTermsLineAttribute5 | ATTRIBUTE5 | — | — |
| 12 | RaTermsLineAttribute6 | ATTRIBUTE6 | — | — |
| 13 | RaTermsLineAttribute7 | ATTRIBUTE7 | — | — |
| 14 | RaTermsLineAttribute8 | ATTRIBUTE8 | — | — |
| 15 | RaTermsLineAttribute9 | ATTRIBUTE9 | — | — |
| 16 | RaTermsLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | RaTermsLineCreatedBy | CREATED_BY | — | ✅ |
| 18 | RaTermsLineCreationDate | CREATION_DATE | — | ✅ |
| 19 | RaTermsLineDueDate | DUE_DATE | — | ✅ |
| 20 | RaTermsLineDueDayOfMonth | DUE_DAY_OF_MONTH | — | ✅ |
| 21 | RaTermsLineDueDays | DUE_DAYS | — | ✅ |
| 22 | RaTermsLineDueMonthsForward | DUE_MONTHS_FORWARD | — | ✅ |
| 23 | RaTermsLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | RaTermsLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | RaTermsLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | RaTermsLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | RaTermsLineRelativeAmount | RELATIVE_AMOUNT | — | ✅ |
| 28 | RaTermsLineSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 29 | RaTermsLineSequenceNum | SEQUENCE_NUM | 🔑 | ✅ |
| 30 | RaTermsLineSetId | SET_ID | — | ✅ |
| 31 | RaTermsLineTermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
