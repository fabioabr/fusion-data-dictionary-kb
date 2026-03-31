---
id: DOC-HCM-653
doc_type: system-doc
title: "PER_DISABILITIES_F — Deficiências/Necessidades Especiais"
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
  - pcd
  - deficiencias
  - disabilities
aliases:
  - PER_DISABILITIES_F
  - per_disabilities_f
  - per-disabilities-f
  - deficiências/necessidades-especiais
  - per-disabilities-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DISABILITIES_F

## 📌 Visão Geral

Armazena os registros de **deficiências e necessidades especiais** dos colaboradores, com vigência temporal. Informação utilizada para programas de inclusão e compliance com cotas legais.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inclusão** — registro de PcD (Pessoas com Deficiência) para programas de inclusão.
- **Compliance de cotas** — atendimento à Lei de Cotas (Lei 8.213/91 no Brasil).
- **Acessibilidade** — identificação de necessidades de adaptação do ambiente de trabalho.
- **Relatórios** — métricas de diversidade e inclusão.
- **Benefícios** — elegibilidade a benefícios especiais.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISABILITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria da deficiência (PHYSICAL, VISUAL, HEARING, etc.) | — | 🟢 85% |
| 6 | DEGREE | VARCHAR2(30) | NULL | Classificação | Grau da deficiência | — | 🟡 75% |
| 7 | STATUS | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador com registro de deficiência)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Colaboradores PcD
```sql
SELECT pd.PERSON_ID, pd.CATEGORY, pd.DEGREE
FROM   PER_DISABILITIES_F pd
WHERE  SYSDATE BETWEEN pd.EFFECTIVE_START_DATE AND pd.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `CATEGORY = 'PHYSICAL'` — Deficiência física
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Dados sensíveis (LGPD) — informações médicas protegidas.
- No Brasil, utilizada para cumprimento da Lei de Cotas (Art. 93, Lei 8.213/91).
- A categoria segue classificação padrão (física, visual, auditiva, mental, múltipla).
---

## 🔗 PVOs Relacionados

### [[contactpersondisabilitypvo|ContactPersonDisabilityPVO]] (HCM · BICC: 27/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOMMODATION_REQUEST | PersonDisabilityPEOAccommodationRequest | — |
| ASSESSMENT_DUE_DATE | PersonDisabilityPEOAssessmentDueDate | ✅ |
| ASSIGNMENT_ID | PersonDisabilityPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | PersonDisabilityPEOBusinessGroupId | ✅ |
| CATEGORY | PersonDisabilityPEOCategory | ✅ |
| CREATED_BY | PersonDisabilityPEOCreatedBy | ✅ |
| CREATION_DATE | PersonDisabilityPEOCreationDate | ✅ |
| DEGREE | PersonDisabilityPEODegree | ✅ |
| DESCRIPTION | PersonDisabilityPEODescription | ✅ |
| DISABILITY_CODE | PersonDisabilityPEODisabilityCode | ✅ |
| DISABILITY_ID | DisabilityId | ✅ |
| DISCLOSURE_DATE | PersonDisabilityPEODisclosureDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| INCIDENT_ID | PersonDisabilityPEOIncidentId | ✅ |
| LAST_UPDATE_DATE | PersonDisabilityPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDisabilityPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonDisabilityPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PersonDisabilityPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PersonDisabilityPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PersonDisabilityPEOOrganizationId | ✅ |
| PERSON_ID | PersonDisabilityPEOPersonId | ✅ |
| PRE_REGISTRATION_JOB | PersonDisabilityPEOPreRegistrationJob | ✅ |
| QUOTA_FTE | PersonDisabilityPEOQuotaFte | ✅ |
| REASON | PersonDisabilityPEOReason | ✅ |
| REGISTRATION_DATE | PersonDisabilityPEORegistrationDate | ✅ |
| REGISTRATION_EXP_DATE | PersonDisabilityPEORegistrationExpDate | ✅ |
| REGISTRATION_ID | PersonDisabilityPEORegistrationId | ✅ |
| SELF_DISCLOSED_TYPE | PersonDisabilityPEOSelfDisclosedType | — |
| STATUS | PersonDisabilityPEOStatus | ✅ |
| WORK_RESTRICTION | PersonDisabilityPEOWorkRestriction | ✅ |

### [[persondisabilitypvo|PersonDisabilityPVO]] (HCM · BICC: 31/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOMMODATION_REQUEST | PersonDisabilityPEOAccommodationRequest | ✅ |
| ASSESSMENT_DUE_DATE | PersonDisabilityPEOAssessmentDueDate | ✅ |
| ASSIGNMENT_ID | PersonDisabilityPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | PersonDisabilityPEOBusinessGroupId | ✅ |
| CATEGORY | PersonDisabilityPEOCategory | ✅ |
| CREATED_BY | PersonDisabilityPEOCreatedBy | ✅ |
| CREATION_DATE | PersonDisabilityPEOCreationDate | ✅ |
| DEGREE | PersonDisabilityPEODegree | ✅ |
| DESCRIPTION | PersonDisabilityPEODescription | ✅ |
| DISABILITY_CODE | PersonDisabilityPEODisabilityCode | ✅ |
| DISABILITY_ID | DisabilityId | ✅ |
| DISCLOSURE_DATE | PersonDisabilityPEODisclosureDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| INCIDENT_ID | PersonDisabilityPEOIncidentId | ✅ |
| LAST_UPDATE_DATE | PersonDisabilityPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDisabilityPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonDisabilityPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PersonDisabilityPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PersonDisabilityPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | PersonDisabilityPEOOrganizationId | ✅ |
| PERSON_ID | PersonDisabilityPEOPersonId | ✅ |
| PRE_REGISTRATION_JOB | PersonDisabilityPEOPreRegistrationJob | ✅ |
| QUOTA_FTE | PersonDisabilityPEOQuotaFte | ✅ |
| REASON | PersonDisabilityPEOReason | ✅ |
| REGISTRATION_DATE | PersonDisabilityPEORegistrationDate | ✅ |
| REGISTRATION_EXP_DATE | PersonDisabilityPEORegistrationExpDate | ✅ |
| REGISTRATION_ID | PersonDisabilityPEORegistrationId | ✅ |
| SELF_DISCLOSED_TYPE | PersonDisabilityPEOSelfDisclosedType | ✅ |
| STATUS | PersonDisabilityPEOStatus | ✅ |
| WORK_RESTRICTION | PersonDisabilityPEOWorkRestriction | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_DISABILITIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdisabilitiesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
