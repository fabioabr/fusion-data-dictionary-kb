---
id: DOC-OTHER-PVO-GroupRuleMemberExtractPVO
doc_type: system-doc
title: "GroupRuleMemberExtractPVO — PVO Cross-Module"
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
  - GroupRuleMemberExtractPVO
  - grouprulememberextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupRuleMemberExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Rule Member Extract. Acessa as tabelas: CSE_GROUP_MEMBERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.GroupRuleMemberExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_group_members|CSE_GROUP_MEMBERS]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cse_group_members|CSE_GROUP_MEMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AssetId | ASSET_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | GroupId | GROUP_ID | 🔑 | ✅ |
| 6 | GroupMemberId | GROUP_MEMBER_ID | 🔑 | ✅ |
| 7 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 8 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
