---
id: DOC-AP-024
doc_type: system-doc
title: "AP_RECON_SUMMARY_PARAMETERS — Parâmetros de Execução da Reconciliação AP"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, reconciliacao, parametros, ap-gl]
aliases: [AP_RECON_SUMMARY_PARAMETERS, ap_recon_summary_parameters, recon_params_ap, parametros_reconciliacao_ap, recon_header_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_RECON_SUMMARY_PARAMETERS

## Visão Geral

Tabela que armazena os parâmetros utilizados em cada execução do processo de reconciliação entre o subledger de Accounts Payable e o General Ledger. Funciona como cabeçalho (header) das reconciliações, registrando critérios de filtro como ledger, período, conta e business unit.

## Propósito de Negócio

Permite rastrear e auditar os parâmetros de cada execução de reconciliação AP vs GL. É essencial para: (1) reproduzir execuções anteriores com os mesmos critérios, (2) auditoria de quem executou e quando, (3) histórico de reconciliações por período, (4) governança do processo de fechamento contábil.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECON_HEADER_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único da execução de reconciliação. | — | 🟢 100% |
| 2 | LEDGER_ID | NUMBER(15) | NOT NULL | FK | FK para GL_LEDGERS. Ledger utilizado na reconciliação. | — | 🟢 95% |
| 3 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Temporal | Nome do período contábil de referência (ex.: MAR-26). | — | 🟢 100% |
| 4 | FROM_ACCOUNT | VARCHAR2(240) | NULL | Filtro | Conta contábil inicial do intervalo de reconciliação. | — | 🟡 75% |
| 5 | TO_ACCOUNT | VARCHAR2(240) | NULL | Filtro | Conta contábil final do intervalo de reconciliação. | — | 🟡 75% |
| 6 | EXECUTION_DATE | DATE | NULL | Temporal | Data/hora da execução da reconciliação. | — | 🟡 80% |
| 7 | REQUEST_ID | NUMBER(15) | NULL | Técnico | ID da requisição concorrente (Concurrent Request). | — | 🟢 90% |
| 8 | STATUS | VARCHAR2(30) | NULL | Status | Status da execução (COMPLETED, ERROR, IN_PROGRESS). | — | 🟡 75% |
| 9 | ORG_ID | NUMBER(15) | NOT NULL | Partição | Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que executou a reconciliação. | — | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- Nenhuma tabela-pai direta identificada (tabela raiz do processo de reconciliação).

### Tabelas-filha

- **[[ap_recon_summary_details]]** — Resultados da reconciliação por conta (1:N via `RECON_HEADER_ID`).

## Uso Típico

```sql
-- Histórico de execuções de reconciliação AP vs GL
SELECT rsp.RECON_HEADER_ID,
       rsp.PERIOD_NAME,
       rsp.EXECUTION_DATE,
       rsp.CREATED_BY,
       rsp.STATUS,
       COUNT(rsd.RECON_ID) AS total_contas
  FROM AP_RECON_SUMMARY_PARAMETERS rsp
  LEFT JOIN AP_RECON_SUMMARY_DETAILS rsd
    ON rsd.RECON_HEADER_ID = rsp.RECON_HEADER_ID
 WHERE rsp.ORG_ID = :p_org_id
 GROUP BY rsp.RECON_HEADER_ID, rsp.PERIOD_NAME,
          rsp.EXECUTION_DATE, rsp.CREATED_BY, rsp.STATUS
 ORDER BY rsp.EXECUTION_DATE DESC;
```

## Observações

- Cada execução de reconciliação gera um registro nesta tabela e múltiplos registros em [[ap_recon_summary_details]].
- Estrutura análoga a [[ar_recon_summary_parameters]] do módulo AR.
- O campo `REQUEST_ID` permite rastrear o job concorrente no Oracle Fusion.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[payablesreconciliationparameterpvo|PayablesReconciliationParameterPVO]] (AP · BICC: 14/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCING_SEGMENT_FROM | ReconParamBalancingSegmentFrom | ✅ |
| BALANCING_SEGMENT_TO | ReconParamBalancingSegmentTo | ✅ |
| BU_ID | ReconParamBuId | — |
| COST_CENTRE_SEGMENT_FROM | ReconParamCostCentreSegmentFrom | — |
| COST_CENTRE_SEGMENT_TO | ReconParamCostCentreSegmentTo | — |
| CREATED_BY | ReconParamCreatedBy | — |
| CREATION_DATE | ReconParamCreationDate | — |
| END_DATE | ReconParamEndDate | ✅ |
| INCLUDE_BILLS_PAYABLE | ReconParamIncludeBillsPayable | ✅ |
| INCLUDE_INTERCOMPANY_TRX | ReconParamIncludeIntercompanyTrx | ✅ |
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
| PERIOD_NAME | ReconParamPeriodName | ✅ |
| RECON_SUMMARY_PARAM_ID | ReconSummaryParamId | ✅ |
| REQUEST_ID | ReconParamRequestId | ✅ |
| REQUEST_NAME | ReconParamRequestName | ✅ |
| START_DATE | ReconParamStartDate | ✅ |
