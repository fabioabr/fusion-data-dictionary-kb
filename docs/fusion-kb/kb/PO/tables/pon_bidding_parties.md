---
id: DOC-PO-010
doc_type: system-doc
title: "PON_BIDDING_PARTIES — Fornecedores Convidados para Negociações"
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
  - bidding-parties
  - fornecedores-convidados
aliases:
  - PON_BIDDING_PARTIES
  - pon_bidding_parties
  - fornecedores-convidados
  - sourcing-bidding-parties
  - invited-suppliers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BIDDING_PARTIES

## Visão Geral

Armazena os **fornecedores convidados** para participar de negociações no módulo Oracle Sourcing. Cada registro representa a inclusão de um fornecedor específico (trading partner) na lista de participantes de uma negociação, com informações de contato, site, status de participação e controle de acesso.

> [!note] Módulo Sourcing (PON)
> Esta tabela controla a lista de fornecedores elegíveis para cada negociação. Apenas fornecedores registrados nesta tabela podem submeter lances/respostas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de convidados:** Lista de fornecedores elegíveis para participar de cada negociação.
- **Controle de acesso:** Apenas fornecedores registrados podem visualizar e responder à negociação.
- **Comunicação:** Base para envio de convites, notificações e lembretes aos fornecedores.
- **Análise de participação:** Métricas de quantos fornecedores foram convidados vs. quantos responderam.
- **Compliance:** Evidência de que o processo de sourcing foi competitivo (múltiplos fornecedores convidados).
- **Histórico de engajamento:** Rastreamento de participação de fornecedores ao longo do tempo.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | PK/FK | Negociação associada | [[pon_auction_headers_all]] | 🟢 95% |
| 2 | TRADING_PARTNER_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do fornecedor (trading partner) | [[hz_parties]] | 🟢 95% |
| 3 | TRADING_PARTNER_NAME | VARCHAR2(240) | NULL | Identificação | Nome do fornecedor (desnormalizado) | — | 🟢 85% |
| 4 | TRADING_PARTNER_CONTACT_ID | NUMBER(18) | NULL | FK | Contato principal do fornecedor | [[hz_parties]] | 🟢 85% |
| 5 | TRADING_PARTNER_CONTACT_NAME | VARCHAR2(240) | NULL | Identificação | Nome do contato (desnormalizado) | — | 🟡 75% |
| 6 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor (endereço/filial) | [[poz_supplier_sites_all_m]] | 🟢 85% |
| 7 | VENDOR_SITE_CODE | VARCHAR2(60) | NULL | Identificação | Código do site do fornecedor (desnormalizado) | — | 🟡 75% |
| 8 | BID_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda de lance do fornecedor | [[fnd_currencies]] | 🟡 75% |
| 9 | INVITATION_DATE | DATE | NULL | Data | Data de envio do convite ao fornecedor | — | 🟢 85% |
| 10 | INVITATION_STATUS | VARCHAR2(30) | NULL | Status | Status do convite: SENT, VIEWED, ACCEPTED, REJECTED | — | 🟢 85% |
| 11 | BID_NUMBER | NUMBER | NULL | Referência cruzada | Número do lance/resposta submetido pelo fornecedor | — | 🟡 75% |
| 12 | ACCESS_TYPE | VARCHAR2(30) | NULL | Controle | Tipo de acesso: FULL, RESTRICTED | — | 🟡 70% |
| 13 | REGISTRATION_ID | NUMBER(18) | NULL | FK | ID de registro do fornecedor na negociação | — | 🟡 65% |
| 14 | SUPP_ACKNOWLEDGEMENT | VARCHAR2(30) | NULL | Status | Confirmação do fornecedor: ACK, NACK, null | — | 🟡 70% |
| 15 | SUPP_ACKNOWLEDGEMENT_DATE | DATE | NULL | Data | Data da confirmação do fornecedor | — | 🟡 70% |
| 16 | LAST_VIEWED_DATE | DATE | NULL | Data | Última vez que o fornecedor visualizou a negociação | — | 🟡 70% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 21 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o fornecedor convidado pertence)
- [[hz_parties]] — via `TRADING_PARTNER_ID` (fornecedor convidado para a negociação)
- [[hz_parties]] — via `TRADING_PARTNER_CONTACT_ID` (contato do fornecedor)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[fnd_currencies]] — via `BID_CURRENCY_CODE` (moeda em que o fornecedor apresentará o lance)

### Tabelas-filha (FK de saída)
- [[pon_acknowledgements]] — via `AUCTION_HEADER_ID` + `TRADING_PARTNER_ID` (confirmações de participação)
- Tabelas de bid/response (ex: `PON_BID_HEADERS`) — via `AUCTION_HEADER_ID` + `TRADING_PARTNER_ID` (lances submetidos)

