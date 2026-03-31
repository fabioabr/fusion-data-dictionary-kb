---
id: DOC-HCM-463
doc_type: system-doc
title: "IRC_CAND_POOL_MEMBERS — Membros de Pools de Candidatos"
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
  - candidate-pool
  - irc-recruiting
aliases:
  - IRC_CAND_POOL_MEMBERS
  - irc_cand_pool_members
  - cand-pool-members
  - cand-pool-hcm
  - irc-cand-pool-members
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_POOL_MEMBERS

## Visao Geral

Associacao entre **candidatos** e **pools de talentos**. Gestao de pipeline de talentos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Pools de talentos:** Controle de membros por pool.
- **Pipeline:** Candidatos pre-qualificados por area.
- **Reengajamento:** Contato com candidatos em pools.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POOL_MEMBER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 90% |
| 3 | POOL_ID | NUMBER(18) | NOT NULL | FK | Pool de talentos | — | 🟢 85% |
| 4 | MEMBER_STATUS | VARCHAR2(30) | NULL | Classificacao | Status no pool | — | 🟡 75% |
| 5 | ADDED_DATE | DATE | NULL | Dados | Data de adicao | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato membro do pool de recrutamento)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Membros ativos em um pool
```sql
SELECT pm.CANDIDATE_ID, pm.MEMBER_STATUS, pm.ADDED_DATE
FROM   IRC_CAND_POOL_MEMBERS pm
WHERE  pm.POOL_ID = :p_pool_id AND pm.MEMBER_STATUS = 'ACTIVE';
```

### Filtros comuns
- `POOL_ID = :id` — Por pool
- `MEMBER_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela associativa N:N.
- Candidatos podem pertencer a multiplos pools.
---

## Referencias

- [Oracle Docs -- IRC_CAND_POOL_MEMBERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandpoolmembers.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENT_PHASE_ID | CurrentPhaseId | ✅ |
| CURRENT_STATE_ID | CurrentStateId | ✅ |
| LAST_ADD_TO_REQ_DATE | LastAddToReqDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LAST_UPDATED_BY_PERSON_ID | LastUpdatedByPersonId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| POOL_ID | PoolId | ✅ |
| POOL_MEMBER_ID | PoolMemberId | ✅ |
| PROCESS_INSTANCE_ID | CandPoolMemberPEOProcessInstanceId | — |
| PROCESS_TEMPLATE_ID | CandPoolMemberPEOProcessTemplateId | — |
