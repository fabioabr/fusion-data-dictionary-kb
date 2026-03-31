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

---

## 🔗 PVOs Relacionados

### [[regulatoryresponsepvo|RegulatoryResponsePVO]] (HCM · BICC: 18/90)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOMMODATION_REQUEST | RegulatoryResponsePEOAccommodationRequest | ✅ |
| ATTRIBUTE_1 | RegulatoryResponsePEOAttribute1 | ✅ |
| ATTRIBUTE_10 | RegulatoryResponsePEOAttribute10 | — |
| ATTRIBUTE_11 | RegulatoryResponsePEOAttribute11 | — |
| ATTRIBUTE_12 | RegulatoryResponsePEOAttribute12 | — |
| ATTRIBUTE_13 | RegulatoryResponsePEOAttribute13 | — |
| ATTRIBUTE_14 | RegulatoryResponsePEOAttribute14 | — |
| ATTRIBUTE_15 | RegulatoryResponsePEOAttribute15 | — |
| ATTRIBUTE_16 | RegulatoryResponsePEOAttribute16 | — |
| ATTRIBUTE_17 | RegulatoryResponsePEOAttribute17 | — |
| ATTRIBUTE_18 | RegulatoryResponsePEOAttribute18 | — |
| ATTRIBUTE_19 | RegulatoryResponsePEOAttribute19 | — |
| ATTRIBUTE_2 | RegulatoryResponsePEOAttribute2 | ✅ |
| ATTRIBUTE_20 | RegulatoryResponsePEOAttribute20 | — |
| ATTRIBUTE_21 | RegulatoryResponsePEOAttribute21 | — |
| ATTRIBUTE_22 | RegulatoryResponsePEOAttribute22 | — |
| ATTRIBUTE_23 | RegulatoryResponsePEOAttribute23 | — |
| ATTRIBUTE_24 | RegulatoryResponsePEOAttribute24 | — |
| ATTRIBUTE_25 | RegulatoryResponsePEOAttribute25 | — |
| ATTRIBUTE_26 | RegulatoryResponsePEOAttribute26 | — |
| ATTRIBUTE_27 | RegulatoryResponsePEOAttribute27 | — |
| ATTRIBUTE_28 | RegulatoryResponsePEOAttribute28 | — |
| ATTRIBUTE_29 | RegulatoryResponsePEOAttribute29 | — |
| ATTRIBUTE_3 | RegulatoryResponsePEOAttribute3 | ✅ |
| ATTRIBUTE_30 | RegulatoryResponsePEOAttribute30 | — |
| ATTRIBUTE_4 | RegulatoryResponsePEOAttribute4 | ✅ |
| ATTRIBUTE_5 | RegulatoryResponsePEOAttribute5 | ✅ |
| ATTRIBUTE_6 | RegulatoryResponsePEOAttribute6 | ✅ |
| ATTRIBUTE_7 | RegulatoryResponsePEOAttribute7 | ✅ |
| ATTRIBUTE_8 | RegulatoryResponsePEOAttribute8 | ✅ |
| ATTRIBUTE_9 | RegulatoryResponsePEOAttribute9 | — |
| ATTRIBUTE_DATE_1 | RegulatoryResponsePEOAttributeDate1 | ✅ |
| ATTRIBUTE_DATE_10 | RegulatoryResponsePEOAttributeDate10 | — |
| ATTRIBUTE_DATE_2 | RegulatoryResponsePEOAttributeDate2 | ✅ |
| ATTRIBUTE_DATE_3 | RegulatoryResponsePEOAttributeDate3 | — |
| ATTRIBUTE_DATE_4 | RegulatoryResponsePEOAttributeDate4 | — |
| ATTRIBUTE_DATE_5 | RegulatoryResponsePEOAttributeDate5 | — |
| ATTRIBUTE_DATE_6 | RegulatoryResponsePEOAttributeDate6 | — |
| ATTRIBUTE_DATE_7 | RegulatoryResponsePEOAttributeDate7 | — |
| ATTRIBUTE_DATE_8 | RegulatoryResponsePEOAttributeDate8 | — |
| ATTRIBUTE_DATE_9 | RegulatoryResponsePEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER_1 | RegulatoryResponsePEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER_10 | RegulatoryResponsePEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER_11 | RegulatoryResponsePEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER_12 | RegulatoryResponsePEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER_13 | RegulatoryResponsePEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER_14 | RegulatoryResponsePEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER_15 | RegulatoryResponsePEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER_16 | RegulatoryResponsePEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER_17 | RegulatoryResponsePEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER_18 | RegulatoryResponsePEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER_19 | RegulatoryResponsePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER_2 | RegulatoryResponsePEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER_20 | RegulatoryResponsePEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER_3 | RegulatoryResponsePEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER_4 | RegulatoryResponsePEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER_5 | RegulatoryResponsePEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER_6 | RegulatoryResponsePEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER_7 | RegulatoryResponsePEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER_8 | RegulatoryResponsePEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER_9 | RegulatoryResponsePEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP_1 | RegulatoryResponsePEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP_10 | RegulatoryResponsePEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP_2 | RegulatoryResponsePEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP_3 | RegulatoryResponsePEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP_4 | RegulatoryResponsePEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP_5 | RegulatoryResponsePEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP_6 | RegulatoryResponsePEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP_7 | RegulatoryResponsePEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP_8 | RegulatoryResponsePEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP_9 | RegulatoryResponsePEOAttributeTimestamp9 | — |
| CREATED_BY | CreatedBy | — |
| CREATED_BY | RegulatoryResponsePEOCreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| CREATION_DATE | RegulatoryResponsePEOCreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_DATE | RegulatoryResponsePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | RegulatoryResponsePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LAST_UPDATED_BY | RegulatoryResponsePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | RegulatoryResponseDFFPEOLegislationCode | — |
| LEGISLATION_CODE | RegulatoryResponsePEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | RegulatoryResponsePEOObjectVersionNumber | — |
| PER_INFORMATION_CATEGORY | PerInformationCategory | — |
| PERSON_ID | RegulatoryResponsePEOPersonId | — |
| RESPONSE_ID | RegulatoryResponseDFFPEOResponseId | — |
| RESPONSE_ID | ResponseId | ✅ |
| SUBMISSION_ID | RegulatoryResponsePEOSubmissionId | — |
