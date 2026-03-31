---
id: DOC-OTHER-PVO-DIRComponentDetailPVO
doc_type: system-doc
title: "DIRComponentDetailPVO — PVO Cross-Module"
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
  - DIRComponentDetailPVO
  - dircomponentdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DIRComponentDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de DIRComponent Detail. Acessa as tabelas: PAY_DIR_COMP_DETAILS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DeductionPersonRecsAM.DIRComponentDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 4 | 1 | 3 | 3 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[pay_dir_comp_details_f|PAY_DIR_COMP_DETAILS_F]] — 4 atributos (3 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_dir_comp_details_f|PAY_DIR_COMP_DETAILS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRComponentDetailDPEODirCardCompId | DIR_CARD_COMP_ID | — | — |
| 2 | DIRComponentDetailDPEODirCompDetailId | DIR_COMP_DETAIL_ID | 🔑 | ✅ |
| 3 | DIRComponentDetailDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | DIRComponentDetailDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
