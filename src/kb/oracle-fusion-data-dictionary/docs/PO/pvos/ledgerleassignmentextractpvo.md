---
id: DOC-PO-PVO-LedgerLeAssignmentExtractPVO
doc_type: system-doc
title: "LedgerLeAssignmentExtractPVO — PVO Purchasing"
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
  - LedgerLeAssignmentExtractPVO
  - ledgerleassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerLeAssignmentExtractPVO

## 📌 Visão Geral

Extrai atribuições de entidades legais a ledgers no contexto de sustentabilidade em procurement. Suporta a correta contabilização por entidade jurídica e consolidação de relatórios ESG.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.LedgerLeAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_ledger_le_assignments|SUS_LEDGER_LE_ASSIGNMENTS]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[sus_ledger_le_assignments|SUS_LEDGER_LE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LedgerId | LEDGER_ID | — | ✅ |
| 8 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
