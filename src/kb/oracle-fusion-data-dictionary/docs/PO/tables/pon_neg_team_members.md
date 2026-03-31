---
id: DOC-PO-026
doc_type: system-doc
title: "PON_NEG_TEAM_MEMBERS — Membros da Equipe de Negociação"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - negotiation
  - team-members
  - sourcing
  - collaboration
aliases:
  - PON_NEG_TEAM_MEMBERS
  - pon_neg_team_members
  - membros-equipe-negociacao
  - negotiation-team-members
  - pon-team-members
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_NEG_TEAM_MEMBERS

## 📌 Visão Geral

Armazena os **membros da equipe de negociação** (collaboration team) de cada negociação no módulo Oracle Sourcing. Cada registro representa a associação de um usuário a uma negociação específica, incluindo seu papel (owner, scorer, approver, viewer), permissões e escopo de acesso.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Colaboração em negociações:** Define quem pode participar na avaliação, pontuação e adjudicação de cada negociação.
- **Controle de acesso:** Restringe a visibilidade e ações permitidas por membro da equipe.
- **Workflow de aprovação:** Identifica aprovadores designados para a negociação.
- **Scoring multi-atributo:** Define quais membros podem atribuir notas em avaliações técnicas e comerciais.
- **Auditoria de participação:** Registro completo de quem participou em cada negociação e em qual papel.
- **Segregação de funções:** Garante que papéis conflitantes (ex: criador e aprovador) sejam atribuídos a pessoas diferentes.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TEAM_MEMBER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do membro na equipe | — | 🟢 90% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Identificador da negociação (cabeçalho) | — | 🟢 90% |
| 3 | USER_ID | NUMBER(18) | NOT NULL | FK | Identificador do usuário (FND user) | — | 🟢 90% |
| 4 | PERSON_ID | NUMBER(18) | NULL | FK | Identificador da pessoa (HCM) | — | 🟡 75% |
| 5 | MEMBER_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de membro: OWNER, SCORER, APPROVER, VIEWER, BUYER | — | 🟢 85% |
| 6 | ACCESS_TYPE | VARCHAR2(30) | NULL | Controle | Tipo de acesso: FULL, VIEW_ONLY, RESTRICTED | — | 🟡 70% |
| 7 | SCORING_ENABLED_FLAG | VARCHAR2(1) | NULL | Configuração | Membro pode atribuir scores (Y/N) | — | 🟡 70% |
| 8 | APPROVER_FLAG | VARCHAR2(1) | NULL | Configuração | Membro é aprovador (Y/N) | — | 🟡 70% |
| 9 | TASK_NAME | VARCHAR2(240) | NULL | Workflow | Nome da tarefa de workflow atribuída | — | 🟡 60% |
| 10 | MENU_NAME | VARCHAR2(240) | NULL | Segurança | Menu de segurança associado ao membro | — | 🟡 55% |
| 11 | TARGET_DATE | DATE | NULL | Data | Data-alvo para conclusão da tarefa do membro | — | 🟡 60% |
| 12 | COMPLETION_DATE | DATE | NULL | Data | Data em que o membro concluiu sua tarefa | — | 🟡 60% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Tabela de cabeçalho de negociação (PON_AUCTION_HEADERS_ALL) — via `AUCTION_HEADER_ID`
- Tabela de usuários (FND_USER) — via `USER_ID`
- Tabela de pessoas HCM — via `PERSON_ID`

### Tabelas-filha (FK de saída)
- Registros de scoring por membro (PON_BID_SCORE_DETAILS) — avaliações atribuídas pelo membro

---

## 📎 Uso Típico

### Membros de uma negociação específica
```sql
SELECT tm.USER_ID, tm.MEMBER_TYPE, tm.ACCESS_TYPE,
       tm.SCORING_ENABLED_FLAG, tm.APPROVER_FLAG
FROM   PON_NEG_TEAM_MEMBERS tm
WHERE  tm.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY tm.MEMBER_TYPE;
```

### Negociações onde um usuário é aprovador
```sql
SELECT tm.AUCTION_HEADER_ID, tm.MEMBER_TYPE, tm.TARGET_DATE,
       tm.COMPLETION_DATE
FROM   PON_NEG_TEAM_MEMBERS tm
WHERE  tm.USER_ID = :p_user_id
  AND  tm.APPROVER_FLAG = 'Y';
```

### Equipe de scoring
```sql
SELECT tm.USER_ID, tm.PERSON_ID, tm.MEMBER_TYPE,
       tm.COMPLETION_DATE
FROM   PON_NEG_TEAM_MEMBERS tm
WHERE  tm.AUCTION_HEADER_ID = :p_auction_header_id
  AND  tm.SCORING_ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- O campo `MEMBER_TYPE` é o principal discriminador de papel: **OWNER** (criador/responsável), **SCORER** (avaliador), **APPROVER** (aprovador), **VIEWER** (somente leitura), **BUYER** (comprador adicional).
- A combinação `AUCTION_HEADER_ID` + `USER_ID` pode ser unique, garantindo que um usuário não apareça duplicado na mesma negociação.
- Membros com `ACCESS_TYPE = 'VIEW_ONLY'` podem ver a negociação mas não podem alterar lances, scores ou aprovar.
- Em negociações two-part (técnica + comercial), os scorers podem ter acesso restrito à parte técnica até que a abertura comercial seja autorizada.
- A remoção de um membro da equipe pode ser soft-delete (flag) ou hard-delete, dependendo do status da negociação.

---

## 🔗 PVOs Relacionados

### [[negotiationcollaborationteamextractpvo|NegotiationCollaborationTeamExtractPVO]] (PO · BICC: 19/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | AccessType | ✅ |
| APPROVAL_STATUS | ApprovalStatus | ✅ |
| APPROVER_FLAG | ApproverFlag | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| COMPLETION_DATE | CompletionDate | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_AMENDMENT_UPDATE | LastAmendmentUpdate | ✅ |
| LAST_NOTIFIED_DATE | LastNotifiedDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MEMBER_TYPE | MemberType | ✅ |
| MODIFIED_FLAG | ModifiedFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PersonId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| TARGET_DATE | TargetDate | ✅ |
| TASK_NAME | TaskName | ✅ |

### [[negotiationcollaborationteampvo|NegotiationCollaborationTeamPVO]] (PO · BICC: 8/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | AccessType | ✅ |
| APPROVAL_STATUS | NegotiationCollaborationApprovalStatus | — |
| APPROVER_FLAG | NegotiationCollaborationApproverFlag | — |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| COMPLETION_DATE | NegotiationCollaborationCompletionDate | ✅ |
| CREATED_BY | NegotiationCollaborationCreatedBy | — |
| CREATION_DATE | NegotiationCollaborationCreationDate | ✅ |
| LAST_AMENDMENT_UPDATE | NegotiationCollaborationLastAmendmentUpdate | — |
| LAST_NOTIFIED_DATE | NegotiationCollaborationLastNotifiedDate | — |
| LAST_UPDATE_DATE | NegotiationCollaborationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationCollaborationLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationCollaborationLastUpdatedBy | — |
| MEMBER_TYPE | NegotiationCollaborationMemberType | — |
| MODIFIED_FLAG | NegotiationCollaborationModifiedFlag | — |
| OBJECT_VERSION_NUMBER | NegotiationCollaborationObjectVersionNumber | — |
| PERSON_ID | NegotiationCollaborationPersonId | — |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| TARGET_DATE | NegotiationCollaborationTargetDate | ✅ |
| TASK_NAME | NegotiationCollaborationTaskName | ✅ |

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
