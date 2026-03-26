---
id: DOC-PO-006
doc_type: system-doc
title: "PON_AUCTION_SECTIONS — Seções de Negociações"
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
  - auction-sections
  - secoes-negociacao
aliases:
  - PON_AUCTION_SECTIONS
  - pon_auction_sections
  - secoes-negociacao
  - sourcing-sections
  - pon-sections
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUCTION_SECTIONS

## Visão Geral

Armazena as **seções (agrupamentos lógicos)** dentro de uma negociação do módulo Oracle Sourcing. As seções organizam os itens e atributos da negociação em grupos temáticos, facilitando a navegação e preenchimento por parte dos fornecedores. Podem representar lotes, categorias funcionais ou divisões geográficas.

> [!note] Módulo Sourcing (PON)
> Seções são opcionais — negociações simples podem não utilizá-las. Em negociações complexas, seções permitem agrupamento por lote (lot bidding), região ou categoria.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Organização de negociações:** Agrupamento lógico de itens por lote, categoria ou região geográfica.
- **Lot bidding:** Permite que fornecedores lancem preços por lote (seção) ao invés de por item individual.
- **Avaliação segmentada:** Scoring e ranking de propostas por seção/lote.
- **Templates reutilizáveis:** Definição de estruturas de seção padronizadas para negociações recorrentes.
- **Experiência do fornecedor:** Navegação organizada na interface de resposta à negociação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟢 90% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Negociação associada | [[pon_auction_headers_all]] | 🟢 95% |
| 3 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da seção (ex: "Lote 1 — Material Elétrico") | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada da seção | — | 🟢 85% |
| 5 | DISPLAY_ORDER | NUMBER | NULL | Controle | Ordem de exibição na interface | — | 🟢 85% |
| 6 | PARENT_SECTION_ID | NUMBER(18) | NULL | FK | Seção-pai (para hierarquia de seções) | [[pon_auction_sections]] | 🟡 70% |
| 7 | LOT_FLAG | VARCHAR2(1) | NULL | Flag | Indica se a seção funciona como lote para bidding (Y/N) | — | 🟡 75% |
| 8 | WEIGHT | NUMBER | NULL | Avaliação | Peso da seção na avaliação multi-critério | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual a seção pertence)
- [[pon_auction_sections]] — via `PARENT_SECTION_ID` (seção-pai, autorrelacionamento)

### Tabelas-filha (FK de saída)
- [[pon_auction_item_prices_all]] — via `SECTION_ID` (itens/linhas dentro da seção)
- [[pon_auction_attributes]] — via `SECTION_ID` (atributos dentro da seção)
- [[pon_auction_sections]] — via `PARENT_SECTION_ID` (subseções)

---

## Uso Típico

### Seções de uma negociação
```sql
SELECT sec.SECTION_ID, sec.SECTION_NAME,
       sec.DESCRIPTION, sec.DISPLAY_ORDER,
       sec.LOT_FLAG
FROM   PON_AUCTION_SECTIONS sec
WHERE  sec.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY sec.DISPLAY_ORDER;
```

### Itens por seção (lote)
```sql
SELECT sec.SECTION_NAME,
       COUNT(ip.LINE_NUMBER) AS qtd_itens,
       SUM(ip.QUANTITY * ip.TARGET_PRICE) AS valor_estimado
FROM   PON_AUCTION_SECTIONS sec
JOIN   PON_AUCTION_ITEM_PRICES_ALL ip
  ON   ip.AUCTION_HEADER_ID = sec.AUCTION_HEADER_ID
  AND  ip.SECTION_ID = sec.SECTION_ID
WHERE  sec.AUCTION_HEADER_ID = :p_auction_header_id
GROUP BY sec.SECTION_NAME
ORDER BY sec.DISPLAY_ORDER;
```

### Filtros comuns
- `LOT_FLAG = 'Y'` — Seções que funcionam como lotes
- `PARENT_SECTION_ID IS NULL` — Seções de nível raiz (sem pai)

---

## Observações

- Seções são opcionais — negociações simples podem ter todos os itens sem seção atribuída.
- O campo `PARENT_SECTION_ID` permite criar hierarquias de seções (ex: Seção → Subseção → Itens).
- Em negociações com `LOT_FLAG = 'Y'`, o fornecedor pode ser obrigado a dar lance em todos os itens do lote (all-or-nothing).
- O `DISPLAY_ORDER` controla a sequência visual na interface, independente do `SECTION_ID`.
- O `WEIGHT` é utilizado em avaliações multi-critério para ponderar a importância relativa de cada seção/lote.

---

## Referências

- [Oracle Docs — PON_AUCTION_SECTIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponauctionsections.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
