---
id: DOC-HCM-129
doc_type: system-doc
title: "HNS_VEH_INC_EVENT_SUMMARY — Resumo de Incidentes Veiculares"
system: Oracle Fusion Cloud HCM
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
  - health-safety
  - resumo-veicular
  - frota
  - hns
aliases:
  - HNS_VEH_INC_EVENT_SUMMARY
  - hns_veh_inc_event_summary
  - hns-veh-inc-event-summary
  - DOC-HCM-129
  - resumo-de-incidentes-veiculares
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_VEH_INC_EVENT_SUMMARY

## 📌 Visão Geral

Armazena o **resumo consolidado de incidentes veiculares** — dados agregados como total de envolvidos, veículos, custos estimados e classificação geral.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Visão consolidada:** Resumo de incidentes veiculares.
- **Indicadores de frota:** KPIs de segurança veicular.
- **Relatórios gerenciais:** Dados agregados para gestores de frota.
- **Custo de acidentes:** Estimativa financeira dos incidentes.
- **Análise de tendências:** Padrões de incidentes ao longo do tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VEH_INC_EVENT_SUMMARY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | VEH_INC_EVENT_ID | NUMBER(18) | NULL | FK | Detalhe do evento veicular | [[hns_veh_inc_event_detail]] | 🟡 80% |
| 4 | TOTAL_PASSENGERS | NUMBER | NULL | Indicador | Total de passageiros envolvidos | — | 🟡 70% |
| 5 | TOTAL_INJURED | NUMBER | NULL | Indicador | Total de lesionados | — | 🟡 70% |
| 6 | ESTIMATED_DAMAGE_COST | NUMBER | NULL | Financeiro | Custo estimado de danos | — | 🟡 65% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente do resumo de evento veicular)
- [[hns_veh_inc_event_detail]] — via `VEH_INC_EVENT_ID` (detalhe do evento veicular resumido)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Resumo de incidentes veiculares
```sql
SELECT s.TOTAL_PASSENGERS, s.TOTAL_INJURED,
       s.ESTIMATED_DAMAGE_COST, s.CURRENCY_CODE
FROM   HNS_VEH_INC_EVENT_SUMMARY s
WHERE  s.INCIDENT_ID = :p_incident_id;
```

