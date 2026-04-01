---
id: DOC-HCM-111
doc_type: system-doc
title: "FND_BPM_TASK_ASSIGNEE — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - FND_BPM_TASK_ASSIGNEE
  - fnd_bpm_task_assignee
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_BPM_TASK_ASSIGNEE

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNEE | — | — | — | — | — | — |
| 2 | ASSIGNEE_GROUP_OR_ROLE | — | — | — | — | — | — |
| 3 | ASSIGNEE_TYPE | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | DOMAIN | — | — | — | — | — | — |
| 7 | INITIATED_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | ORIGINAL_ASSIGNEE_USER | — | — | — | — | — | — |
| 12 | SEQUENCE | — | — | — | — | — | — |
| 13 | TASK_ID | — | — | — | — | — | — |
| 14 | VERSION | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[hcmapprovalstaskp1|HcmApprovalsTaskP1]] (AP · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNEE | FndBpmTaskAssigneePEOAssignee | ✅ |
| ASSIGNEE_GROUP_OR_ROLE | FndBpmTaskAssigneePEOAssigneeGroupOrRole | ✅ |
| ASSIGNEE_TYPE | FndBpmTaskAssigneePEOAssigneeType | ✅ |
| CREATED_BY | FndBpmTaskAssigneePEOCreatedBy4 | — |
| CREATION_DATE | FndBpmTaskAssigneePEOCreationDate4 | — |
| DOMAIN | FndBpmTaskAssigneePEODomain5 | — |
| INITIATED_DATE | FndBpmTaskAssigneePEOInitiatedDate5 | — |
| LAST_UPDATE_DATE | FndBpmTaskAssigneePEOLastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | FndBpmTaskAssigneePEOLastUpdateLogin4 | — |
| LAST_UPDATED_BY | FndBpmTaskAssigneePEOLastUpdatedBy4 | — |
| ORIGINAL_ASSIGNEE_USER | FndBpmTaskAssigneePEOOriginalAssigneeUser | ✅ |
| SEQUENCE | FndBpmTaskAssigneePEOSequence | ✅ |
| TASK_ID | FndBpmTaskAssigneePEOTaskId5 | — |
| VERSION | FndBpmTaskAssigneePEOVersion1 | — |
