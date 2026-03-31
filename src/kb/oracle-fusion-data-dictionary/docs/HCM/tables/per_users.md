---
id: DOC-HCM-717
doc_type: system-doc
title: "PER_USERS — Usuários do Sistema"
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
  - segurança
  - usuários
  - access-management
aliases:
  - PER_USERS
  - per_users
  - per-users
  - usuários-do-sistema
  - users-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_USERS

## Visão Geral

Armazena os **usuários do sistema** HCM, incluindo credenciais, status de conta e vinculação com a pessoa (PERSON_ID). Tabela central para controle de acesso.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de acesso** — controla quem pode acessar o sistema HCM.
- **Vinculação pessoa-usuário** — associa o usuário do sistema à pessoa no cadastro de RH.
- **Auditoria de acessos** — rastreia criação e desativação de contas.
- **Provisionamento** — base para criação automática de contas durante onboarding.
- **Segurança** — controle de status de contas (ativa, bloqueada, expirada).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do usuário | — | 🟢 90% |
| 2 | USER_NAME | VARCHAR2(100) | NOT NULL | Identificação | Nome de login do usuário | — | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa vinculada ao usuário | PER_ALL_PEOPLE_F | 🟢 85% |
| 4 | START_DATE | DATE | NOT NULL | Vigência | Data de início da conta | — | 🟢 85% |
| 5 | END_DATE | DATE | NULL | Vigência | Data de encerramento da conta | — | 🟢 85% |
| 6 | SUSPENDED | VARCHAR2(1) | NULL | Status | Indica se a conta está suspensa (Y/N) | — | 🟡 75% |
| 7 | EMAIL_ADDRESS | VARCHAR2(240) | NULL | Contato | E-mail do usuário | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa vinculada)

### Tabelas-filha (FK de saída)
- [[per_user_history]] — via `USER_ID` (histórico de alterações do usuário)
- [[per_user_roles]] — via `USER_ID` (papéis atribuídos)

---

## Uso Típico

### Usuários ativos com pessoa vinculada
```sql
SELECT u.USER_NAME, u.EMAIL_ADDRESS, p.FULL_NAME
FROM   PER_USERS u
JOIN   PER_ALL_PEOPLE_F p ON u.PERSON_ID = p.PERSON_ID
WHERE  u.SUSPENDED = 'N'
  AND  SYSDATE BETWEEN u.START_DATE AND NVL(u.END_DATE, TO_DATE('4712-12-31','YYYY-MM-DD'));
```

### Filtros comuns
- `SUSPENDED = 'N'` — Apenas contas ativas
- `END_DATE IS NULL` — Contas sem data de expiração

---

## Observações

- A vinculação USER_ID -> PERSON_ID é fundamental para associar acessos a colaboradores.
- Contas podem existir sem PERSON_ID (contas de serviço/sistema).
- O campo SUSPENDED permite desativar temporariamente sem excluir a conta.
- Histórico de alterações rastreado em PER_USER_HISTORY.

---

## Referências

