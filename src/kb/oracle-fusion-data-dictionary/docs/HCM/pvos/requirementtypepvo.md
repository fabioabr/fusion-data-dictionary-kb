---
id: DOC-HCM-PVO-RequirementTypePVO
doc_type: system-doc
title: "RequirementTypePVO — PVO Human Capital Management"
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
  - RequirementTypePVO
  - requirementtypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementTypePVO

## 📌 Visão Geral

Extrai tipos de requisitos com classificações e códigos. Define categorias de requisitos utilizadas no desenvolvimento e gestão de produtos.

**Caminho:** `FscmTopModelAM.RelationshipsAnalyticsAM.RequirementTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 14 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[aca_cs_class_vl|ACA_CS_CLASS_VL]] — 15 atributos (1 PKs, 14 BICC)

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
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | DeletedFlag | DELETED_FLAG | — | ✅ |
| 10 | Description | DESCRIPTION | — | — |
| 11 | DisableDate | DISABLE_DATE | — | ✅ |
| 12 | ObjectCreationAllowedFlag | OBJECT_CREATION_ALLOWED_FLAG | — | ✅ |
| 13 | ParentClassId | PARENT_CLASS_ID | — | ✅ |
| 14 | ProductOwned | PRODUCT_OWNED | — | ✅ |
| 15 | TrackHistoryFlag | TRACK_HISTORY_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
