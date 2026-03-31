---
id: DOC-HCM-273
doc_type: system-doc
title: "HR_ALL_ORGANIZATION_UNITS_F — Unidades Organizacionais"
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
  - organization
  - estrutura
  - core-hr
aliases:
  - HR_ALL_ORGANIZATION_UNITS_F
  - hr_all_organization_units_f
  - hr-all-organization-units-f
  - all-organization-units
  - unidades-organizacionais
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ALL_ORGANIZATION_UNITS_F

## 📌 Visao Geral

Tabela principal que armazena todas as **unidades organizacionais** (departments, business units, legal entities, etc.) com versionamento date-effective. E uma das tabelas mais referenciadas do HCM.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Estrutura organizacional:** Registrar todos os tipos de organizacao.
- **Hierarquia:** Base para construcao de arvores organizacionais.
- **Multi-org:** Filtro por ORG_ID em tabelas transacionais.
- **Relatorios:** Base para todos os relatorios organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da organizacao | — | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao (date-effective) | — | 🟢 100% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 100% |
| 4 | ORGANIZATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de organizacao (DEPARTMENT, BU, LE) | — | 🟢 95% |
| 5 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negocios pai | — | 🟢 90% |
| 6 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao principal | — | 🟢 90% |
| 7 | STATUS | VARCHAR2(30) | NOT NULL | Classificacao | Status (A = Ativo, I = Inativo) | — | 🟢 95% |
| 8 | INTERNAL_EXTERNAL_FLAG | VARCHAR2(1) | NULL | Classificacao | Interna (I) ou Externa (E) | — | 🟢 90% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hr_organization_units_f_tl]] — via `ORGANIZATION_ID` (traducoes multilingue do registro)
- [[hr_org_unit_classifications_f]] — via `ORGANIZATION_ID` (classificacoes da unidade organizacional)
- [[hr_organization_information_f]] — via `ORGANIZATION_ID` (informacoes adicionais da organizacao)

---

## 📎 Uso Tipico

