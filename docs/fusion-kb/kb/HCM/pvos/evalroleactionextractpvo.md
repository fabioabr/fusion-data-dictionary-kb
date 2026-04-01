---
id: DOC-HCM-PVO-EvalRoleActionExtractPVO
doc_type: system-doc
title: "EvalRoleActionExtractPVO — PVO Human Capital Management"
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
  - EvalRoleActionExtractPVO
  - evalroleactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvalRoleActionExtractPVO

## 📌 Visão Geral

Extrai ações realizadas por papéis em avaliações de desempenho (aprovar, revisar, submeter). Suporta auditoria de workflow de performance reviews.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.EvalRoleActionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_role_actions|HRA_EVAL_ROLE_ACTIONS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[hra_eval_role_actions|HRA_EVAL_ROLE_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EvalRoleActionId | EVAL_ROLE_ACTION_ID | 🔑 | ✅ |
| 5 | EvalRoleId | EVAL_ROLE_ID | — | ✅ |
| 6 | EvalSectionId | EVAL_SECTION_ID | — | ✅ |
| 7 | EvaluationId | EVALUATION_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PcpnEnterWrkCmtsFlag | PCPN_ENTER_WRK_CMTS_FLAG | — | ✅ |
| 13 | PersonProfileTypeId | PERSON_PROFILE_TYPE_ID | — | ✅ |
| 14 | QualifierId | QUALIFIER_ID | — | ✅ |
| 15 | ShareCommentsFlag | SHARE_COMMENTS_FLAG | — | ✅ |
| 16 | ShareRatingsFlag | SHARE_RATINGS_FLAG | — | ✅ |
| 17 | UpdateProfileFlag | UPDATE_PROFILE_FLAG | — | ✅ |
| 18 | ViewMgrQstnrFlag | VIEW_MGR_QSTNR_FLAG | — | ✅ |
| 19 | ViewPcpnNameFlag | VIEW_PCPN_NAME_FLAG | — | ✅ |
| 20 | ViewPcpnQstnrFlag | VIEW_PCPN_QSTNR_FLAG | — | ✅ |
| 21 | ViewPcpnRoleFlag | VIEW_PCPN_ROLE_FLAG | — | ✅ |
| 22 | ViewWrkQstnrFlag | VIEW_WRK_QSTNR_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
