---
id: DOC-HCM-499
doc_type: system-doc
title: "IRC_JD_REQ_POSTINGS — Publicacoes de Vagas"
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
  - job-postings
  - irc-recruiting
aliases:
  - IRC_JD_REQ_POSTINGS
  - irc_jd_req_postings
  - jd-req-postings
  - jd-req-hcm
  - irc-jd-req-postings
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_JD_REQ_POSTINGS

## Visao Geral

**Publicacoes** de requisicoes em canais externos e internos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de publicacoes:** Onde cada vaga esta publicada.
- **Multicanalidade:** Multiplos canais.
- **Origem:** Qual canal gerou mais candidaturas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_POSTING_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | POSTING_CHANNEL | VARCHAR2(30) | NULL | Classificacao | Canal | — | 🟡 75% |
| 4 | POSTING_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 80% |
| 5 | POSTING_START_DATE | DATE | NULL | Dados | Inicio | — | 🟡 80% |
| 6 | POSTING_END_DATE | DATE | NULL | Dados | Fim | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao da publicacao de vaga)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Publicacoes ativas
```sql
SELECT rp.POSTING_CHANNEL, rp.POSTING_STATUS, rp.POSTING_START_DATE
FROM   IRC_JD_REQ_POSTINGS rp
WHERE  rp.REQUISITION_ID = :p_id AND rp.POSTING_STATUS = 'ACTIVE';
```

### Filtros comuns
- `POSTING_STATUS = 'ACTIVE'` — Ativas
---

## Observacoes

- Multiplas publicacoes por requisicao.
- POSTING_CHANNEL identifica origem.
---

## Referencias

- [Oracle Docs -- IRC_JD_REQ_POSTINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircjdreqpostings.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[jobposthistorypvo|JobPostHistoryPVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingPEOPostingId | — |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |

### [[jobposthistoryviewallpvo|JobPostHistoryViewAllPVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingPEOPostingId | — |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |

### [[jobpostingpvo|JobPostingPVO]] (HCM · BICC: 11/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingId | ✅ |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |

### [[jobpostingviewallpvo|JobPostingViewAllPVO]] (HCM · BICC: 11/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingId | ✅ |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |

### [[jobpostresultpvo|JobPostResultPVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingPEOPostingId | — |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |

### [[jobpostresultviewallpvo|JobPostResultViewAllPVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostingPEOCreatedBy | ✅ |
| CREATION_DATE | PostingPEOCreationDate | ✅ |
| JD_ERROR_DESC | PostingPEOJdErrorDesc | ✅ |
| LAST_UPDATE_DATE | PostingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostingPEOObjectVersionNumber | — |
| POSTED_BY | PostingPEOPostedBy | ✅ |
| POSTED_DATE | PostingPEOPostedDate | ✅ |
| POSTING_ID | PostingPEOPostingId | — |
| PROVISIONING_ID | PostingPEOProvisioningId | ✅ |
| REQUISITION_ID | PostingPEORequisitionId | ✅ |
