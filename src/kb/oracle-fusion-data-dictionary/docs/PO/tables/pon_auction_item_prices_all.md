---
id: DOC-PO-005
doc_type: system-doc
title: "PON_AUCTION_ITEM_PRICES_ALL — Linhas de Itens e Preços em Negociações"
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
  - auction-items
  - precos-negociacao
aliases:
  - PON_AUCTION_ITEM_PRICES_ALL
  - pon_auction_item_prices_all
  - linhas-itens-negociacao
  - sourcing-item-prices
  - pon-item-prices
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUCTION_ITEM_PRICES_ALL

## Visão Geral

Armazena as **linhas de itens e preços** de cada negociação do módulo Oracle Sourcing. Cada registro representa um item individual dentro da negociação, contendo descrição, quantidade, unidade de medida, preço-alvo (target price), categoria de compra, e informações de award. É a tabela de detalhe principal que complementa o cabeçalho (`PON_AUCTION_HEADERS_ALL`).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` na tabela-pai é necessário para consultas por organização específica.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de escopo:** Itens que compõem a negociação (o que se deseja comprar/contratar).
- **Gestão de preços:** Preço-alvo, preço atual, preço de award e savings calculados.
- **Award de itens:** Registro de qual fornecedor foi awardado para cada linha e em qual quantidade/preço.
- **Análise de savings:** Comparação entre preço-alvo e preço final por item.
- **Integração com requisições:** Vínculo com linhas de requisição de compra originadoras.
- **Relatórios de spend:** Base para análise de gastos por categoria de compra.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | PK/FK | Negociação associada | [[pon_auction_headers_all]] | 🟢 100% |
| 2 | LINE_NUMBER | NUMBER | NOT NULL | PK | Número da linha dentro da negociação | — | 🟢 100% |
| 3 | ITEM_DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição do item/serviço | — | 🟢 95% |
| 4 | ITEM_ID | NUMBER(18) | NULL | FK | Item do catálogo (se aplicável) | [[egp_system_items_b]] | 🟢 90% |
| 5 | ITEM_NUMBER | VARCHAR2(300) | NULL | Identificação | Número do item no catálogo | — | 🟢 90% |
| 6 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compra do item | [[egp_categories_b]] | 🟢 90% |
| 7 | CATEGORY_NAME | VARCHAR2(240) | NULL | Identificação | Nome da categoria de compra (desnormalizado) | — | 🟡 80% |
| 8 | QUANTITY | NUMBER | NULL | Quantidade | Quantidade solicitada | — | 🟢 95% |
| 9 | UOM_CODE | VARCHAR2(30) | NULL | Unidade | Unidade de medida | [[inv_units_of_measure_b]] | 🟢 90% |
| 10 | CURRENT_PRICE | NUMBER | NULL | Financeiro | Preço unitário atual (referência/benchmark) | — | 🟢 90% |
| 11 | TARGET_PRICE | NUMBER | NULL | Financeiro | Preço-alvo desejado pelo comprador | — | 🟢 85% |
| 12 | BID_START_PRICE | NUMBER | NULL | Financeiro | Preço inicial de lance (em auctions) | — | 🟡 80% |
| 13 | AWARD_PRICE | NUMBER | NULL | Financeiro | Preço de award (final negociado) | — | 🟢 85% |
| 14 | AWARD_QUANTITY | NUMBER | NULL | Quantidade | Quantidade awarded | — | 🟢 85% |
| 15 | AWARD_STATUS | VARCHAR2(30) | NULL | Status | Status do award do item: NO, AWARDED, REJECTED | — | 🟢 85% |
| 16 | AWARD_DATE | DATE | NULL | Data | Data do award para este item | — | 🟢 85% |
| 17 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations_all_f]] | 🟡 75% |
| 18 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade do item | — | 🟢 85% |
| 19 | SECTION_ID | NUMBER(18) | NULL | FK | Seção da negociação | [[pon_auction_sections]] | 🟡 70% |
| 20 | LINE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo da linha (bens, serviços, etc.) | — | 🟡 75% |
| 21 | REQUISITION_HEADER_ID | NUMBER(18) | NULL | FK | Requisição de compra originadora | [[por_requisition_headers_all]] | 🟡 75% |
| 22 | REQUISITION_LINE_ID | NUMBER(18) | NULL | FK | Linha da requisição originadora | [[por_requisition_lines_all]] | 🟡 75% |
| 23 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 24 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 25 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 26 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 27 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 28 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 29 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 30 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (cabeçalho da negociação)
- [[pon_auction_sections]] — via `SECTION_ID` (seção do lote à qual o item de negociação pertence)
- [[egp_system_items_b]] — via `ITEM_ID` (item do catálogo)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de compra)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do item de negociação)
- [[por_requisition_headers_all]] — via `REQUISITION_HEADER_ID` (requisição de compra que originou o item de negociação)
- [[por_requisition_lines_all]] — via `REQUISITION_LINE_ID` (linha de requisição)
- [[hr_locations_all_f]] — via `SHIP_TO_LOCATION_ID` (local de entrega)

### Tabelas-filha (FK de saída)
- [[pon_auction_attributes]] — via `AUCTION_HEADER_ID` + `LINE_NUMBER` (atributos do item)
- Tabelas de bid/response (ex: `PON_BID_ITEM_PRICES`) — via `AUCTION_HEADER_ID` + `LINE_NUMBER` (respostas de fornecedores)

---

## Uso Típico

### Itens de uma negociação com preços
```sql
SELECT ip.LINE_NUMBER, ip.ITEM_DESCRIPTION,
       ip.QUANTITY, ip.UOM_CODE,
       ip.CURRENT_PRICE, ip.TARGET_PRICE,
       ip.AWARD_PRICE, ip.AWARD_STATUS
