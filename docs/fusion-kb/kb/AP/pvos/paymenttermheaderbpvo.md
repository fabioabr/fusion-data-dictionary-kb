---
id: DOC-AP-PVO-PaymentTermHeaderBPVO
doc_type: system-doc
title: "PaymentTermHeaderBPVO — PVO Accounts Payable"
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
  - PaymentTermHeaderBPVO
  - paymenttermheaderbpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermHeaderBPVO

## 📌 Visão Geral

Extrai os cabeçalhos das condições de pagamento no contas a pagar, incluindo nome, data de vigência e tipo. Permite catalogar as condições de pagamento disponíveis para negociação com fornecedores (ex: 30/60/90 dias).

**Caminho:** `FscmTopModelAM.FinApInvSetupPmtTermsAM.PaymentTermHeaderBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 7 | 54% |

---

## 🔗 Tabelas Relacionadas

- [[ap_terms_b|AP_TERMS_B]] — 13 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[ap_terms_b|AP_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DueCutoffDay | DUE_CUTOFF_DAY | — | ✅ |
| 4 | EnabledFlag | ENABLED_FLAG | — | — |
| 5 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | Rank | RANK | — | ✅ |
| 11 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 12 | TermId | TERM_ID | 🔑 | ✅ |
| 13 | Type | TYPE | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
