---
id: DOC-PO-032
doc_type: system-doc
title: "PON_REQUIREMENTS — Requisitos de Negociação"
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
  - requisitos
aliases:
  - PON_REQUIREMENTS
  - pon_requirements
  - requisitos-negociacao-sourcing
  - pon-requirements
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_REQUIREMENTS

## Visão Geral

Armazena os **requisitos** definidos em processos de negociação (sourcing negotiations) no módulo Oracle Sourcing. Cada registro representa um requisito técnico, comercial ou funcional que os fornecedores devem atender ao participar de uma negociação (RFQ, RFI, leilão). Os requisitos são organizados em seções e podem ser avaliados/pontuados.

> [!note] Módulo PON
> O prefixo `PON` identifica tabelas do submódulo **Oracle Sourcing / Negotiations**, que gerencia processos competitivos de aquisição com fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de critérios de avaliação:** Especificação dos requisitos técnicos e comerciais que fornecedores devem atender.
- **RFQ/RFI/Leilão:** Estruturação dos critérios de participação e avaliação em processos competitivos.
- **Scoring de fornecedores:** Base para pontuação e classificação de propostas recebidas.
- **Compliance de fornecedores:** Verificação de conformidade com requisitos obrigatórios.
- **Histórico de negociações:** Rastreamento dos critérios utilizados em cada processo de sourcing.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUIREMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do requisito | — | 🟡 75% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Identificador da negociação/leilão | [[pon_auction_headers_all]] | 🟡 75% |
| 3 | SECTION_ID | NUMBER(18) | NULL | FK | Seção à qual o requisito pertence | [[pon_requirement_sections]] | 🟡 70% |
| 4 | REQUIREMENT_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do requisito (TECHNICAL, COMMERCIAL, INTERNAL) | — | 🟡 70% |
| 5 | REQUIREMENT_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome/título do requisito | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada do requisito | — | 🟡 75% |
| 7 | DISPLAY_TARGET_FLAG | VARCHAR2(1) | NULL | Flag | Indica se o valor-alvo é exibido ao fornecedor (Y/N) | — | 🟡 60% |
| 8 | SCORING_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de pontuação (MANUAL, AUTOMATIC, RANGE) | — | 🟡 65% |
| 9 | WEIGHT | NUMBER | NULL | Avaliação | Peso do requisito na avaliação total | — | 🟡 70% |
| 10 | TARGET_VALUE | VARCHAR2(4000) | NULL | Avaliação | Valor-alvo esperado para o requisito | — | 🟡 60% |
| 11 | SEQUENCE_NUMBER | NUMBER | NULL | Controle | Ordem de exibição do requisito | — | 🟡 70% |
| 12 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se o requisito é obrigatório (Y/N) | — | 🟡 65% |
| 13 | RESPONSE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de resposta esperada (TEXT, NUMBER, DATE, LOV) | — | 🟡 60% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação/leilão)
- [[pon_requirement_sections]] — via `SECTION_ID` (seção do requisito)

### Tabelas-filha (FK de saída)
- [[pon_requirement_scores]] — via `REQUIREMENT_ID` (pontuações do requisito)

### Tabelas relacionadas no contexto Sourcing

---

## Uso Típico

### Listar requisitos de uma negociação com peso
```sql
SELECT r.REQUIREMENT_NAME, r.REQUIREMENT_TYPE,
       r.WEIGHT, r.MANDATORY_FLAG, r.SCORING_TYPE,
       rs.SECTION_NAME
FROM   PON_REQUIREMENTS r
       LEFT JOIN PON_REQUIREMENT_SECTIONS rs
         ON r.SECTION_ID = rs.SECTION_ID
WHERE  r.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY r.SEQUENCE_NUMBER;
```

