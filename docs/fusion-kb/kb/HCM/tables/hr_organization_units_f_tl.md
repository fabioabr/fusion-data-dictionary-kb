---
id: DOC-HCM-281
doc_type: system-doc
title: "HR_ORGANIZATION_UNITS_F_TL — Unidades Organizacionais — Traducoes"
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
  - traducoes
  - nls
  - organization
aliases:
  - HR_ORGANIZATION_UNITS_F_TL
  - hr_organization_units_f_tl
  - hr-organization-units-f-tl
  - org-units-translations
  - unidades-organizacionais-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ORGANIZATION_UNITS_F_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hr_all_organization_units_f]].

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-idioma:** Nomes e descricoes traduzidos para multiplos idiomas.
- **Exibicao:** Textos traduzidos para interfaces de usuario e relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hr_all_organization_units_f]] | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 100% |
| 3 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 4 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 5 | NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (registro base do cadastro)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.NAME
FROM   HR_ORGANIZATION_UNITS_F_TL tl
WHERE  tl.ORGANIZATION_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (ORGANIZATION_ID, EFFECTIVE_START_DATE, LANGUAGE).
- JOIN com [[hr_all_organization_units_f]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HR_ORGANIZATION_UNITS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrorganizationunitsftl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTranslationPEOLanguage | — |
| NAME | OrgUnitTranslationPEOName | ✅ |
| ORGANIZATION_ID | OrgUnitTranslationPEOOrganizationId | — |

### [[awardfundingsourcepvo|AwardFundingSourcePVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTranslationPEOLanguage | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| ORGANIZATION_ID | OrgUnitTranslationPEOOrganizationId | — |

### [[awardheaderpvo|AwardHeaderPVO]] (OTHER · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitTranslationP1EffectiveEndDate2 | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationP1EffectiveStartDate2 | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEffectiveStartDate1 | — |
| LANGUAGE | OrganizationUnitTranslationP1Language1 | — |
| LANGUAGE | OrganizationUnitTranslationPLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| NAME | PrevAwardBusinessUnitName | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationPOrganizationId1 | — |
| ORGANIZATION_ID | PrevAwardBusinessUnitId | ✅ |

### [[awardheaderviewpvo|AwardHeaderViewPVO]] (OTHER · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate2 | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate2 | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEffectiveStartDate1 | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage1 | — |
| LANGUAGE | OrganizationUnitTranslationPLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| NAME | PrevAwardBusinessUnitName | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationPOrganizationId1 | — |
| ORGANIZATION_ID | PrevAwardBusinessUnitId | — |

### [[billingeventpvo|BillingEventPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| LANGUAGE | Language | — |
| NAME | EventBusinessUnitPEOName | — |
| ORGANIZATION_ID | OrganizationId | — |

### [[businessunitpvo|BusinessUnitPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[contactpersondisabilitypvo|ContactPersonDisabilityPVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveStartDate | — |
| LANGUAGE | PrvdrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrExpenditureOrgTrnsltnPEOLanguage | — |
| NAME | PrvdrBusinessUnitTrnsltnPEOName | — |
| NAME | RcvrBusinessUnitTrnsltnPEOName | — |
| NAME | RcvrExpenditureOrgTrnsltnPEOName | — |
| OBJECT_VERSION_NUMBER | PrvdrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcvrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PrvdrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrExpenditureOrgTrnsltnPEOOrganizationId | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveStartDate | — |
| LANGUAGE | PrvdrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrExpenditureOrgTrnsltnPEOLanguage | — |
| NAME | PrvdrBusinessUnitTrnsltnPEOName | — |
| NAME | RcvrBusinessUnitTrnsltnPEOName | — |
| NAME | RcvrExpenditureOrgTrnsltnPEOName | — |
| OBJECT_VERSION_NUMBER | PrvdrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcvrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PrvdrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrExpenditureOrgTrnsltnPEOOrganizationId | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveStartDate | — |
| LANGUAGE | PrvdrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrExpenditureOrgTrnsltnPEOLanguage | — |
| NAME | PrvdrBusinessUnitTrnsltnPEOName | ✅ |
| NAME | RcvrBusinessUnitTrnsltnPEOName | ✅ |
| NAME | RcvrExpenditureOrgTrnsltnPEOName | ✅ |
| OBJECT_VERSION_NUMBER | PrvdrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcvrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PrvdrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrExpenditureOrgTrnsltnPEOOrganizationId | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PrvdrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrBusinessUnitTrnsltnPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RcvrExpenditureOrgTrnsltnPEOEffectiveStartDate | — |
| LANGUAGE | PrvdrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrBusinessUnitTrnsltnPEOLanguage | — |
| LANGUAGE | RcvrExpenditureOrgTrnsltnPEOLanguage | — |
| NAME | PrvdrBusinessUnitTrnsltnPEOName | ✅ |
| NAME | RcvrBusinessUnitTrnsltnPEOName | ✅ |
| NAME | RcvrExpenditureOrgTrnsltnPEOName | ✅ |
| OBJECT_VERSION_NUMBER | PrvdrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RcvrBusinessUnitTrnsltnPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PrvdrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrBusinessUnitTrnsltnPEOOrganizationId | — |
| ORGANIZATION_ID | RcvrExpenditureOrgTrnsltnPEOOrganizationId | — |

### [[departmentpvo|DepartmentPVO]] (HCM · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | ✅ |

### [[departmentpvoviewall|DepartmentPVOViewAll]] (HCM · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | ✅ |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[enterprisepvo|EnterprisePVO]] (HCM · BICC: 8/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | ✅ |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[fundingpositionpvo|FundingPositionPVO]] (PO · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | BusinessUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | BusinessUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | BusinessUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | BusinessUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitTranslationPEOLastUpdatedBy | — |
| NAME | BusinessUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | BusinessUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | BusinessUnitTranslationPEOSourceLang | — |

### [[fundingsourcepvo|FundingSourcePVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| NAME | OrganizationPEOName | — |
| ORGANIZATION_ID | FundingSourceAllPEOOrganizationId | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTranslationMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | OrgUnitTranslationMgrPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTranslationMgrPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrgUnitTranslationMgrPEOLastUpdateDate | ✅ |
| NAME | OrgUnitTranslationMgrPEOName | ✅ |
| ORGANIZATION_ID | OrgUnitTranslationMgrPEOOrganizationId | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTranslationMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTranslationMgrPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTranslationMgrPEOLanguage | — |
| LAST_UPDATE_DATE | OrgUnitTranslationMgrPEOLastUpdateDate | ✅ |
| NAME | OrgUnitTranslationMgrPEOName | ✅ |
| ORGANIZATION_ID | OrgUnitTranslationMgrPEOOrganizationId | — |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitTranslationP1EffectiveEndDate6 | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationP1EffectiveStartDate6 | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEffectiveStartDate | — |
| LANGUAGE | OrganizationUnitTranslationP1Language | — |
| LANGUAGE | OrganizationUnitTranslationPLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| NAME | FinancialsBusinessUnitPEOName | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationP1OrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPOrganizationId | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | NonRevSalesOrgEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RevSalesOrgEffectiveEndDate | — |
| EFFECTIVE_START_DATE | NonRevSalesOrgEffectiveStartDate | — |
| EFFECTIVE_START_DATE | RevSalesOrgEffectiveStartDate | — |
| LANGUAGE | NonRevSalesOrgLanguage | — |
| LANGUAGE | RevSalesOrgLanguage | — |
| NAME | NonRevSalesOrgName | ✅ |
| NAME | RevSalesOrgName | ✅ |
| OBJECT_VERSION_NUMBER | NonRevSalesOrgObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RevSalesOrgObjectVersionNumber | — |
| ORGANIZATION_ID | NonRevSalesOrgOrganizationId | — |
| ORGANIZATION_ID | RevSalesOrgOrganizationId | — |

### [[inventoryitem|InventoryItem]] (OTHER · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTLPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTLPEOCreationDate | — |
| EFFECTIVE_END_DATE | MasterOrgUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MasterOrgUnitTLPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTLPEOEffectiveStartDate | ✅ |
| LANGUAGE | MasterOrgUnitTLPEOLanguage | — |
| LANGUAGE | OrganizationUnitTLPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTLPEOLastUpdatedBy | — |
| NAME | MasterOrgUnitTLPEOName | — |
| NAME | OrganizationUnitTLPEOName | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTLPEOObjectVersionNumber | — |
| ORGANIZATION_ID | MasterOrgUnitTLPEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTLPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTLPEOSourceLang | — |

### [[inventoryitemref|InventoryItemRef]] (OTHER · BICC: 8/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTLPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTLPEOCreationDate | — |
| EFFECTIVE_END_DATE | MasterOrgUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MasterOrgUnitTLPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTLPEOEffectiveStartDate | ✅ |
| LANGUAGE | MasterOrgUnitTLPEOLanguage | ✅ |
| LANGUAGE | OrganizationUnitTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTLPEOLastUpdatedBy | — |
| NAME | MasterOrgUnitTLPEOName | ✅ |
| NAME | OrganizationUnitTLPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTLPEOObjectVersionNumber | — |
| ORGANIZATION_ID | MasterOrgUnitTLPEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTLPEOOrganizationId | ✅ |
| SOURCE_LANG | OrganizationUnitTLPEOSourceLang | — |

### [[inventorylocatorpvo|InventoryLocatorPVO]] (OTHER · BICC: 7/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventorylocatorrefpvo|InventoryLocatorRefPVO]] (OTHER · BICC: 6/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparameterscyclecountvcpvo|InventoryOrgParametersCycleCountVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparametersinvtransvcpvo|InventoryOrgParametersInvTransVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparametersonhandqtyvcpvo|InventoryOrgParametersOnhandQtyVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparametersrcvreceiptdatavcpvo|InventoryOrgParametersRcvReceiptDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparametersrefpvo|InventoryOrgParametersRefPVO]] (OTHER · BICC: 4/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventoryorgparametersshipmentdatavcpvo|InventoryOrgParametersShipmentDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | InvOrgNamePEOLanguage | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventorysubinventorypvo|InventorySubinventoryPVO]] (OTHER · BICC: 6/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | InvOrgNamePEOLanguage | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[inventorysubinventoryrefpvo|InventorySubinventoryRefPVO]] (OTHER · BICC: 6/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvOrgNamePEOCreatedBy | — |
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | InvOrgNamePEOCreationDate | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | InvOrgNamePEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | InvOrgNamePEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | InvOrgNamePEOLanguage | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | InvOrgNamePEOLastUpdateDate | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | InvOrgNamePEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvOrgNamePEOLastUpdatedBy | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | InvOrgNamePEOName | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | InvOrgNamePEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | InvOrgNamePEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | InvOrgNamePEOSourceLang | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[invoicedistributionpvo|InvoiceDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate5 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate4 | — |
| LANGUAGE | Language | — |
| NAME | BUPEOName | — |
| ORGANIZATION_ID | OrganizationId | — |

### [[item|Item]] (OTHER · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTLPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTLPEOCreationDate | — |
| EFFECTIVE_END_DATE | MasterOrgUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MasterOrgUnitTLPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTLPEOEffectiveStartDate | ✅ |
| LANGUAGE | MasterOrgUnitTLPEOLanguage | — |
| LANGUAGE | OrganizationUnitTLPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTLPEOLastUpdatedBy | — |
| NAME | MasterOrgUnitTLPEOName | — |
| NAME | OrganizationUnitTLPEOName | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTLPEOObjectVersionNumber | — |
| ORGANIZATION_ID | MasterOrgUnitTLPEOOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitTLPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTLPEOSourceLang | — |

### [[itempendingpvo|ItemPendingPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransPEOEffectiveEndDate1_1 | — |
| EFFECTIVE_START_DATE | OrgUnitTransPEOEffectiveStartDate1_1 | — |
| LANGUAGE | OrgUnitTransPEOLanguage2_1 | — |
| ORGANIZATION_ID | OrgUnitTransPEOOrganizationId3_1 | — |

### [[itemref|ItemRef]] (OTHER · BICC: 10/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTLPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTLPEOCreationDate | — |
| EFFECTIVE_END_DATE | MasterOrgUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MasterOrgUnitTLPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitTLPEOEffectiveStartDate | ✅ |
| LANGUAGE | MasterOrgUnitTLPEOLanguage | ✅ |
| LANGUAGE | OrganizationUnitTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTLPEOLastUpdatedBy | — |
| NAME | MasterOrgUnitTLPEOName | ✅ |
| NAME | OrganizationUnitTLPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTLPEOObjectVersionNumber | — |
| ORGANIZATION_ID | MasterOrgUnitTLPEOOrganizationId | ✅ |
| ORGANIZATION_ID | OrganizationUnitTLPEOOrganizationId | ✅ |
| SOURCE_LANG | OrganizationUnitTLPEOSourceLang | ✅ |

### [[itemreferencepvo|ItemReferencePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransPEOEffectiveEndDate1_1 | — |
| EFFECTIVE_START_DATE | OrgUnitTransPEOEffectiveStartDate1_1 | — |
| LANGUAGE | OrgUnitTransPEOLanguage2_1 | — |
| ORGANIZATION_ID | OrgUnitTransPEOOrganizationId2_1 | — |

### [[legalemployerpvo|LegalEmployerPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 3/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | NonRevSalesOrgEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_END_DATE | RevSalesOrgEffectiveEndDate | — |
| EFFECTIVE_START_DATE | NonRevSalesOrgEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | RevSalesOrgEffectiveStartDate | — |
| LANGUAGE | NonRevSalesOrgLanguage | — |
| LANGUAGE | OrgUnitTransLanguage | — |
| LANGUAGE | RevSalesOrgLanguage | — |
| NAME | NonRevSalesOrgName | ✅ |
| NAME | OrgUnitTransName | — |
| NAME | RevSalesOrgName | ✅ |
| OBJECT_VERSION_NUMBER | NonRevSalesOrgObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RevSalesOrgObjectVersionNumber | — |
| ORGANIZATION_ID | NonRevSalesOrgOrganizationId | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| ORGANIZATION_ID | RevSalesOrgOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | ✅ |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[organizationpvo|OrganizationPVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[organizationrefpvo|OrganizationRefPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |

### [[organizationunitpvo|OrganizationUnitPVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[organizationunittranslationpvo|OrganizationUnitTranslationPVO]] (HCM · BICC: 10/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | ✅ |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | ✅ |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[orgtreebirvoforfscm|OrgTreeBIRVOForFscm]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | AncestorOrgUnitTranslationPEOCreatedBy | — |
| CREATED_BY | ChildOrgUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | AncestorOrgUnitTranslationPEOCreationDate | — |
| CREATION_DATE | ChildOrgUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | AncestorOrgUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ChildOrgUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AncestorOrgUnitTranslationPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | ChildOrgUnitTranslationPEOEffectiveStartDate | — |
| LANGUAGE | AncestorOrgUnitTranslationPEOLanguage | — |
| LANGUAGE | ChildOrgUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | AncestorOrgUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | ChildOrgUnitTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AncestorOrgUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChildOrgUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AncestorOrgUnitTranslationPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | ChildOrgUnitTranslationPEOLastUpdatedBy | — |
| NAME | AncestorOrgUnitTranslationPEOName | — |
| NAME | ChildOrgUnitTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | AncestorOrgUnitTranslationPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChildOrgUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AncestorOrgUnitTranslationPEOOrganizationId | — |
| ORGANIZATION_ID | ChildOrgUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | AncestorOrgUnitTranslationPEOSourceLang | — |
| SOURCE_LANG | ChildOrgUnitTranslationPEOSourceLang | — |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[payrollstatutoryunitpvo|PayrollStatutoryUnitPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[persondisabilitypvo|PersonDisabilityPVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTranslationMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTranslationMgrPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTranslationMgrPEOLanguage | ✅ |
| NAME | OrgUnitTranslationMgrPEOName | — |
| ORGANIZATION_ID | OrgUnitTranslationMgrPEOOrganizationId | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DelegatePositionOrgUnitTlPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ParentPositionOrgUnitTlPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionOrgUnitTlPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionOrgUnitTlPEOEffectiveStartDate | ✅ |
| LANGUAGE | DelegatePositionOrgUnitTlPEOLanguage | — |
| LANGUAGE | ParentPositionOrgUnitTlPEOLanguage | — |
| LAST_UPDATE_DATE | DelegatePositionOrgUnitTlPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionOrgUnitTlPEOLastUpdateDate | ✅ |
| NAME | DelegatePositionOrgUnitTlPEOName | ✅ |
| NAME | ParentPositionOrgUnitTlPEOName | ✅ |
| ORGANIZATION_ID | DelegatePositionOrgUnitTlPEOOrganizationId | — |
| ORGANIZATION_ID | ParentPositionOrgUnitTlPEOOrganizationId | — |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DelegatePositionOrgUnitTlPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ParentPositionOrgUnitTlPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionOrgUnitTlPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionOrgUnitTlPEOEffectiveStartDate | ✅ |
| LANGUAGE | DelegatePositionOrgUnitTlPEOLanguage | — |
| LANGUAGE | ParentPositionOrgUnitTlPEOLanguage | — |
| LAST_UPDATE_DATE | DelegatePositionOrgUnitTlPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionOrgUnitTlPEOLastUpdateDate | ✅ |
| NAME | DelegatePositionOrgUnitTlPEOName | ✅ |
| NAME | ParentPositionOrgUnitTlPEOName | ✅ |
| ORGANIZATION_ID | DelegatePositionOrgUnitTlPEOOrganizationId | — |
| ORGANIZATION_ID | ParentPositionOrgUnitTlPEOOrganizationId | — |

### [[project|Project]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | BusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[projectexec|ProjectExec]] (OTHER · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | BusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | ✅ |

### [[projectexpenditureorganizationpvo|ProjectExpenditureOrganizationPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | BusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[projecttaskowningorganizationpvo|ProjectTaskOwningOrganizationPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[projectunitclassificationpvo|ProjectUnitClassificationPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[projectview|ProjectView]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | BusinessUnitPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BusinessUnitPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| NAME | BusinessUnitPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | BusinessUnitPEOBusinessUnitId | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | FinBuEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationEffectiveEndDate | — |
| EFFECTIVE_START_DATE | FinBuEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationEffectiveStartDate | ✅ |
| LANGUAGE | FinBuLanguage | — |
| LANGUAGE | OrganizationUnitTranslationLanguage | — |
| NAME | BusinessUnitName | — |
| NAME | FinBuName | — |
| NAME | FinBuShortCode | — |
| ORGANIZATION_ID | FinBuBusinessUnitId | — |
| ORGANIZATION_ID | OrganizationUnitTranslationOrganizationId | — |

### [[reportingestablishmentpvo|ReportingEstablishmentPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[reportingestablishmentpvoviewall|ReportingEstablishmentPVOViewAll]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[taxreportingunitpvo|TaxReportingUnitPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | — |
| LANGUAGE | OrgUnitTransLanguage | — |
| NAME | OrgUnitTransName | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | — |
| LANGUAGE | OrgUnitTransLanguage | — |
| NAME | OrgUnitTransName | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | ✅ |
| LANGUAGE | OrgUnitTransLanguage | — |
| NAME | OrgUnitTransName | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 3/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitEffectiveEndDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitNonRevEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | OrganizationUnitEffectiveStartDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitNonRevEffectiveStartDate1 | — |
| LANGUAGE | OrgUnitTransLanguage | — |
| LANGUAGE | OrganizationUnitLanguage | — |
| LANGUAGE | OrganizationUnitNonRevLanguage | — |
| NAME | OrgUnitTransName | — |
| NAME | OrganizationUnitName1 | ✅ |
| NAME | OrganizationUnitNonRevName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitNonRevObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | OrganizationUnitObjectVersionNumber | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| ORGANIZATION_ID | OrganizationUnitNonRevOrganizationId1 | — |
| ORGANIZATION_ID | OrganizationUnitOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | OrgUnitTransEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrgUnitTransEffectiveStartDate | — |
| LANGUAGE | OrgUnitTransLanguage | — |
| NAME | OrgUnitTransName | — |
| ORGANIZATION_ID | OrgUnitTransOrganizationId | — |
| SOURCE_LANG | OrgUnitTransSourceLang | — |

### [[unionpvo|UnionPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | OrganizationUnitTranslationPEOCreatedBy | — |
| CREATION_DATE | OrganizationUnitTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | OrganizationUnitTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationUnitTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | OrganizationUnitTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | OrganizationUnitTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationUnitTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationUnitTranslationPEOLastUpdatedBy | — |
| NAME | OrganizationUnitTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationUnitTranslationPEOObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationUnitTranslationPEOOrganizationId | — |
| SOURCE_LANG | OrganizationUnitTranslationPEOSourceLang | — |
| TITLE | OrganizationUnitTranslationPEOTitle | — |
