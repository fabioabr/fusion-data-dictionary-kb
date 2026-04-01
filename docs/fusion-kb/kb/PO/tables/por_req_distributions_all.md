---
id: DOC-PO-067
doc_type: system-doc
title: "POR_REQ_DISTRIBUTIONS_ALL — Distribuições Contábeis de Requisições"
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
  - requisicoes
  - distribuicoes
  - contabilidade
aliases:
  - POR_REQ_DISTRIBUTIONS_ALL
  - por_req_distributions_all
  - distribuicoes-requisicao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_REQ_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** das linhas de requisição de compra. Cada distribuição define a combinação de contas contábeis (CCID) que será debitada quando a despesa for contabilizada, além do projeto, tarefa e percentual de distribuição quando aplicável. É filha de `POR_REQUISITION_LINES_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Alocação contábil:** Definição de para qual conta, centro de custo e segmento a despesa será alocada.
- **Distribuição multi-conta:** Divisão do custo de uma linha entre múltiplas contas contábeis (rateio).
- **Budgetary control:** Reserva de fundos (encumbrance) na conta contábil correspondente.
- **Project costing:** Associação de requisições a projetos e tarefas para controle de custos por projeto.
- **Reconciliação:** Rastreamento da distribuição contábil desde a requisição até a PO e o pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 100% |
| 2 | REQUISITION_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha de requisição associada | [[por_requisition_lines_all]] | 🟢 100% |
| 3 | DISTRIBUTION_NUM | NUMBER | NOT NULL | Identificação | Número sequencial da distribuição na linha | — | 🟢 95% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 5 | REQ_LINE_QUANTITY | NUMBER | NOT NULL | Quantitativo | Quantidade alocada nesta distribuição | — | 🟢 95% |
| 6 | REQ_LINE_AMOUNT | NUMBER | NULL | Financeiro | Valor alocado nesta distribuição | — | 🟢 90% |
| 7 | DISTRIBUTION_PERCENT | NUMBER | NULL | Percentual | Percentual de distribuição (quando rateio) | — | 🟡 80% |
| 8 | GL_ENCUMBERED_DATE | DATE | NULL | Contabilidade | Data de reserva de fundos (encumbrance) | — | 🟢 90% |
| 9 | GL_ENCUMBERED_PERIOD_NAME | VARCHAR2(15) | NULL | Contabilidade | Período contábil da reserva de fundos | — | 🟢 90% |
| 10 | ENCUMBERED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se os fundos foram reservados (Y/N) | — | 🟢 90% |
| 11 | ENCUMBERED_AMOUNT | NUMBER | NULL | Financeiro | Valor reservado (encumbered) | — | 🟢 90% |
| 12 | BUDGET_ACCOUNT_ID | NUMBER(18) | NULL | FK | Conta orçamentária | [[gl_code_combinations]] | 🟡 80% |
| 13 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto associado (Project Costing) | [[pjf_projects_all_b]] | 🟢 90% |
| 14 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 90% |
| 15 | EXPENDITURE_TYPE | VARCHAR2(30) | NULL | Projeto | Tipo de despesa do projeto | — | 🟢 85% |
| 16 | EXPENDITURE_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização de despesa do projeto | [[hr_all_organization_units_f]] | 🟡 80% |
| 17 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | FK | Ledger (livro contábil) | [[gl_ledgers]] | 🟢 90% |
| 18 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[por_requisition_lines_all]] — via `REQUISITION_LINE_ID` (linha de requisição)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil de despesa)
- [[gl_code_combinations]] — via `BUDGET_ACCOUNT_ID` (conta orçamentária)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil da distribuição de requisição)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a distribuição de requisição é imputada)
- [[pjf_tasks_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição de requisição)

### Tabelas-filha (FK de saída)
- Nenhuma direta — é o nível mais granular da hierarquia de requisição

---

## 📎 Uso Típico

### Distribuições contábeis de uma requisição
```sql
SELECT rd.DISTRIBUTION_NUM, rd.CODE_COMBINATION_ID,
       rd.REQ_LINE_QUANTITY, rd.REQ_LINE_AMOUNT,
       rd.ENCUMBERED_FLAG, rd.ENCUMBERED_AMOUNT
