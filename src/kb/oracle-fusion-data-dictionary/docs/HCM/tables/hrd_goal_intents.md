---
id: DOC-HCM-163
doc_type: system-doc
title: "HRD_GOAL_INTENTS — Intenções de Objetivos de Desenvolvimento"
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
  - development
  - goals
  - intents
aliases:
  - HRD_GOAL_INTENTS
  - hrd_goal_intents
  - intenções-de-objetivos-de-desenvolvimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRD_GOAL_INTENTS

## 📌 Visão Geral

Armazena **intenções de objetivos** no módulo de Desenvolvimento. Relação entre objetivos e intenções de carreira.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento de carreira:** Vincula objetivos a intenções.
- **Desenvolvimento individual:** Alinha metas a aspirações.
- **Analytics de talento:** Análise de gaps.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_INTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 85% |
| 3 | INTENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (CAREER, SKILL, COMPETENCY) | — | 🟡 70% |
| 4 | INTENT_VALUE | VARCHAR2(240) | NULL | Dados | Valor da intenção | — | 🟡 65% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa | [[per_all_people_f]] | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrg_goals]] — via `GOAL_ID` (meta vinculada a intencao de desenvolvimento)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da intencao de desenvolvimento)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Intenções de um colaborador
```sql
SELECT gi.INTENT_TYPE, gi.INTENT_VALUE
FROM   HRD_GOAL_INTENTS gi
WHERE  gi.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Múltiplas intenções por objetivo.
- Utilizado com [[hrd_personal_intents]] para visão completa.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
