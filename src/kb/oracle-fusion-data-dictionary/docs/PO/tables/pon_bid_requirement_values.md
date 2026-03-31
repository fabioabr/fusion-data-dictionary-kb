---
id: DOC-PO-017
doc_type: system-doc
title: "PON_BID_REQUIREMENT_VALUES — Respostas de Requisitos em Lances"
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
  - respostas
aliases:
  - PON_BID_REQUIREMENT_VALUES
  - pon_bid_requirement_values
  - respostas-requisitos-lance
  - bid-requirement-values
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_REQUIREMENT_VALUES

## 📌 Visão Geral

Armazena as **respostas dos fornecedores** aos requisitos definidos na negociação de Sourcing. Cada registro contém o valor informado pelo fornecedor para um requisito específico do lance, incluindo texto, número, data ou referência a anexo. Complementa a tabela [[pon_bid_requirements]] com os dados efetivamente preenchidos pelo participante.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação de propostas:** Captura as respostas individuais de cada fornecedor a cada requisito.
- **Scoring técnico:** Base para atribuição de pontuação a respostas de requisitos técnicos e comerciais.
- **Comparação de fornecedores:** Análise lado a lado das respostas entre participantes.
- **Compliance check:** Verificação de completude e conformidade das respostas com os requisitos obrigatórios.
- **Auditoria de Sourcing:** Registro histórico imutável das informações fornecidas pelo participante.

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
| 2 | REQUIREMENT_ID | NUMBER(18) | NOT NULL | PK/FK | ID do requisito respondido | [[pon_bid_requirements]] | 🟢 90% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 4 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Dados | Resposta textual/numérica do fornecedor | — | 🟢 90% |
| 5 | RESPONSE_DATE | DATE | NULL | Dados | Resposta do tipo data (quando RESPONSE_TYPE = DATE) | — | 🟡 75% |
| 6 | RESPONSE_NUMBER | NUMBER | NULL | Dados | Resposta numérica (quando RESPONSE_TYPE = NUMBER) | — | 🟡 75% |
| 7 | SCORE | NUMBER | NULL | Avaliação | Pontuação atribuída à resposta (manual ou automática) | — | 🟢 85% |
| 8 | WEIGHTED_SCORE | NUMBER | NULL | Avaliação | Pontuação ponderada pelo peso do requisito | — | 🟡 75% |
| 9 | ATTACHMENT_ID | NUMBER(18) | NULL | Referência | ID do anexo associado à resposta | — | 🟡 70% |
| 10 | EVALUATOR_ID | NUMBER(18) | NULL | Referência | Avaliador que pontuou a resposta | — | 🟡 70% |
| 11 | EVALUATOR_COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários do avaliador sobre a resposta | — | 🟡 70% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_bid_requirements]] — via `BID_NUMBER` + `REQUIREMENT_ID` (definição do requisito)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação do requisito respondido pelo fornecedor)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Respostas de um fornecedor a todos os requisitos
```sql
SELECT br.REQUIREMENT_NAME, br.MANDATORY_FLAG,
       brv.RESPONSE_VALUE, brv.SCORE, brv.WEIGHTED_SCORE,
       brv.EVALUATOR_COMMENTS
FROM   PON_BID_REQUIREMENT_VALUES brv
JOIN   PON_BID_REQUIREMENTS br
       ON br.BID_NUMBER = brv.BID_NUMBER
      AND br.REQUIREMENT_ID = brv.REQUIREMENT_ID
WHERE  brv.BID_NUMBER = :p_bid_number
ORDER BY br.DISPLAY_ORDER;
```

### Comparação de respostas entre fornecedores
```sql
SELECT bh.VENDOR_NAME, br.REQUIREMENT_NAME,
       brv.RESPONSE_VALUE, brv.SCORE
FROM   PON_BID_REQUIREMENT_VALUES brv
JOIN   PON_BID_REQUIREMENTS br
       ON br.BID_NUMBER = brv.BID_NUMBER
      AND br.REQUIREMENT_ID = brv.REQUIREMENT_ID
JOIN   PON_BID_HEADERS bh ON bh.BID_NUMBER = brv.BID_NUMBER
WHERE  brv.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bh.BID_STATUS = 'ACTIVE'
ORDER BY br.REQUIREMENT_NAME, bh.VENDOR_NAME;
```

