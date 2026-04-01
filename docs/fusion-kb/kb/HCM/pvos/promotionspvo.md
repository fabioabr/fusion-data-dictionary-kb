---
id: DOC-HCM-PVO-PromotionsPVO
doc_type: system-doc
title: "PromotionsPVO — PVO Human Capital Management"
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
  - PromotionsPVO
  - promotionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PromotionsPVO

## 📌 Visão Geral

Extrai promoções registradas no Compensation Workbench, incluindo datas, atribuições e nomes. Suporta análise de movimentações de carreira e planejamento salarial.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PromotionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_promotions|CMP_CWB_PROMOTIONS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_promotions|CMP_CWB_PROMOTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PromotionId | PROMOTION_ID | 🔑 | ✅ |
| 2 | PromotionPEOAsgChangeDate | ASG_CHANGE_DATE | — | ✅ |
| 3 | PromotionPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 4 | PromotionPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 5 | PromotionPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PromotionPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PromotionPEOGradeId | GRADE_ID | — | ✅ |
| 8 | PromotionPEOGradeMaxVal | GRADE_MAX_VAL | — | ✅ |
| 9 | PromotionPEOGradeMidPoint | GRADE_MID_POINT | — | ✅ |
| 10 | PromotionPEOGradeMinVal | GRADE_MIN_VAL | — | ✅ |
| 11 | PromotionPEOJobId | JOB_ID | — | ✅ |
| 12 | PromotionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PromotionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PromotionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PromotionPEONewAssignmentOvn | NEW_ASSIGNMENT_OVN | — | ✅ |
| 16 | PromotionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PromotionPEOPersonId | PERSON_ID | — | ✅ |
| 18 | PromotionPEOPositionId | POSITION_ID | — | ✅ |
| 19 | PromotionPEOPromOrigUpdatedBy | PROM_ORIG_UPDATED_BY | — | ✅ |
| 20 | PromotionPEOPromUpdateDate | PROM_UPDATE_DATE | — | ✅ |
| 21 | PromotionPEOPromUpdatedBy | PROM_UPDATED_BY | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
