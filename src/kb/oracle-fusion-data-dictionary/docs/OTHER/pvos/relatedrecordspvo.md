---
id: DOC-OTHER-PVO-RelatedRecordsPVO
doc_type: system-doc
title: "RelatedRecordsPVO — PVO Cross-Module"
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
  - RelatedRecordsPVO
  - relatedrecordspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RelatedRecordsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Related Records. Acessa as tabelas: FUSION_GRC.GRC_OTBI_FRC_REL_REC_RPT, GRC_OTBI_FRC_REL_REC_RPT.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RelatedRecordsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 2 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fusion_grc.grc_otbi_frc_rel_rec_rpt|FUSION_GRC.GRC_OTBI_FRC_REL_REC_RPT]] — 10 atributos (3 PKs, 10 BICC)
- [[grc_otbi_frc_rel_rec_rpt|GRC_OTBI_FRC_REL_REC_RPT]] — 3 atributos (3 BICC)

---

## ⚙️ Atributos

### [[fusion_grc.grc_otbi_frc_rel_rec_rpt|FUSION_GRC.GRC_OTBI_FRC_REL_REC_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedRecordsPEOAdvCtrlName | ADV_CTRL_NAME | — | ✅ |
| 2 | RelatedRecordsPEOControlId | CONTROL_ID | 🔑 | ✅ |
| 3 | RelatedRecordsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | RelatedRecordsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | RelatedRecordsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RelatedRecordsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RelatedRecordsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RelatedRecordsPEOPerspItems | PERSP_ITEMS | — | ✅ |
| 9 | RelatedRecordsPEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 10 | RelatedRecordsPEORiskId | RISK_ID | 🔑 | ✅ |

### [[grc_otbi_frc_rel_rec_rpt|GRC_OTBI_FRC_REL_REC_RPT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelatedRecordsPEOCtrlName | CONTROL_NAME | — | ✅ |
| 2 | RelatedRecordsPEOProcName | PROCESS_NAME | — | ✅ |
| 3 | RelatedRecordsPEORiskName | RISK_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
