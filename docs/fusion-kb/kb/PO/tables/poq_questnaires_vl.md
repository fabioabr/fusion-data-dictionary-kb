---
id: DOC-PO-055
doc_type: system-doc
title: "POQ_QUESTNAIRES_VL — Questionários de Qualificação (View Traduzida)"
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
  - questionarios
  - supplier-qualification
aliases:
  - POQ_QUESTNAIRES_VL
  - poq_questnaires_vl
  - questionarios-qualificacao-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTNAIRES_VL

## 📌 Visão Geral

View traduzida que expõe os **questionários de qualificação de fornecedores** do módulo Procurement. Armazena a definição de cada questionário — nome, descrição, tipo de qualificação, status e configurações de pontuação. Cada registro representa um template de questionário que pode ser associado a um ou mais processos de qualificação.

> [!note] Sufixo _VL
> O sufixo `_VL` (View Language) indica uma **view multilíngue** que junta automaticamente a tabela base com a tabela de tradução, retornando os textos no idioma da sessão do usuário.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de questionários:** Cadastro e manutenção dos templates de questionários de qualificação.
- **Processos de sourcing:** Associação de questionários a eventos de negociação e qualificação de fornecedores.
- **Configuração de avaliações:** Definição de parâmetros como pontuação mínima, prazo de validade e tipo de avaliação.
- **Catálogo de questionários:** Pesquisa e reutilização de questionários existentes em novos processos.
- **Compliance regulatório:** Questionários padronizados para atender requisitos normativos (ESG, Due Diligence, etc.).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do questionário | — | 🟡 75% |
| 2 | QUESTIONNAIRE_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome do questionário (traduzido) | — | 🟡 70% |
| 3 | QUESTIONNAIRE_CODE | VARCHAR2(100) | NULL | Identificação | Código mnemônico do questionário | — | 🟡 65% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada do questionário (traduzida) | — | 🟡 70% |
| 5 | QUALIFICATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de qualificação: TECHNICAL, FINANCIAL, COMPLIANCE, GENERAL | — | 🟡 65% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do questionário: ACTIVE, INACTIVE, DRAFT | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início de vigência do questionário | — | 🟡 65% |
| 8 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim de vigência do questionário | — | 🟡 65% |
| 9 | MIN_PASSING_SCORE | NUMBER | NULL | Pontuação | Pontuação mínima para aprovação | — | 🟡 60% |
| 10 | MAX_TOTAL_SCORE | NUMBER | NULL | Pontuação | Pontuação total máxima possível | — | 🟡 60% |
| 11 | SCORING_METHOD | VARCHAR2(30) | NULL | Pontuação | Método de cálculo: WEIGHTED_AVERAGE, SUM, PERCENTAGE | — | 🟡 55% |
| 12 | ALLOW_ATTACHMENTS_FLAG | VARCHAR2(1) | NULL | Configuração | Permite anexos nas respostas (Y/N) | — | 🟡 55% |
| 13 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 14 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma-fonte da tradução | — | 🟢 90% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-filha (FK de saída)
- [[poq_question_structure_v]] — via `QUESTIONNAIRE_ID` (estrutura de perguntas)
- [[poq_questnaire_responses]] — via `QUESTIONNAIRE_ID` (respostas submetidas)
- [[poq_questnaire_resp_headers]] — via `QUESTIONNAIRE_ID` (cabeçalhos de resposta)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Questionários ativos
```sql
SELECT q.QUESTIONNAIRE_ID,
       q.QUESTIONNAIRE_NAME,
       q.QUALIFICATION_TYPE,
       q.MIN_PASSING_SCORE,
       q.MAX_TOTAL_SCORE
FROM   POQ_QUESTNAIRES_VL q
WHERE  q.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN NVL(q.EFFECTIVE_START_DATE, SYSDATE)
                    AND NVL(q.EFFECTIVE_END_DATE, SYSDATE);
```

### Questionários por tipo de qualificação
```sql
SELECT q.QUESTIONNAIRE_NAME,
       q.DESCRIPTION,
       q.SCORING_METHOD,
       q.STATUS
FROM   POQ_QUESTNAIRES_VL q
WHERE  q.QUALIFICATION_TYPE = :p_qualification_type
ORDER BY q.QUESTIONNAIRE_NAME;
```

---

## 🔒 Observações

- Por ser uma view `_VL`, não deve ser utilizada para operações DML — utilizar as tabelas base `_B` e `_TL`.
- O `SCORING_METHOD` define como a pontuação final é calculada: **WEIGHTED_AVERAGE** (média ponderada pelos pesos das perguntas), **SUM** (soma simples), **PERCENTAGE** (percentual do máximo).
- Questionários com `STATUS = 'DRAFT'` não estão disponíveis para associação a processos de qualificação.
- O `MIN_PASSING_SCORE` é utilizado para determinar automaticamente se um fornecedor foi aprovado ou reprovado.
- A nomenclatura `QUESTNAIRES` (sem o 'i' em questionnaires) segue a convenção Oracle original.