FROM   PON_AUCTION_ITEM_PRICES_ALL ip
WHERE  ip.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY ip.LINE_NUMBER;
```

### Savings por negociação
```sql
SELECT SUM((ip.CURRENT_PRICE - ip.AWARD_PRICE) * ip.AWARD_QUANTITY) AS saving_total,
       ROUND(AVG((ip.CURRENT_PRICE - ip.AWARD_PRICE) / NULLIF(ip.CURRENT_PRICE, 0)) * 100, 2) AS saving_pct
FROM   PON_AUCTION_ITEM_PRICES_ALL ip
WHERE  ip.AUCTION_HEADER_ID = :p_auction_header_id
  AND  ip.AWARD_STATUS = 'AWARDED'
  AND  ip.CURRENT_PRICE > 0;
```

### Filtros comuns
- `AWARD_STATUS = 'AWARDED'` — Itens awarded a um fornecedor
- `AWARD_STATUS = 'NO'` — Itens sem award
- `CATEGORY_ID = :cat_id` — Filtro por categoria de compra
- `NEED_BY_DATE <= SYSDATE + 30` — Itens com necessidade nos próximos 30 dias

---

## Observações

- A chave primária é composta por `AUCTION_HEADER_ID` + `LINE_NUMBER`.
- O campo `CURRENT_PRICE` representa o preço de referência/benchmark (preço contratual anterior ou preço de mercado).
- O `TARGET_PRICE` pode ser ocultado dos fornecedores dependendo da configuração da negociação no cabeçalho.
- O `AWARD_PRICE` é preenchido somente após o processo de award; antes disso permanece nulo.
- Linhas podem estar vinculadas a requisições de compra via `REQUISITION_HEADER_ID` + `REQUISITION_LINE_ID`.
- Em negociações do tipo lot, múltiplos itens podem ser agrupados via `SECTION_ID`.

---

## Referências

- [Oracle Docs — PON_AUCTION_ITEM_PRICES_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponauctionitempricesall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