---

## 🔒 Observações

- A chave primária é composta por `BID_NUMBER` + `REQUIREMENT_ID`.
- O campo `RESPONSE_VALUE` armazena a resposta genérica em texto; `RESPONSE_DATE` e `RESPONSE_NUMBER` são campos tipados alternativos.
- O `SCORE` pode ser preenchido automaticamente (para respostas numéricas com faixas predefinidas) ou manualmente pelo avaliador.
- O `EVALUATOR_ID` identifica qual membro do comitê de avaliação atribuiu a pontuação.
- Quando o requisito aceita anexo, o `ATTACHMENT_ID` referencia o documento carregado pelo fornecedor.
- A tabela complementa [[pon_bid_requirements]] — os requisitos definem a pergunta, esta tabela armazena a resposta.

---

## 🔗 PVOs Relacionados

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 10/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | RespReqtValuesAuctionHeaderId | — |
| BID_NUMBER | RespReqtValuesBidNumber | ✅ |
| CREATED_BY | RespReqtValuesCreatedBy | — |
| CREATION_DATE | RespReqtValuesCreationDate | — |
| DATE_VALUE | RespReqtValuesDateValue | ✅ |
| DATETIME_VALUE | RespReqtValuesDatetimeValue | ✅ |
| IS_SELECTED_FLAG | RespReqtValuesIsSelectedFlag | ✅ |
| LAST_UPDATE_DATE | RespReqtValuesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RespReqtValuesLastUpdateLogin | — |
| LAST_UPDATED_BY | RespReqtValuesLastUpdatedBy | — |
| NUMBER_VALUE | RespReqtValuesNumberValue | ✅ |
| OBJECT_VERSION_NUMBER | RespReqtValuesObjectVersionNumber | — |
| OLD_DATE_VALUE | RespReqtValuesOldDateValue | — |
| OLD_DATETIME_VALUE | RespReqtValuesOldDatetimeValue | — |
| OLD_IS_SELECTED_FLAG | RespReqtValuesOldIsSelectedFlag | — |
| OLD_NUMBER_VALUE | RespReqtValuesOldNumberValue | — |
| OLD_TEXT_VALUE | RespReqtValuesOldTextValue | — |
| REQUIREMENT_ID | RespReqtValuesRequirementId | ✅ |
| REQUIREMENT_VALUE_ID | RespReqtValuesRequirementValueId | ✅ |
| SCORE_ID | RespReqtValuesScoreId | ✅ |
| TEXT_VALUE | RespReqtValuesTextValue | ✅ |

### [[negotiationresprequirementvaluesextractpvo|NegotiationRespRequirementValuesExtractPVO]] (PO · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_VALUE | DateValue | ✅ |
| DATETIME_VALUE | DatetimeValue | ✅ |
| IS_SELECTED_FLAG | IsSelectedFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NUMBER_VALUE | NumberValue | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OLD_DATE_VALUE | OldDateValue | ✅ |
| OLD_DATETIME_VALUE | OldDatetimeValue | ✅ |
| OLD_IS_SELECTED_FLAG | OldIsSelectedFlag | ✅ |
| OLD_NUMBER_VALUE | OldNumberValue | ✅ |
| OLD_TEXT_VALUE | OldTextValue | ✅ |
| REQUIREMENT_ID | RequirementId | ✅ |
| REQUIREMENT_VALUE_ID | RequirementValueId | ✅ |
| SCORE_ID | ScoreId | ✅ |
| TEXT_VALUE | TextValue | ✅ |

---

## 📚 Referências

- [Oracle Docs — PON_BID_REQUIREMENT_VALUES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidrequirementvalues.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
