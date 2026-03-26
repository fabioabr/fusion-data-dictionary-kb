---
id: DOC-AR-053
doc_type: system-doc
title: "AR_APPROVAL_ACTION_HISTORY — Histórico de Ações de Aprovação"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, aprovacao, historico, auditoria]
aliases: [AR_APPROVAL_ACTION_HISTORY, ar_approval_action_history, approval_action_history, historico_aprovacao_ar, ar_approval_hist]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_APPROVAL_ACTION_HISTORY

## 📌 Visão Geral

Tabela que registra o **histórico de ações de aprovação** sobre transações e ajustes do AR. Cada registro documenta uma ação tomada (aprovação, rejeição, delegação) por um aprovador, incluindo data, comentários e valor aprovado.

## 🧠 Propósito de Negócio

Esta tabela é o **log de auditoria** do fluxo de aprovações no AR. Fundamental para compliance e rastreabilidade — permite responder "quem aprovou o quê, quando e por quê" para qualquer ajuste ou transação que tenha passado por workflow de aprovação.

Casos de uso principais:
- Trilha de auditoria para ajustes de saldo
- Rastreamento de aprovações de write-off
- Compliance regulatório (SOX, auditorias)
- Análise de SLA de aprovação

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | APPROVAL_ACTION_HISTORY_ID | NUMBER | PK. Identificador único do registro de ação de aprovação. | Chave | 🟢 100% |
| 2 | ADJUSTMENT_ID | NUMBER | FK para [[ar_adjustments_all]]. Ajuste sendo aprovado (nulo se não for ajuste). | Chave Estrangeira | 🟢 100% |
| 3 | ACTION_DATE | DATE | Data e hora em que a ação foi executada. | Temporal | 🟢 100% |
| 4 | ACTION_NAME | VARCHAR2 | Nome da ação: `APPROVE`, `REJECT`, `DELEGATE`, `SUBMIT`, `RETURN`. | Classificação | 🟢 100% |
| 5 | APPROVER_ID | NUMBER | FK para o usuário aprovador. Referencia [[per_all_people_f]] ou [[fnd_user]]. | Chave Estrangeira | 🟢 100% |
| 6 | COMMENTS | VARCHAR2 | Comentários do aprovador sobre a ação. | Informação | 🟢 100% |
| 7 | STATUS | VARCHAR2 | Status resultante da ação: `APPROVED`, `REJECTED`, `PENDING`, etc. | Controle | 🟢 100% |
| 8 | AMOUNT_APPROVED | NUMBER | Valor aprovado (pode diferir do valor solicitado). | Financeiro | 🟢 100% |
| 9 | ORG_ID | NUMBER | Identificador da Business Unit. | Partição | 🟢 100% |
| 10 | CUSTOMER_TRX_ID | NUMBER | FK para [[ra_customer_trx_all]]. Transação associada (se aplicável). | Chave Estrangeira | 🟢 100% |
| 11 | APPROVAL_LEVEL | NUMBER | Nível na hierarquia de aprovação. | Workflow | 🟢 100% |
| 12 | NOTIFICATION_ID | NUMBER | ID da notificação de workflow associada. | Workflow | 🟢 100% |
| 13 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 14 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_adjustments_all]] | ADJUSTMENT_ID | FK | Ajuste sendo aprovado |
| [[ra_customer_trx_all]] | CUSTOMER_TRX_ID | FK | Transação associada |
| [[per_all_people_f]] | APPROVER_ID | FK | Pessoa aprovadora |
| [[hr_operating_units]] | ORG_ID | Referência | Business Unit |

## 📎 Uso Típico

```sql
-- Histórico de aprovações de um ajuste
SELECT aah.action_date,
       aah.action_name,
       aah.status,
       aah.amount_approved,
       aah.comments,
       aah.approver_id
  FROM ar_approval_action_history aah
 WHERE aah.adjustment_id = :p_adjustment_id
 ORDER BY aah.action_date;
```

```sql
-- Ajustes pendentes de aprovação por BU
SELECT aah.adjustment_id,
       adj.amount,
       aah.action_date,
       aah.approver_id
  FROM ar_approval_action_history aah
  JOIN ar_adjustments_all adj ON adj.adjustment_id = aah.adjustment_id
 WHERE aah.status = 'PENDING'
   AND aah.org_id = :p_org_id;
```

## 🔒 Observações

- Esta tabela é **append-only** por natureza — registros de histórico não devem ser atualizados ou excluídos.
- O campo `ACTION_NAME` segue os valores padrão do Oracle Approvals Management (AME).
- `AMOUNT_APPROVED` pode ser menor que o valor solicitado em caso de aprovação parcial.
- Em ambientes com SOX compliance, esta tabela é frequentemente incluída em relatórios de auditoria para evidenciar segregação de funções.
- Registros com `ADJUSTMENT_ID` nulo podem estar associados a outros tipos de aprovação (ex: credit memos, write-offs de transações).

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Approval Action History View Object
- Oracle Fusion Cloud — Receivables Approval Workflows (AME Guide)
