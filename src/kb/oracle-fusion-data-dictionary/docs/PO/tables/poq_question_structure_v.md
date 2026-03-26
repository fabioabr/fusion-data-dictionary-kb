---
id: DOC-PO-054
doc_type: system-doc
title: "POQ_QUESTION_STRUCTURE_V — Estrutura Hierárquica de Perguntas (View)"
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
  - question-structure
  - hierarquia-perguntas
aliases:
  - POQ_QUESTION_STRUCTURE_V
  - poq_question_structure_v
  - estrutura-perguntas-qualificacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTION_STRUCTURE_V

## 📌 Visão Geral

View que expõe a **estrutura hierárquica** das perguntas dentro de questionários de qualificação de fornecedores. Permite visualizar o agrupamento de perguntas em seções e subseções, a ordem de apresentação e as dependências entre perguntas (perguntas condicionais). Facilita a navegação pela árvore de perguntas de cada questionário.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view** (não é tabela física). Normalmente consolida dados de múltiplas tabelas para simplificar consultas sobre a estrutura de questionários.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Renderização de questionários:** Definição da ordem e hierarquia de exibição das perguntas ao fornecedor.
- **Perguntas condicionais:** Mapeamento de dependências entre perguntas (exibir pergunta B apenas se a resposta de A for X).
- **Navegação por seções:** Agrupamento lógico de perguntas em seções temáticas (ex.: Financeiro, Técnico, Compliance).
- **Validação de completude:** Verificação se todas as perguntas obrigatórias de cada seção foram respondidas.
- **Design de questionários:** Interface de configuração para montagem da estrutura do questionário.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_STRUCTURE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da estrutura | — | 🟡 65% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário ao qual a estrutura pertence | [[poq_questnaires_vl]] | 🟡 70% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Pergunta posicionada nesta estrutura | [[poq_questions_vl]] | 🟡 70% |
| 4 | SECTION_ID | NUMBER(18) | NULL | FK | Seção à qual a pergunta pertence | — | 🟡 65% |
| 5 | SECTION_NAME | VARCHAR2(240) | NULL | Dados | Nome da seção (traduzido) | — | 🟡 60% |
| 6 | PARENT_QUESTION_ID | NUMBER(18) | NULL | FK | Pergunta-pai (para perguntas condicionais/aninhadas) | [[poq_questions_vl]] | 🟡 60% |
| 7 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição dentro da seção | — | 🟡 70% |
| 8 | LEVEL_NUMBER | NUMBER | NULL | Hierarquia | Nível hierárquico da pergunta (1 = raiz) | — | 🟡 55% |
| 9 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Configuração | Herança de obrigatoriedade na estrutura (Y/N) | — | 🟡 60% |
| 10 | CONDITION_TYPE | VARCHAR2(30) | NULL | Regra | Tipo de condição para exibição: ALWAYS, IF_EQUALS, IF_CONTAINS | — | 🔴 50% |
| 11 | CONDITION_VALUE | VARCHAR2(4000) | NULL | Regra | Valor que aciona a exibição condicional | — | 🔴 50% |
| 12 | QUESTION_TEXT | VARCHAR2(4000) | NULL | Dados | Texto da pergunta (desnormalizado da view de perguntas) | — | 🟡 60% |
| 13 | QUESTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de resposta esperado (desnormalizado) | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questnaires_vl]] — via `QUESTIONNAIRE_ID` (questionário da estrutura de perguntas)
- [[poq_questions_vl]] — via `QUESTION_ID` e `PARENT_QUESTION_ID` (perguntas)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Estrutura completa de um questionário
```sql
SELECT qs.SECTION_NAME,
       qs.DISPLAY_ORDER,
       qs.QUESTION_TEXT,
       qs.QUESTION_TYPE,
       qs.MANDATORY_FLAG,
       qs.LEVEL_NUMBER
FROM   POQ_QUESTION_STRUCTURE_V qs
WHERE  qs.QUESTIONNAIRE_ID = :p_questionnaire_id
ORDER BY qs.SECTION_ID, qs.DISPLAY_ORDER;
```

### Perguntas condicionais (dependentes de outra)
```sql
SELECT qs.QUESTION_ID,
       qs.QUESTION_TEXT,
       qs.PARENT_QUESTION_ID,
       qs.CONDITION_TYPE,
       qs.CONDITION_VALUE
FROM   POQ_QUESTION_STRUCTURE_V qs
WHERE  qs.PARENT_QUESTION_ID IS NOT NULL
  AND  qs.QUESTIONNAIRE_ID = :p_questionnaire_id;
```

---

## 🔒 Observações

- Por ser uma view (`_V`), não suporta operações DML diretas. Alterações na estrutura devem ser feitas nas tabelas base subjacentes.
- Os campos `CONDITION_TYPE` e `CONDITION_VALUE` (confiança baixa) podem não estar presentes em todos os releases — validar no ambiente.
- O campo `LEVEL_NUMBER` permite a construção de árvores hierárquicas de perguntas (pergunta-mãe → sub-perguntas).
- Campos desnormalizados como `QUESTION_TEXT` e `QUESTION_TYPE` evitam joins adicionais com [[poq_questions_vl]] para cenários de leitura.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
