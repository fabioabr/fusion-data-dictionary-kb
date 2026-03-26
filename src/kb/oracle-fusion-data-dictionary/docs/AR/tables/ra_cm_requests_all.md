---
id: DOC-AR-008
doc_type: system-doc
title: "RA_CM_REQUESTS_ALL — Solicitações de Notas de Crédito"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - credit-memo
  - solicitacoes-credito
  - workflow-aprovacao
aliases:
  - RA_CM_REQUESTS_ALL
  - ra_cm_requests_all
  - solicitacoes-credit-memo
  - credit-memo-requests
  - cm-requests-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CM_REQUESTS_ALL

## 📌 Visão Geral

Armazena **solicitações de notas de crédito (credit memo requests)** geradas a partir de disputas comerciais, processos de aprovação ou ajustes em transações do Accounts Receivable. Cada registro representa uma solicitação pendente ou já processada, com valores solicitados, aprovados e o status do workflow de aprovação.

É a tabela de **controle do fluxo de aprovação de créditos** — conecta a transação original à nota de crédito resultante, mantendo rastreabilidade completa do processo.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Workflow de aprovação de créditos:** Rastreamento de solicitações de credit memo desde a criação até a aprovação/rejeição.
- **Disputas comerciais:** Registro de pedidos de estorno originados de reclamações de clientes.
- **Controle de alçadas:** Comparação entre valor solicitado e valor aprovado para análise de governança.
- **Geração automática de credit memos:** Após aprovação, alimenta a criação da nota de crédito em [[ra_customer_trx_all]].
- **Auditoria financeira:** Trilha completa de quem solicitou, quando e por qual motivo.
- **Relatórios gerenciais:** Análise de volume e valor de créditos concedidos por período, cliente e motivo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CM_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação de credit memo | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | Referência | Transação original contra a qual o crédito é solicitado | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | Referência | Linha específica da transação (se aplicável) | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 4 | LINKED_CM_CUSTOMER_TRX_ID | NUMBER(18) | NULL | Referência | Transação de credit memo gerada após aprovação | [[ra_customer_trx_all]] | 🟢 100% |
| 5 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo da solicitação (lookup AR_CREDIT_MEMO_REASON) | — | 🟢 100% |
| 6 | REQUEST_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor total solicitado para crédito | — | 🟢 100% |
| 7 | APPROVED_AMOUNT | NUMBER | NULL | Financeiro | Valor efetivamente aprovado | — | 🟢 100% |
| 8 | LINE_AMOUNT | NUMBER | NULL | Financeiro | Valor referente à linha da transação | — | 🟢 100% |
| 9 | TAX_AMOUNT | NUMBER | NULL | Financeiro | Valor referente a impostos | — | 🟢 100% |
| 10 | FREIGHT_AMOUNT | NUMBER | NULL | Financeiro | Valor referente a frete | — | 🟢 100% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda (ISO 4217) | — | 🟢 100% |
| 12 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da solicitação (PENDING_APPROVAL, APPROVED, REJECTED, COMPLETE) | — | 🟢 100% |
| 13 | APPROVAL_DATE | DATE | NULL | Workflow | Data da aprovação/rejeição | — | 🟢 100% |
| 14 | APPROVER_ID | NUMBER(18) | NULL | Workflow | ID do aprovador (FND_USER ou pessoa de RH) | — | 🟢 100% |
| 15 | REQUESTOR_ID | NUMBER(18) | NULL | Workflow | ID do solicitante | — | 🟢 100% |
| 16 | REQUEST_DATE | DATE | NOT NULL | Workflow | Data da solicitação | — | 🟢 100% |
| 17 | NOTES | VARCHAR2(2000) | NULL | Texto livre | Observações/justificativa da solicitação | — | 🟢 100% |
| 18 | DISPUTE_DATE | DATE | NULL | Workflow | Data de abertura da disputa (se originada de disputa) | — | 🟢 100% |
| 19 | PAYMENT_SCHEDULE_ID | NUMBER(18) | NULL | Referência | Parcela de pagamento associada | [[ar_payment_schedules_all]] | 🟢 100% |
| 20 | CUSTOMER_REASON | VARCHAR2(240) | NULL | Texto livre | Motivo informado pelo cliente | — | 🟢 100% |
| 21 | BATCH_SOURCE_ID | NUMBER(18) | NULL | Configuração | Fonte de transação para o credit memo gerado | [[ra_batch_sources_all]] | 🟢 100% |
| 22 | CUST_TRX_TYPE_ID | NUMBER(18) | NULL | Configuração | Tipo de transação do credit memo a ser gerado | [[ra_cust_trx_types_all]] | 🟢 100% |
| 23 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 24 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 25 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 26 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 27 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 28 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 29 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 30 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (transação original)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha específica)
- [[ar_payment_schedules_all]] — via `PAYMENT_SCHEDULE_ID` (parcela associada)
- [[ra_batch_sources_all]] — via `BATCH_SOURCE_ID` (fonte de transação)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo de transação)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da solicitação de nota de crédito)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `LINKED_CM_CUSTOMER_TRX_ID` (credit memo gerado após aprovação)

