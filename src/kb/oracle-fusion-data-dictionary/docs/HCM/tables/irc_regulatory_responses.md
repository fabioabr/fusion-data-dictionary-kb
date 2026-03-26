---
id: DOC-HCM-521
doc_type: system-doc
title: "IRC_REGULATORY_RESPONSES — Respostas Regulatorias"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - regulatory-responses
  - irc-recruiting
aliases:
  - IRC_REGULATORY_RESPONSES
  - irc_regulatory_responses
  - regulatory-responses
  - regulatory-responses-hcm
  - irc-regulatory-responses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REGULATORY_RESPONSES

## Visao Geral

**Respostas regulatorias** de candidatos (EEO, diversidade, dados legais).

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Compliance:** Dados obrigatorios por legislacao.
- **Relatorios legais:** Conformidade a orgaos reguladores.
- **Diversidade:** Metricas de diversidade no pipeline.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REGULATORY_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 85% |
| 3 | REGULATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de regulacao | — | 🟡 75% |
| 4 | RESPONSE_VALUE | VARCHAR2(240) | NULL | Dados | Valor da resposta | — | 🟡 70% |
| 5 | RESPONSE_DATE | DATE | NULL | Dados | Data da resposta | — | 🟡 70% |
| 6 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificacao | Legislacao aplicavel | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato da resposta regulatoria)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Respostas por tipo
```sql
SELECT rr.REGULATION_TYPE, rr.RESPONSE_VALUE, COUNT(*) AS total
FROM   IRC_REGULATORY_RESPONSES rr
GROUP BY rr.REGULATION_TYPE, rr.RESPONSE_VALUE;
```

### Filtros comuns
- `REGULATION_TYPE = :tipo` — Por tipo
---

## Observacoes

- Dados altamente sensiveis — acesso restrito.
- Respostas voluntarias em muitas jurisdicoes.
---

## Referencias

- [Oracle Docs -- IRC_REGULATORY_RESPONSES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircregulatoryresponses.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
