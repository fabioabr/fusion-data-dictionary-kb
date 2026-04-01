---
id: DOC-HCM-PVO-LookupValuesTLPVO
doc_type: system-doc
title: "LookupValuesTLPVO — PVO Human Capital Management"
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
  - LookupValuesTLPVO
  - lookupvaluestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LookupValuesTLPVO

## 📌 Visão Geral

Disponibiliza as traduções multilíngues dos valores de lookup do Oracle Fusion. Permite exibição de rótulos de domínio no idioma correto para relatórios internacionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AnalyticsServiceAM.LookupValuesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 5 | 12 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]] — 13 atributos (5 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fnd_lookup_values_tl|FND_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 9 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 10 | Meaning | MEANING | — | ✅ |
| 11 | SetId | SET_ID | 🔑 | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |
| 13 | ViewApplicationId | VIEW_APPLICATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
