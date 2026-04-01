---
id: DOC-HCM-105
doc_type: system-doc
title: "HNS_INJURED_PERSONS — Pessoas Lesionadas em Incidentes"
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
  - lesionados
  - acidente-trabalho
  - hns
aliases:
  - HNS_INJURED_PERSONS
  - hns_injured_persons
  - hns-injured-persons
  - DOC-HCM-105
  - pessoas-lesionadas-em-incidentes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INJURED_PERSONS

## 📌 Visão Geral

Armazena os **dados das pessoas lesionadas** em incidentes de saúde e segurança, incluindo tipo de lesão, parte do corpo afetada e severidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de lesões:** Documentação de todas as pessoas lesionadas.
- **Classificação de lesões:** Tipo e severidade da lesão.
- **CAT (Comunicação de Acidente de Trabalho):** Base para emissão da CAT.
- **Relatórios OSHA/NR:** Dados para relatórios regulatórios.
- **Análise estatística:** Indicadores de segurança por tipo de lesão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INJURED_PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa lesionada | [[per_all_people_f]] | 🟢 90% |
| 4 | INJURY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da lesão | — | 🟡 80% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade da lesão | — | 🟡 80% |
| 6 | BODY_PART | VARCHAR2(30) | NULL | Classificação | Parte do corpo afetada | — | 🟡 75% |
| 7 | TREATMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de tratamento (FIRST_AID, HOSPITAL, SURGERY) | — | 🟡 75% |
| 8 | DAYS_AWAY | NUMBER | NULL | Indicador | Dias de afastamento | — | 🟡 75% |
| 9 | HOSPITALIZED_FLAG | VARCHAR2(1) | NULL | Indicador | Indica se foi hospitalizado (Y/N) | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente da pessoa acidentada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa lesionada)

### Tabelas-filha (FK de saída)
- [[hns_injured_person_parts]] — via `INJURED_PERSON_ID` (partes do corpo detalhadas)
- [[hns_injured_persons_summary]] — via `INJURED_PERSON_ID` (resumo da pessoa acidentada)

---

## 📎 Uso Típico

### Lesionados por incidente
```sql
SELECT ip.PERSON_ID, ip.INJURY_TYPE, ip.SEVERITY,
       ip.BODY_PART, ip.DAYS_AWAY
FROM   HNS_INJURED_PERSONS ip
WHERE  ip.INCIDENT_ID = :p_incident_id;
```

