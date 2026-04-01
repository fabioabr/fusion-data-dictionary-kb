---
id: DOC-PO-PVO-PoAgentPVO
doc_type: system-doc
title: "PoAgentPVO — PVO Purchasing"
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
  - PoAgentPVO
  - poagentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PoAgentPVO

## 📌 Visão Geral

Extrai os agentes de compras (buyers) com suas atribuições, incluindo nome, e-mail e unidade de negócio. Suporta auditoria de acessos, distribuição de workload e governança do processo de procurement.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PoAgentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 1 | 1 | 1 | 1 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_agents_v|PO_AGENTS_V]] — 1 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[po_agents_v|PO_AGENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgentId | AGENT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
