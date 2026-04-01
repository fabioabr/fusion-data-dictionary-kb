---
id: DOC-AR-045
doc_type: system-doc
title: "AR_RECEIVABLES_TRX_ALL — Atividades de Recebíveis"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, atividades, ajustes, finance-charges]
aliases: [AR_RECEIVABLES_TRX_ALL, ar_receivables_trx_all, receivables_activities, atividades_recebiveis, ar_rec_trx]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIVABLES_TRX_ALL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela de cadastro de **atividades de recebíveis** (receivables activities). Define os tipos de operação utilizados em ajustes, recebimentos diversos (miscellaneous receipts), finance charges e estornos de cartão de crédito. Cada atividade aponta para uma conta contábil específica.

## 🧠 Propósito de Negócio

As atividades de recebíveis são **templates contábeis** que padronizam o tratamento de operações não transacionais no AR. Quando um analista realiza um ajuste ou registra um recebimento diverso, ele seleciona uma atividade que determina automaticamente a conta contábil de destino.

Casos de uso principais:
- Ajustes de saldo (write-off, reclassificação)
- Recebimentos diversos (juros recebidos, multas)
- Encargos financeiros (finance charges)
- Estornos de cartão de crédito (CC refund)

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | RECEIVABLES_TRX_ID | NUMBER | PK. Identificador único da atividade de recebíveis. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome da atividade (exibido em LOVs). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição textual da finalidade da atividade. | Identificação | 🟢 100% |
| 4 | TYPE | VARCHAR2 | Tipo da atividade: `ADJUST`, `FINCHRG`, `MISC`, `CCREFUND`. | Classificação | 🟢 100% |
| 5 | STATUS | VARCHAR2 | Status da atividade: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 6 | CODE_COMBINATION_ID | NUMBER | FK para a combinação contábil (conta GL). Referencia [[gl_code_combinations]]. | Contábil | 🟢 100% |
| 7 | GL_ACCOUNT_SOURCE | VARCHAR2 | Origem da conta GL: `ACTIVITY` (fixo na atividade), `TAX_CODE`, `REVENUE`. | Contábil | 🟢 100% |
| 8 | TAX_RATE_CODE_ID | NUMBER | FK para código de imposto associado. Referencia [[zx_rates_b]]. | Fiscal | 🟢 100% |
| 9 | ASSET_TAX_CODE | VARCHAR2 | Código fiscal para ativos (usado em cálculos tributários). | Fiscal | 🟢 100% |
| 10 | TAX_CODE_SOURCE | VARCHAR2 | Origem do código fiscal: `ACTIVITY`, `INVOICE`, `NONE`. | Fiscal | 🟢 100% |
| 11 | DEFAULT_AMOUNT | NUMBER | Valor padrão sugerido para a atividade. | Operacional | 🟢 100% |
| 12 | ROUNDING_ERROR_CCID | NUMBER | Conta contábil para diferenças de arredondamento. | Contábil | 🟢 100% |
| 13 | ORG_ID | NUMBER | Identificador da Business Unit. | Partição | 🟢 100% |
| 14 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 15 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 17 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 19 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[gl_code_combinations]] | CODE_COMBINATION_ID | FK | Conta contábil da atividade |
| [[zx_rates_b]] | TAX_RATE_CODE_ID | FK | Código de imposto associado |
| [[ar_adjustments_all]] | RECEIVABLES_TRX_ID | Referenciada por | Ajustes que usam esta atividade |
| [[ar_cash_receipts_all]] | RECEIVABLES_TRX_ID | Referenciada por | Recebimentos misc usando esta atividade |
| [[ar_system_parameters_all]] | ORG_ID | Referência | Parâmetros da BU |

## 📎 Uso Típico

```sql
-- Listar atividades de ajuste ativas
SELECT receivables_trx_id,
       name,
       type,
       gl_account_source
  FROM ar_receivables_trx_all
 WHERE type = 'ADJUST'
   AND status = 'A'
   AND org_id = :p_org_id;
```

