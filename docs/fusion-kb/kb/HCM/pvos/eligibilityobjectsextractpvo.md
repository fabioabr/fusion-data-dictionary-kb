---
id: DOC-HCM-PVO-EligibilityObjectsExtractPVO
doc_type: system-doc
title: "EligibilityObjectsExtractPVO — PVO Human Capital Management"
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
  - EligibilityObjectsExtractPVO
  - eligibilityobjectsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibilityObjectsExtractPVO

## 📌 Visão Geral

Extrai objetos de elegibilidade de benefícios com critérios de qualificação por coluna e valor. Utilizado para definir regras de acesso a planos de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.EligibilityObjectsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_obj_f|BEN_ELIG_OBJ_F]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[ben_elig_obj_f|BEN_ELIG_OBJ_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | ColumnName | COLUMN_NAME | — | ✅ |
| 3 | ColumnValue | COLUMN_VALUE | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | EligObjId | ELIG_OBJ_ID | 🔑 | ✅ |
| 9 | EligObjType | ELIG_OBJ_TYPE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | TableName | TABLE_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
