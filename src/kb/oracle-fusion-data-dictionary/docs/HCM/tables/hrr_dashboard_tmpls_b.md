---
id: DOC-HCM-203
doc_type: system-doc
title: "HRR_DASHBOARD_TMPLS_B — Templates de Dashboard de Talent Review (Base)"
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
  - dashboard-templates
aliases:
  - HRR_DASHBOARD_TMPLS_B
  - hrr_dashboard_tmpls_b
  - templates-de-dashboard-de-talent-review-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_DASHBOARD_TMPLS_B

## 📌 Visão Geral

Tabela base dos **templates de dashboards** de Talent Review.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Templates reutilizáveis:** Layouts padrão.
- **Padronização:** Visualização consistente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TEMPLATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | TEMPLATE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |
| 4 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Templates ativos
```sql
SELECT t.TEMPLATE_ID, t.TEMPLATE_CODE
FROM   HRR_DASHBOARD_TMPLS_B t
WHERE  t.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrr_dashboard_tmpls_tl]].


---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
