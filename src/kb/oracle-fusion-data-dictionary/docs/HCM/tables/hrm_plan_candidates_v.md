---
id: DOC-HCM-179
doc_type: system-doc
title: "HRM_PLAN_CANDIDATES_V — Candidatos a Sucessão — Visão Enriquecida"
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
  - candidates
aliases:
  - HRM_PLAN_CANDIDATES_V
  - hrm_plan_candidates_v
  - candidatos-a-sucessãovisão-enriquecida
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLAN_CANDIDATES_V

## 📌 Visão Geral

View enriquecida de **candidatos a sucessão** com dados de perfil (nome, cargo, departamento).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Relatórios:** Visão com dados de perfil.
- **Talent Review:** Contexto completo.
- **Dashboards:** Painéis de gestão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_CANDIDATE_ID | NUMBER(18) | NOT NULL | PK | Identificador | — | 🟢 90% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrm_plans_v]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Candidato | [[per_all_people_f]] | 🟢 90% |
| 4 | PERSON_NAME | VARCHAR2(360) | NULL | Descrição | Nome completo | — | 🟡 75% |
| 5 | READINESS_CODE | VARCHAR2(30) | NULL | Classificação | Prontidão | — | 🟡 80% |
| 6 | READINESS_MEANING | VARCHAR2(240) | NULL | Descrição | Prontidão traduzida | — | 🟡 70% |
| 7 | RANKING | NUMBER | NULL | Métrica | Classificação | — | 🟡 70% |
| 8 | CURRENT_JOB_NAME | VARCHAR2(240) | NULL | Descrição | Cargo atual | — | 🟡 65% |
| 9 | CURRENT_DEPARTMENT | VARCHAR2(240) | NULL | Descrição | Departamento | — | 🟡 65% |
| 10 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabela base

---

## 📎 Uso Típico

### Candidatos prontos
```sql
SELECT pcv.PERSON_NAME, pcv.CURRENT_JOB_NAME, pcv.READINESS_MEANING
FROM   HRM_PLAN_CANDIDATES_V pcv
WHERE  pcv.PLAN_ID = :p_id AND pcv.READINESS_CODE = 'READY_NOW'
ORDER BY pcv.RANKING;
```

---

## 🔒 Observações

- View enriquecida (sufixo `_V`).
- Inclui dados de perfil sem joins adicionais.

---

## 🔗 PVOs Relacionados

### [[flex_bi_plancandidatedff_vi|FLEX_BI_PlanCandidateDFF_VI]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| ENTERPRISE_ID | s_k_5000 | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LATEST_RECORD_FLAG | LatestRecordFlag | — |
| PLAN_CANDIDATE_ID | s_k_5001 | — |

### [[plancandidatespvo|PlanCandidatesPVO]] (HCM · BICC: 17/86)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
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
| ATTRIBUTE_CATEGORY | PlanCandidatesPEOAttributeCategory | ✅ |
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
| CANDIDATE_RANKING | CandidateRanking | ✅ |
| CANDIDATE_TYPE | PlanCandidatesPEOCandidateType | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | PlanCandPEODateFrom | — |
| EMERGENCY_SUCCESSOR | EmergencySuccessor | ✅ |
| ENTERPRISE_ID | PlanCandidatesPEOEnterpriseId | ✅ |
| EXTERNAL_CANDIDATE_ID | PlanCandidatesPEOExteCandidateId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_RECORD_FLAG | PlanCandPEOLatestRecordFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PlanCandidatesPEOPersonId | ✅ |
| PLAN_CANDIDATE_ID | PlanCandidatesPEOPlanCandidateId | ✅ |
| PLAN_ID | PlanCandidatesPEOPlanId | ✅ |
| READINESS_CODE | PlanCandidatesPEOReadinessCode | ✅ |
| SHOW_SUCCESSION_STATUS_FLAG | PlanCandPEOShowSuccStatusFlag | — |
| STATUS | PlanCandidatesPEOStatus | ✅ |
| SUCCESSION_STATUS | PlanCandPEOSuccessionStatus | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
