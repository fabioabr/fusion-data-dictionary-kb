---
id: DOC-OTHER-PVO-PSCFeeSchedulePVO
doc_type: system-doc
title: "PSCFeeSchedulePVO — PVO Cross-Module"
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
  - PSCFeeSchedulePVO
  - pscfeeschedulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCFeeSchedulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCFee Schedule. Acessa as tabelas: PSC_COM_FEE_ITEM_TL, PSC_LNP_FEE_RECORD, PSC_LNP_FEE_SCHEDULE_TL (+4).

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCFeeSchedulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 604 | 7 | 1 | 463 | 77% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_fee_item_tl|PSC_COM_FEE_ITEM_TL]] — 11 atributos (1 BICC)
- [[psc_lnp_fee_record|PSC_LNP_FEE_RECORD]] — 32 atributos (1 PKs, 15 BICC)
- [[psc_lnp_fee_schedule_tl|PSC_LNP_FEE_SCHEDULE_TL]] — 13 atributos (1 BICC)
- [[psc_lnp_field_groups|PSC_LNP_FIELD_GROUPS]] — 414 atributos (414 BICC)
- [[psc_lnp_record|PSC_LNP_RECORD]] — 111 atributos (30 BICC)
- [[psc_lnp_record_status_tl|PSC_LNP_RECORD_STATUS_TL]] — 11 atributos (1 BICC)
- [[psc_lnp_record_status_vl|PSC_LNP_RECORD_STATUS_VL]] — 12 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_com_fee_item_tl|PSC_COM_FEE_ITEM_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FeeItemTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | FeeItemTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | FeeItemTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | FeeItemTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | FeeItemTLPEOFeeItemId | FEE_ITEM_ID | — | — |
| 6 | FeeItemTLPEOLanguage | LANGUAGE | — | — |
| 7 | FeeItemTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | FeeItemTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | FeeItemTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | FeeItemTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | FeeItemTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_fee_record|PSC_LNP_FEE_RECORD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FeeSchedulePEOAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | FeeSchedulePEOAcctEventStatus | ACCT_EVENT_STATUS | — | — |
| 3 | FeeSchedulePEOAgencyId | AGENCY_ID | — | — |
| 4 | FeeSchedulePEOAssessedDate | ASSESSED_DATE | — | — |
| 5 | FeeSchedulePEOBillType | BILL_TYPE | — | — |
| 6 | FeeSchedulePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | FeeSchedulePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | FeeSchedulePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | FeeSchedulePEODepartmentId | DEPARTMENT_ID | — | — |
| 10 | FeeSchedulePEOFeeAmount | FEE_AMOUNT | — | ✅ |
| 11 | FeeSchedulePEOFeeItemId | FEE_ITEM_ID | — | ✅ |
| 12 | FeeSchedulePEOFeeMemo | FEE_MEMO | — | ✅ |
| 13 | FeeSchedulePEOFeeQuantity | FEE_QUANTITY | — | ✅ |
| 14 | FeeSchedulePEOFeeRecordKey | FEE_RECORD_KEY | 🔑 | ✅ |
| 15 | FeeSchedulePEOFeeScheduleId | FEE_SCHEDULE_ID | — | ✅ |
| 16 | FeeSchedulePEOFeeScheduleLine | FEE_SCHEDULE_LINE | — | ✅ |
| 17 | FeeSchedulePEOFeeSource | FEE_SOURCE | — | ✅ |
| 18 | FeeSchedulePEOFeeStatus | FEE_STATUS | — | ✅ |
| 19 | FeeSchedulePEOInvoice | INVOICE | — | — |
| 20 | FeeSchedulePEOInvoiceLine | INVOICE_LINE | — | — |
| 21 | FeeSchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | FeeSchedulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 23 | FeeSchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | FeeSchedulePEOLicensePeriod | LICENSE_PERIOD | — | — |
| 25 | FeeSchedulePEOLnpRecordId | LNP_RECORD_ID | — | — |
| 26 | FeeSchedulePEOLnpRecordKey | LNP_RECORD_KEY | — | — |
| 27 | FeeSchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | FeeSchedulePEOPaymentDate | PAYMENT_DATE | — | — |
| 29 | FeeSchedulePEOPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 30 | FeeSchedulePEOPaymentReferenceId | PAYMENT_REFERENCE_ID | — | ✅ |
| 31 | FeeSchedulePEOReceiptNumber | RECEIPT_NUMBER | — | — |
| 32 | FeeSchedulePEORevrecDateOption | REVREC_DATE_OPTION | — | — |

