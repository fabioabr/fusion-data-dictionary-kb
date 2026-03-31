---
id: DOC-HCM-676
doc_type: system-doc
title: "PER_LOCATION_DETAILS_F — Detalhes de Localização"
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
  - per-locations
  - location-details
  - detalhes-localizacao
  - timezone
  - jurisdicao
  - localizacao-hcm
aliases:
  - PER_LOCATION_DETAILS_F
  - per_location_details_f
  - detalhes-localizacao
  - location-details-hcm
  - per-loc-details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_LOCATION_DETAILS_F

## 📌 Visão Geral

Armazena os **detalhes de localização** organizacional com vigência temporal. Cada registro contém informações complementares de um local (endereço, fuso horário, jurisdição), vinculado à tabela principal de localizações.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de localidades corporativas**
- **Configuração de locais para atribuição de colaboradores**
- **Cálculos tributários e jurisdicionais por localidade**
- **Relatórios de distribuição geográfica da força de trabalho**
- **Auditoria de alterações em dados de localização**

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOCATION_DETAILS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe de localização | — | 🟢 95% |
| 2 | LOCATION_ID | NUMBER(18) | NOT NULL | FK | Referência à localização principal | PER_LOCATIONS | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 5 | TIMEZONE_CODE | VARCHAR2(50) | NULL | Configuração | Código do fuso horário da localização | — | 🟡 75% |
| 6 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega associado | PER_LOCATIONS | 🟡 70% |
| 7 | DESIGNATED_RECEIVER_ID | NUMBER(18) | NULL | FK | Pessoa responsável por recebimentos | — | 🟡 65% |
| 8 | INVENTORY_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização de inventário vinculada | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_locations]] — via `LOCATION_ID` (localização dos detalhes adicionais)

### Tabelas-filha (FK de saída)
- [[per_location_details_f_tl]] — via `LOCATION_DETAILS_ID` (traduções dos detalhes da localização)

---

## 📎 Uso Típico

### Detalhes ativos de uma localização
```sql
SELECT ld.LOCATION_DETAILS_ID, ld.LOCATION_ID, ld.TIMEZONE_CODE
FROM   PER_LOCATION_DETAILS_F ld
WHERE  SYSDATE BETWEEN ld.EFFECTIVE_START_DATE AND ld.EFFECTIVE_END_DATE
  AND  ld.LOCATION_ID = :p_location_id;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- O campo TIMEZONE_CODE é essencial para cálculos de horário de trabalho.
- Alterações são rastreadas via OBJECT_VERSION_NUMBER.

---

## 🔗 PVOs Relacionados

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocBasePEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocBasePEOEffectiveStartDate | — |
| LOCATION_DETAILS_ID | LocBasePEOLocationDetailsId | — |
| STANDARD_WORKING_FREQUENCY | LocBasePEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocBasePEOStandardWorkingHours | — |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocBasePEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocBasePEOEffectiveStartDate | — |
| LOCATION_DETAILS_ID | LocBasePEOLocationDetailsId | — |
| STANDARD_WORKING_FREQUENCY | LocBasePEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocBasePEOStandardWorkingHours | — |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocationDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDPEOEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsBasePEOLocationDetailsId | — |
| LOCATION_ID | LocationDPEOLocationId | — |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 20/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION_UNITS | LocationDetailsPEOAnnualWorkingDurationUnits | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | ✅ |
| BUSINESS_GROUP_ID | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | LocationDetailsPEOCreationDate | ✅ |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | ✅ |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | ✅ |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | ✅ |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | ✅ |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | ✅ |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | ✅ |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | ✅ |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | ✅ |
| STANDARD_WORKING_FREQUENCY | LocationDetailsPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocationDetailsPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | LocationDetailsPEOStdAnnualWorkingDuration | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | ✅ |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | ✅ |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 22/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION_UNITS | LocationDetailsPEOAnnualWorkingDurationUnits | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | ✅ |
| BUSINESS_GROUP_ID | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | LocationDetailsPEOCreationDate | ✅ |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | ✅ |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | ✅ |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | ✅ |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | ✅ |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | ✅ |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | ✅ |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | ✅ |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | ✅ |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | ✅ |
| STANDARD_WORKING_FREQUENCY | LocationDetailsPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocationDetailsPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | LocationDetailsPEOStdAnnualWorkingDuration | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | ✅ |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | ✅ |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | ✅ |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | ✅ |
| LOCATION_ID | LocDetailsLocationId | ✅ |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_ID | LocDetailsLocationId | — |

---

## 📚 Referências

- [Oracle Docs — PER_LOCATION_DETAILS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocationdetailsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
