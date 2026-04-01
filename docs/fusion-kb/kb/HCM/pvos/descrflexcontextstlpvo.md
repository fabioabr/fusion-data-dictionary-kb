---
id: DOC-HCM-PVO-DescrFlexContextsTLPVO
doc_type: system-doc
title: "DescrFlexContextsTLPVO — PVO Human Capital Management"
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
  - DescrFlexContextsTLPVO
  - descrflexcontextstlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DescrFlexContextsTLPVO

## 📌 Visão Geral

Fornece traducoes multilingue de contextos de flexfields descritivos. Suporta exibicao localizada de labels de campos customizados.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.DescrFlexContextsTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 11 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_df_contexts_tl|FND_DF_CONTEXTS_TL]] — 12 atributos (4 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_df_contexts_tl|FND_DF_CONTEXTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | ContextCode | CONTEXT_CODE | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | DescriptiveFlexfieldCode | DESCRIPTIVE_FLEXFIELD_CODE | 🔑 | ✅ |
| 7 | Language | LANGUAGE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | Name | NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
