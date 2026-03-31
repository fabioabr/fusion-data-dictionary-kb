---
id: DOC-AP-035
doc_type: system-doc
title: "EXM_EXPENSE_REPORTS — Relatórios de Despesa (Cabeçalho)"
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
  - relatorios-despesa
  - expense-reports
  - reembolso
aliases:
  - EXM_EXPENSE_REPORTS
  - exm_expense_reports
  - relatorios-despesa-exm
  - exm-expense-reports
  - expense-report-headers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_REPORTS

## 📌 Visão Geral

Armazena os **cabeçalhos de relatórios de despesa** (Expense Reports) do módulo Expense Management. Cada registro representa um relatório submetido por um funcionário para reembolso de despesas corporativas, contendo informações gerais como data, propósito da viagem, status de aprovação, totais e referência ao funcionário solicitante.

> [!note] Ciclo de vida
> O relatório de despesa passa pelas fases: rascunho → submetido → em aprovação → aprovado → pago. O status é rastreado nesta tabela.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Solicitação de reembolso:** Agrupamento de despesas individuais em um relatório formal para aprovação.
- **Workflow de aprovação:** Controle do ciclo de aprovação hierárquica ou por políticas.
- **Geração de fatura de reembolso:** Após aprovação, o relatório gera uma fatura em [[ap_invoices_all]] para pagamento.
- **Controle de adiantamentos:** Vinculação a cash advances (adiantamentos) já concedidos ao funcionário.
- **Análise de gastos corporativos:** Base para dashboards de despesas por funcionário, departamento e período.
- **Compliance e auditoria:** Rastreamento de aprovações, políticas violadas e exceções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_REPORT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do relatório de despesa | — | 🟢 95% |
| 2 | EXPENSE_REPORT_NUM | VARCHAR2(50) | NOT NULL | Identificação | Número do relatório de despesa visível ao usuário | — | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Funcionário que submeteu o relatório | [[per_person_names_f_v]] | 🟢 95% |
| 4 | EXPENSE_TEMPLATE_ID | NUMBER(18) | NULL | FK | Template de despesa utilizado | [[exm_expense_templates]] | 🟡 75% |
| 5 | PURPOSE | VARCHAR2(240) | NULL | Texto livre | Propósito/finalidade do relatório (ex: "Viagem São Paulo — reunião cliente") | — | 🟢 90% |
| 6 | EXPENSE_STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status do relatório: SAVED, SUBMITTED, MGRPAYAPPR, INVOICED, PAID, etc. | — | 🟢 95% |
| 7 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Classificação | Status de aprovação: APPROVED, REJECTED, PENDING, etc. | — | 🟢 85% |
| 8 | REPORT_SUBMIT_DATE | DATE | NULL | Data | Data de submissão do relatório | — | 🟢 90% |
| 9 | EXPENSE_REPORT_DATE | DATE | NOT NULL | Data | Data do relatório (informada pelo funcionário) | — | 🟢 90% |
| 10 | TOTAL | NUMBER | NULL | Financeiro | Valor total do relatório na moeda de reembolso | — | 🟢 95% |
| 11 | REIMBURSEMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda de reembolso | — | 🟢 90% |
| 12 | ACCTD_TOTAL | NUMBER | NULL | Financeiro | Valor total na moeda funcional | — | 🟡 75% |
| 13 | AMOUNT_DUE_EMPLOYEE | NUMBER | NULL | Financeiro | Valor devido ao funcionário (descontados adiantamentos) | — | 🟢 85% |
| 14 | AMOUNT_DUE_CCARD_COMPANY | NUMBER | NULL | Financeiro | Valor devido à empresa de cartão corporativo | — | 🟢 85% |
| 15 | ADVANCE_AMOUNT_APPLIED | NUMBER | NULL | Financeiro | Valor de adiantamento abatido | — | 🟡 80% |
| 16 | OVERRIDE_APPROVER_ID | NUMBER(18) | NULL | FK | Aprovador substituto designado | [[per_person_names_f_v]] | 🟡 75% |
| 17 | COST_CENTER | VARCHAR2(25) | NULL | Contabilidade | Centro de custo padrão do relatório | — | 🟡 80% |
| 18 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização do funcionário | [[hr_locations]] | 🟡 75% |
| 19 | INVOICE_ID | NUMBER(18) | NULL | FK | Fatura de reembolso gerada | [[ap_invoices_all]] | 🟢 85% |
| 20 | POLICY_VIOLATION_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se houve violação de política (Y/N) | — | 🟡 75% |
| 21 | RECEIPTS_STATUS | VARCHAR2(30) | NULL | Classificação | Status de comprovantes: REQUIRED, RECEIVED, WAIVED | — | 🟡 70% |
| 22 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_person_names_f_v]] — via `PERSON_ID` (funcionário solicitante)
- [[exm_expense_templates]] — via `EXPENSE_TEMPLATE_ID` (template utilizado)
- [[hr_locations]] — via `LOCATION_ID` (localização do funcionário)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura de reembolso gerada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do relatório de despesas)

### Tabelas-filha (FK de saída)
- [[exm_expenses]] — via `EXPENSE_REPORT_ID` (linhas de despesa do relatório)
- [[exm_expense_dists]] — via `EXPENSE_REPORT_ID` (distribuições contábeis)

---

## 📎 Uso Típico

### Relatórios de despesa por funcionário e status
```sql
SELECT er.EXPENSE_REPORT_NUM, er.PURPOSE, er.EXPENSE_REPORT_DATE,
       er.TOTAL, er.REIMBURSEMENT_CURRENCY_CODE,
       er.EXPENSE_STATUS_CODE
FROM   EXM_EXPENSE_REPORTS er
WHERE  er.PERSON_ID = :p_person_id
ORDER BY er.EXPENSE_REPORT_DATE DESC;
```

### Total de despesas aprovadas por período
```sql
SELECT SUM(er.TOTAL) AS total_aprovado,
       COUNT(*) AS qtd_relatorios
FROM   EXM_EXPENSE_REPORTS er
WHERE  er.EXPENSE_STATUS_CODE IN ('MGRPAYAPPR', 'INVOICED', 'PAID')
  AND  er.EXPENSE_REPORT_DATE BETWEEN :start_date AND :end_date
  AND  er.ORG_ID = :p_org_id;
```

### Relatórios com violação de política
```sql
SELECT er.EXPENSE_REPORT_NUM, er.PURPOSE, er.TOTAL,
       p.DISPLAY_NAME AS funcionario
FROM   EXM_EXPENSE_REPORTS er
JOIN   PER_PERSON_NAMES_F_V p ON p.PERSON_ID = er.PERSON_ID
WHERE  er.POLICY_VIOLATION_FLAG = 'Y'
  AND  er.ORG_ID = :p_org_id;
```

