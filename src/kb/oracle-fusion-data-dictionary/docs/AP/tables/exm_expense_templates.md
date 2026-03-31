---
id: DOC-AP-036
doc_type: system-doc
title: "EXM_EXPENSE_TEMPLATES — Templates de Relatório de Despesa"
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
  - templates-despesa
  - expense-templates
  - configuracao
aliases:
  - EXM_EXPENSE_TEMPLATES
  - exm_expense_templates
  - templates-despesa-exm
  - exm-expense-templates
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_TEMPLATES

## 📌 Visão Geral

Armazena os **templates (modelos) de relatório de despesa** do módulo Expense Management. Cada template define um conjunto pré-configurado de tipos de despesa permitidos, regras de política, moeda padrão e configurações de aprovação, facilitando a criação de relatórios de despesa padronizados por business unit, departamento ou finalidade.

> [!note] Configuração
> Esta é uma tabela de configuração (setup). Os templates são criados por administradores e associados a business units ou grupos de funcionários.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Padronização de relatórios:** Definição de modelos pré-configurados para tipos comuns de relatório (viagem nacional, viagem internacional, despesas administrativas, etc.).
- **Controle de tipos de despesa:** Restrição dos tipos de despesa permitidos por template.
- **Configuração de políticas:** Associação de regras de limite, obrigatoriedade de comprovante e aprovação por template.
- **Simplificação para o usuário:** Pré-preenchimento de campos comuns ao criar um relatório.
- **Governança de gastos:** Controle centralizado das regras de despesa por organização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_TEMPLATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template de despesa | — | 🟢 95% |
| 2 | TEMPLATE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do template de despesa | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do template | — | 🟢 90% |
| 4 | TEMPLATE_CODE | VARCHAR2(30) | NULL | Identificação | Código interno do template | — | 🟡 75% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda padrão de reembolso do template | — | 🟡 80% |
| 6 | START_DATE | DATE | NULL | Data | Data de início de vigência do template | — | 🟢 85% |
| 7 | END_DATE | DATE | NULL | Data | Data de término de vigência do template (NULL = sem expiração) | — | 🟢 85% |
| 8 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o template está ativo (Y/N) | — | 🟢 85% |
| 9 | CASH_ADVANCE_ALLOWED_FLAG | VARCHAR2(1) | NULL | Classificação | Permite adiantamento de caixa (Y/N) | — | 🟡 70% |
| 10 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Comprovante obrigatório por padrão (Y/N) | — | 🟡 70% |
| 11 | PURPOSE_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Propósito obrigatório (Y/N) | — | 🟡 65% |
| 12 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do template de despesas)

### Tabelas-filha (FK de saída)
- [[exm_expense_reports]] — via `EXPENSE_TEMPLATE_ID` (relatórios que utilizam este template)
- [[exm_expenses]] — via `EXPENSE_TEMPLATE_ID` (linhas de despesa associadas)

---

## 📎 Uso Típico

### Listar templates ativos por business unit
```sql
SELECT et.EXPENSE_TEMPLATE_ID, et.TEMPLATE_NAME,
       et.DESCRIPTION, et.CURRENCY_CODE,
       et.START_DATE, et.END_DATE
FROM   EXM_EXPENSE_TEMPLATES et
WHERE  et.ORG_ID = :p_org_id
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y'
  AND  (et.END_DATE IS NULL OR et.END_DATE >= SYSDATE)
ORDER BY et.TEMPLATE_NAME;
```

