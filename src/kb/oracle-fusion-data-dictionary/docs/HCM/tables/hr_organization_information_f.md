---
id: DOC-HCM-280
doc_type: system-doc
title: "HR_ORGANIZATION_INFORMATION_F — Informacoes de Organizacao (Date-Effective)"
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
  - organization-info
  - configuracao
  - eav
aliases:
  - HR_ORGANIZATION_INFORMATION_F
  - hr_organization_information_f
  - hr-organization-information-f
  - org-information
  - informacoes-organizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ORGANIZATION_INFORMATION_F

## 📌 Visao Geral

Armazena **informacoes adicionais** de unidades organizacionais em formato EAV (Entity-Attribute-Value) com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Armazenar atributos especificos por tipo de organizacao.
- **Legal:** Informacoes de entidade legal (CNPJ, inscricao estadual).
- **HR:** Configuracoes de payroll, benefits e workforce por organizacao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_INFORMATION_ID | NUMBER(18) | NOT NULL | PK | Identificador da informacao | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 95% |
| 4 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Organizacao | [[hr_all_organization_units_f]] | 🟢 100% |
| 5 | ORG_INFORMATION_CONTEXT | VARCHAR2(30) | NOT NULL | Classificacao | Contexto/tipo da informacao | — | 🟢 95% |
| 6 | ORG_INFORMATION1 | VARCHAR2(240) | NULL | Dados | Valor do atributo 1 | — | 🟢 90% |
| 7 | ORG_INFORMATION2 | VARCHAR2(240) | NULL | Dados | Valor do atributo 2 | — | 🟢 90% |
| 8 | ORG_INFORMATION3 | VARCHAR2(240) | NULL | Dados | Valor do atributo 3 | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao das informacoes adicionais)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Informacoes por contexto
```sql
SELECT oi.ORG_INFORMATION_CONTEXT,
       oi.ORG_INFORMATION1, oi.ORG_INFORMATION2
FROM   HR_ORGANIZATION_INFORMATION_F oi
WHERE  oi.ORGANIZATION_ID = :p_org_id
  AND  SYSDATE BETWEEN oi.EFFECTIVE_START_DATE AND oi.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Estrutura EAV — o significado de ORG_INFORMATION1..N depende do ORG_INFORMATION_CONTEXT.
- Sufixo `_F` indica date-effective.

---

## 📚 Referencias

- [Oracle Docs — HR_ORGANIZATION_INFORMATION_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrorganizationinformationf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[awardfundingallocationpvo|AwardFundingAllocationPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | ✅ |
| ORG_INFORMATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[awardfundingpvo|AwardFundingPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | ✅ |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[awardheaderpvo|AwardHeaderPVO]] (OTHER · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION2 | BusinessUnitPEOLegalEntityId | ✅ |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORG_INFORMATION_NUMBER8 | BusinessUnitPEODefaultCurrencyCode | ✅ |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[awardheaderviewpvo|AwardHeaderViewPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION2 | BusinessUnitPEOLegalEntityId | — |
| ORG_INFORMATION8 | BusinessUnitPEODefaultCurrencyCode | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[billingeventpvo|BillingEventPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | — |
| ORG_INFORMATION2 | EventBusinessUnitPEOLegalEntityId | — |
| ORG_INFORMATION3 | EventBusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInformationId | — |
| ORGANIZATION_ID | EventBusinessUnitPEOBusinessUnitId | — |

### [[cashadvanceapplicationpvo|CashAdvanceApplicationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[cashadvancepvo|CashAdvancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[corporatecardtransactionpvo|CorporateCardTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[departmentmanagerpvo|DepartmentManagerPVO]] (HCM · BICC: 5/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationPEOBusinessGroupId | — |
| CREATED_BY | OrganizationInformationPEOCreatedBy | — |
| CREATION_DATE | OrganizationInformationPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationPEOLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationPEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationPEOObjectVersionNumber | — |
| ORG_INFORMATION1 | OrganizationInformationPEOOrgInformation1 | — |
| ORG_INFORMATION10 | OrganizationInformationPEOOrgInformation10 | — |
| ORG_INFORMATION11 | OrganizationInformationPEOOrgInformation11 | — |
| ORG_INFORMATION12 | OrganizationInformationPEOOrgInformation12 | — |
| ORG_INFORMATION13 | OrganizationInformationPEOOrgInformation13 | — |
| ORG_INFORMATION14 | OrganizationInformationPEOOrgInformation14 | — |
| ORG_INFORMATION15 | OrganizationInformationPEOOrgInformation15 | — |
| ORG_INFORMATION16 | OrganizationInformationPEOOrgInformation16 | — |
| ORG_INFORMATION17 | OrganizationInformationPEOOrgInformation17 | — |
| ORG_INFORMATION18 | OrganizationInformationPEOOrgInformation18 | — |
| ORG_INFORMATION19 | OrganizationInformationPEOOrgInformation19 | — |
| ORG_INFORMATION2 | OrganizationInformationPEOOrgInformation2 | ✅ |
| ORG_INFORMATION20 | OrganizationInformationPEOOrgInformation20 | — |
| ORG_INFORMATION21 | OrganizationInformationPEOOrgInformation21 | — |
| ORG_INFORMATION22 | OrganizationInformationPEOOrgInformation22 | — |
| ORG_INFORMATION23 | OrganizationInformationPEOOrgInformation23 | — |
| ORG_INFORMATION24 | OrganizationInformationPEOOrgInformation24 | — |
| ORG_INFORMATION25 | OrganizationInformationPEOOrgInformation25 | — |
| ORG_INFORMATION26 | OrganizationInformationPEOOrgInformation26 | — |
| ORG_INFORMATION27 | OrganizationInformationPEOOrgInformation27 | — |
| ORG_INFORMATION28 | OrganizationInformationPEOOrgInformation28 | — |
| ORG_INFORMATION29 | OrganizationInformationPEOOrgInformation29 | — |
| ORG_INFORMATION3 | OrganizationInformationPEOOrgInformation3 | — |
| ORG_INFORMATION30 | OrganizationInformationPEOOrgInformation30 | — |
| ORG_INFORMATION4 | OrganizationInformationPEOOrgInformation4 | — |
| ORG_INFORMATION5 | OrganizationInformationPEOOrgInformation5 | — |
| ORG_INFORMATION6 | OrganizationInformationPEOOrgInformation6 | — |
| ORG_INFORMATION7 | OrganizationInformationPEOOrgInformation7 | — |
| ORG_INFORMATION8 | OrganizationInformationPEOOrgInformation8 | — |
| ORG_INFORMATION9 | OrganizationInformationPEOOrgInformation9 | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_DATE1 | OrganizationInformationPEOOrgInformationDate1 | — |
| ORG_INFORMATION_DATE10 | OrganizationInformationPEOOrgInformationDate10 | — |
| ORG_INFORMATION_DATE11 | OrganizationInformationPEOOrgInformationDate11 | — |
| ORG_INFORMATION_DATE12 | OrganizationInformationPEOOrgInformationDate12 | — |
| ORG_INFORMATION_DATE13 | OrganizationInformationPEOOrgInformationDate13 | — |
| ORG_INFORMATION_DATE14 | OrganizationInformationPEOOrgInformationDate14 | — |
| ORG_INFORMATION_DATE15 | OrganizationInformationPEOOrgInformationDate15 | — |
| ORG_INFORMATION_DATE2 | OrganizationInformationPEOOrgInformationDate2 | — |
| ORG_INFORMATION_DATE3 | OrganizationInformationPEOOrgInformationDate3 | — |
| ORG_INFORMATION_DATE4 | OrganizationInformationPEOOrgInformationDate4 | — |
| ORG_INFORMATION_DATE5 | OrganizationInformationPEOOrgInformationDate5 | — |
| ORG_INFORMATION_DATE6 | OrganizationInformationPEOOrgInformationDate6 | — |
| ORG_INFORMATION_DATE7 | OrganizationInformationPEOOrgInformationDate7 | — |
| ORG_INFORMATION_DATE8 | OrganizationInformationPEOOrgInformationDate8 | — |
| ORG_INFORMATION_DATE9 | OrganizationInformationPEOOrgInformationDate9 | — |
| ORG_INFORMATION_ID | OrgInformationId | ✅ |
| ORG_INFORMATION_NUMBER1 | OrganizationInformationPEOOrgInformationNumber1 | — |
| ORG_INFORMATION_NUMBER10 | OrganizationInformationPEOOrgInformationNumber10 | — |
| ORG_INFORMATION_NUMBER11 | OrganizationInformationPEOOrgInformationNumber11 | — |
| ORG_INFORMATION_NUMBER12 | OrganizationInformationPEOOrgInformationNumber12 | — |
| ORG_INFORMATION_NUMBER13 | OrganizationInformationPEOOrgInformationNumber13 | — |
| ORG_INFORMATION_NUMBER14 | OrganizationInformationPEOOrgInformationNumber14 | — |
| ORG_INFORMATION_NUMBER15 | OrganizationInformationPEOOrgInformationNumber15 | — |
| ORG_INFORMATION_NUMBER16 | OrganizationInformationPEOOrgInformationNumber16 | — |
| ORG_INFORMATION_NUMBER17 | OrganizationInformationPEOOrgInformationNumber17 | — |
| ORG_INFORMATION_NUMBER18 | OrganizationInformationPEOOrgInformationNumber18 | — |
| ORG_INFORMATION_NUMBER19 | OrganizationInformationPEOOrgInformationNumber19 | — |
| ORG_INFORMATION_NUMBER2 | OrganizationInformationPEOOrgInformationNumber2 | — |
| ORG_INFORMATION_NUMBER20 | OrganizationInformationPEOOrgInformationNumber20 | — |
| ORG_INFORMATION_NUMBER3 | OrganizationInformationPEOOrgInformationNumber3 | — |
| ORG_INFORMATION_NUMBER4 | OrganizationInformationPEOOrgInformationNumber4 | — |
| ORG_INFORMATION_NUMBER5 | OrganizationInformationPEOOrgInformationNumber5 | — |
| ORG_INFORMATION_NUMBER6 | OrganizationInformationPEOOrgInformationNumber6 | — |
| ORG_INFORMATION_NUMBER7 | OrganizationInformationPEOOrgInformationNumber7 | — |
| ORG_INFORMATION_NUMBER8 | OrganizationInformationPEOOrgInformationNumber8 | — |
| ORG_INFORMATION_NUMBER9 | OrganizationInformationPEOOrgInformationNumber9 | — |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[expenditureitempvo|ExpenditureItemPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | OrgInfomationPEOPrvdrPrimaryLedgerID | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[expenditureitemrefpvo|ExpenditureItemRefPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | OrgInfomationPEOPrvdrPrimaryLedgerID | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OOrganizationInformationPEOActionOccurrenceId | — |
| ATTRIBUTE_CATEGORY | OOrganizationInformationPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | OrganizationInformationPEOBusinessGroupId | — |
| CREATED_BY | OrganizationInformationPEOCreatedBy | — |
| CREATION_DATE | OrganizationInformationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| LAST_UPDATE_DATE | OrganizationInformationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | OrganizationInformationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationPEOLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationPEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationPEOObjectVersionNumber | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[expensepvo|ExpensePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[externaltransactionspvo|ExternalTransactionsPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DepartmentWorkDayInfoPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | EnterpriseWorkDayInfoPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | LegalEntityWorkDayInfoPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | DepartmentWorkDayInfoPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EnterpriseWorkDayInfoPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | LegalEntityWorkDayInfoPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | DepartmentWorkDayInfoPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | EnterpriseWorkDayInfoPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | LegalEntityWorkDayInfoPEOLastUpdateDate | ✅ |
| ORG_INFORMATION4 | DepartmentWorkDayInfoPEOWorkingHoursFrequency | ✅ |
| ORG_INFORMATION4 | EnterpriseWorkDayInfoPEOWorkingHoursFrequency | ✅ |
| ORG_INFORMATION4 | LegalEntityWorkDayInfoPEOWorkingHoursFrequencey | ✅ |
| ORG_INFORMATION_ID | DepartmentWorkDayInfoPEOOrgInformationId | ✅ |
| ORG_INFORMATION_ID | EnterpriseWorkDayInfoPEOOrgInformationId | ✅ |
| ORG_INFORMATION_ID | LegalEntityWorkDayInfoPEOOrgInformationId | ✅ |
| ORG_INFORMATION_NUMBER1 | DepartmentWorkDayInfoPEOWorkingHours | ✅ |
| ORG_INFORMATION_NUMBER1 | EnterpriseWorkDayInfoPEOWorkingHours | ✅ |
| ORG_INFORMATION_NUMBER1 | LegalEntityWorkDayInfoPEOWorkingHours | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 12/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DepartmentWorkDayInfoPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | EnterpriseWorkDayInfoPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | LegalEntityWorkDayInfoPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DepartmentWorkDayInfoPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EnterpriseWorkDayInfoPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | LegalEntityWorkDayInfoPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | DepartmentWorkDayInfoPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | EnterpriseWorkDayInfoPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | LegalEntityWorkDayInfoPEOLastUpdateDate | ✅ |
| ORG_INFORMATION4 | DepartmentWorkDayInfoPEOWorkingHoursFrequency | ✅ |
| ORG_INFORMATION4 | EnterpriseWorkDayInfoPEOWorkingHoursFrequency | ✅ |
| ORG_INFORMATION4 | LegalEntityWorkDayInfoPEOWorkingHoursFrequencey | ✅ |
| ORG_INFORMATION_ID | DepartmentWorkDayInfoPEOOrgInformationId | — |
| ORG_INFORMATION_ID | EnterpriseWorkDayInfoPEOOrgInformationId | — |
| ORG_INFORMATION_ID | LegalEntityWorkDayInfoPEOOrgInformationId | — |
| ORG_INFORMATION_NUMBER1 | DepartmentWorkDayInfoPEOWorkingHours | ✅ |
| ORG_INFORMATION_NUMBER1 | EnterpriseWorkDayInfoPEOWorkingHours | ✅ |
| ORG_INFORMATION_NUMBER1 | LegalEntityWorkDayInfoPEOWorkingHours | ✅ |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION1 | ManagerId | — |
| ORG_INFORMATION2 | LegalEntityId | — |
| ORG_INFORMATION3 | PrimaryLedgerId | — |
| ORG_INFORMATION4 | DefaultSetId | — |
| ORG_INFORMATION7 | FinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | DefaultCurrencyCode | ✅ |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[invoicedistributionpvo|InvoiceDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate4 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate3 | — |
| ORG_INFORMATION3 | BUPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInformationId | — |
| ORGANIZATION_ID | BUPEOBusinessUnitId | — |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 9/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | ✅ |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | ✅ |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | ✅ |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | ✅ |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | ✅ |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | ✅ |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | ✅ |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[organizationinformationpvo|OrganizationInformationPVO]] (HCM · BICC: 75/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationPEOBusinessGroupId | — |
| CREATED_BY | OrganizationInformationPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationInformationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | OrganizationInformationPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationInformationPEOObjectVersionNumber | — |
| ORG_INFORMATION1 | OrganizationInformationPEOOrgInformation1 | ✅ |
| ORG_INFORMATION10 | OrganizationInformationPEOOrgInformation10 | ✅ |
| ORG_INFORMATION11 | OrganizationInformationPEOOrgInformation11 | ✅ |
| ORG_INFORMATION12 | OrganizationInformationPEOOrgInformation12 | ✅ |
| ORG_INFORMATION13 | OrganizationInformationPEOOrgInformation13 | ✅ |
| ORG_INFORMATION14 | OrganizationInformationPEOOrgInformation14 | ✅ |
| ORG_INFORMATION15 | OrganizationInformationPEOOrgInformation15 | ✅ |
| ORG_INFORMATION16 | OrganizationInformationPEOOrgInformation16 | ✅ |
| ORG_INFORMATION17 | OrganizationInformationPEOOrgInformation17 | ✅ |
| ORG_INFORMATION18 | OrganizationInformationPEOOrgInformation18 | ✅ |
| ORG_INFORMATION19 | OrganizationInformationPEOOrgInformation19 | ✅ |
| ORG_INFORMATION2 | OrganizationInformationPEOOrgInformation2 | ✅ |
| ORG_INFORMATION20 | OrganizationInformationPEOOrgInformation20 | ✅ |
| ORG_INFORMATION21 | OrganizationInformationPEOOrgInformation21 | ✅ |
| ORG_INFORMATION22 | OrganizationInformationPEOOrgInformation22 | ✅ |
| ORG_INFORMATION23 | OrganizationInformationPEOOrgInformation23 | ✅ |
| ORG_INFORMATION24 | OrganizationInformationPEOOrgInformation24 | ✅ |
| ORG_INFORMATION25 | OrganizationInformationPEOOrgInformation25 | ✅ |
| ORG_INFORMATION26 | OrganizationInformationPEOOrgInformation26 | ✅ |
| ORG_INFORMATION27 | OrganizationInformationPEOOrgInformation27 | ✅ |
| ORG_INFORMATION28 | OrganizationInformationPEOOrgInformation28 | ✅ |
| ORG_INFORMATION29 | OrganizationInformationPEOOrgInformation29 | ✅ |
| ORG_INFORMATION3 | OrganizationInformationPEOOrgInformation3 | ✅ |
| ORG_INFORMATION30 | OrganizationInformationPEOOrgInformation30 | ✅ |
| ORG_INFORMATION4 | OrganizationInformationPEOOrgInformation4 | ✅ |
| ORG_INFORMATION5 | OrganizationInformationPEOOrgInformation5 | ✅ |
| ORG_INFORMATION6 | OrganizationInformationPEOOrgInformation6 | ✅ |
| ORG_INFORMATION7 | OrganizationInformationPEOOrgInformation7 | ✅ |
| ORG_INFORMATION8 | OrganizationInformationPEOOrgInformation8 | ✅ |
| ORG_INFORMATION9 | OrganizationInformationPEOOrgInformation9 | ✅ |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | ✅ |
| ORG_INFORMATION_DATE1 | OrganizationInformationPEOOrgInformationDate1 | ✅ |
| ORG_INFORMATION_DATE10 | OrganizationInformationPEOOrgInformationDate10 | ✅ |
| ORG_INFORMATION_DATE11 | OrganizationInformationPEOOrgInformationDate11 | ✅ |
| ORG_INFORMATION_DATE12 | OrganizationInformationPEOOrgInformationDate12 | ✅ |
| ORG_INFORMATION_DATE13 | OrganizationInformationPEOOrgInformationDate13 | ✅ |
| ORG_INFORMATION_DATE14 | OrganizationInformationPEOOrgInformationDate14 | ✅ |
| ORG_INFORMATION_DATE15 | OrganizationInformationPEOOrgInformationDate15 | ✅ |
| ORG_INFORMATION_DATE2 | OrganizationInformationPEOOrgInformationDate2 | ✅ |
| ORG_INFORMATION_DATE3 | OrganizationInformationPEOOrgInformationDate3 | ✅ |
| ORG_INFORMATION_DATE4 | OrganizationInformationPEOOrgInformationDate4 | ✅ |
| ORG_INFORMATION_DATE5 | OrganizationInformationPEOOrgInformationDate5 | ✅ |
| ORG_INFORMATION_DATE6 | OrganizationInformationPEOOrgInformationDate6 | ✅ |
| ORG_INFORMATION_DATE7 | OrganizationInformationPEOOrgInformationDate7 | ✅ |
| ORG_INFORMATION_DATE8 | OrganizationInformationPEOOrgInformationDate8 | ✅ |
| ORG_INFORMATION_DATE9 | OrganizationInformationPEOOrgInformationDate9 | ✅ |
| ORG_INFORMATION_ID | OrgInformationId | ✅ |
| ORG_INFORMATION_NUMBER1 | OrganizationInformationPEOOrgInformationNumber1 | ✅ |
| ORG_INFORMATION_NUMBER10 | OrganizationInformationPEOOrgInformationNumber10 | ✅ |
| ORG_INFORMATION_NUMBER11 | OrganizationInformationPEOOrgInformationNumber11 | ✅ |
| ORG_INFORMATION_NUMBER12 | OrganizationInformationPEOOrgInformationNumber12 | ✅ |
| ORG_INFORMATION_NUMBER13 | OrganizationInformationPEOOrgInformationNumber13 | ✅ |
| ORG_INFORMATION_NUMBER14 | OrganizationInformationPEOOrgInformationNumber14 | ✅ |
| ORG_INFORMATION_NUMBER15 | OrganizationInformationPEOOrgInformationNumber15 | ✅ |
| ORG_INFORMATION_NUMBER16 | OrganizationInformationPEOOrgInformationNumber16 | ✅ |
| ORG_INFORMATION_NUMBER17 | OrganizationInformationPEOOrgInformationNumber17 | ✅ |
| ORG_INFORMATION_NUMBER18 | OrganizationInformationPEOOrgInformationNumber18 | ✅ |
| ORG_INFORMATION_NUMBER19 | OrganizationInformationPEOOrgInformationNumber19 | ✅ |
| ORG_INFORMATION_NUMBER2 | OrganizationInformationPEOOrgInformationNumber2 | ✅ |
| ORG_INFORMATION_NUMBER20 | OrganizationInformationPEOOrgInformationNumber20 | ✅ |
| ORG_INFORMATION_NUMBER3 | OrganizationInformationPEOOrgInformationNumber3 | ✅ |
| ORG_INFORMATION_NUMBER4 | OrganizationInformationPEOOrgInformationNumber4 | ✅ |
| ORG_INFORMATION_NUMBER5 | OrganizationInformationPEOOrgInformationNumber5 | ✅ |
| ORG_INFORMATION_NUMBER6 | OrganizationInformationPEOOrgInformationNumber6 | ✅ |
| ORG_INFORMATION_NUMBER7 | OrganizationInformationPEOOrgInformationNumber7 | ✅ |
| ORG_INFORMATION_NUMBER8 | OrganizationInformationPEOOrgInformationNumber8 | ✅ |
| ORG_INFORMATION_NUMBER9 | OrganizationInformationPEOOrgInformationNumber9 | ✅ |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | ✅ |

### [[organizationperworkdayinfopvo|OrganizationPerWorkDayInfoPVO]] (HCM · BICC: 4/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationPEOActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationPEOBusinessGroupId | — |
| CREATED_BY | OrganizationInformationPEOCreatedBy | — |
| CREATION_DATE | OrganizationInformationPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationPEOLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationPEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationPEOObjectVersionNumber | — |
| ORG_INFORMATION1 | OrganizationInformationPEOOrgInformation1 | — |
| ORG_INFORMATION10 | OrganizationInformationPEOOrgInformation10 | — |
| ORG_INFORMATION11 | OrganizationInformationPEOOrgInformation11 | — |
| ORG_INFORMATION12 | OrganizationInformationPEOOrgInformation12 | — |
| ORG_INFORMATION13 | OrganizationInformationPEOOrgInformation13 | — |
| ORG_INFORMATION14 | OrganizationInformationPEOOrgInformation14 | — |
| ORG_INFORMATION15 | OrganizationInformationPEOOrgInformation15 | — |
| ORG_INFORMATION16 | OrganizationInformationPEOOrgInformation16 | — |
| ORG_INFORMATION17 | OrganizationInformationPEOOrgInformation17 | — |
| ORG_INFORMATION18 | OrganizationInformationPEOOrgInformation18 | — |
| ORG_INFORMATION19 | OrganizationInformationPEOOrgInformation19 | — |
| ORG_INFORMATION2 | OrganizationInformationPEOOrgInformation2 | — |
| ORG_INFORMATION20 | OrganizationInformationPEOOrgInformation20 | — |
| ORG_INFORMATION21 | OrganizationInformationPEOOrgInformation21 | — |
| ORG_INFORMATION22 | OrganizationInformationPEOOrgInformation22 | — |
| ORG_INFORMATION23 | OrganizationInformationPEOOrgInformation23 | — |
| ORG_INFORMATION24 | OrganizationInformationPEOOrgInformation24 | — |
| ORG_INFORMATION25 | OrganizationInformationPEOOrgInformation25 | — |
| ORG_INFORMATION26 | OrganizationInformationPEOOrgInformation26 | — |
| ORG_INFORMATION27 | OrganizationInformationPEOOrgInformation27 | — |
| ORG_INFORMATION28 | OrganizationInformationPEOOrgInformation28 | — |
| ORG_INFORMATION29 | OrganizationInformationPEOOrgInformation29 | — |
| ORG_INFORMATION3 | OrganizationInformationPEOOrgInformation3 | — |
| ORG_INFORMATION30 | OrganizationInformationPEOOrgInformation30 | — |
| ORG_INFORMATION4 | OrganizationInformationPEOOrgInformation4 | — |
| ORG_INFORMATION5 | OrganizationInformationPEOOrgInformation5 | — |
| ORG_INFORMATION6 | OrganizationInformationPEOOrgInformation6 | — |
| ORG_INFORMATION7 | OrganizationInformationPEOOrgInformation7 | — |
| ORG_INFORMATION8 | OrganizationInformationPEOOrgInformation8 | — |
| ORG_INFORMATION9 | OrganizationInformationPEOOrgInformation9 | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_DATE1 | OrganizationInformationPEOOrgInformationDate1 | — |
| ORG_INFORMATION_DATE10 | OrganizationInformationPEOOrgInformationDate10 | — |
| ORG_INFORMATION_DATE11 | OrganizationInformationPEOOrgInformationDate11 | — |
| ORG_INFORMATION_DATE12 | OrganizationInformationPEOOrgInformationDate12 | — |
| ORG_INFORMATION_DATE13 | OrganizationInformationPEOOrgInformationDate13 | — |
| ORG_INFORMATION_DATE14 | OrganizationInformationPEOOrgInformationDate14 | — |
| ORG_INFORMATION_DATE15 | OrganizationInformationPEOOrgInformationDate15 | — |
| ORG_INFORMATION_DATE2 | OrganizationInformationPEOOrgInformationDate2 | — |
| ORG_INFORMATION_DATE3 | OrganizationInformationPEOOrgInformationDate3 | — |
| ORG_INFORMATION_DATE4 | OrganizationInformationPEOOrgInformationDate4 | — |
| ORG_INFORMATION_DATE5 | OrganizationInformationPEOOrgInformationDate5 | — |
| ORG_INFORMATION_DATE6 | OrganizationInformationPEOOrgInformationDate6 | — |
| ORG_INFORMATION_DATE7 | OrganizationInformationPEOOrgInformationDate7 | — |
| ORG_INFORMATION_DATE8 | OrganizationInformationPEOOrgInformationDate8 | — |
| ORG_INFORMATION_DATE9 | OrganizationInformationPEOOrgInformationDate9 | — |
| ORG_INFORMATION_ID | OrgInformationId | ✅ |
| ORG_INFORMATION_NUMBER1 | OrganizationInformationPEOOrgInformationNumber1 | — |
| ORG_INFORMATION_NUMBER10 | OrganizationInformationPEOOrgInformationNumber10 | — |
| ORG_INFORMATION_NUMBER11 | OrganizationInformationPEOOrgInformationNumber11 | — |
| ORG_INFORMATION_NUMBER12 | OrganizationInformationPEOOrgInformationNumber12 | — |
| ORG_INFORMATION_NUMBER13 | OrganizationInformationPEOOrgInformationNumber13 | — |
| ORG_INFORMATION_NUMBER14 | OrganizationInformationPEOOrgInformationNumber14 | — |
| ORG_INFORMATION_NUMBER15 | OrganizationInformationPEOOrgInformationNumber15 | — |
| ORG_INFORMATION_NUMBER16 | OrganizationInformationPEOOrgInformationNumber16 | — |
| ORG_INFORMATION_NUMBER17 | OrganizationInformationPEOOrgInformationNumber17 | — |
| ORG_INFORMATION_NUMBER18 | OrganizationInformationPEOOrgInformationNumber18 | — |
| ORG_INFORMATION_NUMBER19 | OrganizationInformationPEOOrgInformationNumber19 | — |
| ORG_INFORMATION_NUMBER2 | OrganizationInformationPEOOrgInformationNumber2 | — |
| ORG_INFORMATION_NUMBER20 | OrganizationInformationPEOOrgInformationNumber20 | — |
| ORG_INFORMATION_NUMBER3 | OrganizationInformationPEOOrgInformationNumber3 | — |
| ORG_INFORMATION_NUMBER4 | OrganizationInformationPEOOrgInformationNumber4 | — |
| ORG_INFORMATION_NUMBER5 | OrganizationInformationPEOOrgInformationNumber5 | — |
| ORG_INFORMATION_NUMBER6 | OrganizationInformationPEOOrgInformationNumber6 | — |
| ORG_INFORMATION_NUMBER7 | OrganizationInformationPEOOrgInformationNumber7 | — |
| ORG_INFORMATION_NUMBER8 | OrganizationInformationPEOOrgInformationNumber8 | — |
| ORG_INFORMATION_NUMBER9 | OrganizationInformationPEOOrgInformationNumber9 | — |
| ORGANIZATION_ID | OrganizationInformationPEOOrganizationId | — |

### [[organizationunitpvo|OrganizationUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoBUPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrgInfoOrgManagerPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoBUPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrgInfoOrgManagerPEOEffectiveStartDate | — |
| ORG_INFORMATION1 | OrgInfoBUPEOOrgInformation1 | — |
| ORG_INFORMATION2 | OrgInfoOrgManagerPEOOrgInformation2 | — |
| ORG_INFORMATION_ID | OrgInfoBUPEOOrgInformationId | — |
| ORG_INFORMATION_ID | OrgInfoOrgManagerPEOOrgInformationId | — |

### [[otbistatsbasesummarypvo|OtbiStatsBaseSummaryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[otbistatssummarypvo|OtbiStatsSummaryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BUPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[pjsactualcostsp1|PjsActualCostsP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BIImplOrgPEOPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrgInfoPEOOrgInfoContext | — |
| ORG_INFORMATION_ID | OrgInfoPEOOrgInformationId | — |

### [[pjscommitmentcostsp1|PjsCommitmentCostsP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BUImplOrgPEOPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrgInfoPEOOrgInfoContext | — |
| ORG_INFORMATION_ID | OrgInfoPEOOrgInformationId | — |

### [[project|Project]] (OTHER · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | ✅ |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[projectassetlinedetailpvo|ProjectAssetLineDetailPVO]] (OTHER · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CDLBusinessUnitPEOCreatedBy | — |
| CREATED_BY | ExpBUPEOCreatedBy | — |
| CREATION_DATE | CDLBusinessUnitPEOCreationDate | — |
| CREATION_DATE | ExpBUPEOCreationDate | — |
| EFFECTIVE_END_DATE | CDLBusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ExpBUPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | CDLBusinessUnitPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | ExpBUPEOEffectiveStartDate | — |
| LAST_UPDATE_DATE | CDLBusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ExpBUPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CDLBusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ExpBUPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CDLBusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | ExpBUPEOLastUpdatedBy | — |
| ORG_INFORMATION3 | CDLBusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION3 | ExpBUPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | CDLBusinessUnitPEOOrgInformationId | — |
| ORG_INFORMATION_ID | ExpBUPEOOrgInformationId | — |
| ORGANIZATION_ID | CDLBusinessUnitPEOBusinessUnitId | — |
| ORGANIZATION_ID | ExpBUPEOBusinessUnitId | — |

### [[projectcommitmentpvo|ProjectCommitmentPVO]] (OTHER · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrOrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | RcvrOrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION2 | OrgInformationPEOLegalEntityId | — |
| ORG_INFORMATION3 | OrgInfomationPEOPrvdrPrimaryLedgerID | — |
| ORG_INFORMATION3 | RcvrOrgInfomationPEOPrimaryLedgerID | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORG_INFORMATION_ID | RcvrOrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | RcvrOrgInfomationPEOBusinessUnitId | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[projectcostdistributionpvo|ProjectCostDistributionPVO]] (OTHER · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ExpenditureBUPEOCreatedBy | — |
| CREATED_BY | ProjectBUPEOCreatedBy | — |
| CREATION_DATE | ExpenditureBUPEOCreationDate | — |
| CREATION_DATE | ProjectBUPEOCreationDate | — |
| EFFECTIVE_END_DATE | ExpenditureBUPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ProjectBUPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ExpenditureBUPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ProjectBUPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | ExpenditureBUPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ProjectBUPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenditureBUPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ProjectBUPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenditureBUPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | ProjectBUPEOLastUpdatedBy | — |
| ORG_INFORMATION3 | ExpenditureBUPEOPrimaryLedgerId | — |
| ORG_INFORMATION3 | ProjectBUPEOPrimaryLedgerId | ✅ |
| ORG_INFORMATION_ID | ExpenditureBUPEOOrgInformationId | — |
| ORG_INFORMATION_ID | ProjectBUPEOOrgInformationId | — |
| ORGANIZATION_ID | ExpenditureBUPEOBusinessUnitId | — |
| ORGANIZATION_ID | ProjectBUPEOBusinessUnitId | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[projectexec|ProjectExec]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[projectperiodpvo|ProjectPeriodPVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | PrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrgInfoPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrgInfoPEOOrgInformationId | — |

### [[projectplanlinedetailbudgetpvo|ProjectPlanLineDetailBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[projectprogresspvo|ProjectProgressPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[projectview|ProjectView]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | ✅ |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |

### [[projplanlinedetailforecastpvo|ProjPlanLineDetailForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationInformationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationPEOEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPEOPrimaryLedgerId | — |
| ORG_INFORMATION_CONTEXT | OrganizationInformationPEOOrgInformationContext | — |
| ORG_INFORMATION_ID | OrganizationInformationPEOOrgInformationId | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | OrganizationInformationActionOccurrenceId | — |
| BUSINESS_GROUP_ID | OrganizationInformationBusinessGroupId | — |
| CREATED_BY | OrganizationInformationCreatedBy | — |
| CREATION_DATE | OrganizationInformationCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationInformationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationInformationEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | OrganizationInformationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationInformationLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationInformationLastUpdatedBy | — |
| LEGISLATION_CODE | OrganizationInformationLegislationCode | — |
| OBJECT_VERSION_NUMBER | OrganizationInformationObjectVersionNumber | — |
| ORG_INFORMATION1 | BusinessUnitManagerId | — |
| ORG_INFORMATION2 | BusinessUnitLegalEntityId | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION4 | BusinessUnitDefaultSetId | — |
| ORG_INFORMATION5 | OrganizationInformationOrgInformation5 | — |
| ORG_INFORMATION6 | BusinessUnitEnabledForHrFlag | — |
| ORG_INFORMATION7 | BusinessUnitFinancialsBusinessUnitId | — |
| ORG_INFORMATION8 | BusinessUnitDefaultCurrencyCode | — |
| ORG_INFORMATION9 | OrganizationInformationOrgInformation9 | — |
| ORG_INFORMATION_ID | OrganizationInformationOrgInformationId | — |
| ORGANIZATION_ID | OrganizationInformationOrganizationId | — |

### [[referenceaccount|ReferenceAccount]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgInfoEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgInfoEffectiveStartDate | — |
| ORG_INFORMATION3 | BusinessUnitPrimaryLedgerId | — |
| ORG_INFORMATION_ID | OrgInfoOrgInformationId | — |
