---
id: DOC-HCM-228
doc_type: system-doc
title: "HRT_BI_RISK_ITEMS_V — Itens de Risco de Perda de Talentos (BI View)"
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
  - risk
  - talent
  - retention
aliases:
  - HRT_BI_RISK_ITEMS_V
  - hrt_bi_risk_items_v
  - hrt-bi-risk-items-v
  - risk-loss-bi
  - risco-perda-talentos-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_RISK_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de risco de perda** (loss risk) dos colaboradores. Utilizada em processos de talent review para identificar colaboradores com risco elevado de desligamento.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Identificacao de colaboradores em risco de saida.
- **Retencao:** Subsidiar estrategias de retencao com dados de risco.
- **BI/Analytics:** Dashboards de risco de perda para gestao de talentos.

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
| 5 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating de risco | [[hrt_rating_models_b]] | 🟢 90% |
| 6 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de risco atribuido | [[hrt_rating_levels_b]] | 🟢 90% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da avaliacao de risco | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim da avaliacao de risco | — | 🟢 90% |
| 9 | IMPACT_OF_LOSS | VARCHAR2(30) | NULL | Classificacao | Impacto da perda do colaborador (HIGH, MEDIUM, LOW) | — | 🟡 75% |
| 10 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentarios sobre o risco | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa avaliada no item de risco)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de classificacao do risco atribuido)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Colaboradores com alto risco de perda
```sql
SELECT ri.PERSON_ID, ri.RATING_LEVEL_ID,
       ri.IMPACT_OF_LOSS, ri.DATE_FROM
FROM   HRT_BI_RISK_ITEMS_V ri
WHERE  ri.IMPACT_OF_LOSS = 'HIGH'
ORDER BY ri.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- O campo `IMPACT_OF_LOSS` indica o impacto organizacional caso o colaborador saia.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_RISK_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbiriskitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
