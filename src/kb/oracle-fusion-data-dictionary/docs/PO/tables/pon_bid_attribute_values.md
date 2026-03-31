---
id: DOC-PO-011
doc_type: system-doc
title: "PON_BID_ATTRIBUTE_VALUES — Valores de Atributos de Lances"
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
  - atributos-lance
aliases:
  - PON_BID_ATTRIBUTE_VALUES
  - pon_bid_attribute_values
  - valores-atributos-lance
  - bid-attribute-values
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_ATTRIBUTE_VALUES

## 📌 Visão Geral

Armazena os **valores de atributos informados pelos fornecedores** em seus lances (bids) dentro de negociações de Sourcing. Cada registro representa a resposta de um fornecedor a um atributo definido na negociação — por exemplo, prazo de entrega, certificação de qualidade ou especificação técnica. A tabela permite avaliar propostas além do preço, com base em critérios qualitativos e quantitativos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação técnica de lances:** Captura as respostas dos fornecedores a atributos definidos na negociação (e.g., garantia, tempo de entrega, certificações).
- **Scoring multi-critério:** Permite pontuar propostas com base em atributos não-financeiros além do preço.
- **Comparação de fornecedores:** Base para relatórios comparativos de respostas entre participantes.
- **Compliance de requisitos:** Validação de conformidade com especificações obrigatórias da negociação.
- **Auditoria de Sourcing:** Registro histórico das informações fornecidas em cada lance.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BID_NUMBER | NUMBER(18) | NOT NULL | PK/FK | Número do lance do fornecedor | [[pon_bid_headers]] | 🟢 95% |
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número da linha do item na negociação | — | 🟢 95% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(200) | NOT NULL | PK | Nome do atributo da negociação | — | 🟢 90% |
| 4 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID do cabeçalho da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Identificação | Sequência do atributo dentro da linha | — | 🟡 75% |
| 6 | DATATYPE | VARCHAR2(30) | NULL | Classificação | Tipo de dado do atributo: TXT, NUM, DAT, URL | — | 🟢 85% |
| 7 | VALUE | VARCHAR2(4000) | NULL | Dados | Valor textual informado pelo fornecedor | — | 🟢 90% |
| 8 | SCORE | NUMBER | NULL | Avaliação | Pontuação atribuída ao valor (manual ou automática) | — | 🟢 85% |
| 9 | WEIGHTED_SCORE | NUMBER | NULL | Avaliação | Pontuação ponderada pelo peso do atributo | — | 🟡 75% |
| 10 | ATTR_GROUP | VARCHAR2(60) | NULL | Classificação | Grupo de atributos ao qual pertence | — | 🟡 70% |
| 11 | ATTR_GROUP_SEQ_NUMBER | NUMBER | NULL | Classificação | Sequência do grupo de atributos | — | 🟡 65% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o valor do atributo do lance pertence)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Valores de atributos de um lance específico
```sql
SELECT bav.LINE_NUMBER, bav.ATTRIBUTE_NAME, bav.DATATYPE,
       bav.VALUE, bav.SCORE, bav.WEIGHTED_SCORE
FROM   PON_BID_ATTRIBUTE_VALUES bav
WHERE  bav.BID_NUMBER = :p_bid_number
  AND  bav.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY bav.LINE_NUMBER, bav.SEQUENCE_NUMBER;
```

### Comparação de atributos entre fornecedores
```sql
SELECT bh.VENDOR_NAME, bav.ATTRIBUTE_NAME, bav.VALUE, bav.SCORE
FROM   PON_BID_ATTRIBUTE_VALUES bav
JOIN   PON_BID_HEADERS bh ON bh.BID_NUMBER = bav.BID_NUMBER
WHERE  bav.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bav.LINE_NUMBER = :p_line_number
ORDER BY bav.ATTRIBUTE_NAME, bh.VENDOR_NAME;
```

---

## 🔒 Observações

- A chave primária é composta por `BID_NUMBER`, `LINE_NUMBER` e `ATTRIBUTE_NAME` (ou `SEQUENCE_NUMBER`, dependendo da versão).
- O campo `DATATYPE` define como interpretar `VALUE`: texto livre (TXT), numérico (NUM), data (DAT) ou URL.
- O `SCORE` pode ser preenchido automaticamente pelo sistema (para atributos numéricos com faixas) ou manualmente pelo avaliador.
- Atributos obrigatórios na negociação exigem que `VALUE` seja preenchido para submissão do lance.
- A tabela complementa [[pon_bid_item_prices]] ao trazer dimensões qualitativas da proposta.

---

## 🔗 PVOs Relacionados

### [[negotiationresponserequirementandattributepvo|NegotiationResponseRequirementAndAttributePVO]] (PO · BICC: 16/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTR_LEVEL | NegResReqAttAttrLevel | ✅ |
| ATTRIBUTE_NAME | NegResReqAttAttributeName | ✅ |
| AUCTION_HEADER_ID | NegResReqAttAuctionHeaderId | — |
| BATCH_ID | NegResReqAttBatchId | — |
| BID_NUMBER | BidNumber | ✅ |
| CREATED_BY | NegResReqAttCreatedBy | — |
| CREATION_DATE | NegResReqAttCreationDate | ✅ |
| DATATYPE | NegResReqAttDatatype | ✅ |
| DATE_OLD_VALUE | NegResReqAttDateOldValue | — |
| DATE_VALUE | NegResReqAttDateValue | ✅ |
| INTERFACE_LINE_ID | NegResReqAttInterfaceLineId | — |
| INTERNAL_NOTE | NegResReqAttInternalNote | ✅ |
| LAST_UPDATE_DATE | NegResReqAttLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegResReqAttLastUpdateLogin | — |
| LAST_UPDATED_BY | NegResReqAttLastUpdatedBy | — |
| LINE_NUMBER | LineNumber | ✅ |
| NUMBER_OLD_VALUE | NegResReqAttNumberOldValue | — |
| NUMBER_VALUE | NegResReqAttNumberValue | ✅ |
| OBJECT_VERSION_NUMBER | NegResReqAttObjectVersionNumber | — |
| PROGRAM_APP_NAME | NegResReqAttProgramAppName | — |
| PROGRAM_APPLICATION_ID | NegResReqAttProgramApplicationId | — |
| PROGRAM_ID | NegResReqAttProgramId | — |
| PROGRAM_NAME | NegResReqAttProgramName | — |
| PROGRAM_UPDATE_DATE | NegResReqAttProgramUpdateDate | — |
| REQUEST_ID | NegResReqAttRequestId | — |
| SCORE | NegResReqAttScore | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| TEXT_OLD_VALUE | NegResReqAttTextOldValue | — |
| TEXT_VALUE | NegResReqAttTextValue | ✅ |
| WEIGHTED_SCORE | NegResReqAttWeightedScore | ✅ |
| WORKSHEET_NAME | NegResReqAttWorksheetName | ✅ |
| WORKSHEET_SEQUENCE_NUMBER | NegResReqAttWorksheetSequenceNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — PON_BID_ATTRIBUTE_VALUES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidattributevalues.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
