---
id: DOC-AR-005
doc_type: system-doc
title: "RA_CUST_TRX_TYPES_ALL — Tipos de Transação AR"
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
  - tipos-transacao
  - configuracao
  - autoaccounting
aliases:
  - RA_CUST_TRX_TYPES_ALL
  - ra_cust_trx_types_all
  - tipos-transacao-ar
  - ar-transaction-types
  - trx-types-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_TRX_TYPES_ALL

## 📌 Visão Geral

Define os **tipos de transação** utilizados para faturas, notas de débito, notas de crédito, depósitos, garantias e duplicatas a receber (bills receivable) no módulo Accounts Receivable. Cada registro inclui configurações de **AutoAccounting** (contas contábeis padrão), comportamento de impressão, sinais contábeis e valores padrão para criação de transações.

É a tabela de **configuração central do AR** — determina como cada transação se comporta contabilmente e operacionalmente.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de transações:** Cada transação AR é associada a um tipo que define seu comportamento (fatura, credit memo, debit memo, etc.).
- **AutoAccounting:** Contas contábeis padrão (receita, recebível, frete, imposto, unbilled, unearned) são definidas por tipo de transação.
- **Regras de contabilização:** Controla se a transação será postada no GL (`POST_TO_GL`), se afeta saldo contábil, e qual o sinal de criação (positivo/negativo).
- **Impressão e comunicação:** Define opções padrão de impressão para faturas.
- **Filtros em relatórios:** Permite segmentar relatórios por tipo de transação (e.g., apenas credit memos).
- **Controle de funcionalidades:** Flags como `ALLOW_FREIGHT_FLAG`, `NATURAL_APPLICATION_ONLY_FLAG` controlam comportamentos específicos por tipo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_TRX_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de transação | — | 🟢 100% |
| 2 | NAME | VARCHAR2(20) | NOT NULL | Identificação | Nome do tipo de transação (visível ao usuário) | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(80) | NULL | Identificação | Descrição detalhada do tipo de transação | — | 🟢 100% |
| 4 | TYPE | VARCHAR2(20) | NOT NULL | Classificação | Categoria principal: INV, CM, DM, DEP, GUAR, BR | — | 🟢 100% |
| 5 | CLASS | VARCHAR2(20) | NULL | Classificação | Classe da transação (INV, CM, DM, DEP, GUAR, BR) | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do tipo (ativo/inativo) | — | 🟢 100% |
| 7 | POST_TO_GL | VARCHAR2(1) | NOT NULL | Contabilidade | Indica se transações deste tipo são postadas no GL (Y/N) | — | 🟢 100% |
| 8 | ACCOUNTING_AFFECT_FLAG | VARCHAR2(1) | NOT NULL | Contabilidade | Indica se afeta saldos contábeis (Y/N) | — | 🟢 100% |
| 9 | CREATION_SIGN | VARCHAR2(30) | NULL | Contabilidade | Sinal de criação: P (positivo), N (negativo), A (ambos) | — | 🟢 100% |
| 10 | ALLOW_FREIGHT_FLAG | VARCHAR2(1) | NULL | Configuração | Permite linhas de frete (Y/N) | — | 🟢 100% |
| 11 | ALLOW_OVERAPPLICATION_FLAG | VARCHAR2(1) | NULL | Configuração | Permite aplicação acima do saldo (Y/N) | — | 🟢 100% |
| 12 | NATURAL_APPLICATION_ONLY_FLAG | VARCHAR2(1) | NULL | Configuração | Restringe a aplicações naturais — invoice:receipt, CM:invoice (Y/N) | — | 🟢 100% |
| 13 | TAX_CALCULATION_FLAG | VARCHAR2(1) | NULL | Tributação | Indica se calcula imposto automaticamente (Y/N) | — | 🟢 100% |
| 14 | DEFAULT_TERM | NUMBER(18) | NULL | Financeiro | Condição de pagamento padrão | [[ra_terms_b]] | 🟢 100% |
| 15 | DEFAULT_PRINTING_OPTION | VARCHAR2(30) | NULL | Impressão | Opção de impressão padrão (PRI/NOT) | — | 🟢 100% |
| 16 | DEFAULT_STATUS | VARCHAR2(30) | NULL | Configuração | Status padrão para novas transações (OP=Open) | — | 🟢 100% |
| 17 | GL_ID_REV | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Receita | [[gl_code_combinations]] | 🟢 100% |
| 18 | GL_ID_REC | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Recebível | [[gl_code_combinations]] | 🟢 100% |
| 19 | GL_ID_FREIGHT | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Frete | [[gl_code_combinations]] | 🟢 100% |
| 20 | GL_ID_TAX | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Imposto | [[gl_code_combinations]] | 🟢 100% |
| 21 | GL_ID_UNBILLED | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Unbilled Receivable | [[gl_code_combinations]] | 🟢 100% |
| 22 | GL_ID_UNEARNED | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Unearned Revenue | [[gl_code_combinations]] | 🟢 100% |
| 23 | END_DATE | DATE | NULL | Configuração | Data de inativação do tipo de transação | — | 🟢 100% |
| 24 | START_DATE | DATE | NULL | Configuração | Data de ativação do tipo de transação | — | 🟢 100% |
| 25 | CREDIT_MEMO_TYPE_ID | NUMBER(18) | NULL | Referência cruzada | Tipo de credit memo padrão associado | self | 🟢 100% |
| 26 | SUBSEQUENT_TRX_TYPE_ID | NUMBER(18) | NULL | Referência cruzada | Tipo de transação subsequente (bills receivable) | self | 🟢 100% |
| 27 | RULE_SET_ID | NUMBER(18) | NULL | Configuração | Conjunto de regras de aplicação (matching rules) | — | 🟡 70% |
| 28 | SIGNED_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se requer assinatura (bills receivable) | — | 🟢 100% |
| 29 | DRAWEE_ISSUED_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se emitido pelo sacado (bills receivable) | — | 🟢 100% |
| 30 | MAGNETIC_FORMAT_CODE | VARCHAR2(30) | NULL | Configuração | Formato magnético para remessas bancárias | — | 🟡 65% |
| 31 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 32 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 33 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 34 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 35 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 36 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 37 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 38 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 39 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `GL_ID_REV`, `GL_ID_REC`, `GL_ID_FREIGHT`, `GL_ID_TAX`, `GL_ID_UNBILLED`, `GL_ID_UNEARNED` (contas padrão de AutoAccounting)
- [[ra_terms_b]] — via `DEFAULT_TERM` (condição de pagamento padrão)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do tipo de transação de AR)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `CUST_TRX_TYPE_ID` (transações que utilizam este tipo)
- [[ra_cust_trx_line_gl_dist_all]] — via `CUST_TRX_TYPE_ID` (distribuições contábeis, desnormalizado)

