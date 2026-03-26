---
id: DOC-PO-003
doc_type: system-doc
title: "PON_AUCTION_ATTRIBUTES — Atributos de Itens em Negociações"
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
  - auction-attributes
  - atributos-negociacao
aliases:
  - PON_AUCTION_ATTRIBUTES
  - pon_auction_attributes
  - atributos-itens-negociacao
  - sourcing-attributes
  - pon-attributes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUCTION_ATTRIBUTES

## Visão Geral

Armazena os **atributos descritivos dos itens** em negociações do módulo Oracle Sourcing. Cada registro representa um atributo específico (técnico, comercial ou funcional) associado a uma linha de item da negociação, permitindo que compradores definam critérios de avaliação e fornecedores preencham respostas detalhadas.

> [!note] Módulo Sourcing (PON)
> Os atributos complementam as linhas de preço (`PON_AUCTION_ITEM_PRICES_ALL`) com informações qualitativas que suportam avaliação multi-critério (scoring) de propostas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de requisitos técnicos:** Atributos obrigatórios que fornecedores devem preencher (certificações, prazo de entrega, garantia, etc.).
- **Avaliação multi-critério:** Pesos e scores atribuídos a cada atributo para ranking de propostas.
- **Comparação de propostas:** Matriz comparativa de respostas dos fornecedores por atributo.
- **Templates de negociação:** Reuso de conjuntos de atributos padronizados entre negociações.
- **Compliance técnico:** Validação de que fornecedores atendem requisitos mínimos.

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
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número da linha de item na negociação | — | 🟢 90% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do atributo (ex: "Prazo de Entrega", "Certificação ISO") | — | 🟢 90% |
| 4 | SEQUENCE_NUMBER | NUMBER | NOT NULL | PK | Sequência do atributo dentro da linha | — | 🟢 90% |
| 5 | DATATYPE | VARCHAR2(30) | NULL | Classificação | Tipo de dado do atributo: TXT, NUM, DAT, URL | — | 🟢 85% |
| 6 | DISPLAY_TARGET_FLAG | VARCHAR2(1) | NULL | Flag | Exibir valor-alvo ao fornecedor (Y/N) | — | 🟡 75% |
| 7 | VALUE | VARCHAR2(4000) | NULL | Valor | Valor-alvo ou resposta esperada definida pelo comprador | — | 🟢 85% |
| 8 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Flag | Atributo obrigatório (Y/N) | — | 🟢 85% |
| 9 | SCORING_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de scoring: NONE, MANUAL, AUTOMATIC | — | 🟡 75% |
| 10 | WEIGHT | NUMBER | NULL | Avaliação | Peso do atributo na avaliação (0-100) | — | 🟢 85% |
| 11 | SECTION_ID | NUMBER(18) | NULL | FK | Seção à qual o atributo pertence | [[pon_auction_sections]] | 🟡 70% |
| 12 | DISPLAY_PROMPT | VARCHAR2(240) | NULL | Identificação | Rótulo de exibição do atributo na interface | — | 🟡 70% |
| 13 | IP_CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compra associada | — | 🟡 65% |
| 14 | ATTR_GROUP | VARCHAR2(30) | NULL | Classificação | Grupo de atributos (agrupamento lógico) | — | 🟡 65% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual o atributo pertence)
- [[pon_auction_item_prices_all]] — via `AUCTION_HEADER_ID` + `LINE_NUMBER` (linha de item da negociação vinculada ao atributo)
- [[pon_auction_sections]] — via `SECTION_ID` (seção da negociação)

### Tabelas-filha (FK de saída)
- Respostas de fornecedores em tabelas de bid attributes (ex: `PON_BID_ATTRIBUTE_VALUES`) — via `AUCTION_HEADER_ID` + `LINE_NUMBER` + `SEQUENCE_NUMBER`.

---

## Uso Típico

### Atributos de uma linha de negociação
```sql
SELECT attr.SEQUENCE_NUMBER, attr.ATTRIBUTE_NAME,
       attr.DATATYPE, attr.MANDATORY_FLAG,
       attr.WEIGHT, attr.VALUE AS valor_alvo
FROM   PON_AUCTION_ATTRIBUTES attr
WHERE  attr.AUCTION_HEADER_ID = :p_auction_header_id
  AND  attr.LINE_NUMBER = :p_line_number
ORDER BY attr.SEQUENCE_NUMBER;
```

### Atributos obrigatórios sem resposta
```sql
SELECT attr.LINE_NUMBER, attr.ATTRIBUTE_NAME
FROM   PON_AUCTION_ATTRIBUTES attr
WHERE  attr.AUCTION_HEADER_ID = :p_auction_header_id
  AND  attr.MANDATORY_FLAG = 'Y'
ORDER BY attr.LINE_NUMBER, attr.SEQUENCE_NUMBER;
```

### Filtros comuns
- `MANDATORY_FLAG = 'Y'` — Atributos obrigatórios
- `SCORING_TYPE = 'AUTOMATIC'` — Avaliação automática
- `WEIGHT > 0` — Atributos com peso na avaliação

---

## Observações

- A chave primária é composta por `AUCTION_HEADER_ID` + `LINE_NUMBER` + `SEQUENCE_NUMBER`.
- O campo `WEIGHT` é utilizado em negociações com avaliação multi-critério (MAS — Multi-Attribute Scoring).
- Atributos com `SCORING_TYPE = 'AUTOMATIC'` são avaliados pelo sistema com base em regras predefinidas; `MANUAL` requer intervenção do comprador.
- O `DATATYPE` determina o tipo de controle de entrada na interface do fornecedor (campo texto, numérico, data ou URL).
- Atributos podem ser agrupados em seções via `SECTION_ID` para organização visual na interface.

---

## Referências

- [Oracle Docs — PON_AUCTION_ATTRIBUTES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponauctionattributes.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
