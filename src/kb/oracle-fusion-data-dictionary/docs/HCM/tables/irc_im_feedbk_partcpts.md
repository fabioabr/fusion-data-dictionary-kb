---
id: DOC-HCM-492
doc_type: system-doc
title: "IRC_IM_FEEDBK_PARTCPTS — Participantes de Feedback"
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
  - feedback-participants
  - irc-recruiting
aliases:
  - IRC_IM_FEEDBK_PARTCPTS
  - irc_im_feedbk_partcpts
  - im-feedbk-partcpts
  - im-feedbk-hcm
  - irc-im-feedbk-partcpts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_IM_FEEDBK_PARTCPTS

## Visao Geral

**Participantes** de cada feedback de entrevista.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Participacao:** Registro de envolvidos na avaliacao.
- **Painel:** Composicao do grupo avaliador.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FEEDBK_PARTCPT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | IM_FEEDBACK_ID | NUMBER(18) | NOT NULL | FK | Feedback | IRC_IM_FEEDBACKS | 🟢 85% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Participante | PER_ALL_PEOPLE_F | 🟡 80% |
| 4 | PARTICIPANT_ROLE | VARCHAR2(30) | NULL | Classificacao | Papel | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_im_feedbacks]] — via `IM_FEEDBACK_ID` (feedback de entrevista do participante)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa participante da entrevista)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Participantes de um feedback
```sql
SELECT fp.PERSON_ID, fp.PARTICIPANT_ROLE
FROM   IRC_IM_FEEDBK_PARTCPTS fp WHERE fp.IM_FEEDBACK_ID = :p_id;
```

### Filtros comuns
- `IM_FEEDBACK_ID = :id` — Por feedback
---

## Observacoes

- PARTICIPANT_ROLE diferencia entrevistadores e observadores.
---

## Referencias

- [Oracle Docs -- IRC_IM_FEEDBK_PARTCPTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircimfeedbkpartcpts.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| FEEDBACK_ID | FeedbackId1 | — |
| FEEDBACK_PARTICIPANT_ID | FeedbackParticipantId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NOTES | Notes | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTICIPANT_ID | ParticipantId | — |
| QSTNR_VERSION_NUM | QstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
