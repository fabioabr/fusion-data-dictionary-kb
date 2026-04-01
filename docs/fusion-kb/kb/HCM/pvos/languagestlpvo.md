---
id: DOC-HCM-PVO-LanguagesTLPVO
doc_type: system-doc
title: "LanguagesTLPVO — PVO Human Capital Management"
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
  - LanguagesTLPVO
  - languagestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LanguagesTLPVO

## 📌 Visão Geral

Disponibiliza o cadastro de idiomas do sistema com traduções. Tabela de referência utilizada para seleção de idioma em interfaces e relatórios.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.LanguagesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_languages_tl|FND_LANGUAGES_TL]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_languages_tl|FND_LANGUAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LanguageCode | LANGUAGE_CODE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
