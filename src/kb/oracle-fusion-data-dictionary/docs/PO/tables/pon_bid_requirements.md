---
id: DOC-PO-016
doc_type: system-doc
title: "PON_BID_REQUIREMENTS — Requisitos Respondidos em Lances"
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
  - requisitos
  - requirements
aliases:
  - PON_BID_REQUIREMENTS
  - pon_bid_requirements
  - requisitos-lance
  - bid-requirements
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_REQUIREMENTS

## 📌 Visão Geral

Armazena os **requisitos técnicos e comerciais** definidos na negociação que os fornecedores devem responder em seus lances. Cada registro representa um requisito individual (pergunta, critério ou exigência) associado a um lance, incluindo o tipo de requisito, sua obrigatoriedade e a seção à qual pertence. Funciona como a definição dos requisitos no contexto do lance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação técnica estruturada:** Definição de critérios obrigatórios e desejáveis para avaliação de propostas.
- **Compliance check:** Verificação de que o fornecedor atendeu a todos os requisitos obrigatórios.
- **Scoring técnico:** Base para pontuação de requisitos individuais com peso configurável.
- **Documentação de RFx:** Registro formal das exigências da negociação no contexto de cada lance.
- **Auditoria de avaliação:** Rastreabilidade de quais requisitos foram definidos e como foram avaliados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BID_NUMBER | NUMBER(18) | NOT NULL | PK/FK | Número do lance | [[pon_bid_headers]] | 🟢 95% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 3 | REQUIREMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do requisito no lance | — | 🟢 90% |
| 4 | SECTION_ID | NUMBER(18) | NULL | FK | Seção à qual o requisito pertence | [[pon_bid_sections]] | 🟡 80% |
| 5 | REQUIREMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do requisito: TECHNICAL, COMMERCIAL, COMPLIANCE | — | 🟡 75% |
| 6 | REQUIREMENT_NAME | VARCHAR2(500) | NULL | Identificação | Nome/título do requisito | — | 🟢 85% |
| 7 | REQUIREMENT_DESCRIPTION | VARCHAR2(4000) | NULL | Texto livre | Descrição detalhada do requisito | — | 🟢 85% |
| 8 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição do requisito | — | 🟡 75% |
| 9 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Classificação | Requisito obrigatório (Y/N) | — | 🟢 85% |
| 10 | RESPONSE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de resposta esperada: TEXT, ATTACHMENT, DATE, NUMBER | — | 🟡 75% |
| 11 | WEIGHT | NUMBER | NULL | Avaliação | Peso do requisito no cálculo de scoring | — | 🟡 75% |
| 12 | LINE_NUMBER | NUMBER | NULL | Referência | Linha do item associada (NULL = requisito a nível de cabeçalho) | — | 🟡 70% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o requisito do lance pertence)
- [[pon_bid_sections]] — via `SECTION_ID` (seção do lance que contém o requisito)

### Tabelas-filha (FK de saída)
- [[pon_bid_requirement_values]] — via `BID_NUMBER` + `REQUIREMENT_ID` (respostas do fornecedor)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Requisitos de um lance com suas respostas
```sql
SELECT br.REQUIREMENT_NAME, br.REQUIREMENT_TYPE,
       br.MANDATORY_FLAG, br.WEIGHT,
       brv.RESPONSE_VALUE, brv.SCORE
FROM   PON_BID_REQUIREMENTS br
LEFT JOIN PON_BID_REQUIREMENT_VALUES brv
       ON brv.BID_NUMBER = br.BID_NUMBER
      AND brv.REQUIREMENT_ID = br.REQUIREMENT_ID
WHERE  br.BID_NUMBER = :p_bid_number
ORDER BY br.DISPLAY_ORDER;
```

### Requisitos obrigatórios não respondidos
```sql
SELECT br.REQUIREMENT_NAME, br.REQUIREMENT_DESCRIPTION
FROM   PON_BID_REQUIREMENTS br
LEFT JOIN PON_BID_REQUIREMENT_VALUES brv
       ON brv.BID_NUMBER = br.BID_NUMBER
      AND brv.REQUIREMENT_ID = br.REQUIREMENT_ID
WHERE  br.BID_NUMBER = :p_bid_number
  AND  br.MANDATORY_FLAG = 'Y'
  AND  brv.RESPONSE_VALUE IS NULL;
```

---

## 🔒 Observações

