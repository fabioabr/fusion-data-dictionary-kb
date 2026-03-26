---
id: DOC-HCM-202
doc_type: system-doc
title: "HRR_DASHBOARDS — Dashboards de Talent Review"
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
  - talent-review
  - dashboards
aliases:
  - HRR_DASHBOARDS
  - hrr_dashboards
  - dashboards-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_DASHBOARDS

## 📌 Visão Geral

Armazena **dashboards** de Talent Review. Configurados para reuniões de revisão de talentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração:** Dashboards de talent review.
- **Visualização:** Análise de pool de talentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DASHBOARD_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | DASHBOARD_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do dashboard | — | 🟡 80% |
| 3 | TEMPLATE_ID | NUMBER(18) | NULL | FK | Template | [[hrr_dashboard_tmpls_b]] | 🟡 80% |
| 4 | OWNER_PERSON_ID | NUMBER(18) | NULL | FK | Owner | [[per_all_people_f]] | 🟡 75% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboard_tmpls_b]] — via `TEMPLATE_ID` (template do dashboard de talent review)

### Tabelas-filha

---

## 📎 Uso Típico

### Dashboards ativos
```sql
SELECT d.DASHBOARD_ID, d.DASHBOARD_NAME, d.STATUS_CODE
FROM   HRR_DASHBOARDS d
WHERE  d.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Dashboards configuram a visualização de Talent Review.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
