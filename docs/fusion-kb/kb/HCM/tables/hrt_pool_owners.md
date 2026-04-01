---
id: DOC-HCM-244
doc_type: system-doc
title: "HRT_POOL_OWNERS — Proprietarios de Pool de Talento"
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
  - proprietarios
  - talent
aliases:
  - HRT_POOL_OWNERS
  - hrt_pool_owners
  - hrt-pool-owners
  - pool-owners
  - proprietarios-pool
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_POOL_OWNERS

## 📌 Visao Geral

Armazena os **proprietarios/gestores** de cada pool de talento. Define quem tem permissao para gerenciar o pool e seus membros.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Governanca:** Controlar quem pode adicionar/remover membros do pool.
- **Ownership:** Definir responsaveis por processos de talent review.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_OWNER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do proprietario | — | 🟢 95% |
| 2 | POOL_ID | NUMBER(18) | NOT NULL | FK | Pool de talento | [[hrt_pools_vl]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa proprietaria do pool | [[per_all_people_f]] | 🟢 95% |
| 4 | OWNER_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de propriedade (PRIMARY, SECONDARY) | — | 🟡 80% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inicio da propriedade | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim da propriedade | — | 🟢 85% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_pools_vl]] — via `POOL_ID` (pool de talentos do proprietario)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa proprietaria do pool de talentos)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Proprietarios de um pool
```sql
SELECT po.PERSON_ID, po.OWNER_TYPE
FROM   HRT_POOL_OWNERS po
WHERE  po.POOL_ID = :p_pool_id;
```

---

## 🔒 Observacoes

- Um pool pode ter multiplos proprietarios com diferentes niveis de acesso.
- Proprietarios primarios (PRIMARY) tem controle total sobre o pool.

---

## 📚 Referencias

- [Oracle Docs — HRT_POOL_OWNERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtpoolowners.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepoolownerpvo|CandidatePoolOwnerPVO]] (PO · BICC: 10/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| FAVORITE_FLAG | FavoriteFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNER_PERSON_ID | OwnerPersonId | — |
| POOL_ID | PoolId | ✅ |
| POOL_OWNER_ID | PoolOwnerId | ✅ |

### [[talentpooluserspvo|TalentPoolUsersPVO]] (PO · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| ENTERPRISE_ID | OwnerEnterpriseId | ✅ |
| FAVORITE_FLAG | FavoriteFlag | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER_PERSON_ID | OwnerPersonId | ✅ |
| POOL_ID | OwnerPoolId | ✅ |
| POOL_OWNER_ID | PoolOwnerId | — |
