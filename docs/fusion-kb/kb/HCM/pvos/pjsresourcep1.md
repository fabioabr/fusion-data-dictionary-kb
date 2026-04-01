---
id: DOC-HCM-PVO-PjsResourceP1
doc_type: system-doc
title: "PjsResourceP1 — PVO Human Capital Management"
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
  - PjsResourceP1
  - pjsresourcep1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjsResourceP1

## 📌 Visão Geral

Extrai elementos de recurso (RBS) com nomes traduzidos e formatos de exibição. Dimensão de referência para identificação e classificação de recursos em projetos.

**Caminho:** `FscmTopModelAM.PjsProjectPerformanceAM.PjsResourceP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 3 | 1 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 6 atributos (1 PKs, 1 BICC)
- [[pjf_rbs_element_names_tl|PJF_RBS_ELEMENT_NAMES_TL]] — 3 atributos (1 BICC)
- [[pjf_res_formats_vl|PJF_RES_FORMATS_VL]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSElementPEOLeafNodeFlag | LEAF_NODE_FLAG | — | — |
| 2 | RBSElementPEOOutlineNumber | OUTLINE_NUMBER | — | — |
| 3 | RBSElementPEORbsLevel | RBS_LEVEL | — | — |
| 4 | RBSElementPEOResourceClassCode | RESOURCE_CLASS_CODE | — | — |
| 5 | RBSElementPEOResourceClassId | RESOURCE_CLASS_ID | — | — |
| 6 | RbsElementId | RBS_ELEMENT_ID | 🔑 | ✅ |

### [[pjf_rbs_element_names_tl|PJF_RBS_ELEMENT_NAMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RBSNamesTLPEOLanguage | LANGUAGE | — | — |
| 2 | RBSNamesTLPEOName | NAME | — | ✅ |
| 3 | RBSNamesTLPEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_res_formats_vl|PJF_RES_FORMATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceFormatPEOName | NAME | — | ✅ |
| 2 | ResourceFormatPEOResFormatId | RES_FORMAT_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
