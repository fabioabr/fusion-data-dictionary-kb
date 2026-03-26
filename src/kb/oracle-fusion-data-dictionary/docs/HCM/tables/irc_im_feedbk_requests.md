---
id: DOC-HCM-493
doc_type: system-doc
title: "IRC_IM_FEEDBK_REQUESTS — Solicitacoes de Feedback"
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
  - feedback-requests
  - irc-recruiting
aliases:
  - IRC_IM_FEEDBK_REQUESTS
  - irc_im_feedbk_requests
  - im-feedbk-requests
  - im-feedbk-hcm
  - irc-im-feedbk-requests
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_IM_FEEDBK_REQUESTS

## Visao Geral

**Solicitacoes de feedback** enviadas a entrevistadores.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de solicitacoes:** Controle de feedbacks pendentes.
- **SLA:** Tempo de resposta dos entrevistadores.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FEEDBK_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | IM_FEEDBACK_ID | NUMBER(18) | NULL | FK | Feedback esperado | IRC_IM_FEEDBACKS | 🟡 80% |
| 3 | REQUESTEE_ID | NUMBER(18) | NULL | FK | Pessoa solicitada | PER_ALL_PEOPLE_F | 🟡 80% |
| 4 | REQUEST_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 5 | REQUEST_DATE | TIMESTAMP | NULL | Dados | Data da solicitacao | — | 🟡 75% |
| 6 | DUE_DATE | DATE | NULL | Dados | Prazo | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_im_feedbacks]] — via `IM_FEEDBACK_ID` (feedback vinculado a solicitacao)
- [[per_all_people_f]] — via `REQUESTEE_ID` (pessoa solicitada para feedback de entrevista)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Solicitacoes pendentes
```sql
SELECT fr.REQUESTEE_ID, fr.REQUEST_STATUS, fr.DUE_DATE
FROM   IRC_IM_FEEDBK_REQUESTS fr WHERE fr.REQUEST_STATUS = 'PENDING';
```

### Filtros comuns
- `REQUEST_STATUS = 'PENDING'` — Pendentes
---

## Observacoes

- DUE_DATE permite lembretes automaticos.
---

## Referencias

- [Oracle Docs -- IRC_IM_FEEDBK_REQUESTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircimfeedbkrequests.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
