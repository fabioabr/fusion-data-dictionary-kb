---
id: DOC-HCM-501
doc_type: system-doc
title: "IRC_JD_REQ_POST_RESULTS — Resultados de Publicacoes"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - posting-results
  - irc-recruiting
aliases:
  - IRC_JD_REQ_POST_RESULTS
  - irc_jd_req_post_results
  - jd-req-post-results
  - jd-req-hcm
  - irc-jd-req-post-results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_JD_REQ_POST_RESULTS

## Visao Geral

**Resultados** (metricas) de publicacoes de vagas.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Metricas:** Visualizacoes, cliques, candidaturas por canal.
- **ROI por canal:** Canais mais eficazes.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POST_RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REQ_POSTING_ID | NUMBER(18) | NOT NULL | FK | Publicacao | IRC_JD_REQ_POSTINGS | 🟢 85% |
| 3 | METRIC_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de metrica | — | 🟡 70% |
| 4 | METRIC_VALUE | NUMBER | NULL | Dados | Valor | — | 🟡 70% |
| 5 | METRIC_DATE | DATE | NULL | Dados | Data | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_jd_req_postings]] — via `REQ_POSTING_ID` (publicacao de vaga do resultado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Resultados por metrica
```sql
SELECT pr.METRIC_TYPE, SUM(pr.METRIC_VALUE) AS total
FROM   IRC_JD_REQ_POST_RESULTS pr WHERE pr.REQ_POSTING_ID = :p_id
GROUP BY pr.METRIC_TYPE;
```

### Filtros comuns
- `METRIC_TYPE = :tipo` — Por metrica
---

## Observacoes

- Dados atualizados por integracao com job boards.
---

## Referencias

- [Oracle Docs -- IRC_JD_REQ_POST_RESULTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircjdreqpostresults.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
