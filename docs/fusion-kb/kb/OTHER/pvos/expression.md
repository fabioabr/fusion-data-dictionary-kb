---
id: DOC-OTHER-PVO-Expression
doc_type: system-doc
title: "Expression — PVO Cross-Module"
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
  - Expression
  - expression
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Expression

## 📌 Visão Geral

View Object para extração BICC de dados de Expression. Acessa as tabelas: CN_EXPRESSIONS_ALL_B, CN_EXPRESSIONS_ALL_TL.

**Caminho:** `FscmTopModelAM.FormulaAM.Expression`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 2 | 31 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cn_expressions_all_b|CN_EXPRESSIONS_ALL_B]] — 34 atributos (2 PKs, 19 BICC)
- [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[cn_expressions_all_b|CN_EXPRESSIONS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CreatedBy | CREATED_BY | — | ✅ |
| 18 | CreationDate | CREATION_DATE | — | ✅ |
| 19 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 20 | ExpressionId | EXPRESSION_ID | 🔑 | ✅ |
| 21 | ExpressionType | EXPRESSION_TYPE | — | ✅ |
| 22 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | OrgId | ORG_ID | 🔑 | ✅ |
| 27 | PipedSqlFrom | PIPED_SQL_FROM | — | ✅ |
| 28 | PipedSqlSelect | PIPED_SQL_SELECT | — | ✅ |
| 29 | RenderedExpressionDisp | RENDERED_EXPRESSION_DISP | — | ✅ |
| 30 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 31 | SqlFrom | SQL_FROM | — | ✅ |
| 32 | SqlSelect | SQL_SELECT | — | ✅ |
| 33 | StatusCode | STATUS_CODE | — | ✅ |
| 34 | UsesRatetblRsltFlag | USES_RATETBL_RSLT_FLAG | — | ✅ |

### [[cn_expressions_all_tl|CN_EXPRESSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | ✅ |
| 2 | CreationDate1 | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | ExpressionId1 | EXPRESSION_ID | — | ✅ |
| 5 | ExpressionName | EXPRESSION_NAME | — | ✅ |
| 6 | Language1 | LANGUAGE | — | ✅ |
| 7 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OrgId1 | ORG_ID | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
