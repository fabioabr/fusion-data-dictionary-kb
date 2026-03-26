---
id: DOC-PO-031
doc_type: system-doc
title: "PON_PROGRAM_TEAM_MEMBERS — Membros de Equipe de Programa de Negociação"
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
  - sourcing
  - negociacao
  - equipe
aliases:
  - PON_PROGRAM_TEAM_MEMBERS
  - pon_program_team_members
  - membros-equipe-programa-sourcing
  - program-team-members
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_PROGRAM_TEAM_MEMBERS

## Visão Geral

Armazena os **membros da equipe** associados a um programa de negociação (sourcing program) no módulo Oracle Sourcing. Cada registro representa a associação de um usuário/participante a um programa, incluindo seu papel (role) e permissões dentro do contexto do programa de negociação.

> [!note] Módulo PON
> O prefixo `PON` identifica tabelas do submódulo **Oracle Sourcing / Negotiations**, que gerencia processos de licitação, RFQ, leilão reverso e programas de negociação com fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Composição de equipes de negociação:** Definição dos membros que participam de um programa de sourcing (compradores, aprovadores, observadores).
- **Controle de acesso:** Determina quais usuários podem visualizar, editar ou aprovar atividades do programa.
- **Workflow de aprovação:** Identifica os aprovadores responsáveis por etapas do programa de negociação.
- **Auditoria de participação:** Rastreamento de quem participou de cada programa de sourcing.
- **Segregação de funções:** Garante que diferentes papéis (criador, avaliador, aprovador) sejam atribuídos a pessoas distintas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROGRAM_TEAM_MEMBER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do membro da equipe do programa | — | 🟡 75% |
| 2 | PROGRAM_ID | NUMBER(18) | NOT NULL | FK | Identificador do programa de negociação | [[pon_sourcing_programs]] | 🟡 75% |
| 3 | USER_ID | NUMBER(18) | NOT NULL | FK | Identificador do usuário membro da equipe | [[per_users]] | 🟡 70% |
| 4 | MEMBER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo/papel do membro no programa (BUYER, APPROVER, OBSERVER) | — | 🟡 65% |
| 5 | ACCESS_TYPE | VARCHAR2(30) | NULL | Classificação | Nível de acesso do membro (FULL, VIEW_ONLY) | — | 🟡 60% |
| 6 | APPROVER_FLAG | VARCHAR2(1) | NULL | Flag | Indica se o membro é aprovador (Y/N) | — | 🟡 60% |
| 7 | TASK_NAME | VARCHAR2(240) | NULL | Texto livre | Nome da tarefa atribuída ao membro | — | 🟡 55% |
| 8 | SEQUENCE_NUMBER | NUMBER | NULL | Controle | Sequência de avaliação/aprovação | — | 🟡 55% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_sourcing_programs]] — via `PROGRAM_ID` (programa de negociação)
- [[per_users]] — via `USER_ID` (usuário membro da equipe)

### Tabelas-filha (FK de saída)
- Sem tabelas-filha conhecidas diretamente.

### Tabelas relacionadas no contexto Sourcing

---

## Uso Típico

### Listar membros de um programa de negociação
```sql
SELECT ptm.USER_ID, ptm.MEMBER_TYPE, ptm.ACCESS_TYPE,
       ptm.APPROVER_FLAG, ptm.SEQUENCE_NUMBER
FROM   PON_PROGRAM_TEAM_MEMBERS ptm
WHERE  ptm.PROGRAM_ID = :p_program_id
ORDER BY ptm.SEQUENCE_NUMBER;
```

### Identificar aprovadores de um programa
```sql
SELECT ptm.USER_ID, ptm.SEQUENCE_NUMBER
FROM   PON_PROGRAM_TEAM_MEMBERS ptm
WHERE  ptm.PROGRAM_ID = :p_program_id
  AND  ptm.APPROVER_FLAG = 'Y'
ORDER BY ptm.SEQUENCE_NUMBER;
```

---

## Observações

- A tabela pertence ao submódulo **Oracle Sourcing (PON)**, que gerencia processos de negociação eletrônica com fornecedores.
- O campo `MEMBER_TYPE` define o papel funcional do membro dentro do programa (comprador, aprovador, observador).
- O campo `ACCESS_TYPE` controla o nível de permissão do membro no programa.
- A coluna `SEQUENCE_NUMBER` é relevante para definir a ordem de aprovação em workflows sequenciais.
- As colunas e tipos exatos podem variar conforme o release do Oracle Fusion; recomenda-se validação no ambiente.

---

## Referências

- [Oracle Docs — Procurement Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponprogramteammembers.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