### Self-references
- `CREDIT_MEMO_TYPE_ID` — Tipo de credit memo padrão associado a este tipo de fatura
- `SUBSEQUENT_TRX_TYPE_ID` — Tipo de transação subsequente (usado em fluxos de bills receivable)

---

## 📎 Uso Típico

### Listar todos os tipos de transação ativos
```sql
SELECT CUST_TRX_TYPE_ID, NAME, DESCRIPTION, TYPE, CLASS,
       POST_TO_GL, CREATION_SIGN
FROM   RA_CUST_TRX_TYPES_ALL
WHERE  ORG_ID = :p_org_id
  AND  (END_DATE IS NULL OR END_DATE > SYSDATE)
ORDER BY TYPE, NAME;
```

### Transações por tipo (volume e valor)
```sql
SELECT tt.NAME AS tipo_transacao, tt.TYPE,
       COUNT(*) AS qtd_transacoes,
       SUM(ctl.EXTENDED_AMOUNT) AS valor_total
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_CUST_TRX_TYPES_ALL tt
       ON tt.CUST_TRX_TYPE_ID = ct.CUST_TRX_TYPE_ID
JOIN   RA_CUSTOMER_TRX_LINES_ALL ctl
       ON ctl.CUSTOMER_TRX_ID = ct.CUSTOMER_TRX_ID
       AND ctl.LINE_TYPE = 'LINE'
WHERE  ct.ORG_ID = :p_org_id
GROUP BY tt.NAME, tt.TYPE;
```

### Filtros comuns
- `TYPE = 'INV'` — Apenas tipos de fatura
- `TYPE = 'CM'` — Apenas tipos de credit memo
- `TYPE = 'DM'` — Apenas tipos de debit memo
- `TYPE = 'BR'` — Apenas tipos de bills receivable
- `POST_TO_GL = 'Y'` — Tipos que geram lançamento contábil

