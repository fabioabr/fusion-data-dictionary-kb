---
id: DOC-HCM-457
doc_type: system-doc
title: "IRC_CAMP_REQUISITIONS — Requisicoes Vinculadas a Campanhas"
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
  - campaign-requisitions
  - irc-recruiting
aliases:
  - IRC_CAMP_REQUISITIONS
  - irc_camp_requisitions
  - camp-requisitions
  - camp-requisitions-hcm
  - irc-camp-requisitions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_REQUISITIONS

## Visao Geral

Armazena a associacao entre **campanhas** e **requisicoes de vaga**. Tabela associativa N:N.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Vinculacao campanha-vaga:** Associa requisicoes a campanhas.
- **Rastreabilidade:** Quais vagas foram divulgadas por qual campanha.
- **ROI por vaga:** Eficacia de campanha por requisicao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Referencia a campanha | IRC_CAMPAIGNS_B | 🟢 90% |
| 3 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Referencia a requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID`
- [[irc_requisitions_b]] — via `REQUISITION_ID` (requisicao vinculada a campanha)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Requisicoes de uma campanha
```sql
SELECT cr.REQUISITION_ID
FROM   IRC_CAMP_REQUISITIONS cr
WHERE  cr.CAMPAIGN_ID = :p_campaign_id;
```

### Filtros comuns
- `CAMPAIGN_ID = :id` — Por campanha
---

## Observacoes

- Tabela associativa N:N entre campanhas e requisicoes.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_REQUISITIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccamprequisitions.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
