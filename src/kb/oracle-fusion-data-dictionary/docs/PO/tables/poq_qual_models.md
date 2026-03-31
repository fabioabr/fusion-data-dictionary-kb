---
id: DOC-PO-048
doc_type: system-doc
title: "POQ_QUAL_MODELS — Modelos de Qualificação de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - qualificacao
  - supplier-qualification
  - qualification-models
aliases:
  - POQ_QUAL_MODELS
  - poq_qual_models
  - modelos-qualificacao
  - qualification-models
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_MODELS

## 📌 Visão Geral

Armazena os **modelos de qualificação de fornecedores** do Supplier Qualification Management. Cada modelo define o conjunto de áreas de qualificação, seus pesos, e os critérios de aprovação/reprovação que serão aplicados na avaliação de fornecedores. O modelo é a entidade central que estrutura todo o processo de qualificação.

> [!note] Modelo como template
> O modelo funciona como um **template reutilizável** — pode ser vinculado a múltiplas iniciativas de qualificação ao longo do tempo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de critérios:** Configuração dos critérios e pesos de avaliação de fornecedores.
- **Padronização:** Garantia de que todas as avaliações seguem os mesmos critérios dentro de uma categoria.
- **Governança:** Controle centralizado dos modelos aprovados para uso em qualificação.
- **Segmentação:** Diferentes modelos para diferentes categorias de fornecedores (serviços, materiais, TI, etc.).
- **Evolução controlada:** Versionamento de modelos com status de ciclo de vida (draft, active, retired).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_MODEL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do modelo de qualificação | — | 🟢 95% |
| 2 | QUAL_MODEL_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do modelo de qualificação | — | 🟢 90% |
| 3 | QUAL_MODEL_CODE | VARCHAR2(30) | NULL | Identificação | Código interno do modelo | — | 🟡 80% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição do modelo e seu propósito | — | 🟢 90% |
| 5 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status do modelo: DRAFT, ACTIVE, RETIRED | — | 🟢 90% |
| 6 | SCORING_METHOD | VARCHAR2(30) | NULL | Classificação | Método de pontuação: WEIGHTED, PASS_FAIL, MANUAL | — | 🟡 80% |
| 7 | PASSING_SCORE | NUMBER | NULL | Pontuação | Score mínimo para aprovação no modelo | — | 🟡 75% |
| 8 | MAX_TOTAL_SCORE | NUMBER | NULL | Pontuação | Score máximo possível no modelo | — | 🟡 70% |
| 9 | VALIDITY_PERIOD_DAYS | NUMBER | NULL | Configuração | Período de validade da qualificação (em dias) | — | 🟡 65% |
| 10 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compra associada ao modelo | — | 🟡 60% |
| 11 | OWNER_ID | NUMBER(18) | NULL | Referência | Usuário responsável pelo modelo | — | 🟡 70% |
| 12 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (procurement BU) | [[hr_all_organization_units_f]] | 🟡 70% |
| 13 | EFFECTIVE_START_DATE | DATE | NULL | Data | Data de início de vigência do modelo | — | 🟡 75% |
| 14 | EFFECTIVE_END_DATE | DATE | NULL | Data | Data de fim de vigência do modelo | — | 🟡 75% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 20 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 21 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 22 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do modelo de qualificação)

### Tabelas-filha (FK de saída)
- [[poq_qual_model_areas]] — via `QUAL_MODEL_ID` (áreas do modelo)
- [[poq_qual_model_outcomes]] — via `QUAL_MODEL_ID` (outcomes do modelo)
- [[poq_initiatives]] — via `QUAL_MODEL_ID` (iniciativas que usam este modelo)

---

## 📎 Uso Típico

### Modelos ativos
```sql
SELECT qm.QUAL_MODEL_ID, qm.QUAL_MODEL_NAME, qm.SCORING_METHOD,
       qm.PASSING_SCORE, qm.VALIDITY_PERIOD_DAYS
FROM   POQ_QUAL_MODELS qm
WHERE  qm.STATUS_CODE = 'ACTIVE'
  AND  (qm.EFFECTIVE_END_DATE IS NULL OR qm.EFFECTIVE_END_DATE > SYSDATE);
```

### Modelo com suas áreas e pesos
```sql
SELECT qm.QUAL_MODEL_NAME, qa.QUAL_AREA_NAME, qma.WEIGHT_PERCENT
FROM   POQ_QUAL_MODELS qm
JOIN   POQ_QUAL_MODEL_AREAS qma ON qma.QUAL_MODEL_ID = qm.QUAL_MODEL_ID
JOIN   POQ_QUAL_AREAS_VL qa ON qa.QUAL_AREA_ID = qma.QUAL_AREA_ID
WHERE  qm.QUAL_MODEL_ID = :p_model_id
ORDER  BY qma.WEIGHT_PERCENT DESC;
```

### Filtros comuns
- `STATUS_CODE = 'ACTIVE'` — Modelos em uso
- `STATUS_CODE = 'DRAFT'` — Modelos em preparação
- `STATUS_CODE = 'RETIRED'` — Modelos aposentados (apenas histórico)

---

## 🔒 Observações

