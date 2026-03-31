---
id: DOC-HCM-PVO-KeyFlexStructureInstancesPVO
doc_type: system-doc
title: "KeyFlexStructureInstancesPVO — PVO Human Capital Management"
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
  - KeyFlexStructureInstancesPVO
  - keyflexstructureinstancespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeyFlexStructureInstancesPVO

## 📌 Visão Geral

Extrai instâncias de estruturas de key flexfields com código e número. Utilizado para configuração de campos chave em processos do Fusion.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.KeyFlexStructureInstancesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 3 | 5 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_str_instances_b|FND_KF_STR_INSTANCES_B]] — 15 atributos (3 PKs, 5 BICC)
- [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]] — 7 atributos

---

## ⚙️ Atributos

### [[fnd_kf_str_instances_b|FND_KF_STR_INSTANCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DynamicComboCreationFlag | DYNAMIC_COMBO_CREATION_FLAG | — | — |
| 5 | EnabledFlag | ENABLED_FLAG | — | — |
| 6 | KeyFlexfieldCode | KEY_FLEXFIELD_CODE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ShorthandAliasEnabledFlag | SHA_ENABLED_FLAG | — | — |
| 11 | StructureId | STRUCTURE_ID | — | — |
| 12 | StructureInstanceCode | STRUCTURE_INSTANCE_CODE | 🔑 | ✅ |
| 13 | StructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 14 | StructureInstanceIdentifier | STRUCTURE_INSTANCE_IDENTIFIER | — | — |
| 15 | StructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |

### [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId1 | APPLICATION_ID | — | — |
| 2 | Description | DESCRIPTION | — | — |
| 3 | KeyFlexfieldCode1 | KEY_FLEXFIELD_CODE | — | — |
| 4 | Language | LANGUAGE | — | — |
| 5 | Name | NAME | — | — |
| 6 | SourceLang | SOURCE_LANG | — | — |
| 7 | StructureInstanceCode1 | STRUCTURE_INSTANCE_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
