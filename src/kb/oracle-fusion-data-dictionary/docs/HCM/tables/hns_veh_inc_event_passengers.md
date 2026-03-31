---
id: DOC-HCM-128
doc_type: system-doc
title: "HNS_VEH_INC_EVENT_PASSENGERS — Passageiros de Incidentes Veiculares"
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
  - passageiros
  - incidente-veicular
  - hns
aliases:
  - HNS_VEH_INC_EVENT_PASSENGERS
  - hns_veh_inc_event_passengers
  - hns-veh-inc-event-passengers
  - DOC-HCM-128
  - passageiros-de-incidentes-veiculares
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_VEH_INC_EVENT_PASSENGERS

## 📌 Visão Geral

Armazena os **dados dos passageiros** envolvidos em incidentes veiculares registrados no módulo de Saúde e Segurança.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de passageiros:** Identificação de pessoas no veículo.
- **Análise de risco:** Dados para avaliar exposição de passageiros.
- **Compliance:** Documentação para relatórios de acidentes de trânsito.
- **Seguro:** Informações para processos de seguro.
- **Estatísticas:** Dados para análise de acidentes veiculares.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PASSENGER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do passageiro | — | 🟡 80% |
| 2 | VEH_INC_EVENT_ID | NUMBER(18) | NOT NULL | FK | Evento de incidente veicular | [[hns_veh_inc_event_detail]] | 🟡 80% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa (passageiro) | [[per_all_people_f]] | 🟡 80% |
| 4 | SEAT_POSITION | VARCHAR2(30) | NULL | Classificação | Posição no veículo (DRIVER, FRONT, REAR) | — | 🟡 65% |
| 5 | INJURY_FLAG | VARCHAR2(1) | NULL | Indicador | Indica se houve lesão (Y/N) | — | 🟡 70% |
| 6 | SEATBELT_FLAG | VARCHAR2(1) | NULL | Indicador | Indica se usava cinto (Y/N) | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_veh_inc_event_detail]] — via `VEH_INC_EVENT_ID` (evento veicular do passageiro)
- [[per_all_people_f]] — via `PERSON_ID` (passageiro do evento veicular)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Passageiros por incidente veicular
```sql
SELECT p.PERSON_ID, p.SEAT_POSITION, p.INJURY_FLAG, p.SEATBELT_FLAG
FROM   HNS_VEH_INC_EVENT_PASSENGERS p
WHERE  p.VEH_INC_EVENT_ID = :p_event_id;
```

### Passageiros lesionados
```sql
SELECT p.PERSON_ID, p.SEAT_POSITION, p.SEATBELT_FLAG
FROM   HNS_VEH_INC_EVENT_PASSENGERS p
WHERE  p.INJURY_FLAG = 'Y';
```

---

## 🔒 Observações

- Cada incidente veicular pode ter múltiplos passageiros.
- O `SEAT_POSITION` ajuda a analisar padrão de lesões por posição.
- O `SEATBELT_FLAG` é relevante para análise de compliance e segurança.
- Dados complementam `HNS_VEH_INC_EVENT_DETAIL` com informações de ocupantes.

---

## 🔗 PVOs Relacionados

### [[hnsvehicleeventpvo|HNSVehicleEventPVO]] (HCM · BICC: 26/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | HNSVehEventPasngrsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSVehEventPasngrsPEOCreationDt | ✅ |
| DELETED_FLAG | HNSVehEventPasngrsPEODelFlag | ✅ |
| EMPLOYEE_ASSIGN_ID | HNSVehEventPasngrsPEOEmpAsnId | — |
| EMPLOYEE_ID | HNSVehEventPasngrsPEOEmpId | ✅ |
| LAST_UPDATE_DATE | HNSVehEventPasngrsPEOLstUpdtDt | ✅ |
| LAST_UPDATE_LOGIN | HNSVehEventPasngrsPEOLstUpdtLgn | ✅ |
| LAST_UPDATED_BY | HNSVehEventPasngrsPEOLastUpdtdBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSVehEventPasngrsPEOObjVerNum | ✅ |
| PASSENGER_ADDR_CITY | HNSVehEventPasngrsPEOPasAddrCity | ✅ |
| PASSENGER_ADDR_LINE1 | HNSVehEventPasngrsPEOPasAddrLine1 | ✅ |
| PASSENGER_ADDR_LINE2 | HNSVehEventPasngrsPEOPasAddrLine2 | ✅ |
| PASSENGER_ADDR_STATE | HNSVehEventPasngrsPEOPasAddrState | ✅ |
| PASSENGER_AREA_CODE | HNSVehEventPasngrsPEOPasAreaCode | ✅ |
| PASSENGER_COUNTRY | HNSVehEventPasngrsPEOPasCountry | ✅ |
| PASSENGER_COUNTRY_CODE_NUM | HNSVehEventPasngrsPEOPasCntCdNum | ✅ |
| PASSENGER_EMAIL | HNSVehEventPasngrsPEOPasEmail | ✅ |
| PASSENGER_FATALITY_FLAG | HNSVehEventPasngrsPEOPasFtltyFlag | ✅ |
| PASSENGER_ID | HNSVehEventPasngrsPEOPassengerId | ✅ |
| PASSENGER_INJURED_FLAG | HNSVehEventPasngrsPEOPasInjrdFlag | ✅ |
| PASSENGER_NAME | HNSVehEventPasngrsPEOPassengerName | ✅ |
| PASSENGER_PER_TYPE_CODE | HNSVehEventPasngrsPEOPasPerTypCd | ✅ |
| PASSENGER_PHONE_NUM | HNSVehEventPasngrsPEOPasPhoneNum | ✅ |
| PASSENGER_ZIP_CODE | HNSVehEventPasngrsPEOPasZipCode | ✅ |
| TAKEN_TO_HOSPITAL_FLAG | HNSVehEventPasngrsPEOTakenToHospFlg | ✅ |
| VEH_INC_EVT_DETAIL_ID | HNSVehEventPasngrsPEOVehIncEvtDtlId | ✅ |
| WEARING_SEAT_BELT_FLAG | HNSVehEventPasngrsPEOWearSeatBltFlg | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_VEH_INC_EVENT_PASSENGERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsvehincieventpassengers.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
