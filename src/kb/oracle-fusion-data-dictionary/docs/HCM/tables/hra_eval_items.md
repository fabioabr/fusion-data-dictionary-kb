---
id: DOC-HCM-140
doc_type: system-doc
title: "HRA_EVAL_ITEMS — Itens de Avaliação"
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
  - performance-management
  - eval-item
  - avaliacao
  - hra
aliases:
  - HRA_EVAL_ITEMS
  - hra_eval_items
  - hra-eval-items
  - DOC-HCM-140
  - itens-de-avaliação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVAL_ITEMS

## 📌 Visão Geral

Armazena os **registros de itens individuais de avaliação** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de itens individuais de avaliação:** Registro e controle operacional.
- **Workflow de avaliação:** Suporte ao processo de avaliação de performance.
- **Rastreabilidade:** Histórico completo de ações e decisões.
- **Relatórios de performance:** Dados para dashboards e análises.
- **Compliance:** Documentação de processos de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVAL_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 80% |
| 3 | EVALUATION_ID | NUMBER(18) | NULL | FK | Avaliação associada | [[hra_evaluations]] | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto | Descrição | — | 🟡 75% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do item de avaliacao)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao do item avaliado)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVAL_ITEM_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVAL_ITEMS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVAL_ITEM_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVAL_ITEMS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de itens individuais de avaliação.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 📚 Referências

- [Oracle Docs — HRA_EVAL_ITEMS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevalitems.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
