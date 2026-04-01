---
id: DOC-HCM-147
doc_type: system-doc
title: "HRA_FEEDBACK_REQUEST — Solicitações de Feedback"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - performance-management
  - feedback-request
  - avaliacao
  - hra
aliases:
  - HRA_FEEDBACK_REQUEST
  - hra_feedback_request
  - hra-feedback-request
  - DOC-HCM-147
  - solicitações-de-feedback
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_FEEDBACK_REQUEST

## 📌 Visão Geral

Armazena os **registros de solicitações de feedback de performance** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de solicitações de feedback de performance:** Registro e controle operacional.
- **Workflow de avaliação:** Suporte ao processo de avaliação de performance.
- **Rastreabilidade:** Histórico completo de ações e decisões.
- **Relatórios de performance:** Dados para dashboards e análises.
- **Compliance:** Documentação de processos de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FEEDBACK_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 80% |
| 3 | EVALUATION_ID | NUMBER(18) | NULL | FK | Avaliação associada | [[hra_evaluations]] | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto | Descrição | — | 🟡 75% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da solicitacao de feedback)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao da solicitacao de feedback)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.FEEDBACK_REQUEST_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_FEEDBACK_REQUEST r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.FEEDBACK_REQUEST_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_FEEDBACK_REQUEST r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de solicitações de feedback de performance.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[feedbackrequestextractpvo|FeedbackRequestExtractPVO]] (HCM · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DUE_DATE | DueDate | ✅ |
| DUE_DATE_ALERT_SENT | DueDateAlertSent | ✅ |
| FEEDBACK_REQ_ID | FeedbackReqId | ✅ |
| FEEDBACK_REQ_TMPL_ID | FeedbackReqTmplId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MESSAGE_TEXT | MessageText | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PARTICIPANT_PERSON_ID | ParticipantPersonId | ✅ |
| REQUESTED_BY_PERSON_ID | RequestedByPersonId | ✅ |
| REQUESTED_FOR_PERSON_ID | RequestedForPersonId | ✅ |
| SHARE_WITH_MGR_FLAG | ShareWithMgrFlag | ✅ |
| SHARE_WITH_WKR_FLAG | ShareWithWkrFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_FEEDBACK_REQUEST](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrafeedbackrequest.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
