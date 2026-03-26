---
id: DOC-HCM-261
doc_type: system-doc
title: "HRT_RATING_LEVELS_B — Niveis de Rating — Base"
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
  - rating-levels
  - configuracao
  - talent
aliases:
  - HRT_RATING_LEVELS_B
  - hrt_rating_levels_b
  - hrt-rating-levels-b
  - rating-levels-base
  - niveis-rating-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_RATING_LEVELS_B

## 📌 Visao Geral

Tabela base que define os **niveis de rating** dentro de cada modelo — como "Exceeds Expectations", "Meets Expectations". Cada nivel tem valor numerico e sequencia.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Avaliacao:** Definir os niveis disponiveis para avaliacao.
- **Configuracao:** Cada modelo possui seus proprios niveis.
- **Analytics:** Base para analise de distribuicao de avaliacoes.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RATING_LEVEL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do nivel | — | 🟢 100% |
| 2 | RATING_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de rating | [[hrt_rating_models_b]] | 🟢 100% |
| 3 | STEP_VALUE | NUMBER | NOT NULL | Dados | Valor numerico do nivel | — | 🟢 95% |
| 4 | FROM_VALUE | NUMBER | NULL | Dados | Valor inferior da faixa | — | 🟡 80% |
| 5 | TO_VALUE | NUMBER | NULL | Dados | Valor superior da faixa | — | 🟡 80% |
| 6 | SEQUENCE | NUMBER | NULL | Dados | Ordem de exibicao | — | 🟢 90% |
| 7 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio | — | 🟢 95% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de classificacao do nivel)

### Tabelas-filha (FK de saida)
- [[hrt_rating_levels_tl]] — via `RATING_LEVEL_ID` (traducoes do nivel de classificacao)
- [[hrt_profile_items]] — via `RATING_LEVEL_ID` (traducoes do nivel de classificacao)

---

## 📎 Uso Tipico

### Niveis de um modelo
```sql
SELECT rl.RATING_LEVEL_ID, rl.STEP_VALUE, rl.SEQUENCE
FROM   HRT_RATING_LEVELS_B rl
WHERE  rl.RATING_MODEL_ID = :p_rating_model_id
ORDER BY rl.SEQUENCE;
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_rating_levels_tl]].
- STEP_VALUE e o valor numerico; SEQUENCE define a ordem de exibicao.

---

## 📚 Referencias

- [Oracle Docs — HRT_RATING_LEVELS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtratinglevelsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
