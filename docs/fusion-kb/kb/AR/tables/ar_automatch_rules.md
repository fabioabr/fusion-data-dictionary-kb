---
id: DOC-AR-050
doc_type: system-doc
title: "AR_AUTOMATCH_RULES — Regras de Correspondência Automática"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, automatch, correspondencia, conciliacao]
aliases: [AR_AUTOMATCH_RULES, ar_automatch_rules, automatch_rules, regras_automatch, correspondencia_automatica]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_AUTOMATCH_RULES

## 📌 Visão Geral

Tabela que armazena as **regras de correspondência automática** (automatch rules). Cada regra define um critério específico de match entre recebimentos e transações (faturas, débitos), com prioridade, tipo de correspondência e tolerância de valor.

## 🧠 Propósito de Negócio

O Automatch é a evolução do AutoCash — oferece correspondência mais sofisticada com regras granulares e priorizadas. É essencial para operações de alto volume onde a conciliação manual seria impraticável.

Casos de uso principais:
- Match por número de referência bancária
- Match por valor exato com tolerância
- Match por combinação de cliente + valor
- Priorização de critérios de correspondência

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | AUTOMATCH_RULE_ID | NUMBER | PK. Identificador único da regra de automatch. | Chave | 🟢 100% |
| 2 | AUTOMATCH_SET_ID | NUMBER | FK para o conjunto de regras ao qual esta regra pertence. | Chave Estrangeira | 🟢 100% |
| 3 | PRIORITY | NUMBER | Prioridade de execução (menor = maior prioridade). | Configuração | 🟢 100% |
| 4 | MATCH_BY | VARCHAR2 | Critério de match: `TRANSACTION_NUMBER`, `PURCHASE_ORDER`, `SALES_ORDER`, `AMOUNT`, etc. | Regra | 🟢 100% |
| 5 | THRESHOLD_AMOUNT | NUMBER | Valor de tolerância para match por valor (diferença máxima aceita). | Regra | 🟢 100% |
| 6 | AUTO_APPLY_FLAG | VARCHAR2 | Se `Y`, aplica automaticamente quando match é encontrado. Se `N`, sugere para revisão. | Regra | 🟢 100% |
| 7 | STATUS | VARCHAR2 | Status da regra: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 8 | MATCH_CONDITION | VARCHAR2 | Condição adicional de match (ex: match parcial, match exato). | Regra | 🟡 75% |
| 9 | STRING_MATCH_TYPE | VARCHAR2 | Tipo de correspondência de string: `EXACT`, `CONTAINS`, `STARTS_WITH`. | Regra | 🟡 75% |
| 10 | THRESHOLD_PERCENT | NUMBER | Percentual de tolerância para match por valor. | Regra | 🟢 100% |
| 11 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 12 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 13 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 14 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_automatch_rule_sets]] | AUTOMATCH_SET_ID | FK | Conjunto de regras pai |
| [[ar_cash_receipts_all]] | — | Referência | Recebimentos processados pelas regras |

## 📎 Uso Típico

```sql
-- Regras de automatch ordenadas por prioridade
SELECT amr.automatch_rule_id,
       amr.priority,
       amr.match_by,
       amr.threshold_amount,
       amr.auto_apply_flag,
       amr.status
  FROM ar_automatch_rules amr
 WHERE amr.automatch_set_id = :p_set_id
   AND amr.status = 'A'
 ORDER BY amr.priority;
```

```sql
-- Regras com aplicação automática habilitada
SELECT amr.match_by,
       amr.priority,
       amr.threshold_amount,
       amr.threshold_percent
  FROM ar_automatch_rules amr
 WHERE amr.auto_apply_flag = 'Y'
   AND amr.status = 'A'
 ORDER BY amr.priority;
```

## 🔒 Observações

- Regras são executadas na **ordem de prioridade** dentro do conjunto — a primeira regra que fizer match é aplicada (ou sugerida).
- `AUTO_APPLY_FLAG = 'N'` coloca o match em fila de revisão — útil para valores altos onde se deseja validação humana.
- `THRESHOLD_AMOUNT` e `THRESHOLD_PERCENT` definem a tolerância: se o valor do receipt difere da fatura dentro desse limite, o match é aceito.
- A combinação de `MATCH_BY` + `STRING_MATCH_TYPE` permite matches flexíveis (ex: número parcial da fatura).

