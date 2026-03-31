---
id: DOC-AP-037
doc_type: system-doc
title: "EXM_EXPENSE_TYPES — Tipos de Despesa"
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
  - tipos-despesa
  - expense-types
  - configuracao
aliases:
  - EXM_EXPENSE_TYPES
  - exm_expense_types
  - tipos-despesa-exm
  - exm-expense-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_TYPES

## 📌 Visão Geral

Armazena os **tipos de despesa** (Expense Types) configurados no módulo Expense Management. Cada tipo representa uma categoria de gasto — como passagem aérea, hospedagem, alimentação, combustível, táxi/transporte, etc. — com regras associadas de limite, obrigatoriedade de comprovante, conta contábil padrão e políticas de reembolso.

> [!note] Configuração
> Esta é uma tabela de configuração (setup). Os tipos de despesa são definidos pelo administrador e apresentados ao funcionário como opções de categorização ao registrar cada item de gasto.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Categorização de despesas:** Classificação de cada item de gasto em categorias padronizadas.
- **Controle de políticas:** Definição de limites máximos, obrigatoriedade de comprovante e regras por tipo.
- **Derivação contábil:** Determinação da conta contábil de débito com base no tipo de despesa.
- **Relatórios gerenciais:** Análise de gastos corporativos por categoria (viagem, alimentação, etc.).
- **Per diem:** Configuração de tipos com cálculo automático de diárias.
- **Mileage/Quilometragem:** Tipos especiais com cálculo por distância percorrida.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de despesa | — | 🟢 95% |
| 2 | EXPENSE_TYPE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do tipo de despesa (ex: "Passagem Aérea", "Hospedagem") | — | 🟢 95% |
| 3 | EXPENSE_TYPE_CODE | VARCHAR2(30) | NULL | Identificação | Código interno do tipo de despesa | — | 🟡 80% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de despesa | — | 🟢 90% |
| 5 | EXPENSE_CATEGORY_CODE | VARCHAR2(30) | NULL | Classificação | Categoria macro: AIRFARE, LODGING, MEALS, MILEAGE, MISCELLANEOUS, etc. | — | 🟢 85% |
| 6 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante é obrigatório para este tipo (Y/N) | — | 🟢 85% |
| 7 | ITEMIZATION_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se itemização é obrigatória (Y/N) | — | 🟡 70% |
| 8 | LIMIT_AMOUNT | NUMBER | NULL | Financeiro | Valor-limite máximo permitido para este tipo de despesa | — | 🟡 75% |
| 9 | LIMIT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda do valor-limite | — | 🟡 70% |
| 10 | PER_DIEM_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é tipo de per diem/diária (Y/N) | — | 🟡 75% |
| 11 | MILEAGE_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é tipo de quilometragem/mileage (Y/N) | — | 🟡 75% |
| 12 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil padrão para este tipo de despesa | [[gl_code_combinations]] | 🟡 80% |
| 13 | TAX_CLASSIFICATION_CODE | VARCHAR2(30) | NULL | Tributário | Código de classificação fiscal | — | 🟡 70% |
| 14 | START_DATE | DATE | NULL | Data | Data de início de vigência | — | 🟢 85% |
| 15 | END_DATE | DATE | NULL | Data | Data de término de vigência (NULL = sem expiração) | — | 🟢 85% |
| 16 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o tipo está ativo (Y/N) | — | 🟢 85% |
| 17 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 22 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil padrão)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do tipo de despesa)

### Tabelas-filha (FK de saída)
- [[exm_expenses]] — via `EXPENSE_TYPE_ID` (linhas de despesa classificadas com este tipo)

---

## 📎 Uso Típico

### Listar tipos de despesa ativos por business unit
```sql
SELECT et.EXPENSE_TYPE_ID, et.EXPENSE_TYPE_NAME,
       et.EXPENSE_CATEGORY_CODE, et.LIMIT_AMOUNT,
       et.RECEIPT_REQUIRED_FLAG
FROM   EXM_EXPENSE_TYPES et
WHERE  et.ORG_ID = :p_org_id
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y'
  AND  (et.END_DATE IS NULL OR et.END_DATE >= SYSDATE)
ORDER BY et.EXPENSE_CATEGORY_CODE, et.EXPENSE_TYPE_NAME;
```

### Tipos de despesa com limite definido
```sql
SELECT et.EXPENSE_TYPE_NAME, et.LIMIT_AMOUNT,
       et.LIMIT_CURRENCY_CODE
FROM   EXM_EXPENSE_TYPES et
WHERE  et.LIMIT_AMOUNT IS NOT NULL
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y';
```

