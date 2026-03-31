---
id: DOC-AP-PVO-PaymentTermHeaderTranslationPVO
doc_type: system-doc
title: "PaymentTermHeaderTranslationPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PaymentTermHeaderTranslationPVO
  - paymenttermheadertranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermHeaderTranslationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes e descrições das condições de pagamento para diferentes idiomas. Necessário para operações multinacionais onde as condições de pagamento precisam ser apresentadas no idioma local.

**Caminho:** `FscmTopModelAM.FinApInvSetupPmtTermsAM.PaymentTermHeaderTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[ap_terms_tl|AP_TERMS_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[ap_terms_tl|AP_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |
| 11 | TermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
