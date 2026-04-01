---
id: DOC-PO-034
doc_type: system-doc
title: "PON_REQUIREMENT_SECTIONS — Seções de Requisitos de Negociação"
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
  - negociacao
  - secoes
  - requisitos
aliases:
  - PON_REQUIREMENT_SECTIONS
  - pon_requirement_sections
  - secoes-requisitos-sourcing
  - requirement-sections
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_REQUIREMENT_SECTIONS

## Visão Geral

Armazena as **seções (agrupamentos)** de requisitos em processos de negociação do módulo Oracle Sourcing. Cada registro representa uma seção lógica que organiza requisitos relacionados (ex.: "Requisitos Técnicos", "Requisitos Comerciais", "Compliance") dentro de uma negociação, facilitando a estruturação e avaliação das propostas.

> [!note] Módulo PON
> O prefixo `PON` identifica tabelas do submódulo **Oracle Sourcing / Negotiations**. As seções permitem organizar hierarquicamente os requisitos de uma RFQ, RFI ou leilão.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Organização de requisitos:** Agrupamento lógico de requisitos por tema (técnico, comercial, compliance).
- **Estruturação de RFQ/RFI:** Criação de seções que estruturam o documento de solicitação enviado aos fornecedores.
- **Ponderação por seção:** Atribuição de pesos por grupo de requisitos na avaliação consolidada.
- **Apresentação estruturada:** Exibição organizada de requisitos para fornecedores e avaliadores.
- **Templates de negociação:** Reutilização de estruturas de seções em negociações futuras.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟡 75% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Negociação/leilão ao qual a seção pertence | [[pon_auction_headers_all]] | 🟡 75% |
| 3 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da seção (ex.: "Requisitos Técnicos") | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada da seção | — | 🟡 70% |
| 5 | SECTION_ORDER | NUMBER | NULL | Controle | Ordem de exibição da seção | — | 🟡 70% |
| 6 | WEIGHT | NUMBER | NULL | Avaliação | Peso da seção na avaliação total (percentual) | — | 🟡 65% |
| 7 | PARENT_SECTION_ID | NUMBER(18) | NULL | FK | Seção-pai para hierarquias aninhadas | [[pon_requirement_sections]] | 🟡 55% |
| 8 | INTERNAL_FLAG | VARCHAR2(1) | NULL | Flag | Indica se a seção é interna/não visível ao fornecedor (Y/N) | — | 🟡 55% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual a seção de requisitos pertence)
- [[pon_requirement_sections]] — via `PARENT_SECTION_ID` (auto-referência para hierarquia)

### Tabelas-filha (FK de saída)
- [[pon_requirements]] — via `SECTION_ID` (requisitos da seção)
- [[pon_requirement_sections]] — via `PARENT_SECTION_ID` (subseções)

---

## Uso Típico

### Listar seções de uma negociação com peso
```sql
SELECT s.SECTION_NAME, s.DESCRIPTION, s.WEIGHT,
       s.SECTION_ORDER, s.INTERNAL_FLAG
FROM   PON_REQUIREMENT_SECTIONS s
WHERE  s.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY s.SECTION_ORDER;
```

### Seções com contagem de requisitos
```sql
SELECT s.SECTION_NAME, s.WEIGHT,
       COUNT(r.REQUIREMENT_ID) AS qtd_requisitos
FROM   PON_REQUIREMENT_SECTIONS s
       LEFT JOIN PON_REQUIREMENTS r ON s.SECTION_ID = r.SECTION_ID
WHERE  s.AUCTION_HEADER_ID = :p_auction_header_id
GROUP BY s.SECTION_NAME, s.WEIGHT
ORDER BY s.SECTION_ORDER;
```

---

## Observações

- O campo `WEIGHT` define o peso relativo da seção na avaliação global — a soma dos pesos de todas as seções geralmente totaliza 100%.
- A coluna `PARENT_SECTION_ID` permite hierarquias de seções (ex.: "Técnico > Hardware > Servidores"), embora na prática a maioria das implementações use apenas um nível.
- Seções com `INTERNAL_FLAG = 'Y'` não são visíveis para fornecedores — usadas para avaliações internas do comprador.
- A ordem de exibição é controlada por `SECTION_ORDER`, que deve ser mantida consistente para boa experiência do usuário.

---

## Referências