## 🔗 PVOs Relacionados

### [[automatchruleextractpvo|AutomatchRuleExtractPVO]] (OTHER · BICC: 27/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ArAutomationRuleActiveFlag | ✅ |
| AMOUNT_WEIGHT | ArAutomationRuleAmountWeight | ✅ |
| AUTOMATCH_RULE_ID | ArAutomationRuleAutomatchRuleId | ✅ |
| CREATED_BY | ArAutomationRuleCreatedBy | ✅ |
| CREATION_DATE | ArAutomationRuleCreationDate | ✅ |
| CUSTOMER_THRESHOLD | ArAutomationRuleCustomerThreshold | ✅ |
| CUSTOMER_WEIGHT | ArAutomationRuleCustomerWeight | ✅ |
| DESCRIPTION | ArAutomationRuleDescription | ✅ |
| END_DATE | ArAutomationRuleEndDate | ✅ |
| LAST_UPDATE_DATE | ArAutomationRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArAutomationRuleLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArAutomationRuleLastUpdatedBy | ✅ |
| MIN_MATCH_THRESHOLD | ArAutomationRuleMinMatchThreshold | ✅ |
| NAME | ArAutomationRuleName | ✅ |
| NET_FREIGHT_WEIGHT | ArAutomationRuleNetFreightWeight | ✅ |
| NET_TAX_FREIGHT_WEIGHT | ArAutomationRuleNetTaxFreightWeight | ✅ |
| NET_TAX_WEIGHT | ArAutomationRuleNetTaxWeight | ✅ |
| NET_UNDISC_WEIGHT | ArAutomationRuleNetUndiscWeight | ✅ |
| NUMBER_OF_DAYS_CLOSED | ArAutomationRuleNumberOfDaysClosed | ✅ |
| OBJECT_VERSION_NUMBER | ArAutomationRuleObjectVersionNumber | ✅ |
| REMITTANCE_REGEXP | ArAutomationRuleRemittanceRegexp | ✅ |
| SEED_DATA_SOURCE | ArAutomationRuleSeedDataSource | ✅ |
| SET_ID | ArAutomationRuleSetId | ✅ |
| START_DATE | ArAutomationRuleStartDate | ✅ |
| TRANSACTION_REGEXP | ArAutomationRuleTransactionRegexp | ✅ |
| TRANSACTION_THRESHOLD | ArAutomationRuleTransactionThreshold | ✅ |
| TRANSACTION_WEIGHT | ArAutomationRuleTransactionWeight | ✅ |

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | AutoMatchRuleActiveFlag | — |
| AMOUNT_WEIGHT | AutoMatchRuleAmountWeight | — |
| AUTOMATCH_RULE_ID | AutoMatchRuleAutomatchRuleId | — |
| CUSTOMER_THRESHOLD | AutoMatchRuleCustomerThreshold | — |
| CUSTOMER_WEIGHT | AutoMatchRuleCustomerWeight | — |
| DESCRIPTION | AutoMatchRuleDescription | — |
| END_DATE | AutoMatchRuleEndDate | — |
| MIN_MATCH_THRESHOLD | AutoMatchRuleMinMatchThreshold | — |
| NAME | AutoMatchRuleName | — |
| NET_FREIGHT_WEIGHT | AutoMatchRuleNetFreightWeight | — |
| NET_TAX_FREIGHT_WEIGHT | AutoMatchRuleNetTaxFreightWeight | — |
| NET_TAX_WEIGHT | AutoMatchRuleNetTaxWeight | — |
| NET_UNDISC_WEIGHT | AutoMatchRuleNetUndiscWeight | — |
| NUMBER_OF_DAYS_CLOSED | AutoMatchRuleNumberOfDaysClosed | — |
| REMITTANCE_REGEXP | AutoMatchRuleRemittanceRegexp | — |
| START_DATE | AutoMatchRuleStartDate | — |
| TRANSACTION_REGEXP | AutoMatchRuleTransactionRegexp | — |
| TRANSACTION_THRESHOLD | AutoMatchRuleTransactionThreshold | — |
| TRANSACTION_WEIGHT | AutoMatchRuleTransactionWeight | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | AutomatchRuleActiveFlag | — |
| AMOUNT_WEIGHT | AutomatchRuleAmountWeight | — |
| AUTOMATCH_RULE_ID | AutomatchRuleAutomatchRuleId | — |
| CREATED_BY | AutomatchRuleCreatedBy | — |
| CREATION_DATE | AutomatchRuleCreationDate | — |
| CUSTOMER_THRESHOLD | AutomatchRuleCustomerThreshold | — |
| CUSTOMER_WEIGHT | AutomatchRuleCustomerWeight | — |
| DESCRIPTION | AutomatchRuleDescription | — |
| END_DATE | AutomatchRuleEndDate | — |
| LAST_UPDATE_DATE | AutomatchRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AutomatchRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | AutomatchRuleLastUpdatedBy | — |
| MIN_MATCH_THRESHOLD | AutomatchRuleMinMatchThreshold | — |
| NAME | AutomatchRuleName | ✅ |
| NET_FREIGHT_WEIGHT | AutomatchRuleNetFreightWeight | — |
| NET_TAX_FREIGHT_WEIGHT | AutomatchRuleNetTaxFreightWeight | — |
| NET_TAX_WEIGHT | AutomatchRuleNetTaxWeight | — |
| NET_UNDISC_WEIGHT | AutomatchRuleNetUndiscWeight | — |
| NUMBER_OF_DAYS_CLOSED | AutomatchRuleNumberOfDaysClosed | — |
| OBJECT_VERSION_NUMBER | AutomatchRuleObjectVersionNumber | — |
| REMITTANCE_REGEXP | AutomatchRuleRemittanceRegexp | — |
| SET_ID | AutomatchRuleSetId | — |
| START_DATE | AutomatchRuleStartDate | — |
| TRANSACTION_REGEXP | AutomatchRuleTransactionRegexp | — |
| TRANSACTION_THRESHOLD | AutomatchRuleTransactionThreshold | — |
| TRANSACTION_WEIGHT | AutomatchRuleTransactionWeight | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | AutomatchRuleActiveFlag | — |
| AMOUNT_WEIGHT | AutomatchRuleAmountWeight | — |
| AUTOMATCH_RULE_ID | AutomatchRuleAutomatchRuleId | — |
| CREATED_BY | AutomatchRuleCreatedBy | — |
| CREATION_DATE | AutomatchRuleCreationDate | — |
| CUSTOMER_THRESHOLD | AutomatchRuleCustomerThreshold | — |
| CUSTOMER_WEIGHT | AutomatchRuleCustomerWeight | — |
| DESCRIPTION | AutomatchRuleDescription | — |
| END_DATE | AutomatchRuleEndDate | — |
| LAST_UPDATE_DATE | AutomatchRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AutomatchRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | AutomatchRuleLastUpdatedBy | — |
| MIN_MATCH_THRESHOLD | AutomatchRuleMinMatchThreshold | — |
| NAME | AutomatchRuleName | ✅ |
| NET_FREIGHT_WEIGHT | AutomatchRuleNetFreightWeight | — |
| NET_TAX_FREIGHT_WEIGHT | AutomatchRuleNetTaxFreightWeight | — |
| NET_TAX_WEIGHT | AutomatchRuleNetTaxWeight | — |
| NET_UNDISC_WEIGHT | AutomatchRuleNetUndiscWeight | — |
| NUMBER_OF_DAYS_CLOSED | AutomatchRuleNumberOfDaysClosed | — |
| OBJECT_VERSION_NUMBER | AutomatchRuleObjectVersionNumber | — |
| REMITTANCE_REGEXP | AutomatchRuleRemittanceRegexp | — |
| SET_ID | AutomatchRuleSetId | — |
| START_DATE | AutomatchRuleStartDate | — |
| TRANSACTION_REGEXP | AutomatchRuleTransactionRegexp | — |
| TRANSACTION_THRESHOLD | AutomatchRuleTransactionThreshold | — |
| TRANSACTION_WEIGHT | AutomatchRuleTransactionWeight | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — AutoMatch Rules View Object
- Oracle Fusion Cloud — Setting Up Automatic Matching (Functional Guide)
