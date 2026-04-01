---
id: DOC-PO-059
doc_type: system-doc
title: "POQ_QUES_ACC_RESPONSES_VL — Respostas Aceitáveis de Perguntas (View Traduzida)"
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
  - acceptable-responses
  - supplier-qualification
aliases:
  - POQ_QUES_ACC_RESPONSES_VL
  - poq_ques_acc_responses_vl
  - respostas-aceitaveis-perguntas-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUES_ACC_RESPONSES_VL

## 📌 Visão Geral

View traduzida que expõe as **respostas aceitáveis** (acceptable responses) pré-definidas para perguntas de questionários de qualificação de fornecedores. Define as opções válidas de resposta para perguntas de escolha (SINGLE_CHOICE, MULTI_CHOICE), funcionando como uma lista de valores (LOV) traduzida no idioma do usuário.

> [!note] Sufixo _VL
> O sufixo `_VL` (View Language) indica uma **view multilíngue** que junta automaticamente a tabela base com a tabela de tradução, retornando os textos no idioma da sessão do usuário.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Opções de resposta:** Definição das alternativas válidas para perguntas de múltipla escolha.
- **Validação de respostas:** Verificação se a resposta do fornecedor está dentro das opções aceitáveis.
- **Scoring automático:** Associação de cada opção de resposta a uma pontuação específica.
- **Padronização:** Garantia de respostas uniformes entre fornecedores para facilitar comparação.
- **Tradução:** Exibição das opções no idioma do fornecedor/avaliador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACC_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da resposta aceitável | — | 🟡 70% |
| 2 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Pergunta à qual esta resposta aceitável pertence | [[poq_questions_vl]] | 🟡 75% |
| 3 | RESPONSE_VALUE | VARCHAR2(4000) | NOT NULL | Dados | Texto da resposta aceitável (traduzido) | — | 🟡 70% |
| 4 | RESPONSE_CODE | VARCHAR2(100) | NULL | Identificação | Código interno da resposta | — | 🟡 60% |
| 5 | SCORE | NUMBER | NULL | Pontuação | Pontuação associada a esta resposta | — | 🟡 70% |
| 6 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição da opção | — | 🟡 70% |
| 7 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se é a resposta padrão (Y/N) | — | 🟡 55% |
| 8 | ACCEPTABLE_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se a resposta é considerada aceitável para aprovação (Y/N) | — | 🟡 60% |
| 9 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição ou tooltip da opção (traduzida) | — | 🟡 60% |
| 10 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 11 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma-fonte da tradução | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questions_vl]] — via `QUESTION_ID` (pergunta associada)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Opções de resposta para uma pergunta
```sql
SELECT ar.ACC_RESPONSE_ID,
       ar.RESPONSE_VALUE,
       ar.SCORE,
       ar.ACCEPTABLE_FLAG,
       ar.DISPLAY_ORDER
FROM   POQ_QUES_ACC_RESPONSES_VL ar
WHERE  ar.QUESTION_ID = :p_question_id
ORDER BY ar.DISPLAY_ORDER;
```

### Respostas aceitáveis com pontuação máxima
```sql
SELECT ar.QUESTION_ID,
       ar.RESPONSE_VALUE,
       ar.SCORE
FROM   POQ_QUES_ACC_RESPONSES_VL ar
WHERE  ar.ACCEPTABLE_FLAG = 'Y'
  AND  ar.SCORE = (SELECT MAX(ar2.SCORE)
                   FROM   POQ_QUES_ACC_RESPONSES_VL ar2
                   WHERE  ar2.QUESTION_ID = ar.QUESTION_ID);
```

---

## 🔒 Observações

- Por ser uma view `_VL`, não deve ser utilizada para operações DML — utilizar as tabelas base `_B` e `_TL`.
- O campo `ACCEPTABLE_FLAG` permite distinguir entre respostas que são meramente opções (todas exibidas ao fornecedor) e respostas que efetivamente atendem ao critério de qualificação.
- Quando `DEFAULT_FLAG = 'Y'`, a opção é pré-selecionada na interface do questionário.
- O `SCORE` associado a cada resposta aceitável é utilizado para pontuação automática quando o `SCORING_TYPE` da pergunta em [[poq_questions_vl]] é `AUTOMATIC`.
- Apenas perguntas do tipo SINGLE_CHOICE e MULTI_CHOICE possuem registros nesta tabela.