### [[psc_lnp_fee_schedule_tl|PSC_LNP_FEE_SCHEDULE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FeeScheduleTLDPEOAgencyId | AGENCY_ID | — | — |
| 2 | FeeScheduleTLDPEOCreatedBy | CREATED_BY | — | — |
| 3 | FeeScheduleTLDPEOCreationDate | CREATION_DATE | — | — |
| 4 | FeeScheduleTLDPEODescription | DESCRIPTION | — | ✅ |
| 5 | FeeScheduleTLDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | FeeScheduleTLDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | FeeScheduleTLDPEOFeeScheduleId | FEE_SCHEDULE_ID | — | — |
| 8 | FeeScheduleTLDPEOLanguage | LANGUAGE | — | — |
| 9 | FeeScheduleTLDPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | FeeScheduleTLDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | FeeScheduleTLDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | FeeScheduleTLDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | FeeScheduleTLDPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_field_groups|PSC_LNP_FIELD_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitFieldGroupPEOAgencyId | AGENCY_ID | — | ✅ |
| 2 | PermitFieldGroupPEOAreaUom | AREA_UOM | — | ✅ |
| 3 | PermitFieldGroupPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PermitFieldGroupPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PermitFieldGroupPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | PermitFieldGroupPEODemDemolitionReason | DEM_DEMOLITION_REASON | — | ✅ |
| 7 | PermitFieldGroupPEODemDisposalSite | DEM_DISPOSAL_SITE | — | ✅ |
| 8 | PermitFieldGroupPEODemElectricReleaseDate | DEM_ELECTRIC_RELEASE_DATE | — | ✅ |
| 9 | PermitFieldGroupPEODemEntireStructureFlag | DEM_ENTIRE_STRUCTURE_FLAG | — | ✅ |
| 10 | PermitFieldGroupPEODemGasFlag | DEM_GAS_FLAG | — | ✅ |
| 11 | PermitFieldGroupPEODemGasUtilReleaseDate | DEM_GAS_UTIL_RELEASE_DATE | — | ✅ |
| 12 | PermitFieldGroupPEODemHazMatCertNumber | DEM_HAZ_MAT_CERT_NUMBER | — | ✅ |
| 13 | PermitFieldGroupPEODemHazMatCertReqFlag | DEM_HAZ_MAT_CERT_REQ_FLAG | — | ✅ |
| 14 | PermitFieldGroupPEODemHistoricDistrictFlag | DEM_HISTORIC_DISTRICT_FLAG | — | ✅ |
| 15 | PermitFieldGroupPEODemLandmarkFlag | DEM_LANDMARK_FLAG | — | ✅ |
| 16 | PermitFieldGroupPEODemMatlTransportMthd | DEM_MATL_TRANSPORT_MTHD | — | ✅ |
| 17 | PermitFieldGroupPEODemMethod | DEM_METHOD | — | ✅ |
| 18 | PermitFieldGroupPEODemNumStories | DEM_NUM_STORIES | — | ✅ |
| 19 | PermitFieldGroupPEODemOverallHeight | DEM_OVERALL_HEIGHT | — | ✅ |
| 20 | PermitFieldGroupPEODemPowerFlag | DEM_POWER_FLAG | — | ✅ |
| 21 | PermitFieldGroupPEODemSewerFlag | DEM_SEWER_FLAG | — | ✅ |
| 22 | PermitFieldGroupPEODemSewerUtilReleaseDate | DEM_SEWER_UTIL_RELEASE_DATE | — | ✅ |
| 23 | PermitFieldGroupPEODemStructureDescr | DEM_STRUCTURE_DESCR | — | ✅ |
| 24 | PermitFieldGroupPEODemStructureFloorArea | DEM_STRUCTURE_FLOOR_AREA | — | ✅ |
| 25 | PermitFieldGroupPEODemStructureMeritFlag | DEM_STRUCTURE_MERIT_FLAG | — | ✅ |
| 26 | PermitFieldGroupPEODemUgFlameLiqStorFlag | DEM_UG_FLAME_LIQ_STOR_FLAG | — | ✅ |
| 27 | PermitFieldGroupPEODemWaterFlag | DEM_WATER_FLAG | — | ✅ |
| 28 | PermitFieldGroupPEODemWaterUtilReleaseDate | DEM_WATER_UTIL_RELEASE_DATE | — | ✅ |
| 29 | PermitFieldGroupPEODimensionUom | DIMENSION_UOM | — | ✅ |
| 30 | PermitFieldGroupPEODistanceUom | DISTANCE_UOM | — | ✅ |
| 31 | PermitFieldGroupPEODurationUom | DURATION_UOM | — | ✅ |
| 32 | PermitFieldGroupPEODwlChangeDwellingArea | DWL_CHANGE_DWELLING_AREA | — | ✅ |
| 33 | PermitFieldGroupPEODwlChangeDwellingUnits | DWL_CHANGE_DWELLING_UNITS | — | ✅ |
| 34 | PermitFieldGroupPEODwlConcessionIncentiveFlag | DWL_CONCESSION_INCENTIVE_FLAG | — | ✅ |
| 35 | PermitFieldGroupPEODwlDensityBonusFlag | DWL_DENSITY_BONUS_FLAG | — | ✅ |
| 36 | PermitFieldGroupPEODwlDwellingControlRentFlag | DWL_DWELLING_CONTROL_RENT_FLAG | — | ✅ |
| 37 | PermitFieldGroupPEODwlDwellingUnitAreaUom | DWL_DWELLING_UNIT_AREA_UOM | — | ✅ |
| 38 | PermitFieldGroupPEODwlEliminateDwellingFlag | DWL_ELIMINATE_DWELLING_FLAG | — | ✅ |
| 39 | PermitFieldGroupPEODwlExistingDwellingArea | DWL_EXISTING_DWELLING_AREA | — | ✅ |
| 40 | PermitFieldGroupPEODwlExistingDwellingUnits | DWL_EXISTING_DWELLING_UNITS | — | ✅ |
| 41 | PermitFieldGroupPEODwlProposedDwellingArea | DWL_PROPOSED_DWELLING_AREA | — | ✅ |
| 42 | PermitFieldGroupPEODwlProposedDwellingUnits | DWL_PROPOSED_DWELLING_UNITS | — | ✅ |
| 43 | PermitFieldGroupPEOElcDishwashers | ELC_DISHWASHERS | — | ✅ |
| 44 | PermitFieldGroupPEOElcExistingServiceAmps | ELC_EXISTING_SERVICE_AMPS | — | ✅ |
| 45 | PermitFieldGroupPEOElcExistingServiceFlag | ELC_EXISTING_SERVICE_FLAG | — | ✅ |
| 46 | PermitFieldGroupPEOElcFireAlarms | ELC_FIRE_ALARMS | — | ✅ |
| 47 | PermitFieldGroupPEOElcHeatingAppliances | ELC_HEATING_APPLIANCES | — | ✅ |
| 48 | PermitFieldGroupPEOElcMotors | ELC_MOTORS | — | ✅ |
| 49 | PermitFieldGroupPEOElcNumFixturesOutletsSws | ELC_NUM_FIXTURES_OUTLETS_SWS | — | ✅ |
| 50 | PermitFieldGroupPEOElcNumPowerOutlets | ELC_NUM_POWER_OUTLETS | — | ✅ |
| 51 | PermitFieldGroupPEOElcNumPowerOutletsOther | ELC_NUM_POWER_OUTLETS_OTHER | — | ✅ |
| 52 | PermitFieldGroupPEOElcNumTelecomm | ELC_NUM_TELECOMM | — | ✅ |
| 53 | PermitFieldGroupPEOElcServEquipment | ELC_SERV_EQUIPMENT | — | ✅ |
| 54 | PermitFieldGroupPEOElcSignFlag | ELC_SIGN_FLAG | — | ✅ |
| 55 | PermitFieldGroupPEOElcSmokeDetectors | ELC_SMOKE_DETECTORS | — | ✅ |
| 56 | PermitFieldGroupPEOElcSwimmingPools | ELC_SWIMMING_POOLS | — | ✅ |
| 57 | PermitFieldGroupPEOElcTemporaryPoles | ELC_TEMPORARY_POLES | — | ✅ |
| 58 | PermitFieldGroupPEOElcWaterHeaterKvaHp | ELC_WATER_HEATER_KVA_HP | — | ✅ |
| 59 | PermitFieldGroupPEOFenAutocloseGateFlag | FEN_AUTOCLOSE_GATE_FLAG | — | ✅ |
| 60 | PermitFieldGroupPEOFenCornerLotFlag | FEN_CORNER_LOT_FLAG | — | ✅ |
| 61 | PermitFieldGroupPEOFenFoundationType | FEN_FOUNDATION_TYPE | — | ✅ |
| 62 | PermitFieldGroupPEOFenHeightFront | FEN_HEIGHT_FRONT | — | ✅ |
| 63 | PermitFieldGroupPEOFenHeightLeft | FEN_HEIGHT_LEFT | — | ✅ |
| 64 | PermitFieldGroupPEOFenHeightRear | FEN_HEIGHT_REAR | — | ✅ |
| 65 | PermitFieldGroupPEOFenHeightRight | FEN_HEIGHT_RIGHT | — | ✅ |
| 66 | PermitFieldGroupPEOFenLocation | FEN_LOCATION | — | ✅ |
| 67 | PermitFieldGroupPEOFenLockFlag | FEN_LOCK_FLAG | — | ✅ |
| 68 | PermitFieldGroupPEOFenMaterial | FEN_MATERIAL | — | ✅ |
| 69 | PermitFieldGroupPEOFenMaterialOther | FEN_MATERIAL_OTHER | — | ✅ |
| 70 | PermitFieldGroupPEOFenPoolEnclosureFlag | FEN_POOL_ENCLOSURE_FLAG | — | ✅ |
| 71 | PermitFieldGroupPEOFenType | FEN_TYPE | — | ✅ |
| 72 | PermitFieldGroupPEOFenTypeOfUse | FEN_TYPE_OF_USE | — | ✅ |
| 73 | PermitFieldGroupPEOFenTypeOfWork | FEN_TYPE_OF_WORK | — | ✅ |
| 74 | PermitFieldGroupPEOFenTypeOther | FEN_TYPE_OTHER | — | ✅ |
| 75 | PermitFieldGroupPEOGenAddlNumStories | GEN_ADDL_NUM_STORIES | — | ✅ |
| 76 | PermitFieldGroupPEOGenBackflowDeviceFlag | GEN_BACKFLOW_DEVICE_FLAG | — | ✅ |
| 77 | PermitFieldGroupPEOGenExistBldgHeight | GEN_EXIST_BLDG_HEIGHT | — | ✅ |
| 78 | PermitFieldGroupPEOGenExistFireSprinkFlag | GEN_EXIST_FIRE_SPRINK_FLAG | — | ✅ |
| 79 | PermitFieldGroupPEOGenExistingNumStories | GEN_EXISTING_NUM_STORIES | — | ✅ |
| 80 | PermitFieldGroupPEOGenFireAlarmComments | GEN_FIRE_ALARM_COMMENTS | — | ✅ |
| 81 | PermitFieldGroupPEOGenFireSprinkComments | GEN_FIRE_SPRINK_COMMENTS | — | ✅ |
| 82 | PermitFieldGroupPEOGenFireSprinkProject | GEN_FIRE_SPRINK_PROJECT | — | ✅ |
| 83 | PermitFieldGroupPEOGenFireSprinkType | GEN_FIRE_SPRINK_TYPE | — | ✅ |
| 84 | PermitFieldGroupPEOGenFloorAreaAddl | GEN_FLOOR_AREA_ADDL | — | ✅ |
| 85 | PermitFieldGroupPEOGenFloorAreaExist | GEN_FLOOR_AREA_EXIST | — | ✅ |
| 86 | PermitFieldGroupPEOGenFloorAreaTotal | GEN_FLOOR_AREA_TOTAL | — | ✅ |
| 87 | PermitFieldGroupPEOGenIrrigationMeterSize | GEN_IRRIGATION_METER_SIZE | — | ✅ |
| 88 | PermitFieldGroupPEOGenJobCost | GEN_JOB_COST | — | ✅ |
| 89 | PermitFieldGroupPEOGenNewFloorAreaClass | GEN_NEW_FLOOR_AREA_CLASS | — | ✅ |
| 90 | PermitFieldGroupPEOGenOccupantLoad | GEN_OCCUPANT_LOAD | — | ✅ |
| 91 | PermitFieldGroupPEOGenProposedBldgHeight | GEN_PROPOSED_BLDG_HEIGHT | — | ✅ |
| 92 | PermitFieldGroupPEOGenTotalNumStories | GEN_TOTAL_NUM_STORIES | — | ✅ |
| 93 | PermitFieldGroupPEOGenTypeConstruction | GEN_TYPE_CONSTRUCTION | — | ✅ |
| 94 | PermitFieldGroupPEOGenTypeOfUse | GEN_TYPE_OF_USE | — | ✅ |
| 95 | PermitFieldGroupPEOGenTypeOfWork | GEN_TYPE_OF_WORK | — | ✅ |
| 96 | PermitFieldGroupPEOGenWaterMeterSize | GEN_WATER_METER_SIZE | — | ✅ |
| 97 | PermitFieldGroupPEOGrdCutAmount | GRD_CUT_AMOUNT | — | ✅ |
| 98 | PermitFieldGroupPEOGrdCutDisposeSite | GRD_CUT_DISPOSE_SITE | — | ✅ |
| 99 | PermitFieldGroupPEOGrdCutMaterial | GRD_CUT_MATERIAL | — | ✅ |
| 100 | PermitFieldGroupPEOGrdDisturbedAcreage | GRD_DISTURBED_ACREAGE | — | ✅ |
| 101 | PermitFieldGroupPEOGrdExportAmount | GRD_EXPORT_AMOUNT | — | ✅ |
| 102 | PermitFieldGroupPEOGrdFillAmount | GRD_FILL_AMOUNT | — | ✅ |
| 103 | PermitFieldGroupPEOGrdFillMaterial | GRD_FILL_MATERIAL | — | ✅ |
| 104 | PermitFieldGroupPEOGrdImportAmount | GRD_IMPORT_AMOUNT | — | ✅ |
| 105 | PermitFieldGroupPEOGrdNumLots | GRD_NUM_LOTS | — | ✅ |
| 106 | PermitFieldGroupPEOGrdSourceImport | GRD_SOURCE_IMPORT | — | ✅ |
| 107 | PermitFieldGroupPEOGrdTotalAcreage | GRD_TOTAL_ACREAGE | — | ✅ |
| 108 | PermitFieldGroupPEOGrdTypeProject | GRD_TYPE_PROJECT | — | ✅ |
| 109 | PermitFieldGroupPEOImpExemptHydromodFlag | IMP_EXEMPT_HYDROMOD_FLAG | — | ✅ |
| 110 | PermitFieldGroupPEOImpExemptInfiltrationFlag | IMP_EXEMPT_INFILTRATION_FLAG | — | ✅ |
| 111 | PermitFieldGroupPEOImpExemptRainHarvUseFlag | IMP_EXEMPT_RAIN_HARV_USE_FLAG | — | ✅ |
| 112 | PermitFieldGroupPEOImpExistingImperviousArea | IMP_EXISTING_IMPERVIOUS_AREA | — | ✅ |
| 113 | PermitFieldGroupPEOImpImperviousAreaUom | IMP_IMPERVIOUS_AREA_UOM | — | ✅ |
| 114 | PermitFieldGroupPEOImpLotArea | IMP_LOT_AREA | — | ✅ |
| 115 | PermitFieldGroupPEOImpProposedImperviousArea | IMP_PROPOSED_IMPERVIOUS_AREA | — | ✅ |
| 116 | PermitFieldGroupPEOImpSurficeRatioPercentage | IMP_SURFICE_RATIO_PERCENTAGE | — | ✅ |
| 117 | PermitFieldGroupPEOInsBondedFlag | INS_BONDED_FLAG | — | ✅ |
| 118 | PermitFieldGroupPEOInsInsuranceCompany | INS_INSURANCE_COMPANY | — | ✅ |
| 119 | PermitFieldGroupPEOInsInsuranceType | INS_INSURANCE_TYPE | — | ✅ |
| 120 | PermitFieldGroupPEOInsInsuredFlag | INS_INSURED_FLAG | — | ✅ |
| 121 | PermitFieldGroupPEOInsPolicyExpiration | INS_POLICY_EXPIRATION | — | ✅ |
| 122 | PermitFieldGroupPEOInsPolicyNumber | INS_POLICY_NUMBER | — | ✅ |
| 123 | PermitFieldGroupPEOLandUom | LAND_UOM | — | ✅ |
| 124 | PermitFieldGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 125 | PermitFieldGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 126 | PermitFieldGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 127 | PermitFieldGroupPEOLnpRecordId | LNP_RECORD_ID | — | ✅ |
| 128 | PermitFieldGroupPEOLnpRecordKey | LNP_RECORD_KEY | — | ✅ |
| 129 | PermitFieldGroupPEOMecAirhdlrMax | MEC_AIRHDLR_MAX | — | ✅ |
| 130 | PermitFieldGroupPEOMecAirhdlrMin | MEC_AIRHDLR_MIN | — | ✅ |
| 131 | PermitFieldGroupPEOMecBathKitchenExhaust | MEC_BATH_KITCHEN_EXHAUST | — | ✅ |
| 132 | PermitFieldGroupPEOMecChillers | MEC_CHILLERS | — | ✅ |
| 133 | PermitFieldGroupPEOMecChimneys | MEC_CHIMNEYS | — | ✅ |
| 134 | PermitFieldGroupPEOMecCommercialHoods | MEC_COMMERCIAL_HOODS | — | ✅ |
| 135 | PermitFieldGroupPEOMecCompressors | MEC_COMPRESSORS | — | ✅ |
| 136 | PermitFieldGroupPEOMecCoolingTowers | MEC_COOLING_TOWERS | — | ✅ |
| 137 | PermitFieldGroupPEOMecDuctSystemFlag | MEC_DUCT_SYSTEM_FLAG | — | ✅ |
| 138 | PermitFieldGroupPEOMecElectricHeatEquip | MEC_ELECTRIC_HEAT_EQUIP | — | ✅ |
| 139 | PermitFieldGroupPEOMecEvaporatorCoils | MEC_EVAPORATOR_COILS | — | ✅ |
| 140 | PermitFieldGroupPEOMecFireSuprsPipingFlag | MEC_FIRE_SUPRS_PIPING_FLAG | — | ✅ |
| 141 | PermitFieldGroupPEOMecFireSuprsSprinkler | MEC_FIRE_SUPRS_SPRINKLER | — | ✅ |
| 142 | PermitFieldGroupPEOMecFlueLinerFlag | MEC_FLUE_LINER_FLAG | — | ✅ |
| 143 | PermitFieldGroupPEOMecFlueVentDamperFlag | MEC_FLUE_VENT_DAMPER_FLAG | — | ✅ |
| 144 | PermitFieldGroupPEOMecHeatBtuMax | MEC_HEAT_BTU_MAX | — | ✅ |
| 145 | PermitFieldGroupPEOMecHeatBtuMin | MEC_HEAT_BTU_MIN | — | ✅ |
| 146 | PermitFieldGroupPEOMecHeatPumps | MEC_HEAT_PUMPS | — | ✅ |
| 147 | PermitFieldGroupPEOMecHeatRecovryFlag | MEC_HEAT_RECOVRY_FLAG | — | ✅ |
| 148 | PermitFieldGroupPEOMecHotWaterHeaterTanks | MEC_HOT_WATER_HEATER_TANKS | — | ✅ |
| 149 | PermitFieldGroupPEOMecHumidifiers | MEC_HUMIDIFIERS | — | ✅ |
| 150 | PermitFieldGroupPEOMecNewGasPipingFlag | MEC_NEW_GAS_PIPING_FLAG | — | ✅ |
| 151 | PermitFieldGroupPEOMecPoolHeaters | MEC_POOL_HEATERS | — | ✅ |
| 152 | PermitFieldGroupPEOMecRefrigHpMax | MEC_REFRIG_HP_MAX | — | ✅ |
| 153 | PermitFieldGroupPEOMecRefrigHpMin | MEC_REFRIG_HP_MIN | — | ✅ |
| 154 | PermitFieldGroupPEOMecResidentialBoilerFlag | MEC_RESIDENTIAL_BOILER_FLAG | — | ✅ |
| 155 | PermitFieldGroupPEOMecResidentialHeatFlag | MEC_RESIDENTIAL_HEAT_FLAG | — | ✅ |
| 156 | PermitFieldGroupPEOMecTankAboveGroundFlag | MEC_TANK_ABOVE_GROUND_FLAG | — | ✅ |
| 157 | PermitFieldGroupPEOMecTankBelowGroundFlag | MEC_TANK_BELOW_GROUND_FLAG | — | ✅ |
| 158 | PermitFieldGroupPEOMecUnitHeaters | MEC_UNIT_HEATERS | — | ✅ |
| 159 | PermitFieldGroupPEOMecUnitVentilators | MEC_UNIT_VENTILATORS | — | ✅ |
| 160 | PermitFieldGroupPEOMecVavBoxFlag | MEC_VAV_BOX_FLAG | — | ✅ |
| 161 | PermitFieldGroupPEOMecWaterHeaterFlag | MEC_WATER_HEATER_FLAG | — | ✅ |
| 162 | PermitFieldGroupPEOPermitFieldGroupPEORowParkwayImpactFlag | ROW_PARKWAY_IMPACT_FLAG | — | ✅ |
| 163 | PermitFieldGroupPEOPlbBackflowPreventerFlag | PLB_BACKFLOW_PREVENTER_FLAG | — | ✅ |
| 164 | PermitFieldGroupPEOPlbBldgSewerFlag | PLB_BLDG_SEWER_FLAG | — | ✅ |
| 165 | PermitFieldGroupPEOPlbBldgSewerSize | PLB_BLDG_SEWER_SIZE | — | ✅ |
| 166 | PermitFieldGroupPEOPlbDrainageRepairFlag | PLB_DRAINAGE_REPAIR_FLAG | — | ✅ |
| 167 | PermitFieldGroupPEOPlbFireSprinkerNumHeads | PLB_FIRE_SPRINKER_NUM_HEADS | — | ✅ |
| 168 | PermitFieldGroupPEOPlbFixtureTrapFlag | PLB_FIXTURE_TRAP_FLAG | — | ✅ |
| 169 | PermitFieldGroupPEOPlbGasOutlets | PLB_GAS_OUTLETS | — | ✅ |
| 170 | PermitFieldGroupPEOPlbGasReconnections | PLB_GAS_RECONNECTIONS | — | ✅ |
| 171 | PermitFieldGroupPEOPlbGasTanksPumps | PLB_GAS_TANKS_PUMPS | — | ✅ |
| 172 | PermitFieldGroupPEOPlbLawnSprinklers | PLB_LAWN_SPRINKLERS | — | ✅ |
| 173 | PermitFieldGroupPEOPlbRainwaterDrainFlag | PLB_RAINWATER_DRAIN_FLAG | — | ✅ |
| 174 | PermitFieldGroupPEOPlbSewerTapCommercialFlag | PLB_SEWER_TAP_COMMERCIAL_FLAG | — | ✅ |
| 175 | PermitFieldGroupPEOPlbWaterHeaters | PLB_WATER_HEATERS | — | ✅ |
| 176 | PermitFieldGroupPEOPlbWaterSofteners | PLB_WATER_SOFTENERS | — | ✅ |
| 177 | PermitFieldGroupPEOPlnBuildingAssessedValue | PLN_BUILDING_ASSESSED_VALUE | — | ✅ |
| 178 | PermitFieldGroupPEOPlnChangeNumUnits | PLN_CHANGE_NUM_UNITS | — | ✅ |
| 179 | PermitFieldGroupPEOPlnDevelopmentType | PLN_DEVELOPMENT_TYPE | — | ✅ |
| 180 | PermitFieldGroupPEOPlnExistingCommercialArea | PLN_EXISTING_COMMERCIAL_AREA | — | ✅ |
| 181 | PermitFieldGroupPEOPlnExistingNumUnits | PLN_EXISTING_NUM_UNITS | — | ✅ |
| 182 | PermitFieldGroupPEOPlnExistingTypeOfUse | PLN_EXISTING_TYPE_OF_USE | — | ✅ |
| 183 | PermitFieldGroupPEOPlnGrossLotArea | PLN_GROSS_LOT_AREA | — | ✅ |
| 184 | PermitFieldGroupPEOPlnLandAssessedValue | PLN_LAND_ASSESSED_VALUE | — | ✅ |
| 185 | PermitFieldGroupPEOPlnNetLotArea | PLN_NET_LOT_AREA | — | ✅ |
| 186 | PermitFieldGroupPEOPlnProjectArea | PLN_PROJECT_AREA | — | ✅ |
| 187 | PermitFieldGroupPEOPlnProjectLotAreaUom | PLN_PROJECT_LOT_AREA_UOM | — | ✅ |
| 188 | PermitFieldGroupPEOPlnProposedCommercialArea | PLN_PROPOSED_COMMERCIAL_AREA | — | ✅ |
| 189 | PermitFieldGroupPEOPlnProposedNumUnits | PLN_PROPOSED_NUM_UNITS | — | ✅ |
| 190 | PermitFieldGroupPEOPlnProposedSetbackFront | PLN_PROPOSED_SETBACK_FRONT | — | ✅ |
| 191 | PermitFieldGroupPEOPlnProposedSetbackRear | PLN_PROPOSED_SETBACK_REAR | — | ✅ |
| 192 | PermitFieldGroupPEOPlnProposedSetbackSides | PLN_PROPOSED_SETBACK_SIDES | — | ✅ |
| 193 | PermitFieldGroupPEOPlnProposedTypeOfUse | PLN_PROPOSED_TYPE_OF_USE | — | ✅ |
| 194 | PermitFieldGroupPEOPlnRequiredSetbackFront | PLN_REQUIRED_SETBACK_FRONT | — | ✅ |
| 195 | PermitFieldGroupPEOPlnRequiredSetbackRear | PLN_REQUIRED_SETBACK_REAR | — | ✅ |
| 196 | PermitFieldGroupPEOPlnRequiredSetbackSides | PLN_REQUIRED_SETBACK_SIDES | — | ✅ |
| 197 | PermitFieldGroupPEOPlnSetbackUom | PLN_SETBACK_UOM | — | ✅ |
| 198 | PermitFieldGroupPEOPolAutocloseGateFlag | POL_AUTOCLOSE_GATE_FLAG | — | ✅ |
| 199 | PermitFieldGroupPEOPolFenceHeight | POL_FENCE_HEIGHT | — | ✅ |
| 200 | PermitFieldGroupPEOPolFencedFlag | POL_FENCED_FLAG | — | ✅ |
| 201 | PermitFieldGroupPEOPolFrontSetback | POL_FRONT_SETBACK | — | ✅ |
| 202 | PermitFieldGroupPEOPolHeaterFlag | POL_HEATER_FLAG | — | ✅ |
| 203 | PermitFieldGroupPEOPolHeaterType | POL_HEATER_TYPE | — | ✅ |
| 204 | PermitFieldGroupPEOPolLeftSideSetback | POL_LEFT_SIDE_SETBACK | — | ✅ |
| 205 | PermitFieldGroupPEOPolLocation | POL_LOCATION | — | ✅ |
| 206 | PermitFieldGroupPEOPolMaxDepth | POL_MAX_DEPTH | — | ✅ |
| 207 | PermitFieldGroupPEOPolNumPoolLights | POL_NUM_POOL_LIGHTS | — | ✅ |
| 208 | PermitFieldGroupPEOPolRearSetback | POL_REAR_SETBACK | — | ✅ |
| 209 | PermitFieldGroupPEOPolRightSideSetback | POL_RIGHT_SIDE_SETBACK | — | ✅ |
| 210 | PermitFieldGroupPEOPolSurfaceArea | POL_SURFACE_AREA | — | ✅ |
| 211 | PermitFieldGroupPEOPolTypeFence | POL_TYPE_FENCE | — | ✅ |
| 212 | PermitFieldGroupPEOPolTypeOfPool | POL_TYPE_OF_POOL | — | ✅ |
| 213 | PermitFieldGroupPEOQalLicenseClassCode | QAL_LICENSE_CLASS_CODE | — | ✅ |
| 214 | PermitFieldGroupPEOQalLicenseType | QAL_LICENSE_TYPE | — | ✅ |
| 215 | PermitFieldGroupPEOQalStateLicExpire | QAL_STATE_LIC_EXPIRE | — | ✅ |
| 216 | PermitFieldGroupPEOQalStateLicNumber | QAL_STATE_LIC_NUMBER | — | ✅ |
| 217 | PermitFieldGroupPEORbaAdultOrientedFlag | RBA_ADULT_ORIENTED_FLAG | — | ✅ |
| 218 | PermitFieldGroupPEORbaAlcoholLicenseNum | RBA_ALCOHOL_LICENSE_NUM | — | ✅ |
| 219 | PermitFieldGroupPEORbaAlcoholLicenseType | RBA_ALCOHOL_LICENSE_TYPE | — | ✅ |
| 220 | PermitFieldGroupPEORbaAlcoholServed | RBA_ALCOHOL_SERVED | — | ✅ |
| 221 | PermitFieldGroupPEORbaAquaticFeatures | RBA_AQUATIC_FEATURES | — | ✅ |
| 222 | PermitFieldGroupPEORbaCannabisFlag | RBA_CANNABIS_FLAG | — | ✅ |
| 223 | PermitFieldGroupPEORbaCarnivalGames | RBA_CARNIVAL_GAMES | — | ✅ |
| 224 | PermitFieldGroupPEORbaCarnivalRides | RBA_CARNIVAL_RIDES | — | ✅ |
| 225 | PermitFieldGroupPEORbaCasinoGames | RBA_CASINO_GAMES | — | ✅ |
| 226 | PermitFieldGroupPEORbaFirearmFlag | RBA_FIREARM_FLAG | — | ✅ |
| 227 | PermitFieldGroupPEORbaLiveAnimalsFlag | RBA_LIVE_ANIMALS_FLAG | — | ✅ |
| 228 | PermitFieldGroupPEORbaLiveEntertainmentFlag | RBA_LIVE_ENTERTAINMENT_FLAG | — | ✅ |
| 229 | PermitFieldGroupPEORbaOtherFlag | RBA_OTHER_FLAG | — | ✅ |
| 230 | PermitFieldGroupPEORbaOtherSpecify | RBA_OTHER_SPECIFY | — | ✅ |
| 231 | PermitFieldGroupPEORbaPlayEquipmentFlag | RBA_PLAY_EQUIPMENT_FLAG | — | ✅ |
| 232 | PermitFieldGroupPEORbaPyrotechnicsFlag | RBA_PYROTECHNICS_FLAG | — | ✅ |
| 233 | PermitFieldGroupPEORbaTobaccoFlag | RBA_TOBACCO_FLAG | — | ✅ |
| 234 | PermitFieldGroupPEORofExistRoofType | ROF_EXIST_ROOF_TYPE | — | ✅ |
| 235 | PermitFieldGroupPEORofFireLayers | ROF_FIRE_LAYERS | — | ✅ |
| 236 | PermitFieldGroupPEORofNewRoofType | ROF_NEW_ROOF_TYPE | — | ✅ |
| 237 | PermitFieldGroupPEORofNumExistRoofLayers | ROF_NUM_EXIST_ROOF_LAYERS | — | ✅ |
| 238 | PermitFieldGroupPEORofRemoveAllExistRoofFlag | ROF_REMOVE_ALL_EXIST_ROOF_FLAG | — | ✅ |
| 239 | PermitFieldGroupPEORofRoofNumSquares | ROF_ROOF_NUM_SQUARES | — | ✅ |
| 240 | PermitFieldGroupPEORofSheathingRepairFlag | ROF_SHEATHING_REPAIR_FLAG | — | ✅ |
| 241 | PermitFieldGroupPEORowAlleyImpactFlag | ROW_ALLEY_IMPACT_FLAG | — | ✅ |
| 242 | PermitFieldGroupPEORowClosureType | ROW_CLOSURE_TYPE | — | ✅ |
| 243 | PermitFieldGroupPEORowLocation | ROW_LOCATION | — | ✅ |
| 244 | PermitFieldGroupPEORowNumBusStopsBlocked | ROW_NUM_BUS_STOPS_BLOCKED | — | ✅ |
| 245 | PermitFieldGroupPEORowNumCalendarDays | ROW_NUM_CALENDAR_DAYS | — | ✅ |
| 246 | PermitFieldGroupPEORowNumMetersReserved | ROW_NUM_METERS_RESERVED | — | ✅ |
| 247 | PermitFieldGroupPEORowNumNonpaveExcavations | ROW_NUM_NONPAVE_EXCAVATIONS | — | ✅ |
| 248 | PermitFieldGroupPEORowNumPaveExcavaions | ROW_NUM_PAVE_EXCAVAIONS | — | ✅ |
| 249 | PermitFieldGroupPEORowParkingLaneImpactFlag | ROW_PARKING_LANE_IMPACT_FLAG | — | ✅ |
| 250 | PermitFieldGroupPEORowRightOfWayTypeUse | ROW_RIGHT_OF_WAY_TYPE_USE | — | ✅ |
| 251 | PermitFieldGroupPEORowSidewalkImpactFlag | ROW_SIDEWALK_IMPACT_FLAG | — | ✅ |
| 252 | PermitFieldGroupPEORowTotalProjectAreaLength | ROW_TOTAL_PROJECT_AREA_LENGTH | — | ✅ |
| 253 | PermitFieldGroupPEORowTrafficLaneImpactFlag | ROW_TRAFFIC_LANE_IMPACT_FLAG | — | ✅ |
| 254 | PermitFieldGroupPEORowTrafficPlanProvidedFlag | ROW_TRAFFIC_PLAN_PROVIDED_FLAG | — | ✅ |
| 255 | PermitFieldGroupPEOSgnFaceHeight | SGN_FACE_HEIGHT | — | ✅ |
| 256 | PermitFieldGroupPEOSgnFaceWidth | SGN_FACE_WIDTH | — | ✅ |
| 257 | PermitFieldGroupPEOSgnIlluminationType | SGN_ILLUMINATION_TYPE | — | ✅ |
| 258 | PermitFieldGroupPEOSgnPermanentType | SGN_PERMANENT_TYPE | — | ✅ |
| 259 | PermitFieldGroupPEOSgnTemporaryType | SGN_TEMPORARY_TYPE | — | ✅ |
| 260 | PermitFieldGroupPEOSgnTotalFaceArea | SGN_TOTAL_FACE_AREA | — | ✅ |
| 261 | PermitFieldGroupPEOSgnTotalHeight | SGN_TOTAL_HEIGHT | — | ✅ |
| 262 | PermitFieldGroupPEOSgnUsageType | SGN_USAGE_TYPE | — | ✅ |
| 263 | PermitFieldGroupPEOSolInverterPower | SOL_INVERTER_POWER | — | ✅ |
| 264 | PermitFieldGroupPEOSolInverterType | SOL_INVERTER_TYPE | — | ✅ |
| 265 | PermitFieldGroupPEOSolMeterId | SOL_METER_ID | — | ✅ |
| 266 | PermitFieldGroupPEOSolNumPhotovoltaicModules | SOL_NUM_PHOTOVOLTAIC_MODULES | — | ✅ |
| 267 | PermitFieldGroupPEOSolNumRoofConnects | SOL_NUM_ROOF_CONNECTS | — | ✅ |
| 268 | PermitFieldGroupPEOSolNumberOfInverters | SOL_NUMBER_OF_INVERTERS | — | ✅ |
| 269 | PermitFieldGroupPEOSolRoofConnectType | SOL_ROOF_CONNECT_TYPE | — | ✅ |
| 270 | PermitFieldGroupPEOSolRoofCoverage | SOL_ROOF_COVERAGE | — | ✅ |
| 271 | PermitFieldGroupPEOSolRoofLayers | SOL_ROOF_LAYERS | — | ✅ |
| 272 | PermitFieldGroupPEOSolRoofMaterial | SOL_ROOF_MATERIAL | — | ✅ |
| 273 | PermitFieldGroupPEOSolServiceId | SOL_SERVICE_ID | — | ✅ |
| 274 | PermitFieldGroupPEOSolTotalRoofArea | SOL_TOTAL_ROOF_AREA | — | ✅ |
| 275 | PermitFieldGroupPEOSolTypeOfRoof | SOL_TYPE_OF_ROOF | — | ✅ |
| 276 | PermitFieldGroupPEOSolTypeOfUse | SOL_TYPE_OF_USE | — | ✅ |
| 277 | PermitFieldGroupPEOSpeAlcoholCompFlag | SPE_ALCOHOL_COMP_FLAG | — | ✅ |
| 278 | PermitFieldGroupPEOSpeAlcoholEndTime | SPE_ALCOHOL_END_TIME | — | ✅ |
| 279 | PermitFieldGroupPEOSpeAlcoholStartTime | SPE_ALCOHOL_START_TIME | — | ✅ |
| 280 | PermitFieldGroupPEOSpeBannersDescr | SPE_BANNERS_DESCR | — | ✅ |
| 281 | PermitFieldGroupPEOSpeBeerFlag | SPE_BEER_FLAG | — | ✅ |
| 282 | PermitFieldGroupPEOSpeCookingMethod | SPE_COOKING_METHOD | — | ✅ |
| 283 | PermitFieldGroupPEOSpeCookingReqFlag | SPE_COOKING_REQ_FLAG | — | ✅ |
| 284 | PermitFieldGroupPEOSpeCopyNotificationFlag | SPE_COPY_NOTIFICATION_FLAG | — | ✅ |
| 285 | PermitFieldGroupPEOSpeDiscountFee | SPE_DISCOUNT_FEE | — | ✅ |
| 286 | PermitFieldGroupPEOSpeDismantleDatetime | SPE_DISMANTLE_DATETIME | — | ✅ |
| 287 | PermitFieldGroupPEOSpeDistilledSpiritsFlag | SPE_DISTILLED_SPIRITS_FLAG | — | ✅ |
| 288 | PermitFieldGroupPEOSpeDtlRoadCloseDescr | SPE_DTL_ROAD_CLOSE_DESCR | — | ✅ |
| 289 | PermitFieldGroupPEOSpeDtlRoadCloseFlag | SPE_DTL_ROAD_CLOSE_FLAG | — | ✅ |
| 290 | PermitFieldGroupPEOSpeElecPowerFlag | SPE_ELEC_POWER_FLAG | — | ✅ |
| 291 | PermitFieldGroupPEOSpeEndDatetime | SPE_END_DATETIME | — | ✅ |
| 292 | PermitFieldGroupPEOSpeEstDailyAttendance | SPE_EST_DAILY_ATTENDANCE | — | ✅ |
| 293 | PermitFieldGroupPEOSpeEventDescription | SPE_EVENT_DESCRIPTION | — | ✅ |
| 294 | PermitFieldGroupPEOSpeEventName | SPE_EVENT_NAME | — | ✅ |
| 295 | PermitFieldGroupPEOSpeEventType | SPE_EVENT_TYPE | — | ✅ |
| 296 | PermitFieldGroupPEOSpeFirstAidDescr | SPE_FIRST_AID_DESCR | — | ✅ |
| 297 | PermitFieldGroupPEOSpeFirstAidStations | SPE_FIRST_AID_STATIONS | — | ✅ |
| 298 | PermitFieldGroupPEOSpeFoodFlag | SPE_FOOD_FLAG | — | ✅ |
| 299 | PermitFieldGroupPEOSpeFoodPrepFlag | SPE_FOOD_PREP_FLAG | — | ✅ |
| 300 | PermitFieldGroupPEOSpeFoodVendors | SPE_FOOD_VENDORS | — | ✅ |
| 301 | PermitFieldGroupPEOSpeGarbageCleanupPlan | SPE_GARBAGE_CLEANUP_PLAN | — | ✅ |
| 302 | PermitFieldGroupPEOSpeGeneralAdmission | SPE_GENERAL_ADMISSION | — | ✅ |
| 303 | PermitFieldGroupPEOSpeGenerators | SPE_GENERATORS | — | ✅ |
| 304 | PermitFieldGroupPEOSpeMediaFlag | SPE_MEDIA_FLAG | — | ✅ |
| 305 | PermitFieldGroupPEOSpeMusicalFlag | SPE_MUSICAL_FLAG | — | ✅ |
| 306 | PermitFieldGroupPEOSpeNameOfPublicBldg | SPE_NAME_OF_PUBLIC_BLDG | — | ✅ |
| 307 | PermitFieldGroupPEOSpeNameOfPublicPark | SPE_NAME_OF_PUBLIC_PARK | — | ✅ |
| 308 | PermitFieldGroupPEOSpeNameOfPublicPlz | SPE_NAME_OF_PUBLIC_PLZ | — | ✅ |
| 309 | PermitFieldGroupPEOSpeNotificationMethod | SPE_NOTIFICATION_METHOD | — | ✅ |
| 310 | PermitFieldGroupPEOSpeNotifyFlag | SPE_NOTIFY_FLAG | — | ✅ |
| 311 | PermitFieldGroupPEOSpeNumAdaRestrooms | SPE_NUM_ADA_RESTROOMS | — | ✅ |
| 312 | PermitFieldGroupPEOSpeNumAlcoholVendors | SPE_NUM_ALCOHOL_VENDORS | — | ✅ |
| 313 | PermitFieldGroupPEOSpeNumAmbulances | SPE_NUM_AMBULANCES | — | ✅ |
| 314 | PermitFieldGroupPEOSpeNumBands | SPE_NUM_BANDS | — | ✅ |
| 315 | PermitFieldGroupPEOSpeNumBanners | SPE_NUM_BANNERS | — | ✅ |
| 316 | PermitFieldGroupPEOSpeNumBleachers | SPE_NUM_BLEACHERS | — | ✅ |
| 317 | PermitFieldGroupPEOSpeNumCanopies | SPE_NUM_CANOPIES | — | ✅ |
| 318 | PermitFieldGroupPEOSpeNumChairs | SPE_NUM_CHAIRS | — | ✅ |
| 319 | PermitFieldGroupPEOSpeNumDisableParkSpaces | SPE_NUM_DISABLE_PARK_SPACES | — | ✅ |
| 320 | PermitFieldGroupPEOSpeNumDoctors | SPE_NUM_DOCTORS | — | ✅ |
| 321 | PermitFieldGroupPEOSpeNumDumpsterWLids | SPE_NUM_DUMPSTER_W_LIDS | — | ✅ |
| 322 | PermitFieldGroupPEOSpeNumEmergTechs | SPE_NUM_EMERG_TECHS | — | ✅ |
| 323 | PermitFieldGroupPEOSpeNumFoodVendors | SPE_NUM_FOOD_VENDORS | — | ✅ |
| 324 | PermitFieldGroupPEOSpeNumGarbageContainers | SPE_NUM_GARBAGE_CONTAINERS | — | ✅ |
| 325 | PermitFieldGroupPEOSpeNumHandSinks | SPE_NUM_HAND_SINKS | — | ✅ |
| 326 | PermitFieldGroupPEOSpeNumNurses | SPE_NUM_NURSES | — | ✅ |
| 327 | PermitFieldGroupPEOSpeNumParamedics | SPE_NUM_PARAMEDICS | — | ✅ |
| 328 | PermitFieldGroupPEOSpeNumParkSpaces | SPE_NUM_PARK_SPACES | — | ✅ |
| 329 | PermitFieldGroupPEOSpeNumPortableRestrooms | SPE_NUM_PORTABLE_RESTROOMS | — | ✅ |
| 330 | PermitFieldGroupPEOSpeNumRecycleContainers | SPE_NUM_RECYCLE_CONTAINERS | — | ✅ |
| 331 | PermitFieldGroupPEOSpeNumSecurity | SPE_NUM_SECURITY | — | ✅ |
| 332 | PermitFieldGroupPEOSpeNumShuttles | SPE_NUM_SHUTTLES | — | ✅ |
| 333 | PermitFieldGroupPEOSpeNumStages | SPE_NUM_STAGES | — | ✅ |
| 334 | PermitFieldGroupPEOSpeNumTables | SPE_NUM_TABLES | — | ✅ |
| 335 | PermitFieldGroupPEOSpeNumTents | SPE_NUM_TENTS | — | ✅ |
| 336 | PermitFieldGroupPEOSpeOpenToPublicFlag | SPE_OPEN_TO_PUBLIC_FLAG | — | ✅ |
| 337 | PermitFieldGroupPEOSpeOther | SPE_OTHER | — | ✅ |
| 338 | PermitFieldGroupPEOSpeOutdoorEatingFlag | SPE_OUTDOOR_EATING_FLAG | — | ✅ |
| 339 | PermitFieldGroupPEOSpePaSysEndTime | SPE_PA_SYS_END_TIME | — | ✅ |
| 340 | PermitFieldGroupPEOSpePaSysStartTime | SPE_PA_SYS_START_TIME | — | ✅ |
| 341 | PermitFieldGroupPEOSpeParkPlanVerifiedFlag | SPE_PARK_PLAN_VERIFIED_FLAG | — | ✅ |
| 342 | PermitFieldGroupPEOSpeParkProvidedFlag | SPE_PARK_PROVIDED_FLAG | — | ✅ |
| 343 | PermitFieldGroupPEOSpeParkShuttles | SPE_PARK_SHUTTLES | — | ✅ |
| 344 | PermitFieldGroupPEOSpeParkingPlanDescr | SPE_PARKING_PLAN_DESCR | — | ✅ |
| 345 | PermitFieldGroupPEOSpeProfSecurityFlag | SPE_PROF_SECURITY_FLAG | — | ✅ |
| 346 | PermitFieldGroupPEOSpePubAddrFlag | SPE_PUB_ADDR_FLAG | — | ✅ |
| 347 | PermitFieldGroupPEOSpePublicRowDescr | SPE_PUBLIC_ROW_DESCR | — | ✅ |
| 348 | PermitFieldGroupPEOSpeSecurityCompany | SPE_SECURITY_COMPANY | — | ✅ |
| 349 | PermitFieldGroupPEOSpeSecurityPlan | SPE_SECURITY_PLAN | — | ✅ |
| 350 | PermitFieldGroupPEOSpeSeniorAdmission | SPE_SENIOR_ADMISSION | — | ✅ |
| 351 | PermitFieldGroupPEOSpeSetupDatetime | SPE_SETUP_DATETIME | — | ✅ |
| 352 | PermitFieldGroupPEOSpeSizeCanopies | SPE_SIZE_CANOPIES | — | ✅ |
| 353 | PermitFieldGroupPEOSpeSizeChairs | SPE_SIZE_CHAIRS | — | ✅ |
| 354 | PermitFieldGroupPEOSpeSizeDumpsterWLids | SPE_SIZE_DUMPSTER_W_LIDS | — | ✅ |
| 355 | PermitFieldGroupPEOSpeSizeGarbageContainers | SPE_SIZE_GARBAGE_CONTAINERS | — | ✅ |
| 356 | PermitFieldGroupPEOSpeSizeRecycleContainers | SPE_SIZE_RECYCLE_CONTAINERS | — | ✅ |
| 357 | PermitFieldGroupPEOSpeSoundChkFlag | SPE_SOUND_CHK_FLAG | — | ✅ |
| 358 | PermitFieldGroupPEOSpeSoundEquipDescr | SPE_SOUND_EQUIP_DESCR | — | ✅ |
| 359 | PermitFieldGroupPEOSpeStartDatetime | SPE_START_DATETIME | — | ✅ |
| 360 | PermitFieldGroupPEOSpeStrCloseEndDatetime | SPE_STR_CLOSE_END_DATETIME | — | ✅ |
| 361 | PermitFieldGroupPEOSpeStrCloseStartDatetime | SPE_STR_CLOSE_START_DATETIME | — | ✅ |
| 362 | PermitFieldGroupPEOSpeStreetClosureFlag | SPE_STREET_CLOSURE_FLAG | — | ✅ |
| 363 | PermitFieldGroupPEOSpeTempLightingDescr | SPE_TEMP_LIGHTING_DESCR | — | ✅ |
| 364 | PermitFieldGroupPEOSpeTempLightingFlag | SPE_TEMP_LIGHTING_FLAG | — | ✅ |
| 365 | PermitFieldGroupPEOSpeTempPowerFlag | SPE_TEMP_POWER_FLAG | — | ✅ |
| 366 | PermitFieldGroupPEOSpeTrafficEquipDescr | SPE_TRAFFIC_EQUIP_DESCR | — | ✅ |
| 367 | PermitFieldGroupPEOSpeTrafficEquipFlag | SPE_TRAFFIC_EQUIP_FLAG | — | ✅ |
| 368 | PermitFieldGroupPEOSpeTrafficPlanVerifiedFlag | SPE_TRAFFIC_PLAN_VERIFIED_FLAG | — | ✅ |
| 369 | PermitFieldGroupPEOSpeTrafficRouteReqFlag | SPE_TRAFFIC_ROUTE_REQ_FLAG | — | ✅ |
| 370 | PermitFieldGroupPEOSpeUseOfPublicBldgFlag | SPE_USE_OF_PUBLIC_BLDG_FLAG | — | ✅ |
| 371 | PermitFieldGroupPEOSpeUseOfPublicParkFlag | SPE_USE_OF_PUBLIC_PARK_FLAG | — | ✅ |
| 372 | PermitFieldGroupPEOSpeUseOfPublicPlzFlag | SPE_USE_OF_PUBLIC_PLZ_FLAG | — | ✅ |
| 373 | PermitFieldGroupPEOSpeUsePublicRowFlag | SPE_USE_PUBLIC_ROW_FLAG | — | ✅ |
| 374 | PermitFieldGroupPEOSpeWineFlag | SPE_WINE_FLAG | — | ✅ |
| 375 | PermitFieldGroupPEOSpeYouthAdmission | SPE_YOUTH_ADMISSION | — | ✅ |
| 376 | PermitFieldGroupPEOVolumeUom | VOLUME_UOM | — | ✅ |
| 377 | PermitFieldGroupPEOWeightUom | WEIGHT_UOM | — | ✅ |
| 378 | PermitFieldGroupPEOWhrFuelType | WHR_FUEL_TYPE | — | ✅ |
| 379 | PermitFieldGroupPEOWhrHeaterType | WHR_HEATER_TYPE | — | ✅ |
| 380 | PermitFieldGroupPEOWhrNewHeater | WHR_NEW_HEATER | — | ✅ |
| 381 | PermitFieldGroupPEOWhrNumberNew | WHR_NUMBER_NEW | — | ✅ |
| 382 | PermitFieldGroupPEOWhrNumberReplace | WHR_NUMBER_REPLACE | — | ✅ |
| 383 | PermitFieldGroupPEOWhrTankCapacity | WHR_TANK_CAPACITY | — | ✅ |
| 384 | PermitFieldGroupPEOYrdDescription | YRD_DESCRIPTION | — | ✅ |
| 385 | PermitFieldGroupPEOYrdEndDatetime | YRD_END_DATETIME | — | ✅ |
| 386 | PermitFieldGroupPEOYrdNumDays | YRD_NUM_DAYS | — | ✅ |
| 387 | PermitFieldGroupPEOYrdStartDatetime | YRD_START_DATETIME | — | ✅ |
| 388 | PermitFieldGroupPEOZonBaseFloodElevation | ZON_BASE_FLOOD_ELEVATION | — | ✅ |
| 389 | PermitFieldGroupPEOZonDisturbedAcreage | ZON_DISTURBED_ACREAGE | — | ✅ |
| 390 | PermitFieldGroupPEOZonEnvMgmtAreaFlag | ZON_ENV_MGMT_AREA_FLAG | — | ✅ |
| 391 | PermitFieldGroupPEOZonExistingZoneEast | ZON_EXISTING_ZONE_EAST | — | ✅ |
| 392 | PermitFieldGroupPEOZonExistingZoneNorth | ZON_EXISTING_ZONE_NORTH | — | ✅ |
| 393 | PermitFieldGroupPEOZonExistingZoneSouth | ZON_EXISTING_ZONE_SOUTH | — | ✅ |
| 394 | PermitFieldGroupPEOZonExistingZoneWest | ZON_EXISTING_ZONE_WEST | — | ✅ |
| 395 | PermitFieldGroupPEOZonFloodZone | ZON_FLOOD_ZONE | — | ✅ |
| 396 | PermitFieldGroupPEOZonFloodZoneFlag | ZON_FLOOD_ZONE_FLAG | — | ✅ |
| 397 | PermitFieldGroupPEOZonGrdwaterContaminatFlag | ZON_GRDWATER_CONTAMINAT_FLAG | — | ✅ |
| 398 | PermitFieldGroupPEOZonLandUsePrim | ZON_LAND_USE_PRIM | — | ✅ |
| 399 | PermitFieldGroupPEOZonLandUseSec | ZON_LAND_USE_SEC | — | ✅ |
| 400 | PermitFieldGroupPEOZonLandUseTert | ZON_LAND_USE_TERT | — | ✅ |
| 401 | PermitFieldGroupPEOZonParkingRequiredFlag | ZON_PARKING_REQUIRED_FLAG | — | ✅ |
| 402 | PermitFieldGroupPEOZonParkingSpacesProvided | ZON_PARKING_SPACES_PROVIDED | — | ✅ |
| 403 | PermitFieldGroupPEOZonPlanCaseReqFlag | ZON_PLAN_CASE_REQ_FLAG | — | ✅ |
| 404 | PermitFieldGroupPEOZonProposedZoneEast | ZON_PROPOSED_ZONE_EAST | — | ✅ |
| 405 | PermitFieldGroupPEOZonProposedZoneNorth | ZON_PROPOSED_ZONE_NORTH | — | ✅ |
| 406 | PermitFieldGroupPEOZonProposedZoneSouth | ZON_PROPOSED_ZONE_SOUTH | — | ✅ |
| 407 | PermitFieldGroupPEOZonProposedZoneWest | ZON_PROPOSED_ZONE_WEST | — | ✅ |
| 408 | PermitFieldGroupPEOZonReqPlanCaseType | ZON_REQ_PLAN_CASE_TYPE | — | ✅ |
| 409 | PermitFieldGroupPEOZonTotalAcreage | ZON_TOTAL_ACREAGE | — | ✅ |
| 410 | PermitFieldGroupPEOZonWaiveReduceParkingFlag | ZON_WAIVE_REDUCE_PARKING_FLAG | — | ✅ |
| 411 | PermitFieldGroupPEOZonWithinOpenCreekFlag | ZON_WITHIN_OPEN_CREEK_FLAG | — | ✅ |
| 412 | PermitFieldGroupPEOZonZoningPrim | ZON_ZONING_PRIM | — | ✅ |
| 413 | PermitFieldGroupPEOZonZoningSec | ZON_ZONING_SEC | — | ✅ |
| 414 | PermitFieldGroupPEOZonZoningTert | ZON_ZONING_TERT | — | ✅ |

