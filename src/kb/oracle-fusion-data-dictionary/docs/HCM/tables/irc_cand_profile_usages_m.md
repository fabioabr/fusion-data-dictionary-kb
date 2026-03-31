---
id: DOC-HCM-467
doc_type: system-doc
title: "IRC_CAND_PROFILE_USAGES_M — Uso de Perfis (Materializada)"
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
  - profile-usage
  - irc-recruiting
aliases:
  - IRC_CAND_PROFILE_USAGES_M
  - irc_cand_profile_usages_m
  - cand-profile-usages-m
  - cand-profile-hcm
  - irc-cand-profile-usages-m
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_PROFILE_USAGES_M

## Visao Geral

Tabela **materializada** que consolida **uso de perfis** de candidatos em diferentes contextos.

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **materializada** — dados pre-calculados para otimizacao de consultas. Atualizada periodicamente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Performance:** Dados pre-calculados sobre utilizacao de perfis.
- **Engajamento:** Quantas vezes o perfil foi utilizado.
- **Relatorios:** Dashboards de utilizacao do banco de talentos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟡 75% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 3 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de uso | — | 🟡 70% |
| 4 | USAGE_DATE | TIMESTAMP | NULL | Dados | Data do uso | — | 🟡 70% |
| 5 | CONTEXT_ID | NUMBER(18) | NULL | FK | Contexto de uso | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato com uso de perfil registrado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Usos de perfil
```sql
SELECT pu.USAGE_TYPE, COUNT(*) AS total
FROM   IRC_CAND_PROFILE_USAGES_M pu
WHERE  pu.CANDIDATE_ID = :p_candidate_id
GROUP BY pu.USAGE_TYPE;
```

### Filtros comuns
- `CANDIDATE_ID = :id` — Por candidato
---

## Observacoes

- Materializada (_M) — atualizada periodicamente.
- Util para analytics sem impactar tabelas operacionais.
---

## Referencias

- [Oracle Docs -- IRC_CAND_PROFILE_USAGES_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandprofileusagesm.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepoolmemberpvo|CandidatePoolMemberPVO]] (PO · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAND_PROFILE_USAGE_ID | CandProfileUsageId | — |
| EFFECTIVE_END_DATE | CandProfileUsgsPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | CandProfileUsgsPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | CandProfileUsgsPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | CandProfileUsgsPEOEffectiveStartDate | ✅ |
| PROFILE_ID | CandProfileUsgsPEOProfileId | — |

### [[candidatepvo|CandidatePVO]] (HCM · BICC: 1/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAND_PROFILE_USAGE_ID | CandProfileUsageId | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | EffectiveSequence | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| JOB_DEFINITION_NAME | JobDefinitionName1 | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PROFILE_ID | ProfileId | ✅ |
| PROFILE_TYPE | ProfileType | — |
| REQUEST_ID | RequestId1 | — |

### [[prospectspvo|ProspectsPVO]] (HCM · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAND_PROFILE_USAGE_ID | CProUsgPEOCandProfileUsageId | ✅ |
| EFFECTIVE_END_DATE | CProUsgPEOEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | CProUsgPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | CProUsgPEOEffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | CProUsgPEOEffectiveStartDate | ✅ |
| PROFILE_ID | CProUsgPEOCandProfileId | ✅ |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAND_PROFILE_USAGE_ID | CProUsgPEOCandProfileUsageId | — |
| EFFECTIVE_END_DATE | CProUsgPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | CProUsgPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | CProUsgPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | CProUsgPEOEffectiveStartDate | ✅ |
| PROFILE_ID | CProUsgPEOCandProfileId | — |
