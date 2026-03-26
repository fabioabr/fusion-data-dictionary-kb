---
id: DOC-HCM-226
doc_type: system-doc
title: "HRT_BI_PERF_RATING_ITEMS_V — Itens de Avaliacao de Desempenho (BI View)"
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
  - performance
  - talent
  - bi-view
  - ratings
aliases:
  - HRT_BI_PERF_RATING_ITEMS_V
  - hrt_bi_perf_rating_items_v
  - hrt-bi-perf-rating-items-v
  - performance-ratings-bi
  - avaliacao-desempenho-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_PERF_RATING_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de avaliacao de desempenho** (performance ratings) dos colaboradores. Consolida dados de ratings de performance para consumo por ferramentas de analytics e relatorios gerenciais.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Analise de desempenho:** Extracao de ratings de performance para dashboards de RH.
- **Talent Review:** Alimentacao de processos de revisao de talentos com dados historicos de performance.
- **BI/Analytics:** Fonte de dados para OTBI e relatorios customizados de desempenho.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de conteudo | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador avaliado | [[per_all_people_f]] | 🟢 95% |
| 3 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de talento associado | [[hrt_profiles_b]] | 🟢 90% |
| 4 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating utilizado | [[hrt_rating_models_b]] | 🟢 90% |
| 5 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de rating atribuido | [[hrt_rating_levels_b]] | 🟢 90% |
| 6 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo do item | [[hrt_content_types_b]] | 🟢 90% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da avaliacao | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim da avaliacao | — | 🟢 90% |
| 9 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do rating (e.g., MANUAL, SYSTEM) | — | 🟡 75% |
| 10 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentarios sobre a avaliacao | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador avaliado)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de rating)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Ratings de desempenho por colaborador
```sql
SELECT pi.PERSON_ID, pi.RATING_LEVEL_ID,
       pi.DATE_FROM, pi.DATE_TO
FROM   HRT_BI_PERF_RATING_ITEMS_V pi
WHERE  pi.PERSON_ID = :p_person_id
ORDER BY pi.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura otimizada para BI — nao deve ser usada para operacoes transacionais.
- Os dados refletem o ultimo snapshot de performance registrado no perfil de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_PERF_RATING_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbiperfratingitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