---

## 🔗 PVOs Relacionados

### [[questionnaireextractpvo|QuestionnaireExtractPVO]] (PO · BICC: 18/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_CREATE_QUAL_FLAG | AutoCreateQualFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DUE_DATE | DueDate | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INTRODUCTION | Introduction | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| QUESTNAIRE_CUSTOM | QuestnaireCustom | ✅ |
| QUESTNAIRE_ID | QuestnaireId | ✅ |
| QUESTNAIRE_STATUS | QuestnaireStatus | ✅ |
| QUESTNAIRE_TITLE | QuestnaireTitle | ✅ |
| QUESTNAIRE_TYPE | QuestnaireType | ✅ |
| QUESTNAIRE_USAGE_CODE | QuestnaireUsageCode | — |
| SUPPLIER_REG_ID | SupplierRegId | ✅ |
| USE_QUESTION_BRANCH_FLAG | UseQuestionBranchFlag | ✅ |

### [[questionnaireresponseheaderspvo|QuestionnaireResponseHeadersPVO]] (PO · BICC: 16/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QuestionnaireCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireCreationDate | ✅ |
| DUE_DATE | QuestionnaireDueDate | ✅ |
| INITIATIVE_ID | QuestionnaireInitiativeId | ✅ |
| INTRODUCTION | QuestionnaireIntroduction | — |
| LAST_UPDATE_DATE | QuestionnaireLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionnaireLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireObjectVersionNumber | ✅ |
| PRC_BU_ID | QuestionnairePrcBuId | ✅ |
| QUESTNAIRE_CUSTOM | QuestionnaireQuestnaireCustom | ✅ |
| QUESTNAIRE_ID | QuestionnaireQuestnaireId | ✅ |
| QUESTNAIRE_STATUS | QuestionnaireQuestnaireStatus | ✅ |
| QUESTNAIRE_TITLE | QuestionnaireQuestnaireTitle | ✅ |
| QUESTNAIRE_TYPE | QuestionnaireQuestnaireType | ✅ |
| SUPPLIER_REG_ID | QuestionnaireSupplierRegId | ✅ |
| USE_QUESTION_BRANCH_FLAG | QuestionnaireUseQuestionBranchFlag | ✅ |

### [[questionnaireresponsespvo|QuestionnaireResponsesPVO]] (PO · BICC: 16/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QuestionnaireCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireCreationDate | ✅ |
| DUE_DATE | QuestionnaireDueDate | ✅ |
| INITIATIVE_ID | QuestionnaireInitiativeId | ✅ |
| INTRODUCTION | QuestionnaireIntroduction | — |
| LAST_UPDATE_DATE | QuestionnaireLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionnaireLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireObjectVersionNumber | ✅ |
| PRC_BU_ID | QuestionnairePrcBuId | ✅ |
| QUESTNAIRE_CUSTOM | QuestionnaireQuestnaireCustom | ✅ |
| QUESTNAIRE_ID | QuestionnaireQuestnaireId | ✅ |
| QUESTNAIRE_STATUS | QuestionnaireQuestnaireStatus | ✅ |
| QUESTNAIRE_TITLE | QuestionnaireQuestnaireTitle | ✅ |
| QUESTNAIRE_TYPE | QuestionnaireQuestnaireType | ✅ |
| SUPPLIER_REG_ID | QuestionnaireSupplierRegId | ✅ |
| USE_QUESTION_BRANCH_FLAG | QuestionnaireUseQuestionBranchFlag | ✅ |

### [[questionnaireresponsevaluespvo|QuestionnaireResponseValuesPVO]] (PO · BICC: 16/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QuestnaireCreatedBy | ✅ |
| CREATION_DATE | QuestnaireCreationDate | ✅ |
| DUE_DATE | QuestnaireDueDate | ✅ |
| INITIATIVE_ID | QuestnaireInitiativeId | ✅ |
| INTRODUCTION | QuestnaireIntroduction | — |
| LAST_UPDATE_DATE | QuestnaireLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestnaireLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestnaireLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestnaireObjectVersionNumber | ✅ |
| PRC_BU_ID | QuestnairePrcBuId | ✅ |
| QUESTNAIRE_CUSTOM | QuestnaireQuestnaireCustom | ✅ |
| QUESTNAIRE_ID | QuestnaireQuestnaireId | ✅ |
| QUESTNAIRE_STATUS | QuestnaireQuestnaireStatus | ✅ |
| QUESTNAIRE_TITLE | QuestnaireQuestnaireTitle | ✅ |
| QUESTNAIRE_TYPE | QuestnaireQuestnaireType | ✅ |
| SUPPLIER_REG_ID | QuestnaireSupplierRegId | ✅ |
| USE_QUESTION_BRANCH_FLAG | QuestnaireUseQuestionBranchFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
