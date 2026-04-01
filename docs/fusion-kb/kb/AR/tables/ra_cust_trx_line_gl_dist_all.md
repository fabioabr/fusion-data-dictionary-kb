---
id: DOC-AR-003
doc_type: system-doc
title: "RA_CUST_TRX_LINE_GL_DIST_ALL — Distribuições Contábeis AR"
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
  - distribuicoes-contabeis
  - reconciliacao-gl
  - accounting
aliases:
  - RA_CUST_TRX_LINE_GL_DIST_ALL
  - ra_cust_trx_line_gl_dist_all
  - distribuicoes-ar
  - ar-gl-distributions
  - dist-contabeis-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_TRX_LINE_GL_DIST_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** (accounting distributions) das linhas de transação do módulo Accounts Receivable. Liga cada linha de transação às combinações de contas contábeis do General Ledger, permitindo a reconciliação entre AR e GL. Cada linha de transação pode ter múltiplas distribuições, categorizadas por `ACCOUNT_CLASS` (receita, recebível, frete, imposto, etc.).

É a tabela que faz a **ponte entre AR e GL** — indispensável para auditoria contábil e reconciliação de saldos.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconciliação AR × GL:** Cada valor de transação é distribuído para contas contábeis específicas, permitindo conferência entre saldos do subledger e do General Ledger.
- **Análise de receita por conta contábil:** Identificação de receita por centro de custo, departamento ou segmento contábil.
- **Auditoria de lançamentos:** Rastreamento completo de quais contas foram impactadas por cada transação.
- **Posting para GL:** O campo `GL_POSTED_DATE` indica quando a distribuição foi transferida ao General Ledger.
- **Revenue scheduling:** Distribuições com `ACCOUNT_CLASS = 'UNEARN'` ou `'UNBILL'` suportam reconhecimento de receita diferido.
- **AutoAccounting:** As contas são determinadas automaticamente com base nas regras de AutoAccounting configuradas no tipo de transação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_TRX_LINE_GL_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição contábil | — | 🟢 100% |
| 2 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Referência à linha da transação | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 3 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Referência ao cabeçalho da transação | [[ra_customer_trx_all]] | 🟢 100% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (segmentos GL) | [[gl_code_combinations]] | 🟢 100% |
| 5 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição na moeda da transação | — | 🟢 100% |
| 6 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição na moeda funcional (ledger) | — | 🟢 100% |
| 7 | PERCENT | NUMBER | NULL | Financeiro | Percentual da distribuição em relação ao total da linha | — | 🟢 100% |
| 8 | ACCOUNT_CLASS | VARCHAR2(20) | NOT NULL | Classificação | Classe da conta: REV, REC, FREIGHT, TAX, UNBILL, UNEARN, SUSPENSE, ROUND | — | 🟢 100% |
| 9 | ACCOUNT_SET_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Y = modelo de conta (template); N = distribuição real | — | 🟢 100% |
| 10 | GL_DATE | DATE | NULL | Contabilidade | Data contábil da distribuição (período GL) | — | 🟢 100% |
| 11 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi postada no General Ledger | — | 🟢 100% |
| 12 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do controle de posting (-1 = não postado, -2 = não precisa postar, >0 = postado) | — | 🟢 100% |
| 13 | LATEST_REC_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição mais recente do recebível (para ACCOUNT_CLASS = REC) | — | 🟢 100% |
| 14 | ORIGINAL_GL_DATE | DATE | NULL | Contabilidade | Data GL original (antes de repostagem) | — | 🟢 100% |
| 15 | CUST_TRX_TYPE_ID | NUMBER(18) | NULL | Classificação | Tipo da transação (desnormalizado do cabeçalho) | [[ra_cust_trx_types_all]] | 🟢 100% |
| 16 | COLLECTED_TAX_CCID | NUMBER(18) | NULL | Tributação | Combinação de contas para imposto coletado | [[gl_code_combinations]] | 🟡 70% |
| 17 | COLLECTED_TAX_CONCAT_SEG | VARCHAR2(240) | NULL | Tributação | Segmentos concatenados da conta de imposto coletado | — | 🟡 65% |
| 18 | REVENUE_ADJUSTMENT_ID | NUMBER(18) | NULL | Contabilidade | ID do ajuste de receita (Revenue Adjustment) | — | 🟢 100% |
| 19 | REC_OFFSET_FLAG | VARCHAR2(1) | NULL | Classificação | Flag de offset do recebível | — | 🟡 65% |
| 20 | EVENT_ID | NUMBER(18) | NULL | Contabilidade | ID do evento contábil (Subledger Accounting / SLA) | — | 🟢 100% |
| 21 | USER_GENERATED_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição criada manualmente pelo usuário | — | 🟢 100% |
| 22 | ROUNDING_CORRECTION_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição de correção de arredondamento | — | 🟢 100% |
| 23 | CCID_CHANGE_FLAG | VARCHAR2(1) | NULL | Classificação | Y = conta contábil foi alterada manualmente | — | 🟡 70% |
| 24 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 25 | COMMENTS | VARCHAR2(240) | NULL | Texto livre | Comentários da distribuição | — | 🟢 100% |
| 26 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 27 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 28 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 29 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 30 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 31 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 32 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 33 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (cabeçalho da transação)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha da transação)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição da linha de transação)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo da transação)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição contábil da transação)

