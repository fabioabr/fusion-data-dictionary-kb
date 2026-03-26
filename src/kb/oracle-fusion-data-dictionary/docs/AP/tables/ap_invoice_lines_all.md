---
id: DOC-AP-013
doc_type: system-doc
title: "AP_INVOICE_LINES_ALL — Linhas de Faturas de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - linhas-fatura
  - invoice-lines
  - ap-lines
aliases:
  - AP_INVOICE_LINES_ALL
  - ap_invoice_lines_all
  - linhas-fatura-ap
  - invoice-lines-ap
  - linhas-faturas-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICE_LINES_ALL

## 📌 Visão Geral

Armazena as **linhas** de cada fatura do módulo Accounts Payable. Cada linha representa um item, imposto, frete ou encargo dentro da fatura, contendo descrição, quantidade, valor unitário, valor total e referência a pedido de compra. Atua como nível intermediário entre o cabeçalho da fatura ([[ap_invoices_all]]) e as distribuições contábeis ([[ap_invoice_distributions_all]]).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento da fatura:** Cada item, serviço, imposto ou frete recebido é registrado como uma linha separada.
- **Matching com PO:** Linhas do tipo ITEM podem ser vinculadas a linhas de pedido de compra para validação de preço e quantidade.
- **Cálculo de impostos:** Linhas do tipo TAX armazenam os impostos calculados automaticamente ou informados manualmente.
- **Geração de distribuições:** Cada linha gera uma ou mais distribuições contábeis em [[ap_invoice_distributions_all]].
- **Retenções fiscais:** Suporte a linhas de withholding tax (AWT) geradas automaticamente.
- **Rastreabilidade:** Vinculação de cada item da fatura ao respectivo PO line e shipment para auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da fatura (parte da PK composta) | [[ap_invoices_all]] | 🟢 100% |
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número sequencial da linha na fatura | — | 🟢 100% |
| 3 | LINE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da linha (ITEM/TAX/FREIGHT/MISCELLANEOUS/AWT) | [[ap_lookup_codes]] | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da linha na moeda da transação | — | 🟢 100% |
| 5 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 6 | QUANTITY_INVOICED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 7 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preço unitário | — | 🟢 100% |
| 8 | UNIT_MEAS_LOOKUP_CODE | VARCHAR2(25) | NULL | Quantidade | Unidade de medida | — | 🟢 100% |
| 9 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da linha | — | 🟢 100% |
| 10 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil da linha | — | 🟢 100% |
| 11 | DIST_CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil padrão | [[gl_code_combinations]] | 🟢 100% |
| 12 | PO_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | Cabeçalho do PO vinculado | [[po_headers_all]] | 🟢 100% |
| 13 | PO_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Linha do PO vinculada | [[po_lines_all]] | 🟢 100% |
| 14 | PO_LINE_LOCATION_ID | NUMBER(18) | NULL | Referência cruzada | Shipment do PO vinculado | [[po_line_locations_all]] | 🟢 100% |
| 15 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | Referência cruzada | Distribuição do PO vinculada | [[po_distributions_all]] | 🟢 100% |
| 16 | RCV_TRANSACTION_ID | NUMBER(18) | NULL | Referência cruzada | Transação de recebimento vinculada | [[rcv_transactions]] | 🟢 100% |
| 17 | RCV_SHIPMENT_LINE_ID | NUMBER(18) | NULL | Referência cruzada | Linha de shipment de recebimento | [[rcv_shipment_lines]] | 🟡 75% |
| 18 | MATCH_TYPE | VARCHAR2(25) | NULL | Classificação | Tipo de matching (ITEM_TO_PO/ITEM_TO_RECEIPT/etc.) | — | 🟢 100% |
| 19 | TAX_CLASSIFICATION_CODE | VARCHAR2(30) | NULL | Fiscal | Código de classificação fiscal | — | 🟢 100% |
| 20 | TAX_RATE_ID | NUMBER(18) | NULL | Fiscal | ID da taxa de imposto | — | 🟡 75% |
| 21 | TAX_RATE | NUMBER | NULL | Fiscal | Percentual do imposto | — | 🟢 100% |
| 22 | INCOME_TAX_REGION | VARCHAR2(10) | NULL | Fiscal | Região fiscal (imposto de renda) | — | 🟡 75% |
| 23 | TYPE_1099 | VARCHAR2(10) | NULL | Fiscal | Tipo 1099 (reporting fiscal US) | — | 🟡 70% |
| 24 | DISCARDED_FLAG | VARCHAR2(1) | NULL | Status | Indica se a linha foi descartada (Y/N) | — | 🟢 100% |
| 25 | CANCELLED_FLAG | VARCHAR2(1) | NULL | Status | Indica se a linha foi cancelada (Y/N) | — | 🟢 100% |
| 26 | GENERATE_DISTS | VARCHAR2(1) | NULL | Controle | Indica se distribuições foram geradas (Y/D/N) | — | 🟢 100% |
| 27 | ASSETS_TRACKING_FLAG | VARCHAR2(1) | NULL | Controle | Rastreamento de ativo fixo (Y/N) | — | 🟢 100% |
| 28 | PROJECT_ID | NUMBER(18) | NULL | Projetos | Projeto vinculado | [[pjf_projects_all_b]] | 🟢 100% |
| 29 | TASK_ID | NUMBER(18) | NULL | Projetos | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 100% |
| 30 | ITEM_ID | NUMBER(18) | NULL | Item | Item do inventário | [[egp_system_items_b]] | 🟡 75% |
| 31 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Item | Descrição do item | — | 🟢 100% |
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
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura-cabeçalho)
- [[gl_code_combinations]] — via `DIST_CODE_COMBINATION_ID` (conta contábil padrão)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do pedido de compra vinculada à linha da fatura)
- [[po_line_locations_all]] — via `PO_LINE_LOCATION_ID` (shipment do PO referenciado na linha da fatura)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuição do PO)
- [[rcv_transactions]] — via `RCV_TRANSACTION_ID` (recebimento físico vinculado à linha da fatura)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto associado à linha da fatura)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha da fatura)