---

## 🔒 Observações

- A coluna `TYPE` define a categoria funcional: **INV** (Invoice), **CM** (Credit Memo), **DM** (Debit Memo), **DEP** (Deposit), **GUAR** (Guarantee), **BR** (Bills Receivable).
- `CREATION_SIGN` controla o sinal do valor: **P** = apenas positivos, **N** = apenas negativos, **A** = ambos. Credit memos tipicamente têm `CREATION_SIGN = 'A'` ou `'N'`.
- Os campos `GL_ID_*` definem as **contas de AutoAccounting** por tipo de transação. Essas contas servem como template para as distribuições contábeis em [[ra_cust_trx_line_gl_dist_all]].
- O campo `CREDIT_MEMO_TYPE_ID` permite que um tipo de fatura tenha um tipo de credit memo padrão associado, facilitando a criação de notas de crédito.
- Tipos de **Bills Receivable** utilizam campos específicos como `SIGNED_FLAG`, `DRAWEE_ISSUED_FLAG` e `MAGNETIC_FORMAT_CODE` para controle de duplicatas bancárias.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15` para customizações por implementação.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | ✅ |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | — |
| DESCRIPTION | TransactionTypeDescription | ✅ |
| NAME | TransactionTypeName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber11 | — |
| POST_TO_GL | TransactionTypePostToGl | ✅ |
| TYPE | TransactionTypeType | ✅ |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | ✅ |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | — |
| DESCRIPTION | TransactionTypeDescription | ✅ |
| NAME | TransactionTypeName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber7 | — |
| POST_TO_GL | TransactionTypePostToGl | ✅ |
| TYPE | TransactionTypeType | ✅ |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_TRX_TYPE_SEQ_ID | CustTrxTypeSeqId | — |
| DESCRIPTION | TransactionTypePEODescription | ✅ |
| NAME | TransactionTypePEOName | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber7 | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CUST_TRX_TYPE_SEQ_ID | CustTrxTypeSeqId | — |
| DESCRIPTION | TransactionTypeDescription | ✅ |
| NAME | TransactionTypeName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber5 | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 4/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | — |
| ACCOUNTING_AFFECT_FLAG | TransactionTypeSchedAccountingAffectFlag | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeAllocateTaxFreight | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeSchedAllocateTaxFreight | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeAllowFreightFlag | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeSchedAllowFreightFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeAllowOverapplicationFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeSchedAllowOverapplicationFlag | — |
| CREATED_BY | TransactionTypeCreatedBy | — |
| CREATED_BY | TransactionTypeSchedCreatedBy | — |
| CREATION_DATE | TransactionTypeCreationDate | — |
| CREATION_DATE | TransactionTypeSchedCreationDate | — |
| CREATION_SIGN | TransactionTypeCreationSign | — |
| CREATION_SIGN | TransactionTypeSchedCreationSign | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeSchedCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeCreditMemoTypeSeqId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeSchedCreditMemoTypeSeqId | — |
| CUST_TRX_TYPE_ID | TransactionTypeCustTrxTypeId | ✅ |
| CUST_TRX_TYPE_ID | TransactionTypeSchedCustTrxTypeId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | ✅ |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeSchedCustTrxTypeSeqId | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeDefaultPrintingOption | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeSchedDefaultPrintingOption | — |
| DEFAULT_STATUS | TransactionTypeDefaultStatus | — |
| DEFAULT_STATUS | TransactionTypeSchedDefaultStatus | — |
| DEFAULT_TERM | TransactionTypeDefaultTerm | — |
| DEFAULT_TERM | TransactionTypeSchedDefaultTerm | — |
| DESCRIPTION | TransactionTypeDescription | — |
| DESCRIPTION | TransactionTypeSchedDescription | — |
| DOCUMENT_TYPE | TransactionTypeDocumentType | — |
| DOCUMENT_TYPE | TransactionTypeSchedDocumentType | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeDraweeIssuedFlag | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeSchedDraweeIssuedFlag | — |
| END_DATE | TransactionTypeEndDate | — |
| END_DATE | TransactionTypeSchedEndDate | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeExcludeFromLateCharges | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeSchedExcludeFromLateCharges | — |
| FORMAT_PROGRAM_ID | TransactionTypeFormatProgramId | — |
| FORMAT_PROGRAM_ID | TransactionTypeSchedFormatProgramId | — |
| LAST_UPDATE_DATE | TransactionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionTypeSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionTypeSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionTypeSchedLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionTypeLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionTypeSchedLegalEntityId | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeMagneticFormatCode | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeSchedMagneticFormatCode | — |
| NAME | TransactionTypeName | — |
| NAME | TransactionTypeSchedName | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeNaturalApplicationOnlyFlag | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeSchedNaturalApplicationOnlyFlag | — |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionTypeSchedObjectVersionNumber | — |
| POST_TO_GL | TransactionTypePostToGl | — |
| POST_TO_GL | TransactionTypeSchedPostToGl | — |
| RULE_SET_ID | TransactionTypeRuleSetId | — |
| RULE_SET_ID | TransactionTypeSchedRuleSetId | — |
| SET_ID | TransactionTypeSchedSetId | — |
| SET_ID | TransactionTypeSetId | — |
| SIGNED_FLAG | TransactionTypeSchedSignedFlag | — |
| SIGNED_FLAG | TransactionTypeSignedFlag | — |
| START_DATE | TransactionTypeSchedStartDate | — |
| START_DATE | TransactionTypeStartDate | — |
| STATUS | TransactionTypeSchedStatus | — |
| STATUS | TransactionTypeStatus | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSchedSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSchedSubsequentTrxTypeSeqId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSubsequentTrxTypeSeqId | — |
| TAX_CALCULATION_FLAG | TransactionTypeSchedTaxCalculationFlag | — |
| TAX_CALCULATION_FLAG | TransactionTypeTaxCalculationFlag | — |
| TYPE | TransactionTypeSchedType | — |
| TYPE | TransactionTypeType | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 2/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | — |
| ACCOUNTING_AFFECT_FLAG | TransactionTypeSchedAccountingAffectFlag | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeAllocateTaxFreight | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeSchedAllocateTaxFreight | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeAllowFreightFlag | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeSchedAllowFreightFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeAllowOverapplicationFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeSchedAllowOverapplicationFlag | — |
| CREATED_BY | TransactionTypeCreatedBy | — |
| CREATED_BY | TransactionTypeSchedCreatedBy | — |
| CREATION_DATE | TransactionTypeCreationDate | — |
| CREATION_DATE | TransactionTypeSchedCreationDate | — |
| CREATION_SIGN | TransactionTypeCreationSign | — |
| CREATION_SIGN | TransactionTypeSchedCreationSign | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeSchedCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeCreditMemoTypeSeqId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeSchedCreditMemoTypeSeqId | — |
| CUST_TRX_TYPE_ID | TransactionTypeCustTrxTypeId | — |
| CUST_TRX_TYPE_ID | TransactionTypeSchedCustTrxTypeId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeSchedCustTrxTypeSeqId | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeDefaultPrintingOption | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeSchedDefaultPrintingOption | — |
| DEFAULT_STATUS | TransactionTypeDefaultStatus | — |
| DEFAULT_STATUS | TransactionTypeSchedDefaultStatus | — |
| DEFAULT_TERM | TransactionTypeDefaultTerm | — |
| DEFAULT_TERM | TransactionTypeSchedDefaultTerm | — |
| DESCRIPTION | TransactionTypeDescription | — |
| DESCRIPTION | TransactionTypeSchedDescription | — |
| DOCUMENT_TYPE | TransactionTypeDocumentType | — |
| DOCUMENT_TYPE | TransactionTypeSchedDocumentType | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeDraweeIssuedFlag | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeSchedDraweeIssuedFlag | — |
| END_DATE | TransactionTypeEndDate | — |
| END_DATE | TransactionTypeSchedEndDate | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeExcludeFromLateCharges | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeSchedExcludeFromLateCharges | — |
| FORMAT_PROGRAM_ID | TransactionTypeFormatProgramId | — |
| FORMAT_PROGRAM_ID | TransactionTypeSchedFormatProgramId | — |
| LAST_UPDATE_DATE | TransactionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionTypeSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionTypeSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionTypeSchedLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionTypeLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionTypeSchedLegalEntityId | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeMagneticFormatCode | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeSchedMagneticFormatCode | — |
| NAME | TransactionTypeName | — |
| NAME | TransactionTypeSchedName | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeNaturalApplicationOnlyFlag | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeSchedNaturalApplicationOnlyFlag | — |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionTypeSchedObjectVersionNumber | — |
| POST_TO_GL | TransactionTypePostToGl | — |
| POST_TO_GL | TransactionTypeSchedPostToGl | — |
| RULE_SET_ID | TransactionTypeRuleSetId | — |
| RULE_SET_ID | TransactionTypeSchedRuleSetId | — |
| SET_ID | TransactionTypeSchedSetId | — |
| SET_ID | TransactionTypeSetId | — |
| SIGNED_FLAG | TransactionTypeSchedSignedFlag | — |
| SIGNED_FLAG | TransactionTypeSignedFlag | — |
| START_DATE | TransactionTypeSchedStartDate | — |
| START_DATE | TransactionTypeStartDate | — |
| STATUS | TransactionTypeSchedStatus | — |
| STATUS | TransactionTypeStatus | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSchedSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSchedSubsequentTrxTypeSeqId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSubsequentTrxTypeSeqId | — |
| TAX_CALCULATION_FLAG | TransactionTypeSchedTaxCalculationFlag | — |
| TAX_CALCULATION_FLAG | TransactionTypeTaxCalculationFlag | — |
| TYPE | TransactionTypeSchedType | — |
| TYPE | TransactionTypeType | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 2/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | — |
| ACCOUNTING_AFFECT_FLAG | TransactionTypeSchedAccountingAffectFlag | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeAllocateTaxFreight | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeSchedAllocateTaxFreight | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeAllowFreightFlag | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeSchedAllowFreightFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeAllowOverapplicationFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeSchedAllowOverapplicationFlag | — |
| CREATED_BY | TransactionTypeCreatedBy | — |
| CREATED_BY | TransactionTypeSchedCreatedBy | — |
| CREATION_DATE | TransactionTypeCreationDate | — |
| CREATION_DATE | TransactionTypeSchedCreationDate | — |
| CREATION_SIGN | TransactionTypeCreationSign | — |
| CREATION_SIGN | TransactionTypeSchedCreationSign | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeSchedCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeCreditMemoTypeSeqId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeSchedCreditMemoTypeSeqId | — |
| CUST_TRX_TYPE_ID | TransactionTypeCustTrxTypeId | — |
| CUST_TRX_TYPE_ID | TransactionTypeSchedCustTrxTypeId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeSchedCustTrxTypeSeqId | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeDefaultPrintingOption | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeSchedDefaultPrintingOption | — |
| DEFAULT_STATUS | TransactionTypeDefaultStatus | — |
| DEFAULT_STATUS | TransactionTypeSchedDefaultStatus | — |
| DEFAULT_TERM | TransactionTypeDefaultTerm | — |
| DEFAULT_TERM | TransactionTypeSchedDefaultTerm | — |
| DESCRIPTION | TransactionTypeDescription | — |
| DESCRIPTION | TransactionTypeSchedDescription | — |
| DOCUMENT_TYPE | TransactionTypeDocumentType | — |
| DOCUMENT_TYPE | TransactionTypeSchedDocumentType | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeDraweeIssuedFlag | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeSchedDraweeIssuedFlag | — |
| END_DATE | TransactionTypeEndDate | — |
| END_DATE | TransactionTypeSchedEndDate | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeExcludeFromLateCharges | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeSchedExcludeFromLateCharges | — |
| FORMAT_PROGRAM_ID | TransactionTypeFormatProgramId | — |
| FORMAT_PROGRAM_ID | TransactionTypeSchedFormatProgramId | — |
| LAST_UPDATE_DATE | TransactionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionTypeSchedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionTypeSchedLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionTypeSchedLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionTypeLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionTypeSchedLegalEntityId | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeMagneticFormatCode | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeSchedMagneticFormatCode | — |
| NAME | TransactionTypeName | — |
| NAME | TransactionTypeSchedName | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeNaturalApplicationOnlyFlag | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeSchedNaturalApplicationOnlyFlag | — |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionTypeSchedObjectVersionNumber | — |
| POST_TO_GL | TransactionTypePostToGl | — |
| POST_TO_GL | TransactionTypeSchedPostToGl | — |
| RULE_SET_ID | TransactionTypeRuleSetId | — |
| RULE_SET_ID | TransactionTypeSchedRuleSetId | — |
| SET_ID | TransactionTypeSchedSetId | — |
| SET_ID | TransactionTypeSetId | — |
| SIGNED_FLAG | TransactionTypeSchedSignedFlag | — |
| SIGNED_FLAG | TransactionTypeSignedFlag | — |
| START_DATE | TransactionTypeSchedStartDate | — |
| START_DATE | TransactionTypeStartDate | — |
| STATUS | TransactionTypeSchedStatus | — |
| STATUS | TransactionTypeStatus | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSchedSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSchedSubsequentTrxTypeSeqId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSubsequentTrxTypeSeqId | — |
| TAX_CALCULATION_FLAG | TransactionTypeSchedTaxCalculationFlag | — |
| TAX_CALCULATION_FLAG | TransactionTypeTaxCalculationFlag | — |
| TYPE | TransactionTypeSchedType | — |
| TYPE | TransactionTypeType | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR · BICC: 3/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | — |
| ALLOCATE_TAX_FREIGHT | TransactionTypeAllocateTaxFreight | — |
| ALLOW_FREIGHT_FLAG | TransactionTypeAllowFreightFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeAllowOverapplicationFlag | — |
| CREATED_BY | TransactionTypeCreatedBy | — |
| CREATION_DATE | TransactionTypeCreationDate | — |
| CREATION_SIGN | TransactionTypeCreationSign | — |
| CREDIT_MEMO_TYPE_ID | TransactionTypeCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeCreditMemoTypeSeqId | — |
| CUST_TRX_TYPE_ID | TransactionTypeCustTrxTypeId | — |
| CUST_TRX_TYPE_SEQ_ID | TransactionTypeCustTrxTypeSeqId | — |
| DEFAULT_PRINTING_OPTION | TransactionTypeDefaultPrintingOption | — |
| DEFAULT_STATUS | TransactionTypeDefaultStatus | — |
| DEFAULT_TERM | TransactionTypeDefaultTerm | — |
| DESCRIPTION | TransactionTypeDescription | — |
| DOCUMENT_TYPE | TransactionTypeDocumentType | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeDraweeIssuedFlag | — |
| END_DATE | TransactionTypeEndDate | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeExcludeFromLateCharges | — |
| FORMAT_PROGRAM_ID | TransactionTypeFormatProgramId | — |
| LAST_UPDATE_DATE | TransactionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTypeLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | TransactionTypeLegalEntityId | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeMagneticFormatCode | — |
| NAME | TransactionTypeName | — |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeNaturalApplicationOnlyFlag | — |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber | — |
| POST_TO_GL | TransactionTypePostToGl | — |
| RULE_SET_ID | TransactionTypeRuleSetId | — |
| SET_ID | TransactionTypeSetId | — |
| SIGNED_FLAG | TransactionTypeSignedFlag | — |
| START_DATE | TransactionTypeStartDate | — |
| STATUS | TransactionTypeStatus | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSubsequentTrxTypeId | — |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSubsequentTrxTypeSeqId | — |
| TAX_CALCULATION_FLAG | TransactionTypeTaxCalculationFlag | — |
| TYPE | TransactionTypeType | ✅ |

### [[transactiontypeextractpvo|TransactionTypeExtractPVO]] (OTHER · BICC: 41/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | RaCustTrxTypeAccountingAffectFlag | ✅ |
| ALLOCATE_TAX_FREIGHT | RaCustTrxTypeAllocateTaxFreight | ✅ |
| ALLOW_FREIGHT_FLAG | RaCustTrxTypeAllowFreightFlag | ✅ |
| ALLOW_FUTURE_ACCT_DATE_FLAG | RaCustTrxTypeAllowFutureAcctDateFlag | ✅ |
| ALLOW_OVERAPPLICATION_FLAG | RaCustTrxTypeAllowOverapplicationFlag | ✅ |
| ATTRIBUTE1 | RaCustTrxTypeAttribute1 | — |
| ATTRIBUTE10 | RaCustTrxTypeAttribute10 | — |
| ATTRIBUTE11 | RaCustTrxTypeAttribute11 | — |
| ATTRIBUTE12 | RaCustTrxTypeAttribute12 | — |
| ATTRIBUTE13 | RaCustTrxTypeAttribute13 | — |
| ATTRIBUTE14 | RaCustTrxTypeAttribute14 | — |
| ATTRIBUTE15 | RaCustTrxTypeAttribute15 | — |
| ATTRIBUTE2 | RaCustTrxTypeAttribute2 | — |
| ATTRIBUTE3 | RaCustTrxTypeAttribute3 | — |
| ATTRIBUTE4 | RaCustTrxTypeAttribute4 | — |
| ATTRIBUTE5 | RaCustTrxTypeAttribute5 | — |
| ATTRIBUTE6 | RaCustTrxTypeAttribute6 | — |
| ATTRIBUTE7 | RaCustTrxTypeAttribute7 | — |
| ATTRIBUTE8 | RaCustTrxTypeAttribute8 | — |
| ATTRIBUTE9 | RaCustTrxTypeAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaCustTrxTypeAttributeCategory | — |
| CONTROL_COMPLETION_LEVEL_CODE | RaCustTrxTypeControlCompletionLevelCode | ✅ |
| CREATED_BY | RaCustTrxTypeCreatedBy | ✅ |
| CREATION_DATE | RaCustTrxTypeCreationDate | ✅ |
| CREATION_SIGN | RaCustTrxTypeCreationSign | ✅ |
| CREDIT_MEMO_TYPE_ID | RaCustTrxTypeCreditMemoTypeId | ✅ |
| CREDIT_MEMO_TYPE_SEQ_ID | RaCustTrxTypeCreditMemoTypeSeqId | ✅ |
| CUST_TRX_TYPE_ID | RaCustTrxTypeCustTrxTypeId | ✅ |
| CUST_TRX_TYPE_SEQ_ID | RaCustTrxTypeCustTrxTypeSeqId | ✅ |
| DEFAULT_PRINTING_OPTION | RaCustTrxTypeDefaultPrintingOption | ✅ |
| DEFAULT_STATUS | RaCustTrxTypeDefaultStatus | ✅ |
| DEFAULT_TERM | RaCustTrxTypeDefaultTerm | ✅ |
| DESCRIPTION | RaCustTrxTypeDescription | ✅ |
| DOCUMENT_TYPE | RaCustTrxTypeDocumentType | ✅ |
| DRAWEE_ISSUED_FLAG | RaCustTrxTypeDraweeIssuedFlag | ✅ |
| END_DATE | RaCustTrxTypeEndDate | ✅ |
| EXCLUDE_FROM_LATE_CHARGES | RaCustTrxTypeExcludeFromLateCharges | ✅ |
| FORMAT_PROGRAM_ID | RaCustTrxTypeFormatProgramId | ✅ |
| GLOBAL_ATTRIBUTE1 | RaCustTrxTypeGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | RaCustTrxTypeGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | RaCustTrxTypeGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | RaCustTrxTypeGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | RaCustTrxTypeGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | RaCustTrxTypeGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | RaCustTrxTypeGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | RaCustTrxTypeGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | RaCustTrxTypeGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | RaCustTrxTypeGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | RaCustTrxTypeGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | RaCustTrxTypeGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | RaCustTrxTypeGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | RaCustTrxTypeGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | RaCustTrxTypeGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | RaCustTrxTypeGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | RaCustTrxTypeGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | RaCustTrxTypeGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | RaCustTrxTypeGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | RaCustTrxTypeGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | RaCustTrxTypeGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | RaCustTrxTypeGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | RaCustTrxTypeGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | RaCustTrxTypeGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | RaCustTrxTypeGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | RaCustTrxTypeGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | RaCustTrxTypeGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | RaCustTrxTypeGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | RaCustTrxTypeGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | RaCustTrxTypeGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | RaCustTrxTypeGlobalAttributeNumber5 | — |
| LAST_UPDATE_DATE | RaCustTrxTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaCustTrxTypeLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaCustTrxTypeLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | RaCustTrxTypeLegalEntityId | ✅ |
| MAGNETIC_FORMAT_CODE | RaCustTrxTypeMagneticFormatCode | ✅ |
| NAME | RaCustTrxTypeName | ✅ |
| NATURAL_APPLICATION_ONLY_FLAG | RaCustTrxTypeNaturalApplicationOnlyFlag | ✅ |
| OBJECT_VERSION_NUMBER | RaCustTrxTypeObjectVersionNumber | ✅ |
| POST_TO_GL | RaCustTrxTypePostToGl | ✅ |
| RULE_SET_ID | RaCustTrxTypeRuleSetId | ✅ |
| SET_ID | RaCustTrxTypeSetId | ✅ |
| SIGNED_FLAG | RaCustTrxTypeSignedFlag | ✅ |
| START_DATE | RaCustTrxTypeStartDate | ✅ |
| STATUS | RaCustTrxTypeStatus | ✅ |
| SUBSEQUENT_TRX_TYPE_ID | RaCustTrxTypeSubsequentTrxTypeId | ✅ |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | RaCustTrxTypeSubsequentTrxTypeSeqId | ✅ |
| TAX_CALCULATION_FLAG | RaCustTrxTypeTaxCalculationFlag | ✅ |
| TYPE | RaCustTrxTypeType | ✅ |
| USAGE_CATEGORY_CODE | RaCustTrxTypeUsageCategoryCode | ✅ |

### [[transactiontypepvo|TransactionTypePVO]] (AR · BICC: 19/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_AFFECT_FLAG | TransactionTypeAccountingAffectFlag | ✅ |
| ALLOCATE_TAX_FREIGHT | TransactionTypeAllocateTaxFreight | ✅ |
| ALLOW_FREIGHT_FLAG | TransactionTypeAllowFreightFlag | — |
| ALLOW_OVERAPPLICATION_FLAG | TransactionTypeAllowOverapplicationFlag | ✅ |
| CONTROL_COMPLETION_LEVEL_CODE | TransactionTypeControlCompletionLevelCode | — |
| CREATED_BY | TransactionTypeCreatedBy | ✅ |
| CREATION_DATE | TransactionTypeCreationDate | ✅ |
| CREATION_SIGN | TransactionTypeCreationSign | ✅ |
| CREDIT_MEMO_TYPE_ID | TransactionTypeCreditMemoTypeId | — |
| CREDIT_MEMO_TYPE_SEQ_ID | TransactionTypeCreditMemoTypeSeqId | — |
| CUST_TRX_TYPE_ID | TransactionTypeCustTrxTypeId | ✅ |
| CUST_TRX_TYPE_SEQ_ID | CustTrxTypeSeqId | ✅ |
| DEFAULT_PRINTING_OPTION | TransactionTypeDefaultPrintingOption | — |
| DEFAULT_STATUS | TransactionTypeDefaultStatus | — |
| DEFAULT_TERM | TransactionTypeDefaultTerm | — |
| DESCRIPTION | TransactionTypeDescription | ✅ |
| DOCUMENT_TYPE | TransactionTypeDocumentType | — |
| DRAWEE_ISSUED_FLAG | TransactionTypeDraweeIssuedFlag | ✅ |
| END_DATE | TransactionTypeEndDate | — |
| EXCLUDE_FROM_LATE_CHARGES | TransactionTypeExcludeFromLateCharges | — |
| FORMAT_PROGRAM_ID | TransactionTypeFormatProgramId | — |
| LAST_UPDATE_DATE | TransactionTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTypeLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | TransactionTypeLegalEntityId | — |
| MAGNETIC_FORMAT_CODE | TransactionTypeMagneticFormatCode | — |
| NAME | TransactionTypeName | ✅ |
| NATURAL_APPLICATION_ONLY_FLAG | TransactionTypeNaturalApplicationOnlyFlag | ✅ |
| OBJECT_VERSION_NUMBER | TransactionTypeObjectVersionNumber | — |
| POST_TO_GL | TransactionTypePostToGl | ✅ |
| RULE_SET_ID | TransactionTypeRuleSetId | — |
| SET_ID | TransactionTypeSetId | — |
| SIGNED_FLAG | TransactionTypeSignedFlag | ✅ |
| START_DATE | TransactionTypeStartDate | — |
| STATUS | TransactionTypeStatus | — |
| SUBSEQUENT_TRX_TYPE_ID | TransactionTypeSubsequentTrxTypeId | ✅ |
| SUBSEQUENT_TRX_TYPE_SEQ_ID | TransactionTypeSubsequentTrxTypeSeqId | — |
| TAX_CALCULATION_FLAG | TransactionTypeTaxCalculationFlag | ✅ |
| TYPE | TransactionTypeType | ✅ |
| USAGE_CATEGORY_CODE | TransactionTypeUsageCategoryCode | — |

---

## 📚 Referências

- [Oracle Docs — RA_CUST_TRX_TYPES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racusttrxtypesall-25250.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
