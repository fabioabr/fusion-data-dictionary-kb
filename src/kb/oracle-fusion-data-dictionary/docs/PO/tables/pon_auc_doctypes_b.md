---
id: DOC-PO-007
doc_type: system-doc
title: "PON_AUC_DOCTYPES_B — Tipos de Documento de Negociação (Base)"
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
  - document-types
  - doctypes
aliases:
  - PON_AUC_DOCTYPES_B
  - pon_auc_doctypes_b
  - tipos-documento-negociacao
  - sourcing-doctypes-base
  - pon-doctypes-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUC_DOCTYPES_B

## Visão Geral

Armazena a definição base (não traduzível) dos **tipos de documento de negociação** do módulo Oracle Sourcing. Cada registro define um tipo de negociação (RFQ, RFI, Auction, Reverse Auction, etc.) com suas regras e comportamentos associados — outcome esperado, regras de lances, scoring, e flags de configuração. É a tabela `_B` (base) do padrão Oracle MLS (Multi-Language Support).

> [!note] Padrão Oracle MLS (_B/_TL/_VL)
> - `_B` — Dados base independentes de idioma (esta tabela)
> - `_TL` — Traduções (nomes/descrições por idioma) → [[pon_auc_doctypes_tl]]
> - `_VL` — View que combina _B + _TL para o idioma da sessão → [[pon_auc_doctypes_vl]]

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de tipos de negociação:** Define quais tipos estão disponíveis para os compradores criarem.
- **Regras de negócio por tipo:** Cada tipo pode ter regras distintas de lance, visibilidade, award e outcome.
- **Controle de acesso:** Tipos de documento podem ser restritos a determinados compradores ou business units.
- **Integração com PO:** O outcome define que tipo de documento é gerado após award (PO, BPA, CPA).
- **Seed data:** Tipos padrão são fornecidos pelo Oracle (seed); implementadores podem criar tipos customizados.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de documento | — | 🟢 95% |
| 2 | DOCTYPE_GROUP_NAME | VARCHAR2(30) | NOT NULL | Classificação | Grupo funcional: AUCTION, RFQ, RFI, BUYER_AUCTION | — | 🟢 90% |
| 3 | TRANSACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de transação associado | — | 🟢 85% |
| 4 | OUTCOME | VARCHAR2(30) | NULL | Classificação | Resultado esperado: STANDARD_PO, BLANKET, CONTRACT, NONE | — | 🟢 90% |
| 5 | DIRECTION | VARCHAR2(30) | NOT NULL | Classificação | Direção do lance: FORWARD (preço sobe), REVERSE (preço cai) | — | 🟢 85% |
| 6 | PRICE_VISIBILITY_CODE | VARCHAR2(30) | NULL | Regras | Visibilidade de preços: OPEN, SEALED, PARTIALLY_SEALED | — | 🟢 85% |
| 7 | SCORING_FLAG | VARCHAR2(1) | NULL | Flag | Permite scoring/avaliação multi-critério (Y/N) | — | 🟡 80% |
| 8 | ALLOW_MULTIPLE_ROUNDS_FLAG | VARCHAR2(1) | NULL | Flag | Permite múltiplas rodadas de lances (Y/N) | — | 🟡 75% |
| 9 | ALLOW_AWARD_FLAG | VARCHAR2(1) | NULL | Flag | Permite award direto (Y/N) | — | 🟡 75% |
| 10 | BID_RANKING | VARCHAR2(30) | NULL | Regras | Critério de ranking de lances: PRICE_ONLY, MULTI_ATTRIBUTE_SCORING | — | 🟢 80% |
| 11 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Flag | Tipo de documento ativo (Y/N) | — | 🟢 90% |
| 12 | INTERNAL_NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome interno do tipo (não traduzível) | — | 🟢 85% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai direta — tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[pon_auc_doctypes_tl]] — via `DOCTYPE_ID` (traduções do tipo de documento)
- [[pon_auc_doctypes_vl]] — via `DOCTYPE_ID` (view multilíngue do tipo de documento de negociação)
- [[pon_auction_headers_all]] — via `DOCTYPE_ID` (negociações que utilizam este tipo)

---

## Uso Típico

### Tipos de documento ativos
```sql
SELECT dt.DOCTYPE_ID, dt.INTERNAL_NAME,
       dt.DOCTYPE_GROUP_NAME, dt.OUTCOME,
       dt.DIRECTION, dt.BID_RANKING
FROM   PON_AUC_DOCTYPES_B dt
WHERE  dt.ENABLED_FLAG = 'Y'
ORDER BY dt.DOCTYPE_GROUP_NAME;
```

### Tipos com avaliação multi-critério
```sql
SELECT dt.DOCTYPE_ID, dt.INTERNAL_NAME,
       dt.BID_RANKING, dt.SCORING_FLAG
FROM   PON_AUC_DOCTYPES_B dt
WHERE  dt.SCORING_FLAG = 'Y'
  AND  dt.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `DOCTYPE_GROUP_NAME = 'RFQ'` — Solicitações de cotação
- `OUTCOME = 'BLANKET'` — Tipos que geram Blanket Purchase Agreement
- `DIRECTION = 'REVERSE'` — Leilões reversos (preço decresce)

---

## Observações

- Esta tabela segue o padrão Oracle MLS: dados base (não traduzíveis) ficam na `_B`; nomes e descrições traduzidos ficam na `_TL`.
- Os tipos padrão (seed) incluem: RFQ, RFI, Reverse Auction, Buyer Auction, Blanket Agreement Negotiation.
- O campo `OUTCOME` determina que tipo de documento de compra é gerado após o award da negociação.
- `DIRECTION = 'REVERSE'` é o padrão para compras (fornecedores competem por preço mais baixo); `FORWARD` é usado em vendas/leilões.
- Tipos com `SCORING_FLAG = 'Y'` e `BID_RANKING = 'MULTI_ATTRIBUTE_SCORING'` permitem avaliação ponderada de preço + atributos técnicos.
- A flag `ALLOW_MULTIPLE_ROUNDS_FLAG` é típica de negociações RFI → RFQ → Auction (processo em etapas).

---

## Referências

- [Oracle Docs — PON_AUC_DOCTYPES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponaucdoctypesb.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
