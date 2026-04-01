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

## 🔗 PVOs Relacionados

### [[agreementlinepvo|AgreementLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 1/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO · BICC: 26/89)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | — |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| AWARD_DATE | ResponseLineAwardDate | — |
| AWARD_PRICE | ResponseLineAwardPrice1 | — |
| AWARD_QUANTITY | ResponseLineAwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | ResponseLineAwardStatus | ✅ |
| BATCH_ID | ResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | BidNumber | ✅ |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | ResponseLineCreatedBy | — |
| CREATION_DATE | ResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | — |
| DOCUMENT_DISP_LINE_NUMBER | ResponseLineDocumentDispLineNumber | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | ResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | — |
| LINE_NUMBER | LineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | ResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | — |
| OLD_QUANTITY | ResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | — |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | — |
| PROGRAM_NAME | ResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | ResponseLinePromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | ResponseLinePromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | — |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | — |
| PURCHASING_ITEM_ID | PurchasingItemId | — |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | — |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | ResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | — |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CODE | UomCode1 | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | ✅ |
| WORKSHEET_NAME | ResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | — |

### [[draftpurchasingdocumentlinepvo|DraftPurchasingDocumentLinePVO]] (PO · BICC: 1/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[negotiationawardacceptancepvo|NegotiationAwardAcceptancePVO]] (PO · BICC: 78/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | ✅ |
| AWARD_DATE | ResponseLineAwardDate | ✅ |
| AWARD_PRICE | ResponseLineAwardPrice | ✅ |
| AWARD_QUANTITY | ResponseLineAwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | ✅ |
| AWARD_STATUS | ResponseLineAwardStatus | ✅ |
| BATCH_ID | ResponseLineBatchId | ✅ |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | ✅ |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | ✅ |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | ✅ |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | ✅ |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | ✅ |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | ✅ |
| BID_NUMBER | ResponseLineBidNumber | ✅ |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | ✅ |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | ✅ |
| CREATED_BY | ResponseLineCreatedBy | ✅ |
| CREATION_DATE | ResponseLineCreationDate | ✅ |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | ✅ |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | ✅ |
| GROUP_AMOUNT | ResponseLineGroupAmount | ✅ |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | ✅ |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | ✅ |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | ✅ |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | ✅ |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | ✅ |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | ✅ |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | ✅ |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | ✅ |
| LINE_NUMBER | ResponseLineLineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | ✅ |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | ✅ |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | ✅ |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | ✅ |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | ✅ |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | ✅ |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | ✅ |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | ✅ |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | ✅ |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | ✅ |
| OLD_PRICE | ResponseLineOldPrice | ✅ |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | ✅ |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | ✅ |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | ✅ |
| OLD_QUANTITY | ResponseLineOldQuantity | ✅ |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | ✅ |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | ✅ |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | ✅ |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | ✅ |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | ✅ |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | ✅ |
| PROGRAM_NAME | ResponseLineProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | ✅ |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | ✅ |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | ✅ |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | ✅ |
| REQUEST_ID | ResponseLineRequestId | ✅ |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | ✅ |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | ✅ |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| WORKSHEET_NAME | ResponseLineWorksheetName | ✅ |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | ✅ |

### [[negotiationresponsecostfactorpvo|NegotiationResponseCostFactorPVO]] (PO · BICC: 88/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | ✅ |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | ✅ |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| AWARD_DATE | ResponseLineAwardDate | ✅ |
| AWARD_PRICE | ResponseLineAwardPrice | ✅ |
| AWARD_QUANTITY | ResponseLineAwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | ✅ |
| AWARD_STATUS | ResponseLineAwardStatus | ✅ |
| BATCH_ID | ResponseLineBatchId | ✅ |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | ✅ |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | ✅ |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | ✅ |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | ✅ |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | ✅ |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | ✅ |
| BID_NUMBER | ResponseLineBidNumber | ✅ |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | ✅ |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | ✅ |
| CREATED_BY | ResponseLineCreatedBy | ✅ |
| CREATION_DATE | ResponseLineCreationDate | ✅ |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | ✅ |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | ✅ |
| GROUP_AMOUNT | ResponseLineGroupAmount | ✅ |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | ✅ |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | ✅ |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | ✅ |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | ✅ |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | ✅ |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | ✅ |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | ✅ |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | ✅ |
| LINE_NUMBER | ResponseLineLineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | ✅ |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | ✅ |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | ✅ |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | ✅ |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | ✅ |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | ✅ |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | ✅ |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | ✅ |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | ✅ |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | ✅ |
| OLD_PRICE | ResponseLineOldPrice | ✅ |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | ✅ |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | ✅ |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | ✅ |
| OLD_QUANTITY | ResponseLineOldQuantity | ✅ |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | ✅ |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | ✅ |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | ✅ |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | ✅ |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | ✅ |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | ✅ |
| PROGRAM_NAME | ResponseLineProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | ✅ |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | ✅ |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | ResponseLinePromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | ResponseLinePromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | ✅ |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | ✅ |
| PURCHASING_ITEM_ID | PurchasingItemId | ✅ |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | ✅ |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | ✅ |
| REQUEST_ID | ResponseLineRequestId | ✅ |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | ✅ |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | ✅ |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CODE | UomCode | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | ✅ |
| WORKSHEET_NAME | ResponseLineWorksheetName | ✅ |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | ✅ |

