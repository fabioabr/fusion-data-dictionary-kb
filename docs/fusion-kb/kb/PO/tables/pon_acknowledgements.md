---
id: DOC-PO-001
doc_type: system-doc
title: "PON_ACKNOWLEDGEMENTS — Confirmações de Participação em Negociações"
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
  - acknowledgements
  - negociacoes
aliases:
  - PON_ACKNOWLEDGEMENTS
  - pon_acknowledgements
  - confirmacoes-negociacao
  - sourcing-acknowledgements
  - ack-negociacoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_ACKNOWLEDGEMENTS

## Visao Geral

Armazena as **confirmações de participação** (acknowledgements) dos fornecedores convidados para negociações no módulo Oracle Sourcing. Cada registro representa a resposta de um fornecedor a um convite de participação em uma negociação (RFQ, RFI, Auction, etc.), indicando se aceita, rejeita ou ainda não respondeu.

> [!note] Módulo Sourcing (PON)
> O prefixo `PON` identifica tabelas do módulo **Procurement Sourcing** (Oracle Negotiation). Essas tabelas suportam o ciclo completo de negociações eletrônicas entre compradores e fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de convites:** Rastreamento de quais fornecedores confirmaram participação em negociações.
- **Compliance de processo:** Garantia de que fornecedores reconheceram termos e condições antes de submeter lances.
- **Auditoria de negociações:** Registro histórico de confirmações com data/hora e IP de origem.
- **Análise de engajamento:** Métricas de taxa de resposta dos fornecedores convidados.
- **Workflow de sourcing:** Controle de pré-requisitos antes da abertura do período de lances.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACKNOWLEDGEMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da confirmação | — | 🟢 95% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Negociação associada | [[pon_auction_headers_all]] | 🟢 95% |
| 3 | TRADING_PARTNER_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor (trading partner) | [[hz_parties]] | 🟢 90% |
| 4 | TRADING_PARTNER_CONTACT_ID | NUMBER(18) | NULL | FK | Contato do fornecedor que realizou a confirmação | [[hz_parties]] | 🟡 75% |
| 5 | ACKNOWLEDGEMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de confirmação: ACCEPT, REJECT, NO_RESPONSE | — | 🟢 85% |
| 6 | ACKNOWLEDGEMENT_DATE | DATE | NULL | Data | Data/hora em que o fornecedor confirmou participação | — | 🟢 90% |
| 7 | ACKNOWLEDGE_FLAG | VARCHAR2(1) | NULL | Flag | Indicador se o fornecedor já confirmou (Y/N) | — | 🟡 75% |
| 8 | COMMENT | VARCHAR2(2000) | NULL | Texto livre | Comentário do fornecedor na confirmação | — | 🟡 70% |
| 9 | IP_ADDRESS | VARCHAR2(50) | NULL | Auditoria | Endereço IP do fornecedor no momento da confirmação | — | 🟡 65% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o aceite se refere)
- [[hz_parties]] — via `TRADING_PARTNER_ID` (fornecedor que confirmou participação na negociação)
- [[hz_parties]] — via `TRADING_PARTNER_CONTACT_ID` (contato do fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida — tabela terminal de registro de confirmações.

---

## Uso Típico

### Confirmações por negociação
```sql
SELECT ack.TRADING_PARTNER_ID,
       ack.ACKNOWLEDGEMENT_TYPE,
       ack.ACKNOWLEDGEMENT_DATE,
       ack.COMMENT
FROM   PON_ACKNOWLEDGEMENTS ack
WHERE  ack.AUCTION_HEADER_ID = :p_auction_header_id
  AND  ack.ACKNOWLEDGE_FLAG = 'Y';
```

### Taxa de resposta de fornecedores
```sql
SELECT COUNT(CASE WHEN ACKNOWLEDGE_FLAG = 'Y' THEN 1 END) AS confirmados,
       COUNT(*) AS total_convidados,
       ROUND(COUNT(CASE WHEN ACKNOWLEDGE_FLAG = 'Y' THEN 1 END) * 100.0 / COUNT(*), 2) AS taxa_resposta_pct
FROM   PON_ACKNOWLEDGEMENTS
WHERE  AUCTION_HEADER_ID = :p_auction_header_id;
```

### Filtros comuns
- `ACKNOWLEDGE_FLAG = 'Y'` — Fornecedores que confirmaram
- `ACKNOWLEDGEMENT_TYPE = 'ACCEPT'` — Aceitaram participar
- `ACKNOWLEDGEMENT_TYPE = 'REJECT'` — Recusaram participar

---

## Observações

- A tabela registra exclusivamente confirmações no contexto de negociações (Sourcing), não se aplica a ordens de compra.
- O campo `ACKNOWLEDGEMENT_TYPE` distingue entre aceitação e rejeição de convites; fornecedores que não responderam podem não ter registro ou ter `NO_RESPONSE`.
- O `IP_ADDRESS` pode ser utilizado para auditoria de segurança, mas não é garantido em todos os releases.
- A relação com `TRADING_PARTNER_ID` mapeia para o cadastro de fornecedores via TCA (Trading Community Architecture — tabela `HZ_PARTIES`).

---

## Referências

- [Oracle Docs — PON_ACKNOWLEDGEMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponacknowledgements.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement

---

## 🔗 PVOs Relacionados

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACKNOWLEDGEMENT_DATE | AcknowledgeAcknowledgementDate | — |
| ACKNOWLEDGEMENT_RESPONSE | AcknowledgeAcknowledgementResponse | — |
| AUCTION_HEADER_ID | AcknowledgeAuctionHeaderId | — |
| CREATED_BY | AcknowledgeCreatedBy | — |
| CREATION_DATE | AcknowledgeCreationDate | — |
| LAST_UPDATE_DATE | AcknowledgeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcknowledgeLastUpdateLogin | — |
| LAST_UPDATED_BY | AcknowledgeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AcknowledgeObjectVersionNumber | — |
| SURROG_BID_ACK_ENTRY_DATE | AcknowledgeSurrogBidAckEntryDate | — |
| SURROG_BID_ACK_FLAG | AcknowledgeSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | AcknowledgeSurrogBidAckPersonId | — |
| SURROG_METHOD_OF_ACK | AcknowledgeSurrogMethodOfAck | — |
| TRADING_PARTNER_CONTACT_ID | AcknowledgeTradingPartnerContactId | — |
| TRADING_PARTNER_ID | AcknowledgeTradingPartnerId | — |

### [[negotiationsupplieracknowledgementpvo|NegotiationSupplierAcknowledgementPVO]] (PO · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACKNOWLEDGEMENT_DATE | NegSuppAckAcknowledgementDate | ✅ |
| ACKNOWLEDGEMENT_RESPONSE | NegSuppAckAcknowledgementResponse | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| CREATED_BY | NegSuppAckCreatedBy | ✅ |
| CREATION_DATE | NegSuppAckCreationDate | ✅ |
| LAST_UPDATE_DATE | NegSuppAckLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegSuppAckLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | NegSuppAckLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | NegSuppAckObjectVersionNumber | ✅ |
| SURROG_BID_ACK_FLAG | NegSuppAckSurrogBidAckFlag | ✅ |
| SURROG_BID_ACK_PERSON_ID | NegSuppAckSurrogBidAckPersonId | ✅ |
| TRADING_PARTNER_CONTACT_ID | TradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | NegSuppAckTradingPartnerId | ✅ |

### [[unlockednegotiationresponseheaderpvo|UnlockedNegotiationResponseHeaderPVO]] (PO · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACKNOWLEDGEMENT_DATE | AcknowledgeAcknowledgementDate | — |
| ACKNOWLEDGEMENT_RESPONSE | AcknowledgeAcknowledgementResponse | — |
| AUCTION_HEADER_ID | AcknowledgeAuctionHeaderId | — |
| CREATED_BY | AcknowledgeCreatedBy | — |
| CREATION_DATE | AcknowledgeCreationDate | — |
| LAST_UPDATE_DATE | AcknowledgeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcknowledgeLastUpdateLogin | — |
| LAST_UPDATED_BY | AcknowledgeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AcknowledgeObjectVersionNumber | — |
| SURROG_BID_ACK_ENTRY_DATE | AcknowledgeSurrogBidAckEntryDate | ✅ |
| SURROG_BID_ACK_FLAG | AcknowledgeSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | AcknowledgeSurrogBidAckPersonId | — |
| SURROG_METHOD_OF_ACK | AcknowledgeSurrogMethodOfAck | ✅ |
| TRADING_PARTNER_CONTACT_ID | AcknowledgeTradingPartnerContactId | — |
| TRADING_PARTNER_ID | AcknowledgeTradingPartnerId | — |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACKNOWLEDGEMENT_DATE | AcknowledgeAcknowledgementDate | — |
| ACKNOWLEDGEMENT_RESPONSE | AcknowledgeAcknowledgementResponse | — |
| AUCTION_HEADER_ID | AcknowledgeAuctionHeaderId | — |
| CREATED_BY | AcknowledgeCreatedBy | — |
| CREATION_DATE | AcknowledgeCreationDate | — |
| LAST_UPDATE_DATE | AcknowledgeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AcknowledgeLastUpdateLogin | — |
| LAST_UPDATED_BY | AcknowledgeLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AcknowledgeObjectVersionNumber | — |
| SURROG_BID_ACK_ENTRY_DATE | AcknowledgeSurrogBidAckEntryDate | ✅ |
| SURROG_BID_ACK_FLAG | AcknowledgeSurrogBidAckFlag | — |
| SURROG_BID_ACK_PERSON_ID | AcknowledgeSurrogBidAckPersonId | — |
| SURROG_METHOD_OF_ACK | AcknowledgeSurrogMethodOfAck | ✅ |
| TRADING_PARTNER_CONTACT_ID | AcknowledgeTradingPartnerContactId | — |
| TRADING_PARTNER_ID | AcknowledgeTradingPartnerId | — |
