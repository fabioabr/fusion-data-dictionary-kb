---
id: DOC-HCM-240
doc_type: system-doc
title: "HRT_OBJ_RATING_DIST_B — Distribuicao de Ratings de Objetivos — Base"
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
  - rating-distribution
  - calibracao
  - desempenho
aliases:
  - HRT_OBJ_RATING_DIST_B
  - hrt_obj_rating_dist_b
  - hrt-obj-rating-dist-b
  - obj-rating-distribution
  - distribuicao-ratings-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_OBJ_RATING_DIST_B

## 📌 Visao Geral

Armazena a **distribuicao de ratings de objetivos** em processos de avaliacao de desempenho. Controla como os ratings sao distribuidos entre colaboradores em um periodo de avaliacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Calibracao:** Suportar processos de calibracao forcada de ratings.
- **Distribuicao forcada:** Aplicar curvas de distribuicao em avaliacoes de desempenho.
- **Analytics:** Analisar distribuicao de ratings por departamento/periodo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJ_RATING_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da distribuicao | — | 🟢 95% |
| 2 | REVIEW_PERIOD_ID | NUMBER(18) | NULL | FK | Periodo de avaliacao | [[hrt_review_periods_b]] | 🟢 90% |
| 3 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de rating | [[hrt_rating_levels_b]] | 🟢 90% |
| 4 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating | [[hrt_rating_models_b]] | 🟢 90% |
| 5 | TARGET_PERCENT | NUMBER | NULL | Dados | Percentual alvo da distribuicao | — | 🟡 80% |
| 6 | ACTUAL_COUNT | NUMBER | NULL | Dados | Quantidade real de colaboradores neste nivel | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_review_periods_b]] — via `REVIEW_PERIOD_ID` (periodo de avaliacao da distribuicao)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de classificacao na distribuicao)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de classificacao da distribuicao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Distribuicao de ratings por periodo
```sql
SELECT ord.RATING_LEVEL_ID, ord.TARGET_PERCENT,
       ord.ACTUAL_COUNT
FROM   HRT_OBJ_RATING_DIST_B ord
WHERE  ord.REVIEW_PERIOD_ID = :p_review_period_id;
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base.
- Usada em processos de calibracao forcada (forced ranking/bell curve).

---

## 📚 Referencias

- [Oracle Docs — HRT_OBJ_RATING_DIST_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtobjratingdistb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_FROM | ObjectRatingDistributionBPEODateFrom | — |
| DATE_TO | ObjectRatingDistributionBPEODateTo | — |
| OBJ_RATING_DIST_ID | ObjectRatingDistributionBPEOObjRatingDistId | — |
| OBJECT_ID | ObjectRatingDistributionBPEOObjectId | — |
| OBJECT_TYPE_CODE | ObjectRatingDistributionBPEOObjectTypeCode | — |
| RATING_MODEL_ID | ObjectRatingDistributionBPEORatingModelId | — |
