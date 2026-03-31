---
id: DOC-PO-018
doc_type: system-doc
title: "PON_BID_SECTIONS — Seções de Lances de Fornecedores"
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
  - secoes-lance
aliases:
  - PON_BID_SECTIONS
  - pon_bid_sections
  - secoes-lance
  - bid-sections
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_BID_SECTIONS

## 📌 Visão Geral

Armazena as **seções que estruturam o conteúdo de um lance** de fornecedor em negociações de Sourcing. Cada registro representa uma seção lógica (e.g., "Proposta Técnica", "Condições Comerciais", "Documentação") que agrupa requisitos e atributos do lance. A estrutura de seções reflete a organização definida na negociação pelo comprador.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação de propostas:** Organização lógica do lance em seções temáticas.
- **Avaliação segmentada:** Permite que diferentes avaliadores pontuem seções distintas (e.g., técnica vs. comercial).
- **Navegação de propostas:** Facilita a consulta organizada das respostas do fornecedor.
- **Scoring por seção:** Cálculo de pontuação parcial por seção com pesos independentes.
- **Template de RFx:** Reflexo da estrutura de seções definida na negociação.

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
| 2 | SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção no lance | — | 🟢 90% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID da negociação | [[pon_auction_headers_all]] | 🟢 95% |
| 4 | SECTION_NAME | VARCHAR2(500) | NULL | Identificação | Nome/título da seção | — | 🟢 85% |
| 5 | SECTION_DESCRIPTION | VARCHAR2(4000) | NULL | Texto livre | Descrição detalhada da seção | — | 🟡 80% |
| 6 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição da seção no lance | — | 🟢 85% |
| 7 | PARENT_SECTION_ID | NUMBER(18) | NULL | Hierarquia | Seção pai (para estrutura hierárquica de seções) | — | 🟡 75% |
| 8 | SECTION_WEIGHT | NUMBER | NULL | Avaliação | Peso da seção no cálculo de scoring geral | — | 🟡 75% |
| 9 | SECTION_SCORE | NUMBER | NULL | Avaliação | Pontuação consolidada da seção | — | 🟡 70% |
| 10 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da seção: TECHNICAL, COMMERCIAL, GENERAL | — | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_bid_headers]] — via `BID_NUMBER` (cabeçalho do lance)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual a seção do lance pertence)

### Tabelas-filha (FK de saída)
- [[pon_bid_requirements]] — via `SECTION_ID` (requisitos que pertencem à seção)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Estrutura de seções de um lance
```sql
SELECT bs.SECTION_ID, bs.SECTION_NAME, bs.SECTION_TYPE,
       bs.DISPLAY_ORDER, bs.SECTION_WEIGHT, bs.SECTION_SCORE
FROM   PON_BID_SECTIONS bs
WHERE  bs.BID_NUMBER = :p_bid_number
ORDER BY bs.DISPLAY_ORDER;
```

### Requisitos por seção de um lance
```sql
SELECT bs.SECTION_NAME, br.REQUIREMENT_NAME,
       brv.RESPONSE_VALUE, brv.SCORE
FROM   PON_BID_SECTIONS bs
JOIN   PON_BID_REQUIREMENTS br ON br.SECTION_ID = bs.SECTION_ID
                                AND br.BID_NUMBER = bs.BID_NUMBER
LEFT JOIN PON_BID_REQUIREMENT_VALUES brv
       ON brv.BID_NUMBER = br.BID_NUMBER
      AND brv.REQUIREMENT_ID = br.REQUIREMENT_ID
WHERE  bs.BID_NUMBER = :p_bid_number
ORDER BY bs.DISPLAY_ORDER, br.DISPLAY_ORDER;
```

---

## 🔒 Observações

- A chave primária é composta por `BID_NUMBER` + `SECTION_ID`.
- O `PARENT_SECTION_ID` permite hierarquias de seções (seção → sub-seção), embora a maioria das implementações use estrutura plana.
- O `SECTION_WEIGHT` define o peso relativo da seção no scoring total; a soma dos pesos de todas as seções deve totalizar 100%.
- O `SECTION_SCORE` é calculado agregando as pontuações dos requisitos que pertencem à seção.
- As seções refletem a estrutura definida na negociação ([[pon_auction_sections]]); o fornecedor não pode criar seções adicionais.

---

## 🔗 PVOs Relacionados

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegRespSectionsAuctionHeaderId6 | — |
| BID_NUMBER | NegRespSectionsBidNumber2 | — |
| CREATED_BY | NegRespSectionsCreatedBy6 | — |
| CREATION_DATE | NegRespSectionsCreationDate6 | — |
| LAST_UPDATE_DATE | NegRespSectionsLastUpdateDate6 | ✅ |
| LAST_UPDATE_LOGIN | NegRespSectionsLastUpdateLogin6 | — |
| LAST_UPDATED_BY | NegRespSectionsLastUpdatedBy6 | — |
| OBJECT_VERSION_NUMBER | NegRespSectionsObjectVersionNumber6 | — |
| SECTION_ID | NegRespSectionsSectionId3 | — |
| SECTION_VISITED_FLAG | NegRespSectionsSectionVisitedFlag | — |

### [[negotiationresprequirementpvo|NegotiationRespRequirementPVO]] (PO · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegRespSectionsAuctionHeaderId1 | — |
| BID_NUMBER | NegRespSectionsBidNumber1 | ✅ |
| CREATED_BY | NegRespSectionsCreatedBy1 | — |
| CREATION_DATE | NegRespSectionsCreationDate1 | — |
| LAST_UPDATE_DATE | NegRespSectionsLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | NegRespSectionsLastUpdateLogin1 | — |
| LAST_UPDATED_BY | NegRespSectionsLastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | NegRespSectionsObjectVersionNumber1 | — |
| SECTION_ID | NegRespSectionsSectionId1 | ✅ |
| SECTION_VISITED_FLAG | NegRespSectionsSectionVisitedFlag | — |

---

## 📚 Referências

- [Oracle Docs — PON_BID_SECTIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponbidsections.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