---

## Uso Típico

### Fornecedores convidados para uma negociação
```sql
SELECT bp.TRADING_PARTNER_NAME,
       bp.TRADING_PARTNER_CONTACT_NAME,
       bp.VENDOR_SITE_CODE,
       bp.INVITATION_DATE,
       bp.INVITATION_STATUS,
       bp.SUPP_ACKNOWLEDGEMENT
FROM   PON_BIDDING_PARTIES bp
WHERE  bp.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY bp.TRADING_PARTNER_NAME;
```

### Taxa de participação em negociações
```sql
SELECT COUNT(*) AS total_convidados,
       COUNT(CASE WHEN bp.INVITATION_STATUS = 'ACCEPTED' THEN 1 END) AS aceitaram,
       COUNT(CASE WHEN bp.BID_NUMBER IS NOT NULL THEN 1 END) AS submeteram_lance
FROM   PON_BIDDING_PARTIES bp
WHERE  bp.AUCTION_HEADER_ID = :p_auction_header_id;
```

### Fornecedores que nunca visualizaram a negociação
```sql
SELECT bp.TRADING_PARTNER_NAME,
       bp.TRADING_PARTNER_CONTACT_NAME,
       bp.INVITATION_DATE
FROM   PON_BIDDING_PARTIES bp
WHERE  bp.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bp.LAST_VIEWED_DATE IS NULL
  AND  bp.INVITATION_STATUS = 'SENT';
```

### Filtros comuns
- `INVITATION_STATUS = 'ACCEPTED'` — Fornecedores que aceitaram o convite
- `BID_NUMBER IS NOT NULL` — Fornecedores que submeteram lance
- `SUPP_ACKNOWLEDGEMENT = 'ACK'` — Fornecedores que confirmaram participação
- `LAST_VIEWED_DATE IS NULL` — Fornecedores que não visualizaram a negociação

---

## Observações

- A chave primária é composta por `AUCTION_HEADER_ID` + `TRADING_PARTNER_ID` (um fornecedor por negociação).
- O campo `BID_NUMBER` é preenchido apenas quando o fornecedor efetivamente submete uma resposta/lance.
- Os campos desnormalizados (`TRADING_PARTNER_NAME`, `VENDOR_SITE_CODE`, etc.) são mantidos para performance em consultas e relatórios.
- O `VENDOR_SITE_ID` identifica a filial/endereço específico do fornecedor que participará da negociação.
- O campo `LAST_VIEWED_DATE` permite ao comprador identificar fornecedores que não estão engajados e enviar lembretes.
- Em negociações públicas (open bidding), fornecedores podem se auto-registrar, gerando registros nesta tabela automaticamente.
- A relação com `SUPP_ACKNOWLEDGEMENT` complementa os registros em [[pon_acknowledgements]] com informação resumida.

---

## Referências

