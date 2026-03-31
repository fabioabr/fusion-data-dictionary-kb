---
id: DOC-OTHER-PVO-InstitutionContactTypesPVO
doc_type: system-doc
title: "InstitutionContactTypesPVO — PVO Cross-Module"
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
  - InstitutionContactTypesPVO
  - institutioncontacttypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionContactTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Contact Types. Acessa as tabelas: GMS_INSTN_CONTACT_TYPES.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionContactTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[gms_instn_contact_types|GMS_INSTN_CONTACT_TYPES]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[gms_instn_contact_types|GMS_INSTN_CONTACT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionContactTypesPEOContactType | CONTACT_TYPE | — | ✅ |
| 2 | InstitutionContactTypesPEOCreatedBy | CREATED_BY | — | — |
| 3 | InstitutionContactTypesPEOCreationDate | CREATION_DATE | — | — |
| 4 | InstitutionContactTypesPEOInstnContactId | INSTN_CONTACT_ID | — | — |
| 5 | InstitutionContactTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InstitutionContactTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InstitutionContactTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InstitutionContactTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InstnContactTypeId | INSTN_CONTACT_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
