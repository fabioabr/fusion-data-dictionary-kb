---
id: DOC-HCM-PVO-SetIdAssignmentsPVO
doc_type: system-doc
title: "SetIdAssignmentsPVO — PVO Human Capital Management"
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

Disponibiliza atribuições de Set ID com tipos determinantes e valores. Controla o particionamento de dados compartilhados entre unidades de negócio no ERP.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.SetIdAssignmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 4 | 6 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 10 atributos (4 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | DeterminantType | DETERMINANT_TYPE | 🔑 | ✅ |
| 4 | DeterminantValue | DETERMINANT_VALUE | 🔑 | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ReferenceGroupName | REFERENCE_GROUP_NAME | 🔑 | ✅ |
| 10 | SetId | SET_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
