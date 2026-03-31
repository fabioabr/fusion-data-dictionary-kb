---
id: DOC-OTHER-PVO-CFDAViewPVO
doc_type: system-doc
title: "CFDAViewPVO — PVO Cross-Module"
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
  - CFDAViewPVO
  - cfdaviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CFDAViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de CFDAView. Acessa as tabelas: GMS_CFDAS_VL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.CFDAViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 7 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[gms_cfdas_vl|GMS_CFDAS_VL]] — 12 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[gms_cfdas_vl|GMS_CFDAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CFDAPEOAgency | AGENCY | — | ✅ |
| 2 | CFDAPEOAssistanceType | ASSISTANCE_TYPE | — | ✅ |
| 3 | CFDAPEOCreatedBy | CREATED_BY | — | — |
| 4 | CFDAPEOCreationDate | CREATION_DATE | — | — |
| 5 | CFDAPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CFDAPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | CFDAPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | CFDAPEOModifiedDate | MODIFIED_DATE | — | ✅ |
| 9 | CFDAPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CFDAPEOProgramTitle | PROGRAM_TITLE | — | ✅ |
| 11 | CFDAPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 12 | Cfda | CFDA | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
