---
id: DOC-HCM-491
doc_type: system-doc
title: "IRC_IM_FEEDBACKS — Feedbacks de Entrevistas"
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
  - interview-feedback
  - irc-recruiting
aliases:
  - IRC_IM_FEEDBACKS
  - irc_im_feedbacks
  - im-feedbacks
  - im-feedbacks-hcm
  - irc-im-feedbacks
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_IM_FEEDBACKS

## Visao Geral

**Feedbacks** coletados em entrevistas. Avaliacao de entrevistadores sobre candidatos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Avaliacao:** Feedbacks estruturados de entrevistas.
- **Decisao:** Base para decisoes de contratacao.
- **Compliance:** Rastreabilidade de avaliacoes.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | IM_FEEDBACK_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟡 80% |
| 4 | INTERVIEWER_ID | NUMBER(18) | NULL | FK | Entrevistador | PER_ALL_PEOPLE_F | 🟡 80% |
| 5 | OVERALL_RATING | NUMBER | NULL | Dados | Nota geral | — | 🟡 70% |
| 6 | FEEDBACK_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 7 | SUBMISSION_DATE | TIMESTAMP | NULL | Dados | Data de submissao | — | 🟡 75% |
| 8 | COMMENTS | VARCHAR2(4000) | NULL | Dados | Comentarios | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato avaliado na entrevista)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao da entrevista avaliada)
- [[per_all_people_f]] — via `INTERVIEWER_ID` (entrevistador que deu o feedback)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Feedbacks de um candidato
```sql
SELECT f.OVERALL_RATING, f.FEEDBACK_STATUS, f.COMMENTS
FROM   IRC_IM_FEEDBACKS f
WHERE  f.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `FEEDBACK_STATUS = 'SUBMITTED'` — Submetidos
---

## Observacoes

- Feedbacks contem dados subjetivos — confidencialidade.
- Multiplos entrevistadores por candidato.
---

## Referencias

- [Oracle Docs -- IRC_IM_FEEDBACKS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircimfeedbacks.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
