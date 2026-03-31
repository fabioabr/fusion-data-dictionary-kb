---
id: DOC-OTHER-PVO-TermsDeviationP
doc_type: system-doc
title: "TermsDeviationP — PVO Cross-Module"
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
  - TermsDeviationP
  - termsdeviationp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TermsDeviationP

## 📌 Visão Geral

View Object para extração BICC de dados de Terms Deviation P. Acessa as tabelas: OKC_ARTICLES_ALL, OKC_K_HEADERS_ALL_B, OKC_TERMS_DEVIATIONS_T (+1).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.TermsDeviationP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 4 | 1 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[okc_articles_all|OKC_ARTICLES_ALL]] — 9 atributos (9 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 4 atributos (4 BICC)
- [[okc_terms_deviations_t|OKC_TERMS_DEVIATIONS_T]] — 15 atributos (1 PKs, 15 BICC)
- [[okc_xprt_rule_hdrs_all|OKC_XPRT_RULE_HDRS_ALL]] — 5 atributos (5 BICC)

---

## ⚙️ Atributos

### [[okc_articles_all|OKC_ARTICLES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractLibraryClauseDocArticleId | ARTICLE_ID | — | ✅ |
| 2 | ContractLibraryClauseDocArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 3 | ContractLibraryClauseDocArticleTitle | ARTICLE_TITLE | — | ✅ |
| 4 | ContractLibraryClauseOrigArticleId | ARTICLE_ID | — | ✅ |
| 5 | ContractLibraryClauseOrigArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 6 | ContractLibraryClauseOrigArticleTitle | ARTICLE_TITLE | — | ✅ |
| 7 | ContractLibraryClauseRefArticleNumber | ARTICLE_NUMBER | — | ✅ |
| 8 | ContractlibraryClauseRefArticleTitle | ARTICLE_TITLE | — | ✅ |
| 9 | ontractLibraryClauseRefArticleId | ARTICLE_ID | — | ✅ |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderBasePEOId | ID | — | ✅ |
| 2 | ContractHeaderBasePEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 3 | ContractHeaderBasePEOStsCode | STS_CODE | — | ✅ |
| 4 | ContractHeaderBasePEOVersionType | VERSION_TYPE | — | ✅ |

### [[okc_terms_deviations_t|OKC_TERMS_DEVIATIONS_T]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArticleDescription | ARTICLE_DESCRIPTION | — | ✅ |
| 2 | ArticleStatus | ARTICLE_STATUS | — | ✅ |
| 3 | DeviationCategory | DEVIATION_CATEGORY | — | ✅ |
| 4 | DeviationCategoryMeaning | DEVIATION_CATEGORY_MEANING | — | ✅ |
| 5 | DeviationCode | DEVIATION_CODE | — | ✅ |
| 6 | DeviationCodeMeaning | DEVIATION_CODE_MEANING | — | ✅ |
| 7 | DeviationId | DEVIATION_ID | 🔑 | ✅ |
| 8 | DeviationType | DEVIATION_TYPE | — | ✅ |
| 9 | DocumentId | DOCUMENT_ID | — | ✅ |
| 10 | DocumentType | DOCUMENT_TYPE | — | ✅ |
| 11 | OrigArticleId | ORIG_ARTICLE_ID | — | ✅ |
| 12 | RefArticleId | REF_ARTICLE_ID | — | ✅ |
| 13 | RuleId | RULE_ID | — | ✅ |
| 14 | SectionHeading | SECTION_HEADING | — | ✅ |
| 15 | TermsDeviationPEOArticleTitle | ARTICLE_TITLE | — | ✅ |

### [[okc_xprt_rule_hdrs_all|OKC_XPRT_RULE_HDRS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionExprCode | CONDITION_EXPR_CODE | — | ✅ |
| 2 | ContractRulePEORuleId | RULE_ID | — | ✅ |
| 3 | RuleDescription | RULE_DESCRIPTION | — | ✅ |
| 4 | RuleName | RULE_NAME | — | ✅ |
| 5 | RuleType | RULE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
