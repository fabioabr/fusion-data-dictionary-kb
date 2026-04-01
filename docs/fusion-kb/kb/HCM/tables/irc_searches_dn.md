---
id: DOC-HCM-533
doc_type: system-doc
title: "IRC_SEARCHES_DN — Pesquisas de Recrutamento (Desnormalizada)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - searches-dn
  - desnormalizada
  - irc-searches-dn
aliases:
  - IRC_SEARCHES_DN
  - irc_searches_dn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SEARCHES_DN

## 📌 Visão Geral

Visao **desnormalizada** da tabela de pesquisas de recrutamento. Consolida dados de pesquisas com informacoes de contexto pre-calculadas para otimizar consultas de leitura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas otimizadas de pesquisas de recrutamento
- Relatorios de atividade de sourcing
- Dashboards de produtividade de recrutadores

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SEARCH_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da pesquisa | --- | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | ID do recrutador | PER_ALL_PEOPLE_F | 🟢 85% |
| 3 | SEARCH_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da pesquisa | --- | 🟡 75% |
| 4 | SEARCH_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de pesquisa | --- | 🟡 70% |
| 5 | RESULT_COUNT | NUMBER | NULL | Dados | Quantidade de resultados encontrados | --- | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_searches]] --- via `SEARCH_ID` (busca normalizada de origem)

### Tabelas-filha (FK de saída)
- --- Visao desnormalizada, tipicamente consumida por relatorios

---

## 📎 Uso Típico