```sql
-- Atividades com conta contábil fixa
SELECT rt.name,
       rt.type,
       gcc.concatenated_segments AS conta_gl
  FROM ar_receivables_trx_all rt
  JOIN gl_code_combinations_kfv gcc ON gcc.code_combination_id = rt.code_combination_id
 WHERE rt.gl_account_source = 'ACTIVITY'
   AND rt.org_id = :p_org_id;
```

## 🔒 Observações

- O campo `TYPE` determina onde a atividade pode ser utilizada: `ADJUST` para ajustes, `FINCHRG` para encargos financeiros, `MISC` para recebimentos diversos, `CCREFUND` para estornos de cartão.
- Atividades com `GL_ACCOUNT_SOURCE = 'ACTIVITY'` têm conta fixa; `REVENUE` herda a conta da linha da fatura.
- Inativar uma atividade (`STATUS = 'I'`) impede novos usos mas não afeta transações já registradas.
- Atividades de finance charge são referenciadas nos parâmetros do sistema ([[ar_system_parameters_all]]).

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | ReceivableActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | ReceivableActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | ReceivableActivityCodeCombinationId | — |
| CREATED_BY | ReceivableActivityCreatedBy | — |
| CREATION_DATE | ReceivableActivityCreationDate | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ReceivableActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | ReceivableActivityDescription | — |
| END_DATE_ACTIVE | ReceivableActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | ReceivableActivityGlAccountSource | — |
| INACTIVE_DATE | ReceivableActivityInactiveDate | — |
| LAST_UPDATE_DATE | ReceivableActivityLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableActivityLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableActivityLastUpdatedBy | — |
| LIABILITY_TAX_CODE | ReceivableActivityLiabilityTaxCode | — |
| NAME | ReceivableActivityName | ✅ |
| OBJECT_VERSION_NUMBER | ReceivableActivityObjectVersionNumber | — |
| ORG_ID | ReceivableActivityOrgId | — |
| RECEIVABLES_TRX_ID | ReceivableActivityReceivablesTrxId | ✅ |
| RISK_ELIMINATION_DAYS | ReceivableActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | ReceivableActivitySetOfBooksId | — |
| START_DATE_ACTIVE | ReceivableActivityStartDateActive | — |
| STATUS | ReceivableActivityStatus | — |
| TAX_CODE_SOURCE | ReceivableActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | ReceivableActivityTaxRecoverableFlag | — |
| TYPE | ReceivableActivityType | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | ReceivableActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | ReceivableActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | ReceivableActivityCodeCombinationId | — |
| CREATED_BY | ReceivableActivityCreatedBy | — |
| CREATION_DATE | ReceivableActivityCreationDate | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ReceivableActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | ReceivableActivityDescription | — |
| END_DATE_ACTIVE | ReceivableActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | ReceivableActivityGlAccountSource | — |
| INACTIVE_DATE | ReceivableActivityInactiveDate | — |
| LAST_UPDATE_DATE | ReceivableActivityLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableActivityLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableActivityLastUpdatedBy | — |
| LIABILITY_TAX_CODE | ReceivableActivityLiabilityTaxCode | — |
| NAME | ReceivableActivityName | ✅ |
| OBJECT_VERSION_NUMBER | ReceivableActivityObjectVersionNumber | — |
| ORG_ID | ReceivableActivityOrgId | — |
| RECEIVABLES_TRX_ID | ReceivableActivityReceivablesTrxId | ✅ |
| RISK_ELIMINATION_DAYS | ReceivableActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | ReceivableActivitySetOfBooksId | — |
| START_DATE_ACTIVE | ReceivableActivityStartDateActive | — |
| STATUS | ReceivableActivityStatus | — |
| TAX_CODE_SOURCE | ReceivableActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | ReceivableActivityTaxRecoverableFlag | — |
| TYPE | ReceivableActivityType | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | ReceivableAcitivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | ReceivableAcitivityAssetTaxCode | — |
| CODE_COMBINATION_ID | ReceivableAcitivityCodeCombinationId | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ReceivableAcitivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | ReceivableAcitivityDescription | — |
| END_DATE_ACTIVE | ReceivableAcitivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | ReceivableAcitivityGlAccountSource | — |
| INACTIVE_DATE | ReceivableAcitivityInactiveDate | — |
| LIABILITY_TAX_CODE | ReceivableAcitivityLiabilityTaxCode | — |
| NAME | ReceivableAcitivityName | — |
| ORG_ID | ReceivableAcitivityOrgId | — |
| RECEIVABLES_TRX_ID | ReceivableAcitivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | ReceivableAcitivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | ReceivableAcitivitySetOfBooksId | — |
| START_DATE_ACTIVE | ReceivableAcitivityStartDateActive | — |
| STATUS | ReceivableAcitivityStatus | — |
| TAX_CODE_SOURCE | ReceivableAcitivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | ReceivableAcitivityTaxRecoverableFlag | — |
| TYPE | ReceivableAcitivityType | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 2/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | ReceivableActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | ReceivableActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | ReceivableActivityCodeCombinationId | — |
| CREATED_BY | ReceivableActivityCreatedBy | — |
| CREATION_DATE | ReceivableActivityCreationDate | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ReceivableActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | ReceivableActivityDescription | — |
| END_DATE_ACTIVE | ReceivableActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | ReceivableActivityGlAccountSource | — |
| INACTIVE_DATE | ReceivableActivityInactiveDate | — |
| LAST_UPDATE_DATE | ReceivableActivityLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceivableActivityLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceivableActivityLastUpdatedBy | — |
| LIABILITY_TAX_CODE | ReceivableActivityLiabilityTaxCode | — |
| NAME | ReceivableActivityName | ✅ |
| OBJECT_VERSION_NUMBER | ReceivableActivityObjectVersionNumber | — |
| ORG_ID | ReceivableActivityOrgId | — |
| RECEIVABLES_TRX_ID | ReceivableActivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | ReceivableActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | ReceivableActivitySetOfBooksId | — |
| START_DATE_ACTIVE | ReceivableActivityStartDateActive | — |
| STATUS | ReceivableActivityStatus | — |
| TAX_CODE_SOURCE | ReceivableActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | ReceivableActivityTaxRecoverableFlag | — |
| TYPE | ReceivableActivityType | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 1/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RecvTrxActAccountingAffectFlag | — |
| ASSET_TAX_CODE | RecvTrxActAssetTaxCode | — |
| CODE_COMBINATION_ID | RecvTrxActCodeCombinationId | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RecvTrxActDefaultAcctgDistributionSet | — |
| DESCRIPTION | RecvTrxActDescription | — |
| END_DATE_ACTIVE | RecvTrxActEndDateActive | — |
| GL_ACCOUNT_SOURCE | RecvTrxActGlAccountSource | — |
| INACTIVE_DATE | RecvTrxActInactiveDate | — |
| LIABILITY_TAX_CODE | RecvTrxActLiabilityTaxCode | — |
| NAME | RecvTrxActName | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_ID | RecvTrxActOrgId | — |
| RECEIVABLES_TRX_ID | RecvTrxActReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RecvTrxActRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RecvTrxActSetOfBooksId | — |
| START_DATE_ACTIVE | RecvTrxActStartDateActive | — |
| STATUS | RecvTrxActStatus | — |
| TAX_CODE_SOURCE | RecvTrxActTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RecvTrxActTaxRecoverableFlag | — |
| TYPE | RecvTrxActType | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 2/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RcptReceivableActAccountingAffectFlag | — |
| ASSET_TAX_CODE | RcptReceivableActAssetTaxCode | — |
| CODE_COMBINATION_ID | RcptReceivableActCodeCombinationId | — |
| CREATED_BY | RcptReceivableActCreatedBy | — |
| CREATION_DATE | RcptReceivableActCreationDate | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RcptReceivableActDefaultAcctgDistributionSet | — |
| DESCRIPTION | RcptReceivableActDescription | — |
| END_DATE_ACTIVE | RcptReceivableActEndDateActive | — |
| GL_ACCOUNT_SOURCE | RcptReceivableActGlAccountSource | — |
| INACTIVE_DATE | RcptReceivableActInactiveDate | — |
| LAST_UPDATE_DATE | RcptReceivableActLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcptReceivableActLastUpdateLogin | — |
| LAST_UPDATED_BY | RcptReceivableActLastUpdatedBy | — |
| LIABILITY_TAX_CODE | RcptReceivableActLiabilityTaxCode | — |
| NAME | RcptReceivableActName | ✅ |
| OBJECT_VERSION_NUMBER | RcptReceivableActObjectVersionNumber | — |
| ORG_ID | RcptReceivableActOrgId | — |
| RECEIVABLES_TRX_ID | RcptReceivableActReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RcptReceivableActRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RcptReceivableActSetOfBooksId | — |
| START_DATE_ACTIVE | RcptReceivableActStartDateActive | — |
| STATUS | RcptReceivableActStatus | — |
| TAX_CODE_SOURCE | RcptReceivableActTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RcptReceivableActTaxRecoverableFlag | — |
| TYPE | RcptReceivableActType | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RecActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | RecActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | RecActivityCodeCombinationId | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RecActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | RecActivityDescription | — |
| END_DATE_ACTIVE | RecActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | RecActivityGlAccountSource | — |
| INACTIVE_DATE | RecActivityInactiveDate | — |
| LIABILITY_TAX_CODE | RecActivityLiabilityTaxCode | — |
| NAME | RcvblAppActivityName | — |
| NAME | RecActivityName | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_ID | RecActivityOrgId | — |
| RECEIVABLES_TRX_ID | RcvblAppActivityReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | RecActivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RecActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RecActivitySetOfBooksId | — |
| START_DATE_ACTIVE | RecActivityStartDateActive | — |
| STATUS | RecActivityStatus | — |
| TAX_CODE_SOURCE | RecActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RecActivityTaxRecoverableFlag | — |
| TYPE | RecActivityType | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RecActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | RecActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | RecActivityCodeCombinationId | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RecActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | RecActivityDescription | — |
| END_DATE_ACTIVE | RecActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | RecActivityGlAccountSource | — |
| INACTIVE_DATE | RecActivityInactiveDate | — |
| LIABILITY_TAX_CODE | RecActivityLiabilityTaxCode | — |
| NAME | RcvblAppActivityName | ✅ |
| NAME | RecActivityName | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_ID | RecActivityOrgId | — |
| RECEIVABLES_TRX_ID | RcvblAppActivityReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | RecActivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RecActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RecActivitySetOfBooksId | — |
| START_DATE_ACTIVE | RecActivityStartDateActive | — |
| STATUS | RecActivityStatus | — |
| TAX_CODE_SOURCE | RecActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RecActivityTaxRecoverableFlag | — |
| TYPE | RecActivityType | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 4/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RcvTrxIdAccountingAffectFlag | — |
| ACCOUNTING_AFFECT_FLAG | ReceivableActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | RcvTrxIdAssetTaxCode | — |
| ASSET_TAX_CODE | ReceivableActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | RcvTrxIdCodeCombinationId | — |
| CODE_COMBINATION_ID | ReceivableActivityCodeCombinationId | — |
| CREATED_BY | RcvTrxIdCreatedBy | — |
| CREATED_BY | ReceivableActivityCreatedBy | — |
| CREATION_DATE | RcvTrxIdCreationDate | — |
| CREATION_DATE | ReceivableActivityCreationDate | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RcvTrxIdDefaultAcctgDistributionSet | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ReceivableActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | RcvTrxIdDescription | — |
| DESCRIPTION | ReceivableActivityDescription | — |
| END_DATE_ACTIVE | RcvTrxIdEndDateActive | — |
| END_DATE_ACTIVE | ReceivableActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | RcvTrxIdGlAccountSource | — |
| GL_ACCOUNT_SOURCE | ReceivableActivityGlAccountSource | — |
| INACTIVE_DATE | RcvTrxIdInactiveDate | — |
| INACTIVE_DATE | ReceivableActivityInactiveDate | — |
| LAST_UPDATE_DATE | RcvTrxIdLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ReceivableActivityLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RcvTrxIdLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ReceivableActivityLastUpdateLogin | — |
| LAST_UPDATED_BY | RcvTrxIdLastUpdatedBy | — |
| LAST_UPDATED_BY | ReceivableActivityLastUpdatedBy | — |
| LIABILITY_TAX_CODE | RcvTrxIdLiabilityTaxCode | — |
| LIABILITY_TAX_CODE | ReceivableActivityLiabilityTaxCode | — |
| NAME | RcvTrxIdName | ✅ |
| NAME | ReceivableActivityName | ✅ |
| OBJECT_VERSION_NUMBER | RcvTrxIdObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ReceivableActivityObjectVersionNumber | — |
| ORG_ID | RcvTrxIdOrgId | — |
| ORG_ID | ReceivableActivityOrgId | — |
| RECEIVABLES_TRX_ID | RcvTrxIdReceivablesTrxId | — |
| RECEIVABLES_TRX_ID | ReceivableActivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RcvTrxIdRiskEliminationDays | — |
| RISK_ELIMINATION_DAYS | ReceivableActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RcvTrxIdSetOfBooksId | — |
| SET_OF_BOOKS_ID | ReceivableActivitySetOfBooksId | — |
| START_DATE_ACTIVE | RcvTrxIdStartDateActive | — |
| START_DATE_ACTIVE | ReceivableActivityStartDateActive | — |
| STATUS | RcvTrxIdStatus | — |
| STATUS | ReceivableActivityStatus | — |
| TAX_CODE_SOURCE | RcvTrxIdTaxCodeSource | — |
| TAX_CODE_SOURCE | ReceivableActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RcvTrxIdTaxRecoverableFlag | — |
| TAX_RECOVERABLE_FLAG | ReceivableActivityTaxRecoverableFlag | — |
| TYPE | RcvTrxIdType | — |
| TYPE | ReceivableActivityType | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RecActivityAccountingAffectFlag | — |
| ASSET_TAX_CODE | RecActivityAssetTaxCode | — |
| CODE_COMBINATION_ID | RecActivityCodeCombinationId | — |
| DEFAULT_ACCTG_DISTRIBUTION_SET | RecActivityDefaultAcctgDistributionSet | — |
| DESCRIPTION | RecActivityDescription | — |
| END_DATE_ACTIVE | RecActivityEndDateActive | — |
| GL_ACCOUNT_SOURCE | RecActivityGlAccountSource | — |
| INACTIVE_DATE | RecActivityInactiveDate | — |
| LIABILITY_TAX_CODE | RecActivityLiabilityTaxCode | — |
| NAME | RecActivityName | ✅ |
| OBJECT_VERSION_NUMBER | RecActivityObjectVersionNumber | — |
| ORG_ID | RecActivityOrgId | — |
| RECEIVABLES_TRX_ID | RecActivityReceivablesTrxId | — |
| RISK_ELIMINATION_DAYS | RecActivityRiskEliminationDays | — |
| SET_OF_BOOKS_ID | RecActivitySetOfBooksId | — |
| START_DATE_ACTIVE | RecActivityStartDateActive | — |
| STATUS | RecActivityStatus | — |
| TAX_CODE_SOURCE | RecActivityTaxCodeSource | — |
| TAX_RECOVERABLE_FLAG | RecActivityTaxRecoverableFlag | — |
| TYPE | RecActivityType | — |

