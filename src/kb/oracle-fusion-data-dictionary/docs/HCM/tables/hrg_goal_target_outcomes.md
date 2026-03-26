---
id: DOC-HCM-176
doc_type: system-doc
title: "HRG_GOAL_TARGET_OUTCOMES — Resultados Esperados de Objetivos"
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
  - goals
  - outcomes
aliases:
  - HRG_GOAL_TARGET_OUTCOMES
  - hrg_goal_target_outcomes
  - resultados-esperados-de-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_TARGET_OUTCOMES

## 📌 Visão Geral

Armazena **resultados esperados (target outcomes)** de objetivos. Critérios de sucesso.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Critérios de sucesso:** O que significa atingir o objetivo.
- **Avaliação qualitativa:** Complementa métricas quantitativas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_TARGET_OUTCOME_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 90% |
| 3 | OUTCOME_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do resultado | — | 🟡 80% |
| 4 | OUTCOME_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (QUANTITATIVE, QUALITATIVE) | — | 🟡 70% |
| 5 | TARGET_VALUE | VARCHAR2(240) | NULL | Dados | Valor-alvo | — | 🟡 70% |
| 6 | ACTUAL_VALUE | VARCHAR2(240) | NULL | Dados | Valor realizado | — | 🟡 70% |
| 7 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (MET, NOT_MET, PARTIAL) | — | 🟡 65% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goals]] — via `GOAL_ID` (meta dos resultados esperados)

---

## 📎 Uso Típico

### Resultados esperados
```sql
SELECT t.OUTCOME_NAME, t.TARGET_VALUE, t.ACTUAL_VALUE, t.STATUS_CODE
FROM   HRG_GOAL_TARGET_OUTCOMES t
WHERE  t.GOAL_ID = :p_goal_id;
```

---

## 🔒 Observações

- Múltiplos resultados por objetivo.
- `STATUS_CODE`: MET, NOT_MET ou PARTIAL.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
