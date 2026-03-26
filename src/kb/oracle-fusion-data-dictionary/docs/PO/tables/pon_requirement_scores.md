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
