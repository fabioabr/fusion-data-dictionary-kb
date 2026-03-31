---
id: DOC-OTHER-PVO-SystemUsageExtractPVO
doc_type: system-doc
title: "SystemUsageExtractPVO — PVO Cross-Module"
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
  - SystemUsageExtractPVO
  - systemusageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SystemUsageExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de System Usage Extract. Acessa as tabelas: GL_SYSTEM_USAGES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.SystemUsageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 1 | 7 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_system_usages|GL_SYSTEM_USAGES]] — 7 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[gl_system_usages|GL_SYSTEM_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DefaultConversionType | DEFAULT_CONVERSION_TYPE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
