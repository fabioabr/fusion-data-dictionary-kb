---
id: DOC-HCM-719
doc_type: system-doc
title: "PER_USER_ROLES — Papéis de Usuários"
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
  - papéis-usuários
  - rbac
aliases:
  - PER_USER_ROLES
  - per_user_roles
  - per-user-roles
  - papéis-de-usuários
  - user-roles
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_USER_ROLES

## Visão Geral

Armazena a **associação entre usuários e papéis** (roles) de segurança, definindo as permissões e acessos de cada usuário no sistema.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de acesso (RBAC)** — define quais funcionalidades cada usuário pode acessar.
- **Segregação de funções** — garante que papéis conflitantes não sejam atribuídos ao mesmo usuário.
- **Provisionamento automático** — roles atribuídos com base na posição/cargo.
- **Auditoria de permissões** — rastreabilidade de quem tem acesso a quê.
- **Compliance regulatório** — evidência de controle de acesso para auditorias.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_ROLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atribuição | — | 🟢 85% |
| 2 | USER_ID | NUMBER(18) | NOT NULL | FK | Usuário que recebe o papel | PER_USERS | 🟢 85% |
| 3 | ROLE_ID | NUMBER(18) | NOT NULL | FK | Papel atribuído ao usuário | — | 🟢 85% |
| 4 | ROLE_NAME | VARCHAR2(240) | NULL | Identificação | Nome do papel | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início da atribuição | — | 🟢 85% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de término da atribuição | — | 🟢 85% |
| 7 | ASSIGNMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de atribuição (manual, automática) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_users]] — via `USER_ID` (usuário do sistema)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Papéis atribuídos a um usuário
```sql
SELECT ur.ROLE_NAME, ur.START_DATE, ur.END_DATE
FROM   PER_USER_ROLES ur
WHERE  ur.USER_ID = :p_user_id
  AND  SYSDATE BETWEEN ur.START_DATE AND NVL(ur.END_DATE, TO_DATE('4712-12-31','YYYY-MM-DD'));
```

### Filtros comuns
- `USER_ID = :p_user_id` — Papéis de um usuário específico
- `END_DATE IS NULL` — Apenas atribuições sem data de término

---

## Observações

- Um usuário pode ter múltiplos papéis simultaneamente.
- Papéis podem ter vigência temporal (START_DATE / END_DATE).
- A segregação de funções (SoD) deve ser validada externamente.
- Atribuições automáticas são provisionadas pelo Oracle Identity Management.

---

## Referências

- [Oracle Docs — PER_USER_ROLES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peruserroles.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[userroleextractpvo|UserRoleExtractPVO]] (HCM · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| END_DATE | EndDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| METHOD_CODE | MethodCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ROLE_GUID | RoleGuid | ✅ |
| ROLE_ID | RoleId | ✅ |
| START_DATE | StartDate | ✅ |
| TERMINATED_FLAG | TerminatedFlag | ✅ |
| USER_ID | UserId | ✅ |
| USER_ROLE_ID | UserRoleId | ✅ |
