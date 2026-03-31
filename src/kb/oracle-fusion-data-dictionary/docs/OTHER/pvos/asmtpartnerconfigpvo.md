---
id: DOC-OTHER-PVO-AsmtPartnerConfigPVO
doc_type: system-doc
title: "AsmtPartnerConfigPVO — PVO Cross-Module"
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
  - AsmtPartnerConfigPVO
  - asmtpartnerconfigpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AsmtPartnerConfigPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asmt Partner Config. Acessa as tabelas: IRC_ASMT_PARTNER_CONFIG.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecAssessmentsAM.AsmtPartnerConfigPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 8 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[irc_asmt_partner_config|IRC_ASMT_PARTNER_CONFIG]] — 14 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[irc_asmt_partner_config|IRC_ASMT_PARTNER_CONFIG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtPartnerConfigPEOClientId | CLIENT_ID | — | ✅ |
| 2 | AsmtPartnerConfigPEOClientSecret | CLIENT_SECRET | — | ✅ |
| 3 | AsmtPartnerConfigPEOCreatedBy | CREATED_BY | — | — |
| 4 | AsmtPartnerConfigPEOCreationDate | CREATION_DATE | — | — |
| 5 | AsmtPartnerConfigPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AsmtPartnerConfigPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AsmtPartnerConfigPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AsmtPartnerConfigPEOMultiPhaseFlag | MULTI_PHASE_FLAG | — | ✅ |
| 9 | AsmtPartnerConfigPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AsmtPartnerConfigPEOPhaseCount | PHASE_COUNT | — | ✅ |
| 11 | AsmtPartnerConfigPEOProvisioningId | PROVISIONING_ID | — | — |
| 12 | AsmtPartnerConfigPEOShareFlag | SHARE_FLAG | — | ✅ |
| 13 | AsmtPartnerConfigPEOValidityPeriod | VALIDITY_PERIOD | — | ✅ |
| 14 | PartnerConfigId | PARTNER_CONFIG_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
