---
id: DOC-HCM-PVO-ApplyFlowPVO
doc_type: system-doc
title: "ApplyFlowPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ApplyFlowPVO
  - applyflowpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplyFlowPVO

## 📌 Visão Geral

Disponibiliza fluxos de candidatura com codigo, status e nome traduzido. Base para configuracao e gestao dos processos de aplicacao em recrutamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.ApplyFlowPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 6 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[irc_apply_flows_b|IRC_APPLY_FLOWS_B]] — 9 atributos (1 PKs, 3 BICC)
- [[irc_apply_flows_tl|IRC_APPLY_FLOWS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_apply_flows_b|IRC_APPLY_FLOWS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowBPEOAfCode | AF_CODE | — | ✅ |
| 2 | ApplyFlowBPEOAfStatusCode | AF_STATUS_CODE | — | — |
| 3 | ApplyFlowBPEOAfTypeCode | AF_TYPE_CODE | — | — |
| 4 | ApplyFlowBPEOCreatedBy | CREATED_BY | — | — |
| 5 | ApplyFlowBPEOCreationDate | CREATION_DATE | — | — |
| 6 | ApplyFlowBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ApplyFlowBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ApplyFlowBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ApplyFlowId | APPLY_FLOW_ID | 🔑 | ✅ |

### [[irc_apply_flows_tl|IRC_APPLY_FLOWS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowTranslationPEOApplyFlowId1 | APPLY_FLOW_ID | — | — |
| 2 | ApplyFlowTranslationPEOApplyFlowName | APPLY_FLOW_NAME | — | ✅ |
| 3 | ApplyFlowTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | ApplyFlowTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | ApplyFlowTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | ApplyFlowTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ApplyFlowTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ApplyFlowTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ApplyFlowTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ApplyFlowTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ApplyFlowTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
