---
id: DOC-AR-PVO-PaymentCodes
doc_type: system-doc
title: "PaymentCodes — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PaymentCodes
  - paymentcodes
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentCodes

## 📌 Visão Geral

Extrai os códigos de pagamento cadastrados no sistema, com tipo e descrição. Serve como tabela de referência para classificar os tipos de instrumento de pagamento utilizados nas transações de recebíveis.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.PaymentCodes`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 4 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]] — 15 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[iby_payment_codes_vl|IBY_PAYMENT_CODES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PaymentCode | PAYMENT_CODE | 🔑 | ✅ |
| 2 | PaymentCodeType | PAYMENT_CODE_TYPE | 🔑 | ✅ |
| 3 | PaymentCodesCreatedBy | CREATED_BY | — | — |
| 4 | PaymentCodesCreationDate | CREATION_DATE | — | — |
| 5 | PaymentCodesDescription | DESCRIPTION | — | — |
| 6 | PaymentCodesEndDate | END_DATE | — | — |
| 7 | PaymentCodesFormatValue | FORMAT_VALUE | — | — |
| 8 | PaymentCodesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PaymentCodesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PaymentCodesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PaymentCodesMeaning | MEANING | — | ✅ |
| 12 | PaymentCodesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | PaymentCodesSeededFlag | SEEDED_FLAG | — | — |
| 14 | PaymentCodesStartDate | START_DATE | — | — |
| 15 | PaymentCodesTerritoryCode | TERRITORY_CODE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
