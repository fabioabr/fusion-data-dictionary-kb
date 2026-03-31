---
id: DOC-OTHER-PVO-WarrantyClaimTranslationExtractPVO
doc_type: system-doc
title: "WarrantyClaimTranslationExtractPVO — PVO Cross-Module"
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
  - WarrantyClaimTranslationExtractPVO
  - warrantyclaimtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyClaimTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Claim Translation Extract. Acessa as tabelas: CSE_W_CLAIMS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyClaimTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_claims_tl|CSE_W_CLAIMS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cse_w_claims_tl|CSE_W_CLAIMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClaimDescription | CLAIM_DESCRIPTION | — | ✅ |
| 2 | ClaimId | CLAIM_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
