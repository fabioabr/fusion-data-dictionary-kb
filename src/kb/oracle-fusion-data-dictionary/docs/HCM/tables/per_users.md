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
