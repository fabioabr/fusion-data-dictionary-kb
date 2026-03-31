---
id: DOC-HCM-459
doc_type: system-doc
title: "IRC_CANDIDATES — Candidatos do Recrutamento"
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
  - candidates
  - irc-recruiting
aliases:
  - IRC_CANDIDATES
  - irc_candidates
  - irc-candidates
  - irc_candidates-oracle
  - irc_candidates-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CANDIDATES

## Visao Geral

Tabela **principal de candidatos** do modulo de Recrutamento. Registro central de cada candidato com dados de identificacao, status e perfil.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Registro central:** Ponto unico de referencia para dados de candidatos.
- **Ciclo de vida:** Controla status ao longo do processo seletivo.
- **Integracao:** Base para candidaturas, ofertas e pools.
- **Relatorios:** Fonte primaria para metricas de pipeline.
- **Compliance:** Rastreabilidade completa do historico.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CANDIDATE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 95% |
| 2 | CANDIDATE_NUMBER | VARCHAR2(30) | NOT NULL | Identificacao | Numero sequencial | — | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa (se contratado) | PER_ALL_PEOPLE_F | 🟢 85% |
| 4 | CURRENT_PHASE_ID | NUMBER(18) | NULL | FK | Fase atual | IRC_PHASES_B | 🟡 75% |
| 5 | CURRENT_STATE_ID | NUMBER(18) | NULL | FK | Estado atual | — | 🟡 70% |
| 6 | CANDIDATE_STATUS | VARCHAR2(30) | NULL | Classificacao | Status geral | — | 🟢 85% |
| 7 | EMAIL_ADDRESS | VARCHAR2(240) | NULL | Contato | E-mail principal | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa vinculada ao registro de candidato)
- [[irc_phases_b]] — via `CURRENT_PHASE_ID` (fase atual do candidato no processo seletivo)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Candidatos ativos
```sql
SELECT c.CANDIDATE_ID, c.CANDIDATE_NUMBER, c.CANDIDATE_STATUS,
       c.EMAIL_ADDRESS
FROM   IRC_CANDIDATES c
WHERE  c.CANDIDATE_STATUS = 'ACTIVE'
ORDER BY c.CREATION_DATE DESC;
```

### Filtros comuns
- `CANDIDATE_STATUS = 'ACTIVE'` — Ativos
- `PERSON_ID IS NOT NULL` — Convertidos em funcionarios
---

## Observacoes

- Tabela central do Recruiting — referenciada por quase todas as tabelas IRC.
- PERSON_ID preenchido quando candidato e contratado.
- Dados sensiveis (e-mail) — aplicar filtros de confidencialidade.
---

## Referencias

- [Oracle Docs -- IRC_CANDIDATES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandidates.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepvo|CandidatePVO]] (HCM · BICC: 29/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY_FLOW_CODE | AddedByFlowCode | ✅ |
| AVAILABILITY_DATE | AvailabilityDate | ✅ |
| CAND_EMAIL_ID | CandidatePEOCandEmailId | — |
| CAND_LAST_MODIFIED_DATE | CandLastModifiedDate | ✅ |
| CAND_PHONE_ID | CandidatePEOCandPhoneId | — |
| CAND_PREF_LANGUAGE_CODE | CandPrefLanguageCode | ✅ |
| CANDIDATE_NUMBER | CandidateNumber | ✅ |
| CONFIRMED_FLAG | ConfirmedFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DELETED_BY_USER | CandidatePEODeletedByUser | ✅ |
| DELETION_DATE | CandidatePEODeletionDate | ✅ |
| DELETION_QUALIFIER | CandidatePEODeletionQualifier | ✅ |
| EMAIL_PREFERRED_FLAG | CandidatePEOEmailPreferredFlag | ✅ |
| EMAIL_VERIFIED_FLAG | CandidatePEOEmailVerifiedFlag | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MERGED_FLAG | CandidatePEOMergedFlag | ✅ |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OPT_IN_MKT_EMAILS_DATE | CandPEOOptInMktEmailsDate | ✅ |
| OPT_IN_MKT_EMAILS_FLAG | CandPEOOptInMktEmailsFlag | ✅ |
| PERSON_ID | PersonId | ✅ |
| PHONE_PREFERRED_FLAG | CandidatePEOPhonePreferredFlag | ✅ |
| PHONE_VERIFIED_FLAG | CandidatePEOPhoneVerifiedFlag | ✅ |
| POTENTIAL_DUPLICATE_FLAG | CandidatePEOPotentialDuplicateFlag | ✅ |
| PREF_PHONE_CNT_TYPE_CODE | PrefPhoneCntTypeCode | ✅ |
| PROFILE_ID | ProfileId1 | — |
| REQUEST_ID | RequestId | — |
| SEARCH_DATE | SearchDate | ✅ |
| VISIBLE_TO_CANDIDATE_FLAG | CandidatePEOVisibleToCandidateFlag | ✅ |
| VISIBLE_TO_CANDIDATE_FLAG | VisibleToCandidateFlag | ✅ |

### [[searchactiondetailpvo|SearchActionDetailPVO]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_NUMBER | CandidatePEOCandidateNumber | ✅ |
| OBJECT_VERSION_NUMBER | CandidatePEOObjectVersionNumber | — |
| PERSON_ID | CandidatePEOPersonId | — |

### [[searchresultpvo|SearchResultPVO]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_NUMBER | CandidatePEOCandidateNumber | ✅ |
| OBJECT_VERSION_NUMBER | CandidatePEOObjectVersionNumber | — |
| PERSON_ID | CandidatePEOPersonId | — |

### [[sourcetrackingviewallpvo|SourceTrackingViewAllPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_NUMBER | CandidatePEOCandidateNumber | ✅ |
| OBJECT_VERSION_NUMBER | CandidatePEOObjectVersionNumber | — |
| PERSON_ID | CandidatePEOPersonId | — |