### Filtros comuns
- `EXPENSE_STATUS_CODE = 'SUBMITTED'` — Relatórios submetidos (pendentes de aprovação)
- `EXPENSE_STATUS_CODE = 'MGRPAYAPPR'` — Aprovados pelo gestor
- `EXPENSE_STATUS_CODE = 'PAID'` — Reembolsados
- `POLICY_VIOLATION_FLAG = 'Y'` — Com violação de política

---

## 🔒 Observações

- O ciclo de vida do relatório é: **SAVED** (rascunho) → **SUBMITTED** (submetido) → **MGRPAYAPPR** (aprovado) → **INVOICED** (fatura gerada) → **PAID** (pago).
- Quando aprovado, o sistema gera automaticamente uma fatura em [[ap_invoices_all]], cujo `INVOICE_ID` é gravado nesta tabela.
- O campo `AMOUNT_DUE_EMPLOYEE` desconta qualquer adiantamento (`ADVANCE_AMOUNT_APPLIED`) do total.
- `AMOUNT_DUE_CCARD_COMPANY` é usado quando a empresa paga diretamente à operadora de cartão corporativo.
- O `OVERRIDE_APPROVER_ID` permite designar um aprovador diferente do gestor hierárquico.

---

## 🔗 PVOs Relacionados

### [[corporatecardtransactionpvo|CorporateCardTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_CASH_ADV_FLAG | ExpHdrApplyCashAdvFlag | — |
| ASSIGNMENT_ID | ExpHdrAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpHdrAttributeCategory2 | — |
| AUDIT_CODE | ExpHdrAuditCode | — |
| AUDIT_PRIOR_MGR_STATUS_CODE | ExpHdrAuditPriorMgrStatusCode | — |
| AUDIT_RETURN_REASON_CODE | ExpHdrAuditReturnReasonCode | — |
| AWT_GROUP_ID | ExpHdrAwtGroupId1 | — |
| BOTHPAY_FLAG | ExpHdrBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpHdrCashExpensePaidDate | — |
| CREATED_BY | ExpHdrCreatedBy2 | — |
| CREATION_DATE | ExpHdrCreationDate2 | — |
| CURRENT_APPROVER_ID | ExpHdrCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpHdrExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpHdrExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpHdrExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpHdrExpenseReportNum | — |
| EXPENSE_REPORT_TOTAL | ExpHdrExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpHdrExpenseStatusCode | — |
| EXPENSE_STATUS_DATE | ExpHdrExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpHdrExportRejectCode | — |
| EXPORT_REQUEST_ID | ExpHdrExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpHdrFinalApprovalDate | — |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ExpHdrImagedReceiptsReceivedDate | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrImagedReceiptsStatusCode | — |
| LAST_AUDIT_BY | ExpHdrLastAuditBy | — |
| LAST_UPDATE_DATE | ExpHdrLastUpdateDate2 | — |
| LAST_UPDATE_LOGIN | ExpHdrLastUpdateLogin2 | — |
| LAST_UPDATED_BY | ExpHdrLastUpdatedBy2 | — |
| MISSING_IMAGES_REASON | ExpHdrMissingImagesReason | — |
| OBJECT_VERSION_NUMBER | ExpHdrObjectVersionNumber3 | — |
| ORG_ID | ExpHdrOrgId | — |
| OVERDUE_RCPT_CORRELATION_ID | ExpHdrOverdueRcptCorrelationId | — |
| OVERRIDE_APPROVER_ID | ExpHdrOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrParentExpenseReportId | — |
| PAYMENT_HOLD_CORRELATION_ID | ExpHdrPaymentHoldCorrelationId | — |
| PAYMENT_METHOD_CODE | ExpHdrPaymentMethodCode | — |
| PERSON_ID | ExpHdrPersonId | — |
| PREPARER_ID | ExpHdrPreparerId1 | — |
| PURPOSE | ExpHdrPurpose | — |
| RECEIPTS_FILING_NUMBER | ExpHdrReceiptsFilingNumber | — |
| RECEIPTS_RECEIVED_DATE | ExpHdrReceiptsReceivedDate | — |
| RECEIPTS_STATUS_CODE | ExpHdrReceiptsStatusCode | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrReimbursementCurrencyCode1 | — |
| REPORT_CREATION_METHOD_CODE | ExpHdrReportCreationMethodCode | — |
| REPORT_SUBMIT_DATE | ExpHdrReportSubmitDate | — |
| SHORTPAY_TYPE_CODE | ExpHdrShortpayTypeCode | — |
| TRIP_ID | ExpHdrTripId | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrUnappliedAdvancesJust | — |
| UNAPPLIED_CASH_ADV_REASON | ExpHdrUnappliedCashAdvReason | — |
| WORKFLOW_CORRELATION_ID | ExpHdrWorkflowCorrelationId | — |

