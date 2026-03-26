---
id: DOC-HCM-215
doc_type: system-doc
title: "HRR_TMPL_METRIC_CONFIG — Configuração de Métricas de Template"
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
  - metrics
aliases:
  - HRR_TMPL_METRIC_CONFIG
  - hrr_tmpl_metric_config
  - configuração-de-métricas-de-template
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_TMPL_METRIC_CONFIG

## 📌 Visão Geral

Armazena **configuração de métricas** em templates de dashboard de Talent Review.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de KPIs:** Métricas nos dashboards.
- **Personalização:** Métricas exibidas e cálculos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | METRIC_CONFIG_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template | [[hrr_dashboard_tmpls_b]] | 🟢 85% |
| 3 | METRIC_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da métrica | — | 🟡 80% |
| 4 | DISPLAY_SEQUENCE | NUMBER | NULL | Ordenação | Ordem | — | 🟡 70% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativa (Y/N) | — | 🟡 70% |
| 6 | METRIC_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (COUNT, PERCENTAGE, AVERAGE) | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboard_tmpls_b]] — via `TEMPLATE_ID` (template da configuracao de metrica)

---

## 📎 Uso Típico

### Métricas configuradas
```sql
SELECT mc.METRIC_CODE, mc.METRIC_TYPE, mc.DISPLAY_SEQUENCE
FROM   HRR_TMPL_METRIC_CONFIG mc
WHERE  mc.TEMPLATE_ID = :p_id AND NVL(mc.ENABLED_FLAG,'Y') = 'Y'
ORDER BY mc.DISPLAY_SEQUENCE;
```

---

## 🔒 Observações

- `METRIC_TYPE` determina cálculo do valor.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