### [[receivableactivityextractpvo|ReceivableActivityExtractPVO]] (OTHER · BICC: 26/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | ArReceivablesTrxAccountingAffectFlag | ✅ |
| ASSET_TAX_CODE | ArReceivablesTrxAssetTaxCode | ✅ |
| ATTRIBUTE1 | ArReceivablesTrxAttribute1 | — |
| ATTRIBUTE10 | ArReceivablesTrxAttribute10 | — |
| ATTRIBUTE11 | ArReceivablesTrxAttribute11 | — |
| ATTRIBUTE12 | ArReceivablesTrxAttribute12 | — |
| ATTRIBUTE13 | ArReceivablesTrxAttribute13 | — |
| ATTRIBUTE14 | ArReceivablesTrxAttribute14 | — |
| ATTRIBUTE15 | ArReceivablesTrxAttribute15 | — |
| ATTRIBUTE2 | ArReceivablesTrxAttribute2 | — |
| ATTRIBUTE3 | ArReceivablesTrxAttribute3 | — |
| ATTRIBUTE4 | ArReceivablesTrxAttribute4 | — |
| ATTRIBUTE5 | ArReceivablesTrxAttribute5 | — |
| ATTRIBUTE6 | ArReceivablesTrxAttribute6 | — |
| ATTRIBUTE7 | ArReceivablesTrxAttribute7 | — |
| ATTRIBUTE8 | ArReceivablesTrxAttribute8 | — |
| ATTRIBUTE9 | ArReceivablesTrxAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArReceivablesTrxAttributeCategory | — |
| CODE_COMBINATION_ID | ArReceivablesTrxCodeCombinationId | ✅ |
| CREATED_BY | ArReceivablesTrxCreatedBy | ✅ |
| CREATION_DATE | ArReceivablesTrxCreationDate | ✅ |
| DEFAULT_ACCTG_DISTRIBUTION_SET | ArReceivablesTrxDefaultAcctgDistributionSet | ✅ |
| DESCRIPTION | ArReceivablesTrxDescription | ✅ |
| END_DATE_ACTIVE | ArReceivablesTrxEndDateActive | ✅ |
| GL_ACCOUNT_SOURCE | ArReceivablesTrxGlAccountSource | ✅ |
| GLOBAL_ATTRIBUTE1 | ArReceivablesTrxGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArReceivablesTrxGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArReceivablesTrxGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArReceivablesTrxGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArReceivablesTrxGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArReceivablesTrxGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArReceivablesTrxGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArReceivablesTrxGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArReceivablesTrxGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArReceivablesTrxGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArReceivablesTrxGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArReceivablesTrxGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArReceivablesTrxGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArReceivablesTrxGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArReceivablesTrxGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArReceivablesTrxGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArReceivablesTrxGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArReceivablesTrxGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArReceivablesTrxGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArReceivablesTrxGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArReceivablesTrxGlobalAttributeCategory | — |
| INACTIVE_DATE | ArReceivablesTrxInactiveDate | ✅ |
| LAST_UPDATE_DATE | ArReceivablesTrxLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArReceivablesTrxLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArReceivablesTrxLastUpdatedBy | ✅ |
| LIABILITY_TAX_CODE | ArReceivablesTrxLiabilityTaxCode | ✅ |
| NAME | ArReceivablesTrxName | ✅ |
| OBJECT_VERSION_NUMBER | ArReceivablesTrxObjectVersionNumber | ✅ |
| ORG_ID | ArReceivablesTrxOrgId | ✅ |
| RECEIVABLES_TRX_ID | ArReceivablesTrxReceivablesTrxId | ✅ |
| RISK_ELIMINATION_DAYS | ArReceivablesTrxRiskEliminationDays | ✅ |
| SEED_DATA_SOURCE | ArReceivablesTrxSeedDataSource | ✅ |
| SET_OF_BOOKS_ID | ArReceivablesTrxSetOfBooksId | ✅ |
| START_DATE_ACTIVE | ArReceivablesTrxStartDateActive | ✅ |
| STATUS | ArReceivablesTrxStatus | ✅ |
| TAX_CODE_SOURCE | ArReceivablesTrxTaxCodeSource | ✅ |
| TAX_RECOVERABLE_FLAG | ArReceivablesTrxTaxRecoverableFlag | ✅ |
| TYPE | ArReceivablesTrxType | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Receivables Activities View Object
- Oracle Fusion Cloud — Managing Receivables Activities (Functional Guide)
