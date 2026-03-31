---
id: DOC-OTHER-PVO-PartsReqLineDetailsExtractPVO
doc_type: system-doc
title: "PartsReqLineDetailsExtractPVO — PVO Cross-Module"
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
  - PartsReqLineDetailsExtractPVO
  - partsreqlinedetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartsReqLineDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Parts Req Line Details Extract. Acessa as tabelas: RCL_PARTS_REQ_LINE_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RclBiccExtractAM.PartsReqLineDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcl_parts_req_line_details|RCL_PARTS_REQ_LINE_DETAILS]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[rcl_parts_req_line_details|RCL_PARTS_REQ_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | ErrorText | ERROR_TEXT | — | ✅ |
| 4 | ExpectedArrivalDate | EXPECTED_ARRIVAL_DATE | — | ✅ |
| 5 | ExpectedShipDate | EXPECTED_SHIP_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ReqLineDetailId | REQ_LINE_DETAIL_ID | 🔑 | ✅ |
| 11 | RequirementLineId | REQUIREMENT_LINE_ID | — | ✅ |
| 12 | SourceCarrierId | SOURCE_CARRIER_ID | — | ✅ |
| 13 | SourceId | SOURCE_ID | — | ✅ |
| 14 | SourceModeOfTransport | SOURCE_MODE_OF_TRANSPORT | — | ✅ |
| 15 | SourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 16 | SourceRequestDate | SOURCE_REQUEST_DATE | — | ✅ |
| 17 | SourceServiceLevels | SOURCE_SERVICE_LEVELS | — | ✅ |
| 18 | SourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 19 | SourceType | SOURCE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
