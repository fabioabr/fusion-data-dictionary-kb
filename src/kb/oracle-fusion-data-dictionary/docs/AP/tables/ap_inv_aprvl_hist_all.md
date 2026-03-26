---
id: DOC-AP-015
doc_type: system-doc
title: "AP_INV_APRVL_HIST_ALL — Histórico de Aprovação de Faturas"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - aprovacao
  - approval-history
  - workflow
aliases:
  - AP_INV_APRVL_HIST_ALL
  - ap_inv_aprvl_hist_all
  - historico-aprovacao-ap
  - approval-history-ap
  - aprovacao-faturas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INV_APRVL_HIST_ALL

## 📌 Visão Geral

Armazena o **histórico de aprovação** de faturas do módulo Accounts Payable. Cada registro representa uma ação no workflow de aprovação (submissão, aprovação, rejeição, escalonamento), contendo o aprovador, a data da ação, o status resultante e comentários. Permite rastrear todo o fluxo de aprovação de uma fatura desde a submissão até a decisão final.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Trilha de auditoria:** Registro completo de todas as ações de aprovação realizadas em cada fatura.
- **Compliance:** Evidência de que faturas foram aprovadas por pessoas autorizadas antes do pagamento.
- **Análise de gargalos:** Identificação de etapas que demoram no processo de aprovação.
- **Escalonamento:** Rastreamento de faturas que foram escalonadas no workflow de aprovação.
- **Relatórios gerenciais:** Base para dashboards de tempo médio de aprovação e taxa de rejeição.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPROVAL_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de aprovação | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(18) | NOT NULL | FK | Fatura associada | [[ap_invoices_all]] | 🟢 100% |
| 3 | ITERATION | NUMBER | NULL | Controle | Número da iteração de aprovação (resubmissões) | — | 🟢 100% |
| 4 | RESPONSE | VARCHAR2(80) | NULL | Classificação | Ação tomada (APPROVE/REJECT/ESCALATE/REQUEST_INFO/etc.) | — | 🟢 100% |
| 5 | APPROVER_ID | NUMBER(18) | NULL | Aprovador | ID do aprovador (person) | [[per_all_people_f]] | 🟢 100% |
| 6 | APPROVER_NAME | VARCHAR2(240) | NULL | Aprovador | Nome do aprovador | — | 🟡 75% |
| 7 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Status | Status resultante (WFAPPROVED/REJECTED/MANUALLY APPROVED/etc.) | — | 🟢 100% |
| 8 | AMOUNT_APPROVED | NUMBER | NULL | Financeiro | Valor aprovado (pode diferir do valor total em aprovações parciais) | — | 🟡 75% |
| 9 | NOTIFICATION_ID | NUMBER(18) | NULL | Workflow | ID da notificação do workflow | — | 🟡 70% |
| 10 | LINE_NUMBER | NUMBER | NULL | Referência cruzada | Número da linha da fatura (se aprovação por linha) | [[ap_invoice_lines_all]] | 🟢 100% |
| 11 | HIST_TYPE | VARCHAR2(25) | NULL | Classificação | Tipo do histórico (APRVLACTION/LINESAPRVL/HOLDRELEASE) | — | 🟢 100% |
| 12 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários do aprovador | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ação de aprovação | — | 🟢 100% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário do sistema que criou o registro | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 18 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura à qual o histórico de aprovação se refere)
- [[ap_invoice_lines_all]] — via `INVOICE_ID` + `LINE_NUMBER` (linha da fatura, quando aplicável)
- [[per_all_people_f]] — via `APPROVER_ID` (pessoa responsável pela aprovação da fatura)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do histórico de aprovação)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha direta conhecida.

---

## 📎 Uso Típico

### Histórico de aprovação de uma fatura
```sql
SELECT aah.ITERATION, aah.RESPONSE, aah.APPROVER_NAME,
       aah.APPROVAL_STATUS, aah.COMMENTS,
       aah.CREATION_DATE AS data_acao
FROM   AP_INV_APRVL_HIST_ALL aah
WHERE  aah.INVOICE_ID = :p_invoice_id
ORDER BY aah.CREATION_DATE;
```

### Faturas rejeitadas no período
```sql
SELECT ai.INVOICE_NUM, ai.INVOICE_AMOUNT, aah.APPROVER_NAME,
       aah.COMMENTS, aah.CREATION_DATE
FROM   AP_INV_APRVL_HIST_ALL aah
JOIN   AP_INVOICES_ALL ai ON ai.INVOICE_ID = aah.INVOICE_ID
WHERE  aah.RESPONSE = 'REJECT'
  AND  aah.CREATION_DATE BETWEEN :start_date AND :end_date
  AND  aah.ORG_ID = :p_org_id;
```

### Filtros comuns
- `RESPONSE = 'APPROVE'` — Ações de aprovação
- `RESPONSE = 'REJECT'` — Ações de rejeição
- `HIST_TYPE = 'APRVLACTION'` — Ações do workflow de aprovação
- `ITERATION = (SELECT MAX...)` — Última iteração de aprovação

---

## 🔒 Observações

- O campo `ITERATION` incrementa a cada vez que a fatura é resubmetida ao workflow, permitindo identificar quantas rodadas de aprovação foram necessárias.
- O campo `RESPONSE` contém a ação tomada: **APPROVE** (aprovar), **REJECT** (rejeitar), **ESCALATE** (escalar), **REQUEST_INFO** (solicitar informação).
- O campo `HIST_TYPE` diferencia tipos de ações: **APRVLACTION** (ação no workflow), **LINESAPRVL** (aprovação por linha), **HOLDRELEASE** (liberação de hold).
- A coluna `LINE_NUMBER` é preenchida quando a aprovação é feita por linha individual da fatura (line-level approval).
- Esta tabela é apenas de inserção (append-only) — registros não são alterados após criação.

---

## 📚 Referências

- [Oracle Docs — AP_INV_APRVL_HIST_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvaprvlhistall-25758.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
