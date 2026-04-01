---
id: DOC-HCM-718
doc_type: system-doc
title: "PER_USER_HISTORY — Histórico de Usuários"
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
  - histórico-usuários
  - auditoria
aliases:
  - PER_USER_HISTORY
  - per_user_history
  - per-user-history
  - histórico-de-usuários
  - user-history
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_USER_HISTORY

## Visão Geral

Armazena o **histórico de alterações** nos registros de usuários do sistema, incluindo mudanças de status, nome de usuário e vinculações.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de segurança** — rastreia todas as mudanças em contas de usuário.
- **Compliance** — evidência para regulatórios sobre controle de acesso.
- **Troubleshooting** — diagnóstico de problemas de acesso via histórico.
- **Governança** — visibilidade sobre ciclo de vida das contas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro histórico | — | 🟢 85% |
| 2 | USER_ID | NUMBER(18) | NOT NULL | FK | Usuário cujo histórico é registrado | PER_USERS | 🟢 85% |
| 3 | USER_NAME | VARCHAR2(100) | NULL | Identificação | Nome de login no momento da alteração | — | 🟡 80% |
| 4 | CHANGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de alteração realizada | — | 🟡 70% |
| 5 | OLD_VALUE | VARCHAR2(240) | NULL | Dados | Valor anterior | — | 🟡 70% |
| 6 | NEW_VALUE | VARCHAR2(240) | NULL | Dados | Novo valor | — | 🟡 70% |
| 7 | EFFECTIVE_DATE | DATE | NULL | Vigência | Data efetiva da mudança | — | 🟡 75% |
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

### Histórico de alterações de um usuário
```sql
SELECT uh.CHANGE_TYPE, uh.OLD_VALUE, uh.NEW_VALUE, uh.EFFECTIVE_DATE
FROM   PER_USER_HISTORY uh
WHERE  uh.USER_ID = :p_user_id
ORDER BY uh.CREATION_DATE DESC;
```

### Filtros comuns
- `USER_ID = :p_user_id` — Histórico de um usuário específico
- `CHANGE_TYPE = 'STATUS'` — Apenas mudanças de status

---

## Observações

- Tabela de auditoria — registros são imutáveis (somente inserção).
- Permite reconstruir a timeline completa de uma conta de usuário.
- Fundamental para auditorias de segurança e compliance.

---

## Referências

- [Oracle Docs — PER_USER_HISTORY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peruserhistory.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[userpvo|UserPVO]] (HCM · BICC: 9/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | UserHistoryPEOBusinessGroupId | — |
| CREATED_BY | UserHistoryPEOCreatedBy | ✅ |
| CREATION_DATE | UserHistoryPEOCreationDate | ✅ |
| END_DATE | UserHistoryPEOEndDate | ✅ |
| LAST_UPDATE_DATE | UserHistoryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserHistoryPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | UserHistoryPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | UserHistoryPEOObjectVersionNumber | — |
| START_DATE | UserHistoryPEOStartDate | ✅ |
| USER_GUID | UserHistoryPEOUserGuid | ✅ |
| USER_HISTORY_ID | UserHistoryPEOUserHistoryId | ✅ |
| USER_ID | UserHistoryPEOUserId | — |
| USERNAME | UserHistoryPEOUsername | ✅ |
