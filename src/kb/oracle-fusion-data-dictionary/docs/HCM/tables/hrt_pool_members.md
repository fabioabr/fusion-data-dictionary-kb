---
id: DOC-HCM-243
doc_type: system-doc
title: "HRT_POOL_MEMBERS — Membros de Pool de Talento"
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
  - membros
  - talent
aliases:
  - HRT_POOL_MEMBERS
  - hrt_pool_members
  - hrt-pool-members
  - pool-members
  - membros-pool
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_POOL_MEMBERS

## 📌 Visao Geral

Armazena os **membros** (colaboradores) de cada pool de talento. Cada registro vincula um colaborador a um pool com datas de vigencia.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Listar colaboradores participantes de um pool.
- **Sucessao:** Identificar candidatos em pools de sucessao.
- **Desenvolvimento:** Rastrear participantes de programas de desenvolvimento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_MEMBER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do membro | — | 🟢 95% |
| 2 | POOL_ID | NUMBER(18) | NOT NULL | FK | Pool de talento | [[hrt_pools_vl]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador membro | [[per_all_people_f]] | 🟢 95% |
| 4 | MEMBER_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de membro (e.g., CANDIDATE, READY_NOW) | — | 🟡 80% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inclusao no pool | — | 🟢 90% |
| 6 | DATE_TO | DATE | NULL | Data | Data de exclusao do pool | — | 🟢 90% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do membro no pool | — | 🟡 75% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_pools_vl]] — via `POOL_ID` (pool de talentos do membro)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa membro do pool de talentos)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Membros de um pool
```sql
SELECT pm.PERSON_ID, pm.MEMBER_TYPE, pm.DATE_FROM
FROM   HRT_POOL_MEMBERS pm
WHERE  pm.POOL_ID = :p_pool_id
  AND  SYSDATE BETWEEN NVL(pm.DATE_FROM, SYSDATE) AND NVL(pm.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Um colaborador pode ser membro de multiplos pools simultaneamente.
- O campo MEMBER_TYPE pode indicar nivel de prontidao para sucessao.

---

## 📚 Referencias

- [Oracle Docs — HRT_POOL_MEMBERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtpoolmembers.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
