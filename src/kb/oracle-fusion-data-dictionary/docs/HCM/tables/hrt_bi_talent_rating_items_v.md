---
id: DOC-HCM-230
doc_type: system-doc
title: "HRT_BI_TALENT_RATING_ITEMS_V — Itens de Rating de Talento (BI View)"
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
  - bi-view
  - talent-rating
  - potencial
  - 9-box
aliases:
  - HRT_BI_TALENT_RATING_ITEMS_V
  - hrt_bi_talent_rating_items_v
  - hrt-bi-talent-rating-items-v
  - talent-rating-bi
  - rating-talento-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_TALENT_RATING_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **ratings de talento** (potencial) dos colaboradores. Complementa o rating de desempenho para compor a matriz 9-box (desempenho x potencial).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Construcao da matriz 9-box combinando performance e potencial.
- **Sucessao:** Identificacao de colaboradores de alto potencial (HiPo).
- **BI/Analytics:** Dashboards de distribuicao de talentos.

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
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de talento associado | [[hrt_profiles_b]] | 🟢 90% |
| 4 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo | [[hrt_content_types_b]] | 🟢 90% |
| 5 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating de talento | [[hrt_rating_models_b]] | 🟢 90% |
| 6 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de talento atribuido | [[hrt_rating_levels_b]] | 🟢 90% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da avaliacao | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim da avaliacao | — | 🟢 90% |
| 9 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do rating | — | 🟡 75% |
| 10 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentarios sobre o rating | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com avaliacao de talento registrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de talento)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Ratings de talento para matriz 9-box
```sql
SELECT tr.PERSON_ID, tr.RATING_LEVEL_ID,
       tr.DATE_FROM, tr.DATE_TO
FROM   HRT_BI_TALENT_RATING_ITEMS_V tr
WHERE  tr.PERSON_ID = :p_person_id
ORDER BY tr.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Talent rating representa o **potencial** do colaborador, diferente do performance rating.
- Usada em conjunto com HRT_BI_PERF_RATING_ITEMS_V para matriz 9-box.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_TALENT_RATING_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbitalentratingitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
