---
id: DOC-HCM-289
doc_type: system-doc
title: "HTS_SCHEDULES_ATRBS_VIEW — Atributos de Schedules (View)"
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
  - schedules
  - time-labor
  - atributos
aliases:
  - HTS_SCHEDULES_ATRBS_VIEW
  - hts_schedules_atrbs_view
  - hts-schedules-atrbs-view
  - schedules-atrbs-view
  - atributos-schedules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_SCHEDULES_ATRBS_VIEW

## 📌 Visao Geral

View que expoe os **atributos de schedules** (escalas de trabalho) para o modulo de Time and Labor.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Scheduling:** Visualizar atributos de escalas de trabalho.
- **Configuracao:** Consultar parametros de schedules.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_ID | NUMBER(18) | NOT NULL | PK | Identificador do schedule | — | 🟡 80% |
| 2 | SCHEDULE_NAME | VARCHAR2(240) | NULL | Dados | Nome do schedule | — | 🟡 80% |
| 3 | SCHEDULE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de schedule | — | 🟡 75% |
| 4 | START_DATE | DATE | NULL | Data | Data de inicio | — | 🟡 80% |
| 5 | END_DATE | DATE | NULL | Data | Data de fim | — | 🟡 80% |
| 6 | ATTRIBUTE_NAME | VARCHAR2(240) | NULL | Dados | Nome do atributo | — | 🟡 70% |
| 7 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 70% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data de criacao | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Atributos de um schedule
```sql
SELECT sa.ATTRIBUTE_NAME, sa.ATTRIBUTE_VALUE
FROM   HTS_SCHEDULES_ATRBS_VIEW sa
WHERE  sa.SCHEDULE_ID = :p_schedule_id;
```

---

## 🔒 Observacoes

- View somente leitura para consulta de metadados de schedules.

---

## 📚 Referencias

- [Oracle Docs — HTS_SCHEDULES_ATRBS_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htsschedulesatrbsview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
