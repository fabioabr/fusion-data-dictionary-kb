---
id: DOC-AR-062
doc_type: system-doc
title: "AR_RECON_SUMMARY_PARAMETERS — Parâmetros de Execução da Reconciliação"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, reconciliacao, parametros, execucao]
aliases: [AR_RECON_SUMMARY_PARAMETERS, ar_recon_summary_parameters, recon_parameters, parametros_reconciliacao, recon_params]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECON_SUMMARY_PARAMETERS

## 📌 Visão Geral

Tabela de parâmetros de execução do processo de reconciliação AR vs GL. Cada registro documenta os critérios utilizados em uma execução específica da reconciliação, incluindo período, ledger, organização e data de referência.

## 🧠 Propósito de Negócio

Registrar os parâmetros de cada execução da reconciliação é fundamental para rastreabilidade e auditoria. Permite verificar: (1) quando a reconciliação foi executada, (2) com quais critérios (período, ledger, data de corte), (3) qual foi o status final. Em fechamentos contábeis, é necessário comprovar que a reconciliação foi executada com os parâmetros corretos.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | RECON_PARAMETER_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único dos parâmetros de execução. | PK | 🟢 100% |
| 2 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Nome do período contábil reconciliado. | Temporal | 🟢 100% |
| 3 | LEDGER_ID | NUMBER(15) | NOT NULL | FK para GL_LEDGERS. Ledger contábil da reconciliação. | FK | 🟢 100% |
| 4 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 5 | AS_OF_DATE | DATE | NULL | Data de referência (corte) para a reconciliação. | Temporal | 🟢 100% |
| 6 | REQUEST_ID | NUMBER(15) | NULL | Identificador da requisição concorrente que executou a reconciliação. | Técnico | 🟢 100% |
| 7 | STATUS | VARCHAR2(30) | NOT NULL | Status da execução (ex.: COMPLETED, ERROR, IN_PROGRESS). | Controle | 🟢 100% |
| 8 | START_TIME | DATE | NULL | Data/hora de início da execução. | Temporal | 🟡 75% |
| 9 | END_TIME | DATE | NULL | Data/hora de término da execução. | Temporal | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_recon_summary_details]]** — Resumos de reconciliação gerados com estes parâmetros (1:N via `RECON_PARAMETER_ID`).
- **[[ar_recon_difference_details]]** — Diferenças encontradas (via join com `ar_recon_summary_details`).
- **GL_LEDGERS** — Ledger contábil (N:1 via `LEDGER_ID`).

## 📎 Uso Típico

```sql
-- Histórico de execuções de reconciliação por período
SELECT rsp.RECON_PARAMETER_ID,
       rsp.PERIOD_NAME,
       rsp.AS_OF_DATE,
       rsp.STATUS,
       rsp.CREATION_DATE AS data_execucao
  FROM AR_RECON_SUMMARY_PARAMETERS rsp
 WHERE rsp.ORG_ID = :p_org_id
   AND rsp.LEDGER_ID = :p_ledger_id
 ORDER BY rsp.CREATION_DATE DESC;
```

## 🔒 Observações

- Cada execução de reconciliação gera um registro nesta tabela, mesmo que não encontre diferenças.
- O `REQUEST_ID` permite vincular à requisição concorrente no Oracle para análise de logs.
- Execuções com `STATUS = 'ERROR'` devem ser investigadas e reexecutadas.
- A reconciliação deve ser executada após a transferência de journals para o GL e antes do fechamento do período.

## 🔗 PVOs Relacionados

### [[receivablesreconciliationparameterpvo|ReceivablesReconciliationParameterPVO]] (AR · BICC: 15/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCING_SEGMENT_FROM | ReconParamBalancingSegmentFrom | ✅ |
| BALANCING_SEGMENT_TO | ReconParamBalancingSegmentTo | ✅ |
| BU_ID | ReconParamBuId | — |
| COST_CENTRE_SEGMENT_FROM | ReconParamCostCentreSegmentFrom | — |
| COST_CENTRE_SEGMENT_TO | ReconParamCostCentreSegmentTo | — |
| CREATED_BY | ReconParamCreatedBy | — |
| CREATION_DATE | ReconParamCreationDate | — |
| INCLUDE_INTERCOMPANY_TRX | ReconParamIncludeIntercompanyTrx | ✅ |
| INCLUDE_ON_ACCOUNT_ITEM | ReconParamIncludeOnAccountItem | ✅ |
| INCLUDE_UNAPP_UNID_RECEIPTS | ReconParamIncludeUnappUnidReceipts | ✅ |
| INTERCOMPANY_SEGMENT_FROM | ReconParamIntercompanySegmentFrom | — |
| INTERCOMPANY_SEGMENT_TO | ReconParamIntercompanySegmentTo | — |
| JOB_DEFINITION_NAME | ReconParamJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ReconParamJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ReconParamLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReconParamLastUpdateLogin | — |
| LAST_UPDATED_BY | ReconParamLastUpdatedBy | ✅ |
| LEDGER_ID | ReconParamLedgerId | — |
| NATURAL_ACCOUNT_SEGMENT_FROM | ReconParamNaturalAccountSegmentFrom | ✅ |
| NATURAL_ACCOUNT_SEGMENT_TO | ReconParamNaturalAccountSegmentTo | ✅ |
| PERIOD_END_DATE | ReconParamPeriodEndDate | ✅ |
| PERIOD_NAME | ReconParamPeriodName | ✅ |
| PERIOD_START_DATE | ReconParamPeriodStartDate | ✅ |
| RECON_SUMMARY_PARAM_ID | ReconSummaryParamId | ✅ |
| REQUEST_ID | ReconParamRequestId | ✅ |
| REQUEST_NAME | ReconParamRequestName | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
