---
id: DOC-HCM-194
doc_type: system-doc
title: "HRQ_QUESTIONNAIRES_B — Questionários (Base)"
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
aliases:
  - HRQ_QUESTIONNAIRES_B
  - hrq_questionnaires_b
  - questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QUESTIONNAIRES_B

## 📌 Visão Geral

Tabela base dos **questionários** HCM. Configurações, status e período.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição:** Registro central de cada questionário.
- **Ciclo de vida:** Controle de status.
- **Período:** Datas de abertura e encerramento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | QUESTIONNAIRE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟢 85% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[hrq_categories_b]] | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (DRAFT, PUBLISHED, CLOSED) | — | 🟢 85% |
| 5 | START_DATE | DATE | NULL | Data | Abertura | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Data | Encerramento | — | 🟡 80% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Questionários publicados
```sql
SELECT q.QUESTIONNAIRE_ID, q.QUESTIONNAIRE_CODE, q.STATUS_CODE
FROM   HRQ_QUESTIONNAIRES_B q
WHERE  q.STATUS_CODE = 'PUBLISHED';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_questionnaires_tl]].
Ciclo: DRAFT -> PUBLISHED -> CLOSED.
- Tabela central do módulo de questionários.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
