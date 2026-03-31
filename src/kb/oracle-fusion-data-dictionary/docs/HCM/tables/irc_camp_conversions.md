---
id: DOC-HCM-452
doc_type: system-doc
title: "IRC_CAMP_CONVERSIONS — Conversoes de Campanhas de Recrutamento"
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
  - campaign-conversions
  - irc-recruiting
aliases:
  - IRC_CAMP_CONVERSIONS
  - irc_camp_conversions
  - camp-conversions
  - camp-conversions-hcm
  - irc-camp-conversions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_CONVERSIONS

## Visao Geral

Registra as **conversoes** geradas por campanhas de recrutamento. Cada registro representa uma acao de conversao atribuida a uma campanha.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreamento de conversoes:** Monitora candidatos que passaram por etapas-chave.
- **ROI de campanhas:** Base para calcular retorno sobre investimento.
- **Funil de recrutamento:** Analise de taxa de conversao por campanha.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMP_CONVERSION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da conversao | — | 🟢 90% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Referencia a campanha | IRC_CAMPAIGNS_B | 🟢 90% |
| 3 | CONVERSION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de conversao | — | 🟡 70% |
| 4 | CONVERSION_DATE | DATE | NULL | Dados | Data da conversao | — | 🟡 75% |
| 5 | CANDIDATE_ID | NUMBER(18) | NULL | FK | Referencia ao candidato | IRC_CANDIDATES | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID`
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato da conversao de campanha)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Conversoes por campanha
```sql
SELECT cc.CONVERSION_TYPE, COUNT(*) AS total
FROM   IRC_CAMP_CONVERSIONS cc
WHERE  cc.CAMPAIGN_ID = :p_campaign_id
GROUP BY cc.CONVERSION_TYPE;
```

### Filtros comuns
- `CAMPAIGN_ID = :id` — Filtrar por campanha
- `CONVERSION_TYPE = :tipo` — Filtrar por tipo
---

## Observacoes

- Fundamental para relatorios de eficacia de campanhas.
- Cada conversao pode estar associada a um candidato.
---

## Referencias

- [Oracle Docs -- IRC_CAMP_CONVERSIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampconversions.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[campconverapplypvo|CampConverApplyPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAMPAIGN_ID | CampconversionPEOCampaignId | — |
| CONVERSION_ID | ConversionId | ✅ |
| CREATED_BY | CampconversionPEOCreatedBy | — |
| CREATION_DATE | CampconversionPEOCreationDate | — |
| GOAL_ID | CampconversionPEOGoalId | — |
| GOAL_TYPE_CODE | CampconversionPEOGoalTypeCode | — |
| LAST_UPDATE_DATE | CampconversionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CampconversionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CampconversionPEOLastUpdatedBy | — |
| OBJECT_ID | CampconversionPEOObjectId | — |
| OBJECT_VERSION_NUMBER | CampconversionPEOObjectVersionNumber | — |

### [[campconverreferpvo|CampConverReferPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAMPAIGN_ID | CampConversionPEOCampaignId | — |
| CONVERSION_ID | ConversionId | ✅ |
| CREATED_BY | CampConversionPEOCreatedBy | — |
| CREATION_DATE | CampConversionPEOCreationDate | — |
| GOAL_ID | CampConversionPEOGoalId | — |
| GOAL_TYPE_CODE | CampConversionPEOGoalTypeCode | — |
| LAST_UPDATE_DATE | CampConversionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CampConversionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CampConversionPEOLastUpdatedBy | — |
| OBJECT_ID | CampConversionPEOObjectId | — |
| OBJECT_VERSION_NUMBER | CampConversionPEOObjectVersionNumber | — |
