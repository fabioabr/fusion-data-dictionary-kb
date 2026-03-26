---
id: DOC-PO-014
doc_type: system-doc
title: "PON_BID_PO_LINES — Linhas de PO Geradas a partir de Lances"
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
  - sourcing
  - bid
  - po-lines
  - adjudicacao
aliases:
  - PON_BID_PO_LINES
  - pon_bid_po_lines
  - linhas-po-lance
  - bid-po-lines
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_PO_LINES

## 📌 Visão Geral

Armazena o **mapeamento entre linhas de lances adjudicados e linhas de pedidos de compra (PO)** gerados. Cada registro associa uma linha específica de um lance vencedor a uma linha correspondente no PO criado como resultado da adjudicação. Funciona como tabela de bridge entre o módulo de Sourcing e o módulo de Purchasing.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreabilidade Sourcing → PO:** Vínculo direto entre o lance vencedor e o pedido de compra resultante.
- **Auditoria de adjudicação:** Comprovação de que o PO foi criado a partir da proposta vencedora.
- **Reconciliação de quantidades:** Comparação entre quantidade adjudicada no lance e quantidade do PO.
- **Relatórios de ciclo completo:** Do requisito à entrega, passando por negociação e pedido.
- **Análise de savings realizados:** Comparação do preço negociado vs. preço efetivo no PO.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BID_NUMBER | NUMBER(18) | NOT NULL | PK/FK | Número do lance adjudicado | [[pon_bid_headers]] | 🟢 95% |
| 2 | BID_LINE_NUMBER | NUMBER | NOT NULL | PK/FK | Número da linha no lance | [[pon_bid_item_prices]] | 🟢 95% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 4 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID do pedido de compra gerado | [[po_headers_all]] | 🟢 95% |
| 5 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | ID da linha do PO gerada | [[po_lines_all]] | 🟢 95% |
| 6 | LINE_LOCATION_ID | NUMBER(18) | NULL | FK | ID da programação de entrega (schedule) | [[po_line_locations_all]] | 🟡 80% |
| 7 | PO_QUANTITY | NUMBER | NULL | Quantidade | Quantidade no pedido de compra | — | 🟡 75% |
| 8 | PO_PRICE | NUMBER | NULL | Financeiro | Preço unitário no pedido de compra | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_bid_item_prices]] — via `BID_NUMBER` + `BID_LINE_NUMBER` (preço do lance que originou a linha do PO)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação de origem da linha PO do lance)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO gerada a partir do lance)
- [[po_line_locations_all]] — via `LINE_LOCATION_ID` (schedule de entrega)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Rastreabilidade: do lance ao PO
```sql
SELECT bpl.BID_NUMBER, bpl.BID_LINE_NUMBER,
       ph.SEGMENT1 AS po_number, pl.LINE_NUM AS po_line,
       bpl.PO_QUANTITY, bpl.PO_PRICE
FROM   PON_BID_PO_LINES bpl
JOIN   PO_HEADERS_ALL ph ON ph.PO_HEADER_ID = bpl.PO_HEADER_ID
JOIN   PO_LINES_ALL pl ON pl.PO_LINE_ID = bpl.PO_LINE_ID
WHERE  bpl.AUCTION_HEADER_ID = :p_auction_header_id;
```

### POs gerados por lance vencedor
```sql
SELECT DISTINCT bpl.PO_HEADER_ID, ph.SEGMENT1 AS po_number
FROM   PON_BID_PO_LINES bpl
JOIN   PO_HEADERS_ALL ph ON ph.PO_HEADER_ID = bpl.PO_HEADER_ID
WHERE  bpl.BID_NUMBER = :p_bid_number;
```

---

## 🔒 Observações

- A tabela funciona como **bridge table** entre Sourcing (PON) e Purchasing (PO).
- Um mesmo lance pode gerar múltiplos POs (split por business unit, por exemplo).
- Uma mesma linha do lance pode ser dividida em múltiplas linhas de PO (split award por quantidade).
- O `LINE_LOCATION_ID` só é preenchido quando existe schedule de entrega definido no PO.
- Para rastrear o ciclo completo Negociação → Lance → PO, combine com [[pon_bid_po_numbers]].

---

## 📚 Referências

- [Oracle Docs — PON_BID_PO_LINES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidpolines.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
