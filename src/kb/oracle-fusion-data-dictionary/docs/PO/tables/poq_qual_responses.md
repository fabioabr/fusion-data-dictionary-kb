---
id: DOC-PO-051
doc_type: system-doc
title: "POQ_QUAL_RESPONSES — Respostas de Qualificação de Fornecedores"
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
  - qualification-responses
  - supplier-qualification
aliases:
  - POQ_QUAL_RESPONSES
  - poq_qual_responses
  - respostas-qualificacao-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_RESPONSES

## 📌 Visão Geral

Armazena as **respostas de qualificação** fornecidas por fornecedores ou avaliadores internos durante processos de qualificação no módulo de Procurement. Cada registro representa uma resposta individual a uma pergunta de qualificação, incluindo o valor da resposta, pontuação atribuída e metadados de submissão.

> [!note] Contexto POQ
> O prefixo `POQ` indica tabelas do submódulo **Supplier Qualification Management** (SQM) do Oracle Fusion Procurement, responsável por avaliações e qualificações de fornecedores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação de fornecedores:** Registro das respostas dadas a perguntas de qualificação definidas pelo comprador.
- **Scoring de qualificação:** Base para cálculo de pontuação e ranking de fornecedores.
- **Compliance de fornecedores:** Verificação de conformidade com requisitos mínimos de qualificação.
- **Histórico de avaliações:** Rastreabilidade das respostas ao longo do tempo para auditorias.
- **Relatórios de procurement:** Análise comparativa de fornecedores com base em respostas de qualificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da resposta de qualificação | — | 🟡 75% |
| 2 | QUESTIONNAIRE_RESPONSE_ID | NUMBER(18) | NOT NULL | FK | Referência ao cabeçalho de respostas do questionário | [[poq_questnaire_responses]] | 🟡 75% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Pergunta à qual esta resposta se refere | [[poq_questions_vl]] | 🟡 75% |
| 4 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Dados | Valor textual da resposta fornecida | — | 🟡 70% |
| 5 | RESPONSE_NUMBER | NUMBER | NULL | Dados | Valor numérico da resposta (quando aplicável) | — | 🟡 65% |
| 6 | RESPONSE_DATE | DATE | NULL | Dados | Valor de data da resposta (quando aplicável) | — | 🟡 65% |
| 7 | SCORE | NUMBER | NULL | Pontuação | Pontuação atribuída à resposta | — | 🟡 70% |
| 8 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários adicionais sobre a resposta | — | 🟡 65% |
| 9 | SUPPLIER_ID | NUMBER(18) | NULL | FK | Fornecedor que submeteu a resposta | [[ap_suppliers]] | 🟡 65% |
| 10 | QUALIFICATION_ID | NUMBER(18) | NULL | FK | Qualificação à qual a resposta pertence | — | 🟡 65% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questnaire_responses]] — via `QUESTIONNAIRE_RESPONSE_ID` (cabeçalho de respostas do questionário)
- [[poq_questions_vl]] — via `QUESTION_ID` (pergunta de qualificação)
- [[ap_suppliers]] — via `SUPPLIER_ID` (fornecedor avaliado)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Respostas de qualificação por fornecedor
```sql
SELECT qr.QUAL_RESPONSE_ID,
       qr.QUESTION_ID,
       qr.RESPONSE_VALUE,
       qr.SCORE,
       qr.COMMENTS
FROM   POQ_QUAL_RESPONSES qr
WHERE  qr.SUPPLIER_ID = :p_supplier_id
  AND  qr.QUESTIONNAIRE_RESPONSE_ID = :p_questionnaire_response_id;
```

### Média de pontuação por questionário
```sql
SELECT qr.QUESTIONNAIRE_RESPONSE_ID,
       AVG(qr.SCORE) AS media_score,
       COUNT(*) AS total_respostas
FROM   POQ_QUAL_RESPONSES qr
WHERE  qr.SCORE IS NOT NULL
GROUP BY qr.QUESTIONNAIRE_RESPONSE_ID;
```

---

## 🔒 Observações

- As respostas podem ser de diferentes tipos (texto, número, data) dependendo da configuração da pergunta em [[poq_questions_vl]].
- O campo `SCORE` pode ser calculado automaticamente com base em regras de pontuação definidas em [[poq_question_scores]].
- Esta tabela é parte do fluxo de **Supplier Qualification Management** (SQM) do Oracle Fusion Procurement.
- Para análise consolidada de qualificações, combinar com [[poq_questnaire_resp_headers]] e [[poq_questnaire_resp_sections]].

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
