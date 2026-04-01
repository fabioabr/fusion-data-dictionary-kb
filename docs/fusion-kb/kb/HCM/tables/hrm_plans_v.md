---
id: DOC-HCM-177
doc_type: system-doc
title: "HRM_PLANS_V — Planos de Sucessão — Visão"
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
  - succession
  - plans
aliases:
  - HRM_PLANS_V
  - hrm_plans_v
  - planos-de-sucessãovisão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLANS_V

## 📌 Visão Geral

View dos **planos de sucessão** do HCM. Posições-chave e potenciais sucessores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento de sucessão:** Visão consolidada.
- **Continuidade:** Posições-chave e candidatos.
- **Relatórios de talento:** Succession readiness.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano | — | 🟢 85% |
| 3 | PLAN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (POSITION, JOB, INCUMBENT) | — | 🟡 75% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 75% |
| 5 | POSITION_ID | NUMBER(18) | NULL | FK | Posição-chave | [[hr_all_positions_f]] | 🟡 75% |
| 6 | INCUMBENT_PERSON_ID | NUMBER(18) | NULL | FK | Titular atual | [[per_all_people_f]] | 🟡 75% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 8 | END_DATE | DATE | NULL | Data | Término | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

---

## 📎 Uso Típico

### Planos ativos
```sql
SELECT p.PLAN_ID, p.PLAN_NAME, p.PLAN_TYPE, p.STATUS_CODE
FROM   HRM_PLANS_V p
WHERE  p.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- View (sufixo `_V`).
- Utilizado em Talent Review meetings.

---

## 🔗 PVOs Relacionados

### [[planpvo|PlanPVO]] (HCM · BICC: 24/94)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE_CODE | PlanPEOAccessTypeCodeLookupCd | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CATEGORY | PlanPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_UNIT_ID | PlanPEOBusinessUnitId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | PlanPEODateFrom | — |
| DEPARTMENT_ID | PlanPEODepartmentId | ✅ |
| DESCRIPTION | PlanPEODescription | ✅ |
| ENABLE_ALERTS | PlanPEOEnableAlerts | — |
| ENTERPRISE_ID | PlanPEOEnterpriseId | ✅ |
| GRADE_ID | PlanPEOGradeId | ✅ |
| INCUMBENT_PERSON_ID | PlanPEOIncumbentPersonId | ✅ |
| INCUMBENT_ROLE_CHANGE_FLAG | PlanPEOIncumbentRoleChangeFlag | — |
| JOB_FAMILY_ID | PlanPEOJobFamilyId | ✅ |
| JOB_ID | PlanPEOJobId | ✅ |
| JOB_PROFILE_ID | PlanPEOJobProfileId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_RECORD_FLAG | PlanPEOLatestRecordFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_EDIT_ONLY | PlanPEOOwnerEditOnly | ✅ |
| PLAN_ID | PlanPEOPlanId | ✅ |
| PLAN_NAME | PlanPEOPlanName | ✅ |
| PLAN_TYPE | PlanPEOPlanTypeCode | ✅ |
| POSITION_ID | PlanPEOPositionId | ✅ |
| STATUS | PlanPEOStatusLookUpCode | ✅ |
| STATUS_REASON | PlanPEOStatusReason | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
