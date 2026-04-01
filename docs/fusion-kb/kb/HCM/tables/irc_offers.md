---
id: DOC-HCM-513
doc_type: system-doc
title: "IRC_OFFERS — Ofertas de Emprego"
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
  - offers
  - irc-recruiting
aliases:
  - IRC_OFFERS
  - irc_offers
  - irc-offers
  - irc_offers-oracle
  - irc_offers-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_OFFERS

## Visao Geral

**Ofertas de emprego** feitas a candidatos. Termos e condicoes de proposta formal.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de ofertas:** Ciclo completo de ofertas.
- **Negociacao:** Versoes e contra-propostas.
- **Compliance:** Termos oferecidos e aceitos.
- **Metricas:** Taxa de aceite.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OFFER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 90% |
| 3 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 4 | OFFER_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟢 85% |
| 5 | OFFER_DATE | DATE | NULL | Dados | Data da oferta | — | 🟡 80% |
| 6 | EXPIRY_DATE | DATE | NULL | Dados | Data de expiracao | — | 🟡 75% |
| 7 | PROPOSED_SALARY | NUMBER | NULL | Dados | Salario proposto | — | 🟡 70% |
| 8 | PROPOSED_START_DATE | DATE | NULL | Dados | Data inicio proposta | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato que recebeu a proposta)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao da proposta de emprego)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Ofertas aceitas
```sql
SELECT o.OFFER_ID, o.CANDIDATE_ID, o.PROPOSED_SALARY, o.OFFER_DATE
FROM   IRC_OFFERS o WHERE o.OFFER_STATUS = 'ACCEPTED'
ORDER BY o.OFFER_DATE DESC;
```

### Filtros comuns
- `OFFER_STATUS = 'ACCEPTED'` — Aceitas
---

## Observacoes

- PROPOSED_SALARY — dado sensivel.
- Tabela central para metricas de offer-to-hire.
---

## Referencias

- [Oracle Docs -- IRC_OFFERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircoffers.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OffersPEOOfferId | — |

### [[jobapphisteventpvo|JobAppHistEventPVO]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATION_DATE | OffersPEOCreationDate | ✅ |
| MOVE_TO_HR_DATE | OffersPEOMoveToHrDate | — |
| OFFER_ID | OffersPEOOfferId | ✅ |

### [[offerpvo|OfferPVO]] (HCM · BICC: 31/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | AcceptedDate | ✅ |
| ACCEPTED_ON_BEHALF | AcceptedOnBehalf | ✅ |
| ACCEPTED_ON_BEHALF_BY_ID | AcceptedOnBehalfById | ✅ |
| ACCEPTED_ON_BEHALF_DATE | AcceptedOnBehalfDate | ✅ |
| ADDITIONALTEXT1 | OffersPEOAdditionaltext1 | ✅ |
| ADDITIONALTEXT2 | OffersPEOAdditionaltext2 | ✅ |
| APPROVED_DATE | ApprovedDate | ✅ |
| ASSIGNMENT_OFFER_ID | AssignmentOfferId | ✅ |
| BATCH_CREATION_FLAG | OffersPEOBatchCreationFlag | — |
| BYPASS_OFFER_LC_FLAG | OffersPEOBypassOfferLcFlag | — |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| DRAFTED_DATE | OffersPEODraftedDate | — |
| ESIGNATURE_INSTRUCTIONS | EsignatureInstructions | ✅ |
| EXPIRATION_DATE | ExpirationDate | ✅ |
| EXTENDED_DATE | ExtendedDate | ✅ |
| HANDOFF_HR_SCENARIO_ID | HandoffHrScenarioId | ✅ |
| HIRING_MANAGER_ID | HiringManagerId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MERGED_FLAG | OffersPEOMergedFlag | — |
| MOVE_TO_HR_DATE | OffersPEOMoveToHrDate | — |
| OBJECT_STATUS | OffersPEOObjectStatus | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OFFER_ID | OfferId | ✅ |
| OFFER_ID | ParentOffersPEOOfferId | — |
| OFFER_LETTER_CUSTOMIZED_FLAG | OffersPEOOfferLetterCustomizedFlag | ✅ |
| OFFER_LETTER_LAYOUT_ID | OffersPEOOfferLetterLayoutId | — |
| OFFER_NAME | OfferName | ✅ |
| OFFER_NAME | ParentOffersPEOOfferName | — |
| PARENT_OFFER_ID | OffersPEOParentOfferId | — |
| PERSON_ID | PersonId | ✅ |
| PRESELECTED_HR_ACTION_ID | PreselectedHrActionId | ✅ |
| PRESELECTED_HR_ACTIONTYPE_CODE | PreselectedHrActiontypeCode | — |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | ✅ |
| RECRUITER_ID | RecruiterId | ✅ |
| START_DATE_CHANGED_FLAG | OffersPEOStartDateChangedFlag | — |
| STATE_POST_PROCESS_STATUS | OffersPEOStatePostProcessStatus | — |
| SUBMISSION_ID | SubmissionId | ✅ |
| WITHDRAWN_REJECTED_DATE | WithdrawnRejectedDate | ✅ |

### [[offersalarypvo|OfferSalaryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_OFFER_ID | OffersPEOAssignmentOfferId | — |
| HIRING_MANAGER_ID | OffersPEOHiringManagerId | — |
| MANAGER_ASSIGNMENT_ID | OffersPEOManagerAssignmentId | — |
| OFFER_ID | OffersPEOOfferId | — |
| PERSON_ID | OffersPEOPersonId1 | — |
| RECRUITER_ASSIGNMENT_ID | OffersPEORecruiterAssignmentId | — |
| RECRUITER_ID | OffersPEORecruiterId | — |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OffersPEOOfferId | — |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OffersPEOOfferId | — |

### [[submissionqstnrsviewallpvo|SubmissionQstnrsViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OffersPEOOfferId | — |

### [[submissionrestrictedpvo|SubmissionRestrictedPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OfferId | — |

### [[submissionviewallpvo|SubmissionViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OFFER_ID | OfferId | — |
