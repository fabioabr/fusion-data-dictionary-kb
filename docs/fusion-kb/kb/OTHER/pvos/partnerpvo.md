---
id: DOC-OTHER-PVO-PartnerPVO
doc_type: system-doc
title: "PartnerPVO — PVO Cross-Module"
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
  - PartnerPVO
  - partnerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartnerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Partner. Acessa as tabelas: IRC_TP_PARTNERS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecJobDistributionAM.PartnerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 8 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[irc_tp_partners|IRC_TP_PARTNERS]] — 10 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[irc_tp_partners|IRC_TP_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerId | PARTNER_ID | 🔑 | ✅ |
| 2 | PartnerPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PartnerPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PartnerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PartnerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PartnerPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PartnerPEOLogo | LOGO | — | — |
| 8 | PartnerPEOName | NAME | — | ✅ |
| 9 | PartnerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PartnerPEOPartnerGuid | PARTNER_GUID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
