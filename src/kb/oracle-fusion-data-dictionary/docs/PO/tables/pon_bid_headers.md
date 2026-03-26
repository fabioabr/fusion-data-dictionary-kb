---
id: DOC-PO-012
doc_type: system-doc
title: "PON_BID_HEADERS — Cabeçalhos de Lances de Fornecedores"
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
  - lance-fornecedor
aliases:
  - PON_BID_HEADERS
  - pon_bid_headers
  - cabecalho-lance
  - bid-headers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_HEADERS

## 📌 Visão Geral

Armazena os **cabeçalhos dos lances** (bids/quotes) submetidos por fornecedores em negociações de Sourcing. Cada registro representa uma proposta completa de um fornecedor para uma negociação específica, contendo informações como valor total, status de submissão, moeda, termos de pagamento e dados do fornecedor. É a tabela central do lado da resposta do fornecedor no módulo de Sourcing.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Recebimento de propostas:** Registro de cada lance submetido por fornecedor em uma negociação.
- **Avaliação e ranking:** Base para classificação de fornecedores por preço e critérios ponderados.
- **Adjudicação (Award):** Identificação do lance vencedor e criação de pedido de compra.
- **Gestão de rodadas:** Controle de múltiplas rodadas de negociação (surrogação de lances).
- **Auditoria de Sourcing:** Rastreabilidade completa de quem participou, quando e com qual valor.
- **Relatórios de economia (savings):** Cálculo de saving entre preço de referência e lance vencedor.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BID_NUMBER | NUMBER(18) | NOT NULL | PK | Identificador único do lance | — | 🟢 100% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação à qual o lance responde | [[pon_auction_headers_all]] | 🟢 100% |
| 3 | BID_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do lance: ACTIVE, DRAFT, DISQUALIFIED, RESUBMISSION, ARCHIVED | — | 🟢 95% |
| 4 | BID_STATUS_NAME | VARCHAR2(80) | NULL | Classificação | Nome descritivo do status | — | 🟡 70% |
| 5 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 100% |
| 6 | VENDOR_NAME | VARCHAR2(360) | NULL | Referência | Nome do fornecedor (desnormalizado) | — | 🟢 90% |
| 7 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 95% |
| 8 | BID_AMOUNT | NUMBER | NULL | Financeiro | Valor total do lance na moeda da negociação | — | 🟢 90% |
| 9 | BID_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda do lance | — | 🟢 90% |
| 10 | RATE | NUMBER | NULL | Financeiro | Taxa de conversão da moeda do lance para moeda funcional | — | 🟢 85% |
| 11 | PUBLISH_DATE | DATE | NULL | Data | Data/hora de publicação/submissão do lance | — | 🟢 90% |
| 12 | AWARD_STATUS | VARCHAR2(30) | NULL | Classificação | Status de adjudicação: AWARDED, REJECTED, PENDING | — | 🟢 90% |
| 13 | AWARD_DATE | DATE | NULL | Data | Data de adjudicação do lance | — | 🟢 85% |
| 14 | SHORTLIST_FLAG | VARCHAR2(1) | NULL | Classificação | Lance incluído na shortlist (Y/N) | — | 🟡 75% |
| 15 | DISQUALIFY_REASON | VARCHAR2(2000) | NULL | Texto livre | Motivo da desqualificação do lance | — | 🟡 75% |
| 16 | SURROG_BID_FLAG | VARCHAR2(1) | NULL | Classificação | Lance submetido em nome do fornecedor (Y/N) | — | 🟡 70% |
| 17 | PAYMENT_TERMS_ID | NUMBER(18) | NULL | FK | Condição de pagamento proposta | [[ra_terms_b]] | 🟢 85% |
| 18 | FREIGHT_TERMS_CODE | VARCHAR2(30) | NULL | Classificação | Termos de frete propostos | — | 🟢 85% |
| 19 | NOTE_TO_AUCTION_OWNER | VARCHAR2(4000) | NULL | Texto livre | Observação do fornecedor ao comprador | — | 🟢 85% |
| 20 | BID_REVISION_NUMBER | NUMBER | NULL | Controle | Número da revisão do lance (múltiplas submissões) | — | 🟡 75% |
| 21 | TECHNICAL_SCORE | NUMBER | NULL | Avaliação | Pontuação técnica consolidada do lance | — | 🟡 75% |
| 22 | COMMERCIAL_SCORE | NUMBER | NULL | Avaliação | Pontuação comercial consolidada do lance | — | 🟡 75% |
| 23 | TOTAL_WEIGHTED_SCORE | NUMBER | NULL | Avaliação | Pontuação total ponderada (técnica + comercial) | — | 🟡 75% |
| 24 | RANK | NUMBER | NULL | Avaliação | Ranking do lance na negociação | — | 🟡 70% |
| 25 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 26 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 27 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 28 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 29 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual a proposta foi submetida)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor que submeteu a proposta)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[ra_terms_b]] — via `PAYMENT_TERMS_ID` (condição de pagamento)

