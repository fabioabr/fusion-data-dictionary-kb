---
id: DOC-AR-002
doc_type: system-doc
title: "RA_CUSTOMER_TRX_LINES_ALL — Linhas de Transações AR"
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
  - linhas-transacao
  - itens-faturados
  - receita
aliases:
  - RA_CUSTOMER_TRX_LINES_ALL
  - ra_customer_trx_lines_all
  - linhas-transacoes-ar
  - invoice-lines
  - linhas-fatura
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUSTOMER_TRX_LINES_ALL

## 📌 Visão Geral

Armazena as **linhas de detalhe das transações** de clientes no módulo Accounts Receivable, incluindo valores, itens, quantidades e informações de receita. Cada linha pertence a um cabeçalho em [[ra_customer_trx_all]]. As linhas podem ser do tipo **LINE** (item/serviço), **TAX** (imposto) ou **FREIGHT** (frete), formando a estrutura granular de cada transação.

É a tabela de **detalhamento transacional** — toda análise de mix de produtos, receita por item ou reconciliação de valores passa por ela.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de faturamento:** Cada item/serviço faturado é registrado como uma linha individual com quantidade, preço unitário e valor estendido.
- **Cálculo de receita:** Campos como `REVENUE_AMOUNT`, `RULE_START_DATE` e `RULE_END_DATE` suportam reconhecimento de receita ao longo do tempo (revenue scheduling).
- **Análise de mix de produtos:** Associação de linhas a `INVENTORY_ITEM_ID` permite análises por produto/serviço.
- **Tributação:** Linhas do tipo TAX vinculam-se às linhas de item para detalhar impostos aplicados.
- **Frete:** Linhas do tipo FREIGHT registram custos de transporte associados à transação.
- **Referência a pedidos de venda:** Campos `SALES_ORDER` e `SALES_ORDER_LINE` conectam faturamento ao Order Management.
- **Interface com sistemas externos:** Campos `INTERFACE_LINE_ATTRIBUTE1–15` transportam dados da importação via AutoInvoice.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha de transação | — | 🟢 100% |
| 2 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Referência ao cabeçalho da transação | [[ra_customer_trx_all]] | 🟢 100% |
| 3 | LINE_NUMBER | NUMBER | NOT NULL | Identificação | Número sequencial da linha dentro da transação | — | 🟢 100% |
| 4 | LINE_TYPE | VARCHAR2(20) | NOT NULL | Classificação | Tipo da linha: LINE, TAX, FREIGHT, CHARGES | — | 🟢 100% |
| 5 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo (credit memos) | — | 🟢 100% |
| 6 | INVENTORY_ITEM_ID | NUMBER(18) | NULL | Produto | ID do item do inventário | [[mtl_system_items_b]] | 🟢 100% |
| 7 | DESCRIPTION | VARCHAR2(240) | NULL | Produto | Descrição textual da linha | — | 🟢 100% |
| 8 | QUANTITY_ORDERED | NUMBER | NULL | Quantidade | Quantidade originalmente pedida | — | 🟢 100% |
| 9 | QUANTITY_INVOICED | NUMBER | NULL | Quantidade | Quantidade efetivamente faturada | — | 🟢 100% |
| 10 | QUANTITY_CREDITED | NUMBER | NULL | Quantidade | Quantidade creditada (credit memos) | — | 🟢 100% |
| 11 | UNIT_SELLING_PRICE | NUMBER | NULL | Financeiro | Preço unitário de venda | — | 🟢 100% |
| 12 | UNIT_STANDARD_PRICE | NUMBER | NULL | Financeiro | Preço unitário de tabela (lista de preços) | — | 🟢 100% |
| 13 | EXTENDED_AMOUNT | NUMBER | NULL | Financeiro | Valor estendido da linha (qty × unit price) | — | 🟢 100% |
| 14 | REVENUE_AMOUNT | NUMBER | NULL | Financeiro | Valor de receita reconhecida para a linha | — | 🟢 100% |
| 15 | UOM_CODE | VARCHAR2(3) | NULL | Produto | Unidade de medida (Each, Kg, etc.) | — | 🟢 100% |
| 16 | TAX_EXEMPT_FLAG | VARCHAR2(1) | NULL | Tributação | Indica se a linha é isenta de imposto (S/E/R) | — | 🟢 100% |
| 17 | TAX_EXEMPT_REASON_CODE | VARCHAR2(30) | NULL | Tributação | Código do motivo de isenção fiscal | — | 🟢 100% |
| 18 | TAX_RATE | NUMBER | NULL | Tributação | Taxa de imposto aplicada à linha | — | 🟢 100% |
| 19 | TAX_PRECEDENCE | NUMBER | NULL | Tributação | Precedência do imposto (cálculo cascata) | — | 🟡 70% |
| 20 | WAREHOUSE_ID | NUMBER(18) | NULL | Logística | Depósito/almoxarifado de expedição | [[hr_all_organization_units_f]] | 🟢 100% |
| 21 | SALES_ORDER | VARCHAR2(50) | NULL | Referência cruzada | Número do pedido de venda (Order Management) | — | 🟢 100% |
| 22 | SALES_ORDER_LINE | VARCHAR2(30) | NULL | Referência cruzada | Linha do pedido de venda | — | 🟢 100% |
| 23 | SALES_ORDER_DATE | DATE | NULL | Referência cruzada | Data do pedido de venda | — | 🟢 100% |
| 24 | SALES_ORDER_SOURCE | VARCHAR2(50) | NULL | Referência cruzada | Origem do pedido de venda | — | 🟢 100% |
| 25 | ACCOUNTING_RULE_ID | NUMBER(18) | NULL | Contabilidade | Regra de reconhecimento de receita | [[ra_rules]] | 🟢 100% |
| 26 | ACCOUNTING_RULE_DURATION | NUMBER | NULL | Contabilidade | Duração da regra contábil (em períodos) | — | 🟢 100% |
| 27 | RULE_START_DATE | DATE | NULL | Contabilidade | Data de início do reconhecimento de receita | — | 🟢 100% |
| 28 | RULE_END_DATE | DATE | NULL | Contabilidade | Data final do reconhecimento de receita | — | 🟢 100% |
| 29 | AUTORULE_DURATION_PROCESSED | NUMBER | NULL | Contabilidade | Períodos já processados pela regra automática | — | 🟢 100% |
| 30 | AUTORULE_COMPLETE_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se a regra automática foi totalmente processada (Y/N) | — | 🟢 100% |
| 31 | LINK_TO_CUST_TRX_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Referência à linha-pai (TAX/FREIGHT vinculada a LINE) | self | 🟢 100% |
| 32 | PREVIOUS_CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Linha original (para credit memos vinculados a linhas) | self | 🟢 100% |
| 33 | INTERFACE_LINE_CONTEXT | VARCHAR2(30) | NULL | DFF | Contexto do flexfield de interface (AutoInvoice) | — | 🟢 100% |
| 34 | INTERFACE_LINE_ATTRIBUTE1 | VARCHAR2(150) | NULL | DFF | Atributo de interface 1 (tipicamente Sales Order ID) | — | 🟢 100% |
| 35 | INTERFACE_LINE_ATTRIBUTE2 | VARCHAR2(150) | NULL | DFF | Atributo de interface 2 (tipicamente Line ID) | — | 🟢 100% |
| 36 | INTERFACE_LINE_ATTRIBUTE3–15 | VARCHAR2(150) | NULL | DFF | Atributos de interface adicionais (3 a 15) | — | 🟢 100% |
| 37 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 38 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 39 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 40 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 41 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 42 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 43 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 44 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 45 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (cabeçalho da transação)
- [[mtl_system_items_b]] — via `INVENTORY_ITEM_ID` (item do inventário)
- [[ra_rules]] — via `ACCOUNTING_RULE_ID` (regra de reconhecimento de receita)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha de transação de cliente), `WAREHOUSE_ID` (depósito)