### [[expenseattendeedetailspvo|ExpenseAttendeeDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER · BICC: 21/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_CASH_ADV_FLAG | ExpHdrApplyCashAdvFlag | — |
| ASSIGNMENT_ID | ExpHdrAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpHdrAttributeCategory2 | — |
| AUDIT_CODE | ExpHdrAuditCode | ✅ |
| AUDIT_RETURN_REASON_CODE | ExpHdrAuditReturnReasonCode | ✅ |
| AWT_GROUP_ID | ExpHdrAwtGroupId | — |
| BOTHPAY_FLAG | ExpHdrBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpHdrCashExpensePaidDate | ✅ |
| CREATED_BY | ExpHdrCreatedBy | ✅ |
| CREATION_DATE | ExpHdrCreationDate | ✅ |
| CURRENT_APPROVER_ID | ExpHdrCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpHdrExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpHdrExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpHdrExpenseReportDate | ✅ |
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | — |
| EXPENSE_REPORT_ID | ExpHdrPrntExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpHdrExpenseReportNum | ✅ |
| EXPENSE_REPORT_NUM | ExpHdrPrntExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpHdrExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpHdrExpenseStatusCode | ✅ |
| EXPENSE_STATUS_DATE | ExpHdrExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpHdrExportRejectCode | — |
| EXPORT_REQUEST_ID | ExpHdrExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpHdrFinalApprovalDate | ✅ |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ExpHdrImagedReceiptsReceivedDate | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrImagedReceiptsStatusCode | ✅ |
| LAST_AUDIT_BY | ExpHdrLastAuditBy | — |
| LAST_UPDATE_DATE | ExpHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpHdrLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpHdrLastUpdatedBy | ✅ |
| MISSING_IMAGES_REASON | ExpHdrMissingImagesReason | — |
| OBJECT_VERSION_NUMBER | ExpHdrObjectVersionNumber | — |
| ORG_ID | ExpHdrOrgId | — |
| OVERDUE_RCPT_CORRELATION_ID | ExpHdrOverdueRcptCorrelationId | — |
| OVERRIDE_APPROVER_ID | ExpHdrOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrParentExpenseReportId | — |
| PAYMENT_HOLD_CORRELATION_ID | ExpHdrPaymentHoldCorrelationId | — |
| PAYMENT_METHOD_CODE | ExpHdrPaymentMethodCode | ✅ |
| PERSON_ID | ExpHdrPersonId | — |
| PREPARER_ID | ExpHdrPreparerId | — |
| PURPOSE | ExpHdrPurpose | ✅ |
| RECEIPTS_FILING_NUMBER | ExpHdrReceiptsFilingNumber | ✅ |
| RECEIPTS_RECEIVED_DATE | ExpHdrReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ExpHdrReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | FullExpHdrReportCMC | — |
| REPORT_SUBMIT_DATE | ExpHdrReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ExpHdrShortpayTypeCode | ✅ |
| TRIP_ID | ExpHdrTripId | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrUnappliedAdvancesJust | — |
| UNAPPLIED_CASH_ADV_REASON | ExpHdrUnappliedCashAdvReason | — |
| WORKFLOW_CORRELATION_ID | ExpHdrWorkflowCorrelationId | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 31/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | ExpHdrAssignmentId | — |
| ASSIGNMENT_ID | ExpHdrPrntAssignmentId | — |
| ATTRIBUTE_CHAR1 | ExpHdrAttributeChar1 | — |
| ATTRIBUTE_CHAR1 | ExpHdrPrntAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpHdrAttributeChar10 | — |
| ATTRIBUTE_CHAR10 | ExpHdrPrntAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpHdrAttributeChar11 | — |
| ATTRIBUTE_CHAR11 | ExpHdrPrntAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpHdrAttributeChar12 | — |
| ATTRIBUTE_CHAR12 | ExpHdrPrntAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpHdrAttributeChar13 | — |
| ATTRIBUTE_CHAR13 | ExpHdrPrntAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpHdrAttributeChar14 | — |
| ATTRIBUTE_CHAR14 | ExpHdrPrntAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpHdrAttributeChar15 | — |
| ATTRIBUTE_CHAR15 | ExpHdrPrntAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpHdrAttributeChar2 | — |
| ATTRIBUTE_CHAR2 | ExpHdrPrntAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpHdrAttributeChar3 | — |
| ATTRIBUTE_CHAR3 | ExpHdrPrntAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpHdrAttributeChar4 | — |
| ATTRIBUTE_CHAR4 | ExpHdrPrntAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpHdrAttributeChar5 | — |
| ATTRIBUTE_CHAR5 | ExpHdrPrntAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpHdrAttributeChar6 | — |
| ATTRIBUTE_CHAR6 | ExpHdrPrntAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpHdrAttributeChar7 | — |
| ATTRIBUTE_CHAR7 | ExpHdrPrntAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpHdrAttributeChar8 | — |
| ATTRIBUTE_CHAR8 | ExpHdrPrntAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpHdrAttributeChar9 | — |
| ATTRIBUTE_CHAR9 | ExpHdrPrntAttributeChar9 | — |
| AUDIT_CODE | ExpHdrAuditCode | ✅ |
| AUDIT_CODE | ExpHdrPrntAuditCode | — |
| AUDIT_RETURN_REASON_CODE | ExpHdrAuditReturnReasonCode | ✅ |
| AUDIT_RETURN_REASON_CODE | ExpHdrPrntAuditReturnReasonCode | — |
| AWT_GROUP_ID | ExpHdrAwtGroupId | — |
| AWT_GROUP_ID | ExpHdrPrntAwtGroupId | — |
| BOTHPAY_FLAG | ExpHdrBothpayFlag | — |
| BOTHPAY_FLAG | ExpHdrPrntBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpHdrCashExpensePaidDate | ✅ |
| CREATED_BY | ExpHdrCreatedBy | ✅ |
| CREATED_BY | ExpHdrPrntCreatedBy | — |
| CREATION_DATE | ExpHdrCreationDate | ✅ |
| CURRENT_APPROVER_ID | ExpHdrCurrentApproverId | ✅ |
| CURRENT_APPROVER_ID | ExpHdrPrntCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpHdrExchangeRateType | ✅ |
| EXCHANGE_RATE_TYPE | ExpHdrPrntExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpHdrExpRepProcessingId | — |
| EXP_REP_PROCESSING_ID | ExpHdrPrntExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpHdrExpenseReportDate | ✅ |
| EXPENSE_REPORT_DATE | ExpHdrPrntExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | ✅ |
| EXPENSE_REPORT_ID | ExpHdrPrntExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpHdrExpenseReportNum | ✅ |
| EXPENSE_REPORT_NUM | ExpHdrPrntExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpHdrExpenseReportTotal | ✅ |
| EXPENSE_REPORT_TOTAL | ExpHdrPrntExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpHdrExpenseStatusCode | ✅ |
| EXPENSE_STATUS_CODE | ExpHdrPrntExpenseStatusCode | — |
| EXPENSE_STATUS_DATE | ExpHdrExpenseStatusDate | ✅ |
| EXPENSE_STATUS_DATE | ExpHdrPrntExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpHdrExportRejectCode | — |
| EXPORT_REJECT_CODE | ExpHdrPrntExportRejectCode | — |
| EXPORT_REQUEST_ID | ExpHdrExportRequestId | — |
| EXPORT_REQUEST_ID | ExpHdrPrntExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpHdrFinalApprovalDate | ✅ |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrHoldingExpenseReportId | — |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrPrntHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrImagedReceiptsStatusCode | ✅ |
| LAST_AUDIT_BY | ExpHdrLastAuditBy | — |
| LAST_AUDIT_BY | ExpHdrPrntLastAuditBy | — |
| LAST_UPDATE_DATE | ExpHdrLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ExpHdrPrntLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpHdrLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ExpHdrPrntLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpHdrLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ExpHdrPrntLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpHdrPrntObjectVersionNumber | — |
| ORG_ID | ExpHdrOrgId | ✅ |
| ORG_ID | ExpHdrPrntOrgId | — |
| OVERRIDE_APPROVER_ID | ExpHdrOverrideApproverId | ✅ |
| OVERRIDE_APPROVER_ID | ExpHdrPrntOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrParentExpenseReportId | ✅ |
| PARENT_EXPENSE_REPORT_ID | ExpHdrPrntParentExpenseReportId | — |
| PAYMENT_METHOD_CODE | ExpHdrPaymentMethodCode | ✅ |
| PERSON_ID | ExpHdrPersonId | ✅ |
| PERSON_ID | ExpHdrPrntPersonId | — |
| PREPARER_ID | ExpHdrPreparerId | — |
| PREPARER_ID | ExpHdrPrntPreparerId | — |
| PURPOSE | ExpHdrPrntPurpose | — |
| PURPOSE | ExpHdrPurpose | ✅ |
| RECEIPTS_FILING_NUMBER | ExpHdrPrntReceiptsFilingNumber | — |
| RECEIPTS_FILING_NUMBER | ExpHdrReceiptsFilingNumber | ✅ |
| RECEIPTS_RECEIVED_DATE | ExpHdrPrntReceiptsReceivedDate | — |
| RECEIPTS_RECEIVED_DATE | ExpHdrReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ExpHdrPrntReceiptsStatusCode | — |
| RECEIPTS_STATUS_CODE | ExpHdrReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrPrntReimbursementCurrencyCode | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | FullReportCMC | — |
| REPORT_SUBMIT_DATE | ExpHdrPrntReportSubmitDate | — |
| REPORT_SUBMIT_DATE | ExpHdrReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ExpHdrPrntShortpayTypeCode | — |
| SHORTPAY_TYPE_CODE | ExpHdrShortpayTypeCode | ✅ |
| UNAPPLIED_ADVANCES_JUST | ExpHdrPrntUnappliedAdvancesJust | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrUnappliedAdvancesJust | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 25/112)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | ExpHdrAssignmentId | — |
| ASSIGNMENT_ID | ExpHdrPrntAssignmentId | — |
| ATTRIBUTE_CHAR1 | ExpHdrAttributeChar1 | — |
| ATTRIBUTE_CHAR1 | ExpHdrPrntAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpHdrAttributeChar10 | — |
| ATTRIBUTE_CHAR10 | ExpHdrPrntAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpHdrAttributeChar11 | — |
| ATTRIBUTE_CHAR11 | ExpHdrPrntAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpHdrAttributeChar12 | — |
| ATTRIBUTE_CHAR12 | ExpHdrPrntAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpHdrAttributeChar13 | — |
| ATTRIBUTE_CHAR13 | ExpHdrPrntAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpHdrAttributeChar14 | — |
| ATTRIBUTE_CHAR14 | ExpHdrPrntAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpHdrAttributeChar15 | — |
| ATTRIBUTE_CHAR15 | ExpHdrPrntAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpHdrAttributeChar2 | — |
| ATTRIBUTE_CHAR2 | ExpHdrPrntAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpHdrAttributeChar3 | — |
| ATTRIBUTE_CHAR3 | ExpHdrPrntAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpHdrAttributeChar4 | — |
| ATTRIBUTE_CHAR4 | ExpHdrPrntAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpHdrAttributeChar5 | — |
| ATTRIBUTE_CHAR5 | ExpHdrPrntAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpHdrAttributeChar6 | — |
| ATTRIBUTE_CHAR6 | ExpHdrPrntAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpHdrAttributeChar7 | — |
| ATTRIBUTE_CHAR7 | ExpHdrPrntAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpHdrAttributeChar8 | — |
| ATTRIBUTE_CHAR8 | ExpHdrPrntAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpHdrAttributeChar9 | — |
| ATTRIBUTE_CHAR9 | ExpHdrPrntAttributeChar9 | — |
| AUDIT_CODE | ExpHdrAuditCode | ✅ |
| AUDIT_CODE | ExpHdrPrntAuditCode | — |
| AUDIT_RETURN_REASON_CODE | ExpHdrAuditReturnReasonCode | ✅ |
| AUDIT_RETURN_REASON_CODE | ExpHdrPrntAuditReturnReasonCode | — |
| AWT_GROUP_ID | ExpHdrAwtGroupId | — |
| AWT_GROUP_ID | ExpHdrPrntAwtGroupId | — |
| BOTHPAY_FLAG | ExpHdrBothpayFlag | — |
| BOTHPAY_FLAG | ExpHdrPrntBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpHdrCashExpensePaidDate | ✅ |
| CREATED_BY | ExpHdrCreatedBy | ✅ |
| CREATED_BY | ExpHdrPrntCreatedBy | — |
| CREATION_DATE | ExpHdrCreationDate | ✅ |
| CURRENT_APPROVER_ID | ExpHdrCurrentApproverId | — |
| CURRENT_APPROVER_ID | ExpHdrPrntCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpHdrExchangeRateType | ✅ |
| EXCHANGE_RATE_TYPE | ExpHdrPrntExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpHdrExpRepProcessingId | — |
| EXP_REP_PROCESSING_ID | ExpHdrPrntExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpHdrExpenseReportDate | ✅ |
| EXPENSE_REPORT_DATE | ExpHdrPrntExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | — |
| EXPENSE_REPORT_ID | ExpHdrPrntExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpHdrExpenseReportNum | ✅ |
| EXPENSE_REPORT_NUM | ExpHdrPrntExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpHdrExpenseReportTotal | — |
| EXPENSE_REPORT_TOTAL | ExpHdrPrntExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpHdrExpenseStatusCode | ✅ |
| EXPENSE_STATUS_CODE | ExpHdrPrntExpenseStatusCode | — |
| EXPENSE_STATUS_DATE | ExpHdrExpenseStatusDate | ✅ |
| EXPENSE_STATUS_DATE | ExpHdrPrntExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpHdrExportRejectCode | — |
| EXPORT_REJECT_CODE | ExpHdrPrntExportRejectCode | — |
| EXPORT_REQUEST_ID | ExpHdrExportRequestId | — |
| EXPORT_REQUEST_ID | ExpHdrPrntExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpHdrFinalApprovalDate | ✅ |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrHoldingExpenseReportId | — |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrPrntHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrImagedReceiptsStatusCode | ✅ |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrPrntImagedReceiptsStatusCode | — |
| LAST_AUDIT_BY | ExpHdrLastAuditBy | — |
| LAST_AUDIT_BY | ExpHdrPrntLastAuditBy | — |
| LAST_UPDATE_DATE | ExpHdrLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ExpHdrPrntLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpHdrLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ExpHdrPrntLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpHdrLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ExpHdrPrntLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpHdrPrntObjectVersionNumber | — |
| ORG_ID | ExpHdrOrgId | — |
| ORG_ID | ExpHdrPrntOrgId | — |
| OVERRIDE_APPROVER_ID | ExpHdrOverrideApproverId | — |
| OVERRIDE_APPROVER_ID | ExpHdrPrntOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrParentExpenseReportId | ✅ |
| PARENT_EXPENSE_REPORT_ID | ExpHdrPrntParentExpenseReportId | — |
| PAYMENT_METHOD_CODE | ExpHdrPaymentMethodCode | ✅ |
| PERSON_ID | ExpHdrPersonId | — |
| PERSON_ID | ExpHdrPrntPersonId | — |
| PREPARER_ID | ExpHdrPreparerId | — |
| PREPARER_ID | ExpHdrPrntPreparerId | — |
| PURPOSE | ExpHdrPrntPurpose | — |
| PURPOSE | ExpHdrPurpose | ✅ |
| RECEIPTS_FILING_NUMBER | ExpHdrPrntReceiptsFilingNumber | — |
| RECEIPTS_FILING_NUMBER | ExpHdrReceiptsFilingNumber | ✅ |
| RECEIPTS_RECEIVED_DATE | ExpHdrPrntReceiptsReceivedDate | — |
| RECEIPTS_RECEIVED_DATE | ExpHdrReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ExpHdrPrntReceiptsStatusCode | — |
| RECEIPTS_STATUS_CODE | ExpHdrReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrPrntReimbursementCurrencyCode | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | FullExpHdrPrntReportCMC | — |
| REPORT_CREATION_METHOD_CODE | FullExpHdrReportCMC | — |
| REPORT_SUBMIT_DATE | ExpHdrPrntReportSubmitDate | — |
| REPORT_SUBMIT_DATE | ExpHdrReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ExpHdrPrntShortpayTypeCode | — |
| SHORTPAY_TYPE_CODE | ExpHdrShortpayTypeCode | ✅ |
| TRIP_ID | ExpHdrPrntTripId | — |
| TRIP_ID | ExpHdrTripId | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrPrntUnappliedAdvancesJust | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrUnappliedAdvancesJust | — |

### [[expensereportextractpvo|ExpenseReportExtractPVO]] (OTHER · BICC: 23/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_CASH_ADV_FLAG | ExpenseReportApplyCashAdvFlag | — |
| ASSIGNMENT_ID | ExpenseReportAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | ExpenseReportAttributeCategory | — |
| ATTRIBUTE_CHAR1 | ExpenseReportAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpenseReportAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpenseReportAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpenseReportAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpenseReportAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpenseReportAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpenseReportAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpenseReportAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpenseReportAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpenseReportAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpenseReportAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpenseReportAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpenseReportAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpenseReportAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpenseReportAttributeChar9 | — |
| ATTRIBUTE_DATE1 | ExpenseReportAttributeDate1 | — |
| ATTRIBUTE_DATE2 | ExpenseReportAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ExpenseReportAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ExpenseReportAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ExpenseReportAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | ExpenseReportAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | ExpenseReportAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | ExpenseReportAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ExpenseReportAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ExpenseReportAttributeNumber5 | — |
| ATTRIBUTE_TIMESTAMP1 | ExpenseReportAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | ExpenseReportAttributeTimestamp2 | — |
| AUDIT_CODE | ExpenseReportAuditCode | — |
| AUDIT_PRIOR_MGR_STATUS_CODE | ExpenseReportAuditPriorMgrStatusCode | — |
| AUDIT_RETURN_REASON_CODE | ExpenseReportAuditReturnReasonCode | — |
| AWT_GROUP_ID | ExpenseReportAwtGroupId | — |
| BOTHPAY_FLAG | ExpenseReportBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpenseReportCashExpensePaidDate | — |
| CREATED_BY | ExpenseReportCreatedBy | — |
| CREATION_DATE | ExpenseReportCreationDate | ✅ |
| CURRENT_APPROVER_ID | ExpenseReportCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpenseReportExchangeRateType | ✅ |
| EXP_REP_PROCESSING_ID | ExpenseReportExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpenseReportDate | ✅ |
| EXPENSE_REPORT_ID | ExpenseReportId | ✅ |
| EXPENSE_REPORT_NUM | ExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpenseReportTotal | ✅ |
| EXPENSE_STATUS_CODE | ExpenseReportExpenseStatusCode | ✅ |
| EXPENSE_STATUS_DATE | ExpenseReportExpenseStatusDate | ✅ |
| EXPORT_REJECT_CODE | ExpenseReportExportRejectCode | ✅ |
| EXPORT_REQUEST_ID | ExpenseReportExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpenseReportFinalApprovalDate | — |
| HOLDING_EXPENSE_REPORT_ID | ExpenseReportHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ExpenseReportImagedReceiptsReceivedDate | ✅ |
| IMAGED_RECEIPTS_STATUS_CODE | ExpenseReportImagedReceiptsStatusCode | ✅ |
| LAST_AUDIT_BY | ExpenseReportLastAuditBy | — |
| LAST_UPDATE_DATE | ExpenseReportLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseReportLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseReportLastUpdatedBy | — |
| MISSING_IMAGES_REASON | ExpenseReportMissingImagesReason | — |
| OBJECT_VERSION_NUMBER | ExpenseReportObjectVersionNumber | — |
| ORG_ID | ExpenseReportOrgId | ✅ |
| OVERDUE_RCPT_CORRELATION_ID | ExpenseReportOverdueRcptCorrelationId | — |
| OVERRIDE_APPROVER_ID | ExpenseReportOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpenseReportParentExpenseReportId | ✅ |
| PAYMENT_HOLD_CORRELATION_ID | ExpenseReportPaymentHoldCorrelationId | — |
| PAYMENT_METHOD_CODE | ExpenseReportPaymentMethodCode | ✅ |
| PERSON_ID | ExpenseReportPersonId | ✅ |
| PREPARER_ID | ExpenseReportPreparerId | — |
| PURPOSE | ExpenseReportPurpose | ✅ |
| RECEIPTS_FILING_NUMBER | ExpenseReportReceiptsFilingNumber | — |
| RECEIPTS_RECEIVED_DATE | ExpenseReportReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ExpenseReportReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpenseReportReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | ExpenseReportCreationMethodCode | ✅ |
| REPORT_SUBMIT_DATE | ExpenseReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ExpenseReportShortpayTypeCode | — |
| TRIP_ID | ExpenseReportTripId | — |
| UNAPPLIED_ADVANCES_JUST | ExpenseReportUnappliedAdvancesJust | — |
| UNAPPLIED_CASH_ADV_REASON | ExpenseReportUnappliedCashAdvReason | — |
| WORKFLOW_CORRELATION_ID | ExpenseReportWorkflowCorrelationId | — |