- [Oracle Docs — PER_USERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perusers.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[accountcontact|AccountContact]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserCreatedByCreatedBy | — |
| CREATION_DATE | UserCreatedByCreationDate | — |
| LAST_UPDATE_DATE | UserLastUpdatedByLastUpdateDate | — |
| LAST_UPDATED_BY | UserLastUpdatedByLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserLastUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserLastUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserLastUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserLastUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserLastUpdatedByUsername | — |

### [[accountcontactrelationship|AccountContactRelationShip]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserCreatedByCreatedBy | — |
| CREATION_DATE | UserCreatedByCreationDate | — |
| LAST_UPDATE_DATE | UserLastUpdatedByLastUpdateDate | — |
| LAST_UPDATED_BY | UserLastUpdatedByLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserLastUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserLastUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserLastUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserLastUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserLastUpdatedByUsername | — |

### [[acncertaudithistorypvo|ACNCertAuditHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | AudHistCreatedByObjectVerNumber | — |
| PERSON_ID | AudHistCreatedByPersonId | — |
| USER_GUID | AudHistCreatedByUserGuid | — |
| USER_ID | AudHistCreatedByUserId | — |
| USERNAME | AudHistCreatedByUsername | — |

### [[acncertificationpvo|ACNCertificationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CertCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CertRoleUserDecisionByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CertRoleUserUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CertUserUpdatedByObjectVerNumber | — |
| PERSON_ID | CertCreatedByPersonId | — |
| PERSON_ID | CertRoleUserDecisionByPersonId | — |
| PERSON_ID | CertRoleUserUpdatedByPersonId | — |
| PERSON_ID | CertUserUpdatedByPersonId | — |
| USER_GUID | CertCreatedByUserGuid | — |
| USER_GUID | CertRoleUserDecisionByUserGuid | — |
| USER_GUID | CertRoleUserUpdatedByUserGuid | — |
| USER_GUID | CertUserUpdatedByUserGuid | — |
| USER_ID | CertCreatedByUserId | — |
| USER_ID | CertRoleUserDecisionByUserId | — |
| USER_ID | CertRoleUserUpdatedByUserId | — |
| USER_ID | CertUserUpdatedByUserId | — |
| USERNAME | CertCreatedByUsername | — |
| USERNAME | CertRoleUserDecisionByUsername | — |
| USERNAME | CertRoleUserUpdatedByUsername | — |
| USERNAME | CertUserUpdatedByUsername | — |

### [[acncommentspvo|ACNCommentsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVerNumber | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[additionbasepvo|AdditionBasePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 1/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ApprovedUserActiveFlag | — |
| END_DATE | ApprovedUserEndDate | — |
| HR_TERMINATED | ApprovedUserHrTerminated | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber8 | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| START_DATE | ApprovedUserStartDate | — |
| SUSPENDED | ApprovedUserSuspended | — |
| USER_GUID | ApprovedUserUserGuid | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | ApprovedUserUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | ApprovedUserUsername | ✅ |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ApprovedUserActiveFlag | — |
| END_DATE | ApprovedUserEndDate | — |
| HR_TERMINATED | ApprovedUserHrTerminated | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| START_DATE | ApprovedUserStartDate | — |
| SUSPENDED | ApprovedUserSuspended | — |
| USER_GUID | ApprovedUserUserGuid | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | ApprovedUserUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | ApprovedUserUsername | ✅ |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[advancedaccesscontroldetailsrefpvo|AdvancedAccessControlDetailsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmntCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | InvestUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | JobCreatedByObjectVerNumber | — |
| PERSON_ID | CmntCreatedByPersonId | — |
| PERSON_ID | CtrlCreatedByPersonId | — |
| PERSON_ID | CtrlUpdatedByPersonId | — |
| PERSON_ID | InvestUpdatedByPersonId | — |
| PERSON_ID | JobCreatedByPersonId | — |
| USER_GUID | CmntCreatedByUserGuid | — |
| USER_GUID | CtrlCreatedByUserGuid | — |
| USER_GUID | CtrlUpdatedByUserGuid | — |
| USER_GUID | InvestUpdatedByUserGuid | — |
| USER_GUID | JobCreatedByUserGuid | — |
| USER_ID | CmntCreatedByUserId | — |
| USER_ID | CtrlCreatedByUserId | — |
| USER_ID | CtrlUpdatedByUserId | — |
| USER_ID | InvestUpdatedByUserId | — |
| USER_ID | JobCreatedByUserId | — |
| USERNAME | CmntCreatedByUsername | — |
| USERNAME | CtrlCreatedByUsername | — |
| USERNAME | CtrlUpdatedByUsername | — |
| USERNAME | InvestUpdatedByUsername | — |
| USERNAME | JobCreatedByUsername | — |

### [[advancedtransactioncontroldetailsrefpvo|AdvancedTransactionControlDetailsRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmntCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | InvestUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | JobCreatedByObjectVerNumber | — |
| PERSON_ID | CmntCreatedByPersonId | — |
| PERSON_ID | CtrlCreatedByPersonId | — |
| PERSON_ID | CtrlUpdatedByPersonId | — |
| PERSON_ID | InvestUpdatedByPersonId | — |
| PERSON_ID | JobCreatedByPersonId | — |
| USER_GUID | CmntCreatedByUserGuid | — |
| USER_GUID | CtrlCreatedByUserGuid | — |
| USER_GUID | CtrlUpdatedByUserGuid | — |
| USER_GUID | InvestUpdatedByUserGuid | — |
| USER_GUID | JobCreatedByUserGuid | — |
| USER_ID | CmntCreatedByUserId | — |
| USER_ID | CtrlCreatedByUserId | — |
| USER_ID | CtrlUpdatedByUserId | — |
| USER_ID | InvestUpdatedByUserId | — |
| USER_ID | JobCreatedByUserId | — |
| USERNAME | CmntCreatedByUsername | — |
| USERNAME | CtrlCreatedByUsername | — |
| USERNAME | CtrlUpdatedByUsername | — |
| USERNAME | InvestUpdatedByUsername | — |
| USERNAME | JobCreatedByUsername | — |

### [[advcontrolchangehistorypvo|AdvControlChangeHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CHUpdatedByObjectVerNumber | — |
| PERSON_ID | CHUpdatedByPersonId | — |
| USER_GUID | CHUpdatedByUserGuid | — |
| USER_ID | CHUpdatedByUserId | — |
| USERNAME | CHUpdatedByUsername | — |

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | ✅ |

### [[allocatedchecklistspvo|AllocatedChecklistsPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UsersPEOUserId | — |
| USERNAME | UsersPEOAllocatedContactAdhocUsername | ✅ |

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UsersPEOUserId | — |
| USERNAME | UsersPEOAllocatedContactAdhocUsername | ✅ |

### [[assessmentpvo|AssessmentPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | AsmtUpdatedByObjectVerNumber | — |
| PERSON_ID | AsmtUpdatedByPersonId | — |
| USER_GUID | AsmtUpdatedByUserGuid | — |
| USER_ID | AsmtUpdatedByUserId | — |
| USERNAME | AsmtUpdatedByUsername | — |

### [[assessmentresultpvo|AssessmentResultPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | AsRsApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | AsRsAssessedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | AsRsReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | AsRsUpdatedByObjectVerNumber | — |
| PERSON_ID | AsRsApprovedByPersonId | — |
| PERSON_ID | AsRsAssessedByPersonId | — |
| PERSON_ID | AsRsReviewedByPersonId | — |
| PERSON_ID | AsRsUpdatedByPersonId | — |
| USER_GUID | AsRsApprovedByUserGuid | — |
| USER_GUID | AsRsAssessedByUserGuid | — |
| USER_GUID | AsRsReviewedByUserGuid | — |
| USER_GUID | AsRsUpdatedByUserGuid | — |
| USER_ID | AsRsApprovedByUserId | — |
| USER_ID | AsRsAssessedByUserId | — |
| USER_ID | AsRsReviewedByUserId | — |
| USER_ID | AsRsUpdatedByUserId | — |
| USERNAME | AsRsApprovedByUsername | — |
| USERNAME | AsRsAssessedByUsername | — |
| USERNAME | AsRsReviewedByUsername | — |
| USERNAME | AsRsUpdatedByUsername | — |

### [[assetinvoicepvo|AssetInvoicePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[balanceactivitypvo|BalanceActivityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | BalActUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TrHdrUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserObjectVersionNumber | — |
| PERSON_ID | BalActUserCreatedByPersonId | — |
| PERSON_ID | TrHdrUserCreatedByPersonId | — |
| PERSON_ID | UserPersonId | — |
| USER_GUID | BalActUserCreatedByUserGuid | — |
| USER_GUID | TrHdrUserCreatedByUserGuid | — |
| USER_GUID | UserUserGuid | — |
| USER_ID | BalActUserCreatedByUserId | — |
| USER_ID | TrHdrUserCreatedByUserId | — |
| USER_ID | UserUserId | — |
| USERNAME | BalActUserCreatedByUsername | — |
| USERNAME | TrHdrUserCreatedByUsername | — |

### [[balancepvo|BalancePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LastUpdatedByUserCreatedBy | — |
| CREATION_DATE | LastUpdatedByUserCreationDate | — |
| LAST_UPDATE_DATE | LastUpdatedByUserLastUpdateDate | — |
| LAST_UPDATED_BY | LastUpdatedByUserLastUpdatedBy | — |
| PERSON_ID | LastUpdatedByUserPersonId | — |
| USER_ID | LastUpdatedByUserUserId | — |
| USERNAME | LastUpdatedByUserUsername | — |

### [[bankaccountbalanceavailabilitypvo|BankAccountBalanceAvailabilityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bankaccountbalancepvo|BankAccountBalancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bankstatementheaderpvo|BankStatementHeaderPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bankstatementlineavailabilitypvo|BankStatementLineAvailabilityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bankstatementlinechargespvo|BankStatementLineChargesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bankstatementlinespvo|BankStatementLinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[billinglinedetailspvo|BillingLineDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[bookcontrolpvo|BookControlPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[cashadvanceapplicationpvo|CashAdvanceApplicationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CashAdvCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CashAdvUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | CashAdvCreatedByPersonId | — |
| PERSON_ID | CashAdvUserUpdatedByPersonId | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | CashAdvCreatedByUserGuid | — |
| USER_GUID | CashAdvUserUpdatedByUserGuid | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | CashAdvCreatedByUserId | — |
| USER_ID | CashAdvUserUpdatedByUserId | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | CashAdvCreatedByUsername | — |
| USERNAME | CashAdvUserUpdatedByUsername | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[cashadvancepvo|CashAdvancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[categorybookdefaultpvo|CategoryBookDefaultPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[categorybookpvo|CategoryBookPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UsersPEO1UserId | — |
| USER_ID | UsersPEOUserId | — |
| USERNAME | UsersPEO1ChecklistTaskAdhocUsername | — |
| USERNAME | UsersPEOAdhocUserUserName | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UsersPEOUserId | — |
| USERNAME | UsersPEOAdhocUserUserName | ✅ |

### [[commentspvo|CommentsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVerNumber | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[controlpvo|ControlPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CtrlApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlUpdatedByObjectVerNumber | — |
| PERSON_ID | CtrlApprovedByPersonId | — |
| PERSON_ID | CtrlCreatedByPersonId | — |
| PERSON_ID | CtrlReviewedByPersonId | — |
| PERSON_ID | CtrlUpdatedByPersonId | — |
| USER_GUID | CtrlApprovedByUserGuid | — |
| USER_GUID | CtrlCreatedByUserGuid | — |
| USER_GUID | CtrlReviewedByUserGuid | — |
| USER_GUID | CtrlUpdatedByUserGuid | — |
| USER_ID | CtrlApprovedByUserId | — |
| USER_ID | CtrlCreatedByUserId | — |
| USER_ID | CtrlReviewedByUserId | — |
| USER_ID | CtrlUpdatedByUserId | — |
| USERNAME | CtrlApprovedByUsername | — |
| USERNAME | CtrlCreatedByUsername | — |
| USERNAME | CtrlReviewedByUsername | — |
| USERNAME | CtrlUpdatedByUsername | — |

### [[corporatecardpvo|CorporateCardPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[corporatecardtransactionpvo|CorporateCardTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CardCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CardUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TrnxCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TrnxUserUpdatedByObjectVersionNumber | — |
| PERSON_ID | CardCreatedByPersonId | — |
| PERSON_ID | CardUserUpdatedByPersonId | — |
| PERSON_ID | TrnxCreatedByPersonId | — |
| PERSON_ID | TrnxUserUpdatedByPersonId | — |
| USER_GUID | CardCreatedByUserGuid | — |
| USER_GUID | CardUserUpdatedByUserGuid | — |
| USER_GUID | TrnxCreatedByUserGuid | — |
| USER_GUID | TrnxUserUpdatedByUserGuid | — |
| USER_ID | CardCreatedByUserId | — |
| USER_ID | CardUserUpdatedByUserId | — |
| USER_ID | TrnxCreatedByUserId | — |
| USER_ID | TrnxUserUpdatedByUserId | — |
| USERNAME | CardCreatedByUsername | — |
| USERNAME | CardUserUpdatedByUsername | — |
| USERNAME | TrnxCreatedByUsername | — |
| USERNAME | TrnxUserUpdatedByUsername | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[creditmemorequestpvo|CreditMemoRequestPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[customercontractheaderspvo|CustomerContractHeadersPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[dimcontrolpvo|DimControlPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CtrlApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | CtrlUpdatedByObjectVerNumber | — |
| PERSON_ID | CtrlApprovedByPersonId | — |
| PERSON_ID | CtrlCreatedByPersonId | — |
| PERSON_ID | CtrlReviewedByPersonId | — |
| PERSON_ID | CtrlUpdatedByPersonId | — |
| USER_GUID | CtrlApprovedByUserGuid | — |
| USER_GUID | CtrlCreatedByUserGuid | — |
| USER_GUID | CtrlReviewedByUserGuid | — |
| USER_GUID | CtrlUpdatedByUserGuid | — |
| USER_ID | CtrlApprovedByUserId | — |
| USER_ID | CtrlCreatedByUserId | — |
| USER_ID | CtrlReviewedByUserId | — |
| USER_ID | CtrlUpdatedByUserId | — |
| USERNAME | CtrlApprovedByUsername | — |
| USERNAME | CtrlCreatedByUsername | — |
| USERNAME | CtrlReviewedByUsername | — |
| USERNAME | CtrlUpdatedByUsername | — |

### [[dimissuepvo|DimIssuePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueUpdatedByObjectVerNumber | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | IssueApprovedByPersonId | — |
| PERSON_ID | IssueCreatedByPersonId | — |
| PERSON_ID | IssueReviewedByPersonId | — |
| PERSON_ID | IssueUpdatedByPersonId | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | IssueApprovedByUserGuid | — |
| USER_GUID | IssueCreatedByUserGuid | — |
| USER_GUID | IssueReviewedByUserGuid | — |
| USER_GUID | IssueUpdatedByUserGuid | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | IssueApprovedByUserId | — |
| USER_ID | IssueCreatedByUserId | — |
| USER_ID | IssueReviewedByUserId | — |
| USER_ID | IssueUpdatedByUserId | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | IssueApprovedByUsername | — |
| USERNAME | IssueCreatedByUsername | — |
| USERNAME | IssueReviewedByUsername | — |
| USERNAME | IssueUpdatedByUsername | — |

### [[dimprocesspvo|DimProcessPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ProcApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | ProcCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | ProcReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | ProcUpdatedByObjectVerNumber | — |
| PERSON_ID | ProcApprovedByPersonId | — |
| PERSON_ID | ProcCreatedByPersonId | — |
| PERSON_ID | ProcReviewedByPersonId | — |
| PERSON_ID | ProcUpdatedByPersonId | — |
| USER_GUID | ProcApprovedByUserGuid | — |
| USER_GUID | ProcCreatedByUserGuid | — |
| USER_GUID | ProcReviewedByUserGuid | — |
| USER_GUID | ProcUpdatedByUserGuid | — |
| USER_ID | ProcApprovedByUserId | — |
| USER_ID | ProcCreatedByUserId | — |
| USER_ID | ProcReviewedByUserId | — |
| USER_ID | ProcUpdatedByUserId | — |
| USERNAME | ProcApprovedByUsername | — |
| USERNAME | ProcCreatedByUsername | — |
| USERNAME | ProcReviewedByUsername | — |
| USERNAME | ProcUpdatedByUsername | — |

### [[dimremediationplanpvo|DimRemediationPlanPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmntCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnCreatdByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnUpdatedByObjectVerNumber | — |
| PERSON_ID | CmntCreatedByPersonId | — |
| PERSON_ID | RmPnApprovedByPersonId | — |
| PERSON_ID | RmPnCreatedByPersonId | — |
| PERSON_ID | RmPnReviewedByPersonId | — |
| PERSON_ID | RmPnUpdatedByPersonId | — |
| USER_GUID | CmntCreatedByUserGuid | — |
| USER_GUID | RmPnApprovedByUserGuid | — |
| USER_GUID | RmPnCreatedByUserGuid | — |
| USER_GUID | RmPnReviewedByUserGuid | — |
| USER_GUID | RmPnUpdatedByUserGuid | — |
| USER_ID | CmntCreatedByUserId | — |
| USER_ID | RmPnApprovedByUserId | — |
| USER_ID | RmPnCreatedByUserId | — |
| USER_ID | RmPnReviewedByUserId | — |
| USER_ID | RmPnUpdatedByUserId | — |
| USERNAME | CmntCreatedByUsername | — |
| USERNAME | RmPnApprovedByUsername | — |
| USERNAME | RmPnCreatedByUsername | — |
| USERNAME | RmPnReviewedByUsername | — |
| USERNAME | RmPnUpdatedByUsername | — |

### [[dimriskpvo|DimRiskPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | RiskApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RiskCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RiskReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RiskUpdatedByObjectVerNumber | — |
| PERSON_ID | RiskApprovedByPersonId | — |
| PERSON_ID | RiskCreatedByPersonId | — |
| PERSON_ID | RiskReviewedByPersonId | — |
| PERSON_ID | RiskUpdatedByPersonId | — |
| USER_GUID | RiskApprovedByUserGuid | — |
| USER_GUID | RiskCreatedByUserGuid | — |
| USER_GUID | RiskReviewedByUserGuid | — |
| USER_GUID | RiskUpdatedByUserGuid | — |
| USER_ID | RiskApprovedByUserId | — |
| USER_ID | RiskCreatedByUserId | — |
| USER_ID | RiskReviewedByUserId | — |
| USER_ID | RiskUpdatedByUserId | — |
| USERNAME | RiskApprovedByUsername | — |
| USERNAME | RiskCreatedByUsername | — |
| USERNAME | RiskReviewedByUsername | — |
| USERNAME | RiskUpdatedByUsername | — |

### [[distributioninitlinepvo|DistributionInitLinePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[distributionrectlinepvo|DistributionRectLinePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[effectivepriceperiodpvo|EffectivePricePeriodPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[entitlementpvo|EntitlementPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | EntCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | EntUpdatedByObjectVerNumber | — |
| PERSON_ID | EntCreatedByPersonId | — |
| PERSON_ID | EntUpdatedByPersonId | — |
| USER_GUID | EntCreatedByUserGuid | — |
| USER_GUID | EntUpdatedByUserGuid | — |
| USER_ID | EntCreatedByUserId | — |
| USER_ID | EntUpdatedByUserId | — |
| USERNAME | EntCreatedByUsername | — |
| USERNAME | EntUpdatedByUsername | — |

### [[expenseattendeedetailspvo|ExpenseAttendeeDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ExpAttendeeCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpAttendeeUpdatedByObjectVersionNumber | — |
| PERSON_ID | ExpAttendeeCreatedByPersonId | — |
| PERSON_ID | ExpAttendeeUpdatedByPersonId | — |
| USER_GUID | ExpAttendeeCreatedByUserGuid | — |
| USER_GUID | ExpAttendeeUpdatedByUserGuid | — |
| USER_ID | ExpAttendeeCreatedByUserId | — |
| USER_ID | ExpAttendeeUpdatedByUserId | — |
| USERNAME | ExpAttendeeCreatedByUsername | — |
| USERNAME | ExpAttendeeUpdatedByUsername | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ExpAttendeeCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpAttendeeUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpHdrUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenHdrCreatedByObjectVersionNumber | — |
| PERSON_ID | ExpAttendeeCreatedByPersonId | — |
| PERSON_ID | ExpAttendeeUpdatedByPersonId | — |
| PERSON_ID | ExpHdrUserUpdatedByPersonId | — |
| PERSON_ID | ExpUserUpdatedByPersonId | — |
| PERSON_ID | ExpenCreatedByPersonId | — |
| PERSON_ID | ExpenHdrCreatedByPersonId | — |
| USER_GUID | ExpAttendeeCreatedByUserGuid | — |
| USER_GUID | ExpAttendeeUpdatedByUserGuid | — |
| USER_GUID | ExpHdrUserUpdatedByUserGuid | — |
| USER_GUID | ExpUserUpdatedByUserGuid | — |
| USER_GUID | ExpenCreatedByUserGuid | — |
| USER_GUID | ExpenHdrCreatedByUserGuid | — |
| USER_ID | ExpAttendeeCreatedByUserId | — |
| USER_ID | ExpAttendeeUpdatedByUserId | — |
| USER_ID | ExpHdrUserUpdatedByUserId | — |
| USER_ID | ExpUserUpdatedByUserId | — |
| USER_ID | ExpenCreatedByUserId | — |
| USER_ID | ExpenHdrCreatedByUserId | — |
| USERNAME | ExpAttendeeCreatedByUsername | — |
| USERNAME | ExpAttendeeUpdatedByUsername | — |
| USERNAME | ExpHdrUserUpdatedByUsername | — |
| USERNAME | ExpUserUpdatedByUsername | — |
| USERNAME | ExpenCreatedByUsername | — |
| USERNAME | ExpenHdrCreatedByUsername | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | DistUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | DistUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpHdrUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenHdrCreatedByObjectVersionNumber | — |
| PERSON_ID | DistUserCreatedByPersonId | — |
| PERSON_ID | DistUserUpdatedByPersonId | — |
| PERSON_ID | ExpHdrUserUpdatedByPersonId | — |
| PERSON_ID | ExpUserUpdatedByPersonId | — |
| PERSON_ID | ExpenCreatedByPersonId | — |
| PERSON_ID | ExpenHdrCreatedByPersonId | — |
| USER_GUID | DistUserCreatedByUserGuid | — |
| USER_GUID | DistUserUpdatedByUserGuid | — |
| USER_GUID | ExpHdrUserUpdatedByUserGuid | — |
| USER_GUID | ExpUserUpdatedByUserGuid | — |
| USER_GUID | ExpenCreatedByUserGuid | — |
| USER_GUID | ExpenHdrCreatedByUserGuid | — |
| USER_ID | DistUserCreatedByUserId | — |
| USER_ID | DistUserUpdatedByUserId | — |
| USER_ID | ExpHdrUserUpdatedByUserId | — |
| USER_ID | ExpUserUpdatedByUserId | — |
| USER_ID | ExpenCreatedByUserId | — |
| USER_ID | ExpenHdrCreatedByUserId | — |
| USERNAME | DistUserCreatedByUsername | — |
| USERNAME | DistUserUpdatedByUsername | — |
| USERNAME | ExpHdrUserUpdatedByUsername | — |
| USERNAME | ExpUserUpdatedByUsername | — |
| USERNAME | ExpenCreatedByUsername | — |
| USERNAME | ExpenHdrCreatedByUsername | — |

### [[expensepvo|ExpensePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ExpHdrUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenHdrCreatedByObjectVersionNumber | — |
| PERSON_ID | ExpHdrUserUpdatedByPersonId | — |
| PERSON_ID | ExpUserUpdatedByPersonId | — |
| PERSON_ID | ExpenCreatedByPersonId | — |
| PERSON_ID | ExpenHdrCreatedByPersonId | — |
| USER_GUID | ExpHdrUserUpdatedByUserGuid | — |
| USER_GUID | ExpUserUpdatedByUserGuid | — |
| USER_GUID | ExpenCreatedByUserGuid | — |
| USER_GUID | ExpenHdrCreatedByUserGuid | — |
| USER_ID | ExpHdrUserUpdatedByUserId | — |
| USER_ID | ExpUserUpdatedByUserId | — |
| USER_ID | ExpenCreatedByUserId | — |
| USER_ID | ExpenHdrCreatedByUserId | — |
| USERNAME | ExpHdrUserUpdatedByUsername | — |
| USERNAME | ExpUserUpdatedByUsername | — |
| USERNAME | ExpenCreatedByUsername | — |
| USERNAME | ExpenHdrCreatedByUsername | — |

### [[expensereporthistorypvo|ExpenseReportHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ExpRepPrcCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpRepPrcUpdatedByObjectVersionNumber | — |
| PERSON_ID | ExpRepPrcCreatedByPersonId | — |
| PERSON_ID | ExpRepPrcUpdatedByPersonId | — |
| USER_GUID | ExpRepPrcCreatedByUserGuid | — |
| USER_GUID | ExpRepPrcUpdatedByUserGuid | — |
| USER_ID | ExpRepPrcCreatedByUserId | — |
| USER_ID | ExpRepPrcUpdatedByUserId | — |
| USERNAME | ExpRepPrcCreatedByUsername | — |
| USERNAME | ExpRepPrcUpdatedByUsername | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ExpHdrUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpenHdrCreatedByObjectVersionNumber | — |
| PERSON_ID | ExpHdrUserUpdatedByPersonId | — |
| PERSON_ID | ExpUserUpdatedByPersonId | — |
| PERSON_ID | ExpenCreatedByPersonId | — |
| PERSON_ID | ExpenHdrCreatedByPersonId | — |
| USER_GUID | ExpHdrUserUpdatedByUserGuid | — |
| USER_GUID | ExpUserUpdatedByUserGuid | — |
| USER_GUID | ExpenCreatedByUserGuid | — |
| USER_GUID | ExpenHdrCreatedByUserGuid | — |
| USER_ID | ExpHdrUserUpdatedByUserId | — |
| USER_ID | ExpUserUpdatedByUserId | — |
| USER_ID | ExpenCreatedByUserId | — |
| USER_ID | ExpenHdrCreatedByUserId | — |
| USERNAME | ExpHdrUserUpdatedByUsername | — |
| USERNAME | ExpUserUpdatedByUsername | — |
| USERNAME | ExpenCreatedByUsername | — |
| USERNAME | ExpenHdrCreatedByUsername | — |

### [[externaltransactionspvo|ExternalTransactionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[fabalancesextractpvo|FaBalancesExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[fdinterfaceexceptionsp1|FDInterfaceExceptionsP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FDHeaderIntrEOCreatedByUserPActiveFlag | — |
| ACTIVE_FLAG | FDHeaderIntrLastUpdtdByUserPActiveFlag1 | — |
| ACTIVE_FLAG | FDIntHeadersCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FDIntHeadersLUpdatedByUserPEActiveFlag1 | — |
| ACTIVE_FLAG | FDIntLegalProcCreatedByUserPActiveFlag2 | — |
| ACTIVE_FLAG | FDIntLegalProcLUpdatedByUserActiveFlag3 | — |
| ACTIVE_FLAG | FDIntLinesCreatedByUserPEOActiveFlag4 | — |
| ACTIVE_FLAG | FDIntLinesLUpdatedByUserPEOActiveFlag5 | — |
| ACTIVE_FLAG | FDIntRefCreatedByUserPEOActiveFlag6 | — |
| ACTIVE_FLAG | FDIntRefLUpdatedByUserPEOActiveFlag7 | — |
| ACTIVE_FLAG | FDLineIntrEOToCreatedByUserPActiveFlag2 | — |
| ACTIVE_FLAG | FDLineIntrToLastUpdtdByUserPActiveFlag3 | — |
| ACTIVE_FLAG | TaxLineIntrEOCreatedByUserPEActiveFlag | — |
| ACTIVE_FLAG | TaxLineIntrEOLastUpdtdByUserActiveFlag1 | — |
| BUSINESS_GROUP_ID | FDHeaderIntrEOCreatedByUserPBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDHeaderIntrLastUpdtdByUserPBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FDIntHeadersCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDIntHeadersLUpdatedByUserPEBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FDIntLegalProcCreatedByUserPBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | FDIntLegalProcLUpdatedByUserBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | FDIntLinesCreatedByUserPEOBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | FDIntLinesLUpdatedByUserPEOBusinessGroupId5 | — |
| BUSINESS_GROUP_ID | FDIntRefCreatedByUserPEOBusinessGroupId6 | — |
| BUSINESS_GROUP_ID | FDIntRefLUpdatedByUserPEOBusinessGroupId7 | — |
| BUSINESS_GROUP_ID | FDLineIntrEOToCreatedByUserPBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | FDLineIntrToLastUpdtdByUserPBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | TaxLineIntrEOCreatedByUserPEBusinessGroupId | — |
| BUSINESS_GROUP_ID | TaxLineIntrEOLastUpdtdByUserBusinessGroupId1 | — |
| CREATED_BY | FDHeaderIntrEOCreatedByUserPCreatedBy | — |
| CREATED_BY | FDHeaderIntrLastUpdtdByUserPCreatedBy1 | — |
| CREATED_BY | FDIntHeadersCreatedByUserPEOCreatedBy | — |
| CREATED_BY | FDIntHeadersLUpdatedByUserPECreatedBy1 | — |
| CREATED_BY | FDIntLegalProcCreatedByUserPCreatedBy2 | — |
| CREATED_BY | FDIntLegalProcLUpdatedByUserCreatedBy3 | — |
| CREATED_BY | FDIntLinesCreatedByUserPEOCreatedBy4 | — |
| CREATED_BY | FDIntLinesLUpdatedByUserPEOCreatedBy5 | — |
| CREATED_BY | FDIntRefCreatedByUserPEOCreatedBy6 | — |
| CREATED_BY | FDIntRefLUpdatedByUserPEOCreatedBy7 | — |
| CREATED_BY | FDLineIntrEOToCreatedByUserPCreatedBy2 | — |
| CREATED_BY | FDLineIntrToLastUpdtdByUserPCreatedBy3 | — |
| CREATED_BY | TaxLineIntrEOCreatedByUserPECreatedBy | — |
| CREATED_BY | TaxLineIntrEOLastUpdtdByUserCreatedBy1 | — |
| CREATION_DATE | FDHeaderIntrEOCreatedByUserPCreationDate | — |
| CREATION_DATE | FDHeaderIntrLastUpdtdByUserPCreationDate1 | — |
| CREATION_DATE | FDIntHeadersCreatedByUserPEOCreationDate | — |
| CREATION_DATE | FDIntHeadersLUpdatedByUserPECreationDate1 | — |
| CREATION_DATE | FDIntLegalProcCreatedByUserPCreationDate2 | — |
| CREATION_DATE | FDIntLegalProcLUpdatedByUserCreationDate3 | — |
| CREATION_DATE | FDIntLinesCreatedByUserPEOCreationDate4 | — |
| CREATION_DATE | FDIntLinesLUpdatedByUserPEOCreationDate5 | — |
| CREATION_DATE | FDIntRefCreatedByUserPEOCreationDate6 | — |
| CREATION_DATE | FDIntRefLUpdatedByUserPEOCreationDate7 | — |
| CREATION_DATE | FDLineIntrEOToCreatedByUserPCreationDate2 | — |
| CREATION_DATE | FDLineIntrToLastUpdtdByUserPCreationDate3 | — |
| CREATION_DATE | TaxLineIntrEOCreatedByUserPECreationDate | — |
| CREATION_DATE | TaxLineIntrEOLastUpdtdByUserCreationDate1 | — |
| CREDENTIALS_EMAIL_SENT | FDHeaderIntrEOCreatedByUserPCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDHeaderIntrLastUpdtdByUserPCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FDIntHeadersCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDIntHeadersLUpdatedByUserPECredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FDIntLegalProcCreatedByUserPCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FDIntLegalProcLUpdatedByUserCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | FDIntLinesCreatedByUserPEOCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | FDIntLinesLUpdatedByUserPEOCredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | FDIntRefCreatedByUserPEOCredentialsEmailSent6 | — |
| CREDENTIALS_EMAIL_SENT | FDIntRefLUpdatedByUserPEOCredentialsEmailSent7 | — |
| CREDENTIALS_EMAIL_SENT | FDLineIntrEOToCreatedByUserPCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FDLineIntrToLastUpdtdByUserPCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | TaxLineIntrEOCreatedByUserPECredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | TaxLineIntrEOLastUpdtdByUserCredentialsEmailSent1 | — |
| END_DATE | FDHeaderIntrEOCreatedByUserPEndDate | — |
| END_DATE | FDHeaderIntrLastUpdtdByUserPEndDate1 | — |
| END_DATE | FDIntHeadersCreatedByUserPEOEndDate | — |
| END_DATE | FDIntHeadersLUpdatedByUserPEEndDate1 | — |
| END_DATE | FDIntLegalProcCreatedByUserPEndDate2 | — |
| END_DATE | FDIntLegalProcLUpdatedByUserEndDate3 | — |
| END_DATE | FDIntLinesCreatedByUserPEOEndDate4 | — |
| END_DATE | FDIntLinesLUpdatedByUserPEOEndDate5 | — |
| END_DATE | FDIntRefCreatedByUserPEOEndDate6 | — |
| END_DATE | FDIntRefLUpdatedByUserPEOEndDate7 | — |
| END_DATE | FDLineIntrEOToCreatedByUserPEndDate2 | — |
| END_DATE | FDLineIntrToLastUpdtdByUserPEndDate3 | — |
| END_DATE | TaxLineIntrEOCreatedByUserPEEndDate | — |
| END_DATE | TaxLineIntrEOLastUpdtdByUserEndDate1 | — |
| EXTERNAL_ID | FDHeaderIntrEOCreatedByUserPExternalId | — |
| EXTERNAL_ID | FDHeaderIntrLastUpdtdByUserPExternalId1 | — |
| EXTERNAL_ID | FDIntHeadersCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FDIntHeadersLUpdatedByUserPEExternalId1 | — |
| EXTERNAL_ID | FDIntLegalProcCreatedByUserPExternalId2 | — |
| EXTERNAL_ID | FDIntLegalProcLUpdatedByUserExternalId3 | — |
| EXTERNAL_ID | FDIntLinesCreatedByUserPEOExternalId4 | — |
| EXTERNAL_ID | FDIntLinesLUpdatedByUserPEOExternalId5 | — |
| EXTERNAL_ID | FDIntRefCreatedByUserPEOExternalId6 | — |
| EXTERNAL_ID | FDIntRefLUpdatedByUserPEOExternalId7 | — |
| EXTERNAL_ID | FDLineIntrEOToCreatedByUserPExternalId2 | — |
| EXTERNAL_ID | FDLineIntrToLastUpdtdByUserPExternalId3 | — |
| EXTERNAL_ID | TaxLineIntrEOCreatedByUserPEExternalId | — |
| EXTERNAL_ID | TaxLineIntrEOLastUpdtdByUserExternalId1 | — |
| HR_TERMINATED | FDHeaderIntrEOCreatedByUserPHrTerminated | — |
| HR_TERMINATED | FDHeaderIntrLastUpdtdByUserPHrTerminated1 | — |
| HR_TERMINATED | FDIntHeadersCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FDIntHeadersLUpdatedByUserPEHrTerminated1 | — |
| HR_TERMINATED | FDIntLegalProcCreatedByUserPHrTerminated2 | — |
| HR_TERMINATED | FDIntLegalProcLUpdatedByUserHrTerminated3 | — |
| HR_TERMINATED | FDIntLinesCreatedByUserPEOHrTerminated4 | — |
| HR_TERMINATED | FDIntLinesLUpdatedByUserPEOHrTerminated5 | — |
| HR_TERMINATED | FDIntRefCreatedByUserPEOHrTerminated6 | — |
| HR_TERMINATED | FDIntRefLUpdatedByUserPEOHrTerminated7 | — |
| HR_TERMINATED | FDLineIntrEOToCreatedByUserPHrTerminated2 | — |
| HR_TERMINATED | FDLineIntrToLastUpdtdByUserPHrTerminated3 | — |
| HR_TERMINATED | TaxLineIntrEOCreatedByUserPEHrTerminated | — |
| HR_TERMINATED | TaxLineIntrEOLastUpdtdByUserHrTerminated1 | — |
| LAST_UPDATE_DATE | FDHeaderIntrEOCreatedByUserPLastUpdateDate | — |
| LAST_UPDATE_DATE | FDHeaderIntrLastUpdtdByUserPLastUpdateDate1 | — |
| LAST_UPDATE_DATE | FDIntHeadersCreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FDIntHeadersLUpdatedByUserPELastUpdateDate1 | — |
| LAST_UPDATE_DATE | FDIntLegalProcCreatedByUserPLastUpdateDate2 | — |
| LAST_UPDATE_DATE | FDIntLegalProcLUpdatedByUserLastUpdateDate3 | — |
| LAST_UPDATE_DATE | FDIntLinesCreatedByUserPEOLastUpdateDate4 | — |
| LAST_UPDATE_DATE | FDIntLinesLUpdatedByUserPEOLastUpdateDate5 | — |
| LAST_UPDATE_DATE | FDIntRefCreatedByUserPEOLastUpdateDate6 | — |
| LAST_UPDATE_DATE | FDIntRefLUpdatedByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | FDLineIntrEOToCreatedByUserPLastUpdateDate2 | — |
| LAST_UPDATE_DATE | FDLineIntrToLastUpdtdByUserPLastUpdateDate3 | — |
| LAST_UPDATE_DATE | TaxLineIntrEOCreatedByUserPELastUpdateDate | — |
| LAST_UPDATE_DATE | TaxLineIntrEOLastUpdtdByUserLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | FDHeaderIntrEOCreatedByUserPLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FDHeaderIntrLastUpdtdByUserPLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | FDIntHeadersCreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FDIntHeadersLUpdatedByUserPELastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | FDIntLegalProcCreatedByUserPLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | FDIntLegalProcLUpdatedByUserLastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | FDIntLinesCreatedByUserPEOLastUpdateLogin4 | — |
| LAST_UPDATE_LOGIN | FDIntLinesLUpdatedByUserPEOLastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | FDIntRefCreatedByUserPEOLastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | FDIntRefLUpdatedByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | FDLineIntrEOToCreatedByUserPLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | FDLineIntrToLastUpdtdByUserPLastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | TaxLineIntrEOCreatedByUserPELastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TaxLineIntrEOLastUpdtdByUserLastUpdateLogin1 | — |
| LAST_UPDATED_BY | FDHeaderIntrEOCreatedByUserPLastUpdatedBy | — |
| LAST_UPDATED_BY | FDHeaderIntrLastUpdtdByUserPLastUpdatedBy1 | — |
| LAST_UPDATED_BY | FDIntHeadersCreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FDIntHeadersLUpdatedByUserPELastUpdatedBy1 | — |
| LAST_UPDATED_BY | FDIntLegalProcCreatedByUserPLastUpdatedBy2 | — |
| LAST_UPDATED_BY | FDIntLegalProcLUpdatedByUserLastUpdatedBy3 | — |
| LAST_UPDATED_BY | FDIntLinesCreatedByUserPEOLastUpdatedBy4 | — |
| LAST_UPDATED_BY | FDIntLinesLUpdatedByUserPEOLastUpdatedBy5 | — |
| LAST_UPDATED_BY | FDIntRefCreatedByUserPEOLastUpdatedBy6 | — |
| LAST_UPDATED_BY | FDIntRefLUpdatedByUserPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | FDLineIntrEOToCreatedByUserPLastUpdatedBy2 | — |
| LAST_UPDATED_BY | FDLineIntrToLastUpdtdByUserPLastUpdatedBy3 | — |
| LAST_UPDATED_BY | TaxLineIntrEOCreatedByUserPELastUpdatedBy | — |
| LAST_UPDATED_BY | TaxLineIntrEOLastUpdtdByUserLastUpdatedBy1 | — |
| MULTITENANCY_USERNAME | FDHeaderIntrEOCreatedByUserPMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDHeaderIntrLastUpdtdByUserPMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FDIntHeadersCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDIntHeadersLUpdatedByUserPEMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FDIntLegalProcCreatedByUserPMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FDIntLegalProcLUpdatedByUserMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | FDIntLinesCreatedByUserPEOMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | FDIntLinesLUpdatedByUserPEOMultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | FDIntRefCreatedByUserPEOMultitenancyUsername6 | — |
| MULTITENANCY_USERNAME | FDIntRefLUpdatedByUserPEOMultitenancyUsername7 | — |
| MULTITENANCY_USERNAME | FDLineIntrEOToCreatedByUserPMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FDLineIntrToLastUpdtdByUserPMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | TaxLineIntrEOCreatedByUserPEMultitenancyUsername | — |
| MULTITENANCY_USERNAME | TaxLineIntrEOLastUpdtdByUserMultitenancyUsername1 | — |
| OBJECT_VERSION_NUMBER | FDHeaderIntrEOCreatedByUserPObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FDHeaderIntrLastUpdtdByUserPObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | FDIntHeadersCreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FDIntHeadersLUpdatedByUserPEObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | FDIntLegalProcCreatedByUserPObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | FDIntLegalProcLUpdatedByUserObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | FDIntLinesCreatedByUserPEOObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | FDIntLinesLUpdatedByUserPEOObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | FDIntRefCreatedByUserPEOObjectVersionNumber6 | — |
| OBJECT_VERSION_NUMBER | FDIntRefLUpdatedByUserPEOObjectVersionNumber7 | — |
| OBJECT_VERSION_NUMBER | FDLineIntrEOToCreatedByUserPObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | FDLineIntrToLastUpdtdByUserPObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | TaxLineIntrEOCreatedByUserPEObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TaxLineIntrEOLastUpdtdByUserObjectVersionNumber1 | — |
| PARTY_ID | FDHeaderIntrEOCreatedByUserPPartyId | — |
| PARTY_ID | FDHeaderIntrLastUpdtdByUserPPartyId1 | — |
| PARTY_ID | FDIntHeadersCreatedByUserPEOPartyId | — |
| PARTY_ID | FDIntHeadersLUpdatedByUserPEPartyId1 | — |
| PARTY_ID | FDIntLegalProcCreatedByUserPPartyId2 | — |
| PARTY_ID | FDIntLegalProcLUpdatedByUserPartyId3 | — |
| PARTY_ID | FDIntLinesCreatedByUserPEOPartyId4 | — |
| PARTY_ID | FDIntLinesLUpdatedByUserPEOPartyId5 | — |
| PARTY_ID | FDIntRefCreatedByUserPEOPartyId6 | — |
| PARTY_ID | FDIntRefLUpdatedByUserPEOPartyId7 | — |
| PARTY_ID | FDLineIntrEOToCreatedByUserPPartyId2 | — |
| PARTY_ID | FDLineIntrToLastUpdtdByUserPPartyId3 | — |
| PARTY_ID | TaxLineIntrEOCreatedByUserPEPartyId | — |
| PARTY_ID | TaxLineIntrEOLastUpdtdByUserPartyId1 | — |
| PERSON_ID | FDHeaderIntrEOCreatedByUserPPersonId | — |
| PERSON_ID | FDHeaderIntrLastUpdtdByUserPPersonId1 | — |
| PERSON_ID | FDIntHeadersCreatedByUserPEOPersonId | — |
| PERSON_ID | FDIntHeadersLUpdatedByUserPEPersonId1 | — |
| PERSON_ID | FDIntLegalProcCreatedByUserPPersonId2 | — |
| PERSON_ID | FDIntLegalProcLUpdatedByUserPersonId3 | — |
| PERSON_ID | FDIntLinesCreatedByUserPEOPersonId4 | — |
| PERSON_ID | FDIntLinesLUpdatedByUserPEOPersonId5 | — |
| PERSON_ID | FDIntRefCreatedByUserPEOPersonId6 | — |
| PERSON_ID | FDIntRefLUpdatedByUserPEOPersonId7 | — |
| PERSON_ID | FDLineIntrEOToCreatedByUserPPersonId2 | — |
| PERSON_ID | FDLineIntrToLastUpdtdByUserPPersonId3 | — |
| PERSON_ID | TaxLineIntrEOCreatedByUserPEPersonId | — |
| PERSON_ID | TaxLineIntrEOLastUpdtdByUserPersonId1 | — |
| START_DATE | FDHeaderIntrEOCreatedByUserPStartDate | — |
| START_DATE | FDHeaderIntrLastUpdtdByUserPStartDate1 | — |
| START_DATE | FDIntHeadersCreatedByUserPEOStartDate | — |
| START_DATE | FDIntHeadersLUpdatedByUserPEStartDate1 | — |
| START_DATE | FDIntLegalProcCreatedByUserPStartDate2 | — |
| START_DATE | FDIntLegalProcLUpdatedByUserStartDate3 | — |
| START_DATE | FDIntLinesCreatedByUserPEOStartDate4 | — |
| START_DATE | FDIntLinesLUpdatedByUserPEOStartDate5 | — |
| START_DATE | FDIntRefCreatedByUserPEOStartDate6 | — |
| START_DATE | FDIntRefLUpdatedByUserPEOStartDate7 | — |
| START_DATE | FDLineIntrEOToCreatedByUserPStartDate2 | — |
| START_DATE | FDLineIntrToLastUpdtdByUserPStartDate3 | — |
| START_DATE | TaxLineIntrEOCreatedByUserPEStartDate | — |
| START_DATE | TaxLineIntrEOLastUpdtdByUserStartDate1 | — |
| SUSPENDED | FDHeaderIntrEOCreatedByUserPSuspended | — |
| SUSPENDED | FDHeaderIntrLastUpdtdByUserPSuspended1 | — |
| SUSPENDED | FDIntHeadersCreatedByUserPEOSuspended | — |
| SUSPENDED | FDIntHeadersLUpdatedByUserPESuspended1 | — |
| SUSPENDED | FDIntLegalProcCreatedByUserPSuspended2 | — |
| SUSPENDED | FDIntLegalProcLUpdatedByUserSuspended3 | — |
| SUSPENDED | FDIntLinesCreatedByUserPEOSuspended4 | — |
| SUSPENDED | FDIntLinesLUpdatedByUserPEOSuspended5 | — |
| SUSPENDED | FDIntRefCreatedByUserPEOSuspended6 | — |
| SUSPENDED | FDIntRefLUpdatedByUserPEOSuspended7 | — |
| SUSPENDED | FDLineIntrEOToCreatedByUserPSuspended2 | — |
| SUSPENDED | FDLineIntrToLastUpdtdByUserPSuspended3 | — |
| SUSPENDED | TaxLineIntrEOCreatedByUserPESuspended | — |
| SUSPENDED | TaxLineIntrEOLastUpdtdByUserSuspended1 | — |
| USER_DATA_CHECKSUM | FDHeaderIntrEOCreatedByUserPUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDHeaderIntrLastUpdtdByUserPUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FDIntHeadersCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDIntHeadersLUpdatedByUserPEUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FDIntLegalProcCreatedByUserPUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FDIntLegalProcLUpdatedByUserUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | FDIntLinesCreatedByUserPEOUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | FDIntLinesLUpdatedByUserPEOUserDataChecksum5 | — |
| USER_DATA_CHECKSUM | FDIntRefCreatedByUserPEOUserDataChecksum6 | — |
| USER_DATA_CHECKSUM | FDIntRefLUpdatedByUserPEOUserDataChecksum7 | — |
| USER_DATA_CHECKSUM | FDLineIntrEOToCreatedByUserPUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FDLineIntrToLastUpdtdByUserPUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | TaxLineIntrEOCreatedByUserPEUserDataChecksum | — |
| USER_DATA_CHECKSUM | TaxLineIntrEOLastUpdtdByUserUserDataChecksum1 | — |
| USER_DISTINGUISHED_NAME | FDHeaderIntrEOCreatedByUserPUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDHeaderIntrLastUpdtdByUserPUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FDIntHeadersCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDIntHeadersLUpdatedByUserPEUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FDIntLegalProcCreatedByUserPUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FDIntLegalProcLUpdatedByUserUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | FDIntLinesCreatedByUserPEOUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | FDIntLinesLUpdatedByUserPEOUserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | FDIntRefCreatedByUserPEOUserDistinguishedName6 | — |
| USER_DISTINGUISHED_NAME | FDIntRefLUpdatedByUserPEOUserDistinguishedName7 | — |
| USER_DISTINGUISHED_NAME | FDLineIntrEOToCreatedByUserPUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FDLineIntrToLastUpdtdByUserPUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | TaxLineIntrEOCreatedByUserPEUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | TaxLineIntrEOLastUpdtdByUserUserDistinguishedName1 | — |
| USER_GUID | FDHeaderIntrEOCreatedByUserPUserGuid | — |
| USER_GUID | FDHeaderIntrLastUpdtdByUserPUserGuid1 | — |
| USER_GUID | FDIntHeadersCreatedByUserPEOUserGuid | — |
| USER_GUID | FDIntHeadersLUpdatedByUserPEUserGuid1 | — |
| USER_GUID | FDIntLegalProcCreatedByUserPUserGuid2 | — |
| USER_GUID | FDIntLegalProcLUpdatedByUserUserGuid3 | — |
| USER_GUID | FDIntLinesCreatedByUserPEOUserGuid4 | — |
| USER_GUID | FDIntLinesLUpdatedByUserPEOUserGuid5 | — |
| USER_GUID | FDIntRefCreatedByUserPEOUserGuid6 | — |
| USER_GUID | FDIntRefLUpdatedByUserPEOUserGuid7 | — |
| USER_GUID | FDLineIntrEOToCreatedByUserPUserGuid2 | — |
| USER_GUID | FDLineIntrToLastUpdtdByUserPUserGuid3 | — |
| USER_GUID | TaxLineIntrEOCreatedByUserPEUserGuid | — |
| USER_GUID | TaxLineIntrEOLastUpdtdByUserUserGuid1 | — |
| USER_ID | FDHeaderIntrEOCreatedByUserPUserId | — |
| USER_ID | FDHeaderIntrLastUpdtdByUserPUserId1 | — |
| USER_ID | FDIntHeadersCreatedByUserPEOUserId | — |
| USER_ID | FDIntHeadersLUpdatedByUserPEUserId1 | — |
| USER_ID | FDIntLegalProcCreatedByUserPUserId2 | — |
| USER_ID | FDIntLegalProcLUpdatedByUserUserId3 | — |
| USER_ID | FDIntLinesCreatedByUserPEOUserId4 | — |
| USER_ID | FDIntLinesLUpdatedByUserPEOUserId5 | — |
| USER_ID | FDIntRefCreatedByUserPEOUserId6 | — |
| USER_ID | FDIntRefLUpdatedByUserPEOUserId7 | — |
| USER_ID | FDLineIntrEOToCreatedByUserPUserId2 | — |
| USER_ID | FDLineIntrToLastUpdtdByUserPUserId3 | — |
| USER_ID | TaxLineIntrEOCreatedByUserPEUserId | — |
| USER_ID | TaxLineIntrEOLastUpdtdByUserUserId1 | — |
| USERNAME | FDHeaderIntrEOCreatedByUserPUsername | — |
| USERNAME | FDHeaderIntrLastUpdtdByUserPUsername1 | — |
| USERNAME | FDIntHeadersCreatedByUserPEOUsername | — |
| USERNAME | FDIntHeadersLUpdatedByUserPEUsername1 | — |
| USERNAME | FDIntLegalProcCreatedByUserPUsername2 | — |
| USERNAME | FDIntLegalProcLUpdatedByUserUsername3 | — |
| USERNAME | FDIntLinesCreatedByUserPEOUsername4 | — |
| USERNAME | FDIntLinesLUpdatedByUserPEOUsername5 | — |
| USERNAME | FDIntRefCreatedByUserPEOUsername6 | — |
| USERNAME | FDIntRefLUpdatedByUserPEOUsername7 | — |
| USERNAME | FDLineIntrEOToCreatedByUserPUsername2 | — |
| USERNAME | FDLineIntrToLastUpdtdByUserPUsername3 | — |
| USERNAME | TaxLineIntrEOCreatedByUserPEUsername | — |
| USERNAME | TaxLineIntrEOLastUpdtdByUserUsername1 | — |

### [[fiscaldoceventlogp1|FiscalDocEventLogP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FDEventCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FDEventLastUpdatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FDHdrCreatedByUserPEO1_1ActiveFlag1 | — |
| ACTIVE_FLAG | FDHdrUpdatedByUserPEOActiveFlag2 | — |
| BUSINESS_GROUP_ID | FDEventCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDEventLastUpdatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDHdrCreatedByUserPEO1_1BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FDHdrUpdatedByUserPEOBusinessGroupId2 | — |
| CREATED_BY | FDEventCreatedByUserPEOCreatedBy5 | — |
| CREATED_BY | FDEventLastUpdatedByUserPEOCreatedBy | — |
| CREATED_BY | FDHdrCreatedByUserPEO1_1CreatedBy6 | — |
| CREATED_BY | FDHdrUpdatedByUserPEOCreatedBy7 | — |
| CREATION_DATE | FDEventCreatedByUserPEOCreationDate5 | — |
| CREATION_DATE | FDEventLastUpdatedByUserPEOCreationDate | — |
| CREATION_DATE | FDHdrCreatedByUserPEO1_1CreationDate6 | — |
| CREATION_DATE | FDHdrUpdatedByUserPEOCreationDate7 | — |
| CREDENTIALS_EMAIL_SENT | FDEventCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDEventLastUpdatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDHdrCreatedByUserPEO1_1CredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FDHdrUpdatedByUserPEOCredentialsEmailSent2 | — |
| END_DATE | FDEventCreatedByUserPEOEndDate | — |
| END_DATE | FDEventLastUpdatedByUserPEOEndDate | — |
| END_DATE | FDHdrCreatedByUserPEO1_1EndDate1 | — |
| END_DATE | FDHdrUpdatedByUserPEOEndDate2 | — |
| EXTERNAL_ID | FDEventCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FDEventLastUpdatedByUserPEOExternalId | — |
| EXTERNAL_ID | FDHdrCreatedByUserPEO1_1ExternalId1 | — |
| EXTERNAL_ID | FDHdrUpdatedByUserPEOExternalId2 | — |
| HR_TERMINATED | FDEventCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FDEventLastUpdatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FDHdrCreatedByUserPEO1_1HrTerminated1 | — |
| HR_TERMINATED | FDHdrUpdatedByUserPEOHrTerminated2 | — |
| LAST_UPDATE_DATE | FDEventCreatedByUserPEOLastUpdateDate5 | — |
| LAST_UPDATE_DATE | FDEventLastUpdatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FDHdrCreatedByUserPEO1_1LastUpdateDate6 | — |
| LAST_UPDATE_DATE | FDHdrUpdatedByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_LOGIN | FDEventCreatedByUserPEOLastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | FDEventLastUpdatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FDHdrCreatedByUserPEO1_1LastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | FDHdrUpdatedByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATED_BY | FDEventCreatedByUserPEOLastUpdatedBy5 | — |
| LAST_UPDATED_BY | FDEventLastUpdatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FDHdrCreatedByUserPEO1_1LastUpdatedBy6 | — |
| LAST_UPDATED_BY | FDHdrUpdatedByUserPEOLastUpdatedBy7 | — |
| MULTITENANCY_USERNAME | FDEventCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDEventLastUpdatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDHdrCreatedByUserPEO1_1MultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FDHdrUpdatedByUserPEOMultitenancyUsername2 | — |
| OBJECT_VERSION_NUMBER | FDEventCreatedByUserPEOObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | FDEventLastUpdatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FDHdrCreatedByUserPEO1_1ObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | FDHdrUpdatedByUserPEOObjectVersionNumber5 | — |
| PARTY_ID | FDEventCreatedByUserPEOPartyId | — |
| PARTY_ID | FDEventLastUpdatedByUserPEOPartyId | — |
| PARTY_ID | FDHdrCreatedByUserPEO1_1PartyId1 | — |
| PARTY_ID | FDHdrUpdatedByUserPEOPartyId2 | — |
| PERSON_ID | FDEventCreatedByUserPEOPersonId | — |
| PERSON_ID | FDEventLastUpdatedByUserPEOPersonId | — |
| PERSON_ID | FDHdrCreatedByUserPEO1_1PersonId1 | — |
| PERSON_ID | FDHdrUpdatedByUserPEOPersonId2 | — |
| START_DATE | FDEventCreatedByUserPEOStartDate | — |
| START_DATE | FDEventLastUpdatedByUserPEOStartDate | — |
| START_DATE | FDHdrCreatedByUserPEO1_1StartDate1 | — |
| START_DATE | FDHdrUpdatedByUserPEOStartDate2 | — |
| SUSPENDED | FDEventCreatedByUserPEOSuspended | — |
| SUSPENDED | FDEventLastUpdatedByUserPEOSuspended | — |
| SUSPENDED | FDHdrCreatedByUserPEO1_1Suspended1 | — |
| SUSPENDED | FDHdrUpdatedByUserPEOSuspended2 | — |
| USER_DATA_CHECKSUM | FDEventCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDEventLastUpdatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDHdrCreatedByUserPEO1_1UserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FDHdrUpdatedByUserPEOUserDataChecksum2 | — |
| USER_DISTINGUISHED_NAME | FDEventCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDEventLastUpdatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDHdrCreatedByUserPEO1_1UserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FDHdrUpdatedByUserPEOUserDistinguishedName2 | — |
| USER_GUID | FDEventCreatedByUserPEOUserGuid | — |
| USER_GUID | FDEventLastUpdatedByUserPEOUserGuid | — |
| USER_GUID | FDHdrCreatedByUserPEO1_1UserGuid1 | — |
| USER_GUID | FDHdrUpdatedByUserPEOUserGuid2 | — |
| USER_ID | FDEventCreatedByUserPEOUserId | — |
| USER_ID | FDEventLastUpdatedByUserPEOUserId | — |
| USER_ID | FDHdrCreatedByUserPEO1_1UserId1 | — |
| USER_ID | FDHdrUpdatedByUserPEOUserId2 | — |
| USERNAME | FDEventCreatedByUserPEOUsername | — |
| USERNAME | FDEventLastUpdatedByUserPEOUsername | — |
| USERNAME | FDHdrCreatedByUserPEO1_1Username1 | — |
| USERNAME | FDHdrUpdatedByUserPEOUsername2 | — |

### [[fiscaldocheadersp|FiscalDocHeadersP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FiscalDocHeaderExtnCreatedByActiveFlag | — |
| ACTIVE_FLAG | FiscalDocHeaderExtnLastUpdatActiveFlag1 | — |
| ACTIVE_FLAG | LastUpdatedUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | CreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FiscalDocHeaderExtnCreatedByBusinessGroupId | — |
| BUSINESS_GROUP_ID | FiscalDocHeaderExtnLastUpdatBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | LastUpdatedUserPEOBusinessGroupId | — |
| CREATED_BY | CreatedByUserPEOCreatedBy | — |
| CREATED_BY | FiscalDocHeaderExtnCreatedByCreatedBy | — |
| CREATED_BY | FiscalDocHeaderExtnLastUpdatCreatedBy1 | — |
| CREATED_BY | LastUpdatedUserPEOCreatedBy | — |
| CREATION_DATE | CreatedByUserPEOCreationDate | — |
| CREATION_DATE | FiscalDocHeaderExtnCreatedByCreationDate | — |
| CREATION_DATE | FiscalDocHeaderExtnLastUpdatCreationDate1 | — |
| CREATION_DATE | LastUpdatedUserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocHeaderExtnCreatedByCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocHeaderExtnLastUpdatCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedUserPEOCredentialsEmailSent | — |
| END_DATE | CreatedByUserPEOEndDate | — |
| END_DATE | FiscalDocHeaderExtnCreatedByEndDate | — |
| END_DATE | FiscalDocHeaderExtnLastUpdatEndDate1 | — |
| END_DATE | LastUpdatedUserPEOEndDate | — |
| EXTERNAL_ID | CreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FiscalDocHeaderExtnCreatedByExternalId | — |
| EXTERNAL_ID | FiscalDocHeaderExtnLastUpdatExternalId1 | — |
| EXTERNAL_ID | LastUpdatedUserPEOExternalId | — |
| HR_TERMINATED | CreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FiscalDocHeaderExtnCreatedByHrTerminated | — |
| HR_TERMINATED | FiscalDocHeaderExtnLastUpdatHrTerminated1 | — |
| HR_TERMINATED | LastUpdatedUserPEOHrTerminated | — |
| LAST_UPDATE_DATE | CreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FiscalDocHeaderExtnCreatedByLastUpdateDate | — |
| LAST_UPDATE_DATE | FiscalDocHeaderExtnLastUpdatLastUpdateDate1 | — |
| LAST_UPDATE_DATE | LastUpdatedUserPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | CreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FiscalDocHeaderExtnCreatedByLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FiscalDocHeaderExtnLastUpdatLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | LastUpdatedUserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FiscalDocHeaderExtnCreatedByLastUpdatedBy | — |
| LAST_UPDATED_BY | FiscalDocHeaderExtnLastUpdatLastUpdatedBy1 | — |
| LAST_UPDATED_BY | LastUpdatedUserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | CreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FiscalDocHeaderExtnCreatedByMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FiscalDocHeaderExtnLastUpdatMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | LastUpdatedUserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | CreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FiscalDocHeaderExtnCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FiscalDocHeaderExtnLastUpdatObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedUserPEOObjectVersionNumber | — |
| PARTY_ID | CreatedByUserPEOPartyId | — |
| PARTY_ID | FiscalDocHeaderExtnCreatedByPartyId | — |
| PARTY_ID | FiscalDocHeaderExtnLastUpdatPartyId1 | — |
| PARTY_ID | LastUpdatedUserPEOPartyId | — |
| PERSON_ID | CreatedByUserPEOPersonId | — |
| PERSON_ID | FiscalDocHeaderExtnCreatedByPersonId | — |
| PERSON_ID | FiscalDocHeaderExtnLastUpdatPersonId1 | — |
| PERSON_ID | LastUpdatedUserPEOPersonId | — |
| START_DATE | CreatedByUserPEOStartDate | — |
| START_DATE | FiscalDocHeaderExtnCreatedByStartDate | — |
| START_DATE | FiscalDocHeaderExtnLastUpdatStartDate1 | — |
| START_DATE | LastUpdatedUserPEOStartDate | — |
| SUSPENDED | CreatedByUserPEOSuspended | — |
| SUSPENDED | FiscalDocHeaderExtnCreatedBySuspended | — |
| SUSPENDED | FiscalDocHeaderExtnLastUpdatSuspended1 | — |
| SUSPENDED | LastUpdatedUserPEOSuspended | — |
| USER_DATA_CHECKSUM | CreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FiscalDocHeaderExtnCreatedByUserDataChecksum | — |
| USER_DATA_CHECKSUM | FiscalDocHeaderExtnLastUpdatUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | LastUpdatedUserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | CreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FiscalDocHeaderExtnCreatedByUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FiscalDocHeaderExtnLastUpdatUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | LastUpdatedUserPEOUserDistinguishedName | — |
| USER_GUID | CreatedByUserPEOUserGuid | — |
| USER_GUID | FiscalDocHeaderExtnCreatedByUserGuid | — |
| USER_GUID | FiscalDocHeaderExtnLastUpdatUserGuid1 | — |
| USER_GUID | LastUpdatedUserPEOUserGuid | — |
| USER_ID | CreatedByUserPEOUserId | — |
| USER_ID | FiscalDocHeaderExtnCreatedByUserId | — |
| USER_ID | FiscalDocHeaderExtnLastUpdatUserId1 | — |
| USER_ID | LastUpdatedUserPEOUserId | — |
| USERNAME | CreatedByUserPEOUsername | — |
| USERNAME | FiscalDocHeaderExtnCreatedByUsername | — |
| USERNAME | FiscalDocHeaderExtnLastUpdatUsername1 | — |
| USERNAME | LastUpdatedUserPEOUsername | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FdHdrsCrtdByUserPEOActiveFlag3 | — |
| ACTIVE_FLAG | FdHdrsLastUpdByUserPEOActiveFlag2 | — |
| ACTIVE_FLAG | FdHoldsCrtdByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdHoldsLastUpdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FdLinesCrtdByUserPEOActiveFlag5 | — |
| ACTIVE_FLAG | FdLinesLastUpdByUserPEOActiveFlag4 | — |
| ACTIVE_FLAG | FdSchdCrtdByUserPEOActiveFlag7 | — |
| ACTIVE_FLAG | FdSchdLastUpdByUserPEOActiveFlag6 | — |
| BUSINESS_GROUP_ID | FdHdrsCrtdByUserPEOBusinessGroupId5 | — |
| BUSINESS_GROUP_ID | FdHdrsLastUpdByUserPEOBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | FdHoldsCrtdByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdHoldsLastUpdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FdLinesCrtdByUserPEOBusinessGroupId9 | — |
| BUSINESS_GROUP_ID | FdLinesLastUpdByUserPEOBusinessGroupId8 | — |
| BUSINESS_GROUP_ID | FdSchdCrtdByUserPEOBusinessGroupId13 | — |
| BUSINESS_GROUP_ID | FdSchdLastUpdByUserPEOBusinessGroupId12 | — |
| CREATED_BY | FdHdrsCrtdByUserPEOCreatedBy11 | — |
| CREATED_BY | FdHdrsLastUpdByUserPEOCreatedBy10 | — |
| CREATED_BY | FdHoldsCrtdByUserPEOCreatedBy6 | — |
| CREATED_BY | FdHoldsLastUpdByUserPEOCreatedBy7 | — |
| CREATED_BY | FdLinesCrtdByUserPEOCreatedBy15 | — |
| CREATED_BY | FdLinesLastUpdByUserPEOCreatedBy14 | — |
| CREATED_BY | FdSchdCrtdByUserPEOCreatedBy19 | — |
| CREATED_BY | FdSchdLastUpdByUserPEOCreatedBy18 | — |
| CREATION_DATE | FdHdrsCrtdByUserPEOCreationDate11 | — |
| CREATION_DATE | FdHdrsLastUpdByUserPEOCreationDate10 | — |
| CREATION_DATE | FdHoldsCrtdByUserPEOCreationDate6 | — |
| CREATION_DATE | FdHoldsLastUpdByUserPEOCreationDate7 | — |
| CREATION_DATE | FdLinesCrtdByUserPEOCreationDate15 | — |
| CREATION_DATE | FdLinesLastUpdByUserPEOCreationDate14 | — |
| CREATION_DATE | FdSchdCrtdByUserPEOCreationDate19 | — |
| CREATION_DATE | FdSchdLastUpdByUserPEOCreationDate18 | — |
| CREDENTIALS_EMAIL_SENT | FdHdrsCrtdByUserPEOCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | FdHdrsLastUpdByUserPEOCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FdHoldsCrtdByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdHoldsLastUpdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FdLinesCrtdByUserPEOCredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | FdLinesLastUpdByUserPEOCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | FdSchdCrtdByUserPEOCredentialsEmailSent7 | — |
| CREDENTIALS_EMAIL_SENT | FdSchdLastUpdByUserPEOCredentialsEmailSent6 | — |
| END_DATE | FdHdrsCrtdByUserPEOEndDate3 | — |
| END_DATE | FdHdrsLastUpdByUserPEOEndDate2 | — |
| END_DATE | FdHoldsCrtdByUserPEOEndDate | — |
| END_DATE | FdHoldsLastUpdByUserPEOEndDate1 | — |
| END_DATE | FdLinesCrtdByUserPEOEndDate5 | — |
| END_DATE | FdLinesLastUpdByUserPEOEndDate4 | — |
| END_DATE | FdSchdCrtdByUserPEOEndDate7 | — |
| END_DATE | FdSchdLastUpdByUserPEOEndDate6 | — |
| EXTERNAL_ID | FdHdrsCrtdByUserPEOExternalId3 | — |
| EXTERNAL_ID | FdHdrsLastUpdByUserPEOExternalId2 | — |
| EXTERNAL_ID | FdHoldsCrtdByUserPEOExternalId | — |
| EXTERNAL_ID | FdHoldsLastUpdByUserPEOExternalId1 | — |
| EXTERNAL_ID | FdLinesCrtdByUserPEOExternalId5 | — |
| EXTERNAL_ID | FdLinesLastUpdByUserPEOExternalId4 | — |
| EXTERNAL_ID | FdSchdCrtdByUserPEOExternalId7 | — |
| EXTERNAL_ID | FdSchdLastUpdByUserPEOExternalId6 | — |
| HR_TERMINATED | FdHdrsCrtdByUserPEOHrTerminated3 | — |
| HR_TERMINATED | FdHdrsLastUpdByUserPEOHrTerminated2 | — |
| HR_TERMINATED | FdHoldsCrtdByUserPEOHrTerminated | — |
| HR_TERMINATED | FdHoldsLastUpdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | FdLinesCrtdByUserPEOHrTerminated5 | — |
| HR_TERMINATED | FdLinesLastUpdByUserPEOHrTerminated4 | — |
| HR_TERMINATED | FdSchdCrtdByUserPEOHrTerminated7 | — |
| HR_TERMINATED | FdSchdLastUpdByUserPEOHrTerminated6 | — |
| LAST_UPDATE_DATE | FdHdrsCrtdByUserPEOLastUpdateDate11 | — |
| LAST_UPDATE_DATE | FdHdrsLastUpdByUserPEOLastUpdateDate10 | — |
| LAST_UPDATE_DATE | FdHoldsCrtdByUserPEOLastUpdateDate6 | — |
| LAST_UPDATE_DATE | FdHoldsLastUpdByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | FdLinesCrtdByUserPEOLastUpdateDate15 | — |
| LAST_UPDATE_DATE | FdLinesLastUpdByUserPEOLastUpdateDate14 | — |
| LAST_UPDATE_DATE | FdSchdCrtdByUserPEOLastUpdateDate19 | — |
| LAST_UPDATE_DATE | FdSchdLastUpdByUserPEOLastUpdateDate18 | — |
| LAST_UPDATE_LOGIN | FdHdrsCrtdByUserPEOLastUpdateLogin11 | — |
| LAST_UPDATE_LOGIN | FdHdrsLastUpdByUserPEOLastUpdateLogin10 | — |
| LAST_UPDATE_LOGIN | FdHoldsCrtdByUserPEOLastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | FdHoldsLastUpdByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | FdLinesCrtdByUserPEOLastUpdateLogin15 | — |
| LAST_UPDATE_LOGIN | FdLinesLastUpdByUserPEOLastUpdateLogin14 | — |
| LAST_UPDATE_LOGIN | FdSchdCrtdByUserPEOLastUpdateLogin19 | — |
| LAST_UPDATE_LOGIN | FdSchdLastUpdByUserPEOLastUpdateLogin18 | — |
| LAST_UPDATED_BY | FdHdrsCrtdByUserPEOLastUpdatedBy11 | — |
| LAST_UPDATED_BY | FdHdrsLastUpdByUserPEOLastUpdatedBy10 | — |
| LAST_UPDATED_BY | FdHoldsCrtdByUserPEOLastUpdatedBy6 | — |
| LAST_UPDATED_BY | FdHoldsLastUpdByUserPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | FdLinesCrtdByUserPEOLastUpdatedBy15 | — |
| LAST_UPDATED_BY | FdLinesLastUpdByUserPEOLastUpdatedBy14 | — |
| LAST_UPDATED_BY | FdSchdCrtdByUserPEOLastUpdatedBy19 | — |
| LAST_UPDATED_BY | FdSchdLastUpdByUserPEOLastUpdatedBy18 | — |
| MULTITENANCY_USERNAME | FdHdrsCrtdByUserPEOMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | FdHdrsLastUpdByUserPEOMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FdHoldsCrtdByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdHoldsLastUpdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FdLinesCrtdByUserPEOMultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | FdLinesLastUpdByUserPEOMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | FdSchdCrtdByUserPEOMultitenancyUsername7 | — |
| MULTITENANCY_USERNAME | FdSchdLastUpdByUserPEOMultitenancyUsername6 | — |
| OBJECT_VERSION_NUMBER | FdHdrsCrtdByUserPEOObjectVersionNumber10 | — |
| OBJECT_VERSION_NUMBER | FdHdrsLastUpdByUserPEOObjectVersionNumber9 | — |
| OBJECT_VERSION_NUMBER | FdHoldsCrtdByUserPEOObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | FdHoldsLastUpdByUserPEOObjectVersionNumber6 | — |
| OBJECT_VERSION_NUMBER | FdLinesCrtdByUserPEOObjectVersionNumber14 | — |
| OBJECT_VERSION_NUMBER | FdLinesLastUpdByUserPEOObjectVersionNumber13 | — |
| OBJECT_VERSION_NUMBER | FdSchdCrtdByUserPEOObjectVersionNumber18 | — |
| OBJECT_VERSION_NUMBER | FdSchdLastUpdByUserPEOObjectVersionNumber17 | — |
| PARTY_ID | FdHdrsCrtdByUserPEOPartyId4 | — |
| PARTY_ID | FdHdrsLastUpdByUserPEOPartyId3 | — |
| PARTY_ID | FdHoldsCrtdByUserPEOPartyId1 | — |
| PARTY_ID | FdHoldsLastUpdByUserPEOPartyId2 | — |
| PARTY_ID | FdLinesCrtdByUserPEOPartyId6 | — |
| PARTY_ID | FdLinesLastUpdByUserPEOPartyId5 | — |
| PARTY_ID | FdSchdCrtdByUserPEOPartyId8 | — |
| PARTY_ID | FdSchdLastUpdByUserPEOPartyId7 | — |
| PERSON_ID | FdHdrsCrtdByUserPEOPersonId5 | — |
| PERSON_ID | FdHdrsLastUpdByUserPEOPersonId4 | — |
| PERSON_ID | FdHoldsCrtdByUserPEOPersonId | — |
| PERSON_ID | FdHoldsLastUpdByUserPEOPersonId1 | — |
| PERSON_ID | FdLinesCrtdByUserPEOPersonId9 | — |
| PERSON_ID | FdLinesLastUpdByUserPEOPersonId8 | — |
| PERSON_ID | FdSchdCrtdByUserPEOPersonId13 | — |
| PERSON_ID | FdSchdLastUpdByUserPEOPersonId12 | — |
| START_DATE | FdHdrsCrtdByUserPEOStartDate3 | — |
| START_DATE | FdHdrsLastUpdByUserPEOStartDate2 | — |
| START_DATE | FdHoldsCrtdByUserPEOStartDate | — |
| START_DATE | FdHoldsLastUpdByUserPEOStartDate1 | — |
| START_DATE | FdLinesCrtdByUserPEOStartDate5 | — |
| START_DATE | FdLinesLastUpdByUserPEOStartDate4 | — |
| START_DATE | FdSchdCrtdByUserPEOStartDate7 | — |
| START_DATE | FdSchdLastUpdByUserPEOStartDate6 | — |
| SUSPENDED | FdHdrsCrtdByUserPEOSuspended3 | — |
| SUSPENDED | FdHdrsLastUpdByUserPEOSuspended2 | — |
| SUSPENDED | FdHoldsCrtdByUserPEOSuspended | — |
| SUSPENDED | FdHoldsLastUpdByUserPEOSuspended1 | — |
| SUSPENDED | FdLinesCrtdByUserPEOSuspended5 | — |
| SUSPENDED | FdLinesLastUpdByUserPEOSuspended4 | — |
| SUSPENDED | FdSchdCrtdByUserPEOSuspended7 | — |
| SUSPENDED | FdSchdLastUpdByUserPEOSuspended6 | — |
| USER_DATA_CHECKSUM | FdHdrsCrtdByUserPEOUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | FdHdrsLastUpdByUserPEOUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FdHoldsCrtdByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdHoldsLastUpdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FdLinesCrtdByUserPEOUserDataChecksum5 | — |
| USER_DATA_CHECKSUM | FdLinesLastUpdByUserPEOUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | FdSchdCrtdByUserPEOUserDataChecksum7 | — |
| USER_DATA_CHECKSUM | FdSchdLastUpdByUserPEOUserDataChecksum6 | — |
| USER_DISTINGUISHED_NAME | FdHdrsCrtdByUserPEOUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | FdHdrsLastUpdByUserPEOUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FdHoldsCrtdByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdHoldsLastUpdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FdLinesCrtdByUserPEOUserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | FdLinesLastUpdByUserPEOUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | FdSchdCrtdByUserPEOUserDistinguishedName7 | — |
| USER_DISTINGUISHED_NAME | FdSchdLastUpdByUserPEOUserDistinguishedName6 | — |
| USER_GUID | FdHdrsCrtdByUserPEOUserGuid3 | — |
| USER_GUID | FdHdrsLastUpdByUserPEOUserGuid2 | — |
| USER_GUID | FdHoldsCrtdByUserPEOUserGuid | — |
| USER_GUID | FdHoldsLastUpdByUserPEOUserGuid1 | — |
| USER_GUID | FdLinesCrtdByUserPEOUserGuid5 | — |
| USER_GUID | FdLinesLastUpdByUserPEOUserGuid4 | — |
| USER_GUID | FdSchdCrtdByUserPEOUserGuid7 | — |
| USER_GUID | FdSchdLastUpdByUserPEOUserGuid6 | — |
| USER_ID | FdHdrsCrtdByUserPEOUserId3 | — |
| USER_ID | FdHdrsLastUpdByUserPEOUserId2 | — |
| USER_ID | FdHoldsCrtdByUserPEOUserId | — |
| USER_ID | FdHoldsLastUpdByUserPEOUserId1 | — |
| USER_ID | FdLinesCrtdByUserPEOUserId5 | — |
| USER_ID | FdLinesLastUpdByUserPEOUserId4 | — |
| USER_ID | FdSchdCrtdByUserPEOUserId7 | — |
| USER_ID | FdSchdLastUpdByUserPEOUserId6 | — |
| USERNAME | FdHdrsCrtdByUserPEOUsername3 | — |
| USERNAME | FdHdrsLastUpdByUserPEOUsername2 | — |
| USERNAME | FdHoldsCrtdByUserPEOUsername | — |
| USERNAME | FdHoldsLastUpdByUserPEOUsername1 | — |
| USERNAME | FdLinesCrtdByUserPEOUsername5 | — |
| USERNAME | FdLinesLastUpdByUserPEOUsername4 | — |
| USERNAME | FdSchdCrtdByUserPEOUsername7 | — |
| USERNAME | FdSchdLastUpdByUserPEOUsername6 | — |

### [[fiscaldocreferenceattrp1|FiscalDocReferenceAttrP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | LastUpdatedByUserPEO1_1ActiveFlag1 | — |
| ACTIVE_FLAG | RefAttrCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | RefAttrLastUpdateByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | RefDocCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | RefDocLastUpdtdByUserPEOActiveFlag1 | — |
| BUSINESS_GROUP_ID | CreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | LastUpdatedByUserPEO1_1BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | RefAttrCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | RefAttrLastUpdateByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | RefDocCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | RefDocLastUpdtdByUserPEOBusinessGroupId1 | — |
| CREATED_BY | CreatedByUserPEOCreatedBy5 | — |
| CREATED_BY | LastUpdatedByUserPEO1_1CreatedBy6 | — |
| CREATED_BY | RefAttrCreatedByUserPEOCreatedBy1 | — |
| CREATED_BY | RefAttrLastUpdateByUserPEOCreatedBy2 | — |
| CREATED_BY | RefDocCreatedByUserPEOCreatedBy | — |
| CREATED_BY | RefDocLastUpdtdByUserPEOCreatedBy1 | — |
| CREATION_DATE | CreatedByUserPEOCreationDate5 | — |
| CREATION_DATE | LastUpdatedByUserPEO1_1CreationDate6 | — |
| CREATION_DATE | RefAttrCreatedByUserPEOCreationDate1 | — |
| CREATION_DATE | RefAttrLastUpdateByUserPEOCreationDate2 | — |
| CREATION_DATE | RefDocCreatedByUserPEOCreationDate | — |
| CREATION_DATE | RefDocLastUpdtdByUserPEOCreationDate1 | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedByUserPEO1_1CredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | RefAttrCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | RefAttrLastUpdateByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | RefDocCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | RefDocLastUpdtdByUserPEOCredentialsEmailSent1 | — |
| END_DATE | CreatedByUserPEOEndDate | — |
| END_DATE | LastUpdatedByUserPEO1_1EndDate1 | — |
| END_DATE | RefAttrCreatedByUserPEOEndDate | — |
| END_DATE | RefAttrLastUpdateByUserPEOEndDate1 | — |
| END_DATE | RefDocCreatedByUserPEOEndDate | — |
| END_DATE | RefDocLastUpdtdByUserPEOEndDate1 | — |
| EXTERNAL_ID | CreatedByUserPEOExternalId | — |
| EXTERNAL_ID | LastUpdatedByUserPEO1_1ExternalId1 | — |
| EXTERNAL_ID | RefAttrCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | RefAttrLastUpdateByUserPEOExternalId1 | — |
| EXTERNAL_ID | RefDocCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | RefDocLastUpdtdByUserPEOExternalId1 | — |
| HR_TERMINATED | CreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | LastUpdatedByUserPEO1_1HrTerminated1 | — |
| HR_TERMINATED | RefAttrCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | RefAttrLastUpdateByUserPEOHrTerminated1 | — |
| HR_TERMINATED | RefDocCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | RefDocLastUpdtdByUserPEOHrTerminated1 | — |
| LAST_UPDATE_DATE | CreatedByUserPEOLastUpdateDate5 | — |
| LAST_UPDATE_DATE | LastUpdatedByUserPEO1_1LastUpdateDate6 | — |
| LAST_UPDATE_DATE | RefAttrCreatedByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_DATE | RefAttrLastUpdateByUserPEOLastUpdateDate2 | — |
| LAST_UPDATE_DATE | RefDocCreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | RefDocLastUpdtdByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | CreatedByUserPEOLastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | LastUpdatedByUserPEO1_1LastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | RefAttrCreatedByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | RefAttrLastUpdateByUserPEOLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | RefDocCreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RefDocLastUpdtdByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | CreatedByUserPEOLastUpdatedBy5 | — |
| LAST_UPDATED_BY | LastUpdatedByUserPEO1_1LastUpdatedBy6 | — |
| LAST_UPDATED_BY | RefAttrCreatedByUserPEOLastUpdatedBy1 | — |
| LAST_UPDATED_BY | RefAttrLastUpdateByUserPEOLastUpdatedBy2 | — |
| LAST_UPDATED_BY | RefDocCreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | RefDocLastUpdtdByUserPEOLastUpdatedBy1 | — |
| MULTITENANCY_USERNAME | CreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | LastUpdatedByUserPEO1_1MultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | RefAttrCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | RefAttrLastUpdateByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | RefDocCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | RefDocLastUpdtdByUserPEOMultitenancyUsername1 | — |
| OBJECT_VERSION_NUMBER | CreatedByUserPEOObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByUserPEO1_1ObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | RefAttrCreatedByUserPEOObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | RefAttrLastUpdateByUserPEOObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | RefDocCreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RefDocLastUpdtdByUserPEOObjectVersionNumber1 | — |
| PARTY_ID | CreatedByUserPEOPartyId | — |
| PARTY_ID | LastUpdatedByUserPEO1_1PartyId1 | — |
| PARTY_ID | RefAttrCreatedByUserPEOPartyId | — |
| PARTY_ID | RefAttrLastUpdateByUserPEOPartyId1 | — |
| PARTY_ID | RefDocCreatedByUserPEOPartyId | — |
| PARTY_ID | RefDocLastUpdtdByUserPEOPartyId1 | — |
| PERSON_ID | CreatedByUserPEOPersonId | — |
| PERSON_ID | LastUpdatedByUserPEO1_1PersonId1 | — |
| PERSON_ID | RefAttrCreatedByUserPEOPersonId | — |
| PERSON_ID | RefAttrLastUpdateByUserPEOPersonId1 | — |
| PERSON_ID | RefDocCreatedByUserPEOPersonId | — |
| PERSON_ID | RefDocLastUpdtdByUserPEOPersonId1 | — |
| START_DATE | CreatedByUserPEOStartDate | — |
| START_DATE | LastUpdatedByUserPEO1_1StartDate1 | — |
| START_DATE | RefAttrCreatedByUserPEOStartDate | — |
| START_DATE | RefAttrLastUpdateByUserPEOStartDate1 | — |
| START_DATE | RefDocCreatedByUserPEOStartDate | — |
| START_DATE | RefDocLastUpdtdByUserPEOStartDate1 | — |
| SUSPENDED | CreatedByUserPEOSuspended | — |
| SUSPENDED | LastUpdatedByUserPEO1_1Suspended1 | — |
| SUSPENDED | RefAttrCreatedByUserPEOSuspended | — |
| SUSPENDED | RefAttrLastUpdateByUserPEOSuspended1 | — |
| SUSPENDED | RefDocCreatedByUserPEOSuspended | — |
| SUSPENDED | RefDocLastUpdtdByUserPEOSuspended1 | — |
| USER_DATA_CHECKSUM | CreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | LastUpdatedByUserPEO1_1UserDataChecksum1 | — |
| USER_DATA_CHECKSUM | RefAttrCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | RefAttrLastUpdateByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | RefDocCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | RefDocLastUpdtdByUserPEOUserDataChecksum1 | — |
| USER_DISTINGUISHED_NAME | CreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | LastUpdatedByUserPEO1_1UserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | RefAttrCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | RefAttrLastUpdateByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | RefDocCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | RefDocLastUpdtdByUserPEOUserDistinguishedName1 | — |
| USER_GUID | CreatedByUserPEOUserGuid | — |
| USER_GUID | LastUpdatedByUserPEO1_1UserGuid1 | — |
| USER_GUID | RefAttrCreatedByUserPEOUserGuid | — |
| USER_GUID | RefAttrLastUpdateByUserPEOUserGuid1 | — |
| USER_GUID | RefDocCreatedByUserPEOUserGuid | — |
| USER_GUID | RefDocLastUpdtdByUserPEOUserGuid1 | — |
| USER_ID | CreatedByUserPEOUserId | — |
| USER_ID | LastUpdatedByUserPEO1_1UserId1 | — |
| USER_ID | RefAttrCreatedByUserPEOUserId | — |
| USER_ID | RefAttrLastUpdateByUserPEOUserId1 | — |
| USER_ID | RefDocCreatedByUserPEOUserId | — |
| USER_ID | RefDocLastUpdtdByUserPEOUserId1 | — |
| USERNAME | CreatedByUserPEOUsername | — |
| USERNAME | LastUpdatedByUserPEO1_1Username1 | — |
| USERNAME | RefAttrCreatedByUserPEOUsername | — |
| USERNAME | RefAttrLastUpdateByUserPEOUsername1 | — |
| USERNAME | RefDocCreatedByUserPEOUsername | — |
| USERNAME | RefDocLastUpdtdByUserPEOUsername1 | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FdHdrExtnCrtdByUserPEOActiveFlag2 | — |
| ACTIVE_FLAG | FdHdrExtnLastUpdByUserPEOActiveFlag3 | — |
| ACTIVE_FLAG | FdLinesCrtdByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdLinesLastUpdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FdTaxLineCrtdByUserPEOActiveFlag4 | — |
| ACTIVE_FLAG | FdTaxLineLastUpdByUserPEOActiveFlag5 | — |
| ACTIVE_FLAG | LastUpdatedUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | CreatedByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FdHdrExtnCrtdByUserPEOBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | FdHdrExtnLastUpdByUserPEOBusinessGroupId5 | — |
| BUSINESS_GROUP_ID | FdLinesCrtdByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdLinesLastUpdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FdTaxLineCrtdByUserPEOBusinessGroupId8 | — |
| BUSINESS_GROUP_ID | FdTaxLineLastUpdByUserPEOBusinessGroupId9 | — |
| BUSINESS_GROUP_ID | LastUpdatedUserPEOBusinessGroupId | — |
| CREATED_BY | CreatedByUserPEOCreatedBy12 | — |
| CREATED_BY | FdHdrExtnCrtdByUserPEOCreatedBy6 | — |
| CREATED_BY | FdHdrExtnLastUpdByUserPEOCreatedBy7 | — |
| CREATED_BY | FdLinesCrtdByUserPEOCreatedBy2 | — |
| CREATED_BY | FdLinesLastUpdByUserPEOCreatedBy3 | — |
| CREATED_BY | FdTaxLineCrtdByUserPEOCreatedBy10 | — |
| CREATED_BY | FdTaxLineLastUpdByUserPEOCreatedBy11 | — |
| CREATED_BY | LastUpdatedUserPEOCreatedBy11 | — |
| CREATION_DATE | CreatedByUserPEOCreationDate12 | — |
| CREATION_DATE | FdHdrExtnCrtdByUserPEOCreationDate6 | — |
| CREATION_DATE | FdHdrExtnLastUpdByUserPEOCreationDate7 | — |
| CREATION_DATE | FdLinesCrtdByUserPEOCreationDate2 | — |
| CREATION_DATE | FdLinesLastUpdByUserPEOCreationDate3 | — |
| CREATION_DATE | FdTaxLineCrtdByUserPEOCreationDate10 | — |
| CREATION_DATE | FdTaxLineLastUpdByUserPEOCreationDate11 | — |
| CREATION_DATE | LastUpdatedUserPEOCreationDate11 | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FdHdrExtnCrtdByUserPEOCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FdHdrExtnLastUpdByUserPEOCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | FdLinesCrtdByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdLinesLastUpdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FdTaxLineCrtdByUserPEOCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | FdTaxLineLastUpdByUserPEOCredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedUserPEOCredentialsEmailSent | — |
| END_DATE | CreatedByUserPEOEndDate1 | — |
| END_DATE | FdHdrExtnCrtdByUserPEOEndDate2 | — |
| END_DATE | FdHdrExtnLastUpdByUserPEOEndDate3 | — |
| END_DATE | FdLinesCrtdByUserPEOEndDate | — |
| END_DATE | FdLinesLastUpdByUserPEOEndDate1 | — |
| END_DATE | FdTaxLineCrtdByUserPEOEndDate4 | — |
| END_DATE | FdTaxLineLastUpdByUserPEOEndDate5 | — |
| END_DATE | LastUpdatedUserPEOEndDate | — |
| EXTERNAL_ID | CreatedByUserPEOExternalId1 | — |
| EXTERNAL_ID | FdHdrExtnCrtdByUserPEOExternalId2 | — |
| EXTERNAL_ID | FdHdrExtnLastUpdByUserPEOExternalId3 | — |
| EXTERNAL_ID | FdLinesCrtdByUserPEOExternalId | — |
| EXTERNAL_ID | FdLinesLastUpdByUserPEOExternalId1 | — |
| EXTERNAL_ID | FdTaxLineCrtdByUserPEOExternalId4 | — |
| EXTERNAL_ID | FdTaxLineLastUpdByUserPEOExternalId5 | — |
| EXTERNAL_ID | LastUpdatedUserPEOExternalId | — |
| HR_TERMINATED | CreatedByUserPEOHrTerminated1 | — |
| HR_TERMINATED | FdHdrExtnCrtdByUserPEOHrTerminated2 | — |
| HR_TERMINATED | FdHdrExtnLastUpdByUserPEOHrTerminated3 | — |
| HR_TERMINATED | FdLinesCrtdByUserPEOHrTerminated | — |
| HR_TERMINATED | FdLinesLastUpdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | FdTaxLineCrtdByUserPEOHrTerminated4 | — |
| HR_TERMINATED | FdTaxLineLastUpdByUserPEOHrTerminated5 | — |
| HR_TERMINATED | LastUpdatedUserPEOHrTerminated | — |
| LAST_UPDATE_DATE | CreatedByUserPEOLastUpdateDate12 | — |
| LAST_UPDATE_DATE | FdHdrExtnCrtdByUserPEOLastUpdateDate6 | — |
| LAST_UPDATE_DATE | FdHdrExtnLastUpdByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | FdLinesCrtdByUserPEOLastUpdateDate2 | — |
| LAST_UPDATE_DATE | FdLinesLastUpdByUserPEOLastUpdateDate3 | — |
| LAST_UPDATE_DATE | FdTaxLineCrtdByUserPEOLastUpdateDate10 | — |
| LAST_UPDATE_DATE | FdTaxLineLastUpdByUserPEOLastUpdateDate11 | — |
| LAST_UPDATE_DATE | LastUpdatedUserPEOLastUpdateDate11 | — |
| LAST_UPDATE_LOGIN | CreatedByUserPEOLastUpdateLogin12 | — |
| LAST_UPDATE_LOGIN | FdHdrExtnCrtdByUserPEOLastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | FdHdrExtnLastUpdByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | FdLinesCrtdByUserPEOLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | FdLinesLastUpdByUserPEOLastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | FdTaxLineCrtdByUserPEOLastUpdateLogin10 | — |
| LAST_UPDATE_LOGIN | FdTaxLineLastUpdByUserPEOLastUpdateLogin11 | — |
| LAST_UPDATE_LOGIN | LastUpdatedUserPEOLastUpdateLogin11 | — |
| LAST_UPDATED_BY | CreatedByUserPEOLastUpdatedBy12 | — |
| LAST_UPDATED_BY | FdHdrExtnCrtdByUserPEOLastUpdatedBy6 | — |
| LAST_UPDATED_BY | FdHdrExtnLastUpdByUserPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | FdLinesCrtdByUserPEOLastUpdatedBy2 | — |
| LAST_UPDATED_BY | FdLinesLastUpdByUserPEOLastUpdatedBy3 | — |
| LAST_UPDATED_BY | FdTaxLineCrtdByUserPEOLastUpdatedBy10 | — |
| LAST_UPDATED_BY | FdTaxLineLastUpdByUserPEOLastUpdatedBy11 | — |
| LAST_UPDATED_BY | LastUpdatedUserPEOLastUpdatedBy11 | — |
| MULTITENANCY_USERNAME | CreatedByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FdHdrExtnCrtdByUserPEOMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FdHdrExtnLastUpdByUserPEOMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | FdLinesCrtdByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdLinesLastUpdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FdTaxLineCrtdByUserPEOMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | FdTaxLineLastUpdByUserPEOMultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | LastUpdatedUserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | CreatedByUserPEOObjectVersionNumber11 | — |
| OBJECT_VERSION_NUMBER | FdHdrExtnCrtdByUserPEOObjectVersionNumber8 | — |
| OBJECT_VERSION_NUMBER | FdHdrExtnLastUpdByUserPEOObjectVersionNumber9 | — |
| OBJECT_VERSION_NUMBER | FdLinesCrtdByUserPEOObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | FdLinesLastUpdByUserPEOObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | FdTaxLineCrtdByUserPEOObjectVersionNumber14 | — |
| OBJECT_VERSION_NUMBER | FdTaxLineLastUpdByUserPEOObjectVersionNumber15 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedUserPEOObjectVersionNumber10 | — |
| PARTY_ID | CreatedByUserPEOPartyId1 | — |
| PARTY_ID | FdHdrExtnCrtdByUserPEOPartyId2 | — |
| PARTY_ID | FdHdrExtnLastUpdByUserPEOPartyId3 | — |
| PARTY_ID | FdLinesCrtdByUserPEOPartyId | — |
| PARTY_ID | FdLinesLastUpdByUserPEOPartyId1 | — |
| PARTY_ID | FdTaxLineCrtdByUserPEOPartyId4 | — |
| PARTY_ID | FdTaxLineLastUpdByUserPEOPartyId5 | — |
| PARTY_ID | LastUpdatedUserPEOPartyId | — |
| PERSON_ID | CreatedByUserPEOPersonId1 | — |
| PERSON_ID | FdHdrExtnCrtdByUserPEOPersonId4 | — |
| PERSON_ID | FdHdrExtnLastUpdByUserPEOPersonId5 | — |
| PERSON_ID | FdLinesCrtdByUserPEOPersonId | — |
| PERSON_ID | FdLinesLastUpdByUserPEOPersonId1 | — |
| PERSON_ID | FdTaxLineCrtdByUserPEOPersonId8 | — |
| PERSON_ID | FdTaxLineLastUpdByUserPEOPersonId9 | — |
| PERSON_ID | LastUpdatedUserPEOPersonId | — |
| START_DATE | CreatedByUserPEOStartDate1 | — |
| START_DATE | FdHdrExtnCrtdByUserPEOStartDate2 | — |
| START_DATE | FdHdrExtnLastUpdByUserPEOStartDate3 | — |
| START_DATE | FdLinesCrtdByUserPEOStartDate | — |
| START_DATE | FdLinesLastUpdByUserPEOStartDate1 | — |
| START_DATE | FdTaxLineCrtdByUserPEOStartDate4 | — |
| START_DATE | FdTaxLineLastUpdByUserPEOStartDate5 | — |
| START_DATE | LastUpdatedUserPEOStartDate | — |
| SUSPENDED | CreatedByUserPEOSuspended1 | — |
| SUSPENDED | FdHdrExtnCrtdByUserPEOSuspended2 | — |
| SUSPENDED | FdHdrExtnLastUpdByUserPEOSuspended3 | — |
| SUSPENDED | FdLinesCrtdByUserPEOSuspended | — |
| SUSPENDED | FdLinesLastUpdByUserPEOSuspended1 | — |
| SUSPENDED | FdTaxLineCrtdByUserPEOSuspended4 | — |
| SUSPENDED | FdTaxLineLastUpdByUserPEOSuspended5 | — |
| SUSPENDED | LastUpdatedUserPEOSuspended | — |
| USER_DATA_CHECKSUM | CreatedByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FdHdrExtnCrtdByUserPEOUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FdHdrExtnLastUpdByUserPEOUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | FdLinesCrtdByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdLinesLastUpdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FdTaxLineCrtdByUserPEOUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | FdTaxLineLastUpdByUserPEOUserDataChecksum5 | — |
| USER_DATA_CHECKSUM | LastUpdatedUserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | CreatedByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FdHdrExtnCrtdByUserPEOUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FdHdrExtnLastUpdByUserPEOUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | FdLinesCrtdByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdLinesLastUpdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FdTaxLineCrtdByUserPEOUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | FdTaxLineLastUpdByUserPEOUserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | LastUpdatedUserPEOUserDistinguishedName | — |
| USER_GUID | CreatedByUserPEOUserGuid1 | — |
| USER_GUID | FdHdrExtnCrtdByUserPEOUserGuid2 | — |
| USER_GUID | FdHdrExtnLastUpdByUserPEOUserGuid3 | — |
| USER_GUID | FdLinesCrtdByUserPEOUserGuid | — |
| USER_GUID | FdLinesLastUpdByUserPEOUserGuid1 | — |
| USER_GUID | FdTaxLineCrtdByUserPEOUserGuid4 | — |
| USER_GUID | FdTaxLineLastUpdByUserPEOUserGuid5 | — |
| USER_GUID | LastUpdatedUserPEOUserGuid | — |
| USER_ID | CreatedByUserPEOUserId1 | — |
| USER_ID | FdHdrExtnCrtdByUserPEOUserId2 | — |
| USER_ID | FdLinesCrtdByUserPEOUserId | — |
| USER_ID | FdTaxLineCrtdByUserPEOUserId4 | — |
| USER_ID | FdTaxLineLastUpdByUserPEOUserId5 | — |
| USER_ID | LastUpdatedUserPEOUserId | — |
| USER_ID | UserId1 | — |
| USER_ID | UserId3 | — |
| USERNAME | CreatedByUserPEOUsername1 | — |
| USERNAME | FdHdrExtnCrtdByUserPEOUsername2 | — |
| USERNAME | FdHdrExtnLastUpdByUserPEOUsername3 | — |
| USERNAME | FdLinesCrtdByUserPEOUsername | — |
| USERNAME | FdLinesLastUpdByUserPEOUsername1 | — |
| USERNAME | FdTaxLineCrtdByUserPEOUsername4 | — |
| USERNAME | FdTaxLineLastUpdByUserPEOUsername5 | — |
| USERNAME | LastUpdatedUserPEOUsername | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdHdrExtnCrtdByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdHdrExtnLastUpdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FdLinesCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdLinesLastUpdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FdTaxCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | FdTaxLastUpdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | LastUpdatedUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | CreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdHdrExtnCrtdByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdHdrExtnLastUpdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FdLinesCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdLinesLastUpdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FdTaxCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FdTaxLastUpdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | LastUpdatedUserPEOBusinessGroupId | — |
| CREATED_BY | CreatedByUserPEOCreatedBy | — |
| CREATED_BY | FdHdrExtnCrtdByUserPEOCreatedBy | — |
| CREATED_BY | FdHdrExtnLastUpdByUserPEOCreatedBy1 | — |
| CREATED_BY | FdLinesCreatedByUserPEOCreatedBy | — |
| CREATED_BY | FdLinesLastUpdByUserPEOCreatedBy1 | — |
| CREATED_BY | FdTaxCreatedByUserPEOCreatedBy | — |
| CREATED_BY | FdTaxLastUpdByUserPEOCreatedBy1 | — |
| CREATED_BY | LastUpdatedUserPEOCreatedBy | — |
| CREATION_DATE | CreatedByUserPEOCreationDate | — |
| CREATION_DATE | FdHdrExtnCrtdByUserPEOCreationDate | — |
| CREATION_DATE | FdHdrExtnLastUpdByUserPEOCreationDate1 | — |
| CREATION_DATE | FdLinesCreatedByUserPEOCreationDate | — |
| CREATION_DATE | FdLinesLastUpdByUserPEOCreationDate1 | — |
| CREATION_DATE | FdTaxCreatedByUserPEOCreationDate | — |
| CREATION_DATE | FdTaxLastUpdByUserPEOCreationDate1 | — |
| CREATION_DATE | LastUpdatedUserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdHdrExtnCrtdByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdHdrExtnLastUpdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FdLinesCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdLinesLastUpdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FdTaxCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FdTaxLastUpdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedUserPEOCredentialsEmailSent | — |
| END_DATE | CreatedByUserPEOEndDate | — |
| END_DATE | FdHdrExtnCrtdByUserPEOEndDate | — |
| END_DATE | FdHdrExtnLastUpdByUserPEOEndDate1 | — |
| END_DATE | FdLinesCreatedByUserPEOEndDate | — |
| END_DATE | FdLinesLastUpdByUserPEOEndDate1 | — |
| END_DATE | FdTaxCreatedByUserPEOEndDate | — |
| END_DATE | FdTaxLastUpdByUserPEOEndDate1 | — |
| END_DATE | LastUpdatedUserPEOEndDate | — |
| EXTERNAL_ID | CreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FdHdrExtnCrtdByUserPEOExternalId | — |
| EXTERNAL_ID | FdHdrExtnLastUpdByUserPEOExternalId1 | — |
| EXTERNAL_ID | FdLinesCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FdLinesLastUpdByUserPEOExternalId1 | — |
| EXTERNAL_ID | FdTaxCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FdTaxLastUpdByUserPEOExternalId1 | — |
| EXTERNAL_ID | LastUpdatedUserPEOExternalId | — |
| HR_TERMINATED | CreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FdHdrExtnCrtdByUserPEOHrTerminated | — |
| HR_TERMINATED | FdHdrExtnLastUpdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | FdLinesCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FdLinesLastUpdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | FdTaxCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FdTaxLastUpdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | LastUpdatedUserPEOHrTerminated | — |
| LAST_UPDATE_DATE | CreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FdHdrExtnCrtdByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FdHdrExtnLastUpdByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_DATE | FdLinesCreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FdLinesLastUpdByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_DATE | FdTaxCreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | FdTaxLastUpdByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_DATE | LastUpdatedUserPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | CreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FdHdrExtnCrtdByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FdHdrExtnLastUpdByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | FdLinesCreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FdLinesLastUpdByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | FdTaxCreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FdTaxLastUpdByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | LastUpdatedUserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FdHdrExtnCrtdByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FdHdrExtnLastUpdByUserPEOLastUpdatedBy1 | — |
| LAST_UPDATED_BY | FdLinesCreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FdLinesLastUpdByUserPEOLastUpdatedBy1 | — |
| LAST_UPDATED_BY | FdTaxCreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | FdTaxLastUpdByUserPEOLastUpdatedBy1 | — |
| LAST_UPDATED_BY | LastUpdatedUserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | CreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdHdrExtnCrtdByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdHdrExtnLastUpdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FdLinesCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdLinesLastUpdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FdTaxCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FdTaxLastUpdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | LastUpdatedUserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | CreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FdHdrExtnCrtdByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FdHdrExtnLastUpdByUserPEOObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | FdLinesCreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FdLinesLastUpdByUserPEOObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | FdTaxCreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FdTaxLastUpdByUserPEOObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | LastUpdatedUserPEOObjectVersionNumber | — |
| PARTY_ID | CreatedByUserPEOPartyId | — |
| PARTY_ID | FdHdrExtnCrtdByUserPEOPartyId | — |
| PARTY_ID | FdHdrExtnLastUpdByUserPEOPartyId1 | — |
| PARTY_ID | FdLinesCreatedByUserPEOPartyId | — |
| PARTY_ID | FdLinesLastUpdByUserPEOPartyId1 | — |
| PARTY_ID | FdTaxCreatedByUserPEOPartyId | — |
| PARTY_ID | FdTaxLastUpdByUserPEOPartyId1 | — |
| PARTY_ID | LastUpdatedUserPEOPartyId | — |
| PERSON_ID | CreatedByUserPEOPersonId | — |
| PERSON_ID | FdHdrExtnCrtdByUserPEOPersonId | — |
| PERSON_ID | FdHdrExtnLastUpdByUserPEOPersonId1 | — |
| PERSON_ID | FdLinesCreatedByUserPEOPersonId | — |
| PERSON_ID | FdLinesLastUpdByUserPEOPersonId1 | — |
| PERSON_ID | FdTaxCreatedByUserPEOPersonId | — |
| PERSON_ID | FdTaxLastUpdByUserPEOPersonId1 | — |
| PERSON_ID | LastUpdatedUserPEOPersonId | — |
| START_DATE | CreatedByUserPEOStartDate | — |
| START_DATE | FdHdrExtnCrtdByUserPEOStartDate | — |
| START_DATE | FdHdrExtnLastUpdByUserPEOStartDate1 | — |
| START_DATE | FdLinesCreatedByUserPEOStartDate | — |
| START_DATE | FdLinesLastUpdByUserPEOStartDate1 | — |
| START_DATE | FdTaxCreatedByUserPEOStartDate | — |
| START_DATE | FdTaxLastUpdByUserPEOStartDate1 | — |
| START_DATE | LastUpdatedUserPEOStartDate | — |
| SUSPENDED | CreatedByUserPEOSuspended | — |
| SUSPENDED | FdHdrExtnCrtdByUserPEOSuspended | — |
| SUSPENDED | FdHdrExtnLastUpdByUserPEOSuspended1 | — |
| SUSPENDED | FdLinesCreatedByUserPEOSuspended | — |
| SUSPENDED | FdLinesLastUpdByUserPEOSuspended1 | — |
| SUSPENDED | FdTaxCreatedByUserPEOSuspended | — |
| SUSPENDED | FdTaxLastUpdByUserPEOSuspended1 | — |
| SUSPENDED | LastUpdatedUserPEOSuspended | — |
| USER_DATA_CHECKSUM | CreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdHdrExtnCrtdByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdHdrExtnLastUpdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FdLinesCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdLinesLastUpdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FdTaxCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FdTaxLastUpdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | LastUpdatedUserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | CreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdHdrExtnCrtdByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdHdrExtnLastUpdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FdLinesCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdLinesLastUpdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FdTaxCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FdTaxLastUpdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | LastUpdatedUserPEOUserDistinguishedName | — |
| USER_GUID | CreatedByUserPEOUserGuid | — |
| USER_GUID | FdHdrExtnCrtdByUserPEOUserGuid | — |
| USER_GUID | FdHdrExtnLastUpdByUserPEOUserGuid1 | — |
| USER_GUID | FdLinesCreatedByUserPEOUserGuid | — |
| USER_GUID | FdLinesLastUpdByUserPEOUserGuid1 | — |
| USER_GUID | FdTaxCreatedByUserPEOUserGuid | — |
| USER_GUID | FdTaxLastUpdByUserPEOUserGuid1 | — |
| USER_GUID | LastUpdatedUserPEOUserGuid | — |
| USER_ID | CreatedByUserPEOUserId | — |
| USER_ID | FdHdrExtnCrtdByUserPEOUserId | — |
| USER_ID | FdHdrExtnLastUpdByUserPEOUserId1 | — |
| USER_ID | FdLinesCreatedByUserPEOUserId | — |
| USER_ID | FdLinesLastUpdByUserPEOUserId1 | — |
| USER_ID | FdTaxCreatedByUserPEOUserId | — |
| USER_ID | FdTaxLastUpdByUserPEOUserId1 | — |
| USER_ID | LastUpdatedUserPEOUserId | — |
| USERNAME | CreatedByUserPEOUsername | — |
| USERNAME | FdHdrExtnCrtdByUserPEOUsername | — |
| USERNAME | FdHdrExtnLastUpdByUserPEOUsername1 | — |
| USERNAME | FdLinesCreatedByUserPEOUsername | — |
| USERNAME | FdLinesLastUpdByUserPEOUsername1 | — |
| USERNAME | FdTaxCreatedByUserPEOUsername | — |
| USERNAME | FdTaxLastUpdByUserPEOUsername1 | — |
| USERNAME | LastUpdatedUserPEOUsername | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FDHeadersCreatedByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | FDHeadersLastUpdatedByUserPEActiveFlag2 | — |
| ACTIVE_FLAG | FDLinesCreatedByUserPEOActiveFlag5 | — |
| ACTIVE_FLAG | FDLinesLastUpdatedByUserPEO1_1ActiveFlag6 | — |
| ACTIVE_FLAG | FDTaxLineCreatedByUserPEOActiveFlag3 | — |
| ACTIVE_FLAG | FDTaxLineLastUpdatedByUserPEActiveFlag4 | — |
| ACTIVE_FLAG | HeaderExtnEOtoCreatedByUserPActiveFlag | — |
| ACTIVE_FLAG | HeaderExtnToLastUpdtdUserPEOActiveFlag1 | — |
| BUSINESS_GROUP_ID | FDHeadersCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDHeadersLastUpdatedByUserPEBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FDLinesCreatedByUserPEOBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | FDLinesLastUpdatedByUserPEO1_1BusinessGroupId5 | — |
| BUSINESS_GROUP_ID | FDTaxLineCreatedByUserPEOBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | FDTaxLineLastUpdatedByUserPEBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | HeaderExtnEOtoCreatedByUserPBusinessGroupId | — |
| BUSINESS_GROUP_ID | HeaderExtnToLastUpdtdUserPEOBusinessGroupId1 | — |
| CREATED_BY | FDHeadersCreatedByUserPEOCreatedBy10 | — |
| CREATED_BY | FDHeadersLastUpdatedByUserPECreatedBy11 | — |
| CREATED_BY | FDLinesCreatedByUserPEOCreatedBy14 | — |
| CREATED_BY | FDLinesLastUpdatedByUserPEO1_1CreatedBy15 | — |
| CREATED_BY | FDTaxLineCreatedByUserPEOCreatedBy12 | — |
| CREATED_BY | FDTaxLineLastUpdatedByUserPECreatedBy13 | — |
| CREATED_BY | HeaderExtnEOtoCreatedByUserPCreatedBy | — |
| CREATED_BY | HeaderExtnToLastUpdtdUserPEOCreatedBy1 | — |
| CREATION_DATE | FDHeadersCreatedByUserPEOCreationDate10 | — |
| CREATION_DATE | FDHeadersLastUpdatedByUserPECreationDate11 | — |
| CREATION_DATE | FDLinesCreatedByUserPEOCreationDate14 | — |
| CREATION_DATE | FDLinesLastUpdatedByUserPEO1_1CreationDate15 | — |
| CREATION_DATE | FDTaxLineCreatedByUserPEOCreationDate12 | — |
| CREATION_DATE | FDTaxLineLastUpdatedByUserPECreationDate13 | — |
| CREATION_DATE | HeaderExtnEOtoCreatedByUserPCreationDate | — |
| CREATION_DATE | HeaderExtnToLastUpdtdUserPEOCreationDate1 | — |
| CREDENTIALS_EMAIL_SENT | FDHeadersCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDHeadersLastUpdatedByUserPECredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FDLinesCreatedByUserPEOCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | FDLinesLastUpdatedByUserPEO1_1CredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | FDTaxLineCreatedByUserPEOCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FDTaxLineLastUpdatedByUserPECredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | HeaderExtnEOtoCreatedByUserPCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | HeaderExtnToLastUpdtdUserPEOCredentialsEmailSent1 | — |
| END_DATE | FDHeadersCreatedByUserPEOEndDate | — |
| END_DATE | FDHeadersLastUpdatedByUserPEEndDate1 | — |
| END_DATE | FDLinesCreatedByUserPEOEndDate4 | — |
| END_DATE | FDLinesLastUpdatedByUserPEO1_1EndDate5 | — |
| END_DATE | FDTaxLineCreatedByUserPEOEndDate2 | — |
| END_DATE | FDTaxLineLastUpdatedByUserPEEndDate3 | — |
| END_DATE | HeaderExtnEOtoCreatedByUserPEndDate | — |
| END_DATE | HeaderExtnToLastUpdtdUserPEOEndDate1 | — |
| EXTERNAL_ID | FDHeadersCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | FDHeadersLastUpdatedByUserPEExternalId1 | — |
| EXTERNAL_ID | FDLinesCreatedByUserPEOExternalId4 | — |
| EXTERNAL_ID | FDLinesLastUpdatedByUserPEO1_1ExternalId5 | — |
| EXTERNAL_ID | FDTaxLineCreatedByUserPEOExternalId2 | — |
| EXTERNAL_ID | FDTaxLineLastUpdatedByUserPEExternalId3 | — |
| EXTERNAL_ID | HeaderExtnEOtoCreatedByUserPExternalId | — |
| EXTERNAL_ID | HeaderExtnToLastUpdtdUserPEOExternalId1 | — |
| HR_TERMINATED | FDHeadersCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | FDHeadersLastUpdatedByUserPEHrTerminated1 | — |
| HR_TERMINATED | FDLinesCreatedByUserPEOHrTerminated4 | — |
| HR_TERMINATED | FDLinesLastUpdatedByUserPEO1_1HrTerminated5 | — |
| HR_TERMINATED | FDTaxLineCreatedByUserPEOHrTerminated2 | — |
| HR_TERMINATED | FDTaxLineLastUpdatedByUserPEHrTerminated3 | — |
| HR_TERMINATED | HeaderExtnEOtoCreatedByUserPHrTerminated | — |
| HR_TERMINATED | HeaderExtnToLastUpdtdUserPEOHrTerminated1 | — |
| LAST_UPDATE_DATE | FDHeadersCreatedByUserPEOLastUpdateDate10 | — |
| LAST_UPDATE_DATE | FDHeadersLastUpdatedByUserPELastUpdateDate11 | — |
| LAST_UPDATE_DATE | FDLinesCreatedByUserPEOLastUpdateDate14 | — |
| LAST_UPDATE_DATE | FDLinesLastUpdatedByUserPEO1_1LastUpdateDate15 | — |
| LAST_UPDATE_DATE | FDTaxLineCreatedByUserPEOLastUpdateDate12 | — |
| LAST_UPDATE_DATE | FDTaxLineLastUpdatedByUserPELastUpdateDate13 | — |
| LAST_UPDATE_DATE | HeaderExtnEOtoCreatedByUserPLastUpdateDate | — |
| LAST_UPDATE_DATE | HeaderExtnToLastUpdtdUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | FDHeadersCreatedByUserPEOLastUpdateLogin10 | — |
| LAST_UPDATE_LOGIN | FDHeadersLastUpdatedByUserPELastUpdateLogin11 | — |
| LAST_UPDATE_LOGIN | FDLinesCreatedByUserPEOLastUpdateLogin14 | — |
| LAST_UPDATE_LOGIN | FDLinesLastUpdatedByUserPEO1_1LastUpdateLogin15 | — |
| LAST_UPDATE_LOGIN | FDTaxLineCreatedByUserPEOLastUpdateLogin12 | — |
| LAST_UPDATE_LOGIN | FDTaxLineLastUpdatedByUserPELastUpdateLogin13 | — |
| LAST_UPDATE_LOGIN | HeaderExtnEOtoCreatedByUserPLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | HeaderExtnToLastUpdtdUserPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | FDHeadersCreatedByUserPEOLastUpdatedBy10 | — |
| LAST_UPDATED_BY | FDHeadersLastUpdatedByUserPELastUpdatedBy11 | — |
| LAST_UPDATED_BY | FDLinesCreatedByUserPEOLastUpdatedBy14 | — |
| LAST_UPDATED_BY | FDLinesLastUpdatedByUserPEO1_1LastUpdatedBy15 | — |
| LAST_UPDATED_BY | FDTaxLineCreatedByUserPEOLastUpdatedBy12 | — |
| LAST_UPDATED_BY | FDTaxLineLastUpdatedByUserPELastUpdatedBy13 | — |
| LAST_UPDATED_BY | HeaderExtnEOtoCreatedByUserPLastUpdatedBy | — |
| LAST_UPDATED_BY | HeaderExtnToLastUpdtdUserPEOLastUpdatedBy1 | — |
| MULTITENANCY_USERNAME | FDHeadersCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDHeadersLastUpdatedByUserPEMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FDLinesCreatedByUserPEOMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | FDLinesLastUpdatedByUserPEO1_1MultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | FDTaxLineCreatedByUserPEOMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FDTaxLineLastUpdatedByUserPEMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | HeaderExtnEOtoCreatedByUserPMultitenancyUsername | — |
| MULTITENANCY_USERNAME | HeaderExtnToLastUpdtdUserPEOMultitenancyUsername1 | — |
| OBJECT_VERSION_NUMBER | FDHeadersCreatedByUserPEOObjectVersionNumber8 | — |
| OBJECT_VERSION_NUMBER | FDHeadersLastUpdatedByUserPEObjectVersionNumber9 | — |
| OBJECT_VERSION_NUMBER | FDLinesCreatedByUserPEOObjectVersionNumber12 | — |
| OBJECT_VERSION_NUMBER | FDLinesLastUpdatedByUserPEO1_1ObjectVersionNumber13 | — |
| OBJECT_VERSION_NUMBER | FDTaxLineCreatedByUserPEOObjectVersionNumber10 | — |
| OBJECT_VERSION_NUMBER | FDTaxLineLastUpdatedByUserPEObjectVersionNumber11 | — |
| OBJECT_VERSION_NUMBER | HeaderExtnEOtoCreatedByUserPObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | HeaderExtnToLastUpdtdUserPEOObjectVersionNumber1 | — |
| PARTY_ID | FDHeadersCreatedByUserPEOPartyId | — |
| PARTY_ID | FDHeadersLastUpdatedByUserPEPartyId1 | — |
| PARTY_ID | FDLinesCreatedByUserPEOPartyId4 | — |
| PARTY_ID | FDLinesLastUpdatedByUserPEO1_1PartyId5 | — |
| PARTY_ID | FDTaxLineCreatedByUserPEOPartyId2 | — |
| PARTY_ID | FDTaxLineLastUpdatedByUserPEPartyId3 | — |
| PARTY_ID | HeaderExtnEOtoCreatedByUserPPartyId | — |
| PARTY_ID | HeaderExtnToLastUpdtdUserPEOPartyId1 | — |
| PERSON_ID | FDHeadersCreatedByUserPEOPersonId | — |
| PERSON_ID | FDHeadersLastUpdatedByUserPEPersonId1 | — |
| PERSON_ID | FDLinesCreatedByUserPEOPersonId4 | — |
| PERSON_ID | FDLinesLastUpdatedByUserPEO1_1PersonId5 | — |
| PERSON_ID | FDTaxLineCreatedByUserPEOPersonId2 | — |
| PERSON_ID | FDTaxLineLastUpdatedByUserPEPersonId3 | — |
| PERSON_ID | HeaderExtnEOtoCreatedByUserPPersonId | — |
| PERSON_ID | HeaderExtnToLastUpdtdUserPEOPersonId1 | — |
| START_DATE | FDHeadersCreatedByUserPEOStartDate | — |
| START_DATE | FDHeadersLastUpdatedByUserPEStartDate1 | — |
| START_DATE | FDLinesCreatedByUserPEOStartDate4 | — |
| START_DATE | FDLinesLastUpdatedByUserPEO1_1StartDate5 | — |
| START_DATE | FDTaxLineCreatedByUserPEOStartDate2 | — |
| START_DATE | FDTaxLineLastUpdatedByUserPEStartDate3 | — |
| START_DATE | HeaderExtnEOtoCreatedByUserPStartDate | — |
| START_DATE | HeaderExtnToLastUpdtdUserPEOStartDate1 | — |
| SUSPENDED | FDHeadersCreatedByUserPEOSuspended | — |
| SUSPENDED | FDHeadersLastUpdatedByUserPESuspended1 | — |
| SUSPENDED | FDLinesCreatedByUserPEOSuspended4 | — |
| SUSPENDED | FDLinesLastUpdatedByUserPEO1_1Suspended5 | — |
| SUSPENDED | FDTaxLineCreatedByUserPEOSuspended2 | — |
| SUSPENDED | FDTaxLineLastUpdatedByUserPESuspended3 | — |
| SUSPENDED | HeaderExtnEOtoCreatedByUserPSuspended | — |
| SUSPENDED | HeaderExtnToLastUpdtdUserPEOSuspended1 | — |
| USER_DATA_CHECKSUM | FDHeadersCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDHeadersLastUpdatedByUserPEUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FDLinesCreatedByUserPEOUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | FDLinesLastUpdatedByUserPEO1_1UserDataChecksum5 | — |
| USER_DATA_CHECKSUM | FDTaxLineCreatedByUserPEOUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FDTaxLineLastUpdatedByUserPEUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | HeaderExtnEOtoCreatedByUserPUserDataChecksum | — |
| USER_DATA_CHECKSUM | HeaderExtnToLastUpdtdUserPEOUserDataChecksum1 | — |
| USER_DISTINGUISHED_NAME | FDHeadersCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDHeadersLastUpdatedByUserPEUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FDLinesCreatedByUserPEOUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | FDLinesLastUpdatedByUserPEO1_1UserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | FDTaxLineCreatedByUserPEOUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FDTaxLineLastUpdatedByUserPEUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | HeaderExtnEOtoCreatedByUserPUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | HeaderExtnToLastUpdtdUserPEOUserDistinguishedName1 | — |
| USER_GUID | FDHeadersCreatedByUserPEOUserGuid | — |
| USER_GUID | FDHeadersLastUpdatedByUserPEUserGuid1 | — |
| USER_GUID | FDLinesCreatedByUserPEOUserGuid4 | — |
| USER_GUID | FDLinesLastUpdatedByUserPEO1_1UserGuid5 | — |
| USER_GUID | FDTaxLineCreatedByUserPEOUserGuid2 | — |
| USER_GUID | FDTaxLineLastUpdatedByUserPEUserGuid3 | — |
| USER_GUID | HeaderExtnEOtoCreatedByUserPUserGuid | — |
| USER_GUID | HeaderExtnToLastUpdtdUserPEOUserGuid1 | — |
| USER_ID | FDHeadersCreatedByUserPEOUserId | — |
| USER_ID | FDHeadersLastUpdatedByUserPEUserId1 | — |
| USER_ID | FDLinesCreatedByUserPEOUserId4 | — |
| USER_ID | FDLinesLastUpdatedByUserPEO1_1UserId5 | — |
| USER_ID | FDTaxLineCreatedByUserPEOUserId2 | — |
| USER_ID | FDTaxLineLastUpdatedByUserPEUserId3 | — |
| USER_ID | HeaderExtnEOtoCreatedByUserPUserId | — |
| USER_ID | HeaderExtnToLastUpdtdUserPEOUserId1 | — |
| USERNAME | FDHeadersCreatedByUserPEOUsername | — |
| USERNAME | FDHeadersLastUpdatedByUserPEUsername1 | — |
| USERNAME | FDLinesCreatedByUserPEOUsername4 | — |
| USERNAME | FDLinesLastUpdatedByUserPEO1_1Username5 | — |
| USERNAME | FDTaxLineCreatedByUserPEOUsername2 | — |
| USERNAME | FDTaxLineLastUpdatedByUserPEUsername3 | — |
| USERNAME | HeaderExtnEOtoCreatedByUserPUsername | — |
| USERNAME | HeaderExtnToLastUpdtdUserPEOUsername1 | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FiscDocHdrExtnCreatedByUserActiveFlag8 | — |
| ACTIVE_FLAG | FiscDocHdrExtnLastUpdtUserActiveFlag9 | — |
| ACTIVE_FLAG | FiscDocTaxLineCreatedByUserPActiveFlag6 | — |
| ACTIVE_FLAG | FiscDocTaxLineLastUpdtUserPActiveFlag7 | — |
| ACTIVE_FLAG | FiscalDocHeaderCreatedByUserActiveFlag | — |
| ACTIVE_FLAG | FiscalDocHeaderLastUpdatedByActiveFlag1 | — |
| ACTIVE_FLAG | FiscalDocSchedulesCreatedByUActiveFlag5 | — |
| ACTIVE_FLAG | FiscalDocSchedulesLastUpdtUsActiveFlag4 | — |
| ACTIVE_FLAG | FiscalDocumentLinesCreatedByActiveFlag2 | — |
| ACTIVE_FLAG | FiscalDocumentLinesLastUpdatActiveFlag3 | — |
| BUSINESS_GROUP_ID | FiscDocHdrExtnCreatedByUserBusinessGroupId16 | — |
| BUSINESS_GROUP_ID | FiscDocHdrExtnLastUpdtUserBusinessGroupId18 | — |
| BUSINESS_GROUP_ID | FiscDocTaxLineCreatedByUserPBusinessGroupId12 | — |
| BUSINESS_GROUP_ID | FiscDocTaxLineLastUpdtUserPBusinessGroupId | — |
| BUSINESS_GROUP_ID | FiscalDocHeaderCreatedByUserBusinessGroupId20 | — |
| BUSINESS_GROUP_ID | FiscalDocHeaderLastUpdatedByBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FiscalDocSchedulesCreatedByUBusinessGroupId7 | — |
| BUSINESS_GROUP_ID | FiscalDocSchedulesLastUpdtUsBusinessGroupId6 | — |
| BUSINESS_GROUP_ID | FiscalDocumentLinesCreatedByBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | FiscalDocumentLinesLastUpdatBusinessGroupId5 | — |
| CREATED_BY | FiscDocHdrExtnCreatedByUserCreatedBy45 | — |
| CREATED_BY | FiscDocHdrExtnLastUpdtUserCreatedBy47 | — |
| CREATED_BY | FiscDocTaxLineCreatedByUserPCreatedBy41 | — |
| CREATED_BY | FiscDocTaxLineLastUpdtUserPCreatedBy43 | — |
| CREATED_BY | FiscalDocHeaderCreatedByUserCreatedBy18 | — |
| CREATED_BY | FiscalDocHeaderLastUpdatedByCreatedBy19 | — |
| CREATED_BY | FiscalDocSchedulesCreatedByUCreatedBy26 | — |
| CREATED_BY | FiscalDocSchedulesLastUpdtUsCreatedBy25 | — |
| CREATED_BY | FiscalDocumentLinesCreatedByCreatedBy23 | — |
| CREATED_BY | FiscalDocumentLinesLastUpdatCreatedBy24 | — |
| CREATION_DATE | FiscDocHdrExtnCreatedByUserCreationDate45 | — |
| CREATION_DATE | FiscDocHdrExtnLastUpdtUserCreationDate47 | — |
| CREATION_DATE | FiscDocTaxLineCreatedByUserPCreationDate41 | — |
| CREATION_DATE | FiscDocTaxLineLastUpdtUserPCreationDate43 | — |
| CREATION_DATE | FiscalDocHeaderCreatedByUserCreationDate18 | — |
| CREATION_DATE | FiscalDocHeaderLastUpdatedByCreationDate19 | — |
| CREATION_DATE | FiscalDocSchedulesCreatedByUCreationDate26 | — |
| CREATION_DATE | FiscalDocSchedulesLastUpdtUsCreationDate25 | — |
| CREATION_DATE | FiscalDocumentLinesCreatedByCreationDate23 | — |
| CREATION_DATE | FiscalDocumentLinesLastUpdatCreationDate24 | — |
| CREDENTIALS_EMAIL_SENT | FiscDocHdrExtnCreatedByUserCredentialsEmailSent8 | — |
| CREDENTIALS_EMAIL_SENT | FiscDocHdrExtnLastUpdtUserCredentialsEmailSent9 | — |
| CREDENTIALS_EMAIL_SENT | FiscDocTaxLineCreatedByUserPCredentialsEmailSent6 | — |
| CREDENTIALS_EMAIL_SENT | FiscDocTaxLineLastUpdtUserPFiscDocTaxLineLastUpdtUserPCredentialsEmailSent7 | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocHeaderCreatedByUserCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocHeaderLastUpdatedByCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocSchedulesCreatedByUCredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocSchedulesLastUpdtUsCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocumentLinesCreatedByCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FiscalDocumentLinesLastUpdatCredentialsEmailSent3 | — |
| END_DATE | FiscDocHdrExtnCreatedByUserEndDate11 | — |
| END_DATE | FiscDocHdrExtnLastUpdtUserEndDate12 | — |
| END_DATE | FiscDocTaxLineCreatedByUserPEndDate9 | — |
| END_DATE | FiscDocTaxLineLastUpdtUserPEndDate10 | — |
| END_DATE | FiscalDocHeaderCreatedByUserEndDate2 | — |
| END_DATE | FiscalDocHeaderLastUpdatedByEndDate3 | — |
| END_DATE | FiscalDocSchedulesCreatedByUEndDate7 | — |
| END_DATE | FiscalDocSchedulesLastUpdtUsEndDate6 | — |
| END_DATE | FiscalDocumentLinesCreatedByEndDate4 | — |
| END_DATE | FiscalDocumentLinesLastUpdatEndDate5 | — |
| EXTERNAL_ID | FiscDocHdrExtnCreatedByUserExternalId8 | — |
| EXTERNAL_ID | FiscDocHdrExtnLastUpdtUserExternalId9 | — |
| EXTERNAL_ID | FiscDocTaxLineCreatedByUserPExternalId6 | — |
| EXTERNAL_ID | FiscDocTaxLineLastUpdtUserPExternalId7 | — |
| EXTERNAL_ID | FiscalDocHeaderCreatedByUserExternalId | — |
| EXTERNAL_ID | FiscalDocHeaderLastUpdatedByExternalId1 | — |
| EXTERNAL_ID | FiscalDocSchedulesCreatedByUExternalId5 | — |
| EXTERNAL_ID | FiscalDocSchedulesLastUpdtUsExternalId4 | — |
| EXTERNAL_ID | FiscalDocumentLinesCreatedByExternalId2 | — |
| EXTERNAL_ID | FiscalDocumentLinesLastUpdatExternalId3 | — |
| HR_TERMINATED | FiscDocHdrExtnCreatedByUserHrTerminated8 | — |
| HR_TERMINATED | FiscDocHdrExtnLastUpdtUserHrTerminated9 | — |
| HR_TERMINATED | FiscDocTaxLineCreatedByUserPHrTerminated6 | — |
| HR_TERMINATED | FiscDocTaxLineLastUpdtUserPHrTerminated7 | — |
| HR_TERMINATED | FiscalDocHeaderCreatedByUserHrTerminated | — |
| HR_TERMINATED | FiscalDocHeaderLastUpdatedByHrTerminated1 | — |
| HR_TERMINATED | FiscalDocSchedulesCreatedByUHrTerminated5 | — |
| HR_TERMINATED | FiscalDocSchedulesLastUpdtUsHrTerminated4 | — |
| HR_TERMINATED | FiscalDocumentLinesCreatedByHrTerminated2 | — |
| HR_TERMINATED | FiscalDocumentLinesLastUpdatHrTerminated3 | — |
| LAST_UPDATE_DATE | FiscDocHdrExtnCreatedByUserLastUpdateDate45 | — |
| LAST_UPDATE_DATE | FiscDocHdrExtnLastUpdtUserLastUpdateDate47 | — |
| LAST_UPDATE_DATE | FiscDocTaxLineCreatedByUserPLastUpdateDate41 | — |
| LAST_UPDATE_DATE | FiscDocTaxLineLastUpdtUserPLastUpdateDate43 | — |
| LAST_UPDATE_DATE | FiscalDocHeaderCreatedByUserLastUpdateDate18 | — |
| LAST_UPDATE_DATE | FiscalDocHeaderLastUpdatedByLastUpdateDate19 | — |
| LAST_UPDATE_DATE | FiscalDocSchedulesCreatedByULastUpdateDate26 | — |
| LAST_UPDATE_DATE | FiscalDocSchedulesLastUpdtUsLastUpdateDate25 | — |
| LAST_UPDATE_DATE | FiscalDocumentLinesCreatedByLastUpdateDate23 | — |
| LAST_UPDATE_DATE | FiscalDocumentLinesLastUpdatLastUpdateDate24 | — |
| LAST_UPDATE_LOGIN | FiscDocHdrExtnCreatedByUserLastUpdateLogin45 | — |
| LAST_UPDATE_LOGIN | FiscDocHdrExtnLastUpdtUserLastUpdateLogin47 | — |
| LAST_UPDATE_LOGIN | FiscDocTaxLineCreatedByUserPLastUpdateLogin41 | — |
| LAST_UPDATE_LOGIN | FiscDocTaxLineLastUpdtUserPLastUpdateLogin43 | — |
| LAST_UPDATE_LOGIN | FiscalDocHeaderCreatedByUserLastUpdateLogin18 | — |
| LAST_UPDATE_LOGIN | FiscalDocHeaderLastUpdatedByLastUpdateLogin19 | — |
| LAST_UPDATE_LOGIN | FiscalDocSchedulesCreatedByULastUpdateLogin26 | — |
| LAST_UPDATE_LOGIN | FiscalDocSchedulesLastUpdtUsLastUpdateLogin25 | — |
| LAST_UPDATE_LOGIN | FiscalDocumentLinesCreatedByLastUpdateLogin23 | — |
| LAST_UPDATE_LOGIN | FiscalDocumentLinesLastUpdatLastUpdateLogin24 | — |
| LAST_UPDATED_BY | FiscDocHdrExtnCreatedByUserLastUpdatedBy45 | — |
| LAST_UPDATED_BY | FiscDocHdrExtnLastUpdtUserLastUpdatedBy47 | — |
| LAST_UPDATED_BY | FiscDocTaxLineCreatedByUserPLastUpdatedBy41 | — |
| LAST_UPDATED_BY | FiscDocTaxLineLastUpdtUserPLastUpdatedBy43 | — |
| LAST_UPDATED_BY | FiscalDocHeaderCreatedByUserLastUpdatedBy18 | — |
| LAST_UPDATED_BY | FiscalDocHeaderLastUpdatedByLastUpdatedBy19 | — |
| LAST_UPDATED_BY | FiscalDocSchedulesCreatedByULastUpdatedBy26 | — |
| LAST_UPDATED_BY | FiscalDocSchedulesLastUpdtUsLastUpdatedBy25 | — |
| LAST_UPDATED_BY | FiscalDocumentLinesCreatedByLastUpdatedBy23 | — |
| LAST_UPDATED_BY | FiscalDocumentLinesLastUpdatLastUpdatedBy24 | — |
| MULTITENANCY_USERNAME | FiscDocHdrExtnCreatedByUserMultitenancyUsername8 | — |
| MULTITENANCY_USERNAME | FiscDocHdrExtnLastUpdtUserMultitenancyUsername9 | — |
| MULTITENANCY_USERNAME | FiscDocTaxLineCreatedByUserPMultitenancyUsername6 | — |
| MULTITENANCY_USERNAME | FiscDocTaxLineLastUpdtUserPFiscDocTaxLineLastUpdtUserPMultitenancyUsername7 | — |
| MULTITENANCY_USERNAME | FiscalDocHeaderCreatedByUserMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FiscalDocHeaderLastUpdatedByMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FiscalDocSchedulesCreatedByUMultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | FiscalDocSchedulesLastUpdtUsMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | FiscalDocumentLinesCreatedByMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FiscalDocumentLinesLastUpdatMultitenancyUsername3 | — |
| OBJECT_VERSION_NUMBER | FiscDocHdrExtnCreatedByUserObjectVersionNumber43 | — |
| OBJECT_VERSION_NUMBER | FiscDocHdrExtnLastUpdtUserObjectVersionNumber45 | — |
| OBJECT_VERSION_NUMBER | FiscDocTaxLineCreatedByUserPObjectVersionNumber39 | — |
| OBJECT_VERSION_NUMBER | FiscDocTaxLineLastUpdtUserPObjectVersionNumber41 | — |
| OBJECT_VERSION_NUMBER | FiscalDocHeaderCreatedByUserObjectVersionNumber17 | — |
| OBJECT_VERSION_NUMBER | FiscalDocHeaderLastUpdatedByObjectVersionNumber18 | — |
| OBJECT_VERSION_NUMBER | FiscalDocSchedulesCreatedByUObjectVersionNumber24 | — |
| OBJECT_VERSION_NUMBER | FiscalDocSchedulesLastUpdtUsObjectVersionNumber23 | — |
| OBJECT_VERSION_NUMBER | FiscalDocumentLinesCreatedByObjectVersionNumber21 | — |
| OBJECT_VERSION_NUMBER | FiscalDocumentLinesLastUpdatObjectVersionNumber22 | — |
| PARTY_ID | FiscDocHdrExtnCreatedByUserPartyId8 | — |
| PARTY_ID | FiscDocHdrExtnLastUpdtUserPartyId9 | — |
| PARTY_ID | FiscDocTaxLineCreatedByUserPPartyId6 | — |
| PARTY_ID | FiscDocTaxLineLastUpdtUserPPartyId7 | — |
| PARTY_ID | FiscalDocHeaderCreatedByUserPartyId | — |
| PARTY_ID | FiscalDocHeaderLastUpdatedByPartyId1 | — |
| PARTY_ID | FiscalDocSchedulesCreatedByUPartyId5 | — |
| PARTY_ID | FiscalDocSchedulesLastUpdtUsPartyId4 | — |
| PARTY_ID | FiscalDocumentLinesCreatedByPartyId2 | — |
| PARTY_ID | FiscalDocumentLinesLastUpdatPartyId3 | — |
| PERSON_ID | FiscDocHdrExtnCreatedByUserPersonId16 | — |
| PERSON_ID | FiscDocHdrExtnLastUpdtUserPersonId18 | — |
| PERSON_ID | FiscDocTaxLineCreatedByUserPPersonId12 | — |
| PERSON_ID | FiscDocTaxLineLastUpdtUserPPersonId14 | — |
| PERSON_ID | FiscalDocHeaderCreatedByUserPersonId | — |
| PERSON_ID | FiscalDocHeaderLastUpdatedByPersonId1 | — |
| PERSON_ID | FiscalDocSchedulesCreatedByUPersonId7 | — |
| PERSON_ID | FiscalDocSchedulesLastUpdtUsPersonId6 | — |
| PERSON_ID | FiscalDocumentLinesCreatedByPersonId4 | — |
| PERSON_ID | FiscalDocumentLinesLastUpdatPersonId5 | — |
| START_DATE | FiscDocHdrExtnCreatedByUserStartDate12 | — |
| START_DATE | FiscDocHdrExtnLastUpdtUserStartDate13 | — |
| START_DATE | FiscDocTaxLineCreatedByUserPStartDate10 | — |
| START_DATE | FiscDocTaxLineLastUpdtUserPStartDate11 | — |
| START_DATE | FiscalDocHeaderCreatedByUserStartDate3 | — |
| START_DATE | FiscalDocHeaderLastUpdatedByStartDate4 | — |
| START_DATE | FiscalDocSchedulesCreatedByUStartDate8 | — |
| START_DATE | FiscalDocSchedulesLastUpdtUsStartDate7 | — |
| START_DATE | FiscalDocumentLinesCreatedByStartDate5 | — |
| START_DATE | FiscalDocumentLinesLastUpdatStartDate6 | — |
| SUSPENDED | FiscDocHdrExtnCreatedByUserSuspended8 | — |
| SUSPENDED | FiscDocHdrExtnLastUpdtUserSuspended9 | — |
| SUSPENDED | FiscDocTaxLineCreatedByUserPSuspended6 | — |
| SUSPENDED | FiscDocTaxLineLastUpdtUserPSuspended7 | — |
| SUSPENDED | FiscalDocHeaderCreatedByUserSuspended | — |
| SUSPENDED | FiscalDocHeaderLastUpdatedBySuspended1 | — |
| SUSPENDED | FiscalDocSchedulesCreatedByUSuspended5 | — |
| SUSPENDED | FiscalDocSchedulesLastUpdtUsSuspended4 | — |
| SUSPENDED | FiscalDocumentLinesCreatedBySuspended2 | — |
| SUSPENDED | FiscalDocumentLinesLastUpdatSuspended3 | — |
| USER_DATA_CHECKSUM | FiscDocHdrExtnCreatedByUserUserDataChecksum8 | — |
| USER_DATA_CHECKSUM | FiscDocHdrExtnLastUpdtUserUserDataChecksum9 | — |
| USER_DATA_CHECKSUM | FiscDocTaxLineCreatedByUserPUserDataChecksum6 | — |
| USER_DATA_CHECKSUM | FiscDocTaxLineLastUpdtUserPUserDataChecksum7 | — |
| USER_DATA_CHECKSUM | FiscalDocHeaderCreatedByUserUserDataChecksum | — |
| USER_DATA_CHECKSUM | FiscalDocHeaderLastUpdatedByUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FiscalDocSchedulesCreatedByUUserDataChecksum5 | — |
| USER_DATA_CHECKSUM | FiscalDocSchedulesLastUpdtUsUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | FiscalDocumentLinesCreatedByUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FiscalDocumentLinesLastUpdatUserDataChecksum3 | — |
| USER_DISTINGUISHED_NAME | FiscDocHdrExtnCreatedByUserUserDistinguishedName8 | — |
| USER_DISTINGUISHED_NAME | FiscDocHdrExtnLastUpdtUserUserDistinguishedName9 | — |
| USER_DISTINGUISHED_NAME | FiscDocTaxLineCreatedByUserPUserDistinguishedName6 | — |
| USER_DISTINGUISHED_NAME | FiscDocTaxLineLastUpdtUserPUserDistinguishedName7 | — |
| USER_DISTINGUISHED_NAME | FiscalDocHeaderCreatedByUserUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FiscalDocHeaderLastUpdatedByUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FiscalDocSchedulesCreatedByUUserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | FiscalDocSchedulesLastUpdtUsUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | FiscalDocumentLinesCreatedByUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FiscalDocumentLinesLastUpdatUserDistinguishedName3 | — |
| USER_GUID | FiscDocHdrExtnCreatedByUserUserGuid8 | — |
| USER_GUID | FiscDocHdrExtnLastUpdtUserUserGuid9 | — |
| USER_GUID | FiscDocTaxLineCreatedByUserPUserGuid6 | — |
| USER_GUID | FiscDocTaxLineLastUpdtUserPUserGuid7 | — |
| USER_GUID | FiscalDocHeaderCreatedByUserUserGuid | — |
| USER_GUID | FiscalDocHeaderLastUpdatedByUserGuid1 | — |
| USER_GUID | FiscalDocSchedulesCreatedByUUserGuid5 | — |
| USER_GUID | FiscalDocSchedulesLastUpdtUsUserGuid4 | — |
| USER_GUID | FiscalDocumentLinesCreatedByUserGuid2 | — |
| USER_GUID | FiscalDocumentLinesLastUpdatUserGuid3 | — |
| USER_ID | FiscDocHdrExtnCreatedByUserUserId8 | — |
| USER_ID | FiscDocHdrExtnLastUpdtUserUserId9 | — |
| USER_ID | FiscDocTaxLineCreatedByUserPUserId6 | — |
| USER_ID | FiscDocTaxLineLastUpdtUserPUserId7 | — |
| USER_ID | FiscalDocHeaderCreatedByUserUserId | — |
| USER_ID | FiscalDocHeaderLastUpdatedByUserId1 | — |
| USER_ID | FiscalDocSchedulesCreatedByUUserId5 | — |
| USER_ID | FiscalDocSchedulesLastUpdtUsUserId4 | — |
| USER_ID | FiscalDocumentLinesCreatedByUserId2 | — |
| USER_ID | FiscalDocumentLinesLastUpdatUserId3 | — |
| USERNAME | FiscDocHdrExtnCreatedByUserUsername8 | — |
| USERNAME | FiscDocHdrExtnLastUpdtUserUsername9 | — |
| USERNAME | FiscDocTaxLineCreatedByUserPUsername6 | — |
| USERNAME | FiscDocTaxLineLastUpdtUserPUsername7 | — |
| USERNAME | FiscalDocHeaderCreatedByUserUsername | — |
| USERNAME | FiscalDocHeaderLastUpdatedByUsername1 | — |
| USERNAME | FiscalDocSchedulesCreatedByUUsername5 | — |
| USERNAME | FiscalDocSchedulesLastUpdtUsUsername4 | — |
| USERNAME | FiscalDocumentLinesCreatedByUsername2 | — |
| USERNAME | FiscalDocumentLinesLastUpdatUsername3 | — |

### [[fmvlinespvo|FmvLinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |

### [[fmvprofilepvo|FMVProfilePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[frmuserpvo|FRMUserPVO]] (OTHER · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FRMUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | FRMUserPEOBusinessGroupId | — |
| CREATED_BY | FRMUserPEOCreatedBy | — |
| CREATION_DATE | FRMUserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | FRMUserPEOCredentialsEmailSent | — |
| END_DATE | FRMUserPEOEndDate | — |
| HR_TERMINATED | FRMUserPEOHrTerminated | — |
| LAST_UPDATE_DATE | FRMUserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FRMUserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | FRMUserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | FRMUserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | FRMUserPEOObjectVersionNumber | — |
| PARTY_ID | FRMUserPEOPartyId | — |
| PERSON_ID | FRMUserPEOPersonId | — |
| START_DATE | FRMUserPEOStartDate | — |
| SUSPENDED | FRMUserPEOSuspended | — |
| USER_DATA_CHECKSUM | FRMUserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | FRMUserPEOUserDistinguishedName | — |
| USER_GUID | FRMUserPEOUserGuid | ✅ |
| USER_ID | FRMUserPEOUserId | ✅ |
| USERNAME | FRMUserPEOUsername | ✅ |

### [[globalconditionspvo|GlobalConditionsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | GCCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | GCUpdatedByObjectVerNumber | — |
| PERSON_ID | GCCreatedByPersonId | — |
| PERSON_ID | GCUpdatedByPersonId | — |
| USER_GUID | GCCreatedByUserGuid | — |
| USER_GUID | GCUpdatedByUserGuid | — |
| USER_ID | GCCreatedByUserId | — |
| USER_ID | GCUpdatedByUserId | — |
| USERNAME | GCCreatedByUsername | — |
| USERNAME | GCUpdatedByUsername | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 42/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | SupervisorUserPEOActiveFlag | ✅ |
| ACTIVE_FLAG | UserPEOActiveFlag | ✅ |
| BUSINESS_GROUP_ID | SupervisorUserPEOBusinessGroupId | ✅ |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | ✅ |
| CREATED_BY | SupervisorUserPEOCreatedBy | ✅ |
| CREATED_BY | UserPEOCreatedBy | ✅ |
| CREATION_DATE | SupervisorUserPEOCreationDate | ✅ |
| CREATION_DATE | UserPEOCreationDate | ✅ |
| CREDENTIALS_EMAIL_SENT | SupervisorUserPEOCredentialsEmailSent | ✅ |
| CREDENTIALS_EMAIL_SENT | UserPEOCredentialsEmailSent | ✅ |
| END_DATE | SupervisorUserPEOEndDate | ✅ |
| END_DATE | UserPEOEndDate | ✅ |
| HR_TERMINATED | SupervisorUserPEOHrTerminated | ✅ |
| HR_TERMINATED | UserPEOHrTerminated | ✅ |
| LAST_UPDATE_DATE | SupervisorUserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupervisorUserPEOLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SupervisorUserPEOLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | SupervisorUserPEOMultitenancyUsername | ✅ |
| MULTITENANCY_USERNAME | UserPEOMultitenancyUsername | ✅ |
| OBJECT_VERSION_NUMBER | SupervisorUserPEOObjectVersionNumber | ✅ |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | ✅ |
| PARTY_ID | SupervisorUserPEOPartyId | ✅ |
| PARTY_ID | UserPEOPartyId | ✅ |
| PERSON_ID | SupervisorUserPEOPersonId | ✅ |
| PERSON_ID | UserPEOPersonId | ✅ |
| START_DATE | SupervisorUserPEOStartDate | ✅ |
| START_DATE | UserPEOStartDate | ✅ |
| SUSPENDED | SupervisorUserPEOSuspended | ✅ |
| SUSPENDED | UserPEOSuspended | ✅ |
| USER_DATA_CHECKSUM | SupervisorUserPEOUserDataChecksum | ✅ |
| USER_DATA_CHECKSUM | UserPEOUserDataChecksum | ✅ |
| USER_DISTINGUISHED_NAME | SupervisorUserPEOUserDistinguishedName | ✅ |
| USER_DISTINGUISHED_NAME | UserPEOUserDistinguishedName | ✅ |
| USER_GUID | SupervisorUserPEOUserGuid | ✅ |
| USER_GUID | UserPEOUserGuid | ✅ |
| USER_ID | SupervisorUserPEOUserId | ✅ |
| USER_ID | UserPEOUserId | ✅ |
| USERNAME | SupervisorUserPEOUsername | ✅ |
| USERNAME | UserPEOUsername | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 6/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | SupervisorUserPEOActiveFlag | — |
| ACTIVE_FLAG | UserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | SupervisorUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | — |
| CREATED_BY | SupervisorUserPEOCreatedBy | — |
| CREATED_BY | UserPEOCreatedBy | — |
| CREATION_DATE | SupervisorUserPEOCreationDate | — |
| CREATION_DATE | UserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | SupervisorUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | UserPEOCredentialsEmailSent | — |
| END_DATE | SupervisorUserPEOEndDate | — |
| END_DATE | UserPEOEndDate | — |
| HR_TERMINATED | SupervisorUserPEOHrTerminated | — |
| HR_TERMINATED | UserPEOHrTerminated | ✅ |
| LAST_UPDATE_DATE | SupervisorUserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupervisorUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SupervisorUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | SupervisorUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | UserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | SupervisorUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PARTY_ID | SupervisorUserPEOPartyId | — |
| PARTY_ID | UserPEOPartyId | — |
| PERSON_ID | SupervisorUserPEOPersonId | — |
| PERSON_ID | UserPEOPersonId | — |
| START_DATE | SupervisorUserPEOStartDate | — |
| START_DATE | UserPEOStartDate | — |
| SUSPENDED | SupervisorUserPEOSuspended | — |
| SUSPENDED | UserPEOSuspended | ✅ |
| USER_DATA_CHECKSUM | SupervisorUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | UserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | SupervisorUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | UserPEOUserDistinguishedName | — |
| USER_GUID | SupervisorUserPEOUserGuid | — |
| USER_GUID | UserPEOUserGuid | — |
| USER_ID | SupervisorUserPEOUserId | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | SupervisorUserPEOUsername | ✅ |
| USERNAME | UserPEOUsername | ✅ |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[holdinstance|HoldInstance]] (OTHER · BICC: 3/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ApplyUserActiveFlag | — |
| ACTIVE_FLAG | ReleaseUserActiveFlag | — |
| BUSINESS_GROUP_ID | ApplyUserBusinessGroupId | — |
| BUSINESS_GROUP_ID | ReleaseUserBusinessGroupId | — |
| END_DATE | ApplyUserEndDate | ✅ |
| END_DATE | ReleaseUserEndDate | — |
| HR_TERMINATED | ApplyUserHrTerminated | — |
| HR_TERMINATED | ReleaseUserHrTerminated | — |
| OBJECT_VERSION_NUMBER | ApplyUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReleaseUserObjectVersionNumber | — |
| PARTY_ID | ApplyUserPartyId | — |
| PARTY_ID | ReleaseUserPartyId | — |
| PERSON_ID | ApplyUserPersonId | — |
| PERSON_ID | ReleaseUserPersonId | — |
| START_DATE | ApplyUserStartDate | — |
| START_DATE | ReleaseUserStartDate | — |
| SUSPENDED | ApplyUserSuspended | — |
| SUSPENDED | ReleaseUserSuspended | — |
| USER_GUID | ApplyUserUserGuid | — |
| USER_GUID | ReleaseUserUserGuid | — |
| USER_ID | ApplyUserUserId | — |
| USER_ID | ReleaseUserUserId | — |
| USERNAME | ApplyUserUsername | ✅ |
| USERNAME | ReleaseUserUsername | ✅ |

### [[ideacustomerassignmentpvo|IdeaCustomerAssignmentPVO]] (OTHER · BICC: 21/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserActiveFlag | ✅ |
| BUSINESS_GROUP_ID | UserBusinessGroupId | ✅ |
| CREATED_BY | UserCreatedBy | ✅ |
| CREATION_DATE | UserCreationDate | ✅ |
| CREDENTIALS_EMAIL_SENT | UserCredentialsEmailSent | ✅ |
| END_DATE | UserEndDate | ✅ |
| EXTERNAL_ID | UserExternalId | — |
| HR_TERMINATED | UserHrTerminated | ✅ |
| LAST_UPDATE_DATE | UserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | UserLastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | UserMultitenancyUsername | ✅ |
| OBJECT_VERSION_NUMBER | UserObjectVersionNumber | ✅ |
| PARTY_ID | UserPartyId | ✅ |
| PERSON_ID | UserPersonId | ✅ |
| START_DATE | UserStartDate | ✅ |
| SUSPENDED | UserSuspended | ✅ |
| USER_DATA_CHECKSUM | UserUserDataChecksum | ✅ |
| USER_DISTINGUISHED_NAME | UserUserDistinguishedName | ✅ |
| USER_GUID | UserUserGuid | ✅ |
| USER_ID | UserUserId | ✅ |
| USERNAME | UserUsername | ✅ |

### [[idearelationshippvo|IdeaRelationshipPVO]] (HCM · BICC: 21/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserActiveFlag | ✅ |
| BUSINESS_GROUP_ID | UserBusinessGroupId | ✅ |
| CREATED_BY | UserCreatedBy | ✅ |
| CREATION_DATE | UserCreationDate1 | ✅ |
| CREDENTIALS_EMAIL_SENT | UserCredentialsEmailSent | ✅ |
| END_DATE | UserEndDate | ✅ |
| EXTERNAL_ID | UserExternalId | — |
| HR_TERMINATED | UserHrTerminated | ✅ |
| LAST_UPDATE_DATE | UserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | UserLastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | UserMultitenancyUsername | ✅ |
| OBJECT_VERSION_NUMBER | UserObjectVersionNumber | ✅ |
| PARTY_ID | UserPartyId | ✅ |
| PERSON_ID | UserPersonId | ✅ |
| START_DATE | UserStartDate | ✅ |
| SUSPENDED | UserSuspended | ✅ |
| USER_DATA_CHECKSUM | UserUserDataChecksum | ✅ |
| USER_DISTINGUISHED_NAME | UserUserDistinguishedName | ✅ |
| USER_GUID | UserUserGuid | ✅ |
| USER_ID | UserUserId | ✅ |
| USERNAME | UserUsername | ✅ |

### [[ideaspvo|IdeasPVO]] (OTHER · BICC: 20/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserActiveFlag | ✅ |
| BUSINESS_GROUP_ID | UserBusinessGroupId | ✅ |
| CREATED_BY | UserCreatedBy | ✅ |
| CREATION_DATE | UserCreationDate | ✅ |
| CREDENTIALS_EMAIL_SENT | UserCredentialsEmailSent | ✅ |
| END_DATE | UserEndDate | ✅ |
| EXTERNAL_ID | UserExternalId | — |
| HR_TERMINATED | UserHrTerminated | ✅ |
| LAST_UPDATE_DATE | UserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | UserLastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | UserMultitenancyUsername | ✅ |
| OBJECT_VERSION_NUMBER | UserObjectVersionNumber | ✅ |
| PARTY_ID | UserPartyId | ✅ |
| PERSON_ID | UserPersonId | ✅ |
| START_DATE | UserStartDate | ✅ |
| SUSPENDED | UserSuspended | ✅ |
| USER_DATA_CHECKSUM | UserUserDataChecksum | ✅ |
| USER_GUID | UserUserGuid | ✅ |
| USER_ID | UserUserId | ✅ |
| USERNAME | UserUsername | ✅ |

### [[implperfobligtlinespvo|ImplPerfObligTlinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[incidentaccessresultdetailspvo|IncidentAccessResultDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | IncCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IncUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | InvestUpdatedByObjectVerNumber | — |
| PERSON_ID | IncCreatedByPersonId | — |
| PERSON_ID | IncUpdatedByPersonId | — |
| PERSON_ID | InvestUpdatedByPersonId | — |
| USER_GUID | IncCreatedByUserGuid | — |
| USER_GUID | IncUpdatedByUserGuid | — |
| USER_GUID | InvestUpdatedByUserGuid | — |
| USER_ID | IncCreatedByUserId | — |
| USER_ID | IncUpdatedByUserId | — |
| USER_ID | InvestUpdatedByUserId | — |
| USERNAME | IncCreatedByUsername | — |
| USERNAME | IncUpdatedByUsername | — |
| USERNAME | InvestUpdatedByUsername | — |

### [[incidentcommentpvo|IncidentCommentPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmntCreatedByObjectVerNumber | — |
| PERSON_ID | CmntCreatedByPersonId | — |
| USER_GUID | CmntCreatedByUserGuid | — |
| USER_ID | CmntCreatedByUserId | — |
| USERNAME | CmntCreatedByUsername | — |

### [[incidenttransactionresultdetailspvo|IncidentTransactionResultDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | IncCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IncUpdatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | InvestUpdatedByObjectVerNumber | — |
| PERSON_ID | IncCreatedByPersonId | — |
| PERSON_ID | IncUpdatedByPersonId | — |
| PERSON_ID | InvestUpdatedByPersonId | — |
| USER_GUID | IncCreatedByUserGuid | — |
| USER_GUID | IncUpdatedByUserGuid | — |
| USER_GUID | InvestUpdatedByUserGuid | — |
| USER_ID | IncCreatedByUserId | — |
| USER_ID | IncUpdatedByUserId | — |
| USER_ID | InvestUpdatedByUserId | — |
| USERNAME | IncCreatedByUsername | — |
| USERNAME | IncUpdatedByUsername | — |
| USERNAME | InvestUpdatedByUsername | — |

### [[interfacefiscaldocumentp1|InterfaceFiscalDocumentP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FDHeaderIntrEOCreatedByUserPActiveFlag | — |
| ACTIVE_FLAG | FDHeaderIntrLastUpdtdByUserPActiveFlag1 | — |
| ACTIVE_FLAG | FDLineIntrEOToCreatedByUserPActiveFlag2 | — |
| ACTIVE_FLAG | FDLineIntrToLastUpdtdByUserPActiveFlag3 | — |
| ACTIVE_FLAG | IntHdrsCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | IntHdrsLUpdtdByUserPEOActiveFlag1 | — |
| ACTIVE_FLAG | IntLegalProcCreatedByUserPEOActiveFlag4 | — |
| ACTIVE_FLAG | IntLegalProcLUpdtdByUserPEOActiveFlag5 | — |
| ACTIVE_FLAG | IntLinesCreatedByUserPEOActiveFlag2 | — |
| ACTIVE_FLAG | IntLinesLUpdtdByUserPEOActiveFlag3 | — |
| ACTIVE_FLAG | IntRefCreatedByUserPEOActiveFlag6 | — |
| ACTIVE_FLAG | IntRefLUpdtdByUserPEOActiveFlag7 | — |
| ACTIVE_FLAG | TaxLineIntrEOCreatedByUserPEActiveFlag | — |
| ACTIVE_FLAG | TaxLineIntrEOLastUpdtdByUserActiveFlag1 | — |
| BUSINESS_GROUP_ID | FDHeaderIntrEOCreatedByUserPBusinessGroupId | — |
| BUSINESS_GROUP_ID | FDHeaderIntrLastUpdtdByUserPBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | FDLineIntrEOToCreatedByUserPBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | FDLineIntrToLastUpdtdByUserPBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | IntHdrsCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | IntHdrsLUpdtdByUserPEOBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | IntLegalProcCreatedByUserPEOBusinessGroupId4 | — |
| BUSINESS_GROUP_ID | IntLegalProcLUpdtdByUserPEOBusinessGroupId5 | — |
| BUSINESS_GROUP_ID | IntLinesCreatedByUserPEOBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | IntLinesLUpdtdByUserPEOBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | IntRefCreatedByUserPEOBusinessGroupId6 | — |
| BUSINESS_GROUP_ID | IntRefLUpdtdByUserPEOBusinessGroupId7 | — |
| BUSINESS_GROUP_ID | TaxLineIntrEOCreatedByUserPEBusinessGroupId | — |
| BUSINESS_GROUP_ID | TaxLineIntrEOLastUpdtdByUserBusinessGroupId1 | — |
| CREATED_BY | FDHeaderIntrEOCreatedByUserPCreatedBy | — |
| CREATED_BY | FDHeaderIntrLastUpdtdByUserPCreatedBy1 | — |
| CREATED_BY | FDLineIntrEOToCreatedByUserPCreatedBy2 | — |
| CREATED_BY | FDLineIntrToLastUpdtdByUserPCreatedBy3 | — |
| CREATED_BY | IntHdrsCreatedByUserPEOCreatedBy | — |
| CREATED_BY | IntHdrsLUpdtdByUserPEOCreatedBy1 | — |
| CREATED_BY | IntLegalProcCreatedByUserPEOCreatedBy4 | — |
| CREATED_BY | IntLegalProcLUpdtdByUserPEOCreatedBy5 | — |
| CREATED_BY | IntLinesCreatedByUserPEOCreatedBy2 | — |
| CREATED_BY | IntLinesLUpdtdByUserPEOCreatedBy3 | — |
| CREATED_BY | IntRefCreatedByUserPEOCreatedBy6 | — |
| CREATED_BY | IntRefLUpdtdByUserPEOCreatedBy7 | — |
| CREATED_BY | TaxLineIntrEOCreatedByUserPECreatedBy | — |
| CREATED_BY | TaxLineIntrEOLastUpdtdByUserCreatedBy1 | — |
| CREATION_DATE | FDHeaderIntrEOCreatedByUserPCreationDate | — |
| CREATION_DATE | FDHeaderIntrLastUpdtdByUserPCreationDate1 | — |
| CREATION_DATE | FDLineIntrEOToCreatedByUserPCreationDate2 | — |
| CREATION_DATE | FDLineIntrToLastUpdtdByUserPCreationDate3 | — |
| CREATION_DATE | IntHdrsCreatedByUserPEOCreationDate | — |
| CREATION_DATE | IntHdrsLUpdtdByUserPEOCreationDate1 | — |
| CREATION_DATE | IntLegalProcCreatedByUserPEOCreationDate4 | — |
| CREATION_DATE | IntLegalProcLUpdtdByUserPEOCreationDate5 | — |
| CREATION_DATE | IntLinesCreatedByUserPEOCreationDate2 | — |
| CREATION_DATE | IntLinesLUpdtdByUserPEOCreationDate3 | — |
| CREATION_DATE | IntRefCreatedByUserPEOCreationDate6 | — |
| CREATION_DATE | IntRefLUpdtdByUserPEOCreationDate7 | — |
| CREATION_DATE | TaxLineIntrEOCreatedByUserPECreationDate | — |
| CREATION_DATE | TaxLineIntrEOLastUpdtdByUserCreationDate1 | — |
| CREDENTIALS_EMAIL_SENT | FDHeaderIntrEOCreatedByUserPCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | FDHeaderIntrLastUpdtdByUserPCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | FDLineIntrEOToCreatedByUserPCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FDLineIntrToLastUpdtdByUserPCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | IntHdrsCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | IntHdrsLUpdtdByUserPEOCredentialsEmailSent1 | — |
| CREDENTIALS_EMAIL_SENT | IntLegalProcCreatedByUserPEOCredentialsEmailSent4 | — |
| CREDENTIALS_EMAIL_SENT | IntLegalProcLUpdtdByUserPEOCredentialsEmailSent5 | — |
| CREDENTIALS_EMAIL_SENT | IntLinesCreatedByUserPEOCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | IntLinesLUpdtdByUserPEOCredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | IntRefCreatedByUserPEOCredentialsEmailSent6 | — |
| CREDENTIALS_EMAIL_SENT | IntRefLUpdtdByUserPEOCredentialsEmailSent7 | — |
| CREDENTIALS_EMAIL_SENT | TaxLineIntrEOCreatedByUserPECredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | TaxLineIntrEOLastUpdtdByUserCredentialsEmailSent1 | — |
| END_DATE | FDHeaderIntrEOCreatedByUserPEndDate | — |
| END_DATE | FDHeaderIntrLastUpdtdByUserPEndDate1 | — |
| END_DATE | FDLineIntrEOToCreatedByUserPEndDate2 | — |
| END_DATE | FDLineIntrToLastUpdtdByUserPEndDate3 | — |
| END_DATE | IntHdrsCreatedByUserPEOEndDate | — |
| END_DATE | IntHdrsLUpdtdByUserPEOEndDate1 | — |
| END_DATE | IntLegalProcCreatedByUserPEOEndDate4 | — |
| END_DATE | IntLegalProcLUpdtdByUserPEOEndDate5 | — |
| END_DATE | IntLinesCreatedByUserPEOEndDate2 | — |
| END_DATE | IntLinesLUpdtdByUserPEOEndDate3 | — |
| END_DATE | IntRefCreatedByUserPEOEndDate6 | — |
| END_DATE | IntRefLUpdtdByUserPEOEndDate7 | — |
| END_DATE | TaxLineIntrEOCreatedByUserPEEndDate | — |
| END_DATE | TaxLineIntrEOLastUpdtdByUserEndDate1 | — |
| EXTERNAL_ID | FDHeaderIntrEOCreatedByUserPExternalId | — |
| EXTERNAL_ID | FDHeaderIntrLastUpdtdByUserPExternalId1 | — |
| EXTERNAL_ID | FDLineIntrEOToCreatedByUserPExternalId2 | — |
| EXTERNAL_ID | FDLineIntrToLastUpdtdByUserPExternalId3 | — |
| EXTERNAL_ID | IntHdrsCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | IntHdrsLUpdtdByUserPEOExternalId1 | — |
| EXTERNAL_ID | IntLegalProcCreatedByUserPEOExternalId4 | — |
| EXTERNAL_ID | IntLegalProcLUpdtdByUserPEOExternalId5 | — |
| EXTERNAL_ID | IntLinesCreatedByUserPEOExternalId2 | — |
| EXTERNAL_ID | IntLinesLUpdtdByUserPEOExternalId3 | — |
| EXTERNAL_ID | IntRefCreatedByUserPEOExternalId6 | — |
| EXTERNAL_ID | IntRefLUpdtdByUserPEOExternalId7 | — |
| EXTERNAL_ID | TaxLineIntrEOCreatedByUserPEExternalId | — |
| EXTERNAL_ID | TaxLineIntrEOLastUpdtdByUserExternalId1 | — |
| HR_TERMINATED | FDHeaderIntrEOCreatedByUserPHrTerminated | — |
| HR_TERMINATED | FDHeaderIntrLastUpdtdByUserPHrTerminated1 | — |
| HR_TERMINATED | FDLineIntrEOToCreatedByUserPHrTerminated2 | — |
| HR_TERMINATED | FDLineIntrToLastUpdtdByUserPHrTerminated3 | — |
| HR_TERMINATED | IntHdrsCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | IntHdrsLUpdtdByUserPEOHrTerminated1 | — |
| HR_TERMINATED | IntLegalProcCreatedByUserPEOHrTerminated4 | — |
| HR_TERMINATED | IntLegalProcLUpdtdByUserPEOHrTerminated5 | — |
| HR_TERMINATED | IntLinesCreatedByUserPEOHrTerminated2 | — |
| HR_TERMINATED | IntLinesLUpdtdByUserPEOHrTerminated3 | — |
| HR_TERMINATED | IntRefCreatedByUserPEOHrTerminated6 | — |
| HR_TERMINATED | IntRefLUpdtdByUserPEOHrTerminated7 | — |
| HR_TERMINATED | TaxLineIntrEOCreatedByUserPEHrTerminated | — |
| HR_TERMINATED | TaxLineIntrEOLastUpdtdByUserHrTerminated1 | — |
| LAST_UPDATE_DATE | FDHeaderIntrEOCreatedByUserPLastUpdateDate | — |
| LAST_UPDATE_DATE | FDHeaderIntrLastUpdtdByUserPLastUpdateDate1 | — |
| LAST_UPDATE_DATE | FDLineIntrEOToCreatedByUserPLastUpdateDate2 | — |
| LAST_UPDATE_DATE | FDLineIntrToLastUpdtdByUserPLastUpdateDate3 | — |
| LAST_UPDATE_DATE | IntHdrsCreatedByUserPEOLastUpdateDate | — |
| LAST_UPDATE_DATE | IntHdrsLUpdtdByUserPEOLastUpdateDate1 | — |
| LAST_UPDATE_DATE | IntLegalProcCreatedByUserPEOLastUpdateDate4 | — |
| LAST_UPDATE_DATE | IntLegalProcLUpdtdByUserPEOLastUpdateDate5 | — |
| LAST_UPDATE_DATE | IntLinesCreatedByUserPEOLastUpdateDate2 | — |
| LAST_UPDATE_DATE | IntLinesLUpdtdByUserPEOLastUpdateDate3 | — |
| LAST_UPDATE_DATE | IntRefCreatedByUserPEOLastUpdateDate6 | — |
| LAST_UPDATE_DATE | IntRefLUpdtdByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | TaxLineIntrEOCreatedByUserPELastUpdateDate | — |
| LAST_UPDATE_DATE | TaxLineIntrEOLastUpdtdByUserLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | FDHeaderIntrEOCreatedByUserPLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FDHeaderIntrLastUpdtdByUserPLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | FDLineIntrEOToCreatedByUserPLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | FDLineIntrToLastUpdtdByUserPLastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | IntHdrsCreatedByUserPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | IntHdrsLUpdtdByUserPEOLastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | IntLegalProcCreatedByUserPEOLastUpdateLogin4 | — |
| LAST_UPDATE_LOGIN | IntLegalProcLUpdtdByUserPEOLastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | IntLinesCreatedByUserPEOLastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | IntLinesLUpdtdByUserPEOLastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | IntRefCreatedByUserPEOLastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | IntRefLUpdtdByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | TaxLineIntrEOCreatedByUserPELastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TaxLineIntrEOLastUpdtdByUserLastUpdateLogin1 | — |
| LAST_UPDATED_BY | FDHeaderIntrEOCreatedByUserPLastUpdatedBy | — |
| LAST_UPDATED_BY | FDHeaderIntrLastUpdtdByUserPLastUpdatedBy1 | — |
| LAST_UPDATED_BY | FDLineIntrEOToCreatedByUserPLastUpdatedBy2 | — |
| LAST_UPDATED_BY | FDLineIntrToLastUpdtdByUserPLastUpdatedBy3 | — |
| LAST_UPDATED_BY | IntHdrsCreatedByUserPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | IntHdrsLUpdtdByUserPEOLastUpdatedBy1 | — |
| LAST_UPDATED_BY | IntLegalProcCreatedByUserPEOLastUpdatedBy4 | — |
| LAST_UPDATED_BY | IntLegalProcLUpdtdByUserPEOLastUpdatedBy5 | — |
| LAST_UPDATED_BY | IntLinesCreatedByUserPEOLastUpdatedBy2 | — |
| LAST_UPDATED_BY | IntLinesLUpdtdByUserPEOLastUpdatedBy3 | — |
| LAST_UPDATED_BY | IntRefCreatedByUserPEOLastUpdatedBy6 | — |
| LAST_UPDATED_BY | IntRefLUpdtdByUserPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | TaxLineIntrEOCreatedByUserPELastUpdatedBy | — |
| LAST_UPDATED_BY | TaxLineIntrEOLastUpdtdByUserLastUpdatedBy1 | — |
| MULTITENANCY_USERNAME | FDHeaderIntrEOCreatedByUserPMultitenancyUsername | — |
| MULTITENANCY_USERNAME | FDHeaderIntrLastUpdtdByUserPMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | FDLineIntrEOToCreatedByUserPMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FDLineIntrToLastUpdtdByUserPMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | IntHdrsCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | IntHdrsLUpdtdByUserPEOMultitenancyUsername1 | — |
| MULTITENANCY_USERNAME | IntLegalProcCreatedByUserPEOMultitenancyUsername4 | — |
| MULTITENANCY_USERNAME | IntLegalProcLUpdtdByUserPEOMultitenancyUsername5 | — |
| MULTITENANCY_USERNAME | IntLinesCreatedByUserPEOMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | IntLinesLUpdtdByUserPEOMultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | IntRefCreatedByUserPEOMultitenancyUsername6 | — |
| MULTITENANCY_USERNAME | IntRefLUpdtdByUserPEOMultitenancyUsername7 | — |
| MULTITENANCY_USERNAME | TaxLineIntrEOCreatedByUserPEMultitenancyUsername | — |
| MULTITENANCY_USERNAME | TaxLineIntrEOLastUpdtdByUserMultitenancyUsername1 | — |
| OBJECT_VERSION_NUMBER | FDHeaderIntrEOCreatedByUserPObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FDHeaderIntrLastUpdtdByUserPObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | FDLineIntrEOToCreatedByUserPObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | FDLineIntrToLastUpdtdByUserPObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | IntHdrsCreatedByUserPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | IntHdrsLUpdtdByUserPEOObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | IntLegalProcCreatedByUserPEOObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | IntLegalProcLUpdtdByUserPEOObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | IntLinesCreatedByUserPEOObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | IntLinesLUpdtdByUserPEOObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | IntRefCreatedByUserPEOObjectVersionNumber6 | — |
| OBJECT_VERSION_NUMBER | IntRefLUpdtdByUserPEOObjectVersionNumber7 | — |
| OBJECT_VERSION_NUMBER | TaxLineIntrEOCreatedByUserPEObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TaxLineIntrEOLastUpdtdByUserObjectVersionNumber1 | — |
| PARTY_ID | FDHeaderIntrEOCreatedByUserPPartyId | — |
| PARTY_ID | FDHeaderIntrLastUpdtdByUserPPartyId1 | — |
| PARTY_ID | FDLineIntrEOToCreatedByUserPPartyId2 | — |
| PARTY_ID | FDLineIntrToLastUpdtdByUserPPartyId3 | — |
| PARTY_ID | IntHdrsCreatedByUserPEOPartyId | — |
| PARTY_ID | IntHdrsLUpdtdByUserPEOPartyId1 | — |
| PARTY_ID | IntLegalProcCreatedByUserPEOPartyId4 | — |
| PARTY_ID | IntLegalProcLUpdtdByUserPEOPartyId5 | — |
| PARTY_ID | IntLinesCreatedByUserPEOPartyId2 | — |
| PARTY_ID | IntLinesLUpdtdByUserPEOPartyId3 | — |
| PARTY_ID | IntRefCreatedByUserPEOPartyId6 | — |
| PARTY_ID | IntRefLUpdtdByUserPEOPartyId7 | — |
| PARTY_ID | TaxLineIntrEOCreatedByUserPEPartyId | — |
| PARTY_ID | TaxLineIntrEOLastUpdtdByUserPartyId1 | — |
| PERSON_ID | FDHeaderIntrEOCreatedByUserPPersonId | — |
| PERSON_ID | FDHeaderIntrLastUpdtdByUserPPersonId1 | — |
| PERSON_ID | FDLineIntrEOToCreatedByUserPPersonId2 | — |
| PERSON_ID | FDLineIntrToLastUpdtdByUserPPersonId3 | — |
| PERSON_ID | IntHdrsCreatedByUserPEOPersonId | — |
| PERSON_ID | IntHdrsLUpdtdByUserPEOPersonId1 | — |
| PERSON_ID | IntLegalProcCreatedByUserPEOPersonId4 | — |
| PERSON_ID | IntLegalProcLUpdtdByUserPEOPersonId5 | — |
| PERSON_ID | IntLinesCreatedByUserPEOPersonId2 | — |
| PERSON_ID | IntLinesLUpdtdByUserPEOPersonId3 | — |
| PERSON_ID | IntRefCreatedByUserPEOPersonId6 | — |
| PERSON_ID | IntRefLUpdtdByUserPEOPersonId7 | — |
| PERSON_ID | TaxLineIntrEOCreatedByUserPEPersonId | — |
| PERSON_ID | TaxLineIntrEOLastUpdtdByUserPersonId1 | — |
| START_DATE | FDHeaderIntrEOCreatedByUserPStartDate | — |
| START_DATE | FDHeaderIntrLastUpdtdByUserPStartDate1 | — |
| START_DATE | FDLineIntrEOToCreatedByUserPStartDate2 | — |
| START_DATE | FDLineIntrToLastUpdtdByUserPStartDate3 | — |
| START_DATE | IntHdrsCreatedByUserPEOStartDate | — |
| START_DATE | IntHdrsLUpdtdByUserPEOStartDate1 | — |
| START_DATE | IntLegalProcCreatedByUserPEOStartDate4 | — |
| START_DATE | IntLegalProcLUpdtdByUserPEOStartDate5 | — |
| START_DATE | IntLinesCreatedByUserPEOStartDate2 | — |
| START_DATE | IntLinesLUpdtdByUserPEOStartDate3 | — |
| START_DATE | IntRefCreatedByUserPEOStartDate6 | — |
| START_DATE | IntRefLUpdtdByUserPEOStartDate7 | — |
| START_DATE | TaxLineIntrEOCreatedByUserPEStartDate | — |
| START_DATE | TaxLineIntrEOLastUpdtdByUserStartDate1 | — |
| SUSPENDED | FDHeaderIntrEOCreatedByUserPSuspended | — |
| SUSPENDED | FDHeaderIntrLastUpdtdByUserPSuspended1 | — |
| SUSPENDED | FDLineIntrEOToCreatedByUserPSuspended2 | — |
| SUSPENDED | FDLineIntrToLastUpdtdByUserPSuspended3 | — |
| SUSPENDED | IntHdrsCreatedByUserPEOSuspended | — |
| SUSPENDED | IntHdrsLUpdtdByUserPEOSuspended1 | — |
| SUSPENDED | IntLegalProcCreatedByUserPEOSuspended4 | — |
| SUSPENDED | IntLegalProcLUpdtdByUserPEOSuspended5 | — |
| SUSPENDED | IntLinesCreatedByUserPEOSuspended2 | — |
| SUSPENDED | IntLinesLUpdtdByUserPEOSuspended3 | — |
| SUSPENDED | IntRefCreatedByUserPEOSuspended6 | — |
| SUSPENDED | IntRefLUpdtdByUserPEOSuspended7 | — |
| SUSPENDED | TaxLineIntrEOCreatedByUserPESuspended | — |
| SUSPENDED | TaxLineIntrEOLastUpdtdByUserSuspended1 | — |
| USER_DATA_CHECKSUM | FDHeaderIntrEOCreatedByUserPUserDataChecksum | — |
| USER_DATA_CHECKSUM | FDHeaderIntrLastUpdtdByUserPUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | FDLineIntrEOToCreatedByUserPUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FDLineIntrToLastUpdtdByUserPUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | IntHdrsCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | IntHdrsLUpdtdByUserPEOUserDataChecksum1 | — |
| USER_DATA_CHECKSUM | IntLegalProcCreatedByUserPEOUserDataChecksum4 | — |
| USER_DATA_CHECKSUM | IntLegalProcLUpdtdByUserPEOUserDataChecksum5 | — |
| USER_DATA_CHECKSUM | IntLinesCreatedByUserPEOUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | IntLinesLUpdtdByUserPEOUserDataChecksum3 | — |
| USER_DATA_CHECKSUM | IntRefCreatedByUserPEOUserDataChecksum6 | — |
| USER_DATA_CHECKSUM | IntRefLUpdtdByUserPEOUserDataChecksum7 | — |
| USER_DATA_CHECKSUM | TaxLineIntrEOCreatedByUserPEUserDataChecksum | — |
| USER_DATA_CHECKSUM | TaxLineIntrEOLastUpdtdByUserUserDataChecksum1 | — |
| USER_DISTINGUISHED_NAME | FDHeaderIntrEOCreatedByUserPUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | FDHeaderIntrLastUpdtdByUserPUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | FDLineIntrEOToCreatedByUserPUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FDLineIntrToLastUpdtdByUserPUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | IntHdrsCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | IntHdrsLUpdtdByUserPEOUserDistinguishedName1 | — |
| USER_DISTINGUISHED_NAME | IntLegalProcCreatedByUserPEOUserDistinguishedName4 | — |
| USER_DISTINGUISHED_NAME | IntLegalProcLUpdtdByUserPEOUserDistinguishedName5 | — |
| USER_DISTINGUISHED_NAME | IntLinesCreatedByUserPEOUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | IntLinesLUpdtdByUserPEOUserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | IntRefCreatedByUserPEOUserDistinguishedName6 | — |
| USER_DISTINGUISHED_NAME | IntRefLUpdtdByUserPEOUserDistinguishedName7 | — |
| USER_DISTINGUISHED_NAME | TaxLineIntrEOCreatedByUserPEUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | TaxLineIntrEOLastUpdtdByUserUserDistinguishedName1 | — |
| USER_GUID | FDHeaderIntrEOCreatedByUserPUserGuid | — |
| USER_GUID | FDHeaderIntrLastUpdtdByUserPUserGuid1 | — |
| USER_GUID | FDLineIntrEOToCreatedByUserPUserGuid2 | — |
| USER_GUID | FDLineIntrToLastUpdtdByUserPUserGuid3 | — |
| USER_GUID | IntHdrsCreatedByUserPEOUserGuid | — |
| USER_GUID | IntHdrsLUpdtdByUserPEOUserGuid1 | — |
| USER_GUID | IntLegalProcCreatedByUserPEOUserGuid4 | — |
| USER_GUID | IntLegalProcLUpdtdByUserPEOUserGuid5 | — |
| USER_GUID | IntLinesCreatedByUserPEOUserGuid2 | — |
| USER_GUID | IntLinesLUpdtdByUserPEOUserGuid3 | — |
| USER_GUID | IntRefCreatedByUserPEOUserGuid6 | — |
| USER_GUID | IntRefLUpdtdByUserPEOUserGuid7 | — |
| USER_GUID | TaxLineIntrEOCreatedByUserPEUserGuid | — |
| USER_GUID | TaxLineIntrEOLastUpdtdByUserUserGuid1 | — |
| USER_ID | FDHeaderIntrEOCreatedByUserPUserId | — |
| USER_ID | FDHeaderIntrLastUpdtdByUserPUserId1 | — |
| USER_ID | FDLineIntrEOToCreatedByUserPUserId2 | — |
| USER_ID | FDLineIntrToLastUpdtdByUserPUserId3 | — |
| USER_ID | IntHdrsCreatedByUserPEOUserId | — |
| USER_ID | IntHdrsLUpdtdByUserPEOUserId1 | — |
| USER_ID | IntLegalProcCreatedByUserPEOUserId4 | — |
| USER_ID | IntLegalProcLUpdtdByUserPEOUserId5 | — |
| USER_ID | IntLinesCreatedByUserPEOUserId2 | — |
| USER_ID | IntLinesLUpdtdByUserPEOUserId3 | — |
| USER_ID | IntRefCreatedByUserPEOUserId6 | — |
| USER_ID | IntRefLUpdtdByUserPEOUserId7 | — |
| USER_ID | TaxLineIntrEOCreatedByUserPEUserId | — |
| USER_ID | TaxLineIntrEOLastUpdtdByUserUserId1 | — |
| USERNAME | FDHeaderIntrEOCreatedByUserPUsername | — |
| USERNAME | FDHeaderIntrLastUpdtdByUserPUsername1 | — |
| USERNAME | FDLineIntrEOToCreatedByUserPUsername2 | — |
| USERNAME | FDLineIntrToLastUpdtdByUserPUsername3 | — |
| USERNAME | IntHdrsCreatedByUserPEOUsername | — |
| USERNAME | IntHdrsLUpdtdByUserPEOUsername1 | — |
| USERNAME | IntLegalProcCreatedByUserPEOUsername4 | — |
| USERNAME | IntLegalProcLUpdtdByUserPEOUsername5 | — |
| USERNAME | IntLinesCreatedByUserPEOUsername2 | — |
| USERNAME | IntLinesLUpdtdByUserPEOUsername3 | — |
| USERNAME | IntRefCreatedByUserPEOUsername6 | — |
| USERNAME | IntRefLUpdtdByUserPEOUsername7 | — |
| USERNAME | TaxLineIntrEOCreatedByUserPEUsername | — |
| USERNAME | TaxLineIntrEOLastUpdtdByUserUsername1 | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserHoldHeldByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserHoldHeldByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserHoldHeldByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserHoldHeldByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserHoldHeldByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserHoldHeldByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserHoldHeldByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserHoldHeldByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserHoldHeldByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserHoldHeldByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserHoldHeldByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserHoldHeldByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserHoldHeldByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserHoldHeldByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserHoldHeldByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserHoldHeldByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserHoldHeldByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserHoldHeldByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserHoldHeldByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserHoldHeldByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | InvUpdateObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PoHeaderInvLineUpdatedByObjectVersionNumber | — |
| PERSON_ID | PoHeaderInvLineUpdatedByPersonId | — |
| USER_GUID | PoHeaderInvLineUpdatedByUserGuid | — |
| USER_ID | InvUpdateUserId | — |
| USER_ID | PoHeaderInvLineUpdatedByUserId | — |
| USERNAME | PoHeaderInvLineUpdatedByUsername | — |

### [[issuepvo|IssuePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | IssueUpdatedByObjectVerNumber | — |
| PERSON_ID | CreatedByPersonId | — |
| PERSON_ID | IssueApprovedByPersonId | — |
| PERSON_ID | IssueCreatedByPersonId | — |
| PERSON_ID | IssueReviewedByPersonId | — |
| PERSON_ID | IssueUpdatedByPersonId | — |
| USER_GUID | CreatedByUserGuid | — |
| USER_GUID | IssueApprovedByUserGuid | — |
| USER_GUID | IssueCreatedByUserGuid | — |
| USER_GUID | IssueReviewedByUserGuid | — |
| USER_GUID | IssueUpdatedByUserGuid | — |
| USER_ID | CreatedByUserId | — |
| USER_ID | IssueApprovedByUserId | — |
| USER_ID | IssueCreatedByUserId | — |
| USER_ID | IssueReviewedByUserId | — |
| USER_ID | IssueUpdatedByUserId | — |
| USERNAME | CreatedByUsername | — |
| USERNAME | IssueApprovedByUsername | — |
| USERNAME | IssueCreatedByUsername | — |
| USERNAME | IssueReviewedByUsername | — |
| USERNAME | IssueUpdatedByUsername | — |

### [[jobposthistorypvo|JobPostHistoryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[jobposthistoryviewallpvo|JobPostHistoryViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[jobpostingpvo|JobPostingPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[jobpostingviewallpvo|JobPostingViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[jobpostresultpvo|JobPostResultPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[jobpostresultviewallpvo|JobPostResultViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[journalbatchpvo|JournalBatchPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedByUserCreatedBy | — |
| CREATED_BY | LastUpdatedByUserCreatedBy | — |
| CREATION_DATE | CreatedByUserCreationDate | — |
| CREATION_DATE | LastUpdatedByUserCreationDate | — |
| LAST_UPDATE_DATE | CreatedByUserLastUpdateDate | — |
| LAST_UPDATE_DATE | LastUpdatedByUserLastUpdateDate | — |
| LAST_UPDATED_BY | CreatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | LastUpdatedByUserLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CreatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByUserObjectVersionNumber | — |
| PERSON_ID | CreatedByUserPersonId | — |
| PERSON_ID | LastUpdatedByUserPersonId | — |
| USER_ID | CreatedByUserUserId | — |
| USER_ID | LastUpdatedByUserUserId | — |
| USERNAME | CreatedByUserUsername | — |
| USERNAME | LastUpdatedByUserUsername | — |

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL · BICC: 2/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserActiveFlag | — |
| ACTIVE_FLAG | LastUpdatedByUserActiveFlag | — |
| BUSINESS_GROUP_ID | CreatedByUserBusinessGroupId | — |
| BUSINESS_GROUP_ID | LastUpdatedByUserBusinessGroupId | — |
| CREATED_BY | BatchCreatedByUserCreatedBy | — |
| CREATED_BY | BatchLastUpdatedByUserCreatedBy | — |
| CREATED_BY | CreatedByUserCreatedBy | — |
| CREATED_BY | LastUpdatedByUserCreatedBy | — |
| CREATION_DATE | BatchCreatedByUserCreationDate | — |
| CREATION_DATE | BatchLastUpdatedByUserCreationDate | — |
| CREATION_DATE | CreatedByUserCreationDate | — |
| CREATION_DATE | LastUpdatedByUserCreationDate | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedByUserCredentialsEmailSent | — |
| END_DATE | CreatedByUserEndDate | — |
| END_DATE | LastUpdatedByUserEndDate | — |
| HR_TERMINATED | CreatedByUserHrTerminated | — |
| HR_TERMINATED | LastUpdatedByUserHrTerminated | — |
| LAST_UPDATE_DATE | BatchCreatedByUserLastUpdateDate | — |
| LAST_UPDATE_DATE | BatchLastUpdatedByUserLastUpdateDate | — |
| LAST_UPDATE_DATE | CreatedByUserLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | LastUpdatedByUserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BatchCreatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BatchLastUpdatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | CreatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | LastUpdatedByUserLastUpdateLogin | — |
| LAST_UPDATED_BY | BatchCreatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | BatchLastUpdatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | CreatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | LastUpdatedByUserLastUpdatedBy | — |
| MULTITENANCY_USERNAME | CreatedByUserMultitenancyUsername | — |
| MULTITENANCY_USERNAME | LastUpdatedByUserMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | BatchCreatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BatchLastUpdatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CreatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByUserObjectVersionNumber | — |
| PARTY_ID | CreatedByUserPartyId | — |
| PARTY_ID | LastUpdatedByUserPartyId | — |
| PERSON_ID | CreatedByUserPersonId | — |
| PERSON_ID | LastUpdatedByUserPersonId | — |
| START_DATE | CreatedByUserStartDate | — |
| START_DATE | LastUpdatedByUserStartDate | — |
| SUSPENDED | CreatedByUserSuspended | — |
| SUSPENDED | LastUpdatedByUserSuspended | — |
| USER_DATA_CHECKSUM | CreatedByUserUserDataChecksum | — |
| USER_DATA_CHECKSUM | LastUpdatedByUserUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | CreatedByUserUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | LastUpdatedByUserUserDistinguishedName | — |
| USER_GUID | CreatedByUserUserGuid | — |
| USER_GUID | LastUpdatedByUserUserGuid | — |
| USER_ID | BatchCreatedByUserUserId | — |
| USER_ID | BatchLastUpdatedByUserUserId | — |
| USER_ID | CreatedByUserUserId | — |
| USER_ID | LastUpdatedByUserUserId | — |
| USERNAME | BatchCreatedByUserUsername | — |
| USERNAME | BatchLastUpdatedByUserUsername | — |
| USERNAME | CreatedByUserUsername | — |
| USERNAME | LastUpdatedByUserUsername | — |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 2/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | CreatedByUserActiveFlag | — |
| ACTIVE_FLAG | LastUpdatedByUserActiveFlag | — |
| BUSINESS_GROUP_ID | CreatedByUserBusinessGroupId | — |
| BUSINESS_GROUP_ID | LastUpdatedByUserBusinessGroupId | — |
| CREATED_BY | BatchCreatedByUserCreatedBy | — |
| CREATED_BY | BatchLastUpdatedByUserCreatedBy | — |
| CREATED_BY | CreatedByUserCreatedBy | — |
| CREATED_BY | LastUpdatedByUserCreatedBy | — |
| CREATION_DATE | BatchCreatedByUserCreationDate | — |
| CREATION_DATE | BatchLastUpdatedByUserCreationDate | — |
| CREATION_DATE | CreatedByUserCreationDate | — |
| CREATION_DATE | LastUpdatedByUserCreationDate | — |
| CREDENTIALS_EMAIL_SENT | CreatedByUserCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | LastUpdatedByUserCredentialsEmailSent | — |
| END_DATE | CreatedByUserEndDate | — |
| END_DATE | LastUpdatedByUserEndDate | — |
| HR_TERMINATED | CreatedByUserHrTerminated | — |
| HR_TERMINATED | LastUpdatedByUserHrTerminated | — |
| LAST_UPDATE_DATE | BatchCreatedByUserLastUpdateDate | — |
| LAST_UPDATE_DATE | BatchLastUpdatedByUserLastUpdateDate | — |
| LAST_UPDATE_DATE | CreatedByUserLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | LastUpdatedByUserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BatchCreatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BatchLastUpdatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | CreatedByUserLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | LastUpdatedByUserLastUpdateLogin | — |
| LAST_UPDATED_BY | BatchCreatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | BatchLastUpdatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | CreatedByUserLastUpdatedBy | — |
| LAST_UPDATED_BY | LastUpdatedByUserLastUpdatedBy | — |
| MULTITENANCY_USERNAME | CreatedByUserMultitenancyUsername | — |
| MULTITENANCY_USERNAME | LastUpdatedByUserMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | BatchCreatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BatchLastUpdatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CreatedByUserObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | LastUpdatedByUserObjectVersionNumber | — |
| PARTY_ID | CreatedByUserPartyId | — |
| PARTY_ID | LastUpdatedByUserPartyId | — |
| PERSON_ID | CreatedByUserPersonId | — |
| PERSON_ID | LastUpdatedByUserPersonId | — |
| START_DATE | CreatedByUserStartDate | — |
| START_DATE | LastUpdatedByUserStartDate | — |
| SUSPENDED | CreatedByUserSuspended | — |
| SUSPENDED | LastUpdatedByUserSuspended | — |
| USER_DATA_CHECKSUM | CreatedByUserUserDataChecksum | — |
| USER_DATA_CHECKSUM | LastUpdatedByUserUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | CreatedByUserUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | LastUpdatedByUserUserDistinguishedName | — |
| USER_GUID | CreatedByUserUserGuid | — |
| USER_GUID | LastUpdatedByUserUserGuid | — |
| USER_ID | BatchCreatedByUserUserId | — |
| USER_ID | BatchLastUpdatedByUserUserId | — |
| USER_ID | CreatedByUserUserId | — |
| USER_ID | LastUpdatedByUserUserId | — |
| USERNAME | BatchCreatedByUserUsername | — |
| USERNAME | BatchLastUpdatedByUserUsername | — |
| USERNAME | CreatedByUserUsername | — |
| USERNAME | LastUpdatedByUserUsername | — |

### [[ledgerpvo|LedgerPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[legaldocumentassocp1|LegalDocumentAssocP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | FdhCreatedByUserPEOActiveFlag2 | — |
| ACTIVE_FLAG | FdhUpdatedByUserPEO1_1ActiveFlag3 | — |
| ACTIVE_FLAG | LeCreatedByUserPEOActiveFlag | — |
| ACTIVE_FLAG | LeUpdatedByUserPEO1_1ActiveFlag1 | — |
| BUSINESS_GROUP_ID | FdhCreatedByUserPEOBusinessGroupId2 | — |
| BUSINESS_GROUP_ID | FdhUpdatedByUserPEO1_1BusinessGroupId3 | — |
| BUSINESS_GROUP_ID | LeCreatedByUserPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | LeUpdatedByUserPEO1_1BusinessGroupId1 | — |
| CREATED_BY | FdhCreatedByUserPEOCreatedBy7 | — |
| CREATED_BY | FdhUpdatedByUserPEO1_1CreatedBy8 | — |
| CREATED_BY | LeCreatedByUserPEOCreatedBy5 | — |
| CREATED_BY | LeUpdatedByUserPEO1_1CreatedBy6 | — |
| CREATION_DATE | FdhCreatedByUserPEOCreationDate7 | — |
| CREATION_DATE | FdhUpdatedByUserPEO1_1CreationDate8 | — |
| CREATION_DATE | LeCreatedByUserPEOCreationDate5 | — |
| CREATION_DATE | LeUpdatedByUserPEO1_1CreationDate6 | — |
| CREDENTIALS_EMAIL_SENT | FdhCreatedByUserPEOCredentialsEmailSent2 | — |
| CREDENTIALS_EMAIL_SENT | FdhUpdatedByUserPEO1_1CredentialsEmailSent3 | — |
| CREDENTIALS_EMAIL_SENT | LeCreatedByUserPEOCredentialsEmailSent | — |
| CREDENTIALS_EMAIL_SENT | LeUpdatedByUserPEO1_1CredentialsEmailSent1 | — |
| END_DATE | FdhCreatedByUserPEOEndDate2 | — |
| END_DATE | FdhUpdatedByUserPEO1_1EndDate3 | — |
| END_DATE | LeCreatedByUserPEOEndDate | — |
| END_DATE | LeUpdatedByUserPEO1_1EndDate1 | — |
| EXTERNAL_ID | FdhCreatedByUserPEOExternalId2 | — |
| EXTERNAL_ID | FdhUpdatedByUserPEO1_1ExternalId3 | — |
| EXTERNAL_ID | LeCreatedByUserPEOExternalId | — |
| EXTERNAL_ID | LeUpdatedByUserPEO1_1ExternalId1 | — |
| HR_TERMINATED | FdhCreatedByUserPEOHrTerminated2 | — |
| HR_TERMINATED | FdhUpdatedByUserPEO1_1HrTerminated3 | — |
| HR_TERMINATED | LeCreatedByUserPEOHrTerminated | — |
| HR_TERMINATED | LeUpdatedByUserPEO1_1HrTerminated1 | — |
| LAST_UPDATE_DATE | FdhCreatedByUserPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | FdhUpdatedByUserPEO1_1LastUpdateDate8 | — |
| LAST_UPDATE_DATE | LeCreatedByUserPEOLastUpdateDate5 | — |
| LAST_UPDATE_DATE | LeUpdatedByUserPEO1_1LastUpdateDate6 | — |
| LAST_UPDATE_LOGIN | FdhCreatedByUserPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | FdhUpdatedByUserPEO1_1LastUpdateLogin8 | — |
| LAST_UPDATE_LOGIN | LeCreatedByUserPEOLastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | LeUpdatedByUserPEO1_1LastUpdateLogin6 | — |
| LAST_UPDATED_BY | FdhCreatedByUserPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | FdhUpdatedByUserPEO1_1LastUpdatedBy8 | — |
| LAST_UPDATED_BY | LeCreatedByUserPEOLastUpdatedBy5 | — |
| LAST_UPDATED_BY | LeUpdatedByUserPEO1_1LastUpdatedBy6 | — |
| MULTITENANCY_USERNAME | FdhCreatedByUserPEOMultitenancyUsername2 | — |
| MULTITENANCY_USERNAME | FdhUpdatedByUserPEO1_1MultitenancyUsername3 | — |
| MULTITENANCY_USERNAME | LeCreatedByUserPEOMultitenancyUsername | — |
| MULTITENANCY_USERNAME | LeUpdatedByUserPEO1_1MultitenancyUsername1 | — |
| OBJECT_VERSION_NUMBER | FdhCreatedByUserPEOObjectVersionNumber6 | — |
| OBJECT_VERSION_NUMBER | FdhUpdatedByUserPEO1_1ObjectVersionNumber7 | — |
| OBJECT_VERSION_NUMBER | LeCreatedByUserPEOObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | LeUpdatedByUserPEO1_1ObjectVersionNumber5 | — |
| PARTY_ID | FdhCreatedByUserPEOPartyId2 | — |
| PARTY_ID | FdhUpdatedByUserPEO1_1PartyId3 | — |
| PARTY_ID | LeCreatedByUserPEOPartyId | — |
| PARTY_ID | LeUpdatedByUserPEO1_1PartyId1 | — |
| PERSON_ID | FdhCreatedByUserPEOPersonId2 | — |
| PERSON_ID | FdhUpdatedByUserPEO1_1PersonId3 | — |
| PERSON_ID | LeCreatedByUserPEOPersonId | — |
| PERSON_ID | LeUpdatedByUserPEO1_1PersonId1 | — |
| START_DATE | FdhCreatedByUserPEOStartDate2 | — |
| START_DATE | FdhUpdatedByUserPEO1_1StartDate3 | — |
| START_DATE | LeCreatedByUserPEOStartDate | — |
| START_DATE | LeUpdatedByUserPEO1_1StartDate1 | — |
| SUSPENDED | FdhCreatedByUserPEOSuspended2 | — |
| SUSPENDED | FdhUpdatedByUserPEO1_1Suspended3 | — |
| SUSPENDED | LeCreatedByUserPEOSuspended | — |
| SUSPENDED | LeUpdatedByUserPEO1_1Suspended1 | — |
| USER_DATA_CHECKSUM | FdhCreatedByUserPEOUserDataChecksum2 | — |
| USER_DATA_CHECKSUM | FdhUpdatedByUserPEO1_1UserDataChecksum3 | — |
| USER_DATA_CHECKSUM | LeCreatedByUserPEOUserDataChecksum | — |
| USER_DATA_CHECKSUM | LeUpdatedByUserPEO1_1UserDataChecksum1 | — |
| USER_DISTINGUISHED_NAME | FdhCreatedByUserPEOUserDistinguishedName2 | — |
| USER_DISTINGUISHED_NAME | FdhUpdatedByUserPEO1_1UserDistinguishedName3 | — |
| USER_DISTINGUISHED_NAME | LeCreatedByUserPEOUserDistinguishedName | — |
| USER_DISTINGUISHED_NAME | LeUpdatedByUserPEO1_1UserDistinguishedName1 | — |
| USER_GUID | FdhCreatedByUserPEOUserGuid2 | — |
| USER_GUID | FdhUpdatedByUserPEO1_1UserGuid3 | — |
| USER_GUID | LeCreatedByUserPEOUserGuid | — |
| USER_GUID | LeUpdatedByUserPEO1_1UserGuid1 | — |
| USER_ID | FdhCreatedByUserPEOUserId2 | — |
| USER_ID | FdhUpdatedByUserPEO1_1UserId3 | — |
| USER_ID | LeCreatedByUserPEOUserId | — |
| USER_ID | LeUpdatedByUserPEO1_1UserId1 | — |
| USERNAME | FdhCreatedByUserPEOUsername2 | — |
| USERNAME | FdhUpdatedByUserPEO1_1Username3 | — |
| USERNAME | LeCreatedByUserPEOUsername | — |
| USERNAME | LeUpdatedByUserPEO1_1Username1 | — |

### [[legalentityprimaryledgerpvo|LegalEntityPrimaryLedgerPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[legalentitypvo|LegalEntityPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[memolinepvo|MemoLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[obligrulepvo|ObligRulePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[payablesreconciliationparameterpvo|PayablesReconciliationParameterPVO]] (AP · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UpdatedByPersonNameObjectVersionNumber | — |
| PERSON_ID | UpdatedByUserPersonId | — |
| USER_GUID | UpdatedByUserUserGuid | — |
| USER_ID | UpdatedByUserUserId | — |
| USERNAME | UpdatedByUserUsername | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[perfobligationlindistspvo|PerfObligationLinDistsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CustContHeadUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CustContHeadUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PerfObligUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PerfObligUserUpdatedByObjectVersionNumber | — |
| PERSON_ID | CustContHeadUserCreatedByPersonId | — |
| PERSON_ID | CustContHeadUserUpdatedByPersonId | — |
| PERSON_ID | PerfObligUserCreatedByPersonId | — |
| PERSON_ID | PerfObligUserUpdatedByPersonId | — |
| USER_ID | CustContHeadUserCreatedByUserId | — |
| USER_ID | CustContHeadUserUpdatedByUserId | — |
| USER_ID | PerfObligUserCreatedByUserId | — |
| USER_ID | PerfObligUserUpdatedByUserId | — |
| USERNAME | CustContHeadUserCreatedByUsername | — |
| USERNAME | CustContHeadUserUpdatedByUsername | — |
| USERNAME | PerfObligUserCreatedByUsername | — |
| USERNAME | PerfObligUserUpdatedByUsername | — |

### [[perfobligationlinespvo|PerfObligationLinesPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PerfObligUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PerfObligUserUpdatedByObjectVersionNumber | — |
| PERSON_ID | PerfObligUserCreatedByPersonId | — |
| PERSON_ID | PerfObligUserUpdatedByPersonId | — |
| USER_ID | PerfObligUserCreatedByUserId | — |
| USER_ID | PerfObligUserUpdatedByUserId | — |
| USERNAME | PerfObligUserCreatedByUsername | — |
| USERNAME | PerfObligUserUpdatedByUsername | — |

### [[perfobligationspvo|PerfObligationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CustContHeadUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CustContHeadUserUpdatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | CustContHeadUserCreatedByPersonId | — |
| PERSON_ID | CustContHeadUserUpdatedByPersonId | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_ID | CustContHeadUserCreatedByUserId | — |
| USER_ID | CustContHeadUserUpdatedByUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | CustContHeadUserCreatedByUsername | — |
| USERNAME | CustContHeadUserUpdatedByUsername | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[periodstatuspvo|PeriodStatusPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserLastUpdatedByObjectVersionNumber | — |
| USER_ID | UserLastUpdatedByUserId | — |

### [[personnamepvo|PersonNamePVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | ✅ |

### [[personnamepvoviewall|PersonNamePVOViewAll]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | ✅ |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 2/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | SupervisorUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | SupervisorUserPEOBusinessGroupId | — |
| CREATED_BY | SupervisorUserPEOCreatedBy | — |
| CREATION_DATE | SupervisorUserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | SupervisorUserPEOCredentialsEmailSent | — |
| END_DATE | SupervisorUserPEOEndDate | — |
| HR_TERMINATED | SupervisorUserPEOHrTerminated | — |
| LAST_UPDATE_DATE | SupervisorUserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupervisorUserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SupervisorUserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | SupervisorUserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | SupervisorUserPEOObjectVersionNumber | — |
| PARTY_ID | SupervisorUserPEOPartyId | — |
| PERSON_ID | SupervisorUserPEOPersonId | — |
| START_DATE | SupervisorUserPEOStartDate | — |
| SUSPENDED | SupervisorUserPEOSuspended | — |
| USER_DATA_CHECKSUM | SupervisorUserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | SupervisorUserPEOUserDistinguishedName | — |
| USER_GUID | SupervisorUserPEOUserGuid | — |
| USER_ID | SupervisorUserPEOUserId | — |
| USERNAME | SupervisorUserPEOUsername | ✅ |

### [[pricingcombinationpvo|PricingCombinationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |

### [[processactionitempvo|ProcessActionItemPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PrAcCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | PrAcUpdatedByObjectVerNumber | — |
| PERSON_ID | PrAcCreatedByPersonId | — |
| PERSON_ID | PrAcUpdatedByPersonId | — |
| USER_GUID | PrAcCreatedByUserGuid | — |
| USER_GUID | PrAcUpdatedByUserGuid | — |
| USER_ID | PrAcCreatedByUserId | — |
| USER_ID | PrAcUpdatedByUserId | — |
| USERNAME | PrAcCreatedByUsername | — |
| USERNAME | PrAcUpdatedByUsername | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[purchasingagentaccessesextractpvo|PurchasingAgentAccessesExtractPVO]] (PO · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_GUID | UserGuid | ✅ |
| USER_ID | UserId | ✅ |
| USERNAME | Username | ✅ |

### [[qualityactionrelationship|QualityActionRelationship]] (OTHER · BICC: 1/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | — |
| CREATED_BY | UserPEOCreatedBy | — |
| CREATION_DATE | UserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | UserPEOCredentialsEmailSent | — |
| END_DATE | UserPEOEndDate | — |
| EXTERNAL_ID | UserPEOExternalId | — |
| HR_TERMINATED | UserPEOHrTerminated | — |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PARTY_ID | UserPEOPartyId | — |
| PERSON_ID | UserPEOPersonId | — |
| START_DATE | UserPEOStartDate | — |
| SUSPENDED | UserPEOSuspended | — |
| USER_DATA_CHECKSUM | UserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserPEOUserDistinguishedName | — |
| USER_GUID | UserPEOUserGuid | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | — |

### [[qualityactions|QualityActions]] (OTHER · BICC: 1/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPEOUserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | — |
| CREATED_BY | UserPEOCreatedBy | — |
| CREATION_DATE | UserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | UserPEOCredentialsEmailSent | — |
| END_DATE | UserPEOEndDate | — |
| EXTERNAL_ID | UserPEOExternalId | — |
| HR_TERMINATED | UserPEOHrTerminated | — |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PARTY_ID | UserPEOPartyId | — |
| PERSON_ID | UserPEOPersonId | — |
| START_DATE | UserPEOStartDate | — |
| SUSPENDED | UserPEOSuspended | — |
| USER_DATA_CHECKSUM | UserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserPEOUserDistinguishedName | — |
| USER_GUID | UserPEOUserGuid | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | — |

### [[qualityaffectedobjects|QualityAffectedObjects]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPActiveFlag | — |
| BUSINESS_GROUP_ID | UserPBusinessGroupId | — |
| CREATED_BY | UserPCreatedBy | — |
| CREATION_DATE | UserPCreationDate | — |
| CREDENTIALS_EMAIL_SENT | UserPCredentialsEmailSent | — |
| END_DATE | UserPEndDate | — |
| EXTERNAL_ID | UserPExternalId | — |
| HR_TERMINATED | UserPHrTerminated | — |
| LAST_UPDATE_DATE | UserPLastUpdateDate | — |
| LAST_UPDATE_LOGIN | UserPLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserPMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserPObjectVersionNumber | — |
| PARTY_ID | UserPPartyId | — |
| PERSON_ID | UserPPersonId | — |
| START_DATE | UserPStartDate | — |
| SUSPENDED | UserPSuspended | — |
| USER_DATA_CHECKSUM | UserPUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserPUserDistinguishedName | — |
| USER_GUID | UserPUserGuid | — |
| USER_ID | UserPUserId | — |
| USERNAME | UserPUsername | — |

### [[qualityaffectedobjectsaction|QualityAffectedObjectsAction]] (OTHER · BICC: 1/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPActiveFlag | — |
| BUSINESS_GROUP_ID | UserPBusinessGroupId | — |
| CREATED_BY | UserPCreatedBy | — |
| CREATION_DATE | UserPCreationDate | — |
| CREDENTIALS_EMAIL_SENT | UserPCredentialsEmailSent | — |
| END_DATE | UserPEndDate | — |
| EXTERNAL_ID | UserPExternalId | — |
| HR_TERMINATED | UserPHrTerminated | — |
| LAST_UPDATE_DATE | UserPLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserPLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserPMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserPObjectVersionNumber | — |
| PARTY_ID | UserPPartyId | — |
| PERSON_ID | UserPPersonId | — |
| START_DATE | UserPStartDate | — |
| SUSPENDED | UserPSuspended | — |
| USER_DATA_CHECKSUM | UserPUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserPUserDistinguishedName | — |
| USER_GUID | UserPUserGuid | — |
| USER_ID | UserPUserId | — |
| USERNAME | UserPUsername | — |

### [[qualityissues|QualityIssues]] (OTHER · BICC: 1/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserActiveFlag | — |
| BUSINESS_GROUP_ID | UserBusinessGroupId | — |
| CREATED_BY | UserCreatedBy1 | — |
| CREATION_DATE | UserCreationDate1 | — |
| CREDENTIALS_EMAIL_SENT | UserCredentialsEmailSent | — |
| END_DATE | UserEndDate | — |
| EXTERNAL_ID | UserExternalId | — |
| HR_TERMINATED | UserHrTerminated | — |
| LAST_UPDATE_DATE | UserLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserLastUpdateLogin | — |
| LAST_UPDATED_BY | UserLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserObjectVersionNumber | — |
| PARTY_ID | UserPartyId | — |
| PERSON_ID | UserPersonId | — |
| START_DATE | UserStartDate | — |
| SUSPENDED | UserSuspended | — |
| USER_DATA_CHECKSUM | UserUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserUserDistinguishedName | — |
| USER_GUID | UserUserGuid | — |
| USER_ID | UserUserId | — |
| USERNAME | UserUsername | — |

### [[qualityrelationships|QualityRelationships]] (OTHER · BICC: 1/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPEOActiveFlag | — |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | — |
| CREATED_BY | UserPEOCreatedBy | — |
| CREATION_DATE | UserPEOCreationDate | — |
| CREDENTIALS_EMAIL_SENT | UserPEOCredentialsEmailSent | — |
| END_DATE | UserPEOEndDate | — |
| EXTERNAL_ID | UserPEOExternalId | — |
| HR_TERMINATED | UserPEOHrTerminated | — |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | — |
| MULTITENANCY_USERNAME | UserPEOMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PARTY_ID | UserPEOPartyId | — |
| PERSON_ID | UserPEOPersonId | — |
| START_DATE | UserPEOStartDate | — |
| SUSPENDED | UserPEOSuspended | — |
| USER_DATA_CHECKSUM | UserPEOUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UserPEOUserDistinguishedName | — |
| USER_GUID | UserPEOUserGuid | — |
| USER_ID | UserPEOUserId | — |
| USERNAME | UserPEOUsername | — |

### [[rateadjustmentpvo|RateAdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | RAUserCreatedByPersonId | — |
| PERSON_ID | RAUserUpdatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | RAUserCreatedByUserGuid | — |
| USER_GUID | RAUserUpdatedByUserGuid | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | RAUserCreatedByUserId | — |
| USER_ID | RAUserUpdatedByUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | RAUserCreatedByUsername | — |
| USERNAME | RAUserUpdatedByUsername | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | RAUserCreatedByPersonId | — |
| PERSON_ID | RAUserUpdatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | RAUserCreatedByUserGuid | — |
| USER_GUID | RAUserUpdatedByUserGuid | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | RAUserCreatedByUserId | — |
| USER_ID | RAUserUpdatedByUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | RAUserCreatedByUsername | — |
| USERNAME | RAUserUpdatedByUsername | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | RAUserCreatedByPersonId | — |
| PERSON_ID | RAUserUpdatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | RAUserCreatedByUserGuid | — |
| USER_GUID | RAUserUpdatedByUserGuid | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | RAUserCreatedByUserId | — |
| USER_ID | RAUserUpdatedByUserId | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | RAUserCreatedByUsername | — |
| USERNAME | RAUserUpdatedByUsername | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receipthistorydistributionpvo|ReceiptHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receipthistorypvo|ReceiptHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[receivablesreconciliationparameterpvo|ReceivablesReconciliationParameterPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UpdatedByPersonNameObjectVersionNumber | — |
| PERSON_ID | UpdatedByUserPersonId | — |
| USER_GUID | UpdatedByUserUserGuid | — |
| USER_ID | UpdatedByUserUserId | — |
| USERNAME | UpdatedByUserUsername | ✅ |

### [[remediationplanpvo|RemediationPlanPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmntCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnCreatdByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmPnUpdatedByObjectVerNumber | — |
| PERSON_ID | CmntCreatedByPersonId | — |
| PERSON_ID | RmPnApprovedByPersonId | — |
| PERSON_ID | RmPnCreatedByPersonId | — |
| PERSON_ID | RmPnReviewedByPersonId | — |
| PERSON_ID | RmPnUpdatedByPersonId | — |
| USER_GUID | CmntCreatedByUserGuid | — |
| USER_GUID | RmPnApprovedByUserGuid | — |
| USER_GUID | RmPnCreatedByUserGuid | — |
| USER_GUID | RmPnReviewedByUserGuid | — |
| USER_GUID | RmPnUpdatedByUserGuid | — |
| USER_ID | CmntCreatedByUserId | — |
| USER_ID | RmPnApprovedByUserId | — |
| USER_ID | RmPnCreatedByUserId | — |
| USER_ID | RmPnReviewedByUserId | — |
| USER_ID | RmPnUpdatedByUserId | — |
| USERNAME | CmntCreatedByUsername | — |
| USERNAME | RmPnApprovedByUsername | — |
| USERNAME | RmPnCreatedByUsername | — |
| USERNAME | RmPnReviewedByUsername | — |
| USERNAME | RmPnUpdatedByUsername | — |

### [[remediationtaskpvo|RemediationTaskPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | RmTkCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RmTkUpdatedByObjectVerNumber | — |
| PERSON_ID | RmTkCreatedByPersonId | — |
| PERSON_ID | RmTkUpdatedByPersonId | — |
| USER_GUID | RmTkCreatedByUserGuid | — |
| USER_GUID | RmTkUpdatedByUserGuid | — |
| USER_ID | RmTkCreatedByUserId | — |
| USER_ID | RmTkUpdatedByUserId | — |
| USERNAME | RmTkCreatedByUsername | — |
| USERNAME | RmTkUpdatedByUsername | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UserId | — |
| USER_ID | UserId1 | — |
| USER_ID | UserId2 | — |
| USERNAME | UserUsernameReqDistLastUpdatedBy | — |
| USERNAME | UserUsernameReqHeaderLastUpdatedBy | — |
| USERNAME | UserUsernameReqLineLastUpdatedBy | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UserId | — |
| USER_ID | UserId1 | — |
| USER_ID | UserId2 | — |
| USERNAME | UserUsernameReqDistLastUpdatedBy | — |
| USERNAME | UserUsernameReqHeaderLastUpdatedBy | — |
| USERNAME | UserUsernameReqLineLastUpdatedBy | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UserId | — |
| USER_ID | UserId1 | — |
| USERNAME | UserUsernameReqHeaderLastUpdatedBy | — |
| USERNAME | UserUsernameReqLineLastUpdatedBy | — |

### [[resourcepartnerpvo|ResourcePartnerPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| USER_ID | UserId | — |
| USERNAME | Username | — |

### [[revenueadjustmentdistributionpvo|RevenueAdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[revenueadjustmentpvo|RevenueAdjustmentPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[riskanalysispvo|RiskAnalysisPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | RskAnlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RskAnlUpdatedByObjectVerNumber | — |
| PERSON_ID | RskAnlCreatedByPersonId | — |
| PERSON_ID | RskAnlUpdatedByPersonId | — |
| USER_GUID | RskAnlCreatedByUserGuid | — |
| USER_GUID | RskAnlUpdatedByUserGuid | — |
| USER_ID | RskAnlCreatedByUserId | — |
| USER_ID | RskAnlUpdatedByUserId | — |
| USERNAME | RskAnlCreatedByUsername | — |
| USERNAME | RskAnlUpdatedByUsername | — |

### [[riskevaluationpvo|RiskEvaluationPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | RskEvlCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | RskEvlUpdatedByObjectVerNumber | — |
| PERSON_ID | RskEvlCreatedByPersonId | — |
| PERSON_ID | RskEvlUpdatedByPersonId | — |
| USER_GUID | RskEvlCreatedByUserGuid | — |
| USER_GUID | RskEvlUpdatedByUserGuid | — |
| USER_ID | RskEvlCreatedByUserId | — |
| USER_ID | RskEvlUpdatedByUserId | — |
| USERNAME | RskEvlCreatedByUsername | — |
| USERNAME | RskEvlUpdatedByUsername | — |

### [[riskmanagementchangehistorypvo|RiskManagementChangeHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CHUpdatedByObjectVerNumber | — |
| PERSON_ID | CHUpdatedByPersonId | — |
| USER_GUID | CHUpdatedByUserGuid | — |
| USER_ID | CHUpdatedByUserId | — |
| USERNAME | CHUpdatedByUsername | — |

### [[screeningpackagepvo|ScreeningPackagePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PERSON_ID | UserPEOPersonId | — |
| USER_ID | UserPEOUserId | — |

### [[sitecontact|SiteContact]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserCreatedByCreatedBy | — |
| CREATION_DATE | UserCreatedByCreationDate | — |
| LAST_UPDATE_DATE | UserLastUpdatedByLastUpdateDate | — |
| LAST_UPDATED_BY | UserLastUpdatedByLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserLastUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserLastUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserLastUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserLastUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserLastUpdatedByUsername | — |

### [[sitecontactrelationship|SiteContactRelationShip]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserCreatedByCreatedBy | — |
| CREATION_DATE | UserCreatedByCreationDate | — |
| LAST_UPDATE_DATE | UserLastUpdatedByLastUpdateDate | — |
| LAST_UPDATED_BY | UserLastUpdatedByLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserLastUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserLastUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserLastUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserLastUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserLastUpdatedByUsername | — |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[suppliercontactuseracctdetailspvo|SupplierContactUserAcctDetailsPVO]] (PO · BICC: 9/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UsersActiveFlag | ✅ |
| BUSINESS_GROUP_ID | UsersBusinessGroupId | — |
| CREATED_BY | UsersCreatedBy | ✅ |
| CREATION_DATE | UsersCreationDate | ✅ |
| END_DATE | UsersEndDate | — |
| HR_TERMINATED | UsersHrTerminated | — |
| LAST_UPDATE_DATE | UsersLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UsersLastUpdateLogin | — |
| LAST_UPDATED_BY | UsersLastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | UsersMultitenancyUsername | — |
| OBJECT_VERSION_NUMBER | UsersObjectVersionNumber | — |
| PARTY_ID | PartyId | ✅ |
| PERSON_ID | UsersPersonId | — |
| START_DATE | UsersStartDate | — |
| SUSPENDED | UsersSuspended | ✅ |
| USER_DATA_CHECKSUM | UsersUserDataChecksum | — |
| USER_DISTINGUISHED_NAME | UsersUserDistinguishedName | — |
| USER_GUID | UsersUserGuid | — |
| USER_ID | UserId | ✅ |
| USERNAME | UsersUsername | ✅ |

### [[supportingreferencebalancepvo|SupportingReferenceBalancePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[surveyresultspvo|SurveyResultsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | SrvyApprovedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | SrvyCreatedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | SrvyReviewedByObjectVerNumber | — |
| OBJECT_VERSION_NUMBER | SrvyUpdatedByObjectVerNumber | — |
| PERSON_ID | SrvyApprovedByPersonId | — |
| PERSON_ID | SrvyCreatedByPersonId | — |
| PERSON_ID | SrvyReviewedByPersonId | — |
| PERSON_ID | SrvyUpdatedByPersonId | — |
| USER_GUID | SrvyApprovedByUserGuid | — |
| USER_GUID | SrvyCreatedByUserGuid | — |
| USER_GUID | SrvyReviewedByUserGuid | — |
| USER_GUID | SrvyUpdatedByUserGuid | — |
| USER_ID | SrvyApprovedByUserId | — |
| USER_ID | SrvyCreatedByUserId | — |
| USER_ID | SrvyReviewedByUserId | — |
| USER_ID | SrvyUpdatedByUserId | — |
| USERNAME | SrvyApprovedByUsername | — |
| USERNAME | SrvyCreatedByUsername | — |
| USERNAME | SrvyReviewedByUsername | — |
| USERNAME | SrvyUpdatedByUsername | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| PERSON_ID | UserCreatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactioninitheaderpvo|TransactionInitHeaderPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | UserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | UserUpdatedByObjectVersionNumber | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[transactionrectheaderpvo|TransactionRectHeaderPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | UserCreatedByPersonId | — |
| PERSON_ID | UserUpdatedByPersonId | — |
| USER_GUID | UserCreatedByUserGuid | — |
| USER_GUID | UserUpdatedByUserGuid | — |
| USER_ID | UserCreatedByUserId | — |
| USER_ID | UserUpdatedByUserId | — |
| USERNAME | UserCreatedByUsername | — |
| USERNAME | UserUpdatedByUsername | — |

### [[userextractpvo|UserExtractPVO]] (HCM · BICC: 22/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CREDENTIALS_EMAIL_SENT | CredentialsEmailSent | ✅ |
| END_DATE | EndDate | ✅ |
| EXTERNAL_ID | ExternalId | ✅ |
| HR_TERMINATED | HrTerminated | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MULTITENANCY_USERNAME | MultitenancyUsername | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PARTY_ID | PartyId | ✅ |
| PERSON_ID | PersonId | ✅ |
| START_DATE | StartDate | ✅ |
| SUSPENDED | Suspended | ✅ |
| USER_DATA_CHECKSUM | UserDataChecksum | ✅ |
| USER_DISTINGUISHED_NAME | UserDistinguishedName | ✅ |
| USER_GUID | UserGuid | ✅ |
| USER_ID | UserId | ✅ |
| USERNAME | Username | ✅ |

### [[userpvo|UserPVO]] (HCM · BICC: 7/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | UserPEOActiveFlag | ✅ |
| BUSINESS_GROUP_ID | UserPEOBusinessGroupId | — |
| CREATED_BY | UserPEOCreatedBy | — |
| CREATION_DATE | UserPEOCreationDate | — |
| END_DATE | UserPEOEndDate | — |
| HR_TERMINATED | UserPEOHrTerminated | — |
| LAST_UPDATE_DATE | UserPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | UserPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | UserPEOObjectVersionNumber | — |
| PARTY_ID | UserPEOPartyId | ✅ |
| PERSON_ID | UserPEOPersonId | ✅ |
| START_DATE | UserPEOStartDate | — |
| SUSPENDED | UserPEOSuspended | — |
| USER_GUID | UserPEOUserGuid | ✅ |
| USER_ID | UserPEOUserId | ✅ |
| USERNAME | UserPEOUsername | ✅ |

### [[xcccmrexpensetransactionpvo|XccCmrExpenseTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserLastUpdateByObjectVersionNumber | — |
| PERSON_ID | CmrRcvEventsUserCreatedByPersonId | — |
| PERSON_ID | CmrRcvEventsUserLastUpdateByPersonId | — |
| USER_ID | CmrRcvEventsUserCreatedByUserId | — |
| USER_ID | CmrRcvEventsUserLastUpdateByUserId | — |
| USERNAME | CmrRcvEventsUserCreatedByUsername | — |
| USERNAME | CmrRcvEventsUserLastUpdateByUsername | — |

### [[xcccmrinventorytransactionpvo|XccCmrInventoryTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserLastUpdateByObjectVersionNumber | — |
| PERSON_ID | CmrRcvEventsUserCreatedByPersonId | — |
| PERSON_ID | CmrRcvEventsUserLastUpdateByPersonId | — |
| USER_ID | CmrRcvEventsUserCreatedByUserId | — |
| USER_ID | CmrRcvEventsUserLastUpdateByUserId | — |
| USERNAME | CmrRcvEventsUserCreatedByUsername | — |
| USERNAME | CmrRcvEventsUserLastUpdateByUsername | — |

### [[xcccmrreceipttransactionpvo|XccCmrReceiptTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserCreatedByObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | CmrRcvEventsUserLastUpdateByObjectVersionNumber | — |
| PERSON_ID | CmrRcvEventsUserCreatedByPersonId | — |
| PERSON_ID | CmrRcvEventsUserLastUpdateByPersonId | — |
| USER_ID | CmrRcvEventsUserCreatedByUserId | — |
| USER_ID | CmrRcvEventsUserLastUpdateByUserId | — |
| USERNAME | CmrRcvEventsUserCreatedByUsername | — |
| USERNAME | CmrRcvEventsUserLastUpdateByUsername | — |
