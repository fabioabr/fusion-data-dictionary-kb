---
id: DOC-PO-052
doc_type: system-doc
title: "POQ_QUESTIONS_VL — Perguntas de Questionários de Qualificação (View Traduzida)"
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
  - questions
  - supplier-qualification
aliases:
  - POQ_QUESTIONS_VL
  - poq_questions_vl
  - perguntas-qualificacao-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTIONS_VL

## 📌 Visão Geral

View traduzida que expõe as **perguntas de questionários de qualificação** de fornecedores no módulo de Procurement. Combina as tabelas base (`_B`) e de tradução (`_TL`) para fornecer os textos das perguntas no idioma da sessão do usuário. Cada registro representa uma pergunta individual com seu tipo, texto, obrigatoriedade e configuração de pontuação.

> [!note] Sufixo _VL
> O sufixo `_VL` (View Language) indica uma **view multilíngue** que junta automaticamente a tabela base com a tabela de tradução, retornando os textos no idioma da sessão do usuário (`USERENV('LANG')`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de questionários:** Cadastro das perguntas que compõem questionários de qualificação de fornecedores.
- **Avaliação de fornecedores:** Exibição das perguntas durante o preenchimento do questionário pelo fornecedor ou avaliador.
- **Configuração de scoring:** Definição do tipo de resposta esperado e peso da pergunta na pontuação total.
- **Relatórios multilíngues:** Exibição de perguntas traduzidas conforme o idioma do usuário.
- **Compliance:** Perguntas obrigatórias que determinam requisitos mínimos de qualificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pergunta | — | 🟡 75% |
| 2 | QUESTION_TEXT | VARCHAR2(4000) | NOT NULL | Dados | Texto da pergunta traduzido no idioma da sessão | — | 🟡 70% |
| 3 | QUESTION_CODE | VARCHAR2(100) | NULL | Identificação | Código mnemônico da pergunta | — | 🟡 65% |
| 4 | QUESTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da pergunta: TEXT, NUMBER, DATE, SINGLE_CHOICE, MULTI_CHOICE | — | 🟡 70% |
| 5 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se a resposta é obrigatória (Y/N) | — | 🟡 70% |
| 6 | SCORING_TYPE | VARCHAR2(30) | NULL | Pontuação | Tipo de pontuação: MANUAL, AUTOMATIC, NONE | — | 🟡 65% |
| 7 | MAX_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima possível para esta pergunta | — | 🟡 65% |
| 8 | WEIGHT | NUMBER | NULL | Pontuação | Peso da pergunta no cálculo da pontuação total | — | 🟡 65% |
| 9 | SECTION_ID | NUMBER(18) | NULL | FK | Seção do questionário à qual a pergunta pertence | — | 🟡 60% |
| 10 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição da pergunta no questionário | — | 🟡 65% |
| 11 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição ou instrução adicional da pergunta (traduzida) | — | 🟡 65% |
| 12 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 13 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma-fonte da tradução | — | 🟢 90% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-filha (FK de saída)
- [[poq_qual_responses]] — via `QUESTION_ID` (respostas fornecidas a esta pergunta)
- [[poq_question_scores]] — via `QUESTION_ID` (regras de pontuação)
- [[poq_question_structure_v]] — via `QUESTION_ID` (estrutura hierárquica)
- [[poq_ques_acc_responses_vl]] — via `QUESTION_ID` (respostas aceitáveis)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Listar perguntas de um questionário
```sql
SELECT q.QUESTION_ID,
       q.QUESTION_TEXT,
       q.QUESTION_TYPE,
       q.MANDATORY_FLAG,
       q.MAX_SCORE,
       q.WEIGHT,
       q.DISPLAY_ORDER
FROM   POQ_QUESTIONS_VL q
WHERE  q.SECTION_ID = :p_section_id
ORDER BY q.DISPLAY_ORDER;
```

### Perguntas obrigatórias com pontuação automática
```sql
SELECT q.QUESTION_ID,
       q.QUESTION_TEXT,
       q.SCORING_TYPE,
       q.MAX_SCORE
FROM   POQ_QUESTIONS_VL q
WHERE  q.MANDATORY_FLAG = 'Y'
  AND  q.SCORING_TYPE = 'AUTOMATIC';
```

---

## 🔒 Observações

- Por ser uma view `_VL`, não deve ser utilizada para operações DML — utilizar as tabelas base `_B` e `_TL` para inserções e atualizações.
- O `QUESTION_TYPE` determina o formato de resposta esperado e a interface apresentada ao fornecedor.
- Perguntas com `SCORING_TYPE = 'AUTOMATIC'` calculam a pontuação com base nas regras de [[poq_question_scores]].
- O campo `WEIGHT` permite ponderação diferenciada entre perguntas no cálculo da nota final do questionário.
- Recomenda-se sempre filtrar pelo `LANGUAGE` desejado quando acessar diretamente, embora a view já filtre por `USERENV('LANG')`.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