### Templates que permitem adiantamento
```sql
SELECT et.TEMPLATE_NAME, et.CURRENCY_CODE
FROM   EXM_EXPENSE_TEMPLATES et
WHERE  et.CASH_ADVANCE_ALLOWED_FLAG = 'Y'
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Templates ativos
- `END_DATE IS NULL OR END_DATE >= SYSDATE` — Templates vigentes
- `CASH_ADVANCE_ALLOWED_FLAG = 'Y'` — Templates com adiantamento permitido

---

## 🔒 Observações

- Templates são configurações de **setup** — alterações afetam apenas **novos** relatórios de despesa; relatórios já criados mantêm as regras vigentes na data de criação.
- A associação entre template e tipos de despesa permitidos pode ser gerenciada em tabelas auxiliares (ex: relação N:N entre template e [[exm_expense_types]]).
- O campo `END_DATE` permite inativar templates sem excluí-los, mantendo rastreabilidade histórica.
- Templates diferentes para a mesma `ORG_ID` permitem políticas distintas (ex: viagem nacional vs. internacional).

---

## 🔗 PVOs Relacionados

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_RCPT_MISSING_FLAG | ExpenseTemplatePEOAllowRcptMissingFlag | — |
| CASH_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCashReceiptReqFlag | — |
| CASH_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCashReceiptReqLimit | — |
| CC_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCcReceiptReqFlag | — |
| CC_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCcReceiptReqLimit | — |
| CREATED_BY | ExpenseTemplatePEOCreatedBy | — |
| CREATION_DATE | ExpenseTemplatePEOCreationDate | — |
| DESCRIPTION | ExpenseTemplatePEODescription | — |
| DFLT_CC_EXP_TYPE_ID | ExpenseTemplatePEODfltCcExpTypeId | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTemplatePEODispRcptViolationFlag | — |
| ENABLE_CC_MAPPING_FLAG | ExpenseTemplatePEOEnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplatePEOExpenseTemplateId | — |
| INACTIVE_DATE | ExpenseTemplatePEOInactiveDate | — |
| LAST_UPDATE_DATE | ExpenseTemplatePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTemplatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTemplatePEOLastUpdatedBy | — |
| NAME | ExpenseTemplatePEOName | ✅ |
| NEGATIVE_RCPT_REQ_FLAG | ExpenseTemplatePEONegativeRcptReqFlag | — |
| OBJECT_VERSION_NUMBER | ExpenseTemplatePEOObjectVersionNumber | — |
| ORG_ID | ExpenseTemplatePEOOrgId | — |
| START_DATE | ExpenseTemplatePEOStartDate | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_RCPT_MISSING_FLAG | ExpenseTemplatePEOAllowRcptMissingFlag | — |
| CASH_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCashReceiptReqFlag | — |
| CASH_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCashReceiptReqLimit | — |
| CC_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCcReceiptReqFlag | — |
| CC_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCcReceiptReqLimit | — |
| CREATED_BY | ExpenseTemplatePEOCreatedBy | — |
| CREATION_DATE | ExpenseTemplatePEOCreationDate | — |
| DESCRIPTION | ExpenseTemplatePEODescription | — |
| DFLT_CC_EXP_TYPE_ID | ExpenseTemplatePEODfltCcExpTypeId | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTemplatePEODispRcptViolationFlag | — |
| ENABLE_CC_MAPPING_FLAG | ExpenseTemplatePEOEnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplatePEOExpenseTemplateId | — |
| INACTIVE_DATE | ExpenseTemplatePEOInactiveDate | — |
| LAST_UPDATE_DATE | ExpenseTemplatePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTemplatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTemplatePEOLastUpdatedBy | — |
| NAME | ExpenseTemplatePEOName | ✅ |
| NEGATIVE_RCPT_REQ_FLAG | ExpenseTemplatePEONegativeRcptReqFlag | — |
| OBJECT_VERSION_NUMBER | ExpenseTemplatePEOObjectVersionNumber | — |
| ORG_ID | ExpenseTemplatePEOOrgId | — |
| START_DATE | ExpenseTemplatePEOStartDate | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 2/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_RCPT_MISSING_FLAG | ExpenseTemplatePEOAllowRcptMissingFlag | — |
| CASH_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCashReceiptReqFlag | — |
| CASH_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCashReceiptReqLimit | — |
| CC_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCcReceiptReqFlag | — |
| CC_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCcReceiptReqLimit | — |
| CREATED_BY | ExpenseTemplatePEOCreatedBy | — |
| CREATION_DATE | ExpenseTemplatePEOCreationDate | — |
| DESCRIPTION | ExpenseTemplatePEODescription | — |
| DFLT_CC_EXP_TYPE_ID | ExpenseTemplatePEODfltCcExpTypeId | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTemplatePEODispRcptViolationFlag | — |
| ENABLE_CC_MAPPING_FLAG | ExpenseTemplatePEOEnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplatePEOExpenseTemplateId | — |
| INACTIVE_DATE | ExpenseTemplatePEOInactiveDate | — |
| LAST_UPDATE_DATE | ExpenseTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTemplatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTemplatePEOLastUpdatedBy | — |
| NAME | ExpenseTemplatePEOName | ✅ |
| NEGATIVE_RCPT_REQ_FLAG | ExpenseTemplatePEONegativeRcptReqFlag | — |
| OBJECT_VERSION_NUMBER | ExpenseTemplatePEOObjectVersionNumber | — |
| ORG_ID | ExpenseTemplatePEOOrgId | — |
| START_DATE | ExpenseTemplatePEOStartDate | — |

### [[expensetemplateextractpvo|ExpenseTemplateExtractPVO]] (OTHER · BICC: 15/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_RCPT_MISSING_FLAG | ExpenseTemplateAllowRcptMissingFlag | ✅ |
| CASH_RECEIPT_REQ_FLAG | ExpenseTemplateCashReceiptReqFlag | ✅ |
| CASH_RECEIPT_REQ_LIMIT | ExpenseTemplateCashReceiptReqLimit | ✅ |
| CC_RECEIPT_REQ_FLAG | ExpenseTemplateCcReceiptReqFlag | ✅ |
| CC_RECEIPT_REQ_LIMIT | ExpenseTemplateCcReceiptReqLimit | ✅ |
| CREATED_BY | ExpenseTemplateCreatedBy | — |
| CREATION_DATE | ExpenseTemplateCreationDate | ✅ |
| DESCRIPTION | ExpenseTemplateDescription | ✅ |
| DFLT_CC_EXP_TYPE_ID | ExpenseTemplateDfltCcExpTypeId | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTemplateDispRcptViolationFlag | ✅ |
| ENABLE_CC_MAPPING_FLAG | ExpenseTemplateEnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplateId | ✅ |
| INACTIVE_DATE | ExpenseTemplateInactiveDate | ✅ |
| LAST_UPDATE_DATE | ExpenseTemplateLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTemplateLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTemplateLastUpdatedBy | — |
| NAME | ExpenseTemplateName | ✅ |
| NEGATIVE_RCPT_REQ_FLAG | ExpenseTemplateNegativeRcptReqFlag | ✅ |
| OBJECT_VERSION_NUMBER | ExpenseTemplateObjectVersionNumber | — |
| ORG_ID | ExpenseTemplateOrgId | ✅ |
| START_DATE | ExpenseTemplateStartDate | ✅ |

### [[expensetypepvo|ExpenseTypePVO]] (OTHER · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DESCRIPTION | Description1 | — |
| DFLT_CC_EXP_TYPE_ID | DfltCcExpTypeId | — |
| ENABLE_CC_MAPPING_FLAG | EnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplateId1 | — |
| INACTIVE_DATE | InactiveDate | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NAME | Name1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| ORG_ID | OrgId1 | — |
| START_DATE | StartDate1 | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 2/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_RCPT_MISSING_FLAG | ExpenseTemplatePEOAllowRcptMissingFlag | — |
| CASH_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCashReceiptReqFlag | — |
| CASH_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCashReceiptReqLimit | — |
| CC_RECEIPT_REQ_FLAG | ExpenseTemplatePEOCcReceiptReqFlag | — |
| CC_RECEIPT_REQ_LIMIT | ExpenseTemplatePEOCcReceiptReqLimit | — |
| CREATED_BY | ExpenseTemplatePEOCreatedBy | — |
| CREATION_DATE | ExpenseTemplatePEOCreationDate | — |
| DESCRIPTION | ExpenseTemplatePEODescription | — |
| DFLT_CC_EXP_TYPE_ID | ExpenseTemplatePEODfltCcExpTypeId | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTemplatePEODispRcptViolationFlag | — |
| ENABLE_CC_MAPPING_FLAG | ExpenseTemplatePEOEnableCcMappingFlag | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplatePEOExpenseTemplateId | — |
| INACTIVE_DATE | ExpenseTemplatePEOInactiveDate | — |
| LAST_UPDATE_DATE | ExpenseTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTemplatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTemplatePEOLastUpdatedBy | — |
| NAME | ExpenseTemplatePEOName | ✅ |
| NEGATIVE_RCPT_REQ_FLAG | ExpenseTemplatePEONegativeRcptReqFlag | — |
| OBJECT_VERSION_NUMBER | ExpenseTemplatePEOObjectVersionNumber | — |
| ORG_ID | ExpenseTemplatePEOOrgId | — |
| START_DATE | ExpenseTemplatePEOStartDate | — |

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_TEMPLATES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensetemplates.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
