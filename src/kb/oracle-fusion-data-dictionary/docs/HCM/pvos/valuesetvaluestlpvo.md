---
id: DOC-HCM-PVO-ValueSetValuesTLPVO
doc_type: system-doc
title: "ValueSetValuesTLPVO — PVO Human Capital Management"
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
  - ValueSetValuesTLPVO
  - valuesetvaluestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ValueSetValuesTLPVO

## 📌 Visão Geral

Extrai traduções de valores de value sets para referência multilíngue. Suporta internacionalização de listas de valores em interfaces do Oracle Fusion.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.ValueSetValuesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 3 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_values_tl|FND_VS_VALUES_TL]] — 10 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[fnd_vs_values_tl|FND_VS_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | — |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SourceLang | SOURCE_LANG | — | — |
| 9 | TranslatedValue | TRANSLATED_VALUE | — | — |
| 10 | ValueId | VALUE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
