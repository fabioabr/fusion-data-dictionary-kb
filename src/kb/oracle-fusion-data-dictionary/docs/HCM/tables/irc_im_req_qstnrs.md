---
id: DOC-HCM-495
doc_type: system-doc
title: "IRC_IM_REQ_QSTNRS — Questionarios de Requisicoes"
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
  - interview-questionnaires
  - irc-recruiting
aliases:
  - IRC_IM_REQ_QSTNRS
  - irc_im_req_qstnrs
  - im-req-qstnrs
  - im-req-hcm
  - irc-im-req-qstnrs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_IM_REQ_QSTNRS

## Visao Geral

**Questionarios** associados a requisicoes de entrevista.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Padronizacao:** Questionarios estruturados por requisicao.
- **Consistencia:** Mesmas perguntas para todos os candidatos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_QSTNR_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 85% |
| 3 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionario | — | 🟡 80% |
| 4 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de uso | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao do questionario de entrevista)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Questionarios de uma requisicao
```sql
SELECT rq.QUESTIONNAIRE_ID, rq.USAGE_TYPE
FROM   IRC_IM_REQ_QSTNRS rq WHERE rq.REQUISITION_ID = :p_id;
```

### Filtros comuns
- `REQUISITION_ID = :id` — Por requisicao
---

## Observacoes

- Tabela associativa entre requisicoes e questionarios.
---

## Referencias

- [Oracle Docs -- IRC_IM_REQ_QSTNRS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircimreqqstnrs.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| QSTNR_TYPE_CODE | QstnrTypeCode | — |
| QSTNR_VERSION_NUM | QstnrVersionNum4 | — |
| QUESTIONNAIRE_ID | QuestionnaireId4 | — |
| REQUISITION_ID | RequisitionId2 | — |

### [[requisitionqstnrexternalviewallpvo|RequisitionQstnrExternalViewAllPVO]] (PO · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| QSTNR_TYPE_CODE | QstnrTypeCode | — |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |

### [[requisitionqstnrinternalviewallpvo|RequisitionQstnrInternalViewAllPVO]] (PO · BICC: 5/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| QSTNR_TYPE_CODE | QstnrTypeCode | ✅ |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |

### [[requisitionqstnrinterviewviewallpvo|RequisitionQstnrInterviewViewAllPVO]] (PO · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| QSTNR_TYPE_CODE | QstnrTypeCode | — |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |

### [[submissionqstnrsviewallpvo|SubmissionQstnrsViewAllPVO]] (PO · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RequisitionQstnrPEOCreatedBy | — |
| CREATION_DATE | RequisitionQstnrPEOCreationDate | — |
| LAST_UPDATE_DATE | RequisitionQstnrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionQstnrPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionQstnrPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | RequisitionQstnrPEOObjectVersionNumber | — |
| QSTNR_TYPE_CODE | RequisitionQstnrPEOQstnrTypeCode | — |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |
