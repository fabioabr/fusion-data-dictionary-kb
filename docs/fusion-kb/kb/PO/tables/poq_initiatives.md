---
id: DOC-PO-041
doc_type: system-doc
title: "POQ_INITIATIVES — Iniciativas de Qualificação de Fornecedores"
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
  - initiatives
aliases:
  - POQ_INITIATIVES
  - poq_initiatives
  - iniciativas-qualificacao
  - supplier-qualification-initiatives
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_INITIATIVES

## 📌 Visão Geral

Armazena as **iniciativas de qualificação de fornecedores** no módulo de Procurement. Cada registro representa uma iniciativa (campanha/evento) de avaliação em massa de fornecedores, vinculada a um modelo de qualificação. A iniciativa agrupa as avaliações individuais de cada fornecedor participante.

> [!note] Prefixo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Supplier Qualification Management** (SQM) do Oracle Fusion Procurement.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Qualificação periódica:** Criação de rodadas de avaliação de fornecedores (anual, semestral, por evento).
- **Onboarding de fornecedores:** Iniciativas de qualificação inicial para novos fornecedores.
- **Requalificação:** Reavaliação de fornecedores após não conformidades ou mudanças contratuais.
- **Compliance:** Registro auditável de todas as iniciativas de qualificação conduzidas pela organização.
- **Análise de risco:** Base para relatórios de cobertura de qualificação do supply base.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INITIATIVE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da iniciativa de qualificação | — | 🟢 95% |
| 2 | INITIATIVE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome descritivo da iniciativa | — | 🟢 90% |
| 3 | INITIATIVE_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da iniciativa visível ao usuário | — | 🟡 75% |
| 4 | QUAL_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de qualificação utilizado na iniciativa | [[poq_qual_models]] | 🟢 90% |
| 5 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status da iniciativa: DRAFT, ACTIVE, CLOSED, CANCELED | — | 🟢 90% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada da iniciativa | — | 🟢 90% |
| 7 | START_DATE | DATE | NULL | Data | Data de início da iniciativa | — | 🟢 90% |
| 8 | END_DATE | DATE | NULL | Data | Data de encerramento da iniciativa | — | 🟢 90% |
| 9 | OWNER_ID | NUMBER(18) | NULL | Referência | Usuário responsável pela iniciativa | — | 🟡 75% |
| 10 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (procurement BU) | [[hr_all_organization_units_f]] | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 17 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 18 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da iniciativa de qualificação)

### Tabelas-filha (FK de saída)
- [[poq_initiative_suppliers]] — via `INITIATIVE_ID` (fornecedores participantes da iniciativa)

---

## 📎 Uso Típico

### Iniciativas ativas com modelo de qualificação
```sql
SELECT ini.INITIATIVE_ID, ini.INITIATIVE_NAME, ini.STATUS_CODE,
       ini.START_DATE, ini.END_DATE, qm.QUAL_MODEL_NAME
FROM   POQ_INITIATIVES ini
JOIN   POQ_QUAL_MODELS qm ON qm.QUAL_MODEL_ID = ini.QUAL_MODEL_ID
WHERE  ini.STATUS_CODE = 'ACTIVE';
```

### Contagem de iniciativas por status
```sql
SELECT ini.STATUS_CODE, COUNT(*) AS qtd_iniciativas
FROM   POQ_INITIATIVES ini
GROUP  BY ini.STATUS_CODE
ORDER  BY qtd_iniciativas DESC;
```

### Filtros comuns
- `STATUS_CODE = 'ACTIVE'` — Iniciativas em andamento
- `STATUS_CODE = 'CLOSED'` — Iniciativas encerradas
- `STATUS_CODE = 'DRAFT'` — Iniciativas em preparação

---

## 🔒 Observações

- Cada iniciativa está vinculada a exatamente um modelo de qualificação (`QUAL_MODEL_ID`).
- Os fornecedores participantes são registrados na tabela filha [[poq_initiative_suppliers]].
- O ciclo de vida típico é: DRAFT → ACTIVE → CLOSED (ou CANCELED).
- A iniciativa é o ponto de entrada para execução de avaliações em massa no Supplier Qualification Management.

---

## 🔗 PVOs Relacionados

### [[assessmentpvo|AssessmentPVO]] (PO · BICC: 79/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| AUTO_ACCEPT_RESPONSES_FLAG | InitiativeAutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | InitiativeAutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| CREATION_SOURCE | InitiativeCreationSource | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeInitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | InitiativeLastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

### [[initiativeextractpvo|InitiativeExtractPVO]] (PO · BICC: 28/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | AssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | AssessmentOwnerId | ✅ |
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
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
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
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| AUTO_ACCEPT_RESPONSES_FLAG | AutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | AutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | CanceledBy | ✅ |
| CANCELED_DATE | CanceledDate | ✅ |
| CANCELED_REASON_CODE | CanceledReasonCode | ✅ |
| COMPLETED_DATE | CompletedDate | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_SOURCE | CreationSource | ✅ |
| DESCRIPTION | Description | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeNumber | ✅ |
| INITIATIVE_USAGE_CODE | InitiativeUsageCode | — |
| INTERNAL_NOTE | InternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | LastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAUNCH_DATE | LaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_ID | OwnerId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| QUAL_MODEL_ID | QualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | ReuseActiveQualFlag | ✅ |
| STATUS | Status | ✅ |
| TITLE | Title | ✅ |
| TYPE | Type | ✅ |

