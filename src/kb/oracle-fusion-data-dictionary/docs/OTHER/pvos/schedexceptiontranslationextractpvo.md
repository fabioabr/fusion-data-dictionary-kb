---
id: DOC-OTHER-PVO-SchedExceptionTranslationExtractPVO
doc_type: system-doc
title: "SchedExceptionTranslationExtractPVO — PVO Cross-Module"
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
  - SchedExceptionTranslationExtractPVO
  - schedexceptiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SchedExceptionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sched Exception Translation Extract. Acessa as tabelas: ZMM_SR_AVL_EXCEPTIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.SchedExceptionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zmm_sr_avl_exceptions_tl|ZMM_SR_AVL_EXCEPTIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[zmm_sr_avl_exceptions_tl|ZMM_SR_AVL_EXCEPTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvlExceptionId | AVL_EXCEPTION_ID | 🔑 | ✅ |
| 2 | AvlExcpDesc | AVL_EXCP_DESC | — | ✅ |
| 3 | AvlExcpName | AVL_EXCP_NAME | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
