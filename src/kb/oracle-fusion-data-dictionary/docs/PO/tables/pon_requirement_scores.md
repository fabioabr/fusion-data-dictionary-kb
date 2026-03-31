---
id: DOC-PO-033
doc_type: system-doc
title: "PON_REQUIREMENT_SCORES — Pontuações de Requisitos de Negociação"
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
  - scoring
  - avaliacao
aliases:
  - PON_REQUIREMENT_SCORES
  - pon_requirement_scores
  - pontuacoes-requisitos-sourcing
  - requirement-scores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_REQUIREMENT_SCORES

## Visão Geral

Armazena as **pontuações atribuídas** a cada requisito de negociação por avaliador/fornecedor no módulo Oracle Sourcing. Cada registro representa a nota dada por um membro da equipe de avaliação a um requisito específico de uma proposta de fornecedor, permitindo o cálculo de scores consolidados para classificação.

> [!note] Módulo PON
> O prefixo `PON` identifica tabelas do submódulo **Oracle Sourcing / Negotiations**. Esta tabela é central no processo de avaliação de propostas em RFQs, RFIs e leilões.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação de propostas:** Registro das notas atribuídas por cada avaliador a cada requisito.
- **Ranking de fornecedores:** Base para cálculo do score consolidado ponderado por pesos dos requisitos.
- **Transparência do processo:** Permite auditoria das avaliações individuais de cada membro da equipe.
- **Análise comparativa:** Comparação de desempenho de fornecedores por requisito.
- **Compliance de sourcing:** Evidência de avaliação objetiva e rastreável.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCORE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pontuação | — | 🟡 70% |
| 2 | REQUIREMENT_ID | NUMBER(18) | NOT NULL | FK | Requisito avaliado | [[pon_requirements]] | 🟡 75% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Negociação/leilão relacionado | [[pon_auction_headers_all]] | 🟡 75% |
| 4 | BID_NUMBER | NUMBER(18) | NULL | FK | Número da proposta do fornecedor | [[pon_bid_headers]] | 🟡 65% |
| 5 | SCORING_MEMBER_ID | NUMBER(18) | NULL | FK | Membro da equipe que atribuiu a nota | [[pon_program_team_members]] | 🟡 60% |
| 6 | SCORE | NUMBER | NULL | Avaliação | Pontuação atribuída ao requisito (escala definida pela negociação) | — | 🟡 75% |
| 7 | MAX_SCORE | NUMBER | NULL | Avaliação | Pontuação máxima possível para o requisito | — | 🟡 60% |
| 8 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Justificativa/comentário do avaliador | — | 🟡 65% |
| 9 | SUPPLIER_RESPONSE | VARCHAR2(4000) | NULL | Texto livre | Resposta do fornecedor ao requisito | — | 🟡 60% |
| 10 | WEIGHTED_SCORE | NUMBER | NULL | Avaliação | Pontuação ponderada pelo peso do requisito | — | 🟡 55% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_requirements]] — via `REQUIREMENT_ID` (requisito avaliado)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação à qual a pontuação de requisito pertence)
- [[pon_bid_headers]] — via `BID_NUMBER` (proposta do fornecedor)
- [[pon_program_team_members]] — via `SCORING_MEMBER_ID` (membro avaliador que atribuiu a pontuação)

### Tabelas-filha (FK de saída)
- Sem tabelas-filha conhecidas diretamente.

---

## Uso Típico

### Scores de um fornecedor por requisito
```sql
SELECT r.REQUIREMENT_NAME, rs.SCORE, rs.MAX_SCORE,
       rs.WEIGHTED_SCORE, rs.COMMENTS
FROM   PON_REQUIREMENT_SCORES rs
       JOIN PON_REQUIREMENTS r ON rs.REQUIREMENT_ID = r.REQUIREMENT_ID
WHERE  rs.AUCTION_HEADER_ID = :p_auction_header_id
  AND  rs.BID_NUMBER = :p_bid_number
ORDER BY r.SEQUENCE_NUMBER;
```

### Score consolidado por fornecedor
```sql
SELECT rs.BID_NUMBER,
       SUM(rs.WEIGHTED_SCORE) AS score_total,
       COUNT(*) AS requisitos_avaliados
FROM   PON_REQUIREMENT_SCORES rs
WHERE  rs.AUCTION_HEADER_ID = :p_auction_header_id
GROUP BY rs.BID_NUMBER
ORDER BY score_total DESC;
```

---

## Observações

