---
id: DOC-HCM-500
doc_type: system-doc
title: "IRC_JD_REQ_POST_HISTORY — Historico de Publicacoes"
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
  - posting-history
  - irc-recruiting
aliases:
  - IRC_JD_REQ_POST_HISTORY
  - irc_jd_req_post_history
  - jd-req-post-history
  - jd-req-hcm
  - irc-jd-req-post-history
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_JD_REQ_POST_HISTORY

## Visao Geral

**Historico de alteracoes** em publicacoes de vagas.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Auditoria:** Rastreabilidade de alteracoes.
- **Timeline:** Historico completo de publicacao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POST_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REQ_POSTING_ID | NUMBER(18) | NOT NULL | FK | Publicacao | IRC_JD_REQ_POSTINGS | 🟢 85% |
| 3 | ACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de acao | — | 🟡 75% |
| 4 | ACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora | — | 🟡 80% |
| 5 | OLD_STATUS | VARCHAR2(30) | NULL | Dados | Status anterior | — | 🟡 70% |
| 6 | NEW_STATUS | VARCHAR2(30) | NULL | Dados | Novo status | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_jd_req_postings]] — via `REQ_POSTING_ID` (publicacao de vaga do historico)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Historico de uma publicacao
```sql
SELECT ph.ACTION_TYPE, ph.ACTION_DATE, ph.OLD_STATUS, ph.NEW_STATUS
FROM   IRC_JD_REQ_POST_HISTORY ph WHERE ph.REQ_POSTING_ID = :p_id
ORDER BY ph.ACTION_DATE DESC;
```

### Filtros comuns
- `REQ_POSTING_ID = :id` — Por publicacao
---

## Observacoes

- Tabela append-only.
---

## Referencias

- [Oracle Docs -- IRC_JD_REQ_POST_HISTORY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircjdreqposthistory.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[jobposthistorypvo|JobPostHistoryPVO]] (HCM · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostHistoryPEOCreatedBy | ✅ |
| CREATION_DATE | PostHistoryPEOCreationDate | ✅ |
| ERROR_DESC | PostHistoryPEOErrorDesc | ✅ |
| JOB_BOARD_ID | PostHistoryPEOJobBoardId | ✅ |
| JOB_BOARD_NAME | PostHistoryPEOJobBoardName | ✅ |
| LAST_UPDATE_DATE | PostHistoryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostHistoryPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostHistoryPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostHistoryPEOObjectVersionNumber | — |
| POSTING_END_DATE | PostHistoryPEOPostingEndDate | ✅ |
| POSTING_ID | PostHistoryPEOPostingId | ✅ |
| POSTING_LANG | PostHistoryPEOPostingLang | ✅ |
| POSTING_START_DATE | PostHistoryPEOPostingStartDate | ✅ |
| POSTING_STATUS_CODE | PostHistoryPEOPostingStatusCode | ✅ |
| RESULT_ID | ResultId | ✅ |

### [[jobposthistoryviewallpvo|JobPostHistoryViewAllPVO]] (HCM · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PostHistoryPEOCreatedBy | ✅ |
| CREATION_DATE | PostHistoryPEOCreationDate | ✅ |
| ERROR_DESC | PostHistoryPEOErrorDesc | ✅ |
| JOB_BOARD_ID | PostHistoryPEOJobBoardId | ✅ |
| JOB_BOARD_NAME | PostHistoryPEOJobBoardName | ✅ |
| LAST_UPDATE_DATE | PostHistoryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PostHistoryPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PostHistoryPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PostHistoryPEOObjectVersionNumber | — |
| POSTING_END_DATE | PostHistoryPEOPostingEndDate | ✅ |
| POSTING_ID | PostHistoryPEOPostingId | ✅ |
| POSTING_LANG | PostHistoryPEOPostingLang | ✅ |
| POSTING_START_DATE | PostHistoryPEOPostingStartDate | ✅ |
| POSTING_STATUS_CODE | PostHistoryPEOPostingStatusCode | ✅ |
| RESULT_ID | ResultId | ✅ |
