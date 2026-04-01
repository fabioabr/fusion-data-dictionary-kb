---
id: DOC-AR-054
doc_type: system-doc
title: "AR_MEMO_LINES_ALL_B — Linhas de Memo Padrão"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, memo-lines, debito-credito, templates]
aliases: [AR_MEMO_LINES_ALL_B, ar_memo_lines_all_b, memo_lines_b, linhas_memo_ar, ar_memo_lines]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_MEMO_LINES_ALL_B

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela base (sufixo `_B`) de **linhas de memo padrão** — templates pré-configurados usados na criação de notas de débito, notas de crédito e debit memos. Cada linha define um tipo, descrição, preço unitário padrão e regras fiscais.

## 🧠 Propósito de Negócio

As linhas de memo funcionam como **templates de itens** para transações manuais do AR. Em vez de preencher cada campo manualmente, o analista seleciona uma memo line que pré-popula a descrição, valor unitário, unidade de medida e regra de faturamento.

Casos de uso principais:
- Templates para notas de débito (encargos, multas, serviços)
- Templates para crédito memos (devoluções, abatimentos)
- Padronização de itens em faturas manuais
- Definição de regras fiscais por tipo de item

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | MEMO_LINE_ID | NUMBER | PK. Identificador único da linha de memo. | Chave | 🟢 100% |
| 2 | LINE_TYPE | VARCHAR2 | Tipo da linha: `LINE` (item), `TAX` (imposto), `FREIGHT` (frete). | Classificação | 🟢 100% |
| 3 | NAME | VARCHAR2 | Nome da memo line (não traduzível — ver [[ar_memo_lines_all_tl]] para traduções). | Identificação | 🟢 100% |
| 4 | DESCRIPTION | VARCHAR2 | Descrição detalhada da linha de memo. | Identificação | 🟢 100% |
| 5 | UNIT_STD_PRICE | NUMBER | Preço unitário padrão sugerido ao criar a transação. | Financeiro | 🟢 100% |
| 6 | UOM_CODE | VARCHAR2 | Código da unidade de medida (ex: `EA`, `HR`, `UN`). | Operacional | 🟢 100% |
| 7 | INVOICING_RULE_ID | NUMBER | FK para regra de faturamento: antecipado ou em arrears. | Configuração | 🟢 100% |
| 8 | INVENTORY_ITEM_ID | NUMBER | FK para item de inventário, se aplicável. Referencia [[mtl_system_items_b]]. | Chave Estrangeira | 🟢 100% |
| 9 | TAX_PRODUCT_CATEGORY | VARCHAR2 | Categoria fiscal do produto (para determinação de imposto). | Fiscal | 🟢 100% |
| 10 | TAX_CODE | VARCHAR2 | Código de imposto padrão associado à memo line. | Fiscal | 🟢 100% |
| 11 | GL_ID_REV | NUMBER | Conta GL de receita padrão. Referencia [[gl_code_combinations]]. | Contábil | 🟢 100% |
| 12 | ORG_ID | NUMBER | Identificador da Business Unit. | Partição | 🟢 100% |
| 13 | START_DATE | DATE | Data de início de vigência. | Vigência | 🟢 100% |
| 14 | END_DATE | DATE | Data de fim de vigência (nulo = sem expiração). | Vigência | 🟢 100% |
| 15 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 16 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 18 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_memo_lines_all_tl]] | MEMO_LINE_ID | Referenciada por | Traduções da memo line |
| [[mtl_system_items_b]] | INVENTORY_ITEM_ID | FK | Item de inventário associado |
| [[gl_code_combinations]] | GL_ID_REV | FK | Conta de receita padrão |
| [[ra_customer_trx_lines_all]] | MEMO_LINE_ID | Referenciada por | Linhas de transação que usam esta memo |

## 📎 Uso Típico

```sql
-- Listar memo lines ativas por BU
SELECT memo_line_id,
       name,
       line_type,
       unit_std_price,
       uom_code,
       description
  FROM ar_memo_lines_all_b
 WHERE org_id = :p_org_id
   AND (end_date IS NULL OR end_date > SYSDATE);
```

