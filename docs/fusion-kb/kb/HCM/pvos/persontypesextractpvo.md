---
id: DOC-HCM-PVO-PersonTypesExtractPVO
doc_type: system-doc
title: "PersonTypesExtractPVO — PVO Human Capital Management"
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
  - PersonTypesExtractPVO
  - persontypesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonTypesExtractPVO

## 📌 Visão Geral

Extrai os tipos de pessoa (empregado, contingente, candidato, etc.) com status ativo e business group. Dimensão de referência para segmentação da força de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonTypesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_types|PER_PERSON_TYPES]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_person_types|PER_PERSON_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DefaultFlag | DEFAULT_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PersonTypeId | PERSON_TYPE_ID | 🔑 | ✅ |
| 11 | SeededPersonTypeKey | SEEDED_PERSON_TYPE_KEY | — | ✅ |
| 12 | SystemPersonType | SYSTEM_PERSON_TYPE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