---

## 📎 Uso Típico

### Listar solicitações de crédito pendentes de aprovação
```sql
SELECT cmr.CM_REQUEST_ID, ct.TRX_NUMBER, cmr.REASON_CODE,
       cmr.REQUEST_AMOUNT, cmr.CURRENCY_CODE, cmr.REQUEST_DATE
FROM   RA_CM_REQUESTS_ALL cmr
JOIN   RA_CUSTOMER_TRX_ALL ct ON ct.CUSTOMER_TRX_ID = cmr.CUSTOMER_TRX_ID
WHERE  cmr.STATUS = 'PENDING_APPROVAL'
  AND  cmr.ORG_ID = :p_org_id
ORDER BY cmr.REQUEST_DATE;
```

### Análise de créditos aprovados vs. solicitados
```sql
SELECT cmr.REASON_CODE,
       COUNT(*) AS total_solicitacoes,
       SUM(cmr.REQUEST_AMOUNT) AS total_solicitado,
       SUM(cmr.APPROVED_AMOUNT) AS total_aprovado,
       ROUND(SUM(cmr.APPROVED_AMOUNT) / NULLIF(SUM(cmr.REQUEST_AMOUNT), 0) * 100, 2) AS pct_aprovado
FROM   RA_CM_REQUESTS_ALL cmr
WHERE  cmr.STATUS IN ('APPROVED', 'COMPLETE')
  AND  cmr.ORG_ID = :p_org_id
  AND  cmr.APPROVAL_DATE BETWEEN :start_date AND :end_date
GROUP BY cmr.REASON_CODE
ORDER BY total_solicitado DESC;
```

### Filtros comuns
- `STATUS = 'PENDING_APPROVAL'` — Aguardando aprovação
- `STATUS = 'APPROVED'` — Aprovadas
- `STATUS = 'REJECTED'` — Rejeitadas
- `REASON_CODE` — Filtrar por motivo do crédito
- `APPROVAL_DATE BETWEEN :start AND :end` — Período de aprovação

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O campo `LINKED_CM_CUSTOMER_TRX_ID` só é preenchido **após a aprovação e geração efetiva** do credit memo.
- O workflow de aprovação pode ser configurado via **Oracle BPM** com regras de alçada baseadas em valor e motivo.
- Solicitações rejeitadas permanecem na tabela com `STATUS = 'REJECTED'` para fins de auditoria — não são excluídas.
- A diferença entre `REQUEST_AMOUNT` e `APPROVED_AMOUNT` indica ajustes feitos pelo aprovador (aprovação parcial).

---

## 📚 Referências

- [Oracle Docs — RA_CM_REQUESTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racmrequestsall-25087.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
