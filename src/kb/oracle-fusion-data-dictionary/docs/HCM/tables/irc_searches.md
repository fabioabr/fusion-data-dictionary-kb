---
id: DOC-HCM-532
doc_type: system-doc
title: "IRC_SEARCHES — Pesquisas de Recrutamento"
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
  - searches
  - pesquisas
  - irc-searches
aliases:
  - IRC_SEARCHES
  - irc_searches
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SEARCHES

## 📌 Visão Geral

Armazena as **pesquisas salvas** realizadas por recrutadores no modulo Recruiting. Registra criterios de busca utilizados para encontrar candidatos ou requisicoes.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Pesquisas salvas por recrutadores para reutilizacao
- Analise de padroes de busca de candidatos
- Otimizacao de estrategias de sourcing

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
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | ID do recrutador que criou a pesquisa | PER_ALL_PEOPLE_F | 🟢 85% |
| 3 | SEARCH_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da pesquisa salva | --- | 🟡 70% |
| 4 | SEARCH_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de pesquisa (candidato, requisicao) | --- | 🟡 70% |
| 5 | SEARCH_CRITERIA | CLOB | NULL | Dados | Criterios de busca em formato estruturado | --- | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] --- via `PERSON_ID` (recrutador que realizou a busca)

### Tabelas-filha (FK de saída)
- [[irc_search_results]] --- via `SEARCH_ID` (resultados da busca de candidatos)
- [[irc_search_actions]] --- via `SEARCH_ID` (ações realizadas na busca de candidatos)
- [[irc_searches_dn]] --- via `SEARCH_ID` (visão desnormalizada da busca de candidatos)

---

## 📎 Uso Típico

### Pesquisas salvas por recrutador
```sql
SELECT s.SEARCH_ID, s.SEARCH_NAME, s.SEARCH_TYPE
FROM   IRC_SEARCHES s
WHERE  s.PERSON_ID = :p_person_id
ORDER BY s.CREATION_DATE DESC;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[searchpvo|SearchPVO]] (PO · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_TRACKING_UPDATED | SearchPEOCandidateTrackingUpdated | — |
| CREATED_BY | SearchPEOCreatedBy | — |
| CREATION_DATE | SearchPEOCreationDate | ✅ |
| DENORMALIZATION_COMPLETED | SearchPEODenormalizationCompleted | — |
| LAST_UPDATE_DATE | SearchPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | SearchPEOOwnerPersonId | ✅ |
| SEARCH_ID | SearchId | ✅ |
| SEARCH_QUERY | SearchPEOSearchQuery | — |
| SEARCH_RESULT | SearchPEOSearchResult | — |

### [[searchresultpvo|SearchResultPVO]] (PO · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_TRACKING_UPDATED | SearchPEOCandidateTrackingUpdated | — |
| CREATED_BY | SearchPEOCreatedBy | — |
| CREATION_DATE | SearchPEOCreationDate | ✅ |
| DENORMALIZATION_COMPLETED | SearchPEODenormalizationCompleted | — |
| LAST_UPDATE_DATE | SearchPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchPEOObjectVersionNumber | — |
| OWNER_PERSON_ID | SearchPEOOwnerPersonId | ✅ |
| SEARCH_ID | SearchId | ✅ |
| SEARCH_QUERY | SearchPEOSearchQuery | — |
| SEARCH_RESULT | SearchPEOSearchResult | — |

---

## 📚 Referências

- [Oracle Docs — IRC_SEARCHES](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsearches.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