### Tabelas-filha (FK de saída)
- [[ra_cust_trx_line_gl_dist_all]] — via `CUSTOMER_TRX_LINE_ID` (distribuições contábeis)
- [[ra_cust_trx_line_salesreps_all]] — via `CUSTOMER_TRX_LINE_ID` (créditos de vendas)
- [[zx_lines]] — via `TRX_LINE_ID` (linhas de imposto detalhadas)

### Self-references
- `LINK_TO_CUST_TRX_LINE_ID` — Linha-pai (linhas TAX/FREIGHT vinculadas à LINE correspondente)
- `PREVIOUS_CUSTOMER_TRX_LINE_ID` — Linha original (para credit memos que referenciam linhas específicas)

---

## 📎 Uso Típico

### Detalhamento de itens faturados por transação
```sql
SELECT ct.TRX_NUMBER, ctl.LINE_NUMBER, ctl.DESCRIPTION,
       ctl.QUANTITY_INVOICED, ctl.UNIT_SELLING_PRICE,
       ctl.EXTENDED_AMOUNT
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_CUSTOMER_TRX_LINES_ALL ctl
       ON ctl.CUSTOMER_TRX_ID = ct.CUSTOMER_TRX_ID
WHERE  ctl.LINE_TYPE = 'LINE'
  AND  ct.ORG_ID = :p_org_id;
```

### Análise de receita por produto
```sql
SELECT ctl.INVENTORY_ITEM_ID, msib.SEGMENT1 AS item_number,
       SUM(ctl.REVENUE_AMOUNT) AS total_revenue
FROM   RA_CUSTOMER_TRX_LINES_ALL ctl
JOIN   MTL_SYSTEM_ITEMS_B msib
       ON msib.INVENTORY_ITEM_ID = ctl.INVENTORY_ITEM_ID
WHERE  ctl.LINE_TYPE = 'LINE'
  AND  ctl.ORG_ID = :p_org_id
GROUP BY ctl.INVENTORY_ITEM_ID, msib.SEGMENT1;
```

### Filtros comuns
- `LINE_TYPE = 'LINE'` — Apenas linhas de item (excluir TAX/FREIGHT)
- `ACCOUNTING_RULE_ID IS NOT NULL` — Linhas com reconhecimento de receita diferido
- `SALES_ORDER IS NOT NULL` — Linhas originadas de pedidos de venda
- `INTERFACE_LINE_CONTEXT` — Identificar origem da importação (AutoInvoice)

---

## 🔒 Observações

- Linhas do tipo **TAX** e **FREIGHT** possuem `LINK_TO_CUST_TRX_LINE_ID` apontando para a linha de item (LINE) correspondente.
- O campo `EXTENDED_AMOUNT` é calculado como `QUANTITY_INVOICED × UNIT_SELLING_PRICE`, mas pode ser informado diretamente para linhas sem quantidade.
- Os campos `INTERFACE_LINE_ATTRIBUTE1–15` são críticos para rastreabilidade: identificam a origem da linha quando importada via **AutoInvoice** (e.g., Order Management, Projects).
- O campo `ACCOUNTING_RULE_ID` com `RULE_START_DATE` / `RULE_END_DATE` ativa o **Revenue Scheduling** — a receita é distribuída em múltiplos períodos contábeis.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15` para customizações por implementação.
- Para credit memos vinculados a linhas específicas, `PREVIOUS_CUSTOMER_TRX_LINE_ID` conecta à linha original da fatura.

---

## 📚 Referências

- [Oracle Docs — RA_CUSTOMER_TRX_LINES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racustomertrxlinesall-25166.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
