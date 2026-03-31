---
id: DOC-PO-PVO-InitiativeEvaluationTeamExtractPVO
doc_type: system-doc
title: "InitiativeEvaluationTeamExtractPVO — PVO Purchasing"
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
  - InitiativeEvaluationTeamExtractPVO
  - initiativeevaluationteamextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativeEvaluationTeamExtractPVO

## 📌 Visão Geral

Extrai as equipes de avaliação vinculadas a iniciativas de qualificação para carga BICC. Permite análise de alocação de recursos e carga de trabalho em campanhas de homologação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.InitiativeEvaluationTeamExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_evaluation_team|POQ_EVALUATION_TEAM]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[poq_evaluation_team|POQ_EVALUATION_TEAM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddedBy | ADDED_BY | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EvaluationTeamId | EVALUATION_TEAM_ID | 🔑 | ✅ |
| 5 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TeamMemberId | TEAM_MEMBER_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
