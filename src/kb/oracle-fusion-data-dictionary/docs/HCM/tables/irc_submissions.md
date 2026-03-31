---
id: DOC-HCM-540
doc_type: system-doc
title: "IRC_SUBMISSIONS — Candidaturas (Submissions)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - submissions
  - candidaturas
  - irc-submissions
aliases:
  - IRC_SUBMISSIONS
  - irc_submissions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SUBMISSIONS

## 📌 Visão Geral

Tabela central do modulo Recruiting que armazena as **candidaturas** de candidatos a requisicoes. Cada registro representa uma candidatura de um candidato a uma vaga especifica, com seu estado corrente no fluxo seletivo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Registro de todas as candidaturas a vagas
- Controle do estado corrente de cada candidatura no pipeline
- Base para funil de recrutamento e metricas de conversao
- Vinculacao candidato-requisicao-estado

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUBMISSION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da candidatura | --- | 🟢 95% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | ID do candidato | IRC_CANDIDATES | 🟢 95% |
| 3 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | ID da requisicao | IRC_REQUISITIONS_B | 🟢 95% |
| 4 | CURRENT_STATE_ID | NUMBER(18) | NULL | FK | ID do estado corrente | IRC_STATES_B | 🟢 85% |
| 5 | CURRENT_PHASE_ID | NUMBER(18) | NULL | FK | ID da fase corrente | --- | 🟡 75% |
| 6 | SUBMISSION_DATE | DATE | NULL | Dados | Data da candidatura | --- | 🟢 85% |
| 7 | SOURCE | VARCHAR2(30) | NULL | Classificacao | Fonte da candidatura | --- | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] --- via `CANDIDATE_ID` (candidato que realizou a candidatura)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisição de vaga da candidatura)
- [[irc_states_b]] --- via `CURRENT_STATE_ID` (estado atual da candidatura no processo seletivo)

### Tabelas-filha (FK de saída)
- [[irc_source_tracking]] --- via `SUBMISSION_ID` (rastreamento de origem da candidatura)

---

## 📎 Uso Típico

