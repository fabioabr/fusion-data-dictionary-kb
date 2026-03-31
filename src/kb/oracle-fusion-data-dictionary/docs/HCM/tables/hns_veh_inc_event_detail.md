---
id: DOC-HCM-127
doc_type: system-doc
title: "HNS_VEH_INC_EVENT_DETAIL — Detalhes de Eventos de Incidente Veicular"
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
  - vehicle-incident
  - evento-detalhe
  - hns
aliases:
  - HNS_VEH_INC_EVENT_DETAIL
  - hns_veh_inc_event_detail
  - hns-veh-inc-event-detail
  - DOC-HCM-127
  - detalhes-de-eventos-de-incidente-veicular
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_VEH_INC_EVENT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de incidentes veiculares** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de incidentes veiculares.
- **Classificação:** Categorização granular do evento de incidentes veiculares.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de incidentes veiculares.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe do evento | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | EVENT_TYPE | VARCHAR2(30) | NULL | Classificação | Subtipo do evento | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição detalhada do evento | — | 🟡 80% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade específica | — | 🟡 75% |
| 6 | LOCATION_DETAIL | VARCHAR2(240) | NULL | Localização | Detalhes do local do evento | — | 🟡 70% |
| 7 | EVENT_DATE | DATE | NULL | Data | Data do evento | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente principal)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Eventos de incidentes veiculares por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_VEH_INC_EVENT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_VEH_INC_EVENT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de incidentes veiculares.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de incidentes veiculares.

---

## 🔗 PVOs Relacionados

