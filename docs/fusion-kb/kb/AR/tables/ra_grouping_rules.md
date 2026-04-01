---
id: DOC-AR-011
doc_type: system-doc
title: "RA_GROUPING_RULES — Regras de Agrupamento AutoInvoice"
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
  - grouping-rules
  - autoinvoice
  - configuracao
aliases:
  - RA_GROUPING_RULES
  - ra_grouping_rules
  - regras-agrupamento-ar
  - autoinvoice-grouping
  - grouping-rules-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_GROUPING_RULES

## 📌 Visão Geral

Define **regras de agrupamento para a geração automática de faturas** pelo processo AutoInvoice. Cada registro determina quais critérios devem ser iguais para que linhas da interface (`RA_INTERFACE_LINES_ALL`) sejam consolidadas em uma única fatura durante a importação.

É uma tabela de **configuração** com poucos registros — tipicamente uma regra por cenário de negócio (ex.: agrupamento por ordem de venda, por contrato, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **AutoInvoice:** O processo de importação automática de faturas utiliza estas regras para decidir se linhas da interface devem ser agrupadas em uma mesma fatura ou gerar faturas separadas.
- **Otimização de volume:** Regras de agrupamento mais amplas reduzem o número de faturas geradas, otimizando impressão e envio.
- **Conformidade com requisitos de clientes:** Alguns clientes exigem faturas separadas por pedido ou por entrega — as regras de agrupamento atendem essa necessidade.
- **Integração com Order Management:** Pedidos de venda importados no AR utilizam estas regras para consolidar linhas em faturas.
- **Configuração de tipos de transação:** Cada tipo de transação em [[ra_cust_trx_types_all]] pode referenciar uma regra de agrupamento específica.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GROUPING_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra de agrupamento | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome da regra de agrupamento | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição da regra e seus critérios | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status ativo/inativo (A=Active, I=Inactive) | — | 🟢 100% |
| 5 | LINE_ORDERING_RULE_ID | NUMBER(18) | NULL | Configuração | Regra de ordenação de linhas dentro da fatura gerada | [[ra_line_ordering_rules]] | 🟢 100% |
| 6 | GROUP_BY_SALESREP_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por vendedor (Y/N) | — | 🟢 100% |
| 7 | GROUP_BY_GL_DATE_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por data contábil GL (Y/N) | — | 🟢 100% |
| 8 | GROUP_BY_SHIP_TO_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por endereço de entrega (Y/N) | — | 🟢 100% |
| 9 | GROUP_BY_CURRENCY_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por moeda (Y/N) | — | 🟢 100% |
| 10 | GROUP_BY_PAYMENT_TERM_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por condição de pagamento (Y/N) | — | 🟢 100% |
| 11 | GROUP_BY_FOB_POINT_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por ponto FOB (Y/N) | — | 🟢 100% |
| 12 | GROUP_BY_CUSTOMER_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por cliente (Y/N) | — | 🟢 100% |
| 13 | GROUP_BY_FREIGHT_CARRIER_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por transportadora (Y/N) | — | 🟢 100% |
| 14 | GROUP_BY_ORDER_FLAG | VARCHAR2(1) | NULL | Agrupamento | Agrupar por número do pedido (Y/N) | — | 🟢 100% |
| 15 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 21 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 22 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_line_ordering_rules]] — via `LINE_ORDERING_RULE_ID` (regra de ordenação de linhas)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da regra de agrupamento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consultar regras de agrupamento ativas
```sql
SELECT gr.GROUPING_RULE_ID, gr.NAME, gr.DESCRIPTION,
       gr.GROUP_BY_SALESREP_FLAG, gr.GROUP_BY_GL_DATE_FLAG,
       gr.GROUP_BY_SHIP_TO_FLAG, gr.GROUP_BY_ORDER_FLAG
FROM   RA_GROUPING_RULES gr
WHERE  gr.STATUS = 'A'
ORDER BY gr.NAME;
```

### Identificar tipos de transação vinculados a uma regra
```sql
SELECT tt.NAME AS tipo_transacao, gr.NAME AS regra_agrupamento,
       gr.DESCRIPTION
FROM   RA_CUST_TRX_TYPES_ALL tt
JOIN   RA_GROUPING_RULES gr ON gr.GROUPING_RULE_ID = tt.DEFAULT_GROUPING_RULE_ID
WHERE  tt.STATUS = 'A'
  AND  tt.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'A'` — Apenas regras ativas
- `GROUP_BY_ORDER_FLAG = 'Y'` — Regras que agrupam por pedido
- `GROUP_BY_SALESREP_FLAG = 'Y'` — Regras que agrupam por vendedor

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- As colunas `GROUP_BY_*_FLAG` funcionam como **critérios aditivos**: quando marcadas como 'Y', exigem que as linhas de interface tenham o mesmo valor naquele atributo para serem agrupadas.
- Quanto mais flags de agrupamento estiverem como 'Y', **mais restritiva** é a regra — ou seja, mais faturas serão geradas (menor consolidação).
- Regras com todos os flags como 'N' geram a **máxima consolidação** — todas as linhas de um mesmo cliente/organização vão para uma única fatura.
- É uma tabela de **baixo volume** — tipicamente contém menos de 10 registros por implementação.
- Alterações na regra de agrupamento **não afetam faturas já geradas** — apenas processamentos futuros do AutoInvoice.