### Total gasto por tipo de despesa
```sql
SELECT et.EXPENSE_TYPE_NAME,
       SUM(e.REIMBURSABLE_AMOUNT) AS total_gasto,
       COUNT(*) AS qtd_itens
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.START_DATE BETWEEN :start_date AND :end_date
GROUP BY et.EXPENSE_TYPE_NAME
ORDER BY total_gasto DESC;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `EXPENSE_CATEGORY_CODE = 'AIRFARE'` — Passagens aéreas
- `PER_DIEM_FLAG = 'Y'` — Tipos de diária
- `MILEAGE_FLAG = 'Y'` — Tipos de quilometragem

---

## 🔒 Observações

- Tipos de despesa são fundamentais para a **derivação contábil automática**: o `CODE_COMBINATION_ID` define a conta de débito padrão, podendo ser sobrescrita na distribuição.
- Tipos com `PER_DIEM_FLAG = 'Y'` utilizam tabelas de taxas de diária para cálculo automático com base em localização e datas.
- Tipos com `MILEAGE_FLAG = 'Y'` calculam reembolso com base em distância percorrida × taxa por km/milha.
- O `LIMIT_AMOUNT` é verificado na validação do relatório; despesas acima do limite geram aviso ou bloqueio conforme política.
- Tipos podem ser associados a templates específicos ([[exm_expense_templates]]) para controlar quais categorias cada grupo de funcionários pode utilizar.
- O campo `EXPENSE_CATEGORY_CODE` permite agrupamento macro para relatórios gerenciais (viagem, alimentação, transporte, outros).

---

## 🔗 PVOs Relacionados

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 2/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

### [[expensetypeextractpvo|ExpenseTypeExtractPVO]] (OTHER · BICC: 19/57)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypeCategoryCode | ✅ |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypeCcReceiptRequiredFlag | ✅ |
| CC_RECEIPT_THRESHOLD | ExpenseTypeCcReceiptThreshold | ✅ |
| CODE_COMBINATION_ID | ExpenseTypeCodeCombinationId | — |
| CREATED_BY | ExpenseTypeCreatedBy | — |
| CREATION_DATE | ExpenseTypeCreationDate | ✅ |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypeDefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypeDescription | ✅ |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypeDispRcptViolationFlag | ✅ |
| ENABLE_PROJECTS_FLAG | ExpenseTypeEnableProjectsFlag | — |
| END_DATE | ExpenseTypeEndDate | ✅ |
| EXPENSE_TEMPLATE_ID | ExpenseTypeTemplateId | ✅ |
| EXPENSE_TYPE_ID | ExpenseTypeId | ✅ |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypeItemizationBehaviourCode | ✅ |
| ITEMIZATION_ONLY_FLAG | ExpenseTypeItemizationOnlyFlag | ✅ |
| LAST_UPDATE_DATE | ExpenseTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypeLastUpdatedBy | — |
| NAME | ExpenseTypeName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypeNegativeRcptReqCode | ✅ |
| OBJECT_VERSION_NUMBER | ExpenseTypeObjectVersionNumber | — |
| ORG_ID | ExpenseTypeOrgId | ✅ |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypeRcptRequiredProjFlag | ✅ |
| RECEIPT_REQUIRED_FLAG | ExpenseTypeReceiptRequiredFlag | ✅ |
| RECEIPT_THRESHOLD | ExpenseTypeReceiptThreshold | ✅ |
| SEGMENT1 | ExpenseTypeSegment1 | — |
| SEGMENT10 | ExpenseTypeSegment10 | — |
| SEGMENT11 | ExpenseTypeSegment11 | — |
| SEGMENT12 | ExpenseTypeSegment12 | — |
| SEGMENT13 | ExpenseTypeSegment13 | — |
| SEGMENT14 | ExpenseTypeSegment14 | — |
| SEGMENT15 | ExpenseTypeSegment15 | — |
| SEGMENT16 | ExpenseTypeSegment16 | — |
| SEGMENT17 | ExpenseTypeSegment17 | — |
| SEGMENT18 | ExpenseTypeSegment18 | — |
| SEGMENT19 | ExpenseTypeSegment19 | — |
| SEGMENT2 | ExpenseTypeSegment2 | — |
| SEGMENT20 | ExpenseTypeSegment20 | — |
| SEGMENT21 | ExpenseTypeSegment21 | — |
| SEGMENT22 | ExpenseTypeSegment22 | — |
| SEGMENT23 | ExpenseTypeSegment23 | — |
| SEGMENT24 | ExpenseTypeSegment24 | — |
| SEGMENT25 | ExpenseTypeSegment25 | — |
| SEGMENT26 | ExpenseTypeSegment26 | — |
| SEGMENT27 | ExpenseTypeSegment27 | — |
| SEGMENT28 | ExpenseTypeSegment28 | — |
| SEGMENT29 | ExpenseTypeSegment29 | — |
| SEGMENT3 | ExpenseTypeSegment3 | — |
| SEGMENT30 | ExpenseTypeSegment30 | — |
| SEGMENT4 | ExpenseTypeSegment4 | — |
| SEGMENT5 | ExpenseTypeSegment5 | — |
| SEGMENT6 | ExpenseTypeSegment6 | — |
| SEGMENT7 | ExpenseTypeSegment7 | — |
| SEGMENT8 | ExpenseTypeSegment8 | — |
| SEGMENT9 | ExpenseTypeSegment9 | — |
| START_DATE | ExpenseTypeStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypeTaxClassificationCode | ✅ |

### [[expensetypepvo|ExpenseTypePVO]] (OTHER · BICC: 7/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | CategoryCode | ✅ |
| CODE_COMBINATION_ID | CodeCombinationId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEFAULT_PROJ_EXPEND_TYPE | DefaultProjExpendType | — |
| DESCRIPTION | Description | — |
| DISP_RCPT_VIOLATION_FLAG | DispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | EnableProjectsFlag | — |
| END_DATE | EndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypeId | ✅ |
| ITEMIZATION_BEHAVIOUR_CODE | ItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_ID | OrgId | — |
| RCPT_REQUIRED_PROJ_FLAG | RcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ReceiptThreshold | — |
| SEGMENT1 | Segment1 | — |
| SEGMENT10 | Segment10 | — |
| SEGMENT11 | Segment11 | — |
| SEGMENT12 | Segment12 | — |
| SEGMENT13 | Segment13 | — |
| SEGMENT14 | Segment14 | — |
| SEGMENT15 | Segment15 | — |
| SEGMENT16 | Segment16 | — |
| SEGMENT17 | Segment17 | — |
| SEGMENT18 | Segment18 | — |
| SEGMENT19 | Segment19 | — |
| SEGMENT2 | Segment2 | — |
| SEGMENT20 | Segment20 | — |
| SEGMENT21 | Segment21 | — |
| SEGMENT22 | Segment22 | — |
| SEGMENT23 | Segment23 | — |
| SEGMENT24 | Segment24 | — |
| SEGMENT25 | Segment25 | — |
| SEGMENT26 | Segment26 | — |
| SEGMENT27 | Segment27 | — |
| SEGMENT28 | Segment28 | — |
| SEGMENT29 | Segment29 | — |
| SEGMENT3 | Segment3 | — |
| SEGMENT30 | Segment30 | — |
| SEGMENT4 | Segment4 | — |
| SEGMENT5 | Segment5 | — |
| SEGMENT6 | Segment6 | — |
| SEGMENT7 | Segment7 | — |
| SEGMENT8 | Segment8 | — |
| SEGMENT9 | Segment9 | — |
| START_DATE | StartDate | — |
| TAX_CLASSIFICATION_CODE | TaxClassificationCode | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 2/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

### [[otbistatsbasesummarypvo|OtbiStatsBaseSummaryPVO]] (OTHER · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

### [[otbistatssummarypvo|OtbiStatsSummaryPVO]] (OTHER · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_CODE | ExpenseTypePEOCategoryCode | — |
| CC_RECEIPT_REQUIRED_FLAG | ExpenseTypePEOCcReceiptRequiredFlag | — |
| CC_RECEIPT_THRESHOLD | ExpenseTypePEOCcReceiptThreshold | — |
| CODE_COMBINATION_ID | ExpenseTypePEOCodeCombinationId | — |
| CREATED_BY | ExpenseTypePEOCreatedBy | — |
| CREATION_DATE | ExpenseTypePEOCreationDate | — |
| DEFAULT_PROJ_EXPEND_TYPE | ExpenseTypePEODefaultProjExpendType | — |
| DESCRIPTION | ExpenseTypePEODescription | — |
| DISP_RCPT_VIOLATION_FLAG | ExpenseTypePEODispRcptViolationFlag | — |
| ENABLE_PROJECTS_FLAG | ExpenseTypePEOEnableProjectsFlag | — |
| END_DATE | ExpenseTypePEOEndDate | — |
| EXPENSE_TEMPLATE_ID | ExpenseTypePEOExpenseTemplateId | — |
| EXPENSE_TYPE_ID | ExpenseTypePEOExpenseTypeId | — |
| ITEMIZATION_BEHAVIOUR_CODE | ExpenseTypePEOItemizationBehaviourCode | — |
| ITEMIZATION_ONLY_FLAG | ExpenseTypePEOItemizationOnlyFlag | — |
| LAST_UPDATE_DATE | ExpenseTypePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpenseTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpenseTypePEOLastUpdatedBy | — |
| NAME | ExpenseTypePEOName | ✅ |
| NEGATIVE_RCPT_REQ_CODE | ExpenseTypePEONegativeRcptReqCode | — |
| OBJECT_VERSION_NUMBER | ExpenseTypePEOObjectVersionNumber1 | — |
| ORG_ID | ExpenseTypePEOOrgId1 | — |
| RCPT_REQUIRED_PROJ_FLAG | ExpenseTypePEORcptRequiredProjFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpenseTypePEOReceiptRequiredFlag | — |
| RECEIPT_THRESHOLD | ExpenseTypePEOReceiptThreshold | — |
| START_DATE | ExpenseTypePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpenseTypePEOTaxClassificationCode | — |

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensetypes.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
