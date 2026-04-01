---
id: DOC-HCM-536
doc_type: system-doc
title: "IRC_SEARCH_RESULTS — Resultados de Pesquisa de Recrutamento"
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
  - search-results
  - resultados
  - irc-search-results
aliases:
  - IRC_SEARCH_RESULTS
  - irc_search_results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SEARCH_RESULTS

## 📌 Visão Geral

Armazena os **resultados** retornados por pesquisas de candidatos no Recruiting. Cada registro representa um candidato encontrado em uma pesquisa especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Registro de candidatos encontrados por pesquisa
- Analise de efetividade de criterios de busca
- Pipeline de sourcing baseado em resultados de pesquisa

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SEARCH_RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do resultado | --- | 🟢 85% |
| 2 | SEARCH_ID | NUMBER(18) | NOT NULL | FK | ID da pesquisa associada | IRC_SEARCHES | 🟢 85% |
| 3 | CANDIDATE_ID | NUMBER(18) | NULL | FK | ID do candidato encontrado | IRC_CANDIDATES | 🟢 85% |
| 4 | RELEVANCE_SCORE | NUMBER | NULL | Dados | Score de relevancia do resultado | --- | 🟡 60% |
| 5 | RESULT_RANK | NUMBER | NULL | Dados | Ranking do resultado na pesquisa | --- | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_searches]] --- via `SEARCH_ID` (busca que gerou o resultado)
- [[irc_candidates]] --- via `CANDIDATE_ID` (candidato encontrado na busca)

### Tabelas-filha (FK de saída)
- --- Tabela de resultados, sem filhas conhecidas

---

## 📎 Uso Típico

### Resultados de uma pesquisa ordenados por ranking
```sql
SELECT sr.CANDIDATE_ID, sr.RELEVANCE_SCORE, sr.RESULT_RANK
FROM   IRC_SEARCH_RESULTS sr
WHERE  sr.SEARCH_ID = :p_search_id
ORDER BY sr.RESULT_RANK;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[searchresultpvo|SearchResultPVO]] (PO · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SearchResultPEOCreatedBy | — |
| CREATION_DATE | SearchResultPEOCreationDate | — |
| LAST_UPDATE_DATE | SearchResultPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchResultPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchResultPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchResultPEOObjectVersionNumber | — |
| RETRIEVED_ENTITY_ID | SearchResultPEORetrievedEntityId | ✅ |
| SEARCH_ID | SearchResultPEOSearchId | — |
| SEARCH_RESULT_ID | SearchResultId | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_SEARCH_RESULTS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsearchresults.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
