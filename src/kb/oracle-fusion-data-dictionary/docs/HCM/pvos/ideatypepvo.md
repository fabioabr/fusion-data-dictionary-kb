---
id: DOC-HCM-PVO-IdeaTypePVO
doc_type: system-doc
title: "IdeaTypePVO — PVO Human Capital Management"
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
  - IdeaTypePVO
  - ideatypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IdeaTypePVO

## 📌 Visão Geral

Disponibiliza tipos de ideias com classificação e código. Utilizado para categorização em programas de inovação e melhoria contínua.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.IdeaTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 13 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[aca_cs_class_vl|ACA_CS_CLASS_VL]] — 14 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[aca_cs_class_vl|ACA_CS_CLASS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BipTemplate | BIP_TEMPLATE | — | ✅ |
| 2 | ClassCode | CLASS_CODE | — | ✅ |
| 3 | ClassFamilyCode | CLASS_FAMILY_CODE | — | ✅ |
| 4 | ClassId | CLASS_ID | 🔑 | ✅ |
| 5 | ClassName | CLASS_NAME | — | ✅ |
| 6 | ClassPolicy | CLASS_POLICY | — | ✅ |
| 7 | ClassSubFamilyCode | CLASS_SUB_FAMILY_CODE | — | ✅ |
| 8 | DeletedFlag | DELETED_FLAG | — | ✅ |
| 9 | Description | DESCRIPTION | — | — |
| 10 | DisableDate | DISABLE_DATE | — | ✅ |
| 11 | ObjectCreationAllowedFlag | OBJECT_CREATION_ALLOWED_FLAG | — | ✅ |
| 12 | ParentClassId | PARENT_CLASS_ID | — | ✅ |
| 13 | ProductOwned | PRODUCT_OWNED | — | ✅ |
| 14 | TrackHistoryFlag | TRACK_HISTORY_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