### Tabelas-filha (FK de saída)
- [[xla_ae_lines]] — via `EVENT_ID` (linhas de diário do Subledger Accounting)
- [[xla_events]] — via `EVENT_ID` (eventos contábeis SLA)

---

## 📎 Uso Típico

### Reconciliação AR × GL por conta contábil
```sql
SELECT gcc.SEGMENT1 || '-' || gcc.SEGMENT2 || '-' || gcc.SEGMENT3 AS conta,
       dist.ACCOUNT_CLASS,
       SUM(dist.ACCTD_AMOUNT) AS total_funcional
FROM   RA_CUST_TRX_LINE_GL_DIST_ALL dist
JOIN   GL_CODE_COMBINATIONS gcc
       ON gcc.CODE_COMBINATION_ID = dist.CODE_COMBINATION_ID
WHERE  dist.GL_DATE BETWEEN :start_date AND :end_date
  AND  dist.ACCOUNT_SET_FLAG = 'N'
  AND  dist.ORG_ID = :p_org_id
GROUP BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3, dist.ACCOUNT_CLASS;
```

### Distribuições não postadas no GL
```sql
SELECT ct.TRX_NUMBER, dist.GL_DATE, dist.ACCOUNT_CLASS,
       dist.AMOUNT, dist.POSTING_CONTROL_ID
FROM   RA_CUST_TRX_LINE_GL_DIST_ALL dist
JOIN   RA_CUSTOMER_TRX_ALL ct
       ON ct.CUSTOMER_TRX_ID = dist.CUSTOMER_TRX_ID
WHERE  dist.POSTING_CONTROL_ID = -1
  AND  dist.ACCOUNT_SET_FLAG = 'N'
  AND  dist.ORG_ID = :p_org_id;
```

### Filtros comuns
- `ACCOUNT_SET_FLAG = 'N'` — Apenas distribuições reais (excluir templates)
- `ACCOUNT_CLASS = 'REV'` — Apenas distribuições de receita
- `ACCOUNT_CLASS = 'REC'` — Apenas distribuições de recebível
- `POSTING_CONTROL_ID = -1` — Distribuições ainda não postadas no GL
- `LATEST_REC_FLAG = 'Y'` — Distribuição de recebível mais recente (evitar duplicidade)

---

## 🔒 Observações

