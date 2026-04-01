---
id: DOC-PO-PVO-PurchasingAgentAccessesExtractPVO
doc_type: system-doc
title: "PurchasingAgentAccessesExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingAgentAccessesExtractPVO
  - purchasingagentaccessesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAgentAccessesExtractPVO

## 📌 Visão Geral

Extrai os acessos e permissões dos agentes de compras para carga BICC, incluindo unidades de negócio, categorias e tipos de documento. Fundamental para auditoria de segregação de funções.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingAgentAccessesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 2 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_users|PER_USERS]] — 3 atributos (3 BICC)
- [[po_agent_accesses|PO_AGENT_ACCESSES]] — 14 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserGuid | USER_GUID | — | ✅ |
| 2 | UserId | USER_ID | — | ✅ |
| 3 | Username | USERNAME | — | ✅ |

### [[po_agent_accesses|PO_AGENT_ACCESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessActionCode | ACCESS_ACTION_CODE | 🔑 | ✅ |
| 2 | AccessOthersLevelCode | ACCESS_OTHERS_LEVEL_CODE | — | ✅ |
| 3 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 4 | AgentId | AGENT_ID | — | ✅ |
| 5 | AllowedFlag | ALLOWED_FLAG | — | ✅ |
| 6 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | DefaultReqBuId | DEFAULT_REQ_BU_ID | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PrcBuId | PRC_BU_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