### [[negotiationresponselineextractpvo|NegotiationResponseLineExtractPVO]] (PO · BICC: 63/96)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | AdvanceAmount | — |
| ALTERNATE_DISP_LINE_NUMBER | AlternateDispLineNumber | ✅ |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| AWARD_DATE | AwardDate | ✅ |
| AWARD_PRICE | AwardPrice | ✅ |
| AWARD_QUANTITY | AwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | AwardShipmentNumber | ✅ |
| AWARD_STATUS | AwardStatus | ✅ |
| BATCH_ID | BatchId | — |
| BID_CURR_ADVANCE_AMOUNT | BidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | BidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | BidCurrencyLimitPrice | ✅ |
| BID_CURRENCY_PRICE | BidCurrencyPrice | ✅ |
| BID_CURRENCY_TRANS_PRICE | BidCurrencyTransPrice | ✅ |
| BID_CURRENCY_UNIT_PRICE | BidCurrencyUnitPrice | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| BID_START_PRICE | BidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | CancelledLimitPrice | ✅ |
| COPY_PRICE_FOR_PROXY_FLAG | CopyPriceForProxyFlag | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_PRICE_FACTORS_FLAG | DisplayPriceFactorsFlag | — |
| DOCUMENT_DISP_LINE_NUMBER | DocumentDispLineNumber | ✅ |
| FIRST_BID_PRICE | FirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | FixedAmountComponent | — |
| GROUP_AMOUNT | GroupAmount | ✅ |
| HAS_ATTRIBUTES_FLAG | HasAttributesFlag | — |
| HAS_BID_FLAG | HasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | HasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | HasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | HasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | HasShipmentsFlag | — |
| INTERFACE_LINE_ID | InterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | IsChangedLineFlag | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_NUMBER | LineNumber | ✅ |
| MAX_ALTERNATE_DISP_LINE_NUMBER | MaxAlternateDispLineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | MaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OLD_ALTERNATE_LINE_DESCRIPTION | OldAlternateLineDescription | ✅ |
| OLD_BID_CURR_ADVANCE_AMOUNT | OldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | OldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | OldBidCurrencyLimitPrice | ✅ |
| OLD_BID_CURRENCY_PRICE | OldBidCurrencyPrice | ✅ |
| OLD_BID_CURRENCY_UNIT_PRICE | OldBidCurrencyUnitPrice | ✅ |
| OLD_NO_OF_PAYMENTS | OldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | OldNoteToAuctionOwner | ✅ |
| OLD_PO_BID_MIN_REL_AMOUNT | OldPoBidMinRelAmount | ✅ |
| OLD_PRICE | OldPrice | ✅ |
| OLD_PROGRESS_PYMT_RATE_PERCENT | OldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | OldPromisedDate | ✅ |
| OLD_PROMISED_DELIVERY_DATE | OldPromisedDeliveryDate | ✅ |
| OLD_PROMISED_SHIP_DATE | OldPromisedShipDate | ✅ |
| OLD_PUBLISH_DATE | OldPublishDate | ✅ |
| OLD_QUANTITY | OldQuantity | ✅ |
| OLD_RECOUPMENT_RATE_PERCENT | OldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | OldRetainageRatePercent | — |
| OLD_UOM_CODE | OldUomCode | ✅ |
| PARENT_LINE_NUMBER | ParentLineNumber | ✅ |
| PER_UNIT_PRICE_COMPONENT | PerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | PoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | PoMinRelAmount | ✅ |
| PRICE | Price | ✅ |
| PRICE_BREAK_TYPE | PriceBreakType | ✅ |
| PRICE_DIFF_SHIPMENT_NUMBER | PriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | ProgramAppName | — |
| PROGRAM_NAME | ProgramName | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | ProgressPymtRatePercent | — |
| PROMISED_DATE | PromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | PromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | PromisedShipDate | ✅ |
| PROXY_BID_FLAG | ProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | PublishDate | ✅ |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | ✅ |
| PURCHASING_ITEM_ID | PurchasingItemId | ✅ |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | ✅ |
| QUANTITY | Quantity | ✅ |
| RANK | Rank | ✅ |
| RECOUPMENT_RATE_PERCENT | RecoupmentRatePercent | — |
| REQUEST_ID | RequestId | — |
| RETAINAGE_RATE_PERCENT | RetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | TotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | TriggerBidNumber | ✅ |
| UNIT_PRICE | UnitPrice | ✅ |
| UOM_CODE | UomCode | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | ✅ |
| WORKSHEET_NAME | WorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | WorksheetSequenceNumber | — |

