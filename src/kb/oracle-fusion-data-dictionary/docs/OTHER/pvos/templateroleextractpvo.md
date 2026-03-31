---
id: DOC-OTHER-PVO-TemplateRoleExtractPVO
doc_type: system-doc
title: "TemplateRoleExtractPVO — PVO Cross-Module"
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
  - TemplateRoleExtractPVO
  - templateroleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateRoleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Role Extract. Acessa as tabelas: HRA_TMPL_ROLES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.TemplateRoleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_tmpl_roles|HRA_TMPL_ROLES]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hra_tmpl_roles|HRA_TMPL_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MinimumNumPcpns | MINIMUM_NUM_PCPNS | — | ✅ |
| 8 | ModuleId | MODULE_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RoleId | ROLE_ID | — | ✅ |
| 11 | RoleTypeCode | ROLE_TYPE_CODE | — | ✅ |
| 12 | TemplateDefnId | TEMPLATE_DEFN_ID | — | ✅ |
| 13 | TmplRoleId | TMPL_ROLE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