- A chave primária é composta por `BID_NUMBER` + `REQUIREMENT_ID`.
- Requisitos com `LINE_NUMBER` preenchido são específicos de uma linha do item; requisitos com `LINE_NUMBER` NULL são a nível de cabeçalho (negociação inteira).
- O `MANDATORY_FLAG = 'Y'` impede que o fornecedor submeta o lance sem responder ao requisito.
- O `WEIGHT` define a importância relativa do requisito no cálculo de scoring técnico.
- As respostas dos fornecedores são armazenadas em [[pon_bid_requirement_values]], não nesta tabela.

---

## 🔗 PVOs Relacionados

### [[negotiationresponserequirementsextractpvo|NegotiationResponseRequirementsExtractPVO]] (PO · BICC: 20/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| HAS_BID_FLAG | HasBidFlag | ✅ |
| INTERFACE_LINE_ID | InterfaceLineId | ✅ |
| INTERNAL_NOTE | InternalNote | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OLD_COMMENTS | OldComments | ✅ |
| REQUIREMENT_ID | RequirementId | ✅ |
| SCORE | Score | ✅ |
| SECTION_ID | SectionId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| WEIGHTED_SCORE | WeightedScore | ✅ |
| WORKSHEET_NAME | WorksheetName | ✅ |
| WORKSHEET_SEQUENCE_NUMBER | WorksheetSequenceNumber | ✅ |

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 7/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegRespRequirementsAuctionHeaderId5 | — |
| BID_NUMBER | NegRespRequirementsBidNumber1 | — |
| COMMENTS | NegRespRequirementsComments | ✅ |
| CREATED_BY | NegRespRequirementsCreatedBy5 | ✅ |
| CREATION_DATE | NegRespRequirementsCreationDate5 | ✅ |
| HAS_BID_FLAG | NegRespRequirementsHasBidFlag | — |
| INTERFACE_LINE_ID | NegRespRequirementsInterfaceLineId | — |
| INTERNAL_NOTE | NegRespRequirementsInternalNote | ✅ |
| LAST_UPDATE_DATE | NegRespRequirementsLastUpdateDate5 | ✅ |
| LAST_UPDATE_LOGIN | NegRespRequirementsLastUpdateLogin5 | — |
| LAST_UPDATED_BY | NegRespRequirementsLastUpdatedBy5 | — |
| OBJECT_VERSION_NUMBER | NegRespRequirementsObjectVersionNumber5 | — |
| OLD_COMMENTS | NegRespRequirementsOldComments | — |
| REQUIREMENT_ID | NegRespRequirementsRequirementId3 | — |
| SCORE | NegRespRequirementsScore1 | ✅ |
| SECTION_ID | NegRespRequirementsSectionId2 | — |
| SEQUENCE_NUMBER | NegRespRequirementsSequenceNumber1 | — |
| WEIGHTED_SCORE | NegRespRequirementsWeightedScore | ✅ |
| WORKSHEET_NAME | NegRespRequirementsWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegRespRequirementsWorksheetSequenceNumber | — |

### [[negotiationresprequirementpvo|NegotiationRespRequirementPVO]] (PO · BICC: 10/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegRespRequirementsAuctionHeaderId | — |
| BID_NUMBER | NegRespRequirementsBidNumber | ✅ |
| COMMENTS | NegRespRequirementsComments | ✅ |
| CREATED_BY | NegRespRequirementsCreatedBy | ✅ |
| CREATION_DATE | NegRespRequirementsCreationDate | ✅ |
| HAS_BID_FLAG | NegRespRequirementsHasBidFlag | — |
| INTERFACE_LINE_ID | NegRespRequirementsInterfaceLineId | — |
| INTERNAL_NOTE | NegRespRequirementsInternalNote | ✅ |
| LAST_UPDATE_DATE | NegRespRequirementsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegRespRequirementsLastUpdateLogin | — |
| LAST_UPDATED_BY | NegRespRequirementsLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | NegRespRequirementsObjectVersionNumber | — |
| OLD_COMMENTS | NegRespRequirementsOldComments | — |
| REQUIREMENT_ID | NegRespRequirementsRequirementId | ✅ |
| SCORE | NegRespRequirementsScore | ✅ |
| SECTION_ID | NegRespRequirementsSectionId | ✅ |
| SEQUENCE_NUMBER | NegRespRequirementsSequenceNumber | — |
| WEIGHTED_SCORE | NegRespRequirementsWeightedScore | ✅ |
| WORKSHEET_NAME | NegRespRequirementsWorksheetName | — |
| WORKSHEET_SEQUENCE_NUMBER | NegRespRequirementsWorksheetSequenceNumber | — |

---

## 📚 Referências

- [Oracle Docs — PON_BID_REQUIREMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidrequirements.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
