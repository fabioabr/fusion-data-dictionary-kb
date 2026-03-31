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

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | EnterpriseId | — |
| ENTERPRISE_ID | EnterpriseId1 | — |
| MEMBER_ID | MemberId | — |
| POOL_MEMBER_ID | PoolMemberId1 | — |
| STATUS | Status | — |

### [[poolcandhisteventpvo|PoolCandHistEventPVO]] (PO · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATION_DATE | PoolMemberPEOCreationDate | — |
| ENTERPRISE_ID | EnterpriseId | — |
| MEMBER_ID | MemberId | ✅ |
| POOL_ID | PoolId | — |
| POOL_MEMBER_ID | PoolMemberId | — |

### [[poolmemberspvo|PoolMembersPVO]] (PO · BICC: 9/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENTERPRISE_ID | PoolMembersPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MEMBER_ID | PoolMembersPEOMemberId | ✅ |
| MEMBER_SINCE | MemberSince | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| POOL_ID | PoolMembersPEOPoolId | ✅ |
| POOL_MEMBER_ID | PoolMembersPEOPoolMemberId | ✅ |
| POOL_MEMBER_TYPE | PoolMemberType | — |
| STATUS | PoolMembersPEOStatus | ✅ |

### [[sourcetrackingviewallpvo|SourceTrackingViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ENTERPRISE_ID | PoolMemberPEOEnterpriseId | — |
| POOL_MEMBER_ID | PoolMemberPEOPoolMemberId | — |