### Tabelas-filha (FK de saída)
- [[ap_invoice_distributions_all]] — via `INVOICE_ID` + `LINE_NUMBER` (distribuições contábeis)

---

## 📎 Uso Típico

### Linhas de uma fatura
```sql
SELECT ail.LINE_NUMBER, ail.LINE_TYPE_LOOKUP_CODE,
       ail.DESCRIPTION, ail.QUANTITY_INVOICED,
       ail.UNIT_PRICE, ail.AMOUNT
FROM   AP_INVOICE_LINES_ALL ail
WHERE  ail.INVOICE_ID = :p_invoice_id
ORDER BY ail.LINE_NUMBER;
```

### Linhas com matching a PO
```sql
SELECT ail.LINE_NUMBER, ail.AMOUNT, ail.MATCH_TYPE,
       ph.SEGMENT1 AS po_number, pl.LINE_NUM AS po_line
FROM   AP_INVOICE_LINES_ALL ail
JOIN   PO_HEADERS_ALL ph ON ph.PO_HEADER_ID = ail.PO_HEADER_ID
JOIN   PO_LINES_ALL pl ON pl.PO_LINE_ID = ail.PO_LINE_ID
WHERE  ail.INVOICE_ID = :p_invoice_id
  AND  ail.LINE_TYPE_LOOKUP_CODE = 'ITEM';
```

### Filtros comuns
- `LINE_TYPE_LOOKUP_CODE = 'ITEM'` — Apenas linhas de item
- `DISCARDED_FLAG IS NULL OR DISCARDED_FLAG = 'N'` — Exclui descartadas
- `CANCELLED_FLAG IS NULL OR CANCELLED_FLAG = 'N'` — Exclui canceladas

---

## 🔒 Observações

- O campo `LINE_TYPE_LOOKUP_CODE` classifica a linha: **ITEM** (item/serviço), **TAX** (imposto), **FREIGHT** (frete), **MISCELLANEOUS** (diversos), **AWT** (withholding tax).
- Linhas do tipo **ITEM** podem ser vinculadas a PO lines/shipments para matching. O campo `MATCH_TYPE` indica o tipo de matching realizado.
- A PK composta é `INVOICE_ID` + `LINE_NUMBER`.
- O campo `GENERATE_DISTS` controla a geração de distribuições: **Y** (gerar), **D** (já gerado), **N** (não gerar).
- Linhas descartadas (`DISCARDED_FLAG = 'Y'`) permanecem na tabela mas são ignoradas nos processos de negócio.

---

## 📚 Referências

- [Oracle Docs — AP_INVOICE_LINES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicelinesall-10010.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
