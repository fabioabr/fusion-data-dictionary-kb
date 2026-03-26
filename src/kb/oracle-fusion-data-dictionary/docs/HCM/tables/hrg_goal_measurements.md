---
id: DOC-HCM-168
doc_type: system-doc
title: "HRG_GOAL_MEASUREMENTS — Métricas de Objetivos"
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
  - measurements
aliases:
  - HRG_GOAL_MEASUREMENTS
  - hrg_goal_measurements
  - métricas-de-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_MEASUREMENTS

## 📌 Visão Geral

Armazena **métricas e indicadores** de objetivos. Valores-alvo, atuais e unidades de medida.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Mensuração:** Critérios quantitativos de progresso.
- **KPIs individuais:** Indicadores por meta.
- **Acompanhamento automatizado:** Progresso numérico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_MEASUREMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo | [[hrg_goals]] | 🟢 90% |
| 3 | MEASUREMENT_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da métrica | — | 🟡 80% |
| 4 | TARGET_VALUE | NUMBER | NULL | Métrica | Valor-alvo | — | 🟡 80% |
| 5 | ACTUAL_VALUE | NUMBER | NULL | Métrica | Valor atual | — | 🟡 80% |
| 6 | UOM_CODE | VARCHAR2(30) | NULL | Classificação | Unidade de medida | — | 🟡 70% |
| 7 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 8 | TARGET_DATE | DATE | NULL | Data | Data-alvo | — | 🟡 75% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goals]] — via `GOAL_ID` (meta da medicao de progresso)

---

## 📎 Uso Típico

### Métricas e progresso
```sql
SELECT m.MEASUREMENT_NAME, m.TARGET_VALUE, m.ACTUAL_VALUE,
       ROUND(m.ACTUAL_VALUE/NULLIF(m.TARGET_VALUE,0)*100,1) AS pct
FROM   HRG_GOAL_MEASUREMENTS m
WHERE  m.GOAL_ID = :p_goal_id;
```

---

## 🔒 Observações

- Múltiplas métricas por objetivo.
- Progresso = `ACTUAL_VALUE / TARGET_VALUE * 100`.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