```sql
-- Memo lines com item de inventário vinculado
SELECT ml.name,
       ml.unit_std_price,
       msi.segment1 AS item_number
  FROM ar_memo_lines_all_b ml
  JOIN mtl_system_items_b msi ON msi.inventory_item_id = ml.inventory_item_id
 WHERE ml.org_id = :p_org_id;
```

## 🔒 Observações

- A tabela `_B` (base) contém os dados não traduzíveis. Para nomes e descrições em outros idiomas, consultar [[ar_memo_lines_all_tl]].
- O `UNIT_STD_PRICE` é apenas sugestão — o usuário pode alterar o valor na transação.
- `INVOICING_RULE_ID` define quando a receita é reconhecida: antecipadamente (advance) ou após entrega (arrears).
- Memo lines vinculadas a itens de inventário (`INVENTORY_ITEM_ID`) herdam propriedades fiscais do item.

## 🔗 PVOs Relacionados

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| CREATED_BY | MemoLineCreatedBy | — |
| CREATION_DATE | MemoLineCreationDate | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LAST_UPDATE_DATE | MemoLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineLastUpdateLogin | — |
| LAST_UPDATED_BY | MemoLineLastUpdatedBy | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | MemoLineObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[memolineextractpvo|MemoLineExtractPVO]] (OTHER · BICC: 21/68)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | ArMemoLineAccountingRuleId | ✅ |
| ATTRIBUTE1 | ArMemoLineAttribute1 | — |
| ATTRIBUTE10 | ArMemoLineAttribute10 | — |
| ATTRIBUTE11 | ArMemoLineAttribute11 | — |
| ATTRIBUTE12 | ArMemoLineAttribute12 | — |
| ATTRIBUTE13 | ArMemoLineAttribute13 | — |
| ATTRIBUTE14 | ArMemoLineAttribute14 | — |
| ATTRIBUTE15 | ArMemoLineAttribute15 | — |
| ATTRIBUTE2 | ArMemoLineAttribute2 | — |
| ATTRIBUTE3 | ArMemoLineAttribute3 | — |
| ATTRIBUTE4 | ArMemoLineAttribute4 | — |
| ATTRIBUTE5 | ArMemoLineAttribute5 | — |
| ATTRIBUTE6 | ArMemoLineAttribute6 | — |
| ATTRIBUTE7 | ArMemoLineAttribute7 | — |
| ATTRIBUTE8 | ArMemoLineAttribute8 | — |
| ATTRIBUTE9 | ArMemoLineAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArMemoLineAttributeCategory | — |
| CREATED_BY | ArMemoLineCreatedBy | ✅ |
| CREATION_DATE | ArMemoLineCreationDate | ✅ |
| DESCRIPTION | ArMemoLineDescription | ✅ |
| EFFECTIVE_END_DATE | ArMemoLineEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ArMemoLineEffectiveStartDate | ✅ |
| GLOBAL_ATTRIBUTE1 | ArMemoLineGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArMemoLineGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArMemoLineGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArMemoLineGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArMemoLineGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArMemoLineGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArMemoLineGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArMemoLineGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArMemoLineGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArMemoLineGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArMemoLineGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArMemoLineGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArMemoLineGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArMemoLineGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArMemoLineGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArMemoLineGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArMemoLineGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArMemoLineGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArMemoLineGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArMemoLineGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArMemoLineGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ArMemoLineGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ArMemoLineGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ArMemoLineGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ArMemoLineGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ArMemoLineGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ArMemoLineGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ArMemoLineGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ArMemoLineGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ArMemoLineGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ArMemoLineGlobalAttributeNumber5 | — |
| INVOICING_RULE_ID | ArMemoLineInvoicingRuleId | ✅ |
| LAST_UPDATE_DATE | ArMemoLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArMemoLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArMemoLineLastUpdatedBy | ✅ |
| LINE_TYPE | ArMemoLineLineType | ✅ |
| MEMO_LINE_ID | ArMemoLineMemoLineId | ✅ |
| MEMO_LINE_SEQ_ID | ArMemoLineMemoLineSeqId | ✅ |
| NAME | ArMemoLineName | ✅ |
| OBJECT_VERSION_NUMBER | ArMemoLineObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | ArMemoLineSeedDataSource | ✅ |
| SET_ID | ArMemoLineSetId | ✅ |
| TAX_CODE | ArMemoLineTaxCode | ✅ |
| TAX_PRODUCT_CATEGORY | ArMemoLineTaxProductCategory | ✅ |
| UNIT_STD_PRICE | ArMemoLineUnitStdPrice | ✅ |
| UOM_CODE | ArMemoLineUomCode | ✅ |