### [[negotiationresponsepricetierpvo|NegotiationResponsePriceTierPVO]] (PO · BICC: 88/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | ✅ |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | ✅ |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| AWARD_DATE | ResponseLineAwardDate | ✅ |
| AWARD_PRICE | ResponseLineAwardPrice | ✅ |
| AWARD_QUANTITY | ResponseLineAwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | ✅ |
| AWARD_STATUS | ResponseLineAwardStatus | ✅ |
| BATCH_ID | ResponseLineBatchId | ✅ |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | ✅ |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | ✅ |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | ✅ |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | ✅ |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | ✅ |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | ✅ |
| BID_NUMBER | ResponseLineBidNumber | ✅ |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | ✅ |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | ✅ |
| CREATED_BY | ResponseLineCreatedBy | ✅ |
| CREATION_DATE | ResponseLineCreationDate | ✅ |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | ✅ |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | ✅ |
| GROUP_AMOUNT | ResponseLineGroupAmount | ✅ |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | ✅ |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | ✅ |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | ✅ |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | ✅ |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | ✅ |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | ✅ |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | ✅ |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | ✅ |
| LINE_NUMBER | ResponseLineLineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | ✅ |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | ✅ |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | ✅ |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | ✅ |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | ✅ |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | ✅ |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | ✅ |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | ✅ |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | ✅ |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | ✅ |
| OLD_PRICE | ResponseLineOldPrice | ✅ |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | ✅ |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | ✅ |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | ✅ |
| OLD_QUANTITY | ResponseLineOldQuantity | ✅ |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | ✅ |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | ✅ |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | ✅ |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | ✅ |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | ✅ |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | ✅ |
| PROGRAM_NAME | ResponseLineProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | ✅ |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | ✅ |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | ResponseLinePromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | ResponseLinePromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | ✅ |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | ✅ |
| PURCHASING_ITEM_ID | PurchasingItemId | ✅ |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | ✅ |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | ✅ |
| REQUEST_ID | ResponseLineRequestId | ✅ |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | ✅ |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | ✅ |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CODE | UomCode | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | ✅ |
| WORKSHEET_NAME | ResponseLineWorksheetName | ✅ |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | ✅ |

### [[negotiationresponsepurchaseorderlinepvo|NegotiationResponsePurchaseOrderLinePVO]] (PO · BICC: 20/85)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | — |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | — |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | — |
| AWARD_DATE | AwardDate | — |
| AWARD_DATE | ResponseLineAwardDate | — |
| AWARD_PRICE | ResponseLineAwardPrice | ✅ |
| AWARD_QUANTITY | ResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | ResponseLineAwardStatus | — |
| BATCH_ID | ResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | ✅ |
| BID_NUMBER | ResponseLineBidNumber | — |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | ResponseLineCreatedBy | — |
| CREATION_DATE | ResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | — |
| DOCUMENT_DISP_LINE_NUMBER | ResponseLineDocumentDispLineNumber | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | ResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | — |
| LINE_NUMBER | ResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | ResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | — |
| OLD_QUANTITY | ResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | — |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | — |
| PROGRAM_NAME | ResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | PromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | PromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | — |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | ResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | — |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | — |
| WORKSHEET_NAME | ResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | — |

