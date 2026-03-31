---
id: DOC-HCM-494
doc_type: system-doc
title: "IRC_IM_FEEDBK_REVIEWS — Revisoes de Feedback"
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
  - feedback-reviews
  - irc-recruiting
aliases:
  - IRC_IM_FEEDBK_REVIEWS
  - irc_im_feedbk_reviews
  - im-feedbk-reviews
  - im-feedbk-hcm
  - irc-im-feedbk-reviews
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_IM_FEEDBK_REVIEWS

## Visao Geral

**Revisoes** sobre feedbacks de entrevista.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Revisao de qualidade:** Gestores validam feedbacks.
- **Calibracao:** Suporte a sessoes de calibracao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FEEDBK_REVIEW_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | IM_FEEDBACK_ID | NUMBER(18) | NOT NULL | FK | Feedback revisado | IRC_IM_FEEDBACKS | 🟢 85% |
| 3 | REVIEWER_ID | NUMBER(18) | NULL | FK | Revisor | PER_ALL_PEOPLE_F | 🟡 80% |
| 4 | REVIEW_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 5 | REVIEW_DATE | TIMESTAMP | NULL | Dados | Data da revisao | — | 🟡 75% |
| 6 | REVIEW_COMMENTS | VARCHAR2(4000) | NULL | Dados | Comentarios | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_im_feedbacks]] — via `IM_FEEDBACK_ID` (feedback de entrevista em revisao)
- [[per_all_people_f]] — via `REVIEWER_ID` (pessoa revisora do feedback de entrevista)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Revisoes pendentes
```sql
SELECT fr.REVIEWER_ID, fr.REVIEW_STATUS
FROM   IRC_IM_FEEDBK_REVIEWS fr WHERE fr.REVIEW_STATUS = 'PENDING';
```

### Filtros comuns
- `REVIEW_STATUS = 'PENDING'` — Pendentes
---

## Observacoes

- Permite multiplas revisoes por feedback.
---

## Referencias

- [Oracle Docs -- IRC_IM_FEEDBK_REVIEWS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircimfeedbkreviews.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| FEEDBACK_REQUEST_ID | FeedbackRequestId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| PERSON_ID | PersonId | — |
| REVIEW_DATE | ReviewDate | ✅ |
