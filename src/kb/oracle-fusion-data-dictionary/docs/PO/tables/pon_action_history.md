---
id: DOC-PO-002
doc_type: system-doc
title: "PON_ACTION_HISTORY — Histórico de Ações em Negociações"
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
  - action-history
  - auditoria
aliases:
  - PON_ACTION_HISTORY
  - pon_action_history
  - historico-acoes-negociacao
  - sourcing-action-history
  - audit-trail-sourcing
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_ACTION_HISTORY

## Visão Geral

Armazena o **histórico completo de ações** executadas em negociações do módulo Oracle Sourcing. Cada registro representa uma ação de workflow (criação, submissão, aprovação, rejeição, cancelamento, etc.) realizada por um usuário ou processo automático sobre uma negociação, fornecendo trilha de auditoria completa.

> [!note] Módulo Sourcing (PON)
> O prefixo `PON` identifica tabelas do módulo **Procurement Sourcing** (Oracle Negotiation). Esta tabela é a principal fonte de auditoria para o ciclo de vida das negociações.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de negociações:** Trilha completa de todas as ações realizadas em cada negociação.
- **Workflow de aprovação:** Registro de quem aprovou/rejeitou em cada etapa do fluxo.
- **Compliance regulatório:** Evidência de segregação de funções e controles de acesso.
- **Análise de ciclo de vida:** Medição de tempo entre ações (criação→submissão→aprovação→publicação).
- **Troubleshooting:** Diagnóstico de negociações travadas ou em estado inconsistente.
- **Relatórios gerenciais:** Dashboards de volume e tempo de processamento por aprovador.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de ação | — | 🟢 90% |
| 2 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do objeto (negociação) associado | [[pon_auction_headers_all]] | 🟢 90% |
| 3 | OBJECT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do objeto: NEGOTIATION, AMENDMENT, etc. | — | 🟢 85% |
| 4 | SEQUENCE_NUM | NUMBER | NOT NULL | Controle | Número de sequência da ação dentro da negociação | — | 🟢 85% |
| 5 | ACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da ação: SUBMIT, APPROVE, REJECT, CANCEL, PUBLISH, AWARD, CLOSE | — | 🟢 90% |
| 6 | ACTION_DATE | DATE | NOT NULL | Data | Data/hora da execução da ação | — | 🟢 95% |
| 7 | ACTION_USER_ID | NUMBER(18) | NULL | FK | Usuário que executou a ação | [[per_all_people_f]] | 🟢 85% |
| 8 | ACTION_USER_NAME | VARCHAR2(100) | NULL | Identificação | Nome do usuário que executou a ação (desnormalizado) | — | 🟡 75% |
| 9 | ACTION_NOTE | VARCHAR2(4000) | NULL | Texto livre | Nota/comentário associado à ação | — | 🟢 85% |
| 10 | FROM_STATUS_CODE | VARCHAR2(30) | NULL | Status | Status anterior à ação | — | 🟢 85% |
| 11 | TO_STATUS_CODE | VARCHAR2(30) | NULL | Status | Status resultante após a ação | — | 🟢 85% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER | NULL | Controle | Número da versão do objeto (controle de concorrência) | — | 🟢 90% |
| 13 | AUCTION_HEADER_ID | NUMBER(18) | NULL | FK | Referência direta ao cabeçalho da negociação | [[pon_auction_headers_all]] | 🟢 90% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `OBJECT_ID` / `AUCTION_HEADER_ID` (negociação à qual a ação de histórico se refere)
- [[per_all_people_f]] — via `ACTION_USER_ID` (usuário que executou a ação)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida — tabela terminal de registro de auditoria.

---

## Uso Típico

### Histórico completo de uma negociação
```sql
SELECT ah.SEQUENCE_NUM, ah.ACTION_TYPE, ah.ACTION_DATE,
       ah.ACTION_USER_NAME, ah.ACTION_NOTE,
       ah.FROM_STATUS_CODE, ah.TO_STATUS_CODE
FROM   PON_ACTION_HISTORY ah
WHERE  ah.OBJECT_ID = :p_auction_header_id
ORDER BY ah.SEQUENCE_NUM;
```

### Tempo médio de aprovação
```sql
SELECT AVG(approve.ACTION_DATE - submit.ACTION_DATE) AS dias_aprovacao
FROM   PON_ACTION_HISTORY submit
JOIN   PON_ACTION_HISTORY approve
  ON   submit.OBJECT_ID = approve.OBJECT_ID
WHERE  submit.ACTION_TYPE = 'SUBMIT'
  AND  approve.ACTION_TYPE = 'APPROVE';
```

### Filtros comuns
- `ACTION_TYPE = 'APPROVE'` — Ações de aprovação
- `ACTION_TYPE = 'REJECT'` — Rejeições
- `ACTION_TYPE = 'SUBMIT'` — Submissões para aprovação
- `OBJECT_TYPE_CODE = 'NEGOTIATION'` — Ações sobre negociações (excluindo amendments)

---

## Observações

- A tabela funciona como **audit trail** imutável — registros não são deletados ou alterados após a criação.
- O campo `SEQUENCE_NUM` garante a ordenação cronológica dentro de uma mesma negociação.
- Os campos `FROM_STATUS_CODE` e `TO_STATUS_CODE` permitem reconstruir a máquina de estados da negociação.
- O `ACTION_USER_NAME` é desnormalizado para performance em relatórios; o `ACTION_USER_ID` é a referência canônica.
- Negociações com amendments geram registros adicionais com `OBJECT_TYPE_CODE = 'AMENDMENT'`.

---

## Referências

- [Oracle Docs — PON_ACTION_HISTORY](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponactionhistory.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