### [[negotiationresponserequirementandattributepvo|NegotiationResponseRequirementAndAttributePVO]] (PO · BICC: 23/89)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | — |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | — |
| AUCTION_LINE_NUMBER | AuctionLineNumber | — |
| AWARD_DATE | ResponseLineAwardDate | — |
| AWARD_PRICE | ResponseLineAwardPrice | ✅ |
| AWARD_QUANTITY | ResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | ResponseLineAwardStatus | — |
| BATCH_ID | ResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | ResponseLineBidNumber | — |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | ResponseLineCreatedBy | — |
| CREATION_DATE | ResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | — |
| DOCUMENT_DISP_LINE_NUMBER | ResponseLineDocumentDispLineNumber | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | ResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | — |
| LINE_NUMBER | ResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | ResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | — |
| OLD_QUANTITY | ResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | ✅ |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | — |
| PROGRAM_NAME | ResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | ResponseLinePromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | ResponseLinePromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | — |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | ✅ |
| PURCHASING_ITEM_ID | PurchasingItemId | — |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | — |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | ResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | — |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CODE | UomCode | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | — |
| WORKSHEET_NAME | ResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | — |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 1/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[standardlinepvo|StandardLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | NegotiationResponseLineAdvanceAmount | — |
| AUCTION_HEADER_ID | NegotiationResponseLineAuctionHeaderId | — |
| AWARD_DATE | NegotiationResponseLineAwardDate | — |
| AWARD_PRICE | NegotiationResponseLineAwardPrice | — |
| AWARD_QUANTITY | NegotiationResponseLineAwardQuantity | — |
| AWARD_SHIPMENT_NUMBER | NegotiationResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | NegotiationResponseLineAwardStatus | — |
| BATCH_ID | NegotiationResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | NegotiationResponseLineBidCurrencyPrice | — |
| BID_CURRENCY_TRANS_PRICE | NegotiationResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | NegotiationResponseLineBidNumber | — |
| BID_START_PRICE | NegotiationResponseLineBidStartPrice | — |
| CANCELLED_LIMIT_PRICE | NegotiationResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | NegotiationResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | NegotiationResponseLineCreatedBy | — |
| CREATION_DATE | NegotiationResponseLineCreationDate | — |
| DISPLAY_PRICE_FACTORS_FLAG | NegotiationResponseLineDisplayPriceFactorsFlag | — |
| FIRST_BID_PRICE | NegotiationResponseLineFirstBidPrice | — |
| FIXED_AMOUNT_COMPONENT | NegotiationResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | NegotiationResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | NegotiationResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | NegotiationResponseLineHasBidFlag | — |
| HAS_BID_PAYMENTS_FLAG | NegotiationResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | NegotiationResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | NegotiationResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | NegotiationResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | NegotiationResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | NegotiationResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | NegotiationResponseLineLastUpdateDate | — |
| LAST_UPDATE_LOGIN | NegotiationResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationResponseLineLastUpdatedBy | — |
| LINE_NUMBER | NegotiationResponseLineLineNumber | — |
| MAX_RETAINAGE_AMOUNT | NegotiationResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | NegotiationResponseLineNoteToAuctionOwner | — |
| OBJECT_VERSION_NUMBER | NegotiationResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | NegotiationResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | NegotiationResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | NegotiationResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | NegotiationResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | NegotiationResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | NegotiationResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | NegotiationResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | NegotiationResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | NegotiationResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | NegotiationResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | NegotiationResponseLineOldPublishDate | — |
| OLD_QUANTITY | NegotiationResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | NegotiationResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | NegotiationResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | NegotiationResponseLinePerUnitPriceComponent | — |
| PO_BID_MIN_REL_AMOUNT | NegotiationResponseLinePoBidMinRelAmount | — |
| PO_MIN_REL_AMOUNT | NegotiationResponseLinePoMinRelAmount | — |
| PRICE | NegotiationResponseLinePrice | — |
| PRICE_BREAK_TYPE | NegotiationResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | NegotiationResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | NegotiationResponseLineProgramAppName | — |
| PROGRAM_NAME | NegotiationResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | NegotiationResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | NegotiationResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | NegotiationResponseLinePromisedDate | — |
| PROXY_BID_FLAG | NegotiationResponseLineProxyBidFlag | — |
| PROXY_BID_LIMIT_PRICE | NegotiationResponseLineProxyBidLimitPrice | — |
| PUBLISH_DATE | NegotiationResponseLinePublishDate | — |
| QUANTITY | NegotiationResponseLineQuantity | — |
| RANK | NegotiationResponseLineRank | — |
| RECOUPMENT_RATE_PERCENT | NegotiationResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | NegotiationResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | NegotiationResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | NegotiationResponseLineTotalWeightedScore | — |
| TRIGGER_BID_NUMBER | NegotiationResponseLineTriggerBidNumber | — |
| UNIT_PRICE | NegotiationResponseLineUnitPrice | — |
| WORKSHEET_NAME | NegotiationResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegotiationResponseLineWorksheetSequenceNumber | — |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO · BICC: 36/89)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADVANCE_AMOUNT | ResponseLineAdvanceAmount | — |
| ALTERNATE_LINE_DESCRIPTION | AlternateLineDescription | ✅ |
| ALTERNATE_LINE_FLAG | AlternateLineFlag | ✅ |
| AUCTION_HEADER_ID | ResponseLineAuctionHeaderId | ✅ |
| AUCTION_LINE_NUMBER | AuctionLineNumber | ✅ |
| AWARD_DATE | ResponseLineAwardDate | — |
| AWARD_PRICE | ResponseLineAwardPrice1 | — |
| AWARD_QUANTITY | ResponseLineAwardQuantity | ✅ |
| AWARD_SHIPMENT_NUMBER | ResponseLineAwardShipmentNumber | — |
| AWARD_STATUS | ResponseLineAwardStatus | ✅ |
| BATCH_ID | ResponseLineBatchId | — |
| BID_CURR_ADVANCE_AMOUNT | ResponseLineBidCurrAdvanceAmount | — |
| BID_CURR_MAX_RETAINAGE_AMT | ResponseLineBidCurrMaxRetainageAmt | — |
| BID_CURRENCY_LIMIT_PRICE | ResponseLineBidCurrencyLimitPrice | — |
| BID_CURRENCY_PRICE | ResponseLineBidCurrencyPrice | ✅ |
| BID_CURRENCY_TRANS_PRICE | ResponseLineBidCurrencyTransPrice | — |
| BID_CURRENCY_UNIT_PRICE | ResponseLineBidCurrencyUnitPrice | — |
| BID_NUMBER | BidNumber | ✅ |
| BID_START_PRICE | ResponseLineBidStartPrice | ✅ |
| CANCELLED_LIMIT_PRICE | ResponseLineCancelledLimitPrice | — |
| COPY_PRICE_FOR_PROXY_FLAG | ResponseLineCopyPriceForProxyFlag | — |
| CREATED_BY | ResponseLineCreatedBy | ✅ |
| CREATION_DATE | ResponseLineCreationDate | ✅ |
| DISPLAY_PRICE_FACTORS_FLAG | ResponseLineDisplayPriceFactorsFlag | — |
| DOCUMENT_DISP_LINE_NUMBER | ResponseLineDocumentDispLineNumber | ✅ |
| FIRST_BID_PRICE | ResponseLineFirstBidPrice | ✅ |
| FIXED_AMOUNT_COMPONENT | ResponseLineFixedAmountComponent | — |
| GROUP_AMOUNT | ResponseLineGroupAmount | — |
| HAS_ATTRIBUTES_FLAG | ResponseLineHasAttributesFlag | — |
| HAS_BID_FLAG | ResponseLineHasBidFlag | ✅ |
| HAS_BID_PAYMENTS_FLAG | ResponseLineHasBidPaymentsFlag | — |
| HAS_PRICE_DIFFERENTIALS_FLAG | ResponseLineHasPriceDifferentialsFlag | — |
| HAS_QUANTITY_TIERS | ResponseLineHasQuantityTiers | — |
| HAS_SHIPMENTS_FLAG | ResponseLineHasShipmentsFlag | — |
| INTERFACE_LINE_ID | ResponseLineInterfaceLineId | — |
| IS_CHANGED_LINE_FLAG | ResponseLineIsChangedLineFlag | — |
| LAST_UPDATE_DATE | ResponseLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseLineLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponseLineLastUpdatedBy | ✅ |
| LINE_NUMBER | LineNumber | ✅ |
| MAX_RETAINAGE_AMOUNT | ResponseLineMaxRetainageAmount | — |
| NOTE_TO_AUCTION_OWNER | ResponseLineNoteToAuctionOwner | ✅ |
| OBJECT_VERSION_NUMBER | ResponseLineObjectVersionNumber | — |
| OLD_BID_CURR_ADVANCE_AMOUNT | ResponseLineOldBidCurrAdvanceAmount | — |
| OLD_BID_CURR_MAX_RETAINAGE_AMT | ResponseLineOldBidCurrMaxRetainageAmt | — |
| OLD_BID_CURRENCY_LIMIT_PRICE | ResponseLineOldBidCurrencyLimitPrice | — |
| OLD_BID_CURRENCY_PRICE | ResponseLineOldBidCurrencyPrice | — |
| OLD_BID_CURRENCY_UNIT_PRICE | ResponseLineOldBidCurrencyUnitPrice | — |
| OLD_NO_OF_PAYMENTS | ResponseLineOldNoOfPayments | — |
| OLD_NOTE_TO_AUCTION_OWNER | ResponseLineOldNoteToAuctionOwner | — |
| OLD_PO_BID_MIN_REL_AMOUNT | ResponseLineOldPoBidMinRelAmount | — |
| OLD_PRICE | ResponseLineOldPrice | — |
| OLD_PROGRESS_PYMT_RATE_PERCENT | ResponseLineOldProgressPymtRatePercent | — |
| OLD_PROMISED_DATE | ResponseLineOldPromisedDate | — |
| OLD_PUBLISH_DATE | ResponseLineOldPublishDate | — |
| OLD_QUANTITY | ResponseLineOldQuantity | — |
| OLD_RECOUPMENT_RATE_PERCENT | ResponseLineOldRecoupmentRatePercent | — |
| OLD_RETAINAGE_RATE_PERCENT | ResponseLineOldRetainageRatePercent | — |
| PER_UNIT_PRICE_COMPONENT | ResponseLinePerUnitPriceComponent | ✅ |
| PO_BID_MIN_REL_AMOUNT | ResponseLinePoBidMinRelAmount | ✅ |
| PO_MIN_REL_AMOUNT | ResponseLinePoMinRelAmount | ✅ |
| PRICE | ResponseLinePrice | ✅ |
| PRICE_BREAK_TYPE | ResponseLinePriceBreakType | — |
| PRICE_DIFF_SHIPMENT_NUMBER | ResponseLinePriceDiffShipmentNumber | — |
| PROGRAM_APP_NAME | ResponseLineProgramAppName | — |
| PROGRAM_NAME | ResponseLineProgramName | — |
| PROGRAM_UPDATE_DATE | ResponseLineProgramUpdateDate | — |
| PROGRESS_PYMT_RATE_PERCENT | ResponseLineProgressPymtRatePercent | — |
| PROMISED_DATE | ResponseLinePromisedDate | ✅ |
| PROMISED_DELIVERY_DATE | ResponseLinePromisedDeliveryDate | ✅ |
| PROMISED_SHIP_DATE | ResponseLinePromisedShipDate | ✅ |
| PROXY_BID_FLAG | ResponseLineProxyBidFlag | ✅ |
| PROXY_BID_LIMIT_PRICE | ResponseLineProxyBidLimitPrice | ✅ |
| PUBLISH_DATE | ResponseLinePublishDate | — |
| PURCHASING_ITEM_DESC | PurchasingItemDesc | ✅ |
| PURCHASING_ITEM_ID | PurchasingItemId | ✅ |
| PURCHASING_ITEM_REVISION | PurchasingItemRevision | ✅ |
| QUANTITY | ResponseLineQuantity | ✅ |
| RANK | ResponseLineRank | ✅ |
| RECOUPMENT_RATE_PERCENT | ResponseLineRecoupmentRatePercent | — |
| REQUEST_ID | ResponseLineRequestId | — |
| RETAINAGE_RATE_PERCENT | ResponseLineRetainageRatePercent | — |
| TOTAL_WEIGHTED_SCORE | ResponseLineTotalWeightedScore | ✅ |
| TRIGGER_BID_NUMBER | ResponseLineTriggerBidNumber | — |
| UNIT_PRICE | ResponseLineUnitPrice | ✅ |
| UOM_CODE | UomCode1 | ✅ |
| UOM_CONVERSION_FACTOR | UomConversionFactor | ✅ |
| WORKSHEET_NAME | ResponseLineWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | ResponseLineWorksheetSequenceNumber | — |

---

## 📚 Referências

- [Oracle Docs — PON_BID_ITEM_PRICES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbiditemprices.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
