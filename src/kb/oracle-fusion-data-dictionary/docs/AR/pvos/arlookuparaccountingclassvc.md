---
id: DOC-AR-PVO-ArLookupArAccountingClassVC
doc_type: system-doc
title: "ArLookupArAccountingClassVC — PVO Accounts Receivable"
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
  - ArLookupArAccountingClassVC
  - arlookuparaccountingclassvc
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ArLookupArAccountingClassVC

## 📌 Visão Geral

Extrai os valores de domínio (lookup) para classes contábeis de Contas a Receber. Classifica as distribuições contábeis (receita, imposto, frete, etc.) para correta contabilização das transações.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.ArLookupArAccountingClassVC`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 5 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[ar_lookups|AR_LOOKUPS]] — 13 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[ar_lookups|AR_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EnabledFlag | ENABLED_FLAG | — | — |
| 5 | EndDateActive | END_DATE_ACTIVE | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 10 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 11 | Meaning | MEANING | — | ✅ |
| 12 | StartDateActive | START_DATE_ACTIVE | — | — |
| 13 | Tag | TAG | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
