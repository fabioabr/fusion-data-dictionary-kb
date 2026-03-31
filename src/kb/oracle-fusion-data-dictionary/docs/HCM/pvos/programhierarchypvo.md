---
id: DOC-HCM-PVO-ProgramHierarchyPVO
doc_type: system-doc
title: "ProgramHierarchyPVO — PVO Human Capital Management"
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
  - ProgramHierarchyPVO
  - programhierarchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramHierarchyPVO

## 📌 Visão Geral

Disponibiliza a hierarquia de programas de benefícios com datas de vigência. Utilizado para mapear a estrutura plano-opção-programa no módulo Benefits.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ProgramHierarchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_program_hierarchy_v|BEN_PROGRAM_HIERARCHY_V]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ben_program_hierarchy_v|BEN_PROGRAM_HIERARCHY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OipleffectiveEndDate | OIPLEFFECTIVE_END_DATE | — | ✅ |
| 4 | OipleffectiveStartDate | OIPLEFFECTIVE_START_DATE | — | ✅ |
| 5 | OptId | OPT_ID | — | ✅ |
| 6 | PgmId | PGM_ID | 🔑 | ✅ |
| 7 | PlId | PL_ID | — | ✅ |
| 8 | PlTypId | PL_TYP_ID | — | ✅ |
| 9 | PlipeffectiveEndDate | PLIPEFFECTIVE_END_DATE | — | ✅ |
| 10 | PlipeffectiveStartDate | PLIPEFFECTIVE_START_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
