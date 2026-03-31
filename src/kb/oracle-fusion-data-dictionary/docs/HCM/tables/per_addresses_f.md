---
id: DOC-HCM-618
doc_type: system-doc
title: "PER_ADDRESSES_F — Endereços de Pessoas"
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
  - workforce-management
  - enderecos
  - addresses
aliases:
  - PER_ADDRESSES_F
  - per_addresses_f
  - per-addresses-f
  - endereços-de-pessoas
  - per-addresses-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ADDRESSES_F

## 📌 Visão Geral

Armazena os **endereços** dos colaboradores e contatos, com controle de vigência temporal (date-effective). Suporta múltiplos endereços por pessoa (residencial, comercial, etc.).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de endereços** — armazena endereços residenciais, comerciais e de correspondência.
- **Compliance tributário** — endereço determina jurisdição fiscal para folha de pagamento.
- **Comunicações** — endereço de correspondência para envio de documentos.
- **Benefícios** — elegibilidade a benefícios pode depender da localização.
- **Relatórios demográficos** — análise geográfica da força de trabalho.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDRESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do endereço | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | ADDRESS_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de endereço (HOME, MAIL, etc.) | — | 🟢 90% |
| 6 | ADDRESS_LINE_1 | VARCHAR2(240) | NOT NULL | Endereço | Logradouro (linha 1) | — | 🟢 90% |
| 7 | TOWN_OR_CITY | VARCHAR2(30) | NULL | Endereço | Cidade | — | 🟢 90% |
| 8 | REGION_2 | VARCHAR2(120) | NULL | Endereço | Estado/Província | — | 🟢 85% |
| 9 | POSTAL_CODE | VARCHAR2(30) | NULL | Endereço | CEP/Código postal | — | 🟢 90% |
| 10 | COUNTRY | VARCHAR2(60) | NOT NULL | Endereço | País (código ISO) | — | 🟢 90% |
| 11 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | Endereço primário (Y/N) | — | 🟢 85% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa associada)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Endereço atual de um colaborador
```sql
SELECT pa.ADDRESS_LINE_1, pa.TOWN_OR_CITY, pa.REGION_2,
       pa.POSTAL_CODE, pa.COUNTRY
FROM   PER_ADDRESSES_F pa
WHERE  pa.PERSON_ID = :p_person_id
  AND  pa.ADDRESS_TYPE = 'HOME'
  AND  SYSDATE BETWEEN pa.EFFECTIVE_START_DATE AND pa.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ADDRESS_TYPE = 'HOME'` — Endereço residencial
- `PRIMARY_FLAG = 'Y'` — Endereço principal
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência para obter o endereço corrente.
- Um colaborador pode ter múltiplos endereços simultâneos (residencial, correspondência, etc.).
- O campo `COUNTRY` usa código ISO — fundamental para regras tributárias.
- Dados sensíveis — sujeitos a regras de privacidade (LGPD/GDPR).
---

## 🔗 PVOs Relacionados