### Candidaturas e estados por requisicao
```sql
SELECT s.SUBMISSION_ID, s.CANDIDATE_ID, s.REQUISITION_ID,
       s.SUBMISSION_DATE, sb.STATE_CODE
FROM   IRC_SUBMISSIONS s
JOIN   IRC_STATES_B sb ON sb.STATE_ID = s.CURRENT_STATE_ID
WHERE  s.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | SubmissionPEOObjectVersionNumber | — |
| PERSON_ID | SubmissionPEOPersonId | ✅ |
| REQUISITION_ID | SubmissionPEORequisitionId | — |
| SUBMISSION_ID | SubmissionPEOSubmissionId | ✅ |

### [[jobapphisteventpvo|JobAppHistEventPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATION_DATE | SubmissionPEOCreationDate | ✅ |
| OBJECT_VERSION_NUMBER | SubmissionPEOObjectVersionNumber | — |
| PERSON_ID | SubmissionPEOPersonId | — |
| REQUISITION_ID | SubmissionPEORequisitionId | — |
| SUBMISSION_ID | SubmissionId | ✅ |

### [[prospectspvo|ProspectsPVO]] (HCM · BICC: 5/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | SubmissionPEOActiveFlag | ✅ |
| CREATION_DATE | SubmissionPEOCreationDate | ✅ |
| OBJECT_VERSION_NUMBER | SubmissionPEOObjectVersionNum | ✅ |
| SUBMISSION_DATE | SubmissionPEOSubmissionDate | ✅ |
| SUBMISSION_ID | SubmissionPEOSubmissionId | ✅ |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | SubmissionPEOActiveFlag | — |
| CREATION_DATE | SubmissionPEOCreationDate | — |
| OBJECT_VERSION_NUMBER | SubmissionPEOObjectVersionNum | — |
| SUBMISSION_DATE | SubmissionPEOSubmissionDate | — |
| SUBMISSION_ID | SubmissionPEOSubmissionId | — |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | SubmissionPEOPersonId | ✅ |
| REQUISITION_ID | SubmissionPEORequisitionId | ✅ |
| SUBMISSION_ID | SubmissionPEOSubmissionId | — |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | SubmissionPEOPersonId | ✅ |
| REQUISITION_ID | SubmissionPEORequisitionId | ✅ |
| SUBMISSION_ID | SubmissionPEOSubmissionId | — |

### [[submissionqstnrsviewallpvo|SubmissionQstnrsViewAllPVO]] (PO · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATION_DATE | CreationDate | — |
| INTERNAL_FLAG | SubmissionPEOInternalFlag | — |
| OBJECT_VERSION_NUMBER | SubmissionPEOObjectVersionNumber | — |
| PERSON_ID | SubmissionPEOPersonId | — |
| QSTNR_SCORE | SubmissionPEOQstnrScore | ✅ |
| SUBMISSION_ID | SubmissionPEOSubmissionId | ✅ |

### [[submissionrestrictedpvo|SubmissionRestrictedPVO]] (HCM · BICC: 27/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| ADDED_BY_CONTEXT_CODE | SubmissionPEOAddedByContextCode | ✅ |
| ADDED_BY_PERSON_ID | SubmissionPEOAddedByPersonId | ✅ |
| AF_VERSION_ID | SubmissionPEOAfVersionId | — |
| CONFIRMED_BY_PERSON_ID | ConfirmedByPersonId | ✅ |
| CONFIRMED_FLAG | ConfirmedFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | ✅ |
| CURRENT_STATE_ID | CurrentStateId | ✅ |
| DISCARDED_FLAG | SubmissionPEODiscardedFlag | — |
| DISQUALIFIED_FLAG | DisqualifiedFlag | ✅ |
| ESIGN_DESC_VERSION_ID | EsignDescVersionId | — |
| INTERNAL_FLAG | InternalFlag | ✅ |
| IS_COMPLETED_FLAG | IsCompletedFlag | ✅ |
| IS_RESTRICTED_FLAG | IsRestrictedFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_DESC_VERSION_ID | LegalDescVersionId | — |
| MERGED_FLAG | SubmissionPEOMergedFlag | ✅ |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |
| PIPELINE_SUBMISSION_ID | SubmissionPEOPipelineSubmissionId | ✅ |
| PROCESS_ID | ProcessId | — |
| PROFILE_ID | ProfileId | ✅ |
| PUBLIC_STATE_ID | PublicStateId | ✅ |
| REQUISITION_ID | RequisitionId | — |
| SITE_NUMBER | SiteNumber | ✅ |
| SUBM_LAST_MODIFIED_DATE | SubmLastModifiedDate | ✅ |
| SUBMISSION_CONFIRMED_DATE | SubmissionConfirmedDate | ✅ |
| SUBMISSION_DATE | SubmissionDate | ✅ |
| SUBMISSION_ID | SubmissionId | ✅ |
| SUBMISSION_LANGUAGE_CODE | SubmissionLanguageCode | ✅ |
| SYSTEM_PERSON_TYPE | SubmissionPEOSystemPersonType | ✅ |

### [[submissionviewallpvo|SubmissionViewAllPVO]] (HCM · BICC: 27/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| ADDED_BY_CONTEXT_CODE | SubmissionPEOAddedByContextCode | ✅ |
| ADDED_BY_PERSON_ID | SubmissionPEOAddedByPersonId | ✅ |
| AF_VERSION_ID | SubmissionPEOAfVersionId | — |
| CONFIRMED_BY_PERSON_ID | ConfirmedByPersonId | ✅ |
| CONFIRMED_FLAG | ConfirmedFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | ✅ |
| CURRENT_STATE_ID | CurrentStateId | ✅ |
| DISCARDED_FLAG | SubmissionPEODiscardedFlag | — |
| DISQUALIFIED_FLAG | DisqualifiedFlag | ✅ |
| ESIGN_DESC_VERSION_ID | EsignDescVersionId | — |
| INTERNAL_FLAG | InternalFlag | ✅ |
| IS_COMPLETED_FLAG | IsCompletedFlag | ✅ |
| IS_RESTRICTED_FLAG | IsRestrictedFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_DESC_VERSION_ID | LegalDescVersionId | — |
| MERGED_FLAG | SubmissionPEOMergedFlag | ✅ |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |
| PIPELINE_SUBMISSION_ID | SubmissionPEOPipelineSubmissionId | ✅ |
| PROCESS_ID | ProcessId | — |
| PROFILE_ID | ProfileId | ✅ |
| PUBLIC_STATE_ID | PublicStateId | ✅ |
| REQUISITION_ID | RequisitionId | — |
| SITE_NUMBER | SiteNumber | ✅ |
| SUBM_LAST_MODIFIED_DATE | SubmLastModifiedDate | ✅ |
| SUBMISSION_CONFIRMED_DATE | SubmissionConfirmedDate | ✅ |
| SUBMISSION_DATE | SubmissionDate | ✅ |
| SUBMISSION_ID | SubmissionId | ✅ |
| SUBMISSION_LANGUAGE_CODE | SubmissionLanguageCode | ✅ |
| SYSTEM_PERSON_TYPE | SubmissionPEOSystemPersonType | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_SUBMISSIONS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsubmissions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
