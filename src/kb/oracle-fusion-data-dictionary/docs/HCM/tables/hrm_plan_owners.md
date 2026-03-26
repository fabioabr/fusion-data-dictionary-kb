---
id: DOC-HCM-180
doc_type: system-doc
title: "HRM_PLAN_OWNERS — Responsáveis por Planos de Sucessão"
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
  - succession
  - owners
aliases:
  - HRM_PLAN_OWNERS
  - hrm_plan_owners
  - responsáveis-por-planos-de-sucessão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLAN_OWNERS

## 📌 Visão Geral

Armazena **responsáveis (owners)** dos planos de sucessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Governça:** Quem é responsável.
- **Accountability:** Responsáveis identificados.
- **Notificações:** Alertas aos owners.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_OWNER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrm_plans_v]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Responsável | [[per_all_people_f]] | 🟢 90% |
| 4 | OWNER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (PRIMARY, SECONDARY) | — | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrm_plans_v]] — via `PLAN_ID` (plano de sucessao do proprietario)
- [[per_all_people_f]] — via `PERSON_ID` (proprietario do plano de sucessao)

---

## 📎 Uso Típico

### Owners de um plano
```sql
SELECT po.PERSON_ID, po.OWNER_TYPE
FROM   HRM_PLAN_OWNERS po
WHERE  po.PLAN_ID = :p_id;
```

---

## 🔒 Observações

- Múltiplos owners por plano.
- Owner primário = principal responsável.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
