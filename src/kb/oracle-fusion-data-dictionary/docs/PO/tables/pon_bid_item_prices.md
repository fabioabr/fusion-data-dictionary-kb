---
id: DOC-PO-013
doc_type: system-doc
title: "PON_BID_ITEM_PRICES — Preços de Itens em Lances"
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
  - precos-itens
aliases:
  - PON_BID_ITEM_PRICES
  - pon_bid_item_prices
  - precos-itens-lance
  - bid-item-prices
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_ITEM_PRICES

## 📌 Visão Geral

Armazena os **preços unitários e informações de linha** dos itens ofertados pelos fornecedores em seus lances (bids) de Sourcing. Cada registro representa o preço proposto para um item específico da negociação, incluindo quantidade, unidade de medida, data prometida de entrega e informações de cost breakdown. É a tabela central para análise financeira de propostas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Análise de preços:** Comparação de preços unitários e totais entre fornecedores participantes.
- **Cálculo de savings:** Diferença entre preço de referência (target price) e preço ofertado.
- **Adjudicação por linha:** Permite adjudicar itens individualmente a diferentes fornecedores (split award).
- **Geração de PO:** Base para criação automática de pedidos de compra a partir do lance vencedor.
- **Negociação multi-rodada:** Histórico de evolução de preços ao longo das rodadas.
- **Análise TCO (Total Cost of Ownership):** Quando integrado com cost factors e atributos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BID_NUMBER | NUMBER(18) | NOT NULL | PK/FK | Número do lance do fornecedor | [[pon_bid_headers]] | 🟢 100% |
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número da linha do item na negociação | — | 🟢 100% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 4 | AUCTION_LINE_NUMBER | NUMBER | NOT NULL | FK | Número da linha na negociação | [[pon_auction_item_prices_all]] | 🟢 95% |
| 5 | BID_PRICE | NUMBER | NULL | Financeiro | Preço unitário ofertado pelo fornecedor | — | 🟢 95% |
| 6 | BID_QUANTITY | NUMBER | NULL | Quantidade | Quantidade ofertada | — | 🟢 90% |
| 7 | PRICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do preço ofertado | — | 🟢 90% |
| 8 | UNIT_OF_MEASURE | VARCHAR2(25) | NULL | Classificação | Unidade de medida do item | — | 🟢 90% |
| 9 | BID_LINE_TOTAL | NUMBER | NULL | Financeiro | Valor total da linha (preço × quantidade) | — | 🟢 85% |
| 10 | PROMISED_DATE | DATE | NULL | Data | Data prometida de entrega | — | 🟢 85% |
| 11 | AWARD_STATUS | VARCHAR2(30) | NULL | Classificação | Status de adjudicação da linha: AWARDED, REJECTED | — | 🟢 90% |
| 12 | AWARD_QUANTITY | NUMBER | NULL | Quantidade | Quantidade adjudicada (pode ser parcial — split award) | — | 🟢 85% |
| 13 | AWARD_DATE | DATE | NULL | Data | Data de adjudicação da linha | — | 🟢 85% |
| 14 | AWARD_PRICE | NUMBER | NULL | Financeiro | Preço final adjudicado (pode diferir do bid_price após negociação) | — | 🟡 75% |
| 15 | TARGET_PRICE | NUMBER | NULL | Financeiro | Preço de referência/target definido pelo comprador | — | 🟡 70% |
| 16 | PO_HEADER_ID | NUMBER(18) | NULL | FK | Pedido de compra gerado a partir deste lance | [[po_headers_all]] | 🟢 85% |
| 17 | PO_LINE_ID | NUMBER(18) | NULL | FK | Linha do PO gerada | [[po_lines_all]] | 🟢 85% |
| 18 | NOTE_TO_BUYER | VARCHAR2(4000) | NULL | Texto livre | Comentários do fornecedor ao comprador sobre a linha | — | 🟢 85% |
| 19 | ITEM_ID | NUMBER(18) | NULL | FK | ID do item no catálogo | — | 🟡 75% |
| 20 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Referência | Descrição do item (desnormalizado) | — | 🟢 90% |
| 21 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria do item | [[egp_categories_tl]] | 🟡 75% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 23 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 25 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 26 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o preço do lance pertence)
- [[pon_auction_item_prices_all]] — via `AUCTION_HEADER_ID` + `AUCTION_LINE_NUMBER` (linha da negociação)

### Tabelas-filha (FK de saída)
- [[pon_bid_attribute_values]] — via `BID_NUMBER` + `LINE_NUMBER` (atributos da linha)

### Tabelas relacionadas
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra gerado a partir do lance vencedor)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO gerado)

---

## 📎 Uso Típico

### Preços ofertados por todos os fornecedores para um item
```sql
SELECT bh.VENDOR_NAME, bip.BID_PRICE, bip.BID_QUANTITY,
       bip.BID_LINE_TOTAL, bip.PROMISED_DATE, bip.AWARD_STATUS
FROM   PON_BID_ITEM_PRICES bip
JOIN   PON_BID_HEADERS bh ON bh.BID_NUMBER = bip.BID_NUMBER
WHERE  bip.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bip.LINE_NUMBER = :p_line_number
  AND  bh.BID_STATUS = 'ACTIVE'
ORDER BY bip.BID_PRICE;
```

### Linhas adjudicadas com PO gerado
```sql
SELECT bip.LINE_NUMBER, bip.ITEM_DESCRIPTION, bip.BID_PRICE,
       bip.AWARD_QUANTITY, bip.PO_HEADER_ID, bip.PO_LINE_ID
FROM   PON_BID_ITEM_PRICES bip
WHERE  bip.BID_NUMBER = :p_bid_number
  AND  bip.AWARD_STATUS = 'AWARDED'
  AND  bip.PO_HEADER_ID IS NOT NULL;
```

---

## 🔒 Observações

- A chave primária é composta por `BID_NUMBER` + `LINE_NUMBER`.
- O `AWARD_STATUS` é independente por linha — permite split award (adjudicação parcial a diferentes fornecedores).
- O `PO_HEADER_ID` e `PO_LINE_ID` são preenchidos após a criação automática do pedido de compra a partir do lance.
- O `TARGET_PRICE` pode não estar visível ao fornecedor dependendo da configuração da negociação.
- Para negociações com multi-moeda, o `PRICE_CURRENCY_CODE` pode diferir da moeda base da negociação.

---

## 📚 Referências

- [Oracle Docs — PON_BID_ITEM_PRICES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbiditemprices.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