### Custo total de incidentes veiculares
```sql
SELECT SUM(s.ESTIMATED_DAMAGE_COST) AS custo_total
FROM   HNS_VEH_INC_EVENT_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- Complementa dados detalhados com visão consolidada.
- O `ESTIMATED_DAMAGE_COST` inclui danos ao veículo e propriedade de terceiros.
- Dados alimentam relatórios de gestão de frota.
- Um incidente pode ter múltiplos resumos se houver atualização.

---

## 🔗 PVOs Relacionados

### [[hnsvehicleeventpvo|HNSVehicleEventPVO]] (HCM · BICC: 24/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HnsVehIncEventSummaryPEOAttribute1 | — |
| ATTRIBUTE10 | HnsVehIncEventSummaryPEOAttribute10 | — |
| ATTRIBUTE11 | HnsVehIncEventSummaryPEOAttribute11 | — |
| ATTRIBUTE12 | HnsVehIncEventSummaryPEOAttribute12 | — |
| ATTRIBUTE13 | HnsVehIncEventSummaryPEOAttribute13 | — |
| ATTRIBUTE14 | HnsVehIncEventSummaryPEOAttribute14 | — |
| ATTRIBUTE15 | HnsVehIncEventSummaryPEOAttribute15 | — |
| ATTRIBUTE16 | HnsVehIncEventSummaryPEOAttribute16 | — |
| ATTRIBUTE17 | HnsVehIncEventSummaryPEOAttribute17 | — |
| ATTRIBUTE18 | HnsVehIncEventSummaryPEOAttribute18 | — |
| ATTRIBUTE19 | HnsVehIncEventSummaryPEOAttribute19 | — |
| ATTRIBUTE2 | HnsVehIncEventSummaryPEOAttribute2 | — |
| ATTRIBUTE20 | HnsVehIncEventSummaryPEOAttribute20 | — |
| ATTRIBUTE21 | HnsVehIncEventSummaryPEOAttribute21 | — |
| ATTRIBUTE22 | HnsVehIncEventSummaryPEOAttribute22 | — |
| ATTRIBUTE23 | HnsVehIncEventSummaryPEOAttribute23 | — |
| ATTRIBUTE24 | HnsVehIncEventSummaryPEOAttribute24 | — |
| ATTRIBUTE25 | HnsVehIncEventSummaryPEOAttribute25 | — |
| ATTRIBUTE26 | HnsVehIncEventSummaryPEOAttribute26 | — |
| ATTRIBUTE27 | HnsVehIncEventSummaryPEOAttribute27 | — |
| ATTRIBUTE28 | HnsVehIncEventSummaryPEOAttribute28 | — |
| ATTRIBUTE29 | HnsVehIncEventSummaryPEOAttribute29 | — |
| ATTRIBUTE3 | HnsVehIncEventSummaryPEOAttribute3 | — |
| ATTRIBUTE30 | HnsVehIncEventSummaryPEOAttribute30 | — |
| ATTRIBUTE4 | HnsVehIncEventSummaryPEOAttribute4 | — |
| ATTRIBUTE5 | HnsVehIncEventSummaryPEOAttribute5 | — |
| ATTRIBUTE6 | HnsVehIncEventSummaryPEOAttribute6 | — |
| ATTRIBUTE7 | HnsVehIncEventSummaryPEOAttribute7 | — |
| ATTRIBUTE8 | HnsVehIncEventSummaryPEOAttribute8 | — |
| ATTRIBUTE9 | HnsVehIncEventSummaryPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HnsVehIncEventSummaryPEOAttrCat | — |
| ATTRIBUTE_NUMBER1 | HnsVehIncEventSummaryPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HnsVehIncEventSummaryPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HnsVehIncEventSummaryPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HnsVehIncEventSummaryPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HnsVehIncEventSummaryPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HnsVehIncEventSummaryPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HnsVehIncEventSummaryPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HnsVehIncEventSummaryPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HnsVehIncEventSummaryPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HnsVehIncEventSummaryPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HnsVehIncEventSummaryPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HnsVehIncEventSummaryPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HnsVehIncEventSummaryPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HnsVehIncEventSummaryPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HnsVehIncEventSummaryPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HnsVehIncEventSummaryPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HnsVehIncEventSummaryPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HnsVehIncEventSummaryPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HnsVehIncEventSummaryPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HnsVehIncEventSummaryPEOAttrTimestamp9 | — |
| CITATION_NUM | HnsVehIncEventSummaryPEOCitationNum | ✅ |
| CREATED_BY | HnsVehIncEventSummaryPEOCreatedBy | ✅ |
| CREATION_DATE | HnsVehIncEventSummaryPEOCreationDate | ✅ |
| DELETED_FLAG | HnsVehIncEventSummaryPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HnsVehIncEventSummaryPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HnsVehIncEventSummaryPEOLstUpdtDt | ✅ |
| LAST_UPDATE_LOGIN | HnsVehIncEventSummaryPEOLatUpdtLgn | ✅ |
| LAST_UPDATED_BY | HnsVehIncEventSummaryPEOLastUpdatedBy | ✅ |
| LIGHT_CONDITION_CODE | HnsVehIncEventSummaryPEOLightCondCd | ✅ |
| OBJECT_VERSION_NUMBER | HnsVehIncEventSummaryPEOObjVerNum | ✅ |
| POLICE_AGENCY_LOCATION | HnsVehIncEventSummaryPEOPoliceAgncLoc | ✅ |
| POLICE_BADGE_NUM | HnsVehIncEventSummaryPEOPoliceBadgeNum | ✅ |
| POLICE_REPORT_FLAG | HnsVehIncEventSummaryPEOPoliceReportFlag | ✅ |
| ROAD_CONDITION_CODE | HnsVehIncEventSummaryPEORoadCondCd | ✅ |
| TRAFFIC_CONDITION_CODE | HnsVehIncEventSummaryPEOTrafCondCd | ✅ |
| TRAFFIC_CONTROLS_CODE | HnsVehIncEventSummaryPEOTrafCtrlsCd | ✅ |
| VEH_INC_EVT_SUMMARY_ID | HnsVehIncEventSummaryPEOVehIncEvtSumId | ✅ |
| VEHICLE_ACC_CATEGORY_CODE | VehicleAccCategoryCode | ✅ |
| VEHICLE_COLLISION_TYPE_CODE | HnsVehIncEventSummaryPEOVehClsnTypCd | ✅ |
| VEHICLE_SPEED_LIMIT | HnsVehIncEventSummaryPEOVehSpeedLmt | ✅ |
| VEHICLE_SPEED_UNIT_CD | HnsVehIncEventSummaryPEOVehSpeedUntCd | ✅ |
| VEHICLE_STRUCK_BY_CODE | VehicleStruckByCode | ✅ |
| VEHICLE_STRUCK_CODE | HnsVehIncEventSummaryPEOVehStruckCode | ✅ |
| WEATHER_CONDITION_CODE | HnsVehIncEventSummaryPEOWeatherCondCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_VEH_INC_EVENT_SUMMARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsvehincsummary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