### Requisitos obrigatórios de uma negociação
```sql
SELECT r.REQUIREMENT_NAME, r.DESCRIPTION, r.TARGET_VALUE
FROM   PON_REQUIREMENTS r
WHERE  r.AUCTION_HEADER_ID = :p_auction_header_id
  AND  r.MANDATORY_FLAG = 'Y'
ORDER BY r.SEQUENCE_NUMBER;
```

---

## Observações

- O campo `WEIGHT` define o peso relativo do requisito na avaliação geral — a soma dos pesos dentro de uma seção geralmente totaliza 100.
- O `SCORING_TYPE` determina se a pontuação é atribuída manualmente pelo avaliador ou calculada automaticamente com base na resposta do fornecedor.
- Requisitos com `MANDATORY_FLAG = 'Y'` são eliminatórios — fornecedores que não os atendam podem ser desqualificados.
- O `RESPONSE_TYPE` controla o formato de entrada da resposta do fornecedor (texto livre, numérico, data, lista de valores).
- A tabela trabalha em conjunto com [[pon_requirement_sections]] (agrupamento) e [[pon_requirement_scores]] (pontuações individuais).

---

## Referências

- [Oracle Docs — PON_REQUIREMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponrequirements.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[negotiationrequirementandscoringpvo|NegotiationRequirementAndScoringPVO]] (PO · BICC: 26/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSOLUTE_SECTION_SEQUENCE | NegotiationRequirementAbsoluteSectionSequence | ✅ |
| ALLOW_ATTACHMENT_CODE | NegotiationRequirementAllowAttachmentCode | ✅ |
| ALLOW_COMMENTS | NegotiationRequirementAllowComments | ✅ |
| AUCTION_HEADER_ID | NegotiationRequirementAuctionHeaderId | — |
| CATEGORY_CODE | NegotiationRequirementCategoryCode | — |
| CREATED_BY | NegotiationRequirementCreatedBy | ✅ |
| CREATION_DATE | NegotiationRequirementCreationDate | ✅ |
| DATATYPE | NegotiationRequirementDatatype | ✅ |
| DATE_VALUE | NegotiationRequirementDateValue | ✅ |
| DATETIME_VALUE | NegotiationRequirementDatetimeValue | ✅ |
| DISP_SEQ_NUMBER | NegotiationRequirementDispSeqNumber | — |
| DISPLAY_TARGET_FLAG | NegotiationRequirementDisplayTargetFlag | ✅ |
| HINT | NegotiationRequirementHint | ✅ |
| IS_QUESTION_BRANCH | NegotiationRequirementIsQuestionBranch | — |
| KNOCKOUT_SCORE | NegotiationRequirementKnockoutScore | ✅ |
| LAST_AMENDMENT_UPDATE | NegotiationRequirementLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationRequirementLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationRequirementLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationRequirementLastUpdatedBy | — |
| MAX_SCORE | NegotiationRequirementMaxScore | ✅ |
| MODIFIED_DATE | NegotiationRequirementModifiedDate | — |
| MODIFIED_FLAG | NegotiationRequirementModifiedFlag | — |
| NUMBER_VALUE | NegotiationRequirementNumberValue | ✅ |
| OBJECT_VERSION_NUMBER | NegotiationRequirementObjectVersionNumber | — |
| PARENT_LEVEL | NegotiationRequirementParentLevel | — |
| PARENT_REQUIREMENT_ID | NegotiationRequirementParentRequirementId | — |
| PREVIOUS_REQUIREMENT_ID | NegotiationRequirementPreviousRequirementId | — |
| QUESTION_ID | NegotiationRequirementQuestionId | ✅ |
| REQ_DISPLAY_NUMBER | NegotiationRequirementReqDisplayNumber | ✅ |
| REQUIREMENT_ID | NegotiationRequirementRequirementId | ✅ |
| REQUIREMENT_NAME | NegotiationRequirementRequirementName | ✅ |
| REQUIREMENT_TEXT | NegotiationRequirementRequirementText | ✅ |
| REQUIREMENT_TREE_LEVEL | NegotiationRequirementRequirementTreeLevel | — |
| REQUIREMENT_TYPE | NegotiationRequirementRequirementType | ✅ |
| RESPONSE_TYPE | NegotiationRequirementResponseType | ✅ |
| REVISION_NUMBER | NegotiationRequirementRevisionNumber | ✅ |
| ROOT_REQUIREMENT_ID | NegotiationRequirementRootRequirementId | — |
| SCORE_ID | NegotiationRequirementScoreId | — |
| SCORING_METHOD | NegotiationRequirementScoringMethod | ✅ |
| SCORING_TYPE | NegotiationRequirementScoringType | — |
| SECTION_ID | NegotiationRequirementSectionId | — |
| SEQUENCE_NUMBER | NegotiationRequirementSequenceNumber | — |
| SUPPLIER_LEVEL | NegotiationRequirementSupplierLevel | ✅ |
| TEXT_VALUE | NegotiationRequirementTextValue | ✅ |
| WEIGHT | NegotiationRequirementWeight | ✅ |

### [[negotiationrequirementextractpvo|NegotiationRequirementExtractPVO]] (PO · BICC: 45/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSOLUTE_SECTION_SEQUENCE | AbsoluteSectionSequence | ✅ |
| ALLOW_ATTACHMENT_CODE | AllowAttachmentCode | ✅ |
| ALLOW_COMMENTS | AllowComments | ✅ |
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| CATEGORY_CODE | CategoryCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATATYPE | Datatype | ✅ |
| DATE_VALUE | DateValue | ✅ |
| DATETIME_VALUE | DatetimeValue | ✅ |
| DISP_SEQ_NUMBER | DispSeqNumber | ✅ |
| DISPLAY_TARGET_FLAG | DisplayTargetFlag | ✅ |
| HINT | Hint | ✅ |
| IS_QUESTION_BRANCH | IsQuestionBranch | ✅ |
| KNOCKOUT_SCORE | KnockoutScore | ✅ |
| LAST_AMENDMENT_UPDATE | LastAmendmentUpdate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MAX_SCORE | MaxScore | ✅ |
| MODIFIED_DATE | ModifiedDate | ✅ |
| MODIFIED_FLAG | ModifiedFlag | ✅ |
| NUMBER_VALUE | NumberValue | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PARENT_LEVEL | ParentLevel | ✅ |
| PARENT_REQUIREMENT_ID | ParentRequirementId | ✅ |
| PREVIOUS_REQUIREMENT_ID | PreviousRequirementId | ✅ |
| QUESTION_ID | QuestionId | ✅ |
| REQ_DISPLAY_NUMBER | ReqDisplayNumber | ✅ |
| REQUIREMENT_ID | RequirementId | ✅ |
| REQUIREMENT_NAME | RequirementName | ✅ |
| REQUIREMENT_TEXT | RequirementText | ✅ |
| REQUIREMENT_TREE_LEVEL | RequirementTreeLevel | ✅ |
| REQUIREMENT_TYPE | RequirementType | ✅ |
| RESPONSE_TYPE | ResponseType | ✅ |
| REVISION_NUMBER | RevisionNumber | ✅ |
| ROOT_REQUIREMENT_ID | RootRequirementId | ✅ |
| SCORE_ID | ScoreId | ✅ |
| SCORING_METHOD | ScoringMethod | ✅ |
| SCORING_TYPE | ScoringType | ✅ |
| SECTION_ID | SectionId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| SUPPLIER_LEVEL | SupplierLevel | ✅ |
| TEXT_VALUE | TextValue | ✅ |
| WEIGHT | Weight | ✅ |

### [[negotiationrequirementpvo|NegotiationRequirementPVO]] (PO · BICC: 26/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSOLUTE_SECTION_SEQUENCE | NegotiationRequirementAbsoluteSectionSequence | ✅ |
| ALLOW_ATTACHMENT_CODE | NegotiationRequirementAllowAttachmentCode | ✅ |
| ALLOW_COMMENTS | NegotiationRequirementAllowComments | ✅ |
| AUCTION_HEADER_ID | NegotiationRequirementAuctionHeaderId | — |
| CATEGORY_CODE | NegotiationRequirementCategoryCode | — |
| CREATED_BY | NegotiationRequirementCreatedBy | ✅ |
| CREATION_DATE | NegotiationRequirementCreationDate | ✅ |
| DATATYPE | NegotiationRequirementDatatype | ✅ |
| DATE_VALUE | NegotiationRequirementDateValue | ✅ |
| DATETIME_VALUE | NegotiationRequirementDatetimeValue | ✅ |
| DISP_SEQ_NUMBER | NegotiationRequirementDispSeqNumber | — |
| DISPLAY_TARGET_FLAG | NegotiationRequirementDisplayTargetFlag | ✅ |
| HINT | NegotiationRequirementHint | ✅ |
| IS_QUESTION_BRANCH | NegotiationRequirementIsQuestionBranch | — |
| KNOCKOUT_SCORE | NegotiationRequirementKnockoutScore | ✅ |
| LAST_AMENDMENT_UPDATE | NegotiationRequirementLastAmendmentUpdate | — |
| LAST_UPDATE_DATE | NegotiationRequirementLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationRequirementLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationRequirementLastUpdatedBy | — |
| MAX_SCORE | NegotiationRequirementMaxScore | ✅ |
| MODIFIED_DATE | NegotiationRequirementModifiedDate | — |
| MODIFIED_FLAG | NegotiationRequirementModifiedFlag | — |
| NUMBER_VALUE | NegotiationRequirementNumberValue | ✅ |
| OBJECT_VERSION_NUMBER | NegotiationRequirementObjectVersionNumber | — |
| PARENT_LEVEL | NegotiationRequirementParentLevel | — |
| PARENT_REQUIREMENT_ID | NegotiationRequirementParentRequirementId | — |
| PREVIOUS_REQUIREMENT_ID | NegotiationRequirementPreviousRequirementId | — |
| QUESTION_ID | NegotiationRequirementQuestionId | ✅ |
| REQ_DISPLAY_NUMBER | NegotiationRequirementReqDisplayNumber | ✅ |
| REQUIREMENT_ID | RequirementId | ✅ |
| REQUIREMENT_NAME | NegotiationRequirementRequirementName | ✅ |
| REQUIREMENT_TEXT | NegotiationRequirementRequirementText | ✅ |
| REQUIREMENT_TREE_LEVEL | NegotiationRequirementRequirementTreeLevel | — |
| REQUIREMENT_TYPE | NegotiationRequirementRequirementType | ✅ |
| RESPONSE_TYPE | NegotiationRequirementResponseType | ✅ |
| REVISION_NUMBER | NegotiationRequirementRevisionNumber | ✅ |
| ROOT_REQUIREMENT_ID | NegotiationRequirementRootRequirementId | — |
| SCORE_ID | NegotiationRequirementScoreId | — |
| SCORING_METHOD | NegotiationRequirementScoringMethod | ✅ |
| SCORING_TYPE | NegotiationRequirementScoringType | — |
| SECTION_ID | NegotiationRequirementSectionId | — |
| SEQUENCE_NUMBER | NegotiationRequirementSequenceNumber | — |
| SUPPLIER_LEVEL | NegotiationRequirementSupplierLevel | ✅ |
| TEXT_VALUE | NegotiationRequirementTextValue | ✅ |
| WEIGHT | NegotiationRequirementWeight | ✅ |

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 13/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSOLUTE_SECTION_SEQUENCE | NegotiationRequirementAbsoluteSectionSequence | ✅ |
| ALLOW_ATTACHMENT_CODE | NegotiationRequirementAllowAttachmentCode | — |
| ALLOW_COMMENTS | NegotiationRequirementAllowComments | — |
| AUCTION_HEADER_ID | NegotiationRequirementAuctionHeaderId2 | — |
| CATEGORY_CODE | NegotiationRequirementCategoryCode | — |
| CREATED_BY | NegotiationRequirementCreatedBy2 | — |
| CREATION_DATE | NegotiationRequirementCreationDate2 | — |
| DATATYPE | NegotiationRequirementDatatype | ✅ |
| DATE_VALUE | NegotiationRequirementDateValue1 | — |
| DATETIME_VALUE | NegotiationRequirementDatetimeValue1 | — |
| DISP_SEQ_NUMBER | NegotiationRequirementDispSeqNumber1 | — |
| DISPLAY_TARGET_FLAG | NegotiationRequirementDisplayTargetFlag | — |
| HINT | NegotiationRequirementHint | — |
| IS_QUESTION_BRANCH | NegotiationRequirementIsQuestionBranch | — |
| KNOCKOUT_SCORE | NegotiationRequirementKnockoutScore | — |
| LAST_AMENDMENT_UPDATE | NegotiationRequirementLastAmendmentUpdate1 | — |
| LAST_UPDATE_DATE | NegotiationRequirementLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | NegotiationRequirementLastUpdateLogin2 | — |
| LAST_UPDATED_BY | NegotiationRequirementLastUpdatedBy2 | — |
| MAX_SCORE | NegotiationRequirementMaxScore | — |
| MODIFIED_DATE | NegotiationRequirementModifiedDate | — |
| MODIFIED_FLAG | NegotiationRequirementModifiedFlag1 | — |
| NUMBER_VALUE | NegotiationRequirementNumberValue1 | — |
| OBJECT_VERSION_NUMBER | NegotiationRequirementObjectVersionNumber2 | — |
| PARENT_LEVEL | NegotiationRequirementParentLevel | — |
| PARENT_REQUIREMENT_ID | NegotiationRequirementParentRequirementId | — |
| PREVIOUS_REQUIREMENT_ID | NegotiationRequirementPreviousRequirementId | — |
| QUESTION_ID | NegotiationRequirementQuestionId | ✅ |
| REQ_DISPLAY_NUMBER | NegotiationRequirementReqDisplayNumber | ✅ |
| REQUIREMENT_ID | NegotiationRequirementRequirementId1 | ✅ |
| REQUIREMENT_NAME | NegotiationRequirementRequirementName | ✅ |
| REQUIREMENT_TEXT | NegotiationRequirementRequirementText | ✅ |
| REQUIREMENT_TREE_LEVEL | NegotiationRequirementRequirementTreeLevel | — |
| REQUIREMENT_TYPE | NegotiationRequirementRequirementType | ✅ |
| RESPONSE_TYPE | NegotiationRequirementResponseType | ✅ |
| REVISION_NUMBER | NegotiationRequirementRevisionNumber | ✅ |
| ROOT_REQUIREMENT_ID | NegotiationRequirementRootRequirementId | — |
| SCORE_ID | NegotiationRequirementScoreId1 | — |
| SCORING_METHOD | NegotiationRequirementScoringMethod | ✅ |
| SCORING_TYPE | NegotiationRequirementScoringType | — |
| SECTION_ID | NegotiationRequirementSectionId1 | — |
| SEQUENCE_NUMBER | NegotiationRequirementSequenceNumber | — |
| SUPPLIER_LEVEL | NegotiationRequirementSupplierLevel | ✅ |
| TEXT_VALUE | NegotiationRequirementTextValue1 | — |
| WEIGHT | NegotiationRequirementWeight | — |

### [[negotiationresprequirementpvo|NegotiationRespRequirementPVO]] (PO · BICC: 13/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSOLUTE_SECTION_SEQUENCE | NegotiationRequirementAbsoluteSectionSequence | ✅ |
| ALLOW_ATTACHMENT_CODE | NegotiationRequirementAllowAttachmentCode | — |
| ALLOW_COMMENTS | NegotiationRequirementAllowComments | — |
| AUCTION_HEADER_ID | NegotiationRequirementAuctionHeaderId5 | — |
| CATEGORY_CODE | NegotiationRequirementCategoryCode | — |
| CREATED_BY | NegotiationRequirementCreatedBy5 | — |
| CREATION_DATE | NegotiationRequirementCreationDate5 | — |
| DATATYPE | NegotiationRequirementDatatype | ✅ |
| DATE_VALUE | NegotiationRequirementDateValue | — |
| DATETIME_VALUE | NegotiationRequirementDatetimeValue | — |
| DISP_SEQ_NUMBER | NegotiationRequirementDispSeqNumber1 | — |
| DISPLAY_TARGET_FLAG | NegotiationRequirementDisplayTargetFlag | — |
| HINT | NegotiationRequirementHint | — |
| IS_QUESTION_BRANCH | NegotiationRequirementIsQuestionBranch | — |
| KNOCKOUT_SCORE | NegotiationRequirementKnockoutScore | — |
| LAST_AMENDMENT_UPDATE | NegotiationRequirementLastAmendmentUpdate1 | — |
| LAST_UPDATE_DATE | NegotiationRequirementLastUpdateDate5 | ✅ |
| LAST_UPDATE_LOGIN | NegotiationRequirementLastUpdateLogin5 | — |
| LAST_UPDATED_BY | NegotiationRequirementLastUpdatedBy5 | — |
| MAX_SCORE | NegotiationRequirementMaxScore | — |
| MODIFIED_DATE | NegotiationRequirementModifiedDate | — |
| MODIFIED_FLAG | NegotiationRequirementModifiedFlag1 | — |
| NUMBER_VALUE | NegotiationRequirementNumberValue | — |
| OBJECT_VERSION_NUMBER | NegotiationRequirementObjectVersionNumber5 | — |
| PARENT_LEVEL | NegotiationRequirementParentLevel | — |
| PARENT_REQUIREMENT_ID | NegotiationRequirementParentRequirementId | — |
| PREVIOUS_REQUIREMENT_ID | NegotiationRequirementPreviousRequirementId | — |
| QUESTION_ID | NegotiationRequirementQuestionId | ✅ |
| REQ_DISPLAY_NUMBER | NegotiationRequirementReqDisplayNumber | ✅ |
| REQUIREMENT_ID | NegotiationRequirementRequirementId1 | ✅ |
| REQUIREMENT_NAME | NegotiationRequirementRequirementName | ✅ |
| REQUIREMENT_TEXT | NegotiationRequirementRequirementText | ✅ |
| REQUIREMENT_TREE_LEVEL | NegotiationRequirementRequirementTreeLevel | — |
| REQUIREMENT_TYPE | NegotiationRequirementRequirementType | ✅ |
| RESPONSE_TYPE | NegotiationRequirementResponseType | ✅ |
| REVISION_NUMBER | NegotiationRequirementRevisionNumber | ✅ |
| ROOT_REQUIREMENT_ID | NegotiationRequirementRootRequirementId | — |
| SCORE_ID | NegotiationRequirementScoreId | — |
| SCORING_METHOD | NegotiationRequirementScoringMethod | ✅ |
| SCORING_TYPE | NegotiationRequirementScoringType | — |
| SECTION_ID | NegotiationRequirementSectionId3 | — |
| SEQUENCE_NUMBER | NegotiationRequirementSequenceNumber1 | — |
| SUPPLIER_LEVEL | NegotiationRequirementSupplierLevel | ✅ |
| TEXT_VALUE | NegotiationRequirementTextValue | — |
| WEIGHT | NegotiationRequirementWeight | — |
