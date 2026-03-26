---
id: DOC-HCM-210
doc_type: system-doc
title: "HRR_TMPL_ANALYTIC_TYPES_B — Tipos Analíticos de Template (Base)"
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
  - analytics
aliases:
  - HRR_TMPL_ANALYTIC_TYPES_B
  - hrr_tmpl_analytic_types_b
  - tipos-analíticos-de-template-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_TMPL_ANALYTIC_TYPES_B

## 📌 Visão Geral

Tabela base dos **tipos analíticos** de templates de Talent Review (9-Box, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração:** Tipos de análise (9-Box, Performance Grid).
- **Dimensões analíticas:** Eixos e categorizações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ANALYTIC_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template de dashboard | [[hrr_dashboard_tmpls_b]] | 🟢 85% |
| 3 | ANALYTIC_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do tipo | — | 🟡 80% |
| 4 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboard_tmpls_b]] — via `TEMPLATE_ID` (template do tipo analitico de talent review)

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Tipos analíticos
```sql
SELECT at_.ANALYTIC_TYPE_ID, at_.ANALYTIC_TYPE_CODE
FROM   HRR_TMPL_ANALYTIC_TYPES_B at_
WHERE  at_.TEMPLATE_ID = :p_id;
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrr_tmpl_analytic_types_tl]].


---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
