---
id: DOC-OTHER-PVO-EquipmentAutomationProgramsExtractPVO
doc_type: system-doc
title: "EquipmentAutomationProgramsExtractPVO — PVO Cross-Module"
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
  - EquipmentAutomationProgramsExtractPVO
  - equipmentautomationprogramsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EquipmentAutomationProgramsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Equipment Automation Programs Extract. Acessa as tabelas: WIS_EQP_AUTOMATION_PROGRAMS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.EquipmentAutomationProgramsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_eqp_automation_programs|WIS_EQP_AUTOMATION_PROGRAMS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[wis_eqp_automation_programs|WIS_EQP_AUTOMATION_PROGRAMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EquipmentAutomationProgramsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | EquipmentAutomationProgramsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | EquipmentAutomationProgramsPEODocumentItemId | DOCUMENT_ITEM_ID | — | ✅ |
| 4 | EquipmentAutomationProgramsPEOEqpAutomationProgramId | EQP_AUTOMATION_PROGRAM_ID | 🔑 | ✅ |
| 5 | EquipmentAutomationProgramsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EquipmentAutomationProgramsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | EquipmentAutomationProgramsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | EquipmentAutomationProgramsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | EquipmentAutomationProgramsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 10 | EquipmentAutomationProgramsPEOResourceId | RESOURCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
