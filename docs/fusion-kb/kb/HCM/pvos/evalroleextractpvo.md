---
id: DOC-HCM-PVO-EvalRoleExtractPVO
doc_type: system-doc
title: "EvalRoleExtractPVO — PVO Human Capital Management"
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
  - EvalRoleExtractPVO
  - evalroleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvalRoleExtractPVO

## 📌 Visão Geral

Extrai definições de papéis em avaliações de desempenho (gestor, auto, par). Utilizado na configuração de fluxos e permissões de performance review.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.EvalRoleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_roles|HRA_EVAL_ROLES]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hra_eval_roles|HRA_EVAL_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EvalRoleId | EVAL_ROLE_ID | 🔑 | ✅ |
| 5 | EvaluationId | EVALUATION_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MinimumNumPcpns | MINIMUM_NUM_PCPNS | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | RoleTypeCode | ROLE_TYPE_CODE | — | ✅ |
| 12 | TmplRoleId | TMPL_ROLE_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