- O `WEIGHTED_SCORE` é tipicamente calculado como `(SCORE / MAX_SCORE) * WEIGHT` do requisito associado.
- Quando há múltiplos avaliadores (`SCORING_MEMBER_ID`), a pontuação final pode ser a média ou consenso, dependendo da configuração da negociação.
- O campo `SUPPLIER_RESPONSE` armazena a resposta literal do fornecedor, permitindo auditoria independente da nota atribuída.
- Esta tabela é filha de [[pon_requirements]] e referencia [[pon_bid_headers]] para associar scores a propostas específicas.

---

## Referências

- [Oracle Docs — PON_REQUIREMENT_SCORES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponrequirementscores.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[negotiationrequirementandscoringpvo|NegotiationRequirementAndScoringPVO]] (PO · BICC: 17/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | NegotiationRequirementScoreAccResponseId | — |
| ACC_RESPONSE_ID | ParentRequirementScoreAccResponseId | — |
| ALLOW_ATTACHMENT_CODE | NegotiationRequirementScoreAllowAttachmentCode | ✅ |
| ALLOW_ATTACHMENT_CODE | ParentRequirementScoreAllowAttachmentCode | — |
| AUCTION_HEADER_ID | NegotiationRequirementScoreAuctionHeaderId | — |
| AUCTION_HEADER_ID | ParentRequirementScoreAuctionHeaderId | — |
| CREATED_BY | NegotiationRequirementScoreCreatedBy | — |
| CREATED_BY | ParentRequirementScoreCreatedBy | — |
| CREATION_DATE | NegotiationRequirementScoreCreationDate | — |
| CREATION_DATE | ParentRequirementScoreCreationDate | — |
| DATE_FROM_RANGE | NegotiationRequirementScoreDateFromRange | ✅ |
| DATE_FROM_RANGE | ParentRequirementScoreDateFromRange | — |
| DATE_TO_RANGE | NegotiationRequirementScoreDateToRange | ✅ |
| DATE_TO_RANGE | ParentRequirementScoreDateToRange | — |
| DATETIME_FROM_RANGE | NegotiationRequirementScoreDatetimeFromRange | ✅ |
| DATETIME_FROM_RANGE | ParentRequirementScoreDatetimeFromRange | — |
| DATETIME_TO_RANGE | NegotiationRequirementScoreDatetimeToRange | ✅ |
| DATETIME_TO_RANGE | ParentRequirementScoreDatetimeToRange | — |
| DISP_SEQ_NUMBER | NegotiationRequirementScoreDispSeqNumber | ✅ |
| DISP_SEQ_NUMBER | ParentRequirementScoreDispSeqNumber | ✅ |
| IS_DEFAULT_SCORE_ROW | NegotiationRequirementScoreIsDefaultScoreRow | ✅ |
| IS_DEFAULT_SCORE_ROW | ParentRequirementScoreIsDefaultScoreRow | — |
| LAST_UPDATE_DATE | NegotiationRequirementScoreLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentRequirementScoreLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NegotiationRequirementScoreLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ParentRequirementScoreLastUpdateLogin | — |
| LAST_UPDATED_BY | NegotiationRequirementScoreLastUpdatedBy | — |
| LAST_UPDATED_BY | ParentRequirementScoreLastUpdatedBy | — |
| NUMBER_FROM_RANGE | NegotiationRequirementScoreNumberFromRange | ✅ |
| NUMBER_FROM_RANGE | ParentRequirementScoreNumberFromRange | — |
| NUMBER_TO_RANGE | NegotiationRequirementScoreNumberToRange | ✅ |
| NUMBER_TO_RANGE | ParentRequirementScoreNumberToRange | — |
| OBJECT_VERSION_NUMBER | NegotiationRequirementScoreObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ParentRequirementScoreObjectVersionNumber | — |
| PREVIOUS_SCORE_ID | NegotiationRequirementScorePreviousScoreId | — |
| PREVIOUS_SCORE_ID | ParentRequirementScorePreviousScoreId | — |
| REQUIREMENT_ID | NegotiationRequirementScoreRequirementId | — |
| REQUIREMENT_ID | ParentRequirementScoreRequirementId | — |
| SCORE | NegotiationRequirementScoreScore | ✅ |
| SCORE | ParentRequirementScoreScore | — |
| SCORE_DISPLAY_NUMBER | NegotiationRequirementScoreScoreDisplayNumber | ✅ |
| SCORE_DISPLAY_NUMBER | ParentRequirementScoreScoreDisplayNumber | — |
| SCORE_ID | ParentRequirementScoreScoreId | — |
| SCORE_ID | ScoreId | ✅ |
| SCORE_LEVEL | NegotiationRequirementScoreScoreLevel | — |
| SCORE_LEVEL | ParentRequirementScoreScoreLevel | — |
| TARGET_FLAG | NegotiationRequirementScoreTargetFlag | ✅ |
| TARGET_FLAG | ParentRequirementScoreTargetFlag | — |
| TEXT_VALUE | NegotiationRequirementScoreTextValue | ✅ |
| TEXT_VALUE | ParentRequirementScoreTextValue | — |

### [[negotiationrequirementpvo|NegotiationRequirementPVO]] (PO · BICC: 2/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | ParentRequirementScoreAccResponseId | — |
| ALLOW_ATTACHMENT_CODE | ParentRequirementScoreAllowAttachmentCode | — |
| AUCTION_HEADER_ID | ParentRequirementScoreAuctionHeaderId | — |
| CREATED_BY | ParentRequirementScoreCreatedBy | — |
| CREATION_DATE | ParentRequirementScoreCreationDate | — |
| DATE_FROM_RANGE | ParentRequirementScoreDateFromRange | — |
| DATE_TO_RANGE | ParentRequirementScoreDateToRange | — |
| DATETIME_FROM_RANGE | ParentRequirementScoreDatetimeFromRange | — |
| DATETIME_TO_RANGE | ParentRequirementScoreDatetimeToRange | — |
| DISP_SEQ_NUMBER | ParentRequirementScoreDispSeqNumber | ✅ |
| IS_DEFAULT_SCORE_ROW | ParentRequirementScoreIsDefaultScoreRow | — |
| LAST_UPDATE_DATE | ParentRequirementScoreLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ParentRequirementScoreLastUpdateLogin | — |
| LAST_UPDATED_BY | ParentRequirementScoreLastUpdatedBy | — |
| NUMBER_FROM_RANGE | ParentRequirementScoreNumberFromRange | — |
| NUMBER_TO_RANGE | ParentRequirementScoreNumberToRange | — |
| OBJECT_VERSION_NUMBER | ParentRequirementScoreObjectVersionNumber | — |
| PREVIOUS_SCORE_ID | ParentRequirementScorePreviousScoreId | — |
| REQUIREMENT_ID | ParentRequirementScoreRequirementId | — |
| SCORE | ParentRequirementScoreScore | — |
| SCORE_DISPLAY_NUMBER | ParentRequirementScoreScoreDisplayNumber | — |
| SCORE_ID | ParentRequirementScoreScoreId | — |
| SCORE_LEVEL | ParentRequirementScoreScoreLevel | — |
| TARGET_FLAG | ParentRequirementScoreTargetFlag | — |
| TEXT_VALUE | ParentRequirementScoreTextValue | — |

### [[negotiationresprequirementandvaluespvo|NegotiationRespRequirementAndValuesPVO]] (PO · BICC: 3/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | NegotiationScoresAccResponseId | — |
| ALLOW_ATTACHMENT_CODE | NegotiationScoresAllowAttachmentCode1 | — |
| AUCTION_HEADER_ID | NegotiationScoresAuctionHeaderId3 | — |
| CREATED_BY | NegotiationScoresCreatedBy3 | — |
| CREATION_DATE | NegotiationScoresCreationDate3 | — |
| DATE_FROM_RANGE | NegotiationScoresDateFromRange | — |
| DATE_TO_RANGE | NegotiationScoresDateToRange | — |
| DATETIME_FROM_RANGE | NegotiationScoresDatetimeFromRange | — |
| DATETIME_TO_RANGE | NegotiationScoresDatetimeToRange | — |
| DISP_SEQ_NUMBER | NegotiationScoresDispSeqNumber2 | — |
| IS_DEFAULT_SCORE_ROW | NegotiationScoresIsDefaultScoreRow | — |
| LAST_UPDATE_DATE | NegotiationScoresLastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | NegotiationScoresLastUpdateLogin3 | — |
| LAST_UPDATED_BY | NegotiationScoresLastUpdatedBy3 | — |
| NUMBER_FROM_RANGE | NegotiationScoresNumberFromRange | — |
| NUMBER_TO_RANGE | NegotiationScoresNumberToRange | — |
| OBJECT_VERSION_NUMBER | NegotiationScoresObjectVersionNumber3 | — |
| PREVIOUS_SCORE_ID | NegotiationScoresPreviousScoreId | — |
| REQUIREMENT_ID | NegotiationScoresRequirementId2 | — |
| SCORE | NegotiationScoresScore | — |
| SCORE_DISPLAY_NUMBER | NegotiationScoresScoreDisplayNumber | — |
| SCORE_ID | NegotiationScoresScoreId2 | ✅ |
| SCORE_LEVEL | NegotiationScoresScoreLevel | — |
| TARGET_FLAG | NegotiationScoresTargetFlag | — |
| TEXT_VALUE | NegotiationScoresTextValue2 | ✅ |
