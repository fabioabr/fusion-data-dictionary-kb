---
id: DOC-HCM-PVO-ReligionPVO
doc_type: system-doc
title: "ReligionPVO — PVO Human Capital Management"
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
  - ReligionPVO
  - religionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReligionPVO

## 📌 Visão Geral

Extrai dados de religião de colaboradores com datas e identificadores. Utilizado para gestão de diversidade e conformidade com requisitos regulatórios de RH.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ReligionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_religions|PER_RELIGIONS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_religions|PER_RELIGIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReligionId | RELIGION_ID | 🔑 | ✅ |
| 2 | ReligionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | ReligionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ReligionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ReligionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ReligionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ReligionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ReligionPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 9 | ReligionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ReligionPEOPersonId | PERSON_ID | — | ✅ |
| 11 | ReligionPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 12 | ReligionPEOReligion | RELIGION | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
