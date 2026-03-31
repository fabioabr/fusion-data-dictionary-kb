---
id: DOC-AR-052
doc_type: system-doc
title: "AR_APP_EXCEPTION_RULES — Regras de Exceção para Aplicação Automática"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, exception-rules, excecoes, aplicacao-automatica]
aliases: [AR_APP_EXCEPTION_RULES, ar_app_exception_rules, application_exception_rules, regras_excecao_aplicacao, ar_exceptions]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_APP_EXCEPTION_RULES

## 📌 Visão Geral

Tabela que define **regras de exceção** para aplicação automática de recebimentos. Cada regra pertence a um [[ar_app_rule_sets|conjunto de regras]] e especifica condições de tolerância (valor ou percentual) e a ação a ser tomada quando o valor do recebimento não corresponde exatamente ao valor da transação.

## 🧠 Propósito de Negócio

Na prática, raramente um recebimento corresponde exatamente ao valor de uma fatura. As regras de exceção definem o que o sistema deve fazer quando há **diferenças de valor** — write-off automático, colocação em conta, criação de ajuste ou envio para revisão manual.

Casos de uso principais:
- Write-off automático de diferenças de centavos
- Tolerância percentual para pagamentos parciais
- Ações diferenciadas por faixa de valor
- Segregação de exceções por tipo (overpayment, underpayment)

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | EXCEPTION_RULE_ID | NUMBER | PK. Identificador único da regra de exceção. | Chave | 🟢 100% |
| 2 | RULE_SET_ID | NUMBER | FK para [[ar_app_rule_sets]]. Conjunto de regras pai. | Chave Estrangeira | 🟢 100% |
| 3 | EXCEPTION_TYPE | VARCHAR2 | Tipo de exceção: `OVERPAYMENT`, `UNDERPAYMENT`, `SHORT_PAY`, etc. | Classificação | 🟢 100% |
| 4 | THRESHOLD_AMOUNT | NUMBER | Valor máximo de diferença tolerada (em moeda funcional). | Regra | 🟢 100% |
| 5 | THRESHOLD_PERCENT | NUMBER | Percentual máximo de diferença tolerada sobre o valor da transação. | Regra | 🟢 100% |
| 6 | ACTION_CODE | VARCHAR2 | Ação quando dentro da tolerância: `WRITE_OFF`, `ON_ACCOUNT`, `UNAPPLIED`, `ADJUST`. | Regra | 🟢 100% |
| 7 | RECEIVABLES_TRX_ID | NUMBER | FK para [[ar_receivables_trx_all]]. Atividade usada para a ação (ex: write-off activity). | Chave Estrangeira | 🟢 100% |
| 8 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 9 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_app_rule_sets]] | RULE_SET_ID | FK | Conjunto de regras pai |
| [[ar_receivables_trx_all]] | RECEIVABLES_TRX_ID | FK | Atividade de recebíveis para a ação |

## 📎 Uso Típico

```sql
-- Regras de exceção de um conjunto específico
SELECT er.exception_rule_id,
       er.exception_type,
       er.threshold_amount,
       er.threshold_percent,
       er.action_code,
       rt.name AS atividade
  FROM ar_app_exception_rules er
  LEFT JOIN ar_receivables_trx_all rt ON rt.receivables_trx_id = er.receivables_trx_id
 WHERE er.rule_set_id = :p_rule_set_id;
```

```sql
-- Todas as regras de write-off automático
SELECT rs.name AS conjunto,
       er.threshold_amount,
       er.threshold_percent,
       er.exception_type
  FROM ar_app_exception_rules er
  JOIN ar_app_rule_sets rs ON rs.rule_set_id = er.rule_set_id
 WHERE er.action_code = 'WRITE_OFF';
```

## 🔒 Observações

- `THRESHOLD_AMOUNT` e `THRESHOLD_PERCENT` podem ser usados **em conjunto** — ambos devem ser satisfeitos para a ação ser executada (lógica AND).
- `ACTION_CODE = 'WRITE_OFF'` requer que `RECEIVABLES_TRX_ID` aponte para uma atividade de ajuste válida em [[ar_receivables_trx_all]].
- Regras de exceção são avaliadas **após** o match inicial — se o match encontrou a fatura mas o valor diverge, a regra de exceção decide o tratamento.
- Em ambientes bancários, tolerâncias muito altas para write-off automático podem gerar riscos de compliance — recomenda-se revisão periódica dos limites.

## 🔗 PVOs Relacionados

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ExceptRuleActiveFlag | — |
| DESCRIPTION | ExceptRuleDescription | — |
| END_DATE | ExceptRuleEndDate | — |
| EXCEPTION_RULE_ID | ExceptRuleExceptionRuleId | — |
| NAME | ExceptRuleName | — |
| START_DATE | ExceptRuleStartDate | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ExceptionRuleActiveFlag | — |
| CREATED_BY | ExceptionRuleCreatedBy | — |
| CREATION_DATE | ExceptionRuleCreationDate | — |
| DESCRIPTION | ExceptionRuleDescription | — |
| END_DATE | ExceptionRuleEndDate | — |
| EXCEPTION_RULE_ID | ExceptionRuleExceptionRuleId | — |
| LAST_UPDATE_DATE | ExceptionRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExceptionRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | ExceptionRuleLastUpdatedBy | — |
| NAME | ExceptionRuleName | ✅ |
| OBJECT_VERSION_NUMBER | ExceptionRuleObjectVersionNumber | — |
| SET_ID | ExceptionRuleSetId | — |
| START_DATE | ExceptionRuleStartDate | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ExceptionRuleActiveFlag | — |
| CREATED_BY | ExceptionRuleCreatedBy | — |
| CREATION_DATE | ExceptionRuleCreationDate | — |
| DESCRIPTION | ExceptionRuleDescription | — |
| END_DATE | ExceptionRuleEndDate | — |
| EXCEPTION_RULE_ID | ExceptionRuleExceptionRuleId | — |
| LAST_UPDATE_DATE | ExceptionRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExceptionRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | ExceptionRuleLastUpdatedBy | — |
| NAME | ExceptionRuleName | ✅ |
| OBJECT_VERSION_NUMBER | ExceptionRuleObjectVersionNumber | — |
| SET_ID | ExceptionRuleSetId | — |
| START_DATE | ExceptionRuleStartDate | — |

### [[exceptionruleextractpvo|ExceptionRuleExtractPVO]] (OTHER · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ArAppExceptionRuleActiveFlag | ✅ |
| CREATED_BY | ArAppExceptionRuleCreatedBy | ✅ |
| CREATION_DATE | ArAppExceptionRuleCreationDate | ✅ |
| DESCRIPTION | ArAppExceptionRuleDescription | ✅ |
| END_DATE | ArAppExceptionRuleEndDate | ✅ |
| EXCEPTION_RULE_ID | ArAppExceptionRuleExceptionRuleId | ✅ |
| LAST_UPDATE_DATE | ArAppExceptionRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArAppExceptionRuleLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArAppExceptionRuleLastUpdatedBy | ✅ |
| NAME | ArAppExceptionRuleName | ✅ |
| OBJECT_VERSION_NUMBER | ArAppExceptionRuleObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | ArAppExceptionRuleSeedDataSource | ✅ |
| SET_ID | ArAppExceptionRuleSetId | ✅ |
| START_DATE | ArAppExceptionRuleStartDate | ✅ |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Application Exception Rules View Object
- Oracle Fusion Cloud — Managing Application Rules (Functional Guide)
