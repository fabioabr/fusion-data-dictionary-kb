---
id: DOC-HCM-267
doc_type: system-doc
title: "HRT_REVIEW_PERIODS_B — Periodos de Avaliacao — Base"
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
  - review-periods
  - performance
  - avaliacao
aliases:
  - HRT_REVIEW_PERIODS_B
  - hrt_review_periods_b
  - hrt-review-periods-b
  - review-periods-base
  - periodos-avaliacao-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_REVIEW_PERIODS_B

## 📌 Visao Geral

Tabela base que define os **periodos de avaliacao** (review periods) para processos de performance management. Cada periodo determina o intervalo temporal de um ciclo de avaliacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Performance Management:** Definir ciclos de avaliacao (anual, semestral).
- **Calibracao:** Associar processos de calibracao a periodos.
- **Historico:** Rastrear avaliacoes por periodo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REVIEW_PERIOD_ID | NUMBER(18) | NOT NULL | PK | Identificador do periodo | — | 🟢 95% |
| 2 | REVIEW_PERIOD_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do periodo | — | 🟢 90% |
| 3 | PERIOD_START_DATE | DATE | NOT NULL | Data | Data de inicio do periodo | — | 🟢 95% |
| 4 | PERIOD_END_DATE | DATE | NOT NULL | Data | Data de fim do periodo | — | 🟢 95% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do periodo (ACTIVE, CLOSED) | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hrt_review_periods_tl]] — via `REVIEW_PERIOD_ID` (traducoes do periodo de avaliacao)
- [[hrt_obj_rating_dist_b]] — via `REVIEW_PERIOD_ID` (traducoes do periodo de avaliacao)

---

## 📎 Uso Tipico

### Periodos de avaliacao ativos
```sql
SELECT rp.REVIEW_PERIOD_ID, rp.REVIEW_PERIOD_CODE,
       rp.PERIOD_START_DATE, rp.PERIOD_END_DATE
FROM   HRT_REVIEW_PERIODS_B rp
WHERE  rp.STATUS = 'ACTIVE';
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_review_periods_tl]].
- Periodos definem o timeframe de ciclos de avaliacao.

---

## 📚 Referencias

- [Oracle Docs — HRT_REVIEW_PERIODS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtreviewperiodsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
