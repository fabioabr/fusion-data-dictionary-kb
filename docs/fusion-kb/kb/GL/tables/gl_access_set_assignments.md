---
id: DOC-GL-004
doc_type: system-doc
title: "GL_ACCESS_SET_ASSIGNMENTS — Atribuições de Conjuntos de Acesso"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - acesso
  - atribuicao
  - seguranca
aliases:
  - GL_ACCESS_SET_ASSIGNMENTS
  - gl_access_set_assignments
  - atribuicoes-acesso-gl
  - access-set-assignments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ACCESS_SET_ASSIGNMENTS

## Visao Geral

Armazena as **atribuições de conjuntos de acesso** (Data Access Sets) a ledgers específicos, definindo o nível de privilégio (leitura, leitura/escrita) que cada conjunto concede sobre cada ledger. Funciona como a tabela de interseção entre conjuntos de acesso e os ledgers que eles permitem acessar, com granularidade de permissão.

> [!note] Relação com segurança
> Esta tabela complementa [[gl_access_sets]] e [[gl_access_set_ledgers]], detalhando as atribuições efetivas que controlam quem pode lançar ou apenas consultar dados em cada ledger.

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Controle de acesso granular:** Define se um conjunto de acesso permite apenas leitura ou leitura/escrita em cada ledger.
- **Segregação de funções:** Garante que equipes específicas só possam lançar em ledgers autorizados.
- **Provisioning de usuários:** Base para configuração de acesso ao criar ou alterar perfis de usuários financeiros.
- **Auditoria de permissões:** Rastreamento de quais permissões foram concedidas a cada conjunto de acesso.
- **Configuração multi-ledger:** Permite que um mesmo conjunto acesse múltiplos ledgers com diferentes níveis de permissão.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCESS_SET_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do conjunto de acesso | [[gl_access_sets]] | 🟢 95% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger atribuído | [[gl_ledgers]] | 🟢 95% |
| 3 | ACCESS_PRIVILEGE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Nível de acesso: READ_ONLY, READ_AND_WRITE, etc. | — | 🟢 90% |
| 4 | START_DATE | DATE | NULL | Data | Data de início da atribuição | — | 🟡 75% |
| 5 | END_DATE | DATE | NULL | Data | Data de fim da atribuição (NULL = sem expiração) | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_access_sets]] — via `ACCESS_SET_ID` (conjunto de acesso)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger atribuído)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de interseção (leaf table).

---

## Uso Tipico

### Listar atribuições de um conjunto de acesso
```sql
SELECT asa.ACCESS_SET_ID, das.NAME AS access_set,
       asa.LEDGER_ID, gl.NAME AS ledger,
       asa.ACCESS_PRIVILEGE_CODE
FROM   GL_ACCESS_SET_ASSIGNMENTS asa
JOIN   GL_ACCESS_SETS das ON das.ACCESS_SET_ID = asa.ACCESS_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = asa.LEDGER_ID
WHERE  asa.ACCESS_SET_ID = :p_access_set_id
ORDER BY gl.NAME;
```

### Ledgers com acesso de escrita
```sql
SELECT gl.NAME AS ledger, das.NAME AS access_set
FROM   GL_ACCESS_SET_ASSIGNMENTS asa
JOIN   GL_ACCESS_SETS das ON das.ACCESS_SET_ID = asa.ACCESS_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = asa.LEDGER_ID
WHERE  asa.ACCESS_PRIVILEGE_CODE = 'READ_AND_WRITE';
```

### Filtros comuns
- `ACCESS_PRIVILEGE_CODE = 'READ_ONLY'` — Acesso somente leitura
- `ACCESS_PRIVILEGE_CODE = 'READ_AND_WRITE'` — Acesso de leitura e escrita
- `END_DATE IS NULL` — Atribuições sem data de expiração (permanentes)

---

## Observacoes

- A chave primária é composta por `ACCESS_SET_ID` + `LEDGER_ID` — cada ledger aparece no máximo uma vez por conjunto de acesso.
- O `ACCESS_PRIVILEGE_CODE` controla se o usuário pode apenas consultar dados (`READ_ONLY`) ou também lançar/alterar (`READ_AND_WRITE`).
- Atribuições com `END_DATE` preenchida são temporárias e deixam de valer após a data informada.
- Esta tabela é consultada em tempo real pelo GL para validar se o usuário tem permissão para executar operações em um ledger específico.

---

## Referencias

- [Oracle Docs — GL_ACCESS_SET_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glaccesssetassignments-25064.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL

---

## 🔗 PVOs Relacionados

### [[bsvdataaccesssetassignmentpvo|BsvDataAccessSetAssignmentPVO]] (GL · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_PRIVILEGE_CODE | DasAssignmentAccessPrivilegeCode | — |
| ACCESS_SET_ID | AccessSetId | ✅ |
| CREATED_BY | DasAssignmentCreatedBy | — |
| CREATION_DATE | DasAssignmentCreationDate | — |
| END_DATE | DasAssignmentEndDate | — |
| LAST_UPDATE_DATE | DasAssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DasAssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | DasAssignmentLastUpdatedBy | — |
| LEDGER_ID | LedgerId | ✅ |
| OBJECT_VERSION_NUMBER | DasAssignmentObjectVersionNumber | — |
| PARENT_RECORD_ID | DasAssignmentParentRecordId | — |
| SEGMENT_VALUE | SegmentValue | ✅ |
| START_DATE | DasAssignmentStartDate | — |
