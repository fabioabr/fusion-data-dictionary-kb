---
id: DOC-OTHER-PVO-SchedExceptionAssociationsExtractPVO
doc_type: system-doc
title: "SchedExceptionAssociationsExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SchedExceptionAssociationsExtractPVO
  - schedexceptionassociationsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedExceptionAssociationsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sched Exception Associations Extract. Acessa as tabelas: ZMM_SR_SCHED_AVL_EXCPS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.SchedExceptionAssociationsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_sched_avl_excps|ZMM_SR_SCHED_AVL_EXCPS]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_sched_avl_excps|ZMM_SR_SCHED_AVL_EXCPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedAvlExcpId | SCHED_AVL_EXCP_ID | 🔑 | ✅ |
| 2 | SchedExceptionAssociationsPE1AvlExceptionId | AVL_EXCEPTION_ID | — | ✅ |
| 3 | SchedExceptionAssociationsPE1CreatedBy | CREATED_BY | — | ✅ |
| 4 | SchedExceptionAssociationsPE1CreationDate | CREATION_DATE | — | ✅ |
| 5 | SchedExceptionAssociationsPE1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SchedExceptionAssociationsPE1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | SchedExceptionAssociationsPE1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SchedExceptionAssociationsPE1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SchedExceptionAssociationsPE1ScheduleId | SCHEDULE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