- O modelo é o ponto central do SQM: liga áreas, perguntas, outcomes e iniciativas.
- O `SCORING_METHOD` determina como a nota final é calculada: `WEIGHTED` (soma ponderada), `PASS_FAIL` (aprovado/reprovado por área), `MANUAL` (avaliador define).
- O `PASSING_SCORE` é o limiar mínimo para que o fornecedor receba outcome `QUALIFIED`.
- O `VALIDITY_PERIOD_DAYS` define por quanto tempo a qualificação é válida — após esse período, o fornecedor precisa ser reavaliado.
- Modelos `RETIRED` não podem ser usados em novas iniciativas, mas avaliações históricas permanecem vinculadas.

---

## 🔗 PVOs Relacionados

### [[qualificationmodelareaspvo|QualificationModelAreasPVO]] (PO · BICC: 19/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QualModelCreatedBy | ✅ |
| CREATION_DATE | QualModelCreationDate | ✅ |
| GLOBAL_FLAG | QualModelGlobalFlag | ✅ |
| LAST_UPDATE_DATE | QualModelLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualModelLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QualModelLastUpdatedBy | ✅ |
| LATEST_REVISION_FLAG | QualModelLatestRevisionFlag | ✅ |
| OBJECT_VERSION_NUMBER | QualModelObjectVersionNumber | ✅ |
| ORIGINAL_QUAL_MODEL_ID | QualModelOriginalQualModelId | ✅ |
| OWNER_ID | QualModelOwnerId | ✅ |
| PRC_BU_ID | QualModelPrcBuId | ✅ |
| QUAL_MODEL_DESCRIPTION | QualModelQualModelDescription | ✅ |
| QUAL_MODEL_ID | QualModelQualModelId | ✅ |
| QUAL_MODEL_LEVEL | QualModelQualModelLevel | ✅ |
| QUAL_MODEL_NAME | QualModelQualModelName | ✅ |
| QUAL_MODEL_STATUS | QualModelQualModelStatus | ✅ |
| QUAL_MODEL_USAGE_CODE | QualModelUsageCode | — |
| REVISION_NUMBER | QualModelRevisionNumber | ✅ |
| STDS_ORG_CODE | QualModelStdsOrgCode | ✅ |
| SUBJECT_CODE | QualModelSubjectCode | ✅ |

### [[qualificationmodelpvo|QualificationModelPVO]] (PO · BICC: 27/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVATION_DATE | QualificationModelActivationDate | ✅ |
| ASSESSMENT_OWNER_ID | QualificationModelAssessmentOwnerId | — |
| AUTO_EVAL_ASSESSMENT_FLAG | QualificationModelAutoEvalAssessmentFlag | ✅ |
| CREATED_BY | QualificationModelCreatedBy | ✅ |
| CREATION_DATE | QualificationModelCreationDate | ✅ |
| DEFAULT_ASSESSMT_OWNER_FLAG | QualificationModelDefaultAssessmtOwnerFlag | — |
| ENABLE_SCORING_FLAG | QualificationModelEnableScoringFlag | ✅ |
| EXPIRATION_REMINDER_PERIOD | QualificationModelExpirationReminderPeriod | ✅ |
| EXPIRATION_REMINDER_TYPE | QualificationModelExpirationReminderType | ✅ |
| GLOBAL_FLAG | QualificationModelGlobalFlag | ✅ |
| LAST_UPDATE_DATE | QualificationModelLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualificationModelLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QualificationModelLastUpdatedBy | ✅ |
| LATEST_REVISION_FLAG | QualificationModelLatestRevisionFlag | ✅ |
| NOTE_TO_SUPPLIER | QualificationModelNoteToSupplier | ✅ |
| OBJECT_VERSION_NUMBER | QualificationModelObjectVersionNumber | ✅ |
| ORIGINAL_QUAL_MODEL_ID | QualificationModelOriginalQualModelId | ✅ |
| OWNER_ID | QualificationModelOwnerId | ✅ |
| PRC_BU_ID | QualificationModelPrcBuId | ✅ |
| QUAL_MODEL_DESCRIPTION | QualificationModelQualModelDescription | ✅ |
| QUAL_MODEL_ID | QualModelId | ✅ |
| QUAL_MODEL_LEVEL | QualificationModelQualModelLevel | ✅ |
| QUAL_MODEL_NAME | QualificationModelQualModelName | ✅ |
| QUAL_MODEL_STATUS | QualificationModelQualModelStatus | ✅ |
| QUAL_MODEL_USAGE_CODE | QualModelUsageCode | — |
| REVISION_NUMBER | QualificationModelRevisionNumber | ✅ |
| SHOW_ASSESSMENT_QUAL_FLAG | QualificationModelShowAssessmentQualFlag | ✅ |
| SHOW_ASSESSMT_TO_SUPP_FLAG | QualificationModelShowAssessmtToSuppFlag | ✅ |
| SOURCING_ELIGIBLE_FLAG | QualificationModelSourcingEligibleFlag | — |
| SOURCING_SHARE_ELIG_FLAG | QualificationModelSourcingShareEligFlag | — |
| STDS_ORG_CODE | QualificationModelStdsOrgCode | ✅ |
| SUBJECT_CODE | QualificationModelSubjectCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
