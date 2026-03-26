---
id: DOC-HCM-242
doc_type: system-doc
title: "HRT_POOL_ASSOCIATIONS — Associacoes de Pool de Talento"
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
  - pools
  - associacoes
  - talent
aliases:
  - HRT_POOL_ASSOCIATIONS
  - hrt_pool_associations
  - hrt-pool-associations
  - pool-associations
  - associacoes-pool
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_POOL_ASSOCIATIONS

## 📌 Visao Geral

Armazena as **associacoes entre pools de talento e outros objetos** (organizacoes, posicoes, jobs). Define o escopo e contexto de cada pool.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Escopo:** Definir a quais organizacoes ou posicoes um pool esta vinculado.
- **Contexto:** Associar pools a processos de sucessao ou desenvolvimento especificos.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_ASSOCIATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da associacao | — | 🟢 95% |
| 2 | POOL_ID | NUMBER(18) | NOT NULL | FK | Pool de talento | [[hrt_pools_vl]] | 🟢 95% |
| 3 | ASSOCIATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo da associacao (ORGANIZATION, POSITION, JOB) | — | 🟡 80% |
| 4 | ASSOCIATION_ID | NUMBER(18) | NOT NULL | FK | ID do objeto associado | — | 🟡 80% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inicio | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 85% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_pools_vl]] — via `POOL_ID` (pool de talentos da associacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Associacoes de um pool
```sql
SELECT pa.ASSOCIATION_TYPE, pa.ASSOCIATION_ID
FROM   HRT_POOL_ASSOCIATIONS pa
WHERE  pa.POOL_ID = :p_pool_id;
```

---

## 🔒 Observacoes

- O campo ASSOCIATION_TYPE determina como interpretar ASSOCIATION_ID.
- Suporta associacao polimorfica (organizacao, posicao ou job).

---

## 📚 Referencias

- [Oracle Docs — HRT_POOL_ASSOCIATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtpoolassociations.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
