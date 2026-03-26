---
id: DOC-PO-058
doc_type: system-doc
title: "POQ_QUESTNAIRE_RESP_SECTIONS — Seções de Respostas de Questionários"
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
  - response-sections
  - supplier-qualification
aliases:
  - POQ_QUESTNAIRE_RESP_SECTIONS
  - poq_questnaire_resp_sections
  - secoes-respostas-questionario
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTNAIRE_RESP_SECTIONS

## 📌 Visão Geral

Armazena as **seções de respostas** de questionários de qualificação de fornecedores. Cada registro representa uma seção temática (ex.: Capacidade Técnica, Saúde Financeira, Compliance) dentro de uma submissão de questionário, com a pontuação parcial daquela seção e status de completude. Permite análise granular por área de avaliação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação por seção:** Pontuação parcial por área temática do questionário.
- **Análise de lacunas:** Identificação de seções onde o fornecedor obteve baixa pontuação.
- **Completude de respostas:** Verificação de quais seções foram totalmente respondidas.
- **Relatórios segmentados:** Comparação de fornecedores por seção específica (ex.: todos os scores de Compliance).
- **Dashboard de qualificação:** Visualização gráfica de desempenho por área de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESP_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção de resposta | — | 🟡 70% |
| 2 | QUESTIONNAIRE_RESPONSE_ID | NUMBER(18) | NOT NULL | FK | Resposta do questionário à qual esta seção pertence | [[poq_questnaire_responses]] | 🟡 70% |
| 3 | RESPONSE_HEADER_ID | NUMBER(18) | NULL | FK | Cabeçalho da resposta (redundância para consultas diretas) | [[poq_questnaire_resp_headers]] | 🟡 60% |
| 4 | SECTION_ID | NUMBER(18) | NOT NULL | FK | Seção do questionário | — | 🟡 70% |
| 5 | SECTION_NAME | VARCHAR2(240) | NULL | Dados | Nome da seção (desnormalizado) | — | 🟡 60% |
| 6 | SECTION_SCORE | NUMBER | NULL | Pontuação | Pontuação obtida nesta seção | — | 🟡 65% |
| 7 | MAX_SECTION_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima possível na seção | — | 🟡 60% |
| 8 | PERCENTAGE_SCORE | NUMBER | NULL | Pontuação | Percentual da pontuação da seção | — | 🟡 55% |
| 9 | COMPLETION_STATUS | VARCHAR2(30) | NULL | Classificação | Status de completude: COMPLETE, PARTIAL, NOT_STARTED | — | 🟡 60% |
| 10 | TOTAL_QUESTIONS | NUMBER | NULL | Estatísticas | Total de perguntas na seção | — | 🟡 55% |
| 11 | ANSWERED_QUESTIONS | NUMBER | NULL | Estatísticas | Total de perguntas respondidas na seção | — | 🟡 55% |
| 12 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários do avaliador sobre a seção | — | 🟡 60% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questnaire_responses]] — via `QUESTIONNAIRE_RESPONSE_ID` (submissão do questionário)
- [[poq_questnaire_resp_headers]] — via `RESPONSE_HEADER_ID` (cabeçalho do processo)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Pontuação por seção de uma submissão
```sql
SELECT rs.SECTION_NAME,
       rs.SECTION_SCORE,
       rs.MAX_SECTION_SCORE,
       rs.PERCENTAGE_SCORE,
       rs.COMPLETION_STATUS,
       rs.ANSWERED_QUESTIONS || '/' || rs.TOTAL_QUESTIONS AS progresso
FROM   POQ_QUESTNAIRE_RESP_SECTIONS rs
WHERE  rs.QUESTIONNAIRE_RESPONSE_ID = :p_questionnaire_response_id
ORDER BY rs.SECTION_ID;
```

### Seções com pontuação abaixo de 50%
```sql
SELECT rs.QUESTIONNAIRE_RESPONSE_ID,
       rs.SECTION_NAME,
       rs.PERCENTAGE_SCORE
FROM   POQ_QUESTNAIRE_RESP_SECTIONS rs
WHERE  rs.PERCENTAGE_SCORE < 50
  AND  rs.COMPLETION_STATUS = 'COMPLETE';
```

---

## 🔒 Observações

- O `COMPLETION_STATUS` indica se todas as perguntas obrigatórias da seção foram respondidas: **COMPLETE**, **PARTIAL** (parcialmente respondido), **NOT_STARTED** (nenhuma resposta).
- Os campos `TOTAL_QUESTIONS` e `ANSWERED_QUESTIONS` permitem calcular o progresso de preenchimento por seção.
- O `PERCENTAGE_SCORE` é calculado como `SECTION_SCORE / MAX_SECTION_SCORE * 100`.
- Esta tabela é intermediária na hierarquia: [[poq_questnaire_resp_headers]] → [[poq_questnaire_responses]] → **POQ_QUESTNAIRE_RESP_SECTIONS** → [[poq_qual_responses]].
- A nomenclatura `QUESTNAIRE` (sem o 'i') segue a convenção Oracle original.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