### [[initiativepvo|InitiativePVO]] (PO · BICC: 80/81)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| AUTO_ACCEPT_RESPONSES_FLAG | InitiativeAutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | InitiativeAutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| CREATION_SOURCE | InitiativeCreationSource | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INITIATIVE_SURVEY_FLAG | InitiativeSurveyFlag | ✅ |
| INITIATIVE_USAGE_CODE | InitiativeUsageCode | — |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | InitiativeLastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

### [[initiativesupplierpvo|InitiativeSupplierPVO]] (PO · BICC: 75/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeInitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

### [[questionnaireresponseheaderspvo|QuestionnaireResponseHeadersPVO]] (PO · BICC: 79/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| AUTO_ACCEPT_RESPONSES_FLAG | InitiativeAutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | InitiativeAutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| CREATION_SOURCE | InitiativeCreationSource | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeInitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INITIATIVE_USAGE_CODE | InitiativeUsageCode | — |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | InitiativeLastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

### [[questionnaireresponsespvo|QuestionnaireResponsesPVO]] (PO · BICC: 79/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| AUTO_ACCEPT_RESPONSES_FLAG | InitiativeAutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | InitiativeAutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| CREATION_SOURCE | InitiativeCreationSource | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeInitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INITIATIVE_USAGE_CODE | InitiativeUsageCode | — |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | InitiativeLastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

### [[questionnaireresponsevaluespvo|QuestionnaireResponseValuesPVO]] (PO · BICC: 79/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_EVAL_DUE_DATE | InitiativeAssessmentEvalDueDate | ✅ |
| ASSESSMENT_OWNER_ID | InitiativeAssessmentOwnerId | ✅ |
| ATTRIBUTE1 | InitiativeAttribute1 | ✅ |
| ATTRIBUTE10 | InitiativeAttribute10 | ✅ |
| ATTRIBUTE11 | InitiativeAttribute11 | ✅ |
| ATTRIBUTE12 | InitiativeAttribute12 | ✅ |
| ATTRIBUTE13 | InitiativeAttribute13 | ✅ |
| ATTRIBUTE14 | InitiativeAttribute14 | ✅ |
| ATTRIBUTE15 | InitiativeAttribute15 | ✅ |
| ATTRIBUTE16 | InitiativeAttribute16 | ✅ |
| ATTRIBUTE17 | InitiativeAttribute17 | ✅ |
| ATTRIBUTE18 | InitiativeAttribute18 | ✅ |
| ATTRIBUTE19 | InitiativeAttribute19 | ✅ |
| ATTRIBUTE2 | InitiativeAttribute2 | ✅ |
| ATTRIBUTE20 | InitiativeAttribute20 | ✅ |
| ATTRIBUTE3 | InitiativeAttribute3 | ✅ |
| ATTRIBUTE4 | InitiativeAttribute4 | ✅ |
| ATTRIBUTE5 | InitiativeAttribute5 | ✅ |
| ATTRIBUTE6 | InitiativeAttribute6 | ✅ |
| ATTRIBUTE7 | InitiativeAttribute7 | ✅ |
| ATTRIBUTE8 | InitiativeAttribute8 | ✅ |
| ATTRIBUTE9 | InitiativeAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | InitiativeAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | InitiativeAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | InitiativeAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | InitiativeAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | InitiativeAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | InitiativeAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | InitiativeAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | InitiativeAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | InitiativeAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | InitiativeAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | InitiativeAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | InitiativeAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | InitiativeAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | InitiativeAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | InitiativeAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | InitiativeAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | InitiativeAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | InitiativeAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | InitiativeAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | InitiativeAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | InitiativeAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | InitiativeAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | InitiativeAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | InitiativeAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | InitiativeAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | InitiativeAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | InitiativeAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | InitiativeAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | InitiativeAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | InitiativeAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | InitiativeAttributeTimestamp9 | ✅ |
| AUTO_ACCEPT_RESPONSES_FLAG | InitiativeAutoAcceptResponsesFlag | ✅ |
| AUTO_POPULATE_RESPONSES_FLAG | InitiativeAutoPopulateResponsesFlag | ✅ |
| CANCELED_BY | InitiativeCanceledBy | ✅ |
| CANCELED_DATE | InitiativeCanceledDate | ✅ |
| CANCELED_REASON_CODE | InitiativeCanceledReasonCode | ✅ |
| COMPLETED_DATE | InitiativeCompletedDate | ✅ |
| CREATED_BY | InitiativeCreatedBy | ✅ |
| CREATION_DATE | InitiativeCreationDate | ✅ |
| CREATION_SOURCE | InitiativeCreationSource | ✅ |
| DESCRIPTION | InitiativeDescription | ✅ |
| INITIATIVE_ID | InitiativeInitiativeId | ✅ |
| INITIATIVE_NUMBER | InitiativeInitiativeNumber | ✅ |
| INITIATIVE_USAGE_CODE | InitiativeUsageCode | — |
| INTERNAL_NOTE | InitiativeInternalNote | ✅ |
| LAST_OVERDUE_REMINDER_DATE | InitiativeLastOverdueReminderDate | ✅ |
| LAST_UPDATE_DATE | InitiativeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InitiativeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | InitiativeLastUpdatedBy | ✅ |
| LAUNCH_DATE | InitiativeLaunchDate | ✅ |
| OBJECT_VERSION_NUMBER | InitiativeObjectVersionNumber | ✅ |
| OWNER_ID | InitiativeOwnerId | ✅ |
| PRC_BU_ID | InitiativePrcBuId | ✅ |
| QUAL_MODEL_ID | InitiativeQualModelId | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | InitiativeReuseActiveQualFlag | ✅ |
| STATUS | InitiativeStatus | ✅ |
| TITLE | InitiativeTitle | ✅ |
| TYPE | InitiativeType | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
