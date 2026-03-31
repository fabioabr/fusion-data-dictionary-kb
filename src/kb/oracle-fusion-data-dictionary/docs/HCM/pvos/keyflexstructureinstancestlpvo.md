---
id: DOC-HCM-PVO-KeyFlexStructureInstancesTLPVO
doc_type: system-doc
title: "KeyFlexStructureInstancesTLPVO — PVO Human Capital Management"
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
  - KeyFlexStructureInstancesTLPVO
  - keyflexstructureinstancestlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeyFlexStructureInstancesTLPVO

## 📌 Visão Geral

Extrai traduções de instâncias de estruturas de key flexfields. Suporta exibição multilíngue de campos chave em interfaces.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.KeyFlexStructureInstancesTLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 11 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]] — 12 atributos (4 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_str_instances_tl|FND_KF_STR_INSTANCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | KeyFlexfieldCode | KEY_FLEXFIELD_CODE | 🔑 | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | Name | NAME | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |
| 12 | StructureInstanceCode | STRUCTURE_INSTANCE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
