---
id: DOC-HCM-PVO-ApplyFlowVersionPVO
doc_type: system-doc
title: "ApplyFlowVersionPVO — PVO Human Capital Management"
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
  - ApplyFlowVersionPVO
  - applyflowversionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplyFlowVersionPVO

## 📌 Visão Geral

Gerencia versoes dos fluxos de candidatura com tipo, status e codigo. Suporta versionamento e controle de mudancas nos processos de aplicacao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.ApplyFlowVersionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 3 | 1 | 18 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[irc_af_versions|IRC_AF_VERSIONS]] — 16 atributos (1 PKs, 11 BICC)
- [[irc_apply_flows_b|IRC_APPLY_FLOWS_B]] — 9 atributos (5 BICC)
- [[irc_apply_flows_tl|IRC_APPLY_FLOWS_TL]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[irc_af_versions|IRC_AF_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AfVersionId | AF_VERSION_ID | 🔑 | ✅ |
| 2 | ApplyFlowVersionPEOTcOptinEnabledFlag | TC_OPTIN_ENABLED_FLAG | — | ✅ |
| 3 | ApplyflowVersionPEOApplyFlowId | APPLY_FLOW_ID | — | ✅ |
| 4 | ApplyflowVersionPEOCreatedBy | CREATED_BY | — | — |
| 5 | ApplyflowVersionPEOCreationDate | CREATION_DATE | — | — |
| 6 | ApplyflowVersionPEOEsignEnabledFlag | ESIGN_ENABLED_FLAG | — | ✅ |
| 7 | ApplyflowVersionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ApplyflowVersionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ApplyflowVersionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ApplyflowVersionPEOLegalEnabledFlag | LEGAL_ENABLED_FLAG | — | ✅ |
| 11 | ApplyflowVersionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ApplyflowVersionPEOOptinEnabledFlag | OPTIN_ENABLED_FLAG | — | ✅ |
| 13 | ApplyflowVersionPEOSingleClickApplyFlag | SINGLE_CLICK_APPLY_FLAG | — | ✅ |
| 14 | ApplyflowVersionPEOVersionName | VERSION_NAME | — | ✅ |
| 15 | ApplyflowVersionPEOVersionStartDate | VERSION_START_DATE | — | ✅ |
| 16 | ApplyflowVersionPEOVersionStatusCode | VERSION_STATUS_CODE | — | ✅ |

### [[irc_apply_flows_b|IRC_APPLY_FLOWS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowBPEOAfCode | AF_CODE | — | ✅ |
| 2 | ApplyFlowBPEOAfStatusCode | AF_STATUS_CODE | — | ✅ |
| 3 | ApplyFlowBPEOAfTypeCode | AF_TYPE_CODE | — | ✅ |
| 4 | ApplyFlowBPEOApplyFlowId | APPLY_FLOW_ID | — | ✅ |
| 5 | ApplyFlowBPEOCreatedBy | CREATED_BY | — | — |
| 6 | ApplyFlowBPEOCreationDate | CREATION_DATE | — | — |
| 7 | ApplyFlowBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ApplyFlowBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ApplyFlowBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |

### [[irc_apply_flows_tl|IRC_APPLY_FLOWS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowTranslationPEOApplyFlowId | APPLY_FLOW_ID | — | — |
| 2 | ApplyFlowTranslationPEOApplyFlowName | APPLY_FLOW_NAME | — | ✅ |
| 3 | ApplyFlowTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ApplyFlowTranslationPEOLanguage | LANGUAGE | — | — |
| 5 | ApplyFlowTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