FROM   POR_REQ_DISTRIBUTIONS_ALL rd
JOIN   POR_REQUISITION_LINES_ALL rl ON rl.REQUISITION_LINE_ID = rd.REQUISITION_LINE_ID
WHERE  rl.REQUISITION_HEADER_ID = :p_req_header_id
ORDER BY rl.LINE_NUMBER, rd.DISTRIBUTION_NUM;
```

### Total encumbered por conta contábil
```sql
SELECT rd.CODE_COMBINATION_ID,
       SUM(rd.ENCUMBERED_AMOUNT) AS total_encumbered
FROM   POR_REQ_DISTRIBUTIONS_ALL rd
WHERE  rd.ENCUMBERED_FLAG = 'Y'
  AND  rd.ORG_ID = :p_org_id
GROUP BY rd.CODE_COMBINATION_ID;
```

---

## 🔒 Observações

- Uma linha de requisição pode ter múltiplas distribuições (rateio entre contas).
- A soma de `DISTRIBUTION_PERCENT` de todas as distribuições de uma linha deve ser 100%.
- O `ENCUMBERED_FLAG = 'Y'` indica que os fundos foram reservados no orçamento.
- Os campos de projeto (`PROJECT_ID`, `TASK_ID`, `EXPENDITURE_TYPE`) são preenchidos apenas quando a despesa é associada a um projeto no Oracle Projects.
- A conta contábil (`CODE_COMBINATION_ID`) é herdada pela PO e pela fatura do fornecedor, garantindo rastreabilidade end-to-end.

---

## 🔗 PVOs Relacionados

### [[inventorysupplypvo|InventorySupplyPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISTRIBUTION_ID | DistributionId | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPjcProjectId | — |
| PJC_TASK_ID | RequisitionDistributionPEOPjcTaskId | — |

### [[maintenancewoprocurementpopvo|MaintenanceWOProcurementPOPVO]] (OTHER · BICC: 1/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[maintenancewoprocurementreceiptpvo|MaintenanceWOProcurementReceiptPVO]] (OTHER · BICC: 1/33)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[maintenancewoprocurementreqpvo|MaintenanceWOProcurementReqPVO]] (OTHER · BICC: 4/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | ✅ |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | DistributionId | ✅ |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | ✅ |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId1 | — |
| ATTRIBUTE1 | RequisitionDistributionPEOAttribute180 | — |
| ATTRIBUTE10 | RequisitionDistributionPEOAttribute1014 | — |
| ATTRIBUTE11 | RequisitionDistributionPEOAttribute1118 | — |
| ATTRIBUTE12 | RequisitionDistributionPEOAttribute1216 | — |
| ATTRIBUTE13 | RequisitionDistributionPEOAttribute1314 | — |
| ATTRIBUTE14 | RequisitionDistributionPEOAttribute1414 | — |
| ATTRIBUTE15 | RequisitionDistributionPEOAttribute1514 | — |
| ATTRIBUTE16 | RequisitionDistributionPEOAttribute1611 | — |
| ATTRIBUTE17 | RequisitionDistributionPEOAttribute1711 | — |
| ATTRIBUTE18 | RequisitionDistributionPEOAttribute1811 | — |
| ATTRIBUTE19 | RequisitionDistributionPEOAttribute1911 | — |
| ATTRIBUTE2 | RequisitionDistributionPEOAttribute216 | — |
| ATTRIBUTE20 | RequisitionDistributionPEOAttribute2011 | — |
| ATTRIBUTE3 | RequisitionDistributionPEOAttribute315 | — |
| ATTRIBUTE4 | RequisitionDistributionPEOAttribute415 | — |
| ATTRIBUTE5 | RequisitionDistributionPEOAttribute514 | — |
| ATTRIBUTE6 | RequisitionDistributionPEOAttribute614 | — |
| ATTRIBUTE7 | RequisitionDistributionPEOAttribute714 | — |
| ATTRIBUTE8 | RequisitionDistributionPEOAttribute814 | — |
| ATTRIBUTE9 | RequisitionDistributionPEOAttribute914 | — |
| ATTRIBUTE_CATEGORY | RequisitionDistributionPEOAttributeCategory14 | — |
| ATTRIBUTE_DATE1 | RequisitionDistributionPEOAttributeDate116 | — |
| ATTRIBUTE_DATE10 | RequisitionDistributionPEOAttributeDate108 | — |
| ATTRIBUTE_DATE2 | RequisitionDistributionPEOAttributeDate214 | — |
| ATTRIBUTE_DATE3 | RequisitionDistributionPEOAttributeDate314 | — |
| ATTRIBUTE_DATE4 | RequisitionDistributionPEOAttributeDate414 | — |
| ATTRIBUTE_DATE5 | RequisitionDistributionPEOAttributeDate514 | — |
| ATTRIBUTE_DATE6 | RequisitionDistributionPEOAttributeDate68 | — |
| ATTRIBUTE_DATE7 | RequisitionDistributionPEOAttributeDate78 | — |
| ATTRIBUTE_DATE8 | RequisitionDistributionPEOAttributeDate88 | — |
| ATTRIBUTE_DATE9 | RequisitionDistributionPEOAttributeDate98 | — |
| ATTRIBUTE_NUMBER1 | RequisitionDistributionPEOAttributeNumber116 | — |
| ATTRIBUTE_NUMBER10 | RequisitionDistributionPEOAttributeNumber1011 | — |
| ATTRIBUTE_NUMBER2 | RequisitionDistributionPEOAttributeNumber214 | — |
| ATTRIBUTE_NUMBER3 | RequisitionDistributionPEOAttributeNumber314 | — |
| ATTRIBUTE_NUMBER4 | RequisitionDistributionPEOAttributeNumber414 | — |
| ATTRIBUTE_NUMBER5 | RequisitionDistributionPEOAttributeNumber514 | — |
| ATTRIBUTE_NUMBER6 | RequisitionDistributionPEOAttributeNumber611 | — |
| ATTRIBUTE_NUMBER7 | RequisitionDistributionPEOAttributeNumber711 | — |
| ATTRIBUTE_NUMBER8 | RequisitionDistributionPEOAttributeNumber811 | — |
| ATTRIBUTE_NUMBER9 | RequisitionDistributionPEOAttributeNumber911 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionDistributionPEOAttributeTimestamp19 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionDistributionPEOAttributeTimestamp106 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionDistributionPEOAttributeTimestamp29 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionDistributionPEOAttributeTimestamp39 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionDistributionPEOAttributeTimestamp49 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionDistributionPEOAttributeTimestamp59 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionDistributionPEOAttributeTimestamp66 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionDistributionPEOAttributeTimestamp76 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionDistributionPEOAttributeTimestamp86 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionDistributionPEOAttributeTimestamp96 | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate4 | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId3 | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy20 | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate20 | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus9 | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName12 | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage12 | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate20 | — |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin20 | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy20 | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax3 | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber17 | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG4 | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG4 | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY4 | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID4 | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID4 | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE4 | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID4 | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID4 | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID4 | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID4 | — |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE14 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE104 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE24 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE34 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE44 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE54 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE64 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE74 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE84 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE94 | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID4 | — |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE14 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE104 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE24 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE34 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE44 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE54 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE64 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE74 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE84 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE94 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID4 | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax1 | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId6 | — |
| REQUEST_ID | RequisitionDistributionPEORequestId15 | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId3 | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId1 | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId1 | — |
| ATTRIBUTE1 | RequisitionDistributionPEOAttribute180 | — |
| ATTRIBUTE10 | RequisitionDistributionPEOAttribute1014 | — |
| ATTRIBUTE11 | RequisitionDistributionPEOAttribute1118 | — |
| ATTRIBUTE12 | RequisitionDistributionPEOAttribute1216 | — |
| ATTRIBUTE13 | RequisitionDistributionPEOAttribute1314 | — |
| ATTRIBUTE14 | RequisitionDistributionPEOAttribute1414 | — |
| ATTRIBUTE15 | RequisitionDistributionPEOAttribute1514 | — |
| ATTRIBUTE16 | RequisitionDistributionPEOAttribute1611 | — |
| ATTRIBUTE17 | RequisitionDistributionPEOAttribute1711 | — |
| ATTRIBUTE18 | RequisitionDistributionPEOAttribute1811 | — |
| ATTRIBUTE19 | RequisitionDistributionPEOAttribute1911 | — |
| ATTRIBUTE2 | RequisitionDistributionPEOAttribute216 | — |
| ATTRIBUTE20 | RequisitionDistributionPEOAttribute2011 | — |
| ATTRIBUTE3 | RequisitionDistributionPEOAttribute315 | — |
| ATTRIBUTE4 | RequisitionDistributionPEOAttribute415 | — |
| ATTRIBUTE5 | RequisitionDistributionPEOAttribute514 | — |
| ATTRIBUTE6 | RequisitionDistributionPEOAttribute614 | — |
| ATTRIBUTE7 | RequisitionDistributionPEOAttribute714 | — |
| ATTRIBUTE8 | RequisitionDistributionPEOAttribute814 | — |
| ATTRIBUTE9 | RequisitionDistributionPEOAttribute914 | — |
| ATTRIBUTE_CATEGORY | RequisitionDistributionPEOAttributeCategory14 | — |
| ATTRIBUTE_DATE1 | RequisitionDistributionPEOAttributeDate116 | — |
| ATTRIBUTE_DATE10 | RequisitionDistributionPEOAttributeDate108 | — |
| ATTRIBUTE_DATE2 | RequisitionDistributionPEOAttributeDate214 | — |
| ATTRIBUTE_DATE3 | RequisitionDistributionPEOAttributeDate314 | — |
| ATTRIBUTE_DATE4 | RequisitionDistributionPEOAttributeDate414 | — |
| ATTRIBUTE_DATE5 | RequisitionDistributionPEOAttributeDate514 | — |
| ATTRIBUTE_DATE6 | RequisitionDistributionPEOAttributeDate68 | — |
| ATTRIBUTE_DATE7 | RequisitionDistributionPEOAttributeDate78 | — |
| ATTRIBUTE_DATE8 | RequisitionDistributionPEOAttributeDate88 | — |
| ATTRIBUTE_DATE9 | RequisitionDistributionPEOAttributeDate98 | — |
| ATTRIBUTE_NUMBER1 | RequisitionDistributionPEOAttributeNumber116 | — |
| ATTRIBUTE_NUMBER10 | RequisitionDistributionPEOAttributeNumber1011 | — |
| ATTRIBUTE_NUMBER2 | RequisitionDistributionPEOAttributeNumber214 | — |
| ATTRIBUTE_NUMBER3 | RequisitionDistributionPEOAttributeNumber314 | — |
| ATTRIBUTE_NUMBER4 | RequisitionDistributionPEOAttributeNumber414 | — |
| ATTRIBUTE_NUMBER5 | RequisitionDistributionPEOAttributeNumber514 | — |
| ATTRIBUTE_NUMBER6 | RequisitionDistributionPEOAttributeNumber611 | — |
| ATTRIBUTE_NUMBER7 | RequisitionDistributionPEOAttributeNumber711 | — |
| ATTRIBUTE_NUMBER8 | RequisitionDistributionPEOAttributeNumber811 | — |
| ATTRIBUTE_NUMBER9 | RequisitionDistributionPEOAttributeNumber911 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionDistributionPEOAttributeTimestamp19 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionDistributionPEOAttributeTimestamp106 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionDistributionPEOAttributeTimestamp29 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionDistributionPEOAttributeTimestamp39 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionDistributionPEOAttributeTimestamp49 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionDistributionPEOAttributeTimestamp59 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionDistributionPEOAttributeTimestamp66 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionDistributionPEOAttributeTimestamp76 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionDistributionPEOAttributeTimestamp86 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionDistributionPEOAttributeTimestamp96 | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate4 | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId3 | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy20 | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate20 | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus9 | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName12 | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage12 | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate20 | — |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin20 | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy20 | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax3 | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber17 | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG4 | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG4 | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY4 | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID4 | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID4 | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE4 | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID4 | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID4 | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID4 | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID4 | — |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE14 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE104 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE24 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE34 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE44 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE54 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE64 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE74 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE84 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE94 | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID4 | — |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE14 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE104 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE24 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE34 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE44 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE54 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE64 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE74 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE84 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE94 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID4 | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax1 | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId6 | — |
| REQUEST_ID | RequisitionDistributionPEORequestId15 | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId3 | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId1 | — |

### [[receivingreceiptp2ptransactionpvo|ReceivingReceiptP2PTransactionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| ATTRIBUTE1 | RequisitionDistributionPEOAttribute1 | — |
| ATTRIBUTE10 | RequisitionDistributionPEOAttribute10 | — |
| ATTRIBUTE11 | RequisitionDistributionPEOAttribute11 | — |
| ATTRIBUTE12 | RequisitionDistributionPEOAttribute12 | — |
| ATTRIBUTE13 | RequisitionDistributionPEOAttribute13 | — |
| ATTRIBUTE14 | RequisitionDistributionPEOAttribute14 | — |
| ATTRIBUTE15 | RequisitionDistributionPEOAttribute15 | — |
| ATTRIBUTE16 | RequisitionDistributionPEOAttribute16 | — |
| ATTRIBUTE17 | RequisitionDistributionPEOAttribute17 | — |
| ATTRIBUTE18 | RequisitionDistributionPEOAttribute18 | — |
| ATTRIBUTE19 | RequisitionDistributionPEOAttribute19 | — |
| ATTRIBUTE2 | RequisitionDistributionPEOAttribute2 | — |
| ATTRIBUTE20 | RequisitionDistributionPEOAttribute20 | — |
| ATTRIBUTE3 | RequisitionDistributionPEOAttribute3 | — |
| ATTRIBUTE4 | RequisitionDistributionPEOAttribute4 | — |
| ATTRIBUTE5 | RequisitionDistributionPEOAttribute5 | — |
| ATTRIBUTE6 | RequisitionDistributionPEOAttribute6 | — |
| ATTRIBUTE7 | RequisitionDistributionPEOAttribute7 | — |
| ATTRIBUTE8 | RequisitionDistributionPEOAttribute8 | — |
| ATTRIBUTE9 | RequisitionDistributionPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | RequisitionDistributionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | RequisitionDistributionPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | RequisitionDistributionPEOAttributeDate10 | — |
| ATTRIBUTE_DATE2 | RequisitionDistributionPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | RequisitionDistributionPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | RequisitionDistributionPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | RequisitionDistributionPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | RequisitionDistributionPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | RequisitionDistributionPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | RequisitionDistributionPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | RequisitionDistributionPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | RequisitionDistributionPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | RequisitionDistributionPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | RequisitionDistributionPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | RequisitionDistributionPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | RequisitionDistributionPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | RequisitionDistributionPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | RequisitionDistributionPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | RequisitionDistributionPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | RequisitionDistributionPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | RequisitionDistributionPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionDistributionPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionDistributionPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionDistributionPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionDistributionPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionDistributionPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionDistributionPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionDistributionPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionDistributionPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionDistributionPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionDistributionPEOAttributeTimestamp9 | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPEOPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPEOPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[requisitiondistributionextractpvo|RequisitionDistributionExtractPVO]] (PO · BICC: 39/90)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | AccountUserOverrideFlag | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| BUDGET_DATE | BudgetDate | ✅ |
| CODE_COMBINATION_ID | CodeCombinationId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISTRIBUTION_AMOUNT | DistributionAmount | ✅ |
| DISTRIBUTION_CURRENCY_AMOUNT | DistributionCurrencyAmount | ✅ |
| DISTRIBUTION_ID | DistributionId | ✅ |
| DISTRIBUTION_NUMBER | DistributionNumber | ✅ |
| DISTRIBUTION_QUANTITY | DistributionQuantity | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NONRECOVERABLE_CURRENCY_TAX | NonrecoverableCurrencyTax | ✅ |
| NONRECOVERABLE_TAX | NonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERCENT | Percent | ✅ |
| PJC_BILLABLE_FLAG | PJC_BILLABLE_FLAG | ✅ |
| PJC_CAPITALIZABLE_FLAG | PJC_CAPITALIZABLE_FLAG | ✅ |
| PJC_CONTEXT_CATEGORY | PJC_CONTEXT_CATEGORY | ✅ |
| PJC_CONTRACT_ID | PJC_CONTRACT_ID | ✅ |
| PJC_CONTRACT_LINE_ID | PJC_CONTRACT_LINE_ID | ✅ |
| PJC_EXPENDITURE_ITEM_DATE | PJC_EXPENDITURE_ITEM_DATE | ✅ |
| PJC_EXPENDITURE_TYPE_ID | PJC_EXPENDITURE_TYPE_ID | ✅ |
| PJC_FUNDING_ALLOCATION_ID | PJC_FUNDING_ALLOCATION_ID | ✅ |
| PJC_ORGANIZATION_ID | PJC_ORGANIZATION_ID | ✅ |
| PJC_PROJECT_ID | PJC_PROJECT_ID | ✅ |
| PJC_TASK_ID | PJC_TASK_ID | ✅ |
| PJC_WORK_TYPE_ID | PJC_WORK_TYPE_ID | ✅ |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | ✅ |
| RECOVERABLE_CURRENCY_TAX | RecoverableCurrencyTax | ✅ |
| RECOVERABLE_TAX | RecoverableTax | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| REQUISITION_LINE_ID | RequisitionLineId | ✅ |
| VARIANCE_ACCOUNT_ID | VarianceAccountId | ✅ |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 19/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionBudgetDate | ✅ |
| CODE_COMBINATION_ID | RequisitionDistributionCodeCombinationId | ✅ |
| CREATED_BY | RequisitionDistributionCreatedBy | ✅ |
| CREATION_DATE | RequisitionDistributionCreationDate | ✅ |
| DISTRIBUTION_AMOUNT | RequisitionDistributionDistributionAmount | ✅ |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionDistributionCurrencyAmount | ✅ |
| DISTRIBUTION_ID | DistributionId | ✅ |
| DISTRIBUTION_NUMBER | RequisitionDistributionDistributionNumber | ✅ |
| DISTRIBUTION_QUANTITY | RequisitionDistributionDistributionQuantity | ✅ |
| FUNDS_STATUS | RequisitionDistributionFundsStatus | ✅ |
| JOB_DEFINITION_NAME | RequisitionDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionLastUpdatedBy | ✅ |
| NONRECOVERABLE_TAX | RequisitionDistributionNonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | RequisitionDistributionObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPercent | ✅ |
| PJC_BILLABLE_FLAG | RequisitionDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPJC_PROJECT_ID | ✅ |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | RequisitionDistributionPJC_TASK_ID | ✅ |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPrimaryLedgerId | ✅ |
| RECOVERABLE_TAX | RequisitionDistributionRecoverableTax | ✅ |
| REQ_BU_ID | RequisitionDistributionReqBuId | — |
| REQUEST_ID | RequisitionDistributionRequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionRequisitionLineId | ✅ |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionVarianceAccountId | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 12/58)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionBudgetDate | ✅ |
| CODE_COMBINATION_ID | RequisitionDistributionCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionCreatedBy | — |
| CREATION_DATE | RequisitionDistributionCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionDistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionDistributionCurrencyAmount | ✅ |
| DISTRIBUTION_ID | DistributionId | ✅ |
| DISTRIBUTION_NUMBER | RequisitionDistributionDistributionNumber | ✅ |
| DISTRIBUTION_QUANTITY | RequisitionDistributionDistributionQuantity | ✅ |
| FUNDS_STATUS | RequisitionDistributionFundsStatus | ✅ |
| JOB_DEFINITION_NAME | RequisitionDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionNonrecoverableTax | ✅ |
| OBJECT_VERSION_NUMBER | RequisitionDistributionObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPercent | ✅ |
| PJC_BILLABLE_FLAG | RequisitionDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPJC_CAPITALIZABLE_FLAG | ✅ |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPJC_EXPENDITURE_ITEM_DATE | ✅ |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | RequisitionDistributionPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionRecoverableTax | ✅ |
| REQ_BU_ID | RequisitionDistributionReqBuId | — |
| REQUEST_ID | RequisitionDistributionRequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionRequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionVarianceAccountId | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionAccrualAccountId | — |
| CODE_COMBINATION_ID | RequisitionDistributionCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionCreatedBy | — |
| CREATION_DATE | RequisitionDistributionCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionDistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionDistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionDistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionDistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionDistributionQuantity | — |
| JOB_DEFINITION_NAME | RequisitionDistributionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionNonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPJC_PROJECT_ID | — |
| PJC_RESERVED_ATTRIBUTE1 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE1 | — |
| PJC_RESERVED_ATTRIBUTE10 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE10 | — |
| PJC_RESERVED_ATTRIBUTE2 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE2 | — |
| PJC_RESERVED_ATTRIBUTE3 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE3 | — |
| PJC_RESERVED_ATTRIBUTE4 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE4 | — |
| PJC_RESERVED_ATTRIBUTE5 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE5 | — |
| PJC_RESERVED_ATTRIBUTE6 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE6 | — |
| PJC_RESERVED_ATTRIBUTE7 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE7 | — |
| PJC_RESERVED_ATTRIBUTE8 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE8 | — |
| PJC_RESERVED_ATTRIBUTE9 | RequisitionDistributionPJC_RESERVED_ATTRIBUTE9 | — |
| PJC_TASK_ID | RequisitionDistributionPJC_TASK_ID | — |
| PJC_USER_DEF_ATTRIBUTE1 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE1 | — |
| PJC_USER_DEF_ATTRIBUTE10 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE10 | — |
| PJC_USER_DEF_ATTRIBUTE2 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE2 | — |
| PJC_USER_DEF_ATTRIBUTE3 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE3 | — |
| PJC_USER_DEF_ATTRIBUTE4 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE4 | — |
| PJC_USER_DEF_ATTRIBUTE5 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE5 | — |
| PJC_USER_DEF_ATTRIBUTE6 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE6 | — |
| PJC_USER_DEF_ATTRIBUTE7 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE7 | — |
| PJC_USER_DEF_ATTRIBUTE8 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE8 | — |
| PJC_USER_DEF_ATTRIBUTE9 | RequisitionDistributionPJC_USER_DEF_ATTRIBUTE9 | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionRecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionReqBuId | — |
| REQUEST_ID | RequisitionDistributionRequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionRequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionVarianceAccountId | — |

### [[woprocurementpopvo|WOProcurementPOPVO]] (OTHER · BICC: 1/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate | — |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | — |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[woprocurementreceiptpvo|WOProcurementReceiptPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| DISTRIBUTION_ID | RequisitionDistributionPEODistributionId | — |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | — |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

### [[woprocurementreqpvo|WOProcurementReqPVO]] (OTHER · BICC: 5/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_USER_OVERRIDE_FLAG | RequisitionDistributionPEOAccountUserOverrideFlag | — |
| ACCRUAL_ACCOUNT_ID | RequisitionDistributionPEOAccrualAccountId | — |
| BUDGET_DATE | RequisitionDistributionPEOBudgetDate | — |
| CODE_COMBINATION_ID | RequisitionDistributionPEOCodeCombinationId | — |
| CREATED_BY | RequisitionDistributionPEOCreatedBy | — |
| CREATION_DATE | RequisitionDistributionPEOCreationDate | ✅ |
| DISTRIBUTION_AMOUNT | RequisitionDistributionPEODistributionAmount | ✅ |
| DISTRIBUTION_CURRENCY_AMOUNT | RequisitionDistributionPEODistributionCurrencyAmount | — |
| DISTRIBUTION_ID | DistributionId | ✅ |
| DISTRIBUTION_NUMBER | RequisitionDistributionPEODistributionNumber | — |
| DISTRIBUTION_QUANTITY | RequisitionDistributionPEODistributionQuantity | ✅ |
| FUNDS_STATUS | RequisitionDistributionPEOFundsStatus | — |
| JOB_DEFINITION_NAME | RequisitionDistributionPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionDistributionPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | RequisitionDistributionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionDistributionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionDistributionPEOLastUpdatedBy | — |
| NONRECOVERABLE_TAX | RequisitionDistributionPEONonrecoverableTax | — |
| OBJECT_VERSION_NUMBER | RequisitionDistributionPEOObjectVersionNumber | — |
| PERCENT | RequisitionDistributionPEOPercent | — |
| PJC_BILLABLE_FLAG | RequisitionDistributionPEOPJC_BILLABLE_FLAG | — |
| PJC_CAPITALIZABLE_FLAG | RequisitionDistributionPEOPJC_CAPITALIZABLE_FLAG | — |
| PJC_CONTEXT_CATEGORY | RequisitionDistributionPEOPJC_CONTEXT_CATEGORY | — |
| PJC_CONTRACT_ID | RequisitionDistributionPEOPJC_CONTRACT_ID | — |
| PJC_CONTRACT_LINE_ID | RequisitionDistributionPEOPJC_CONTRACT_LINE_ID | — |
| PJC_EXPENDITURE_ITEM_DATE | RequisitionDistributionPEOPJC_EXPENDITURE_ITEM_DATE | — |
| PJC_EXPENDITURE_TYPE_ID | RequisitionDistributionPEOPJC_EXPENDITURE_TYPE_ID | — |
| PJC_FUNDING_ALLOCATION_ID | RequisitionDistributionPEOPJC_FUNDING_ALLOCATION_ID | — |
| PJC_ORGANIZATION_ID | RequisitionDistributionPEOPJC_ORGANIZATION_ID | — |
| PJC_PROJECT_ID | RequisitionDistributionPEOPJC_PROJECT_ID | — |
| PJC_TASK_ID | RequisitionDistributionPEOPJC_TASK_ID | — |
| PJC_WORK_TYPE_ID | RequisitionDistributionPEOPJC_WORK_TYPE_ID | — |
| PRIMARY_LEDGER_ID | RequisitionDistributionPEOPrimaryLedgerId | — |
| RECOVERABLE_TAX | RequisitionDistributionPEORecoverableTax | — |
| REQ_BU_ID | RequisitionDistributionPEOReqBuId | — |
| REQUEST_ID | RequisitionDistributionPEORequestId | — |
| REQUISITION_LINE_ID | RequisitionDistributionPEORequisitionLineId | — |
| VARIANCE_ACCOUNT_ID | RequisitionDistributionPEOVarianceAccountId | — |

---

## 📚 Referências

- [Oracle Docs — POR_REQ_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/porreqdistributionsall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
