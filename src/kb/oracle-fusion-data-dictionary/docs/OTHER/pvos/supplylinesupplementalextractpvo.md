---
id: DOC-OTHER-PVO-SupplyLineSupplementalExtractPVO
doc_type: system-doc
title: "SupplyLineSupplementalExtractPVO — PVO Cross-Module"
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
  - SupplyLineSupplementalExtractPVO
  - supplylinesupplementalextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyLineSupplementalExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Line Supplemental Extract. Acessa as tabelas: DOS_LINE_SUPPLEMENTAL_INFO.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyLineSupplementalExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_line_supplemental_info|DOS_LINE_SUPPLEMENTAL_INFO]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[dos_line_supplemental_info|DOS_LINE_SUPPLEMENTAL_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosLineSupplementalInfoPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DosLineSupplementalInfoPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DosLineSupplementalInfoPEODetailType | DETAIL_TYPE | — | ✅ |
| 4 | DosLineSupplementalInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | DosLineSupplementalInfoPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | DosLineSupplementalInfoPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | DosLineSupplementalInfoPEOLineId | LINE_ID | 🔑 | ✅ |
| 8 | DosLineSupplementalInfoPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | DosLineSupplementalInfoPEOTrackingLineId | TRACKING_LINE_ID | — | ✅ |
| 10 | DosLineSupplementalInfoPEOTrackingLnSuplmInfrmtnId | TRACKING_LN_SUPLM_INFRMTN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
