---
id: DOC-PO-046
doc_type: system-doc
title: "POQ_QUAL_AREA_QUESTIONS — Perguntas de Áreas de Qualificação"
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
  - questions
  - area-questions
aliases:
  - POQ_QUAL_AREA_QUESTIONS
  - poq_qual_area_questions
  - perguntas-area-qualificacao
  - qualification-area-questions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_AREA_QUESTIONS

## 📌 Visão Geral

Armazena as **perguntas associadas a cada área de qualificação** de fornecedores. Cada registro define uma pergunta individual — seu texto, tipo de resposta esperada, peso na pontuação e obrigatoriedade — vinculada a uma área de qualificação específica.

> [!note] Tabela base de perguntas
> Esta é a tabela base (física) das perguntas. Para consultas com textos traduzidos, utilize a view [[poq_qual_area_all_questions_v]].

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de questionários:** Cadastro das perguntas que compõem cada área de qualificação.
- **Avaliação de fornecedores:** Base para montagem do formulário de avaliação enviado ao fornecedor ou ao avaliador interno.
- **Pontuação automatizada:** Configuração de pesos e scores máximos para cálculo automático da nota.
- **Gestão de compliance:** Perguntas regulatórias obrigatórias (certificações, licenças, seguros).
- **Versionamento:** Controle de perguntas ativas/inativas para evolução dos critérios de qualificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pergunta | — | 🟢 90% |
| 2 | QUAL_AREA_ID | NUMBER(18) | NOT NULL | FK | Área de qualificação à qual a pergunta pertence | [[poq_qual_areas_vl]] | 🟢 90% |
| 3 | QUESTION_TEXT | VARCHAR2(4000) | NOT NULL | Conteúdo | Texto da pergunta | — | 🟢 90% |
| 4 | QUESTION_NUMBER | NUMBER | NULL | Identificação | Número sequencial da pergunta na área | — | 🟡 80% |
| 5 | RESPONSE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de resposta: TEXT, NUMBER, DATE, SINGLE_CHOICE, MULTI_CHOICE, ATTACHMENT | — | 🟡 80% |
| 6 | MANDATORY_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Pergunta obrigatória: Y/N | — | 🟡 80% |
| 7 | SCORING_FLAG | VARCHAR2(1) | NULL | Classificação | Se a pergunta contribui para pontuação: Y/N | — | 🟡 75% |
| 8 | MAX_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima possível para esta pergunta | — | 🟡 75% |
| 9 | WEIGHT | NUMBER | NULL | Pontuação | Peso da pergunta no cálculo da nota da área | — | 🟡 70% |
| 10 | HELP_TEXT | VARCHAR2(4000) | NULL | Conteúdo | Texto de orientação/ajuda para o respondente | — | 🟡 70% |
| 11 | DEFAULT_VALUE | VARCHAR2(2000) | NULL | Conteúdo | Valor padrão pré-preenchido na resposta | — | 🟡 65% |
| 12 | VALIDATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de validação aplicada à resposta | — | 🔴 50% |
| 13 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Se a pergunta está ativa: Y/N | — | 🟡 80% |
| 14 | PARENT_QUESTION_ID | NUMBER(18) | NULL | FK | Pergunta pai (para perguntas condicionais/dependentes) | [[poq_qual_area_questions]] | 🟡 60% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 20 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_areas_vl]] — via `QUAL_AREA_ID` (área de qualificação)
- [[poq_qual_area_questions]] (auto-referência) — via `PARENT_QUESTION_ID` (pergunta pai)

### Tabelas-filha / Views

### Tabelas relacionadas

---

## 📎 Uso Típico

### Perguntas ativas de uma área
```sql
SELECT q.QUESTION_NUMBER, q.QUESTION_TEXT, q.RESPONSE_TYPE,
       q.MANDATORY_FLAG, q.MAX_SCORE, q.WEIGHT
FROM   POQ_QUAL_AREA_QUESTIONS q
WHERE  q.QUAL_AREA_ID = :p_qual_area_id
  AND  q.ENABLED_FLAG = 'Y'
ORDER  BY q.QUESTION_NUMBER;
```

### Perguntas obrigatórias com pontuação
```sql
SELECT q.QUESTION_TEXT, q.MAX_SCORE, q.WEIGHT
FROM   POQ_QUAL_AREA_QUESTIONS q
WHERE  q.QUAL_AREA_ID = :p_qual_area_id
  AND  q.MANDATORY_FLAG = 'Y'
  AND  q.SCORING_FLAG = 'Y'
  AND  q.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Perguntas ativas
- `MANDATORY_FLAG = 'Y'` — Perguntas obrigatórias
- `RESPONSE_TYPE = 'SINGLE_CHOICE'` — Perguntas de múltipla escolha (única resposta)
- `SCORING_FLAG = 'Y'` — Perguntas que contribuem para a nota

---

## 🔒 Observações

- O `RESPONSE_TYPE` determina como a interface renderiza o campo: `TEXT` (campo livre), `SINGLE_CHOICE` (radio/dropdown), `ATTACHMENT` (upload de arquivo), etc.
- Perguntas com `PARENT_QUESTION_ID` preenchido são exibidas condicionalmente, dependendo da resposta à pergunta pai.
- A pontuação total da área é calculada como soma ponderada: `SUM(score_pergunta * WEIGHT)`.
- Perguntas desativadas (`ENABLED_FLAG = 'N'`) permanecem no banco para histórico, mas não aparecem em novos questionários.
- Para consultas que precisam de tradução, preferir a view [[poq_qual_area_all_questions_v]].

---

## 🔗 PVOs Relacionados

### [[qualareaquestionpvo|QualAreaQuestionPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QualAreaQuestionCreatedBy | ✅ |
| CREATION_DATE | QualAreaQuestionCreationDate | ✅ |
| DISPLAY_SEQUENCE | QualAreaQuestionDisplaySequence | ✅ |
| KNOCKOUT_SCORE | QualAreaQuestionKnockoutScore | ✅ |
| LAST_UPDATE_DATE | QualAreaQuestionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualAreaQuestionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QualAreaQuestionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QualAreaQuestionObjectVersionNumber | ✅ |
| QUAL_AREA_ID | QualAreaQuestionQualAreaId | ✅ |
| QUAL_AREA_QUESTION_ID | QualAreaQuestionId | ✅ |
| QUESTION_ID | QualAreaQuestionQuestionId | ✅ |
| WEIGHT | QualAreaQuestionWeight | ✅ |

### [[qualarearepositoryresponsepvo|QualAreaRepositoryResponsePVO]] (PO · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | QualAreaQuestionCreatedBy | ✅ |
| CREATION_DATE | QualAreaQuestionCreationDate | ✅ |
| DISPLAY_SEQUENCE | QualAreaQuestionDisplaySequence | ✅ |
| LAST_UPDATE_DATE | QualAreaQuestionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualAreaQuestionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QualAreaQuestionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QualAreaQuestionObjectVersionNumber | ✅ |
| QUAL_AREA_ID | QualAreaQuestionQualAreaId | ✅ |
| QUAL_AREA_QUESTION_ID | QualAreaQuestionQualAreaQuestionId | ✅ |
| QUESTION_ID | QualAreaQuestionQuestionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
