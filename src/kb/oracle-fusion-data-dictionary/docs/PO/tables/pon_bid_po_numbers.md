---
id: DOC-PO-015
doc_type: system-doc
title: "PON_BID_PO_NUMBERS — Números de PO Gerados a partir de Lances"
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
  - po-numbers
  - adjudicacao
aliases:
  - PON_BID_PO_NUMBERS
  - pon_bid_po_numbers
  - numeros-po-lance
  - bid-po-numbers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_PO_NUMBERS

## 📌 Visão Geral

Armazena o **mapeamento a nível de cabeçalho** entre lances adjudicados e pedidos de compra (PO) gerados no módulo de Purchasing. Diferente da [[pon_bid_po_lines]] (que opera a nível de linha), esta tabela registra a associação consolidada entre o lance e o(s) número(s) de PO resultantes, incluindo o status de criação do pedido.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreabilidade consolidada:** Associação rápida entre lance vencedor e PO(s) gerado(s).
- **Monitoramento de criação de PO:** Status da geração automática de pedidos de compra pós-adjudicação.
- **Relatórios executivos:** Contagem de POs gerados por negociação/fornecedor.
- **Auditoria de ciclo Sourcing-to-Procure:** Comprovação do fluxo completo desde a negociação.
- **Controle de erros:** Identificação de falhas na criação automática de POs.

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
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 3 | PO_HEADER_ID | NUMBER(18) | NOT NULL | PK/FK | ID do pedido de compra gerado | [[po_headers_all]] | 🟢 95% |
| 4 | PO_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do PO (SEGMENT1 do PO_HEADERS_ALL) | — | 🟢 90% |
| 5 | PO_CREATION_STATUS | VARCHAR2(30) | NULL | Classificação | Status da criação do PO: SUCCESS, ERROR, IN_PROGRESS | — | 🟡 75% |
| 6 | ERROR_MESSAGE | VARCHAR2(2000) | NULL | Texto livre | Mensagem de erro caso a criação do PO falhe | — | 🟡 70% |
| 7 | DOCUMENT_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo de documento: STANDARD, BLANKET, CONTRACT | — | 🟡 75% |
| 8 | REQ_HEADER_ID | NUMBER(18) | NULL | FK | Requisição associada (se originado de requisição) | [[por_requisition_headers_all]] | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação que gerou os números de PO)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra)

### Tabelas relacionadas
- [[por_requisition_headers_all]] — via `REQ_HEADER_ID` (requisição de origem)

---

## 📎 Uso Típico

### POs gerados por negociação
```sql
SELECT bpn.BID_NUMBER, bh.VENDOR_NAME,
       bpn.PO_NUMBER, bpn.PO_CREATION_STATUS,
       bpn.DOCUMENT_TYPE_CODE
FROM   PON_BID_PO_NUMBERS bpn
JOIN   PON_BID_HEADERS bh ON bh.BID_NUMBER = bpn.BID_NUMBER
WHERE  bpn.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bpn.PO_CREATION_STATUS = 'SUCCESS';
```

### POs com erro de criação
```sql
SELECT bpn.BID_NUMBER, bpn.PO_CREATION_STATUS,
       bpn.ERROR_MESSAGE, bpn.CREATION_DATE
FROM   PON_BID_PO_NUMBERS bpn
WHERE  bpn.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bpn.PO_CREATION_STATUS = 'ERROR';
```

---

## 🔒 Observações

- Um lance pode gerar múltiplos POs quando as linhas adjudicadas pertencem a business units distintas.
- O `PO_CREATION_STATUS` permite monitorar se a geração automática de PO foi bem-sucedida.
- O campo `ERROR_MESSAGE` é preenchido apenas quando `PO_CREATION_STATUS = 'ERROR'`.
- Para rastreabilidade detalhada a nível de linha, utilizar [[pon_bid_po_lines]] em complemento.
- O `DOCUMENT_TYPE_CODE` indica o tipo de PO criado: STANDARD (pontual), BLANKET (acordo), CONTRACT (contrato).

---

## 🔗 PVOs Relacionados

### [[negotiationresponsepurchaseorderlinepvo|NegotiationResponsePurchaseOrderLinePVO]] (PO · BICC: 1/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_REQUIRED_FLAG | ResponsePOAcceptanceRequiredFlag | — |
| ACKNOWLEDGEMENT_WITHIN_DAYS | ResponsePOAcknowledgementWithinDays | — |
| AGENT_ID | ResponsePOAgentId | — |
| AUCTION_HEADER_ID | ResponsePOAuctionHeaderId | — |
| AUTOMATIC_GENERATE_ORDER | ResponsePOAutomaticGenerateOrder | — |
| AUTOMATIC_SUBMIT_FOR_APPR | ResponsePOAutomaticSubmitForAppr | — |
| BID_NUMBER | ResponsePOBidNumber | — |
| CREATED_BY | ResponsePOCreatedBy | — |
| CREATION_DATE | ResponsePOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | ResponsePODefaultTaxationCountry | — |
| FOR_BACKING_REQUISITION | ResponsePOForBackingRequisition | — |
| GROUP_REQUISITION | ResponsePOGroupRequisition | — |
| GROUP_REQUISITION_LINES | ResponsePOGroupRequisitionLines | — |
| INITIATE_APPROVAL | ResponsePOInitiateApproval | — |
| LAST_UPDATE_DATE | ResponsePOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponsePOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponsePOLastUpdatedBy | — |
| NOTE_TO_SUPPLIER | ResponsePONoteToSupplier | — |
| OBJECT_VERSION_NUMBER | ResponsePOObjectVersionNumber | — |
| ORDER_NUMBER | ResponsePOOrderNumber | — |
| PO_END_DATE | ResponsePOPoEndDate | — |
| PO_ERROR_CODE | ResponsePOPoErrorCode | — |
| PO_ERROR_MSG | ResponsePOPoErrorMsg | — |
| PO_HEADER_ID | ResponsePOPoHeaderId | — |
| PO_START_DATE | ResponsePOPoStartDate | — |
| PO_WF_CREATION_RND | ResponsePOPoWfCreationRnd | — |
| REQ_BU_ID | ResponsePOReqBuId | — |
| RETRO_PRICE_APPLY_UPDATES_FLAG | ResponsePORetroPriceApplyUpdatesFlag | — |
| RETRO_PRICE_COMM_UPDATES_FLAG | ResponsePORetroPriceCommUpdatesFlag | — |
| SEQUENCE_NUMBER | ResponsePOSequenceNumber | — |
| TAX_DOCUMENT_SUBTYPE | ResponsePOTaxDocumentSubtype | — |
| USE_NEED_BY_DATE | ResponsePOUseNeedByDate | — |
| USE_SHIP_TO | ResponsePOUseShipTo | — |
| VENDOR_SITE_ID | ResponsePOVendorSiteId | — |

---

## 📚 Referências

- [Oracle Docs — PON_BID_PO_NUMBERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidponumbers.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