### [[addressespvo|AddressesPVO]] (HCM · BICC: 31/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_ADDRESS_ATTRIBUTE1 | AddressesPEOAddlAddressAttribute1 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE2 | AddressesPEOAddlAddressAttribute2 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE3 | AddressesPEOAddlAddressAttribute3 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE4 | AddressesPEOAddlAddressAttribute4 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE5 | AddressesPEOAddlAddressAttribute5 | ✅ |
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | ✅ |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| DERIVED_LOCALE | AddressesPEODerivedLocale | ✅ |
| DQ_VALIDATION_LEVEL | AddressesPEODqValidationLevel | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | ✅ |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_ADDRESS_ATTRIBUTE1 | AddressAddlAddressAttribute1 | — |
| ADDL_ADDRESS_ATTRIBUTE2 | AddressAddlAddressAttribute2 | — |
| ADDL_ADDRESS_ATTRIBUTE3 | AddressAddlAddressAttribute3 | — |
| ADDL_ADDRESS_ATTRIBUTE4 | AddressAddlAddressAttribute4 | — |
| ADDL_ADDRESS_ATTRIBUTE5 | AddressAddlAddressAttribute5 | — |
| ADDR_ATTRIBUTE1 | AddressAddrAttribute1 | — |
| ADDR_ATTRIBUTE10 | AddressAddrAttribute10 | — |
| ADDR_ATTRIBUTE11 | AddressAddrAttribute11 | — |
| ADDR_ATTRIBUTE12 | AddressAddrAttribute12 | — |
| ADDR_ATTRIBUTE13 | AddressAddrAttribute13 | — |
| ADDR_ATTRIBUTE14 | AddressAddrAttribute14 | — |
| ADDR_ATTRIBUTE15 | AddressAddrAttribute15 | — |
| ADDR_ATTRIBUTE16 | AddressAddrAttribute16 | — |
| ADDR_ATTRIBUTE17 | AddressAddrAttribute17 | — |
| ADDR_ATTRIBUTE18 | AddressAddrAttribute18 | — |
| ADDR_ATTRIBUTE19 | AddressAddrAttribute19 | — |
| ADDR_ATTRIBUTE2 | AddressAddrAttribute2 | — |
| ADDR_ATTRIBUTE20 | AddressAddrAttribute20 | — |
| ADDR_ATTRIBUTE21 | AddressAddrAttribute21 | — |
| ADDR_ATTRIBUTE22 | AddressAddrAttribute22 | — |
| ADDR_ATTRIBUTE23 | AddressAddrAttribute23 | — |
| ADDR_ATTRIBUTE24 | AddressAddrAttribute24 | — |
| ADDR_ATTRIBUTE25 | AddressAddrAttribute25 | — |
| ADDR_ATTRIBUTE26 | AddressAddrAttribute26 | — |
| ADDR_ATTRIBUTE27 | AddressAddrAttribute27 | — |
| ADDR_ATTRIBUTE28 | AddressAddrAttribute28 | — |
| ADDR_ATTRIBUTE29 | AddressAddrAttribute29 | — |
| ADDR_ATTRIBUTE3 | AddressAddrAttribute3 | — |
| ADDR_ATTRIBUTE30 | AddressAddrAttribute30 | — |
| ADDR_ATTRIBUTE4 | AddressAddrAttribute4 | — |
| ADDR_ATTRIBUTE5 | AddressAddrAttribute5 | — |
| ADDR_ATTRIBUTE6 | AddressAddrAttribute6 | — |
| ADDR_ATTRIBUTE7 | AddressAddrAttribute7 | — |
| ADDR_ATTRIBUTE8 | AddressAddrAttribute8 | — |
| ADDR_ATTRIBUTE9 | AddressAddrAttribute9 | — |
| ADDR_ATTRIBUTE_CATEGORY | AddressAddrAttributeCategory | — |
| ADDRESS_ID | AddressAddressId | — |
| BUILDING | AddressBuilding | — |
| BUSINESS_GROUP_ID | AddressBusinessGroupId | — |
| CREATED_BY | AddressCreatedBy | — |
| CREATION_DATE | AddressCreationDate | — |
| DERIVED_LOCALE | AddressDerivedLocale | — |
| DQ_VALIDATION_LEVEL | AddressDqValidationLevel | — |
| EFFECTIVE_END_DATE | AddressEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressFloorNumber | — |
| LAST_UPDATE_DATE | AddressLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressLongPostalCode | — |
| OBJECT_VERSION_NUMBER | AddressObjectVersionNumber | — |
| REGION_1 | AddressRegion1 | — |
| REGION_2 | AddressRegion2 | — |
| REGION_3 | AddressRegion3 | — |
| TIMEZONE_CODE | AddressTimezoneCode | — |

### [[candidateaddressespvo|CandidateAddressesPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_LINE_1 | AddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressLine2 | ✅ |
| COUNTRY | Country | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| POSTAL_CODE | PostalCode | ✅ |
| REGION_1 | Region1 | ✅ |
| REGION_2 | Region2 | ✅ |
| REGION_3 | Region3 | ✅ |
| TOWN_OR_CITY | TownOrCity | ✅ |

