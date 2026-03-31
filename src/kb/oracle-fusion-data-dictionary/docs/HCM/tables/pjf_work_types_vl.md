---
id: DOC-HCM-837
doc_type: system-doc
title: "PJF_WORK_TYPES_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - PJF_WORK_TYPES_VL
  - pjf_work_types_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PJF_WORK_TYPES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 2 | NAME | — | — | — | — | — | — |
| 3 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 4 | WORK_TYPE_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[project|Project]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTypeWorkTypePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | ProjectTypeWorkTypePEOWorkTypeId | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[projectcommitmentpvo|ProjectCommitmentPVO]] (OTHER · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | ✅ |

### [[projectexec|ProjectExec]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTypeWorkTypePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | ProjectTypeWorkTypePEOWorkTypeId | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTypeWorkTypePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | ProjectTypeWorkTypePEOWorkTypeId | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[projectview|ProjectView]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | ProjectTypeWorkTypePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | ProjectTypeWorkTypePEOWorkTypeId | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[taskmspvo|TaskMSPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[taskmsvlpvo|TaskMSVLPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | — |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[taskrefpvo|TaskRefPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |

### [[taskvlpvo|TaskVLPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | WorkTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | WorkTypePEOObjectVersionNumber | — |
| WORK_TYPE_ID | WorkTypePEOWorkTypeId | — |