### Pesquisas desnormalizadas por recrutador
```sql
SELECT sdn.SEARCH_ID, sdn.SEARCH_NAME, sdn.RESULT_COUNT
FROM   IRC_SEARCHES_DN sdn
WHERE  sdn.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[searchpvo|SearchPVO]] (PO · BICC: 23/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SearchDNPEOCreatedBy | — |
| CREATION_DATE | SearchDNPEOCreationDate | — |
| FILTER_ASSESSMENT_PACKAGE | SearchDNPEOFilterAssessmentPackage | ✅ |
| FILTER_ASSESSMENT_PERCENTILE | SearchDNPEOFilterAssessmentPercentile | ✅ |
| FILTER_ASSESSMENT_RESULT | SearchDNPEOFilterAssessmentResult | ✅ |
| FILTER_BASIC_INFO | SearchDNPEOFilterBasicInfo | ✅ |
| FILTER_CANDIDATE_TYPE | SearchDNPEOFilterCandidateType | ✅ |
| FILTER_COMPANIES | SearchDNPEOFilterCompanies | ✅ |
| FILTER_DEGREES | SearchDNPEOFilterDegrees | ✅ |
| FILTER_EVENT | SearchDNPEOFilterEvent | — |
| FILTER_JOB | SearchDNPEOFilterJob | ✅ |
| FILTER_LABEL | SearchDNPEOFilterSearchByLabel | — |
| FILTER_LANGUAGE | SearchDNPEOFilterLanguage | ✅ |
| FILTER_LAST_UPDATED_DATE | SearchDNPEOFilterLastUpdatedDate | ✅ |
| FILTER_LICENSE | SearchDNPEOFilterLicense | ✅ |
| FILTER_LOCATIONS | SearchDNPEOFilterLocations | ✅ |
| FILTER_OPT_IN_MKT_EMAILS_PREF | SearchDNPEOFilterSearchByOptInMktEmailPref | — |
| FILTER_POOL | SearchDNPEOFilterPool | ✅ |
| FILTER_REHIRE_RECOMMENDATION | SearchDNPEOFilterRehireRecommendation | ✅ |
| FILTER_REQUISITION | SearchDNPEOFilterRequisition | — |
| FILTER_SKILL | SearchDNPEOFilterSkill | — |
| FILTER_SOURCE | SearchDNPEOFilterSource | ✅ |
| FILTER_SOURCE_MEDIUM | SearchDNPEOFilterSourceMedium | ✅ |
| FILTER_YEARS_OF_EXP | SearchDNPEOFilterYearsOfExp | ✅ |
| LAST_UPDATE_DATE | SearchDNPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchDNPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchDNPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchDNPEOObjectVersionNumber | — |
| PRECRITERIA_CAND_DETAILS | SearchDNPEOPrecriteriaCandDetails | ✅ |
| PRECRITERIA_COMPANY | SearchDNPEOPrecriteriaCompany | ✅ |
| PRECRITERIA_EDUCATION | SearchDNPEOPrecriteriaEducation | ✅ |
| PRECRITERIA_EXPERIENCE | SearchDNPEOPrecriteriaExperience | ✅ |
| PRECRITERIA_LOCATION | SearchDNPEOPrecriteriaLocation | ✅ |
| SEARCH_BY_EMAIL_FLAG | SearchDNPEOFilterSearchByEmailFlag | — |
| SEARCH_BY_PHONE_FLAG | SearchDNPEOFilterSearchByPhoneFlag | — |
| SEARCH_ID | SearchDNPEOSearchId | — |
| SEARCH_KEYWORDS | SearchDNPEOSearchKeywords | ✅ |
| SEARCHDN_ID | SearchdnId | — |

### [[searchresultpvo|SearchResultPVO]] (PO · BICC: 23/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SearchDNPEOCreatedBy | — |
| CREATION_DATE | SearchDNPEOCreationDate | — |
| FILTER_ASSESSMENT_PACKAGE | SearchDNPEOFilterAssessmentPackage | ✅ |
| FILTER_ASSESSMENT_PERCENTILE | SearchDNPEOFilterAssessmentPercentile | ✅ |
| FILTER_ASSESSMENT_RESULT | SearchDNPEOFilterAssessmentResult | ✅ |
| FILTER_BASIC_INFO | SearchDNPEOFilterBasicInfo | ✅ |
| FILTER_CANDIDATE_TYPE | SearchDNPEOFilterCandidateType | ✅ |
| FILTER_COMPANIES | SearchDNPEOFilterCompanies | ✅ |
| FILTER_DEGREES | SearchDNPEOFilterDegrees | ✅ |
| FILTER_EVENT | SearchDNPEOFilterEvent | — |
| FILTER_JOB | SearchDNPEOFilterJob | ✅ |
| FILTER_LABEL | SearchDNPEOFilterSearchByLabel | — |
| FILTER_LANGUAGE | SearchDNPEOFilterLanguage | ✅ |
| FILTER_LAST_UPDATED_DATE | SearchDNPEOFilterLastUpdatedDate | ✅ |
| FILTER_LICENSE | SearchDNPEOFilterLicense | ✅ |
| FILTER_LOCATIONS | SearchDNPEOFilterLocations | ✅ |
| FILTER_OPT_IN_MKT_EMAILS_PREF | SearchDNPEOFilterSearchByOptInMktEmailPref | — |
| FILTER_POOL | SearchDNPEOFilterPool | ✅ |
| FILTER_REHIRE_RECOMMENDATION | SearchDNPEOFilterRehireRecommendation | ✅ |
| FILTER_REQUISITION | SearchDNPEOFilterRequisition | — |
| FILTER_SKILL | SearchDNPEOFilterSkill | — |
| FILTER_SOURCE | SearchDNPEOFilterSource | ✅ |
| FILTER_SOURCE_MEDIUM | SearchDNPEOFilterSourceMedium | ✅ |
| FILTER_YEARS_OF_EXP | SearchDNPEOFilterYearsOfExp | ✅ |
| LAST_UPDATE_DATE | SearchDNPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchDNPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchDNPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchDNPEOObjectVersionNumber | — |
| PRECRITERIA_CAND_DETAILS | SearchDNPEOPrecriteriaCandDetails | ✅ |
| PRECRITERIA_COMPANY | SearchDNPEOPrecriteriaCompany | ✅ |
| PRECRITERIA_EDUCATION | SearchDNPEOPrecriteriaEducation | ✅ |
| PRECRITERIA_EXPERIENCE | SearchDNPEOPrecriteriaExperience | ✅ |
| PRECRITERIA_LOCATION | SearchDNPEOPrecriteriaLocation | ✅ |
| SEARCH_BY_EMAIL_FLAG | SearchDNPEOFilterSearchByEmailFlag | — |
| SEARCH_BY_PHONE_FLAG | SearchDNPEOFilterSearchByPhoneFlag | — |
| SEARCH_ID | SearchDNPEOSearchId | — |
| SEARCH_KEYWORDS | SearchDNPEOSearchKeywords | ✅ |
| SEARCHDN_ID | SearchdnId | — |

---

## 📚 Referências

- [Oracle Docs — IRC_SEARCHES_DN](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsearchesdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
