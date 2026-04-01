---
id: DOC-PO-PVO-MoacBusinessUnitP1
doc_type: system-doc
title: "MoacBusinessUnitP1 — PVO Purchasing"
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
  - MoacBusinessUnitP1
  - moacbusinessunitp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MoacBusinessUnitP1

## 📌 Visão Geral

Extrai unidades de negócio no contexto MOAC (Multi-Org Access Control), definindo acessos multi-organizacionais do usuário. Fundamental para segurança de dados e governança em ambientes multi-empresa.

**Caminho:** `FscmTopModelAM.PrcPorPublicViewAM.MoacBusinessUnitP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 3 | 1 | 1 | 2 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 3 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | 🔑 | ✅ |
| 2 | Name | BU_NAME | — | ✅ |
| 3 | ShortCode | SHORT_CODE | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
