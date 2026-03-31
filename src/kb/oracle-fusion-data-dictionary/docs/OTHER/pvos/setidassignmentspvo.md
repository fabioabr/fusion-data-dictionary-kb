---
id: DOC-OTHER-PVO-SetIdAssignmentsPVO
doc_type: system-doc
title: "SetIdAssignmentsPVO — PVO Cross-Module"
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
  - SetIdAssignmentsPVO
  - setidassignmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SetIdAssignmentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Set Id Assignments. Acessa as tabelas: FND_SETID_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.SetIdAssignmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 0 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DeterminantType | DETERMINANT_TYPE | — | ✅ |
| 4 | DeterminantValue | DETERMINANT_VALUE | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ReferenceGroupName | REFERENCE_GROUP_NAME | — | ✅ |
| 10 | SetId | SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