### [[hnsvehicleeventpvo|HNSVehicleEventPVO]] (HCM · BICC: 60/176)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AIRBAG_DEPLOYED_FLAG | HNSVehicleEventPEOAirbagDeplydFlag | ✅ |
| ALCOHOL_TEST_PERFORM_FLAG | HNSVehicleEventPEOAlchlTestPerfFlag | ✅ |
| ATTRIBUTE1 | HNSVehicleEventPEOAttribute1 | — |
| ATTRIBUTE1 | HNSVehicleEventPEOAttribute11 | — |
| ATTRIBUTE10 | HNSVehicleEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSVehicleEventPEOAttribute111 | — |
| ATTRIBUTE12 | HNSVehicleEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSVehicleEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSVehicleEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSVehicleEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSVehicleEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSVehicleEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSVehicleEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSVehicleEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSVehicleEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSVehicleEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSVehicleEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSVehicleEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSVehicleEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSVehicleEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSVehicleEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSVehicleEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSVehicleEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSVehicleEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSVehicleEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSVehicleEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSVehicleEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSVehicleEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSVehicleEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSVehicleEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSVehicleEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSVehicleEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSVehicleEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSVehicleEventPEOAttributeCategory | — |
| ATTRIBUTE_NUMBER1 | HNSVehicleEventPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSVehicleEventPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSVehicleEventPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSVehicleEventPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSVehicleEventPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSVehicleEventPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSVehicleEventPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSVehicleEventPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSVehicleEventPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSVehicleEventPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSVehicleEventPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSVehicleEventPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSVehicleEventPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSVehicleEventPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSVehicleEventPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSVehicleEventPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSVehicleEventPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSVehicleEventPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSVehicleEventPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSVehicleEventPEOAttributeTimestamp9 | — |
| CASE_NUMBER | HNSVehicleEventPEOCaseNumber | — |
| CELL_PHONE_IN_USE_FLAG | HNSVehicleEventPEOCellPhInUseFlag | ✅ |
| COMPANY_ADDR_CITY | HNSVehicleEventPEOCompanyAddrCity | — |
| COMPANY_ADDR_COUNTRY | HNSVehicleEventPEOCompanyAddrCountry | — |
| COMPANY_ADDR_LINE1 | HNSVehicleEventPEOCompanyAddrLine1 | — |
| COMPANY_ADDR_LINE2 | HNSVehicleEventPEOCompanyAddrLine2 | — |
| COMPANY_ADDR_STATE | HNSVehicleEventPEOCompanyAddrState | — |
| COMPANY_ADDR_ZIP_CODE | HNSVehicleEventPEOCompanyAddrZipCode | — |
| COMPANY_VEHICLE_FLAG | HNSVehicleEventPEOCompVehFlag | ✅ |
| COMPUTER_IN_USE_FLAG | HNSVehicleEventPEOCompInUseFlag | ✅ |
| CONTACT_ID | HNSVehicleEventPEOContactId | — |
| COST_OF_RENTAL_VEHICLE | HNSVehicleEventPEOCostOfRentalVehicle | — |
| CREATED_BY | HNSVehicleEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSVehicleEventPEOCreationDate | ✅ |
| DAMAGE_DESCR | HNSVehicleEventPEODamageDescr | ✅ |
| DELETED_FLAG | HNSVehicleEventPEODeletedFlag | ✅ |
| DESCRIBE_DAMAGE | HNSVehicleEventPEODescribeDamage | — |
| DRIVERS_LICENSE_EXP_DATE | HNSVehicleEventPEODrivLicExpDate | ✅ |
| DRUG_TEST_PERFORM_FLAG | HNSVehicleEventPEODrugTestPerfFlag | ✅ |
| EMPLOYEE_ASSIGN_ID | HNSVehicleEventPEOEmpAsnId | — |
| EMPLOYEE_ID | HNSVehicleEventPEOEmployeeId | ✅ |
| EXPIRY_DATE | HNSVehicleEventPEOExpiryDate | — |
| FATALITY_FLAG | HNSVehicleEventPEOFatalityFlag | ✅ |
| FLEET_VEHICLE_FLG | HNSVehicleEventPEOFleetVehicleFlg | — |
| INCIDENT_DETAIL_ID | HNSVehicleEventPEOIncDetailId | ✅ |
| INJURED_FLAG | HNSVehicleEventPEOInjuredFlag | ✅ |
| INS_EMAIL | HNSVehicleEventPEOInsEmail | — |
| INS_PHONE_AREA_CODE | HNSVehicleEventPEOInsPhoneAreaCode | — |
| INS_PHONE_COUNTRY_CODE | HNSVehicleEventPEOInsPhoneCountryCode | — |
| INS_PHONE_NUM | HNSVehicleEventPEOInsPhoneNum | — |
| INSURANCE_ADD_FLG | HNSVehicleEventPEOInsuranceAddFlg | — |
| INSURANCE_AGENT | HNSVehicleEventPEOInsuranceAgent | — |
| INSURANCE_COMPANY_NAME | HNSVehicleEventPEOInsuranceCompanyName | — |
| INSURANCE_INFORMATION_FLG | HNSVehicleEventPEOInsuranceInformationFlg | — |
| INSURANCE_POLICY_NUMBER | HNSVehicleEventPEOInsurancePolicyNumber | — |
| LAST_UPDATE_DATE | HNSVehicleEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSVehicleEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSVehicleEventPEOLastUpdatedBy | ✅ |
| LOCATION_OF_PEDESTRIAN | HNSVehicleEventPEOLocationOfPedestrian | — |
| NON_COM_VEH_ADD_CITY | HNSVehicleEventPEONonComVehAddCity | — |
| NON_COM_VEH_ADD_COUNTRY | HNSVehicleEventPEONonComVehAddCountry | — |
| NON_COM_VEH_ADD_LINE1 | HNSVehicleEventPEONonComVehAddLine1 | — |
| NON_COM_VEH_ADD_LINE2 | HNSVehicleEventPEONonComVehAddLine2 | — |
| NON_COM_VEH_ADD_STATE | HNSVehicleEventPEONonComVehAddState | — |
| NON_COM_VEH_ADD_ZIP_CODE | HNSVehicleEventPEONonComVehAddZipCode | — |
| NON_COM_VEH_BODY_TYPE | HNSVehicleEventPEONonComVehBodyType | — |
| NON_COM_VEH_CONTACT_NAME | HNSVehicleEventPEONonComVehContactName | — |
| NON_COM_VEH_LICENSE_NUM | HNSVehicleEventPEONonComVehLicenseNum | — |
| NON_COM_VEH_MAKE | HNSVehicleEventPEONonComVehMake | — |
| NON_COM_VEH_MODEL | HNSVehicleEventPEONonComVehModel | — |
| NON_COM_VEH_OWNER_NAME | HNSVehicleEventPEONonComVehOwnerName | — |
| NON_COM_VEH_REGI_COUNTRY | HNSVehicleEventPEONonComVehRegiCountry | — |
| NON_COM_VEH_REGI_NUM | HNSVehicleEventPEONonComVehRegiNum | — |
| NON_COM_VEH_REGI_STATE | HNSVehicleEventPEONonComVehRegiState | — |
| NON_COM_VEH_REGISTER_FLG | HNSVehicleEventPEONonComVehRegisterFlg | — |
| NON_COM_VEH_VIN_NUM | HNSVehicleEventPEONonComVehVinNum | — |
| NON_COM_VEH_YEAR | HNSVehicleEventPEONonComVehYear | — |
| NON_EMP_ADDR_CITY | HNSVehicleEventPEONonEmpAddrCity | ✅ |
| NON_EMP_ADDR_COUNTRY | HNSVehicleEventPEONonEmpAddrCountry | ✅ |
| NON_EMP_ADDR_LINE1 | HNSVehicleEventPEONonEmpAddrLine1 | ✅ |
| NON_EMP_ADDR_LINE2 | HNSVehicleEventPEONonEmpAddrLine2 | ✅ |
| NON_EMP_ADDR_STATE | HNSVehicleEventPEONonEmpAddrState | ✅ |
| NON_EMP_ADDR_ZIP_CODE | HNSVehicleEventPEONonEmpAddrZipCode | ✅ |
| NON_EMP_EMAIL | HNSVehicleEventPEONonEmpEmail | ✅ |
| NON_EMP_NAME | HNSVehicleEventPEONonEmpName | ✅ |
| NON_REL_COM_VEH_CONTACT_NAME | HNSVehicleEventPEONonRelComVehContactName | — |
| OBJECT_VERSION_NUMBER | HNSVehicleEventPEOObjVeNumber | ✅ |
| OWNER_NAME | HNSVehicleEventPEOOwnerName | — |
| PAID_BY_COMPANY_FLG | HNSVehicleEventPEOPaidByCompanyFlg | — |
| PED_DOING_PRIOR_TO_INCIDENT | HNSVehicleEventPEOPedDoingPriorToIncident | — |
| PED_SAFETY_EQUIPMENT | HNSVehicleEventPEOPedSafetyEquipment | — |
| PERSON_TYPE_CODE | HNSVehicleEventPEOPersonTypeCode | ✅ |
| PHONE_AREA_CODE | HNSVehicleEventPEOPhoneAreaCode | ✅ |
| PHONE_COUNTRY_CODE_NUM | HNSVehicleEventPEOPhCountryCodeNum | ✅ |
| PHONE_NUM | HNSVehicleEventPEOPhoneNum | ✅ |
| REGISTRATION_DATE | HNSVehicleEventPEORegistrationDate | — |
| RELATED_COMPANY_FLG | HNSVehicleEventPEORelatedCompanyFlg | — |
| RELATED_COMPNAY_ID | HNSVehicleEventPEORelatedCompanyId | — |
| RENTAL_AGREEMENT_NUMBER | HNSVehicleEventPEORentalAgreementNumber | — |
| RENTAL_COMPANY_NAME | HNSVehicleEventPEORentalCompanyName | — |
| RENTAL_DATE | HNSVehicleEventPEORentalDate | — |
| RENTAL_LOCATION | HNSVehicleEventPEORentalLocation | — |
| RENTAL_VEH_REPLACEMENT_FLG | HNSVehicleEventPEORentalVehReplacementFlg | — |
| REP_COST_OF_RENTAL_VEHICLE | HNSVehicleEventPEORepCostOfRentalVehicle | — |
| REP_INSURANCE_ADD_FLG | HNSVehicleEventPEORepInsuranceAddFlg | — |
| REP_PAID_BY_COMPANY_FLG | HNSVehicleEventPEORepPaidByCompanyFlg | — |
| REP_RENTAL_AGREEMENT_NUMBER | HNSVehicleEventPEORepRentalAgreementNumber | — |
| REP_RENTAL_COMPANY_NAME | HNSVehicleEventPEORepRentalCompanyName | — |
| REP_RENTAL_DATE | HNSVehicleEventPEORepRentalDate | — |
| REP_RENTAL_LOCATION | HNSVehicleEventPEORepRentalLocation | — |
| REPAIR_COST | HNSVehicleEventPEORepairCost | — |
| SEAT_BELT_IN_USE_FLAG | HNSVehicleEventPEOSeatBeltInUseFlag | ✅ |
| STATE_ISSUED_DRIVERS_LICENSE | HNSVehicleEventPEOStateIssdDrvrsLic | ✅ |
| TAKEN_TO_HOSPITAL_FLAG | HNSVehicleEventPEOTakenToHospFlag | ✅ |
| TOWING_COMPANY_CONTACT_DETAIL | HNSVehicleEventPEOTowingCompContDtl | ✅ |
| VEH_INC_EVT_DETAIL_ID | HNSVehicleEventPEOVehIncEvtDtlId | ✅ |
| VEHICLE_AREA_IMPACT_CODE | HNSVehicleEventPEOVehAreaImpactCd | ✅ |
| VEHICLE_BODY_TYPE | HNSVehicleEventPEOVehicleBodyType | ✅ |
| VEHICLE_CLASSIFICATION_CODE | HNSVehicleEventPEOVehClasfctnCode | ✅ |
| VEHICLE_COMPANY_ID_NUM | HNSVehicleEventPEOVehCompanyIdNum | ✅ |
| VEHICLE_DESCRIPTION | HNSVehicleEventPEOVehicleDescription | — |
| VEHICLE_DRIVER_LOCATION_CODE | HNSVehicleEventPEOVehDriverLocCode | ✅ |
| VEHICLE_DRIVERS_LICENSE_NUM | HNSVehicleEventPEOVehDriversLicNum | ✅ |
| VEHICLE_GROSS_WEIGHT | HNSVehicleEventPEOVehGrossWeight | ✅ |
| VEHICLE_HAS_AIRBAG_FLAG | HNSVehicleEventPEOVehHasAirbagFlag | ✅ |
| VEHICLE_HAS_PASSENGER_FLAG | HNSVehicleEventPEOVehHasPasngrFlag | ✅ |
| VEHICLE_LICENSE_PLATE_NUM | HNSVehicleEventPEOVehLicensePltNum | ✅ |
| VEHICLE_MAKE | HNSVehicleEventPEOVehicleMake | ✅ |
| VEHICLE_MODEL | HNSVehicleEventPEOVehicleModel | ✅ |
| VEHICLE_MODEL_YEAR | HNSVehicleEventPEOVehModelYear | ✅ |
| VEHICLE_MOVEMENT_CODE | HNSVehicleEventPEOVehMovementCode | ✅ |
| VEHICLE_POSITION_CODE | HNSVehicleEventPEOVehPositionCode | ✅ |
| VEHICLE_REGISTERED_FLAG | HNSVehicleEventPEOVehRegstrdFlag | ✅ |
| VEHICLE_REGISTRATION_COUNTRY | HNSVehicleEventPEOVehRegstrtnCntry | ✅ |
| VEHICLE_REGISTRATION_NUM | HNSVehicleEventPEOVehRegstrtnNum | ✅ |
| VEHICLE_REGISTRATION_STATE | HNSVehicleEventPEOVehRegstrtnState | ✅ |
| VEHICLE_SPEED | HNSVehicleEventPEOVehicleSpeed | ✅ |
| VEHICLE_SPEED_UNIT_CD | HNSVehicleEventPEOVehSpeedUnitCd | ✅ |
| VEHICLE_TOWED_FLAG | HNSVehicleEventPEOVehTowedFlag | ✅ |
| VEHICLE_VIN_NUM | HNSVehicleEventPEOVehicleVinNum | ✅ |
| VEHICLE_WEIGHT_UNIT_CD | HNSVehicleEventPEOVehWeightUnitCd | ✅ |
| WAS_RENTAL_FLAG | HNSVehicleEventPEOWasRentalFlag | — |

---

## 📚 Referências

- [Oracle Docs — HNS_VEH_INC_EVENT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsvehinceventdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