### Tabelas-filha (FK de saída)
- [[pon_bid_item_prices]] — via `BID_NUMBER` (preços dos itens do lance)
- [[pon_bid_attribute_values]] — via `BID_NUMBER` (valores de atributos)
- [[pon_bid_po_lines]] — via `BID_NUMBER` (linhas de PO geradas)
- [[pon_bid_po_numbers]] — via `BID_NUMBER` (números de PO gerados)
- [[pon_bid_requirements]] — via `BID_NUMBER` (requisitos do lance)
- [[pon_bid_requirement_values]] — via `BID_NUMBER` (valores de requisitos)
- [[pon_bid_sections]] — via `BID_NUMBER` (seções do lance)

---

## 📎 Uso Típico

### Lances ativos por negociação
```sql
SELECT bh.BID_NUMBER, bh.VENDOR_NAME, bh.BID_AMOUNT,
       bh.BID_CURRENCY_CODE, bh.PUBLISH_DATE, bh.RANK
FROM   PON_BID_HEADERS bh
WHERE  bh.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bh.BID_STATUS = 'ACTIVE'
ORDER BY bh.RANK;
```

### Lances adjudicados (vencedores)
```sql
SELECT bh.BID_NUMBER, bh.VENDOR_NAME, bh.BID_AMOUNT,
       bh.AWARD_DATE, bh.TOTAL_WEIGHTED_SCORE
FROM   PON_BID_HEADERS bh
WHERE  bh.AUCTION_HEADER_ID = :p_auction_header_id
  AND  bh.AWARD_STATUS = 'AWARDED';
```

### Filtros comuns
- `BID_STATUS = 'ACTIVE'` — Lances ativos (submetidos)
- `BID_STATUS = 'DRAFT'` — Lances em rascunho (não submetidos)
- `AWARD_STATUS = 'AWARDED'` — Lances vencedores
- `SURROG_BID_FLAG = 'Y'` — Lances submetidos em nome do fornecedor

---

## 🔒 Observações

- Cada fornecedor pode ter múltiplos registros para a mesma negociação se houver rodadas de re-submissão; o `BID_REVISION_NUMBER` diferencia as versões.
- O `BID_STATUS = 'ACTIVE'` identifica o lance mais recente e válido do fornecedor; versões anteriores ficam como `ARCHIVED`.
- O campo `SURROG_BID_FLAG` indica lances submetidos pelo comprador em nome do fornecedor (surrogate bidding).
- O `RANK` é calculado automaticamente pelo sistema com base nos critérios de avaliação definidos na negociação.
- `TOTAL_WEIGHTED_SCORE` combina `TECHNICAL_SCORE` e `COMMERCIAL_SCORE` conforme os pesos definidos na negociação.

---

## 📚 Referências

- [Oracle Docs — PON_BID_HEADERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidheaders.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