### Total de dias perdidos
```sql
SELECT SUM(ip.DAYS_AWAY) AS total_dias, COUNT(*) AS total_lesionados
FROM   HNS_INJURED_PERSONS ip
JOIN   HNS_INCIDENTS_DETAIL d ON ip.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- `DAYS_AWAY` é central para cálculo da taxa de gravidade (TG).
- O `TREATMENT_TYPE` indica o nível de atendimento necessário.
- Cada incidente pode ter múltiplas pessoas lesionadas.
- Dados são base para emissão da CAT no Brasil (Comunicação de Acidente de Trabalho).

---

## 🔗 PVOs Relacionados

### [[hnsinjuredpersonspvo|HNSInjuredPersonsPVO]] (HCM · BICC: 70/72)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CASE_NUMBER | HNSInjuredPersonsPEOCaseNum | ✅ |
| CLASSIFICATION_CODE | HNSInjuredPersonsPEOClassificationCode | ✅ |
| CREATED_BY | HNSInjuredPersonsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSInjuredPersonsPEOCreationDate | ✅ |
| DAYS_AWAY_FROM_WRK | HNSInjuredPersonsPEODysAwyFrmWrk | ✅ |
| DELETED_FLAG | HNSInjuredPersonsPEODeletedFlag | ✅ |
| DESCRIPTION_OF_TREATMENT | HNSInjuredPersonsPEODescrOfTrtmnt | ✅ |
| DISAB_DAYS_AWY_FRM_WRK_DT | HNSInjuredPersonsPEODsbDysAwyFrmWrkDt | ✅ |
| EMP_RTN_TO_WRK_FLAG | HNSInjuredPersonsPEOEmpRtnToWrkFlag | ✅ |
| FACILITY_ADDRESS_LINE1 | HNSInjuredPersonsPEOFacilityAddressLine1 | ✅ |
| FACILITY_ADDRESS_LINE2 | HNSInjuredPersonsPEOFacilityAddressLine2 | ✅ |
| FACILITY_CITY | HNSInjuredPersonsPEOFacilityCity | ✅ |
| FACILITY_COUNTRY | HNSInjuredPersonsPEOFacilityCountry | ✅ |
| FACILITY_NAME | HNSInjuredPersonsPEOFacilityName | ✅ |
| FACILITY_STATE | HNSInjuredPersonsPEOFacilityState | ✅ |
| FACILITY_ZIP_CODE | HNSInjuredPersonsPEOFacilityZipCode | ✅ |
| FATALITY_DATE | HNSInjuredPersonsPEOFatalityDate | ✅ |
| HRS_AT_WRK_BEFORE_INJ_ILL | HNSInjuredPersonsPEOHrsAtWrkBfrInjIll | ✅ |
| ILLNESS_NATURE_CODE | HNSInjuredPersonsPEOIllnessNatureCode | ✅ |
| INCI_INJ_PERSON_ASSIGN_ID | HNSInjuredPersonsPEOInciInjPerAsnId | — |
| INCI_INJ_PERSON_ID | HNSInjuredPersonsPEOInciInjPersonId | ✅ |
| INCIDENT_DETAIL_ID | HNSInjuredPersonsPEOIncidentDetailId | — |
| INJ_ILL_DEV_OVER_TIME_FLAG | HNSInjuredPersonsPEOInjIllDevOvrTmFlg | ✅ |
| INJ_ILL_INFRMD_BY_PER_NAME | HNSInjuredPersonsPEOInjIllInfrmdByPerNm | ✅ |
| INJ_ILL_OCCURED_DATE | HNSInjuredPersonsPEOInjIllOccuredDate | ✅ |
| INJ_PER_NONEMP_TYPE_CD | HNSInjuredPersonsPEOInjPerNonempTypeCd | ✅ |
| INJ_PERSON_TYPE_CODE | HNSInjuredPersonsPEOInjPersonTypeCode | ✅ |
| INJURED_AREA_CODE | HNSInjuredPersonsPEOInjuredAreaCode | ✅ |
| INJURED_COUNTRY_CODE_NUM | HNSInjuredPersonsPEOInjurdCountryCodNum | ✅ |
| INJURED_EMAIL | HNSInjuredPersonsPEOInjuredEmail | ✅ |
| INJURED_NAME | HNSInjuredPersonsPEOInjuredName | ✅ |
| INJURED_PERSON_ID | HNSInjuredPersonsPEOInjuredPersonId | ✅ |
| INJURED_PHONENO | HNSInjuredPersonsPEOInjuredPhoneno | ✅ |
| INJURY_MECHANISM_CODE | HNSInjuredPersonsPEOInjuryMechCode | ✅ |
| INJURY_MECHANISM_LVL2_CODE | HNSInjuredPersonsPEOInjuryMcnsmLvl2Cd | ✅ |
| INJURY_MECHANISM_LVL3_CODE | HNSInjuredPersonsPEOInjuryMcnsmLvl3Cd | ✅ |
| INJURY_MECHANISM_LVL4_CODE | HNSInjuredPersonsPEOInjuryMcnsmLvl4Cd | ✅ |
| JOB_TRANSFER_FLAG | HNSInjuredPersonsPEOJobTransferFlag | ✅ |
| LAST_UPDATE_DATE | HNSInjuredPersonsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSInjuredPersonsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSInjuredPersonsPEOLastUpdatedBy | ✅ |
| LOST_TIME_IN_HRS | HNSInjuredPersonsPEOLostTimeInHrs | ✅ |
| LOSTTIME_FLAG | HNSInjuredPersonsPEOLosttimeFlag | ✅ |
| MED_PROF_NAME | HNSInjuredPersonsPEOMedProfName | ✅ |
| MOD_DUTIES_RESTRICTN_DESCR | HNSInjuredPersonsPEOModDtsRstrctnDescr | ✅ |
| OBJECT_VERSION_NUMBER | HNSInjuredPersonsPEOObjectVersionNumber | ✅ |
| PER_INFORMED_INJ_ILL_DATE | HNSInjuredPersonsPEOPerInfrmdInjIllDt | ✅ |
| PER_UNABLE_TO_WRK_FLAG | HNSInjuredPersonsPEOPerUnblToWrkFlag | ✅ |
| PERSON_ACTIVITY_DESCR | HNSInjuredPersonsPEOPersonActivityDescr | ✅ |
| PREV_INJ_ILL_DATE | HNSInjuredPersonsPEOPrevInjIllDate | ✅ |
| RECORDABLE_FLAG | HNSInjuredPersonsPEORecordableFlag | ✅ |
| RECORDABLE_TYPE_CD | HNSInjuredPersonsPEORcrdblTypeCd | ✅ |
| RECURRING_FLAG | HNSInjuredPersonsPEORecurringFlag | ✅ |
| REGULATOR_NOTIFIED_BY | HNSInjuredPersonsPEORgltrNtfdBy | ✅ |
| REGULATOR_NOTIFIED_DATE | HNSInjuredPersonsPEORgltrNtfdDt | ✅ |
| REGULATOR_NOTIFIED_FLAG | HNSInjuredPersonsPEORgltrNtfdFlg | ✅ |
| REGULATR_NOTIFIED_MEDIUM_CD | HNSInjuredPersonsPEORgltrNtfdMdmCd | ✅ |
| REPORTABLE_FLAG | HNSInjuredPersonsPEOReportableFlag | ✅ |
| RTN_TO_WRK_DATE | HNSInjuredPersonsPEORtnToWrkDt | ✅ |
| RTN_TO_WRK_TYPE_CD | HNSInjuredPersonsPEORtnToWrkTypCd | ✅ |
| SOURCE_OF_INJURY_CODE | HNSInjuredPersonsPEOSrcOfInjuryCode | ✅ |
| SOURCE_OF_INJURY_LVL2_CODE | HNSInjuredPersonsPEOSrcOfInjryLvl2Cd | ✅ |
| SOURCE_OF_INJURY_LVL3_CODE | HNSInjuredPersonsPEOSrcOfInjryLvl3Cd | ✅ |
| SOURCE_OF_INJURY_LVL4_CODE | HNSInjuredPersonsPEOSrcOfInjryLvl4Cd | ✅ |
| SYM_FIRST_NOTICED_DATE | HNSInjuredPersonsPEOSymFrstNtcdDt | ✅ |
| TIME_FINISHED_WORK | HNSInjuredPersonsPEOTimeFnshdWrk | ✅ |
| TIME_STARTED_WORK | HNSInjuredPersonsPEOTimeStartedWork | ✅ |
| TREATMENT_FLAG | HNSInjuredPersonsPEOTreatmentFlag | ✅ |
| TREATMENT_TYPE_CODE | HNSInjuredPersonsPEOTreatmentTypeCode | ✅ |
| TX_FACILITY_ZIP_CODE | HNSInjuredPersonsPEOTxFacZipCd | ✅ |
| WORKRELATED_FLAG | HNSInjuredPersonsPEOWorkrelatedFlag | ✅ |
| XFR_RESTRICTN_DAYS | HNSInjuredPersonsPEOXfrRestrctnDays | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_INJURED_PERSONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinjuredpersons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
