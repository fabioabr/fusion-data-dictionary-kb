---
id: DOC-PO-132
doc_type: system-doc
title: "PO_LINES_ALL — Linhas de Ordens de Compra"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_LINES_ALL
  - po_lines_all
  - po-lines-all
  - po-lines
  - linhas-de-ordens-de-compra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINES_ALL

## 📌 Visão Geral

Armazena as **linhas de ordens de compra**. Cada linha representa um item ou servico comprado com quantidade, preco unitario, tipo de linha e referencias de catalogo.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento do PO:** Itens/servicos com preco e quantidade.
- **Catalogo:** Referencia a itens internos ou externos.
- **Agreements:** Linhas de BPA e CPA.
- **Receiving:** Base para recebimento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_LINE_ID | NUMBER(18) | NOT NULL | PK | ID unico | — | 🟢 100% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟢 100% |
| 3 | LINE_NUM | NUMBER | NOT NULL | Identificacao | Numero da linha | — | 🟢 100% |
| 4 | LINE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de linha | [[po_line_types_b]] | 🟢 100% |
| 5 | ITEM_ID | NUMBER(18) | NULL | FK | Item | [[egp_system_items_b]] | 🟢 100% |
| 6 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao do item | — | 🟢 100% |
| 7 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[egp_categories_b]] | 🟢 100% |
| 8 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preco unitario | — | 🟢 100% |
| 9 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade total | — | 🟢 100% |
| 10 | UNIT_MEAS_LOOKUP_CODE | VARCHAR2(25) | NULL | Classificacao | UoM | — | 🟢 100% |
| 11 | AMOUNT | NUMBER | NULL | Financeiro | Valor total | — | 🟢 95% |
| 12 | FROM_HEADER_ID | NUMBER(18) | NULL | FK | Agreement de referencia | [[po_headers_all]] | 🟢 90% |
| 13 | VENDOR_PRODUCT_NUM | VARCHAR2(25) | NULL | Identificacao | Codigo no fornecedor | — | 🟢 85% |
| 14 | CANCEL_FLAG | VARCHAR2(1) | NULL | Flag | Cancelada | — | 🟢 95% |
| 15 | CLOSED_CODE | VARCHAR2(25) | NULL | Status | OPEN/CLOSED/FINALLY CLOSED | — | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra ao qual a linha pertence)
- [[po_line_types_b]] — via `LINE_TYPE_ID` (tipo da linha do pedido de compra)
- [[egp_system_items_b]] — via `ITEM_ID` (item do catálogo na linha do pedido de compra)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de compra da linha do PO)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Linhas de um PO
```sql
SELECT PO_LINE_ID, LINE_NUM, ITEM_DESCRIPTION, UNIT_PRICE, QUANTITY
FROM   PO_LINES_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
  AND  NVL(CANCEL_FLAG,'N') = 'N'
ORDER BY LINE_NUM;
```


---

## 🔒 Observações

- Cada linha pode ter multiplos schedules.
- O `FROM_HEADER_ID` referencia agreement de origem.
- Linhas de servico usam `AMOUNT` em vez de `QUANTITY` x `UNIT_PRICE`.

---

## 📚 Referências

- [Oracle Docs — PO_LINES_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/polinesall-10200.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