- [Oracle Docs — PON_REQUIREMENT_SECTIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponrequirementsections.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[negotiationrequirementandscoringpvo|NegotiationRequirementAndScoringPVO]] (PO · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegotiationSectionAuctionHeaderId | — |
| CREATED_BY | NegotiationSectionCreatedBy | — |
| CREATION_DATE | NegotiationSectionCreationDate | — |
| DISP_SEQ_NUMBER | NegotiationSectionDispSeqNumber | ✅ |
| IS_INTERNAL | NegotiationSectionIsInternal | — |
| LAST_AMENDMENT_UPDATE | NegotiationSectionLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationSectionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationSectionLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationSectionLastUpdatedBy | — |
| MODIFIED_FLAG | NegotiationSectionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | NegotiationSectionObjectVersionNumber | — |
| PREVIOUS_SECTION_ID | NegotiationSectionPreviousSectionId | — |
| SECTION_DISPLAY_NUMBER | NegotiationSectionSectionDisplayNumber | ✅ |
| SECTION_ID | NegotiationSectionSectionId | ✅ |
| SECTION_LEVEL | NegotiationSectionSectionLevel | — |
| SECTION_NAME | NegotiationSectionSectionName | ✅ |
| TWO_PART_SECTION_TYPE | NegotiationSectionTwoPartSectionType | ✅ |

### [[negotiationrequirementpvo|NegotiationRequirementPVO]] (PO · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegotiationSectionAuctionHeaderId | — |
| CREATED_BY | NegotiationSectionCreatedBy | — |
| CREATION_DATE | NegotiationSectionCreationDate | — |
| DISP_SEQ_NUMBER | NegotiationSectionDispSeqNumber | ✅ |
| IS_INTERNAL | NegotiationSectionIsInternal | — |
| LAST_AMENDMENT_UPDATE | NegotiationSectionLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationSectionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationSectionLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationSectionLastUpdatedBy | — |
| MODIFIED_FLAG | NegotiationSectionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | NegotiationSectionObjectVersionNumber | — |
| PREVIOUS_SECTION_ID | NegotiationSectionPreviousSectionId | — |
| SECTION_DISPLAY_NUMBER | NegotiationSectionSectionDisplayNumber | ✅ |
| SECTION_ID | NegotiationSectionSectionId | ✅ |
| SECTION_LEVEL | NegotiationSectionSectionLevel | — |
| SECTION_NAME | NegotiationSectionSectionName | ✅ |
| TWO_PART_SECTION_TYPE | NegotiationSectionTwoPartSectionType | ✅ |

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegotiationSectionsAuctionHeaderId1 | — |
| CREATED_BY | NegotiationSectionsCreatedBy1 | — |
| CREATION_DATE | NegotiationSectionsCreationDate1 | — |
| DISP_SEQ_NUMBER | NegotiationSectionsDispSeqNumber | ✅ |
| IS_INTERNAL | NegotiationSectionsIsInternal | — |
| LAST_AMENDMENT_UPDATE | NegotiationSectionsLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationSectionsLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | NegotiationSectionsLastUpdateLogin1 | — |
| LAST_UPDATED_BY | NegotiationSectionsLastUpdatedBy1 | — |
| MODIFIED_FLAG | NegotiationSectionsModifiedFlag | — |
| OBJECT_VERSION_NUMBER | NegotiationSectionsObjectVersionNumber1 | — |
| PREVIOUS_SECTION_ID | NegotiationSectionsPreviousSectionId | — |
| SECTION_DISPLAY_NUMBER | NegotiationSectionsSectionDisplayNumber | ✅ |
| SECTION_ID | NegotiationSectionsSectionId | ✅ |
| SECTION_LEVEL | NegotiationSectionsSectionLevel | — |
| SECTION_NAME | NegotiationSectionsSectionName | ✅ |
| TWO_PART_SECTION_TYPE | NegotiationSectionsTwoPartSectionType | ✅ |

### [[negotiationresprequirementpvo|NegotiationRespRequirementPVO]] (PO · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | NegotiationSectionsAuctionHeaderId2 | — |
| CREATED_BY | NegotiationSectionsCreatedBy2 | — |
| CREATION_DATE | NegotiationSectionsCreationDate2 | — |
| DISP_SEQ_NUMBER | NegotiationSectionsDispSeqNumber | ✅ |
| IS_INTERNAL | NegotiationSectionsIsInternal | — |
| LAST_AMENDMENT_UPDATE | NegotiationSectionsLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationSectionsLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | NegotiationSectionsLastUpdateLogin2 | — |
| LAST_UPDATED_BY | NegotiationSectionsLastUpdatedBy2 | — |
| MODIFIED_FLAG | NegotiationSectionsModifiedFlag | — |
| OBJECT_VERSION_NUMBER | NegotiationSectionsObjectVersionNumber2 | — |
| PREVIOUS_SECTION_ID | NegotiationSectionsPreviousSectionId | — |
| SECTION_DISPLAY_NUMBER | NegotiationSectionsSectionDisplayNumber | ✅ |
| SECTION_ID | NegotiationSectionsSectionId2 | ✅ |
| SECTION_LEVEL | NegotiationSectionsSectionLevel | — |
| SECTION_NAME | NegotiationSectionsSectionName | ✅ |
| TWO_PART_SECTION_TYPE | NegotiationSectionsTwoPartSectionType | ✅ |

### [[negotiationsectionextractpvo|NegotiationSectionExtractPVO]] (PO · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISP_SEQ_NUMBER | DispSeqNumber | ✅ |
| IS_INTERNAL | IsInternal | ✅ |
| LAST_AMENDMENT_UPDATE | LastAmendmentUpdate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODIFIED_FLAG | ModifiedFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PREVIOUS_SECTION_ID | PreviousSectionId | ✅ |
| SECTION_DISPLAY_NUMBER | SectionDisplayNumber | ✅ |
| SECTION_ID | SectionId | ✅ |
| SECTION_LEVEL | SectionLevel | ✅ |
| SECTION_NAME | SectionName | ✅ |
| TWO_PART_SECTION_TYPE | TwoPartSectionType | ✅ |
