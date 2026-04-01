---
id: DOC-AR-PVO-PaymentTermTranslationPVO
doc_type: system-doc
title: "PaymentTermTranslationPVO — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PaymentTermTranslationPVO
  - paymenttermtranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermTranslationPVO

## 📌 Visão Geral

Extrai as traduções das condições de pagamento para diferentes idiomas. Garante que faturas e comunicações com clientes apresentem os termos de pagamento no idioma adequado ao destinatário.

**Caminho:** `FscmTopModelAM.FinArTopPublicModelAM.PaymentTermTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 11 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_tl|RA_TERMS_TL]] — 12 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ra_terms_tl|RA_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SetId | SET_ID | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |
| 12 | TermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
