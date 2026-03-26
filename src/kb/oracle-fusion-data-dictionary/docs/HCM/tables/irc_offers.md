---
id: DOC-HCM-513
doc_type: system-doc
title: "IRC_OFFERS — Ofertas de Emprego"
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
  - offers
  - irc-recruiting
aliases:
  - IRC_OFFERS
  - irc_offers
  - irc-offers
  - irc_offers-oracle
  - irc_offers-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_OFFERS

## Visao Geral

**Ofertas de emprego** feitas a candidatos. Termos e condicoes de proposta formal.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de ofertas:** Ciclo completo de ofertas.
- **Negociacao:** Versoes e contra-propostas.
- **Compliance:** Termos oferecidos e aceitos.
- **Metricas:** Taxa de aceite.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OFFER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | IRC_CANDIDATES | 🟢 90% |
| 3 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 4 | OFFER_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟢 85% |
| 5 | OFFER_DATE | DATE | NULL | Dados | Data da oferta | — | 🟡 80% |
| 6 | EXPIRY_DATE | DATE | NULL | Dados | Data de expiracao | — | 🟡 75% |
| 7 | PROPOSED_SALARY | NUMBER | NULL | Dados | Salario proposto | — | 🟡 70% |
| 8 | PROPOSED_START_DATE | DATE | NULL | Dados | Data inicio proposta | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato que recebeu a proposta)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao da proposta de emprego)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Ofertas aceitas
```sql
SELECT o.OFFER_ID, o.CANDIDATE_ID, o.PROPOSED_SALARY, o.OFFER_DATE
FROM   IRC_OFFERS o WHERE o.OFFER_STATUS = 'ACCEPTED'
ORDER BY o.OFFER_DATE DESC;
```

### Filtros comuns
- `OFFER_STATUS = 'ACCEPTED'` — Aceitas
---

## Observacoes

- PROPOSED_SALARY — dado sensivel.
- Tabela central para metricas de offer-to-hire.
---

## Referencias

- [Oracle Docs -- IRC_OFFERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircoffers.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