### [[contactpersonaddresspvo|ContactPersonAddressPVO]] (HCM · BICC: 22/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 24/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | ✅ |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | ✅ |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 16/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | — |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | — |
| CREATION_DATE | AddressesPEOCreationDate | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | — |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | — |
| CREATION_DATE | AddressesPEOCreationDate | — |
| DERIVED_LOCALE | AddressesPEODerivedLocale | — |
| DQ_VALIDATION_LEVEL | AddressesPEODqValidationLevel | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | — |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | — |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | — |
| CREATION_DATE | AddressesPEOCreationDate | — |
| DERIVED_LOCALE | AddressesPEODerivedLocale | — |
| DQ_VALIDATION_LEVEL | AddressesPEODqValidationLevel | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | — |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 26/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | ✅ |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| DERIVED_LOCALE | AddressesPEODerivedLocale | ✅ |
| DQ_VALIDATION_LEVEL | AddressesPEODqValidationLevel | ✅ |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | ✅ |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM · BICC: 5/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | — |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | — |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | — |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | — |
| BUILDING | AddressesPEOBuilding | — |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | — |
| CREATED_BY | AddressesPEOCreatedBy | — |
| CREATION_DATE | AddressesPEOCreationDate | — |
| DERIVED_LOCALE | AddressesPEODerivedLocale | — |
| DQ_VALIDATION_LEVEL | AddressesPEODqValidationLevel | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | — |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | — |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | — |
| REGION_2 | AddressesPEORegion2 | — |
| REGION_3 | AddressesPEORegion3 | — |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | — |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[locationrefpvo|LocationRefPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | — |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | — |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | — |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | — |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | — |
| BUILDING | AddressesPEOBuilding | — |
| COUNTRY | AddressesPEOCountry | — |
| CREATED_BY | AddressesPEOCreatedBy | — |
| CREATION_DATE | AddressesPEOCreationDate | — |
| DERIVED_LOCALE | AddressesPEODerivedLocale | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | — |
| FLOOR_NUMBER | AddressesPEOFloorNumber | — |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | — |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | — |
| REGION_1 | AddressesPEORegion1 | — |
| REGION_2 | AddressesPEORegion2 | — |
| REGION_3 | AddressesPEORegion3 | — |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | — |
| TOWN_OR_CITY | AddressesPEOTownOrCity | — |

### [[personaddresspvo|PersonAddressPVO]] (HCM · BICC: 27/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_ADDRESS_ATTRIBUTE1 | AddressesPEOAddlAddressAttribute1 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE2 | AddressesPEOAddlAddressAttribute2 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE3 | AddressesPEOAddlAddressAttribute3 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE4 | AddressesPEOAddlAddressAttribute4 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE5 | AddressesPEOAddlAddressAttribute5 | ✅ |
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | — |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[personaddresspvoviewall|PersonAddressPVOViewAll]] (HCM · BICC: 28/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_ADDRESS_ATTRIBUTE1 | AddressesPEOAddlAddressAttribute1 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE2 | AddressesPEOAddlAddressAttribute2 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE3 | AddressesPEOAddlAddressAttribute3 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE4 | AddressesPEOAddlAddressAttribute4 | ✅ |
| ADDL_ADDRESS_ATTRIBUTE5 | AddressesPEOAddlAddressAttribute5 | ✅ |
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | ✅ |
| BUILDING | AddressesPEOBuilding | ✅ |
| BUSINESS_GROUP_ID | AddressesPEOBusinessGroupId | ✅ |
| COUNTRY | AddressesPEOCountry | ✅ |
| CREATED_BY | AddressesPEOCreatedBy | ✅ |
| CREATION_DATE | AddressesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FLOOR_NUMBER | AddressesPEOFloorNumber | ✅ |
| GEOMETRY | AddressesPEOGeometry | — |
| LAST_UPDATE_DATE | AddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AddressesPEOLastUpdatedBy | ✅ |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | ✅ |
| OBJECT_VERSION_NUMBER | AddressesPEOObjectVersionNumber | — |
| POSTAL_CODE | AddressesPEOPostalCode | ✅ |
| REGION_1 | AddressesPEORegion1 | ✅ |
| REGION_2 | AddressesPEORegion2 | ✅ |
| REGION_3 | AddressesPEORegion3 | ✅ |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | ✅ |
| TOWN_OR_CITY | AddressesPEOTownOrCity | ✅ |

### [[personrefpvo|PersonRefPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressesPEOAddressId | — |
| ADDRESS_LINE_1 | AddressesPEOAddressLine1 | — |
| ADDRESS_LINE_2 | AddressesPEOAddressLine2 | — |
| ADDRESS_LINE_3 | AddressesPEOAddressLine3 | — |
| ADDRESS_LINE_4 | AddressesPEOAddressLine4 | — |
| BUILDING | AddressesPEOBuilding | — |
| COUNTRY | AddressesPEOCountry | — |
| EFFECTIVE_END_DATE | AddressesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddressesPEOEffectiveStartDate | — |
| FLOOR_NUMBER | AddressesPEOFloorNumber | — |
| LONG_POSTAL_CODE | AddressesPEOLongPostalCode | — |
| POSTAL_CODE | AddressesPEOPostalCode | — |
| REGION_1 | AddressesPEORegion1 | — |
| REGION_2 | AddressesPEORegion2 | — |
| REGION_3 | AddressesPEORegion3 | — |
| TIMEZONE_CODE | AddressesPEOTimezoneCode | — |
| TOWN_OR_CITY | AddressesPEOTownOrCity | — |

---

## 📚 Referências

- [Oracle Docs — PER_ADDRESSES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peraddressesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
