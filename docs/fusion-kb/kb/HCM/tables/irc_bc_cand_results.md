---
id: DOC-HCM-444
doc_type: system-doc
title: "IRC_BC_CAND_RESULTS — Resultados de Background Check de Candidatos"
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
  - irc
  - background-check
  - resultado-verificacao
aliases:
  - IRC_BC_CAND_RESULTS
  - irc_bc_cand_results
  - irc-bc-cand-results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_BC_CAND_RESULTS

## 📌 Visao Geral

Armazena os **resultados de verificacao de antecedentes** (background check) de candidatos do modulo Recruiting (IRC). Contem os resultados retornados por parceiros de background screening.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Verificacao de antecedentes:** armazena resultados de background checks.
- **Compliance:** garante conformidade com politicas de contratacao.
- **Decisao de contratacao:** informa decisoes com base em verificacoes.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAND_RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador do resultado | — | 🟡 70% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato verificado | — | 🟡 65% |
| 3 | SCREENING_ID | NUMBER(18) | NOT NULL | FK | Triagem associada | IRC_BC_CAND_SCREENINGS | 🟡 65% |
| 4 | RESULT_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo do resultado | — | 🟡 60% |
| 5 | RESULT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status (CLEAR, ALERT, PENDING) | — | 🟡 60% |
| 6 | RESULT_DATE | TIMESTAMP | NULL | Periodo | Data do resultado | — | 🟡 55% |
| 7 | DETAILS | VARCHAR2(4000) | NULL | Dados | Detalhes do resultado | — | 🟡 50% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_bc_cand_screenings]] — via `SCREENING_ID` (triagem de antecedentes do resultado)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Resultados de background check por candidato
```sql
SELECT cr.RESULT_CODE, cr.RESULT_STATUS, cr.RESULT_DATE
FROM   IRC_BC_CAND_RESULTS cr
WHERE  cr.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `CANDIDATE_ID = :p_candidate_id — Por candidato`
- `RESULT_STATUS = 'CLEAR' — Verificacoes aprovadas`

---

## 🔒 Observacoes

- Contem resultados de verificacoes de antecedentes de candidatos.
- Dados sensiveis — sujeitos a politicas de privacidade e retencao.
- Status ALERT requer revisao manual antes de prosseguir com contratacao.

---

## 📚 Referencias

- [Oracle Docs — IRC_BC_CAND_RESULTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircbccandresults.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP · BICC: 13/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | ScreeningResultPEOAccountId | ✅ |
| BC_ERROR_DESC | ScreeningResultPEOBcErrorDesc | ✅ |
| BC_STATUS_CODE | ScreeningResultPEOBcStatusCode | ✅ |
| CREATED_BY | ScreeningResultPEOCreatedBy | ✅ |
| CREATION_DATE | ScreeningResultPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | ScreeningResultPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ScreeningResultPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ScreeningResultPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ScreeningResultPEOObjectVersionNumber | — |
| PROVISIONING_ID | ScreeningResultPEOProvisioningId | ✅ |
| REQUEST_DATE | ScreeningResultPEORequestDate | ✅ |
| REQUESTED_BY | ScreeningResultPEORequestedBy | ✅ |
| RESULT_ID | ScreeningResultPEOResultId | ✅ |
| SUBMISSION_ID | ScreeningResultPEOSubmissionId | ✅ |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP · BICC: 13/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | ScreeningResultPEOAccountId | ✅ |
| BC_ERROR_DESC | ScreeningResultPEOBcErrorDesc | ✅ |
| BC_STATUS_CODE | ScreeningResultPEOBcStatusCode | ✅ |
| CREATED_BY | ScreeningResultPEOCreatedBy | ✅ |
| CREATION_DATE | ScreeningResultPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | ScreeningResultPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ScreeningResultPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ScreeningResultPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ScreeningResultPEOObjectVersionNumber | — |
| PROVISIONING_ID | ScreeningResultPEOProvisioningId | ✅ |
| REQUEST_DATE | ScreeningResultPEORequestDate | ✅ |
| REQUESTED_BY | ScreeningResultPEORequestedBy | ✅ |
| RESULT_ID | ScreeningResultPEOResultId | ✅ |
| SUBMISSION_ID | ScreeningResultPEOSubmissionId | ✅ |