- [Oracle Docs — PON_BIDDING_PARTIES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbiddingparties.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement

---

## 🔗 PVOs Relacionados

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | BiddingPartiesAccessType | — |
| ACK_NOTE_TO_AUCTIONEER | BiddingPartiesAckNoteToAuctioneer | — |
| ACK_PARTNER_CONTACT_ID | BiddingPartiesAckPartnerContactId | — |
| ACKNOWLEDGEMENT_TIME | BiddingPartiesAcknowledgementTime | — |
| ADDITIONAL_CONTACT_EMAIL | BiddingPartiesAdditionalContactEmail | — |
| AUCTION_HEADER_ID | BiddingPartiesAuctionHeaderId | — |
| BID_CURRENCY_CODE | BiddingPartiesBidCurrencyCode | — |
| CREATED_BY | BiddingPartiesCreatedBy | — |
| CREATION_DATE | BiddingPartiesCreationDate | — |
| LAST_AMENDMENT_UPDATE | BiddingPartiesLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | BiddingPartiesLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BiddingPartiesLastUpdateLogin | — |
| LAST_UPDATED_BY | BiddingPartiesLastUpdatedBy | — |
| LIST_ID | BiddingPartiesListId | — |
| MODIFIED_FLAG | BiddingPartiesModifiedFlag | — |
| NUMBER_PRICE_DECIMALS | BiddingPartiesNumberPriceDecimals | — |
| OBJECT_VERSION_NUMBER | BiddingPartiesObjectVersionNumber | — |
| RATE | BiddingPartiesRate | — |
| RATE_DSP | BiddingPartiesRateDsp | — |
| REGISTRATION_ID | BiddingPartiesRegistrationId | — |
| REQUESTED_SUPP_CONTACT_NAME | BiddingPartiesRequestedSuppContactName | — |
| REQUESTED_SUPPLIER_CONTACT_ID | BiddingPartiesRequestedSupplierContactId | — |
| REQUESTED_SUPPLIER_ID | BiddingPartiesRequestedSupplierId | — |
| REQUESTED_SUPPLIER_NAME | BiddingPartiesRequestedSupplierName | — |
| ROUND_NUMBER | BiddingPartiesRoundNumber | — |
| SEQUENCE | BiddingPartiesSequence | — |
| SUPP_ACKNOWLEDGEMENT | BiddingPartiesSuppAcknowledgement | — |
| SURROG_BID_ACK_FLAG | BiddingPartiesSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | BiddingPartiesSurrogBidAckPersonId | — |
| TRADING_PARTNER_CONTACT_ID | BiddingPartiesTradingPartnerContactId | — |
| TRADING_PARTNER_ID | BiddingPartiesTradingPartnerId | — |
| VENDOR_SITE_ID | BiddingPartiesVendorSiteId | — |
| WF_ITEM_KEY | BiddingPartiesWfItemKey | — |
| WF_USER_NAME | BiddingPartiesWfUserName | — |

### [[negdocumentsourcingsupplierinviteepvo|NegDocumentSourcingSupplierInviteePVO]] (PO · BICC: 18/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | NegBiddPartiesAccessType | — |
| ACK_NOTE_TO_AUCTIONEER | NegBiddPartiesAckNoteToAuctioneer | — |
| ACK_PARTNER_CONTACT_ID | NegBiddPartiesAckPartnerContactId | — |
| ACKNOWLEDGEMENT_TIME | NegBiddPartiesAcknowledgementTime | — |
| ADDITIONAL_CONTACT_EMAIL | NegBiddPartiesAdditionalContactEmail | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| BID_CURRENCY_CODE | NegBiddPartiesBidCurrencyCode | — |
| CREATED_BY | NegBiddPartiesCreatedBy | ✅ |
| CREATION_DATE | NegBiddPartiesCreationDate | ✅ |
| LAST_AMENDMENT_UPDATE | NegBiddPartiesLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegBiddPartiesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegBiddPartiesLastUpdateLogin | — |
| LAST_UPDATED_BY | NegBiddPartiesLastUpdatedBy | ✅ |
| LIST_ID | ListId | ✅ |
| MODIFIED_FLAG | NegBiddPartiesModifiedFlag | ✅ |
| NUMBER_PRICE_DECIMALS | NegBiddPartiesNumberPriceDecimals | — |
| OBJECT_VERSION_NUMBER | NegBiddPartiesObjectVersionNumber | — |
| RATE | NegBiddPartiesRate | — |
| RATE_DSP | NegBiddPartiesRateDsp | — |
| REGISTRATION_ID | NegBiddPartiesRegistrationId | ✅ |
| REQUESTED_SUPP_CONTACT_NAME | NegBiddPartiesRequestedSuppContactName | ✅ |
| REQUESTED_SUPPLIER_CONTACT_ID | NegBiddPartiesRequestedSupplierContactId | ✅ |
| REQUESTED_SUPPLIER_ID | NegBiddPartiesRequestedSupplierId | ✅ |
| REQUESTED_SUPPLIER_NAME | NegBiddPartiesRequestedSupplierName | ✅ |
| ROUND_NUMBER | NegBiddPartiesRoundNumber | — |
| SEQUENCE | Sequence | ✅ |
| SUPP_ACKNOWLEDGEMENT | NegBiddPartiesSuppAcknowledgement | ✅ |
| TRADING_PARTNER_CONTACT_ID | NegBiddPartiesTradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | NegBiddPartiesTradingPartnerId | ✅ |
| VENDOR_SITE_ID | NegBiddPartiesVendorSiteId | ✅ |
| WF_ITEM_KEY | NegBiddPartiesWfItemKey | — |
| WF_USER_NAME | NegBiddPartiesWfUserName | — |

### [[negotiationsupplierinviteeextractpvo|NegotiationSupplierInviteeExtractPVO]] (PO · BICC: 30/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | AccessType | ✅ |
| ACK_NOTE_TO_AUCTIONEER | AckNoteToAuctioneer | ✅ |
| ACK_PARTNER_CONTACT_ID | AckPartnerContactId | ✅ |
| ACKNOWLEDGEMENT_TIME | AcknowledgementTime | ✅ |
| ADDITIONAL_CONTACT_EMAIL | AdditionalContactEmail | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| BID_CURRENCY_CODE | BidCurrencyCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_AMENDMENT_UPDATE | LastAmendmentUpdate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LIST_ID | ListId | — |
| MODIFIED_FLAG | ModifiedFlag | — |
| NUMBER_PRICE_DECIMALS | NumberPriceDecimals | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATE | Rate | ✅ |
| RATE_DSP | RateDsp | ✅ |
| REGISTRATION_ID | RegistrationId | ✅ |
| REQUESTED_SUPP_CONTACT_NAME | RequestedSuppContactName | ✅ |
| REQUESTED_SUPPLIER_CONTACT_ID | RequestedSupplierContactId | ✅ |
| REQUESTED_SUPPLIER_ID | RequestedSupplierId | ✅ |
| REQUESTED_SUPPLIER_NAME | RequestedSupplierName | ✅ |
| ROUND_NUMBER | RoundNumber | ✅ |
| SEQUENCE | Sequence | ✅ |
| SUPP_ACKNOWLEDGEMENT | SuppAcknowledgement | ✅ |
| SURROG_BID_ACK_FLAG | SurrogBidAckFlag | ✅ |
| SURROG_BID_ACK_PERSON_ID | SurrogBidAckPersonId | ✅ |
| TRADING_PARTNER_CONTACT_ID | TradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | TradingPartnerId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |
| WF_ITEM_KEY | WfItemKey | — |
| WF_USER_NAME | WfUserName | — |

### [[negotiationsupplierinviteesextractpvo|NegotiationSupplierInviteesExtractPVO]] (PO · BICC: 35/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | AccessType | ✅ |
| ACK_NOTE_TO_AUCTIONEER | AckNoteToAuctioneer | ✅ |
| ACK_PARTNER_CONTACT_ID | AckPartnerContactId | ✅ |
| ACKNOWLEDGEMENT_TIME | AcknowledgementTime | ✅ |
| ADDITIONAL_CONTACT_EMAIL | AdditionalContactEmail | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| BID_CURRENCY_CODE | BidCurrencyCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_AMENDMENT_UPDATE | LastAmendmentUpdate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LIST_ID | ListId | ✅ |
| MODIFIED_FLAG | ModifiedFlag | ✅ |
| NOTIFY_CONTACTS_FLAG | NotifyContactsFlag | ✅ |
| NUMBER_PRICE_DECIMALS | NumberPriceDecimals | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATE | Rate | ✅ |
| RATE_DSP | RateDsp | ✅ |
| REGISTRATION_ID | RegistrationId | ✅ |
| REQUESTED_SUPP_CONTACT_NAME | RequestedSuppContactName | ✅ |
| REQUESTED_SUPPLIER_CONTACT_ID | RequestedSupplierContactId | ✅ |
| REQUESTED_SUPPLIER_ID | RequestedSupplierId | ✅ |
| REQUESTED_SUPPLIER_NAME | RequestedSupplierName | ✅ |
| ROUND_NUMBER | RoundNumber | ✅ |
| SEQUENCE | Sequence | ✅ |
| SUPP_ACKNOWLEDGEMENT | SuppAcknowledgement | ✅ |
| SURROG_BID_ACK_FLAG | SurrogBidAckFlag | ✅ |
| SURROG_BID_ACK_PERSON_ID | SurrogBidAckPersonId | ✅ |
| TRADING_PARTNER_CONTACT_ID | TradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | TradingPartnerId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |
| WF_ITEM_KEY | WfItemKey | ✅ |
| WF_USER_NAME | WfUserName | ✅ |

### [[unlockednegotiationresponseheaderpvo|UnlockedNegotiationResponseHeaderPVO]] (PO · BICC: 2/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | BiddingPartiesAccessType | — |
| ACK_NOTE_TO_AUCTIONEER | BiddingPartiesAckNoteToAuctioneer | — |
| ACK_PARTNER_CONTACT_ID | BiddingPartiesAckPartnerContactId | — |
| ACKNOWLEDGEMENT_TIME | BiddingPartiesAcknowledgementTime | ✅ |
| ADDITIONAL_CONTACT_EMAIL | BiddingPartiesAdditionalContactEmail | — |
| AUCTION_HEADER_ID | BiddingPartiesAuctionHeaderId | — |
| BID_CURRENCY_CODE | BiddingPartiesBidCurrencyCode | — |
| CREATED_BY | BiddingPartiesCreatedBy | — |
| CREATION_DATE | BiddingPartiesCreationDate | — |
| LAST_AMENDMENT_UPDATE | BiddingPartiesLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | BiddingPartiesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BiddingPartiesLastUpdateLogin | — |
| LAST_UPDATED_BY | BiddingPartiesLastUpdatedBy | — |
| LIST_ID | BiddingPartiesListId | — |
| MODIFIED_FLAG | BiddingPartiesModifiedFlag | — |
| NUMBER_PRICE_DECIMALS | BiddingPartiesNumberPriceDecimals | — |
| OBJECT_VERSION_NUMBER | BiddingPartiesObjectVersionNumber | — |
| RATE | BiddingPartiesRate | — |
| RATE_DSP | BiddingPartiesRateDsp | — |
| REGISTRATION_ID | BiddingPartiesRegistrationId | — |
| REQUESTED_SUPP_CONTACT_NAME | BiddingPartiesRequestedSuppContactName | — |
| REQUESTED_SUPPLIER_CONTACT_ID | BiddingPartiesRequestedSupplierContactId | — |
| REQUESTED_SUPPLIER_ID | BiddingPartiesRequestedSupplierId | — |
| REQUESTED_SUPPLIER_NAME | BiddingPartiesRequestedSupplierName | — |
| ROUND_NUMBER | BiddingPartiesRoundNumber | — |
| SEQUENCE | BiddingPartiesSequence | — |
| SUPP_ACKNOWLEDGEMENT | BiddingPartiesSuppAcknowledgement | — |
| SURROG_BID_ACK_FLAG | BiddingPartiesSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | BiddingPartiesSurrogBidAckPersonId | — |
| TRADING_PARTNER_CONTACT_ID | BiddingPartiesTradingPartnerContactId | — |
| TRADING_PARTNER_ID | BiddingPartiesTradingPartnerId | — |
| VENDOR_SITE_ID | BiddingPartiesVendorSiteId | — |
| WF_ITEM_KEY | BiddingPartiesWfItemKey | — |
| WF_USER_NAME | BiddingPartiesWfUserName | — |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO · BICC: 2/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TYPE | BiddingPartiesAccessType | — |
| ACK_NOTE_TO_AUCTIONEER | BiddingPartiesAckNoteToAuctioneer | — |
| ACK_PARTNER_CONTACT_ID | BiddingPartiesAckPartnerContactId | — |
| ACKNOWLEDGEMENT_TIME | BiddingPartiesAcknowledgementTime | ✅ |
| ADDITIONAL_CONTACT_EMAIL | BiddingPartiesAdditionalContactEmail | — |
| AUCTION_HEADER_ID | BiddingPartiesAuctionHeaderId | — |
| BID_CURRENCY_CODE | BiddingPartiesBidCurrencyCode | — |
| CREATED_BY | BiddingPartiesCreatedBy | — |
| CREATION_DATE | BiddingPartiesCreationDate | — |
| LAST_AMENDMENT_UPDATE | BiddingPartiesLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | BiddingPartiesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BiddingPartiesLastUpdateLogin | — |
| LAST_UPDATED_BY | BiddingPartiesLastUpdatedBy | — |
| LIST_ID | BiddingPartiesListId | — |
| MODIFIED_FLAG | BiddingPartiesModifiedFlag | — |
| NUMBER_PRICE_DECIMALS | BiddingPartiesNumberPriceDecimals | — |
| OBJECT_VERSION_NUMBER | BiddingPartiesObjectVersionNumber | — |
| RATE | BiddingPartiesRate | — |
| RATE_DSP | BiddingPartiesRateDsp | — |
| REGISTRATION_ID | BiddingPartiesRegistrationId | — |
| REQUESTED_SUPP_CONTACT_NAME | BiddingPartiesRequestedSuppContactName | — |
| REQUESTED_SUPPLIER_CONTACT_ID | BiddingPartiesRequestedSupplierContactId | — |
| REQUESTED_SUPPLIER_ID | BiddingPartiesRequestedSupplierId | — |
| REQUESTED_SUPPLIER_NAME | BiddingPartiesRequestedSupplierName | — |
| ROUND_NUMBER | BiddingPartiesRoundNumber | — |
| SEQUENCE | BiddingPartiesSequence | — |
| SUPP_ACKNOWLEDGEMENT | BiddingPartiesSuppAcknowledgement | — |
| SURROG_BID_ACK_FLAG | BiddingPartiesSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | BiddingPartiesSurrogBidAckPersonId | — |
| TRADING_PARTNER_CONTACT_ID | BiddingPartiesTradingPartnerContactId | — |
| TRADING_PARTNER_ID | BiddingPartiesTradingPartnerId | — |
| VENDOR_SITE_ID | BiddingPartiesVendorSiteId | — |
| WF_ITEM_KEY | BiddingPartiesWfItemKey | — |
| WF_USER_NAME | BiddingPartiesWfUserName | — |
