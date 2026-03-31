---
id: DOC-OTHER-PVO-SupportingReferenceVlPVO
doc_type: system-doc
title: "SupportingReferenceVlPVO — PVO Cross-Module"
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
  - SupportingReferenceVlPVO
  - supportingreferencevlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupportingReferenceVlPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supporting Reference Vl. Acessa as tabelas: XLA_ANALYTICAL_HDRS_VL.

**Caminho:** `FscmTopModelAM.FinXlaAmsSuppRefAM.SupportingReferenceVlPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 3 | 6 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[xla_analytical_hdrs_vl|XLA_ANALYTICAL_HDRS_VL]] — 21 atributos (3 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[xla_analytical_hdrs_vl|XLA_ANALYTICAL_HDRS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | ApplicationId | APPLICATION_ID | — | — |
| 3 | BalancingFlag | BALANCING_FLAG | — | — |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Description | DESCRIPTION | — | — |
| 7 | DisplayOrder | DISPLAY_ORDER | — | — |
| 8 | EnabledFlag | ENABLED_FLAG | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | Name | NAME | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RowId1 | ROW_ID | — | — |
| 15 | SuppRefOrder | SUPP_REF_ORDER | — | — |
| 16 | SupportingReferenceCode | ANALYTICAL_CRITERION_CODE | 🔑 | ✅ |
| 17 | SupportingReferenceTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | 🔑 | ✅ |
| 18 | UpdatedFlag | UPDATED_FLAG | — | — |
| 19 | UpdatedInEssbase | UPDATED_IN_ESSBASE | — | — |
| 20 | VersionNum | VERSION_NUM | — | — |
| 21 | YearEndCarryForwardCode | YEAR_END_CARRY_FORWARD_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
