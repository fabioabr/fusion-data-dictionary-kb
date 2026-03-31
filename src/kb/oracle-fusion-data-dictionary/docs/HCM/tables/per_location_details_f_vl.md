---
id: DOC-HCM-677
doc_type: system-doc
title: "PER_LOCATION_DETAILS_F_VL — View de Detalhes de Localização com Tradução"
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
  - location-details-vl
  - view-traduzida
  - multilanguage
aliases:
  - PER_LOCATION_DETAILS_F_VL
  - per_location_details_f_vl
  - view-detalhes-localizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_LOCATION_DETAILS_F_VL

## Visão Geral

**View** que combina os dados da tabela base `PER_LOCATION_DETAILS_F` com as traduções da tabela `PER_LOCATION_DETAILS_F_TL`, apresentando os detalhes de localização já com os campos traduzidos no idioma da sessão do usuário.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **View com Language** — join automático entre a tabela base (_F) e a tabela de tradução (_TL), filtrando pelo idioma da sessão.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consultas simplificadas** — elimina a necessidade de join manual entre base e TL
- **Relatórios localizados** — dados já no idioma do usuário corrente
- **Integrações com BI/Analytics** — fonte preferida para relatórios OTBI e BIP
- **APIs REST** — muitas APIs HCM utilizam views _VL como fonte de dados

---

## Colunas Principais

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
| 6 | LOCATION_DETAILS_NAME | VARCHAR2(360) | NULL | Tradução | Nome traduzido do detalhe de localização | — | 🟡 75% |
| 7 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_locations]] — via `LOCATION_ID` (localização da visão traduzida de detalhes)

### Tabelas-filha (FK de saída)
- Nenhuma — views não possuem FKs diretas.

---

## Uso Típico

### Detalhes traduzidos de uma localização ativa
```sql
SELECT vl.LOCATION_DETAILS_ID, vl.LOCATION_DETAILS_NAME,
       vl.TIMEZONE_CODE, vl.DESCRIPTION
FROM   PER_LOCATION_DETAILS_F_VL vl
WHERE  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE
  AND  vl.LOCATION_ID = :p_location_id;
```

---

## Observações

- Por ser uma view, não aceita DML direto — alterações devem ser feitas via tabelas base.
- O filtro de idioma é aplicado automaticamente com base no `USERENV('LANG')`.
- Preferir esta view em relatórios OTBI para garantir tradução automática.

---

## Referências

