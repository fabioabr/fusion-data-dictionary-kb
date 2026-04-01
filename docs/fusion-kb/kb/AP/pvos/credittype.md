---
id: DOC-AP-PVO-CreditType
doc_type: system-doc
title: "CreditType — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CreditType
  - credittype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CreditType

## 📌 Visão Geral

Extrai os tipos de crédito configurados para planos de compensação por incentivos (ICM), incluindo nome, unidade de negócio e descrição. Permite categorizar e controlar os diferentes tipos de crédito utilizados no cálculo de comissões e bonificações.

**Caminho:** `FscmTopModelAM.ApplicationSetupAM.CreditType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 3 | 2 | 10 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[cn_credit_types_all_b|CN_CREDIT_TYPES_ALL_B]] — 11 atributos (2 PKs, 6 BICC)
- [[cn_credit_types_all_tl|CN_CREDIT_TYPES_ALL_TL]] — 6 atributos (3 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_credit_types_all_b|CN_CREDIT_TYPES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | CreditTypeId | CREDIT_TYPE_ID | 🔑 | ✅ |
| 4 | ExtendedPrecision | EXTENDED_PRECISION | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | MonetaryFlag | MONETARY_FLAG | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | OrgId | ORG_ID | 🔑 | ✅ |
| 11 | Precision | PRECISION | — | ✅ |

### [[cn_credit_types_all_tl|CN_CREDIT_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditTypeId1 | CREDIT_TYPE_ID | — | — |
| 2 | CreditTypeName | CREDIT_TYPE_NAME | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | — | ✅ |
| 5 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 6 | OrgId1 | ORG_ID | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