---

## 🔗 PVOs Relacionados

### [[questionacceptableresponsespvo|QuestionAcceptableResponsesPVO]] (PO · BICC: 21/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | AccResponseId | ✅ |
| ATTACHMENT_ALLOWED_CODE | QuestionAcceptableResponseAttachmentAllowedCode | ✅ |
| ATTRIBUTE_CODE | QuestionAcceptableResponseAttributeCode | ✅ |
| ATTRIBUTE_CODE2 | QuestionAcceptableResponseAttributeCode2 | ✅ |
| ATTRIBUTE_ID | QuestionAcceptableResponseAttributeId | ✅ |
| CATEGORY_ID | QuestionAcceptableResponseCategoryId | ✅ |
| CATEGORY_NAME | QuestionAcceptableResponseCategoryName | ✅ |
| CREATED_BY | QuestionAcceptableResponseCreatedBy | ✅ |
| CREATION_DATE | QuestionAcceptableResponseCreationDate | ✅ |
| CRITICAL_RESPONSE_FLAG | CriticalResponseFlag | — |
| DISPLAY_SEQUENCE | QuestionAcceptableResponseDisplaySequence | ✅ |
| EXCLUDE_SCORING_FLAG | ExcludeScoringFlag | — |
| LAST_UPDATE_DATE | QuestionAcceptableResponseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionAcceptableResponseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionAcceptableResponseLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionAcceptableResponseObjectVersionNumber | ✅ |
| ORIGINAL_ACC_RESPONSE_ID | QuestionAcceptableResponseOriginalAccResponseId | ✅ |
| PARENT_CATEGORY_ID | QuestionAcceptableResponseParentCategoryId | ✅ |
| PREFERRED_RESPONSE_FLAG | QuestionAcceptableResponsePreferredResponseFlag | ✅ |
| PURCHASING_CAT_FLAG | QuestionAcceptableResponsePurchasingCatFlag | ✅ |
| QUESTION_ID | QuestionAcceptableResponseQuestionId | ✅ |
| RESPONSE_TEXT | QuestionAcceptableResponseResponseText | ✅ |
| SCORE | QuestionAcceptableResponseScore | ✅ |

### [[questionnaireresponsevaluespvo|QuestionnaireResponseValuesPVO]] (PO · BICC: 20/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | QuestionAccResponseAccResponseId | ✅ |
| ATTACHMENT_ALLOWED_CODE | QuestionAccResponseAttachmentAllowedCode | ✅ |
| ATTRIBUTE_CODE | QuestionAccResponseAttributeCode | ✅ |
| ATTRIBUTE_CODE2 | QuestionAccResponseAttributeCode2 | ✅ |
| ATTRIBUTE_ID | QuestionAccResponseAttributeId | ✅ |
| CATEGORY_ID | QuestionAccResponseCategoryId | ✅ |
| CATEGORY_NAME | QuestionAccResponseCategoryName | ✅ |
| CREATED_BY | QuestionAccResponseCreatedBy | ✅ |
| CREATION_DATE | QuestionAccResponseCreationDate | ✅ |
| DISPLAY_SEQUENCE | QuestionAccResponseDisplaySequence | ✅ |
| LAST_UPDATE_DATE | QuestionAccResponseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionAccResponseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionAccResponseLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionAccResponseObjectVersionNumber | ✅ |
| ORIGINAL_ACC_RESPONSE_ID | QuestionAccResponseOriginalAccResponseId | ✅ |
| PARENT_CATEGORY_ID | QuestionAccResponseParentCategoryId | ✅ |
| PREFERRED_RESPONSE_FLAG | QuestionAccResponsePreferredResponseFlag | ✅ |
| PURCHASING_CAT_FLAG | QuestionAccResponsePurchasingCatFlag | ✅ |
| QUESTION_ID | QuestionAccResponseQuestionId | ✅ |
| RESPONSE_TEXT | QuestionAccResponseResponseText | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
