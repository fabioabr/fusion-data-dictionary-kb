---
id: DOC-HCM-193
doc_type: system-doc
title: "HRQ_QSTN_RESPONSES — Respostas por Questão"
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
  - questionnaires
  - responses
aliases:
  - HRQ_QSTN_RESPONSES
  - hrq_qstn_responses
  - respostas-por-questão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTN_RESPONSES

## 📌 Visão Geral

Armazena **respostas individuais por questão**. Cada registro = um participante + uma questão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro granular:** Resposta por questão e participante.
- **Análise detalhada:** Questão a questão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QSTN_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Questão | [[hrq_questions_b]] | 🟢 90% |
| 3 | PARTICIPANT_ID | NUMBER(18) | NOT NULL | FK | Participante | [[hrq_qstnr_participants]] | 🟢 85% |
| 4 | ANSWER_ID | NUMBER(18) | NULL | FK | Resposta selecionada | [[hrq_qstn_answers_b]] | 🟡 80% |
| 5 | FREE_TEXT_RESPONSE | VARCHAR2(4000) | NULL | Texto livre | Resposta em texto livre | — | 🟡 70% |
| 6 | NUMERIC_RESPONSE | NUMBER | NULL | Métrica | Resposta numérica | — | 🟡 65% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai

---

## 📎 Uso Típico

### Respostas de uma questão
```sql
SELECT qr.PARTICIPANT_ID, qr.ANSWER_ID, qr.FREE_TEXT_RESPONSE
FROM   HRQ_QSTN_RESPONSES qr
WHERE  qr.QUESTION_ID = :p_id;
```

---

## 🔒 Observações

- Suporta múltipla escolha, texto livre e numérico.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