- O campo `ACCOUNT_SET_FLAG` é crítico: registros com valor `'Y'` são **templates** usados pelo AutoAccounting e **não representam valores reais**. Sempre filtrar `ACCOUNT_SET_FLAG = 'N'` em consultas de valores.
- O `POSTING_CONTROL_ID` segue a convenção: `-1` = não postado, `-2` = não precisa postar (e.g., tipo de transação com `POST_TO_GL = 'N'`), valores positivos = ID do batch de posting.
- Para `ACCOUNT_CLASS = 'REC'`, usar `LATEST_REC_FLAG = 'Y'` para obter apenas a distribuição mais recente do recebível (evita dupla contagem após aplicações parciais).
- Distribuições com `ACCOUNT_CLASS` em `'UNBILL'` ou `'UNEARN'` estão relacionadas ao **revenue scheduling** e devem ser consideradas em análises de receita diferida.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15`.

---

## 🔗 PVOs Relacionados

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR · BICC: 4/74)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | RefCustTrxDistAccountClass | ✅ |
| ACCOUNT_CLASS | TransactionLineDistributionAccountClass | — |
| ACCOUNT_SET_FLAG | RefCustTrxDistAccountSetFlag | — |
| ACCOUNT_SET_FLAG | TransactionLineDistributionAccountSetFlag | — |
| ACCTD_AMOUNT | RefCustTrxDistAcctdAmount | — |
| ACCTD_AMOUNT | TransactionLineDistributionAcctdAmount | — |
| AMOUNT | RefCustTrxDistAmount | — |
| AMOUNT | TransactionLineDistributionAmount | — |
| CODE_COMBINATION_ID | RefCustTrxDistCodeCombinationId | — |
| CODE_COMBINATION_ID | TransactionLineDistributionCodeCombinationId | — |
| COLLECTED_TAX_CCID | RefCustTrxDistCollectedTaxCcid | — |
| COLLECTED_TAX_CCID | TransactionLineDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | RefCustTrxDistCollectedTaxConcatSeg | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionLineDistributionCollectedTaxConcatSeg | — |
| COMMENTS | RefCustTrxDistComments | — |
| COMMENTS | TransactionLineDistributionComments | — |
| CONCATENATED_SEGMENTS | RefCustTrxDistConcatenatedSegments | — |
| CONCATENATED_SEGMENTS | TransactionLineDistributionConcatenatedSegments | — |
| CREATED_BY | RefCustTrxDistCreatedBy | — |
| CREATION_DATE | RefCustTrxDistCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | RefCustTrxDistCustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_GL_DIST_ID | TransactionLineDistributionCustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | RefCustTrxDistCustTrxLineSalesrepId | — |
| CUST_TRX_LINE_SALESREP_ID | TransactionLineDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | RefCustTrxDistCustomerTrxId | — |
| CUSTOMER_TRX_ID | TransactionLineDistributionCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | RefCustTrxDistCustomerTrxLineId | — |
| CUSTOMER_TRX_LINE_ID | TransactionLineDistributionCustomerTrxLineId | — |
| EVENT_ID | RefCustTrxDistEventId | — |
| EVENT_ID | TransactionLineDistributionEventId | — |
| GL_DATE | RefCustTrxDistGlDate | — |
| GL_DATE | TransactionLineDistributionGlDate | — |
| GL_POSTED_DATE | RefCustTrxDistGlPostedDate | — |
| GL_POSTED_DATE | TransactionLineDistributionGlPostedDate | — |
| LAST_UPDATE_DATE | RefCustTrxDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RefCustTrxDistLastUpdateLogin | — |
| LAST_UPDATED_BY | RefCustTrxDistLastUpdatedBy | — |
| LATEST_REC_FLAG | RefCustTrxDistLatestRecFlag | — |
| LATEST_REC_FLAG | TransactionLineDistributionLatestRecFlag | — |
| OBJECT_VERSION_NUMBER | RefCustTrxDistObjectVersionNumber | — |
| ORG_ID | RefCustTrxDistOrgId | — |
| ORG_ID | TransactionLineDistributionOrgId | — |
| ORIGINAL_GL_DATE | RefCustTrxDistOriginalGlDate | — |
| ORIGINAL_GL_DATE | TransactionLineDistributionOriginalGlDate | — |
| PERCENT | RefCustTrxDistPercent | — |
| PERCENT | TransactionLineDistributionPercent | — |
| POST_REQUEST_ID | RefCustTrxDistPostRequestId | — |
| POST_REQUEST_ID | TransactionLineDistributionPostRequestId | — |
| POSTING_CONTROL_ID | RefCustTrxDistPostingControlId | — |
| POSTING_CONTROL_ID | TransactionLineDistributionPostingControlId | — |
| PROGRAM_APPLICATION_ID | RefCustTrxDistProgramApplicationId | — |
| PROGRAM_APPLICATION_ID | TransactionLineDistributionProgramApplicationId | — |
| PROGRAM_ID | RefCustTrxDistProgramId | — |
| PROGRAM_ID | TransactionLineDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | RefCustTrxDistProgramUpdateDate | — |
| PROGRAM_UPDATE_DATE | TransactionLineDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | RefCustTrxDistRaPostLoopNumber | — |
| RA_POST_LOOP_NUMBER | TransactionLineDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | RefCustTrxDistRecOffsetFlag | — |
| REC_OFFSET_FLAG | TransactionLineDistributionRecOffsetFlag | — |
| REQUEST_ID | RefCustTrxDistRequestId | — |
| REQUEST_ID | TransactionLineDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | RefCustTrxDistRevAdjClassTemp | — |
| REV_ADJ_CLASS_TEMP | TransactionLineDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | RefCustTrxDistRevenueAdjustmentId | — |
| REVENUE_ADJUSTMENT_ID | TransactionLineDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | RefCustTrxDistRoundingCorrectionFlag | — |
| ROUNDING_CORRECTION_FLAG | TransactionLineDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | RefCustTrxDistSetOfBooksId | — |
| SET_OF_BOOKS_ID | TransactionLineDistributionSetOfBooksId | — |
| TRANSFER_TO_COSTING | RefCustTrxDistTransferToCosting | — |
| TRANSFER_TO_COSTING | TransactionLineDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | RefCustTrxDistUserGeneratedFlag | — |
| USER_GENERATED_FLAG | TransactionLineDistributionUserGeneratedFlag | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR · BICC: 10/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TransactionLineDistributionAccountClass | ✅ |
| ACCOUNT_SET_FLAG | TransactionLineDistributionAccountSetFlag | ✅ |
| ACCTD_AMOUNT | TransactionLineDistributionAcctdAmount | ✅ |
| AMOUNT | TransactionLineDistributionAmount | ✅ |
| CODE_COMBINATION_ID | TransactionLineDistributionCodeCombinationId | ✅ |
| COLLECTED_TAX_CCID | TransactionLineDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionLineDistributionCollectedTaxConcatSeg | — |
| COMMENTS | TransactionLineDistributionComments | — |
| CONCATENATED_SEGMENTS | TransactionLineDistributionConcatenatedSegments | — |
| CREATED_BY | TransactionLineDistributionCreatedBy | — |
| CREATION_DATE | TransactionLineDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | CustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | TransactionLineDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | TransactionLineDistributionCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | TransactionLineDistributionCustomerTrxLineId | — |
| EVENT_ID | TransactionLineDistributionEventId | — |
| GL_DATE | TransactionLineDistributionGlDate | ✅ |
| GL_POSTED_DATE | TransactionLineDistributionGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionLineDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionLineDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionLineDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TransactionLineDistributionLatestRecFlag | — |
| OBJECT_VERSION_NUMBER | TransactionLineDistributionObjectVersionNumber | — |
| ORG_ID | TransactionLineDistributionOrgId | — |
| ORIGINAL_GL_DATE | TransactionLineDistributionOriginalGlDate | — |
| PERCENT | TransactionLineDistributionPercent | — |
| POST_REQUEST_ID | TransactionLineDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TransactionLineDistributionPostingControlId | — |
| PROGRAM_APPLICATION_ID | TransactionLineDistributionProgramApplicationId | — |
| PROGRAM_ID | TransactionLineDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionLineDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TransactionLineDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TransactionLineDistributionRecOffsetFlag | — |
| REQUEST_ID | TransactionLineDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TransactionLineDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TransactionLineDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TransactionLineDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TransactionLineDistributionSetOfBooksId | ✅ |
| TRANSFER_TO_COSTING | TransactionLineDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TransactionLineDistributionUserGeneratedFlag | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 11/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TransactionDistributionAccountClass | ✅ |
| ACCOUNT_SET_FLAG | TransactionDistributionAccountSetFlag | — |
| ACCTD_AMOUNT | TransactionDistributionAcctdAmount | ✅ |
| AMOUNT | TransactionDistributionAmount | ✅ |
| CODE_COMBINATION_ID | TransactionDistributionCodeCombinationId | ✅ |
| COLLECTED_TAX_CCID | TransactionDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionDistributionCollectedTaxConcatSeg | — |
| COMMENTS | TransactionDistributionComments | — |
| CONCATENATED_SEGMENTS | TransactionDistributionConcatenatedSegments | — |
| CREATED_BY | TransactionDistributionCreatedBy | — |
| CREATION_DATE | TransactionDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | TransactionDistributionCustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | TransactionDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | TransactionDistributionCustomerTrxId | ✅ |
| CUSTOMER_TRX_LINE_ID | TransactionDistributionCustomerTrxLineId | — |
| EVENT_ID | TransactionDistributionEventId | — |
| GL_DATE | TransactionDistributionGlDate | ✅ |
| GL_POSTED_DATE | TransactionDistributionGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TransactionDistributionLatestRecFlag | ✅ |
| OBJECT_VERSION_NUMBER | TransactionDistributionObjectVersionNumber | — |
| ORG_ID | TransactionDistributionOrgId | — |
| ORIGINAL_GL_DATE | TransactionDistributionOriginalGlDate | — |
| PERCENT | TransactionDistributionPercent | — |
| POST_REQUEST_ID | TransactionDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TransactionDistributionPostingControlId | — |
| PROGRAM_APPLICATION_ID | TransactionDistributionProgramApplicationId | — |
| PROGRAM_ID | TransactionDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TransactionDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TransactionDistributionRecOffsetFlag | — |
| REQUEST_ID | TransactionDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TransactionDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TransactionDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TransactionDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TransactionDistributionSetOfBooksId | ✅ |
| TRANSFER_TO_COSTING | TransactionDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TransactionDistributionUserGeneratedFlag | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TransactionDistributionAccountClass | — |
| ACCOUNT_SET_FLAG | TransactionDistributionAccountSetFlag | — |
| ACCTD_AMOUNT | TransactionDistributionAcctdAmount | — |
| AMOUNT | TransactionDistributionAmount | — |
| CODE_COMBINATION_ID | TransactionDistributionCodeCombinationId | — |
| COLLECTED_TAX_CCID | TransactionDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionDistributionCollectedTaxConcatSeg | — |
| COMMENTS | TransactionDistributionComments | — |
| CONCATENATED_SEGMENTS | TransactionDistributionConcatenatedSegments | — |
| CREATED_BY | TransactionDistributionCreatedBy | — |
| CREATION_DATE | TransactionDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | TransactionDistributionCustTrxLineGlDistId | — |
| CUST_TRX_LINE_SALESREP_ID | TransactionDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | TransactionDistributionCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | TransactionDistributionCustomerTrxLineId | — |
| EVENT_ID | TransactionDistributionEventId | — |
| GL_DATE | TransactionDistributionGlDate | — |
| GL_POSTED_DATE | TransactionDistributionGlPostedDate | — |
| LAST_UPDATE_DATE | TransactionDistributionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TransactionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TransactionDistributionLatestRecFlag | — |
| OBJECT_VERSION_NUMBER | TransactionDistributionObjectVersionNumber | — |
| ORG_ID | TransactionDistributionOrgId | — |
| ORIGINAL_GL_DATE | TransactionDistributionOriginalGlDate | — |
| PERCENT | TransactionDistributionPercent | — |
| POST_REQUEST_ID | TransactionDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TransactionDistributionPostingControlId | — |
| PROGRAM_APPLICATION_ID | TransactionDistributionProgramApplicationId | — |
| PROGRAM_ID | TransactionDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TransactionDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TransactionDistributionRecOffsetFlag | — |
| REQUEST_ID | TransactionDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TransactionDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TransactionDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TransactionDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TransactionDistributionSetOfBooksId | — |
| TRANSFER_TO_COSTING | TransactionDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TransactionDistributionUserGeneratedFlag | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TransactionDistributionAccountClass | — |
| ACCOUNT_SET_FLAG | TransactionDistributionAccountSetFlag | — |
| ACCTD_AMOUNT | TransactionDistributionAcctdAmount | — |
| AMOUNT | TransactionDistributionAmount | — |
| CODE_COMBINATION_ID | TransactionDistributionCodeCombinationId | — |
| COLLECTED_TAX_CCID | TransactionDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionDistributionCollectedTaxConcatSeg | — |
| COMMENTS | TransactionDistributionComments | — |
| CONCATENATED_SEGMENTS | TransactionDistributionConcatenatedSegments | — |
| CREATED_BY | TransactionDistributionCreatedBy | — |
| CREATION_DATE | TransactionDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | TransactionDistributionCustTrxLineGlDistId | — |
| CUST_TRX_LINE_SALESREP_ID | TransactionDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | TransactionDistributionCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | TransactionDistributionCustomerTrxLineId | — |
| EVENT_ID | TransactionDistributionEventId | — |
| GL_DATE | TransactionDistributionGlDate | — |
| GL_POSTED_DATE | TransactionDistributionGlPostedDate | — |
| LAST_UPDATE_DATE | TransactionDistributionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TransactionDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TransactionDistributionLatestRecFlag | — |
| OBJECT_VERSION_NUMBER | TransactionDistributionObjectVersionNumber | — |
| ORG_ID | TransactionDistributionOrgId | — |
| ORIGINAL_GL_DATE | TransactionDistributionOriginalGlDate | — |
| PERCENT | TransactionDistributionPercent | — |
| POST_REQUEST_ID | TransactionDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TransactionDistributionPostingControlId | — |
| PROGRAM_APPLICATION_ID | TransactionDistributionProgramApplicationId | — |
| PROGRAM_ID | TransactionDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TransactionDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TransactionDistributionRecOffsetFlag | — |
| REQUEST_ID | TransactionDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TransactionDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TransactionDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TransactionDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TransactionDistributionSetOfBooksId | — |
| TRANSFER_TO_COSTING | TransactionDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TransactionDistributionUserGeneratedFlag | — |

### [[revenueadjustmentdistributionpvo|RevenueAdjustmentDistributionPVO]] (AR · BICC: 14/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TrxDistributionAccountClass | — |
| ACCOUNT_SET_FLAG | TrxDistributionAccountSetFlag | — |
| ACCTD_AMOUNT | TrxDistributionAcctdAmount | ✅ |
| AMOUNT | TrxDistributionAmount | ✅ |
| CODE_COMBINATION_ID | TrxDistributionCodeCombinationId | — |
| COLLECTED_TAX_CCID | TrxDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TrxDistributionCollectedTaxConcatSeg | ✅ |
| COMMENTS | TrxDistributionComments | ✅ |
| CONCATENATED_SEGMENTS | TrxDistributionConcatenatedSegments | ✅ |
| CREATED_BY | TrxDistributionCreatedBy | — |
| CREATION_DATE | TrxDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | CustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | TrxDistributionCustTrxLineSalesrepId | — |
| CUSTOMER_TRX_ID | TrxDistributionCustomerTrxId | — |
| CUSTOMER_TRX_LINE_ID | TrxDistributionCustomerTrxLineId | — |
| EVENT_ID | TrxDistributionEventId | ✅ |
| GL_DATE | TrxDistributionGlDate | ✅ |
| GL_POSTED_DATE | TrxDistributionGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TrxDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TrxDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TrxDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TrxDistributionLatestRecFlag | ✅ |
| OBJECT_VERSION_NUMBER | TrxDistributionObjectVersionNumber | — |
| ORG_ID | TrxDistributionOrgId | — |
| ORIGINAL_GL_DATE | TrxDistributionOriginalGlDate | ✅ |
| PERCENT | TrxDistributionPercent | ✅ |
| POST_REQUEST_ID | TrxDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TrxDistributionPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | TrxDistributionProgramApplicationId | — |
| PROGRAM_ID | TrxDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TrxDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TrxDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TrxDistributionRecOffsetFlag | — |
| REQUEST_ID | TrxDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TrxDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TrxDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TrxDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TrxDistributionSetOfBooksId | — |
| TRANSFER_TO_COSTING | TrxDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TrxDistributionUserGeneratedFlag | — |

### [[transactiondistributionextractpvo|TransactionDistributionExtractPVO]] (OTHER · BICC: 39/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | RaCustTrxLineGlDistAccountClass | ✅ |
| ACCOUNT_SET_FLAG | RaCustTrxLineGlDistAccountSetFlag | ✅ |
| ACCTD_AMOUNT | RaCustTrxLineGlDistAcctdAmount | ✅ |
| AMOUNT | RaCustTrxLineGlDistAmount | ✅ |
| ATTRIBUTE1 | RaCustTrxLineGlDistAttribute1 | — |
| ATTRIBUTE10 | RaCustTrxLineGlDistAttribute10 | — |
| ATTRIBUTE11 | RaCustTrxLineGlDistAttribute11 | — |
| ATTRIBUTE12 | RaCustTrxLineGlDistAttribute12 | — |
| ATTRIBUTE13 | RaCustTrxLineGlDistAttribute13 | — |
| ATTRIBUTE14 | RaCustTrxLineGlDistAttribute14 | — |
| ATTRIBUTE15 | RaCustTrxLineGlDistAttribute15 | — |
| ATTRIBUTE2 | RaCustTrxLineGlDistAttribute2 | — |
| ATTRIBUTE3 | RaCustTrxLineGlDistAttribute3 | — |
| ATTRIBUTE4 | RaCustTrxLineGlDistAttribute4 | — |
| ATTRIBUTE5 | RaCustTrxLineGlDistAttribute5 | — |
| ATTRIBUTE6 | RaCustTrxLineGlDistAttribute6 | — |
| ATTRIBUTE7 | RaCustTrxLineGlDistAttribute7 | — |
| ATTRIBUTE8 | RaCustTrxLineGlDistAttribute8 | — |
| ATTRIBUTE9 | RaCustTrxLineGlDistAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaCustTrxLineGlDistAttributeCategory | — |
| CODE_COMBINATION_ID | RaCustTrxLineGlDistCodeCombinationId | ✅ |
| COLLECTED_TAX_CCID | RaCustTrxLineGlDistCollectedTaxCcid | ✅ |
| COLLECTED_TAX_CONCAT_SEG | RaCustTrxLineGlDistCollectedTaxConcatSeg | ✅ |
| COMMENTS | RaCustTrxLineGlDistComments | ✅ |
| CONCATENATED_SEGMENTS | RaCustTrxLineGlDistConcatenatedSegments | ✅ |
| CREATED_BY | RaCustTrxLineGlDistCreatedBy | ✅ |
| CREATION_DATE | RaCustTrxLineGlDistCreationDate | ✅ |
| CUST_TRX_LINE_GL_DIST_ID | RaCustTrxLineGlDistCustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | RaCustTrxLineGlDistCustTrxLineSalesrepId | ✅ |
| CUSTOMER_TRX_ID | RaCustTrxLineGlDistCustomerTrxId | ✅ |
| CUSTOMER_TRX_LINE_ID | RaCustTrxLineGlDistCustomerTrxLineId | ✅ |
| EVENT_ID | RaCustTrxLineGlDistEventId | ✅ |
| GL_DATE | RaCustTrxLineGlDistGlDate | ✅ |
| GL_POSTED_DATE | RaCustTrxLineGlDistGlPostedDate | ✅ |
| LAST_UPDATE_DATE | RaCustTrxLineGlDistLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaCustTrxLineGlDistLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaCustTrxLineGlDistLastUpdatedBy | ✅ |
| LATEST_REC_FLAG | RaCustTrxLineGlDistLatestRecFlag | ✅ |
| OBJECT_VERSION_NUMBER | RaCustTrxLineGlDistObjectVersionNumber | ✅ |
| ORG_ID | RaCustTrxLineGlDistOrgId | ✅ |
| ORIGINAL_GL_DATE | RaCustTrxLineGlDistOriginalGlDate | ✅ |
| PERCENT | RaCustTrxLineGlDistPercent | ✅ |
| POST_REQUEST_ID | RaCustTrxLineGlDistPostRequestId | ✅ |
| POSTING_CONTROL_ID | RaCustTrxLineGlDistPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | RaCustTrxLineGlDistProgramApplicationId | ✅ |
| PROGRAM_ID | RaCustTrxLineGlDistProgramId | ✅ |
| PROGRAM_UPDATE_DATE | RaCustTrxLineGlDistProgramUpdateDate | ✅ |
| REC_OFFSET_FLAG | RaCustTrxLineGlDistRecOffsetFlag | ✅ |
| REQUEST_ID | RaCustTrxLineGlDistRequestId | ✅ |
| REV_ADJ_CLASS_TEMP | RaCustTrxLineGlDistRevAdjClassTemp | ✅ |
| REVENUE_ADJUSTMENT_ID | RaCustTrxLineGlDistRevenueAdjustmentId | ✅ |
| ROUNDING_CORRECTION_FLAG | RaCustTrxLineGlDistRoundingCorrectionFlag | ✅ |
| SET_OF_BOOKS_ID | RaCustTrxLineGlDistSetOfBooksId | ✅ |
| TRANSFER_TO_COSTING | RaCustTrxLineGlDistTransferToCosting | ✅ |
| USER_GENERATED_FLAG | RaCustTrxLineGlDistUserGeneratedFlag | ✅ |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 19/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_CLASS | TransactionLineDistributionAccountClass | ✅ |
| ACCOUNT_SET_FLAG | TransactionLineDistributionAccountSetFlag | ✅ |
| ACCTD_AMOUNT | TransactionLineDistributionAcctdAmount | ✅ |
| AMOUNT | TransactionLineDistributionAmount | ✅ |
| CODE_COMBINATION_ID | TransactionLineDistributionCodeCombinationId | — |
| COLLECTED_TAX_CCID | TransactionLineDistributionCollectedTaxCcid | — |
| COLLECTED_TAX_CONCAT_SEG | TransactionLineDistributionCollectedTaxConcatSeg | ✅ |
| COMMENTS | TransactionLineDistributionComments | ✅ |
| CONCATENATED_SEGMENTS | TransactionLineDistributionConcatenatedSegments | ✅ |
| CREATED_BY | TransactionLineDistributionCreatedBy | — |
| CREATION_DATE | TransactionLineDistributionCreationDate | — |
| CUST_TRX_LINE_GL_DIST_ID | CustTrxLineGlDistId | ✅ |
| CUST_TRX_LINE_SALESREP_ID | TransactionLineDistributionCustTrxLineSalesrepId | ✅ |
| CUSTOMER_TRX_ID | TransactionLineDistributionCustomerTrxId | ✅ |
| CUSTOMER_TRX_LINE_ID | TransactionLineDistributionCustomerTrxLineId | ✅ |
| EVENT_ID | TransactionLineDistributionEventId | ✅ |
| GL_DATE | TransactionLineDistributionGlDate | ✅ |
| GL_POSTED_DATE | TransactionLineDistributionGlPostedDate | ✅ |
| LAST_UPDATE_DATE | TransactionLineDistributionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionLineDistributionLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionLineDistributionLastUpdatedBy | — |
| LATEST_REC_FLAG | TransactionLineDistributionLatestRecFlag | ✅ |
| OBJECT_VERSION_NUMBER | TransactionLineDistributionObjectVersionNumber | — |
| ORG_ID | TransactionLineDistributionOrgId | — |
| ORIGINAL_GL_DATE | TransactionLineDistributionOriginalGlDate | ✅ |
| PERCENT | TransactionLineDistributionPercent | ✅ |
| POST_REQUEST_ID | TransactionLineDistributionPostRequestId | — |
| POSTING_CONTROL_ID | TransactionLineDistributionPostingControlId | ✅ |
| PROGRAM_APPLICATION_ID | TransactionLineDistributionProgramApplicationId | — |
| PROGRAM_ID | TransactionLineDistributionProgramId | — |
| PROGRAM_UPDATE_DATE | TransactionLineDistributionProgramUpdateDate | — |
| RA_POST_LOOP_NUMBER | TransactionLineDistributionRaPostLoopNumber | — |
| REC_OFFSET_FLAG | TransactionLineDistributionRecOffsetFlag | — |
| REQUEST_ID | TransactionLineDistributionRequestId | — |
| REV_ADJ_CLASS_TEMP | TransactionLineDistributionRevAdjClassTemp | — |
| REVENUE_ADJUSTMENT_ID | TransactionLineDistributionRevenueAdjustmentId | — |
| ROUNDING_CORRECTION_FLAG | TransactionLineDistributionRoundingCorrectionFlag | — |
| SET_OF_BOOKS_ID | TransactionLineDistributionSetOfBooksId | — |
| TRANSFER_TO_COSTING | TransactionLineDistributionTransferToCosting | — |
| USER_GENERATED_FLAG | TransactionLineDistributionUserGeneratedFlag | — |

---

## 📚 Referências

- [Oracle Docs — RA_CUST_TRX_LINE_GL_DIST_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racusttrxlinegldistall-25198.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