---

## 🔗 PVOs Relacionados

### [[customerfinancialprofilepvo|CustomerFinancialProfilePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TrxReqGroupingRuleDescription | — |
| END_DATE | TrxReqGroupingRuleEndDate | — |
| GROUPING_RULE_ID | TrxReqGroupingRuleGroupingRuleId | — |
| NAME | TrxReqGroupingRuleName | — |
| ORDERING_RULE_ID | TrxReqGroupingRuleOrderingRuleId | — |
| START_DATE | TrxReqGroupingRuleStartDate | — |

### [[customerprofile|CustomerProfile]] (AR · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | RaGrpRuleAttributeCategory | — |
| CREATED_BY | RaGrpRuleCreatedBy | — |
| CREATION_DATE | RaGrpRuleCreationDate | — |
| DESCRIPTION | RaGrpRuleDescription | — |
| END_DATE | RaGrpRuleEndDate | — |
| GROUPING_RULE_ID | RaGrpRuleGroupingRuleId | — |
| LAST_UPDATE_DATE | RaGrpRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaGrpRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | RaGrpRuleLastUpdatedBy | — |
| NAME | RaGrpRuleName | ✅ |
| OBJECT_VERSION_NUMBER | RaGrpRuleObjectVersionNumber | — |
| ORDERING_RULE_ID | RaGrpRuleOrderingRuleId | — |
| START_DATE | RaGrpRuleStartDate | — |

### [[customersiteprofile|CustomerSiteProfile]] (AR · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | RaGrpRuleAttributeCategory | — |
| CREATED_BY | RaGrpRuleCreatedBy | — |
| CREATION_DATE | RaGrpRuleCreationDate | — |
| DESCRIPTION | RaGrpRuleDescription | — |
| END_DATE | RaGrpRuleEndDate | — |
| GROUPING_RULE_ID | RaGrpRuleGroupingRuleId | — |
| LAST_UPDATE_DATE | RaGrpRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaGrpRuleLastUpdateLogin | — |
| LAST_UPDATED_BY | RaGrpRuleLastUpdatedBy | — |
| NAME | RaGrpRuleName | ✅ |
| OBJECT_VERSION_NUMBER | RaGrpRuleObjectVersionNumber | — |
| ORDERING_RULE_ID | RaGrpRuleOrderingRuleId | — |
| START_DATE | RaGrpRuleStartDate | — |

### [[transactionrequestgroupingruleextractpvo|TransactionRequestGroupingRuleExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | RaGroupingRuleAttribute1 | — |
| ATTRIBUTE10 | RaGroupingRuleAttribute10 | — |
| ATTRIBUTE11 | RaGroupingRuleAttribute11 | — |
| ATTRIBUTE12 | RaGroupingRuleAttribute12 | — |
| ATTRIBUTE13 | RaGroupingRuleAttribute13 | — |
| ATTRIBUTE14 | RaGroupingRuleAttribute14 | — |
| ATTRIBUTE15 | RaGroupingRuleAttribute15 | — |
| ATTRIBUTE2 | RaGroupingRuleAttribute2 | — |
| ATTRIBUTE3 | RaGroupingRuleAttribute3 | — |
| ATTRIBUTE4 | RaGroupingRuleAttribute4 | — |
| ATTRIBUTE5 | RaGroupingRuleAttribute5 | — |
| ATTRIBUTE6 | RaGroupingRuleAttribute6 | — |
| ATTRIBUTE7 | RaGroupingRuleAttribute7 | — |
| ATTRIBUTE8 | RaGroupingRuleAttribute8 | — |
| ATTRIBUTE9 | RaGroupingRuleAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaGroupingRuleAttributeCategory | — |
| CREATED_BY | RaGroupingRuleCreatedBy | ✅ |
| CREATION_DATE | RaGroupingRuleCreationDate | ✅ |
| DESCRIPTION | RaGroupingRuleDescription | ✅ |
| END_DATE | RaGroupingRuleEndDate | ✅ |
| GROUPING_RULE_ID | RaGroupingRuleGroupingRuleId | ✅ |
| LAST_UPDATE_DATE | RaGroupingRuleLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaGroupingRuleLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaGroupingRuleLastUpdatedBy | ✅ |
| NAME | RaGroupingRuleName | ✅ |
| OBJECT_VERSION_NUMBER | RaGroupingRuleObjectVersionNumber | ✅ |
| ORDERING_RULE_ID | RaGroupingRuleOrderingRuleId | ✅ |
| SEED_DATA_SOURCE | RaGroupingRuleSeedDataSource | ✅ |
| START_DATE | RaGroupingRuleStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — RA_GROUPING_RULES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ragroupingrules-10058.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