### [[expensereporthistorypvo|ExpenseReportHistoryPVO]] (OTHER · BICC: 1/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_CASH_ADV_FLAG | ExpenseReportPEOApplyCashAdvFlag | — |
| ASSIGNMENT_ID | ExpenseReportPEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpenseReportPEOAttributeCategory | — |
| AUDIT_CODE | ExpenseReportPEOAuditCode | — |
| AUDIT_RETURN_REASON_CODE | ExpenseReportPEOAuditReturnReasonCode1 | — |
| AWT_GROUP_ID | ExpenseReportPEOAwtGroupId | — |
| BOTHPAY_FLAG | ExpenseReportPEOBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpenseReportPEOCashExpensePaidDate | — |
| CREATED_BY | ExpenseReportPEOCreatedBy1 | — |
| CREATION_DATE | ExpenseReportPEOCreationDate1 | — |
| CURRENT_APPROVER_ID | ExpenseReportPEOCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpenseReportPEOExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpenseReportPEOExpRepProcessingId1 | — |
| EXPENSE_REPORT_DATE | ExpenseReportPEOExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpenseReportPEOExpenseReportId | — |
| EXPENSE_REPORT_ID | HoldingExpenseReportPEOExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpenseReportPEOExpenseReportNum | — |
| EXPENSE_REPORT_NUM | HoldingExpenseReportPEOExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpenseReportPEOExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpenseReportPEOExpenseStatusCode1 | — |
| EXPENSE_STATUS_DATE | ExpenseReportPEOExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpenseReportPEOExportRejectCode1 | — |
| EXPORT_REQUEST_ID | ExpenseReportPEOExportRequestId1 | — |
| FINAL_APPROVAL_DATE | ExpenseReportPEOFinalApprovalDate | — |
| HOLDING_EXPENSE_REPORT_ID | ExpenseReportPEOHoldingExpenseReportId1 | — |
| HOLDING_EXPENSE_REPORT_ID | HoldingExpenseReportPEOHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ExpenseReportPEOImagedReceiptsReceivedDate | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpenseReportPEOImagedReceiptsStatusCode1 | — |
| LAST_AUDIT_BY | ExpenseReportPEOLastAuditBy | — |
| LAST_UPDATE_DATE | ExpenseReportPEOLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | ExpenseReportPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | ExpenseReportPEOLastUpdatedBy1 | — |
| MISSING_IMAGES_REASON | ExpenseReportPEOMissingImagesReason | — |
| OBJECT_VERSION_NUMBER | ExpenseReportPEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseReportPEOOrgId | — |
| OVERDUE_RCPT_CORRELATION_ID | ExpenseReportPEOOverdueRcptCorrelationId | — |
| OVERRIDE_APPROVER_ID | ExpenseReportPEOOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpenseReportPEOParentExpenseReportId | — |
| PAYMENT_HOLD_CORRELATION_ID | ExpenseReportPEOPaymentHoldCorrelationId | — |
| PAYMENT_METHOD_CODE | ExpenseReportPEOPaymentMethodCode | — |
| PERSON_ID | ExpenseReportPEOPersonId | — |
| PREPARER_ID | ExpenseReportPEOPreparerId | — |
| PURPOSE | ExpenseReportPEOPurpose | — |
| RECEIPTS_FILING_NUMBER | ExpenseReportPEOReceiptsFilingNumber | — |
| RECEIPTS_RECEIVED_DATE | ExpenseReportPEOReceiptsReceivedDate | — |
| RECEIPTS_STATUS_CODE | ExpenseReportPEOReceiptsStatusCode1 | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpenseReportPEOReimbursementCurrencyCode | — |
| REPORT_CREATION_METHOD_CODE | ExpenseReportPEOReportCreationMethodCode | — |
| REPORT_SUBMIT_DATE | ExpenseReportPEOReportSubmitDate | — |
| SHORTPAY_TYPE_CODE | ExpenseReportPEOShortpayTypeCode | — |
| TRIP_ID | ExpenseReportPEOTripId | — |
| UNAPPLIED_ADVANCES_JUST | ExpenseReportPEOUnappliedAdvancesJust | — |
| UNAPPLIED_CASH_ADV_REASON | ExpenseReportPEOUnappliedCashAdvReason | — |
| WORKFLOW_CORRELATION_ID | ExpenseReportPEOWorkflowCorrelationId | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER · BICC: 24/116)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_CASH_ADV_FLAG | ApplyCashAdvFlag | — |
| APPLY_CASH_ADV_FLAG | ParentExpReportApplyCashAdvFlag | — |
| ASSIGNMENT_ID | AssignmentId | — |
| ASSIGNMENT_ID | ParentExpReportAssignmentId | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR11 | AttributeChar11 | — |
| ATTRIBUTE_CHAR12 | AttributeChar12 | — |
| ATTRIBUTE_CHAR13 | AttributeChar13 | — |
| ATTRIBUTE_CHAR14 | AttributeChar14 | — |
| ATTRIBUTE_CHAR15 | AttributeChar15 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
| AUDIT_CODE | AuditCode | ✅ |
| AUDIT_CODE | ParentExpReportAuditCode | — |
| AUDIT_RETURN_REASON_CODE | AuditReturnReasonCode | ✅ |
| AUDIT_RETURN_REASON_CODE | ParentExpReportAuditReturnReasonCode | — |
| AWT_GROUP_ID | AwtGroupId | — |
| AWT_GROUP_ID | ParentExpReportAwtGroupId | — |
| BOTHPAY_FLAG | BothpayFlag | — |
| BOTHPAY_FLAG | ParentExpReportBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | CashExpensePaidDate | ✅ |
| CASH_EXPENSE_PAID_DATE | ParentExpReportCashExpensePaidDate | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATED_BY | ParentExpReportCreatedBy | — |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_DATE | ParentExpReportCreationDate | — |
| CURRENT_APPROVER_ID | CurrentApproverId | — |
| CURRENT_APPROVER_ID | ParentExpReportCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ParentExpReportExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpRepProcessingId | — |
| EXP_REP_PROCESSING_ID | ParentExpReportExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpenseReportDate | ✅ |
| EXPENSE_REPORT_DATE | ParentExpReportExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpenseReportId | ✅ |
| EXPENSE_REPORT_ID | ParentExpReportExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpenseReportNum | ✅ |
| EXPENSE_REPORT_NUM | ParentExpReportExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpenseReportTotal | ✅ |
| EXPENSE_REPORT_TOTAL | ParentExpReportExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpenseStatusCode | ✅ |
| EXPENSE_STATUS_CODE | ParentExpReportExpenseStatusCode | — |
| EXPENSE_STATUS_DATE | ExpenseStatusDate | — |
| EXPENSE_STATUS_DATE | ParentExpReportExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExportRejectCode | — |
| EXPORT_REJECT_CODE | ParentExpReportExportRejectCode | — |
| EXPORT_REQUEST_ID | ExportRequestId | — |
| EXPORT_REQUEST_ID | ParentExpReportExportRequestId | — |
| FINAL_APPROVAL_DATE | FinalApprovalDate | ✅ |
| FINAL_APPROVAL_DATE | ParentExpReportFinalApprovalDate | — |
| HOLDING_EXPENSE_REPORT_ID | HoldingExpenseReportId | — |
| HOLDING_EXPENSE_REPORT_ID | ParentExpReportHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ImagedReceiptsReceivedDate | — |
| IMAGED_RECEIPTS_RECEIVED_DATE | ParentExpReportImagedReceiptsReceivedDate | — |
| IMAGED_RECEIPTS_STATUS_CODE | ImagedReceiptsStatusCode | ✅ |
| IMAGED_RECEIPTS_STATUS_CODE | ParentExpReportImagedReceiptsStatusCode | — |
| LAST_AUDIT_BY | LastAuditBy | — |
| LAST_AUDIT_BY | ParentExpReportLastAuditBy | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentExpReportLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ParentExpReportLastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ParentExpReportLastUpdatedBy | — |
| MISSING_IMAGES_REASON | MissingImagesReason | — |
| MISSING_IMAGES_REASON | ParentExpReportMissingImagesReason | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ParentExpReportObjectVersionNumber | — |
| ORG_ID | OrgId | — |
| ORG_ID | ParentExpReportOrgId | — |
| OVERDUE_RCPT_CORRELATION_ID | OverdueRcptCorrelationId | — |
| OVERDUE_RCPT_CORRELATION_ID | ParentExpReportOverdueRcptCorrelationId | — |
| OVERRIDE_APPROVER_ID | OverrideApproverId | — |
| OVERRIDE_APPROVER_ID | ParentExpReportOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ParentExpReportParentExpenseReportId | — |
| PARENT_EXPENSE_REPORT_ID | ParentExpenseReportId | — |
| PAYMENT_HOLD_CORRELATION_ID | ParentExpReportPaymentHoldCorrelationId | — |
| PAYMENT_HOLD_CORRELATION_ID | PaymentHoldCorrelationId | — |
| PAYMENT_METHOD_CODE | ParentExpReportPaymentMethodCode | — |
| PAYMENT_METHOD_CODE | PaymentMethodCode | ✅ |
| PERSON_ID | ParentExpReportPersonId | — |
| PERSON_ID | PersonId | — |
| PREPARER_ID | ParentExpReportPreparerId | — |
| PREPARER_ID | PreparerId | — |
| PURPOSE | ParentExpReportPurpose | — |
| PURPOSE | Purpose | ✅ |
| RECEIPTS_FILING_NUMBER | ParentExpReportReceiptsFilingNumber | — |
| RECEIPTS_FILING_NUMBER | ReceiptsFilingNumber | ✅ |
| RECEIPTS_RECEIVED_DATE | ParentExpReportReceiptsReceivedDate | — |
| RECEIPTS_RECEIVED_DATE | ReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ParentExpReportReceiptsStatusCode | — |
| RECEIPTS_STATUS_CODE | ReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ParentExpReportReimbursementCurrencyCode | — |
| REIMBURSEMENT_CURRENCY_CODE | ReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | FullReportCMC | — |
| REPORT_CREATION_METHOD_CODE | ParentExpReportReportCreationMethodCode | — |
| REPORT_SUBMIT_DATE | ParentExpReportReportSubmitDate | — |
| REPORT_SUBMIT_DATE | ReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ParentExpReportShortpayTypeCode | — |
| SHORTPAY_TYPE_CODE | ShortpayTypeCode | ✅ |
| TRIP_ID | ParentExpReportTripId | — |
| TRIP_ID | TripId | — |
| UNAPPLIED_ADVANCES_JUST | ParentExpReportUnappliedAdvancesJust | — |
| UNAPPLIED_ADVANCES_JUST | UnappliedAdvancesJust | — |
| UNAPPLIED_CASH_ADV_REASON | ParentExpReportUnappliedCashAdvReason | — |
| UNAPPLIED_CASH_ADV_REASON | UnappliedCashAdvReason | — |
| WORKFLOW_CORRELATION_ID | ParentExpReportWorkflowCorrelationId | — |
| WORKFLOW_CORRELATION_ID | WorkflowCorrelationId | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 22/107)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | ExpHdrAssignmentId | — |
| ASSIGNMENT_ID | ExpHdrPrntAssignmentId | — |
| ATTRIBUTE_CHAR1 | ExpHdrAttributeChar1 | — |
| ATTRIBUTE_CHAR1 | ExpHdrPrntAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpHdrAttributeChar10 | — |
| ATTRIBUTE_CHAR10 | ExpHdrPrntAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpHdrAttributeChar11 | — |
| ATTRIBUTE_CHAR11 | ExpHdrPrntAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpHdrAttributeChar12 | — |
| ATTRIBUTE_CHAR12 | ExpHdrPrntAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpHdrAttributeChar13 | — |
| ATTRIBUTE_CHAR13 | ExpHdrPrntAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpHdrAttributeChar14 | — |
| ATTRIBUTE_CHAR14 | ExpHdrPrntAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpHdrAttributeChar15 | — |
| ATTRIBUTE_CHAR15 | ExpHdrPrntAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpHdrAttributeChar2 | — |
| ATTRIBUTE_CHAR2 | ExpHdrPrntAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpHdrAttributeChar3 | — |
| ATTRIBUTE_CHAR3 | ExpHdrPrntAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpHdrAttributeChar4 | — |
| ATTRIBUTE_CHAR4 | ExpHdrPrntAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpHdrAttributeChar5 | — |
| ATTRIBUTE_CHAR5 | ExpHdrPrntAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpHdrAttributeChar6 | — |
| ATTRIBUTE_CHAR6 | ExpHdrPrntAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpHdrAttributeChar7 | — |
| ATTRIBUTE_CHAR7 | ExpHdrPrntAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpHdrAttributeChar8 | — |
| ATTRIBUTE_CHAR8 | ExpHdrPrntAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpHdrAttributeChar9 | — |
| ATTRIBUTE_CHAR9 | ExpHdrPrntAttributeChar9 | — |
| AUDIT_CODE | ExpHdrAuditCode | ✅ |
| AUDIT_CODE | ExpHdrPrntAuditCode | — |
| AUDIT_RETURN_REASON_CODE | ExpHdrAuditReturnReasonCode | ✅ |
| AUDIT_RETURN_REASON_CODE | ExpHdrPrntAuditReturnReasonCode | — |
| AWT_GROUP_ID | ExpHdrAwtGroupId | — |
| AWT_GROUP_ID | ExpHdrPrntAwtGroupId | — |
| BOTHPAY_FLAG | ExpHdrBothpayFlag | — |
| BOTHPAY_FLAG | ExpHdrPrntBothpayFlag | — |
| CASH_EXPENSE_PAID_DATE | ExpHdrCashExpensePaidDate | ✅ |
| CREATED_BY | ExpHdrCreatedBy | ✅ |
| CREATED_BY | ExpHdrPrntCreatedBy | — |
| CREATION_DATE | ExpHdrCreationDate | ✅ |
| CURRENT_APPROVER_ID | ExpHdrCurrentApproverId | — |
| CURRENT_APPROVER_ID | ExpHdrPrntCurrentApproverId | — |
| EXCHANGE_RATE_TYPE | ExpHdrExchangeRateType | — |
| EXCHANGE_RATE_TYPE | ExpHdrPrntExchangeRateType | — |
| EXP_REP_PROCESSING_ID | ExpHdrExpRepProcessingId | — |
| EXP_REP_PROCESSING_ID | ExpHdrPrntExpRepProcessingId | — |
| EXPENSE_REPORT_DATE | ExpHdrExpenseReportDate | ✅ |
| EXPENSE_REPORT_DATE | ExpHdrPrntExpenseReportDate | — |
| EXPENSE_REPORT_ID | ExpHdrExpenseReportId | — |
| EXPENSE_REPORT_ID | ExpHdrPrntExpenseReportId | — |
| EXPENSE_REPORT_NUM | ExpHdrExpenseReportNum | ✅ |
| EXPENSE_REPORT_NUM | ExpHdrPrntExpenseReportNum | ✅ |
| EXPENSE_REPORT_TOTAL | ExpHdrExpenseReportTotal | — |
| EXPENSE_REPORT_TOTAL | ExpHdrPrntExpenseReportTotal | — |
| EXPENSE_STATUS_CODE | ExpHdrExpenseStatusCode | ✅ |
| EXPENSE_STATUS_CODE | ExpHdrPrntExpenseStatusCode | — |
| EXPENSE_STATUS_DATE | ExpHdrExpenseStatusDate | ✅ |
| EXPENSE_STATUS_DATE | ExpHdrPrntExpenseStatusDate | — |
| EXPORT_REJECT_CODE | ExpHdrExportRejectCode | — |
| EXPORT_REJECT_CODE | ExpHdrPrntExportRejectCode | — |
| EXPORT_REQUEST_ID | ExpHdrExportRequestId | — |
| EXPORT_REQUEST_ID | ExpHdrPrntExportRequestId | — |
| FINAL_APPROVAL_DATE | ExpHdrFinalApprovalDate | ✅ |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrHoldingExpenseReportId | — |
| HOLDING_EXPENSE_REPORT_ID | ExpHdrPrntHoldingExpenseReportId | — |
| IMAGED_RECEIPTS_STATUS_CODE | ExpHdrImagedReceiptsStatusCode | ✅ |
| LAST_AUDIT_BY | ExpHdrLastAuditBy | — |
| LAST_AUDIT_BY | ExpHdrPrntLastAuditBy | — |
| LAST_UPDATE_DATE | ExpHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpHdrLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ExpHdrPrntLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpHdrLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ExpHdrPrntLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ExpHdrObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ExpHdrPrntObjectVersionNumber | — |
| ORG_ID | ExpHdrOrgId | — |
| ORG_ID | ExpHdrPrntOrgId | — |
| OVERRIDE_APPROVER_ID | ExpHdrOverrideApproverId | — |
| OVERRIDE_APPROVER_ID | ExpHdrPrntOverrideApproverId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrParentExpenseReportId | — |
| PARENT_EXPENSE_REPORT_ID | ExpHdrPrntParentExpenseReportId | — |
| PAYMENT_METHOD_CODE | ExpHdrPaymentMethodCode | ✅ |
| PERSON_ID | ExpHdrPersonId | — |
| PERSON_ID | ExpHdrPrntPersonId | — |
| PREPARER_ID | ExpHdrPreparerId | — |
| PREPARER_ID | ExpHdrPrntPreparerId | — |
| PURPOSE | ExpHdrPrntPurpose | — |
| PURPOSE | ExpHdrPurpose | ✅ |
| RECEIPTS_FILING_NUMBER | ExpHdrPrntReceiptsFilingNumber | — |
| RECEIPTS_FILING_NUMBER | ExpHdrReceiptsFilingNumber | ✅ |
| RECEIPTS_RECEIVED_DATE | ExpHdrPrntReceiptsReceivedDate | — |
| RECEIPTS_RECEIVED_DATE | ExpHdrReceiptsReceivedDate | ✅ |
| RECEIPTS_STATUS_CODE | ExpHdrPrntReceiptsStatusCode | — |
| RECEIPTS_STATUS_CODE | ExpHdrReceiptsStatusCode | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrPrntReimbursementCurrencyCode | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpHdrReimbursementCurrencyCode | ✅ |
| REPORT_CREATION_METHOD_CODE | FullExpHdrReportCMC | — |
| REPORT_SUBMIT_DATE | ExpHdrPrntReportSubmitDate | — |
| REPORT_SUBMIT_DATE | ExpHdrReportSubmitDate | ✅ |
| SHORTPAY_TYPE_CODE | ExpHdrPrntShortpayTypeCode | — |
| SHORTPAY_TYPE_CODE | ExpHdrShortpayTypeCode | ✅ |
| UNAPPLIED_ADVANCES_JUST | ExpHdrPrntUnappliedAdvancesJust | — |
| UNAPPLIED_ADVANCES_JUST | ExpHdrUnappliedAdvancesJust | — |

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_REPORTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensereports.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