### [[psc_lnp_record|PSC_LNP_RECORD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitPEOAboutToExpireDate | ABOUT_TO_EXPIRE_DATE | — | — |
| 2 | PermitPEOAddress1 | ADDRESS1 | — | ✅ |
| 3 | PermitPEOAddress2 | ADDRESS2 | — | ✅ |
| 4 | PermitPEOAddress3 | ADDRESS3 | — | — |
| 5 | PermitPEOAddress4 | ADDRESS4 | — | — |
| 6 | PermitPEOAdjustmentFlag | ADJUSTMENT_FLAG | — | — |
| 7 | PermitPEOAgencyId | AGENCY_ID | — | — |
| 8 | PermitPEOAppAcceptDate | APP_ACCEPT_DATE | — | ✅ |
| 9 | PermitPEOApplExpirationDate | APPL_EXPIRATION_DATE | — | — |
| 10 | PermitPEOApplicant | APPLICANT | — | — |
| 11 | PermitPEOApplicantBizProfileId | APPLICANT_BIZ_PROFILE_ID | — | — |
| 12 | PermitPEOApplicantProfileId | APPLICANT_PROFILE_ID | — | — |
| 13 | PermitPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 14 | PermitPEOBusBusinessName | BUS_BUSINESS_NAME | — | — |
| 15 | PermitPEOBusDbaBusinessName | BUS_DBA_BUSINESS_NAME | — | — |
| 16 | PermitPEOBusDescription | BUS_DESCRIPTION | — | — |
| 17 | PermitPEOBusDisadvOwnedFlag | BUS_DISADV_OWNED_FLAG | — | — |
| 18 | PermitPEOBusEstAnnualGross | BUS_EST_ANNUAL_GROSS | — | — |
| 19 | PermitPEOBusExistAnnualGross | BUS_EXIST_ANNUAL_GROSS | — | — |
| 20 | PermitPEOBusFedTaxId | BUS_FED_TAX_ID | — | — |
| 21 | PermitPEOBusFemaleOwnedFlag | BUS_FEMALE_OWNED_FLAG | — | — |
| 22 | PermitPEOBusFloorArea | BUS_FLOOR_AREA | — | — |
| 23 | PermitPEOBusIndustryId | BUS_INDUSTRY_ID | — | — |
| 24 | PermitPEOBusMinorityOwnedFlag | BUS_MINORITY_OWNED_FLAG | — | — |
| 25 | PermitPEOBusNumEmployees | BUS_NUM_EMPLOYEES | — | — |
| 26 | PermitPEOBusOwnershipType | BUS_OWNERSHIP_TYPE | — | — |
| 27 | PermitPEOBusStartDate | BUS_START_DATE | — | — |
| 28 | PermitPEOBusStateTaxId | BUS_STATE_TAX_ID | — | — |
| 29 | PermitPEOCity | CITY | — | ✅ |
| 30 | PermitPEOClassification | CLASSIFICATION | — | — |
| 31 | PermitPEOConflictId | CONFLICT_ID | — | — |
| 32 | PermitPEOCoordinateX | COORDINATE_X | — | — |
| 33 | PermitPEOCoordinateY | COORDINATE_Y | — | — |
| 34 | PermitPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 35 | PermitPEOCountry | COUNTRY | — | ✅ |
| 36 | PermitPEOCounty | COUNTY | — | ✅ |
| 37 | PermitPEOCpdrfLastUpd | CPDRF_LAST_UPD | — | — |
| 38 | PermitPEOCpdrfVerPillar | CPDRF_VER_PILLAR | — | — |
| 39 | PermitPEOCpdrfVerSor | CPDRF_VER_SOR | — | — |
| 40 | PermitPEOCreatedBy | CREATED_BY | — | ✅ |
| 41 | PermitPEOCreationDate | CREATION_DATE | — | ✅ |
| 42 | PermitPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 43 | PermitPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 44 | PermitPEOCurrentTransFlag | CURRENT_TRANS_FLAG | — | — |
| 45 | PermitPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 46 | PermitPEODelinquentDate | DELINQUENT_DATE | — | — |
| 47 | PermitPEODescription | DESCRIPTION | — | — |
| 48 | PermitPEOEmailAddress1 | EMAIL_ADDRESS1 | — | ✅ |
| 49 | PermitPEOEmailAddress2 | EMAIL_ADDRESS2 | — | — |
| 50 | PermitPEOEsignature | ESIGNATURE | — | — |
| 51 | PermitPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 52 | PermitPEOExpirationGraceDate | EXPIRATION_GRACE_DATE | — | — |
| 53 | PermitPEOExpirationStatus | EXPIRATION_STATUS | — | ✅ |
| 54 | PermitPEOFilerId | FILER_ID | — | — |
| 55 | PermitPEOFinalInsCmpDate | FINAL_INS_CMP_DATE | — | — |
| 56 | PermitPEOGender | GENDER | — | — |
| 57 | PermitPEOIsContractor | IS_CONTRACTOR | — | — |
| 58 | PermitPEOIssueDate | ISSUE_DATE | — | — |
| 59 | PermitPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 60 | PermitPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 61 | PermitPEOLastAction | LAST_ACTION | — | — |
| 62 | PermitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | PermitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | PermitPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 65 | PermitPEOLnpRecordId | LNP_RECORD_ID | — | ✅ |
| 66 | PermitPEOLnpRecordKey | LNP_RECORD_KEY | — | ✅ |
| 67 | PermitPEOMigratedDataFlag | MIGRATED_DATA_FLAG | — | — |
| 68 | PermitPEOMobileFlag | MOBILE_FLAG | — | — |
| 69 | PermitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | PermitPEOOrganizationName | ORGANIZATION_NAME | — | — |
| 71 | PermitPEOOriginator | ORIGINATOR | — | — |
| 72 | PermitPEOParentRecordKey | PARENT_RECORD_KEY | — | — |
| 73 | PermitPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 74 | PermitPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 75 | PermitPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 76 | PermitPEOPersonName | PERSON_NAME | — | ✅ |
| 77 | PermitPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 78 | PermitPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 79 | PermitPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 80 | PermitPEOPhoneAreaCode | PHONE_AREA_CODE | — | — |
| 81 | PermitPEOPhoneCountryCode | PHONE_COUNTRY_CODE | — | — |
| 82 | PermitPEOPhoneExtension | PHONE_EXTENSION | — | — |
| 83 | PermitPEOPhoneNumber | PHONE_NUMBER | — | ✅ |
| 84 | PermitPEOPlanReviewCmpDate | PLAN_REVIEW_CMP_DATE | — | — |
| 85 | PermitPEOPostalCode | POSTAL_CODE | — | ✅ |
| 86 | PermitPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 87 | PermitPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 88 | PermitPEOPrimaryRecordId | PRIMARY_RECORD_ID | — | — |
| 89 | PermitPEOPrimaryRecordKey | PRIMARY_RECORD_KEY | — | — |
| 90 | PermitPEOProjectKey | PROJECT_KEY | — | — |
| 91 | PermitPEOProvince | PROVINCE | — | ✅ |
| 92 | PermitPEOReceivedDate | RECEIVED_DATE | — | — |
| 93 | PermitPEORecordName | RECORD_NAME | — | — |
| 94 | PermitPEORecordNumber | RECORD_NUMBER | — | — |
| 95 | PermitPEOReissueDate | REISSUE_DATE | — | — |
| 96 | PermitPEORenewalDate | RENEWAL_DATE | — | — |
| 97 | PermitPEORenewalDueDate | RENEWAL_DUE_DATE | — | — |
| 98 | PermitPEOSrid | SRID | — | — |
| 99 | PermitPEOState | STATE | — | ✅ |
| 100 | PermitPEOStatus | STATUS | — | ✅ |
| 101 | PermitPEOSubapplicationFlag | SUBAPPLICATION_FLAG | — | — |
| 102 | PermitPEOSubmitDate | SUBMIT_DATE | — | — |
| 103 | PermitPEOSubmittedBy | SUBMITTED_BY | — | ✅ |
| 104 | PermitPEOSubmittedByName | SUBMITTED_BY_NAME | — | — |
| 105 | PermitPEOSystemStatus | SYSTEM_STATUS | — | ✅ |
| 106 | PermitPEOTermsUseAcceptDate | TERMS_USE_ACCEPT_DATE | — | — |
| 107 | PermitPEOTermsUseAcceptedBy | TERMS_USE_ACCEPTED_BY | — | — |
| 108 | PermitPEOTermsUseId | TERMS_USE_ID | — | — |
| 109 | PermitPEOTermsUsePersonType | TERMS_USE_PERSON_TYPE | — | — |
| 110 | PermitPEOUserLastUpdateDate | USER_LAST_UPDATE_DATE | — | — |
| 111 | PermitPEOVersionType | VERSION_TYPE | — | ✅ |

