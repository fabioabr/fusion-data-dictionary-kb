---
id: DOC-HCM-241
doc_type: system-doc
title: "HRT_POOLS_VL — Pools de Talento (View Linguistica)"
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
  - talent
  - sucessao
aliases:
  - HRT_POOLS_VL
  - hrt_pools_vl
  - hrt-pools-vl
  - talent-pools-vl
  - pools-talento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_POOLS_VL

## 📌 Visao Geral

View linguistica que combina dados base e traducoes dos **pools de talento**. Pools sao agrupamentos de colaboradores para processos de talent review, sucessao e desenvolvimento.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Agrupar colaboradores em pools para revisao de talentos.
- **Sucessao:** Pools de candidatos a posicoes criticas.
- **Desenvolvimento:** Agrupar colaboradores por programas de desenvolvimento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do pool | — | 🟢 95% |
| 2 | POOL_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome do pool (traduzido) | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao do pool | — | 🟢 90% |
| 4 | POOL_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do pool (e.g., SUCCESSION, DEVELOPMENT) | — | 🟡 80% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do pool (ACTIVE, INACTIVE) | — | 🟡 80% |
| 6 | DATE_FROM | DATE | NULL | Data | Data de inicio de vigencia | — | 🟢 90% |
| 7 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hrt_pool_members]] — via `POOL_ID` (membros do pool de talentos)
- [[hrt_pool_owners]] — via `POOL_ID` (proprietarios do pool de talentos)
- [[hrt_pool_associations]] — via `POOL_ID` (associacoes do pool de talentos)

---

## 📎 Uso Tipico

### Pools de talento ativos
```sql
SELECT p.POOL_ID, p.POOL_NAME, p.POOL_TYPE, p.STATUS
FROM   HRT_POOLS_VL p
WHERE  p.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN NVL(p.DATE_FROM, SYSDATE) AND NVL(p.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_VL` indica View Linguistica (base + traducao).
- Pools podem ser publicos ou restritos a determinados gestores.

---

## 📚 Referencias

- [Oracle Docs — HRT_POOLS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtpoolsvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| POOL_ID | PoolId1 | — |

### [[candidatepoolownerpvo|CandidatePoolOwnerPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| POOL_ID | PoolId1 | — |
| POOL_TYPE_CODE | PoolTypeCode | — |

### [[candidatepoolpvo|CandidatePoolPVO]] (PO · BICC: 8/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEPARTMENT_ID | DepartmentId | — |
| DESCRIPTION | Description | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| GRADE_ID | GradeId | — |
| JOB_FAMILY_ID | JobFamilyId | — |
| JOB_ID | JobId | — |
| JOB_PROFILE_ID | JobProfileId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| POOL_ID | PoolId | ✅ |
| POOL_NAME | PoolName | ✅ |
| POOL_TYPE_CODE | PoolTypeCode | ✅ |
| POSITION_ID | PositionId | — |
| STATUS | Status | ✅ |

### [[poolcandhisteventpvo|PoolCandHistEventPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| POOL_ID | PoolId1 | — |

### [[sourcetrackingviewallpvo|SourceTrackingViewAllPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | EnterpriseId | — |
| POOL_ID | FromPoolPEOPoolId | — |
| POOL_NAME | FromPoolPEOPoolName | ✅ |