### Departamentos ativos
```sql
SELECT o.ORGANIZATION_ID, o.ORGANIZATION_TYPE, o.STATUS
FROM   HR_ALL_ORGANIZATION_UNITS_F o
WHERE  o.STATUS = 'A'
  AND  SYSDATE BETWEEN o.EFFECTIVE_START_DATE AND o.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica tabela date-effective (versionada por data).
- PK composta: (ORGANIZATION_ID, EFFECTIVE_START_DATE).
- Uma das tabelas mais referenciadas — usada como ORG_ID em quase todas as tabelas transacionais.

---

## 📚 Referencias

- [Oracle Docs — HR_ALL_ORGANIZATION_UNITS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrallorganizationunitsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationCreatedBy | — |
| CREATION_DATE | OrganizationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| LOCATION_ID | OrganizationLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |
| TYPE | OrganizationType | — |

### [[businessunitpvo|BusinessUnitPVO]] (HCM · BICC: 7/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[cashadvanceapplicationpvo|CashAdvanceApplicationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[cashadvancepvo|CashAdvancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[contactpersondisabilitypvo|ContactPersonDisabilityPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |

### [[corporatecardtransactionpvo|CorporateCardTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[departmentpvo|DepartmentPVO]] (HCM · BICC: 17/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | ✅ |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | ✅ |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[departmentpvoviewall|DepartmentPVOViewAll]] (HCM · BICC: 17/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | ✅ |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | ✅ |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[enterprisepvo|EnterprisePVO]] (HCM · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationCreatedBy | — |
| CREATION_DATE | OrganizationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| ESTABLISHMENT_ID | OrganizationEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationLastUpdateDate | — |
| LAST_UPDATE_LOGIN | OrganizationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| LOCATION_ID | OrganizationLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |
| TYPE | OrganizationType | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[expensepvo|ExpensePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationEffectiveStartDate | — |
| LEGAL_ENTITY_ID | OrganizationLegalEntityId | — |
| ORGANIZATION_ID | OrganizationOrganizationId | — |

### [[fundingpositionpvo|FundingPositionPVO]] (PO · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | BusinessUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | BusinessUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | BusinessUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | BusinessUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | BusinessUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | BusinessUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitPEOOrganizationId | — |
| TYPE | BusinessUnitPEOType | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 22/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | ✅ |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | ✅ |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationUnitMgrPEOOrganizationId | ✅ |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 5/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitMgrPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitMgrPEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | BusinessUnitPEODateTo | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEO1EffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEODateFrom | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEO1EffectiveStartDate | — |
| LOCATION_ID | LocationId | — |
| ORGANIZATION_ID | BusinessUnitId | — |
| ORGANIZATION_ID | FinancialsBusinessUnitPEOBusinessUnitId1 | — |

### [[inventoryitem|InventoryItem]] (OTHER · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |
| TYPE | OrganizationUnitPEOType | — |

### [[inventoryitemref|InventoryItemRef]] (OTHER · BICC: 3/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOType | — |

### [[inventorylocatorpvo|InventoryLocatorPVO]] (OTHER · BICC: 6/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvHrAttributesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InvHrAttributesPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | InvHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvHrAttributesPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | InvHrAttributesPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | InvHrAttributesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvHrAttributesPEOOrganizationId | — |
| TYPE | InvHrAttributesPEOType | ✅ |

### [[inventorylocatorrefpvo|InventoryLocatorRefPVO]] (OTHER · BICC: 6/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvHrAttributesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InvHrAttributesPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | InvHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvHrAttributesPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | InvHrAttributesPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | InvHrAttributesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvHrAttributesPEOOrganizationId | — |
| TYPE | InvHrAttributesPEOType | ✅ |

### [[inventoryorgparameterscyclecountvcpvo|InventoryOrgParametersCycleCountVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvOrgHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvOrgHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvOrgHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvOrgHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvOrgHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvOrgHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvOrgHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvOrgHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvOrgHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvOrgHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvOrgHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvOrgHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvOrgHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvOrgHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvOrgHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvOrgHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvOrgHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvOrgHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvOrgHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvOrgHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvOrgHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvOrgHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvOrgHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvOrgHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvOrgHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvOrgHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvOrgHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvOrgHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvOrgHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvOrgHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvOrgHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvOrgHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvOrgHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvOrgHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvOrgHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvOrgHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvOrgHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvOrgHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvOrgHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvOrgHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgHrAttributesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvOrgHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvOrgHrAttributesPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | InvOrgHrAttributesPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | InvOrgHrAttributesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvOrgHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvOrgHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvOrgHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgHrAttributesPEOOrganizationId | — |
| TYPE | InvOrgHrAttributesPEOType | — |

### [[inventoryorgparametersinvtransvcpvo|InventoryOrgParametersInvTransVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvOrgHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvOrgHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvOrgHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvOrgHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvOrgHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvOrgHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvOrgHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvOrgHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvOrgHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvOrgHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvOrgHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvOrgHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvOrgHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvOrgHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvOrgHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvOrgHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvOrgHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvOrgHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvOrgHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvOrgHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvOrgHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvOrgHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvOrgHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvOrgHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvOrgHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvOrgHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvOrgHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvOrgHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvOrgHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvOrgHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvOrgHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvOrgHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvOrgHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvOrgHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvOrgHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvOrgHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvOrgHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvOrgHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvOrgHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvOrgHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgHrAttributesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvOrgHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvOrgHrAttributesPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | InvOrgHrAttributesPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | InvOrgHrAttributesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvOrgHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvOrgHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvOrgHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgHrAttributesPEOOrganizationId | — |
| TYPE | InvOrgHrAttributesPEOType | — |

### [[inventoryorgparametersonhandqtyvcpvo|InventoryOrgParametersOnhandQtyVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvOrgHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvOrgHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvOrgHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvOrgHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvOrgHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvOrgHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvOrgHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvOrgHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvOrgHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvOrgHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvOrgHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvOrgHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvOrgHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvOrgHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvOrgHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvOrgHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvOrgHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvOrgHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvOrgHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvOrgHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvOrgHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvOrgHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvOrgHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvOrgHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvOrgHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvOrgHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvOrgHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvOrgHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvOrgHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvOrgHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvOrgHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvOrgHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvOrgHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvOrgHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvOrgHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvOrgHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvOrgHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvOrgHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvOrgHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvOrgHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgHrAttributesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvOrgHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvOrgHrAttributesPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | InvOrgHrAttributesPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | InvOrgHrAttributesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvOrgHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvOrgHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvOrgHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgHrAttributesPEOOrganizationId | — |
| TYPE | InvOrgHrAttributesPEOType | — |

### [[inventoryorgparametersrcvreceiptdatavcpvo|InventoryOrgParametersRcvReceiptDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvOrgHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvOrgHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvOrgHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvOrgHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvOrgHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvOrgHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvOrgHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvOrgHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvOrgHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvOrgHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvOrgHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvOrgHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvOrgHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvOrgHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvOrgHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvOrgHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvOrgHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvOrgHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvOrgHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvOrgHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvOrgHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvOrgHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvOrgHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvOrgHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvOrgHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvOrgHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvOrgHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvOrgHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvOrgHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvOrgHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvOrgHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvOrgHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvOrgHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvOrgHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvOrgHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvOrgHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvOrgHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvOrgHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvOrgHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvOrgHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgHrAttributesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvOrgHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvOrgHrAttributesPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | InvOrgHrAttributesPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | InvOrgHrAttributesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvOrgHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvOrgHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvOrgHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgHrAttributesPEOOrganizationId | — |
| TYPE | InvOrgHrAttributesPEOType | — |

### [[inventoryorgparametersrefpvo|InventoryOrgParametersRefPVO]] (OTHER · BICC: 5/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvHrAttributesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InvHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvHrAttributesPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | InvHrAttributesPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | InvHrAttributesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvHrAttributesPEOOrganizationId | — |
| TYPE | InvHrAttributesPEOType | ✅ |

### [[inventoryorgparametersshipmentdatavcpvo|InventoryOrgParametersShipmentDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvOrgHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvOrgHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvOrgHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvOrgHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvOrgHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvOrgHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvOrgHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvOrgHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvOrgHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvOrgHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvOrgHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvOrgHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvOrgHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvOrgHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvOrgHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvOrgHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvOrgHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvOrgHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvOrgHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvOrgHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvOrgHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvOrgHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvOrgHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvOrgHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvOrgHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvOrgHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvOrgHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvOrgHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvOrgHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvOrgHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvOrgHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvOrgHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvOrgHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvOrgHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvOrgHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvOrgHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvOrgHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvOrgHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvOrgHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvOrgHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgHrAttributesPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgHrAttributesPEOEffectiveStartDate | — |
| ESTABLISHMENT_ID | InvOrgHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvOrgHrAttributesPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | InvOrgHrAttributesPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | InvOrgHrAttributesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvOrgHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvOrgHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvOrgHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgHrAttributesPEOOrganizationId | — |
| TYPE | InvOrgHrAttributesPEOType | — |

### [[inventorysubinventorypvo|InventorySubinventoryPVO]] (OTHER · BICC: 6/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvHrAttributesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InvHrAttributesPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | InvHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvHrAttributesPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | InvHrAttributesPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | InvHrAttributesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvHrAttributesPEOOrganizationId | — |
| TYPE | InvHrAttributesPEOType | ✅ |

### [[inventorysubinventoryrefpvo|InventorySubinventoryRefPVO]] (OTHER · BICC: 6/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | InvHrAttributesPEOActionOccurrenceId | — |
| ATTRIBUTE_DATE1 | InvHrAttributesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | InvHrAttributesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | InvHrAttributesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | InvHrAttributesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | InvHrAttributesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | InvHrAttributesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | InvHrAttributesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | InvHrAttributesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | InvHrAttributesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | InvHrAttributesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | InvHrAttributesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | InvHrAttributesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | InvHrAttributesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | InvHrAttributesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | InvHrAttributesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | InvHrAttributesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | InvHrAttributesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | InvHrAttributesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | InvHrAttributesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | InvHrAttributesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | InvHrAttributesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | InvHrAttributesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | InvHrAttributesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | InvHrAttributesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | InvHrAttributesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | InvHrAttributesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | InvHrAttributesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | InvHrAttributesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | InvHrAttributesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | InvHrAttributesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | InvHrAttributesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | InvHrAttributesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | InvHrAttributesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | InvHrAttributesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | InvHrAttributesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | InvHrAttributesPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | InvHrAttributesPEOCostAllocationKeyflexId | — |
| CREATED_BY | InvHrAttributesPEOCreatedBy | — |
| CREATION_DATE | InvHrAttributesPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvHrAttributesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | InvHrAttributesPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | InvHrAttributesPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | InvHrAttributesPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | InvHrAttributesPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | InvHrAttributesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvHrAttributesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvHrAttributesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | InvHrAttributesPEOLegalEntityId | — |
| LOCATION_ID | InvHrAttributesPEOLocationId | — |
| OBJECT_VERSION_NUMBER | InvHrAttributesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvHrAttributesPEOOrganizationId | — |
| TYPE | InvHrAttributesPEOType | ✅ |

### [[item|Item]] (OTHER · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |
| TYPE | OrganizationUnitPEOType | — |

### [[itempendingpvo|ItemPendingPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId2_1 | — |

### [[itemref|ItemRef]] (OTHER · BICC: 6/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOType | ✅ |

### [[itemreferencepvo|ItemReferencePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId3_1 | — |

### [[legalemployerpvo|LegalEmployerPVO]] (HCM · BICC: 16/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | ✅ |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | ✅ |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 10/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | ✅ |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | ✅ |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[organizationpvo|OrganizationPVO]] (HCM · BICC: 3/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[organizationrefpvo|OrganizationRefPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[organizationunitpvo|OrganizationUnitPVO]] (HCM · BICC: 11/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[organizationunittranslationpvo|OrganizationUnitTranslationPVO]] (HCM · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | ✅ |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | ✅ |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | ✅ |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[payrollstatutoryunitpvo|PayrollStatutoryUnitPVO]] (HCM · BICC: 9/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | ✅ |

### [[persondisabilitypvo|PersonDisabilityPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitMgrPEOEffectiveStartDate | ✅ |
| ORGANIZATION_ID | OrganizationUnitMgrPEOOrganizationId | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 4/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DelegatePositionOrgUnitPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ParentPositionOrgUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionOrgUnitPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionOrgUnitPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | DelegatePositionOrgUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionOrgUnitPEOLastUpdateDate | ✅ |
| ORGANIZATION_ID | DelegatePositionOrgUnitPEOOrganizationId | — |
| ORGANIZATION_ID | ParentPositionOrgUnitPEOOrganizationId | — |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 4/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DelegatePositionOrgUnitPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ParentPositionOrgUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionOrgUnitPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionOrgUnitPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | DelegatePositionOrgUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionOrgUnitPEOLastUpdateDate | ✅ |
| ORGANIZATION_ID | DelegatePositionOrgUnitPEOOrganizationId | — |
| ORGANIZATION_ID | ParentPositionOrgUnitPEOOrganizationId | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[projectexpenditureorganizationpvo|ProjectExpenditureOrganizationPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[projecttaskowningorganizationpvo|ProjectTaskOwningOrganizationPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[projectunitclassificationpvo|ProjectUnitClassificationPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitActionOccurrenceId | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitCostAllocationKeyflexId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | ✅ |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitDateTo | ✅ |
| EFFECTIVE_START_DATE | BusinessUnitDateFrom | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitId | ✅ |
| TYPE | OrganizationUnitType | — |

### [[reportingestablishmentpvo|ReportingEstablishmentPVO]] (HCM · BICC: 8/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[reportingestablishmentpvoviewall|ReportingEstablishmentPVOViewAll]] (HCM · BICC: 7/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | — |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[sitetaxexemption|SiteTaxExemption]] (AR · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrganizationUnitBusinessGroupId | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitEffectiveStartDate | — |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | OrganizationUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber4 | — |
| ORGANIZATION_ID | OrganizationUnitOrganizationId | — |
| TYPE | OrganizationUnitType | — |

### [[taxexemption|TaxExemption]] (AR · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrganizationUnitBusinessGroupId | — |
| CREATED_BY | OrganizationUnitCreatedBy | — |
| CREATION_DATE | OrganizationUnitCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitEffectiveStartDate | — |
| ESTABLISHMENT_ID | OrganizationUnitEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitLegalEntityId | — |
| LOCATION_ID | OrganizationUnitLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber4 | — |
| ORGANIZATION_ID | OrganizationUnitOrganizationId | — |
| TYPE | OrganizationUnitType | — |

### [[taxreportingunitpvo|TaxReportingUnitPVO]] (HCM · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | ✅ |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | — |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |

### [[unionpvo|UnionPVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationUnitPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationUnitPEOBusinessGroupId | — |
| COST_ALLOCATION_KEYFLEX_ID | OrganizationUnitPEOCostAllocationKeyflexId | — |
| CREATED_BY | OrganizationUnitPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitPEOEffectiveStartDate | ✅ |
| ESTABLISHMENT_ID | OrganizationUnitPEOEstablishmentId | — |
| INTERNAL_ADDRESS_LINE | OrganizationUnitPEOInternalAddressLine | ✅ |
| INTERNAL_EXTERNAL_FLAG | OrganizationUnitPEOInternalExternalFlag | — |
| LAST_UPDATE_DATE | OrganizationUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | OrganizationUnitPEOLegalEntityId | — |
| LOCATION_ID | OrganizationUnitPEOLocationId | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitPEOOrganizationId | ✅ |
| TYPE | OrganizationUnitPEOOrganizationUnitPEOType | — |