- [Oracle Docs — PER_LOCATION_DETAILS_F_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocationdetailsfvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[careerpreferencelocationpvo|CareerPreferenceLocationPVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[careerpreferencelocationpvo_viewall|CareerPreferenceLocationPVO_Viewall]] (HCM · BICC: 2/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation1pvo|ExcludedLocation1PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation1pvo_viewall|ExcludedLocation1PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation2pvo|ExcludedLocation2PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation2pvo_viewall|ExcludedLocation2PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation3pvo|ExcludedLocation3PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation3pvo_viewall|ExcludedLocation3PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation4pvo|ExcludedLocation4PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[excludedlocation4pvo_viewall|ExcludedLocation4PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 5/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocationDetailsMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsMgrPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LocationDetailsMgrPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsMgrPEOLocationDetailsId | ✅ |
| LOCATION_NAME | LocationDetailsMgrPEOLocationName | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocationDetailsMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsMgrPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LocationDetailsMgrPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsMgrPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsMgrPEOLocationName | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 41/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION_UNITS | LocationDetailsPEOAnnualWorkingDurationUnits | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | ✅ |
| business_group_id | LocationDetailsPEOBusinessGroupId | ✅ |
| CREATED_BY | LocationDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | LocationDetailsPEOCreationDate | ✅ |
| DESCRIPTION | LocationDetailsPEODescription | ✅ |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | ✅ |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | ✅ |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | ✅ |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | ✅ |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | ✅ |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | ✅ |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | ✅ |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | ✅ |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | ✅ |
| LOCATION_CODE | LocationDetailsPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_ID | LocationDetailsPEOLocationId | ✅ |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | ✅ |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | ✅ |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | ✅ |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | ✅ |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | ✅ |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | ✅ |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | ✅ |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | ✅ |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | ✅ |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | ✅ |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | ✅ |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | ✅ |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | ✅ |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | ✅ |
| STANDARD_WORKING_FREQUENCY | LocationDetailsPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocationDetailsPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | LocationDetailsPEOStdAnnualWorkingDuration | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | ✅ |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | ✅ |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM · BICC: 4/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| ANNUAL_WORKING_DURATION_UNITS | LocationDetailsPEOAnnualWorkingDurationUnits | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsPEOCreationDate | — |
| DESCRIPTION | LocationDetailsPEODescription | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationDetailsPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| STANDARD_WORKING_FREQUENCY | LocationDetailsPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocationDetailsPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | LocationDetailsPEOStdAnnualWorkingDuration | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsEffectiveStartDate | — |
| LOCATION_DETAILS_ID | LocDetailsLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | ✅ |

### [[locationdetailspvoviewall|LocationDetailsPVOViewAll]] (HCM · BICC: 5/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | AcLocationCode | — |
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| ANNUAL_WORKING_DURATION_UNITS | LocationDetailsPEOAnnualWorkingDurationUnits | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsPEOCreationDate | — |
| DESCRIPTION | Description | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| LOCATION_NAME | LocationName | ✅ |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| STANDARD_WORKING_FREQUENCY | LocationDetailsPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | LocationDetailsPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | LocationDetailsPEOStdAnnualWorkingDuration | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[locationdetailstranslationpvo|LocationDetailsTranslationPVO]] (HCM · BICC: 4/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsPEOCreationDate | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | — |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | ✅ |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | ✅ |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[locationdetailstranslationpvoviewall|LocationDetailsTranslationPVOViewAll]] (HCM · BICC: 2/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsPEOCreationDate | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | — |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[locationrefpvo|LocationRefPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| CREATED_BY | LocationDetailsPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsPEOLastUpdatedBy | — |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | ✅ |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| OBJECT_VERSION_NUMBER | LocationDetailsPEOObjectVersionNumber | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsPEOLocationName | ✅ |

### [[preferredlocation1pvo|PreferredLocation1PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation1pvo_viewall|PreferredLocation1PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation2pvo|PreferredLocation2PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation2pvo_viewall|PreferredLocation2PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation3pvo|PreferredLocation3PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation3pvo_viewall|PreferredLocation3PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation4pvo|PreferredLocation4PVO]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |

### [[preferredlocation4pvo_viewall|PreferredLocation4PVO_Viewall]] (HCM · BICC: 3/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | LocationDetailsPEOActiveStatus | — |
| BILL_TO_SITE_FLAG | LocationDetailsPEOBillToSiteFlag | — |
| business_group_id | LocationDetailsPEOBusinessGroupId | — |
| DESIGNATED_RECEIVER_ID | LocationDetailsPEODesignatedReceiverId | — |
| EFFECTIVE_END_DATE | LocationDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LocationDetailsPEOEffectiveStartDate | ✅ |
| EMAIL_ADDRESS | LocationDetailsPEOEmailAddress | — |
| FAX_AREA_CODE2 | LocationDetailsPEOFaxAreaCode2 | — |
| FAX_COUNTRY_CODE2 | LocationDetailsPEOFaxCountryCode2 | — |
| FAX_EXTENSION2 | LocationDetailsPEOFaxExtension2 | — |
| FAX_SUBSCRIBER_NUM2 | LocationDetailsPEOFaxSubscriberNum2 | — |
| GEO_HIERARCHY_NODE_ID | LocationDetailsPEOGeoHierarchyNodeId | — |
| GEO_HIERARCHY_NODE_VALUE | LocationDetailsPEOGeoHierarchyNodeValue | — |
| INVENTORY_ORGANIZATION_ID | LocationDetailsPEOInventoryOrganizationId | — |
| LAST_UPDATE_DATE | LocationDetailsPEOLastUpdateDate | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsPEOLocationDetailsId | — |
| LOCATION_ID | LocationDetailsPEOLocationId | — |
| MAIN_ADDRESS_ID | LocationDetailsPEOMainAddressId | — |
| MAINPHONE_AREA_CODE1 | LocationDetailsPEOMainphoneAreaCode1 | — |
| MAINPHONE_COUNTRY_CODE1 | LocationDetailsPEOMainphoneCountryCode1 | — |
| MAINPHONE_EXTENSION1 | LocationDetailsPEOMainphoneExtension1 | — |
| MAINPHONE_SUBSCRIBER_NUM1 | LocationDetailsPEOMainphoneSubscriberNum1 | — |
| OFFICE_SITE_FLAG | LocationDetailsPEOOfficeSiteFlag | — |
| OFFICIAL_LANGUAGE_CODE | LocationDetailsPEOOfficialLanguageCode | — |
| OTHERPHONE_AREA_CODE3 | LocationDetailsPEOOtherphoneAreaCode3 | — |
| OTHERPHONE_COUNTRY_CODE3 | LocationDetailsPEOOtherphoneCountryCode3 | — |
| OTHERPHONE_EXTENSION3 | LocationDetailsPEOOtherphoneExtension3 | — |
| OTHERPHONE_SUBSCRIBER_NUM3 | LocationDetailsPEOOtherphoneSubscriberNum3 | — |
| RECEIVING_SITE_FLAG | LocationDetailsPEOReceivingSiteFlag | — |
| SHIP_TO_LOCATION_ID | LocationDetailsPEOShipToLocationId | — |
| SHIP_TO_SITE_FLAG | LocationDetailsPEOShipToSiteFlag | — |
| TELEPHONE_NUMBER_1 | LocationDetailsPEOTelephoneNumber1 | — |
| TELEPHONE_NUMBER_2 | LocationDetailsPEOTelephoneNumber2 | — |
| TELEPHONE_NUMBER_3 | LocationDetailsPEOTelephoneNumber3 | — |
