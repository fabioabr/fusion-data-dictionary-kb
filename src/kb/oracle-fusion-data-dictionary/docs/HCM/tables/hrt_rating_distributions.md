---
id: DOC-HCM-260
doc_type: system-doc
title: "HRT_RATING_DISTRIBUTIONS — Distribuicoes de Rating"
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
  - rating-distributions
  - calibracao
  - desempenho
aliases:
  - HRT_RATING_DISTRIBUTIONS
  - hrt_rating_distributions
  - hrt-rating-distributions
  - rating-distributions
  - distribuicoes-rating
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_DISTRIBUTIONS

## 📌 Visao Geral

Armazena as **distribuicoes de rating** para processos de avaliacao de desempenho. Define os percentuais-alvo de cada nivel de rating (curva de distribuicao forcada/bell curve).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Calibracao:** Definir curvas de distribuicao para calibracao de ratings.
- **Performance Management:** Garantir distribuicao balanceada de ratings.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador da distribuicao | — | 🟢 95% |
| 2 | RATING_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de rating | [[hrt_rating_models_b]] | 🟢 90% |
| 3 | RATING_LEVEL_ID | NUMBER(18) | NOT NULL | FK | Nivel de rating | [[hrt_rating_levels_b]] | 🟢 90% |
| 4 | TARGET_PERCENT | NUMBER | NULL | Dados | Percentual alvo | — | 🟡 80% |
| 5 | MIN_PERCENT | NUMBER | NULL | Dados | Percentual minimo | — | 🟡 75% |
| 6 | MAX_PERCENT | NUMBER | NULL | Dados | Percentual maximo | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de classificacao da distribuicao)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de classificacao na distribuicao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Curva de distribuicao
```sql
SELECT rd.RATING_LEVEL_ID, rd.TARGET_PERCENT,
       rd.MIN_PERCENT, rd.MAX_PERCENT
FROM   HRT_RATING_DISTRIBUTIONS rd
WHERE  rd.RATING_MODEL_ID = :p_rating_model_id;
```

---

## 🔒 Observacoes

- Usada para configurar bell curves de calibracao.
- TARGET_PERCENT, MIN_PERCENT e MAX_PERCENT definem a faixa aceitavel.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_DISTRIBUTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratingdistributions.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