### [[psc_lnp_record_status_tl|PSC_LNP_RECORD_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitStatusTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | PermitStatusTLPEOClassification1 | CLASSIFICATION | — | — |
| 3 | PermitStatusTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | PermitStatusTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | PermitStatusTLPEODescription | DESCRIPTION | — | ✅ |
| 6 | PermitStatusTLPEOLanguage | LANGUAGE | — | — |
| 7 | PermitStatusTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | PermitStatusTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PermitStatusTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | PermitStatusTLPEORecordStatus | RECORD_STATUS | — | — |
| 11 | PermitStatusTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_lnp_record_status_vl|PSC_LNP_RECORD_STATUS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PermitStatusPEOAgencyId | AGENCY_ID | — | — |
| 2 | PermitStatusPEOClassification | CLASSIFICATION | — | — |
| 3 | PermitStatusPEOCreatedBy | CREATED_BY | — | — |
| 4 | PermitStatusPEOCreationDate | CREATION_DATE | — | — |
| 5 | PermitStatusPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | PermitStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | PermitStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PermitStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PermitStatusPEOModuleId | MODULE_ID | — | — |
| 10 | PermitStatusPEORecordStatus | RECORD_STATUS | — | — |
| 11 | PermitStatusPEOSystemStatus | SYSTEM_STATUS | — | — |
| 12 | PermitStatusPEOSystemUse | SYSTEM_USE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