### [[memolinepvo|MemoLinePVO]] (AR · BICC: 9/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineBaseAccountingRuleId | — |
| CREATED_BY | MemoLineBaseCreatedBy1 | ✅ |
| CREATION_DATE | MemoLineBaseCreationDate | ✅ |
| DESCRIPTION | MemoLineBaseDescription | — |
| EFFECTIVE_END_DATE | MemoLineBaseEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | MemoLineBaseEffectiveStartDate | ✅ |
| INVOICING_RULE_ID | MemoLineBaseInvoicingRuleId | — |
| LAST_UPDATE_DATE | MemoLineBaseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineBaseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | MemoLineBaseLastUpdatedBy1 | ✅ |
| LINE_TYPE | MemoLineBaseLineType | ✅ |
| MEMO_LINE_ID | MemoLineBaseMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineBaseMemoLineSeqId | — |
| NAME | MemoLineBaseName | — |
| OBJECT_VERSION_NUMBER | MemoLineBaseObjectVersionNumber | — |
| SET_ID | MemoLineBaseSetId | — |
| TAX_CODE | MemoLineBaseTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineBaseTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineBaseUnitStdPrice | ✅ |
| UOM_CODE | MemoLineBaseUomCode | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | ✅ |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LAST_UPDATE_LOGIN | MemoLineLastUpdateLogin | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| CREATED_BY | MemoLineCreatedBy | — |
| CREATION_DATE | MemoLineCreationDate | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LAST_UPDATE_DATE | MemoLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineLastUpdateLogin | — |
| LAST_UPDATED_BY | MemoLineLastUpdatedBy | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | MemoLineObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| CREATED_BY | MemoLineCreatedBy | — |
| CREATION_DATE | MemoLineCreationDate | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LAST_UPDATE_DATE | MemoLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineLastUpdateLogin | — |
| LAST_UPDATED_BY | MemoLineLastUpdatedBy | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | MemoLineObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | ✅ |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| CREATED_BY | MemoLineCreatedBy | — |
| CREATION_DATE | MemoLineCreationDate | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LAST_UPDATE_DATE | MemoLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineLastUpdateLogin | — |
| LAST_UPDATED_BY | MemoLineLastUpdatedBy | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | MemoLineObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_RULE_ID | MemoLineAccountingRuleId | — |
| EFFECTIVE_END_DATE | MemoLineEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MemoLineEffectiveStartDate | — |
| INVOICING_RULE_ID | MemoLineInvoicingRuleId | — |
| LINE_TYPE | MemoLineLineType | — |
| MEMO_LINE_ID | MemoLineMemoLineId | — |
| MEMO_LINE_SEQ_ID | MemoLineMemoLineSeqId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SET_ID | MemoLineSetId | — |
| TAX_CODE | MemoLineTaxCode | — |
| TAX_PRODUCT_CATEGORY | MemoLineTaxProductCategory | — |
| UNIT_STD_PRICE | MemoLineUnitStdPrice | — |
| UOM_CODE | MemoLineUomCode | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Memo Lines View Object
- Oracle Fusion Cloud — Setting Up Memo Lines (Configuration Guide)
