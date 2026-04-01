---
id: DOC-HCM-PVO-HNSFireEventPVO
doc_type: system-doc
title: "HNSFireEventPVO — PVO Human Capital Management"
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
  - HNSFireEventPVO
  - hnsfireeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSFireEventPVO

## 📌 Visão Geral

Extrai eventos de incêndio registrados em saúde e segurança do trabalho. Suporta gestão de prevenção e combate a incêndios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSFireEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 1 | 23 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hns_fire_inc_event_detail|HNS_FIRE_INC_EVENT_DETAIL]] — 23 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[hns_fire_inc_event_detail|HNS_FIRE_INC_EVENT_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSFireEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | HNSFireEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | HNSFireEventPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | HNSFireEventPEOExplosionFlag | EXPLOSION_FLAG | — | ✅ |
| 5 | HNSFireEventPEOExplsnFuelOrEnergyCd | EXPLOSION_FUEL_OR_ENERGY_CODE | — | ✅ |
| 6 | HNSFireEventPEOExplsnIgntnSrcCd | EXPLOSION_IGNITION_SOURCE_CODE | — | ✅ |
| 7 | HNSFireEventPEOExplsnOriginCd | EXPLOSION_ORIGIN_CODE | — | ✅ |
| 8 | HNSFireEventPEOFireFlag | FIRE_FLAG | — | ✅ |
| 9 | HNSFireEventPEOFireFuelOrEnergyCd | FIRE_FUEL_OR_ENERGY_CODE | — | ✅ |
| 10 | HNSFireEventPEOFireIgntnSrcCode | FIRE_IGNITION_SOURCE_CODE | — | ✅ |
| 11 | HNSFireEventPEOFireIncEvtDtlId | FIRE_INC_EVT_DETAIL_ID | 🔑 | ✅ |
| 12 | HNSFireEventPEOFireOrgnCode | FIRE_ORIGIN_CODE | — | ✅ |
| 13 | HNSFireEventPEOIncDetailId | INCIDENT_DETAIL_ID | — | ✅ |
| 14 | HNSFireEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | HNSFireEventPEOLastUpdateLgn | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | HNSFireEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | HNSFireEventPEOMatFirstIgnitedCode | MATERIAL_FIRST_IGNITED_CODE | — | ✅ |
| 18 | HNSFireEventPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | HNSFireEventPEOPosCauseOfExplsnCd | POSSIBLE_CAUSE_OF_EXPLOSION_CD | — | ✅ |
| 20 | HNSFireEventPEOPosCauseOfFireCode | POSSIBLE_CAUSE_OF_FIRE_CODE | — | ✅ |
| 21 | HNSFireEventPEOReplnFireFghEquipFlag | REPLN_FIRE_FIGHTING_EQUIP_FLAG | — | ✅ |
| 22 | HNSFireEventPEOTypeOfExplsnCode | TYPE_OF_EXPLOSION_CODE | — | ✅ |
| 23 | HNSFireEventPEOTypeOfFireCode | TYPE_OF_FIRE_CODE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
