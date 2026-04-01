---
id: DOC-HCM-535
doc_type: system-doc
title: "IRC_SEARCH_ACTION_DETAILS — Detalhes de Acoes de Pesquisa"
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
  - search-action-details
  - detalhes
  - irc-action-details
aliases:
  - IRC_SEARCH_ACTION_DETAILS
  - irc_search_action_details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SEARCH_ACTION_DETAILS

## 📌 Visão Geral

Armazena os **detalhes granulares** de cada acao de pesquisa executada no Recruiting. Complementa `IRC_SEARCH_ACTIONS` com informacoes adicionais sobre o contexto da acao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Detalhamento de acoes de sourcing
- Rastreamento completo do ciclo pesquisa-acao-resultado
- Auditoria detalhada de interacoes de recrutamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do detalhe | --- | 🟢 85% |
| 2 | SEARCH_ACTION_ID | NUMBER(18) | NOT NULL | FK | ID da acao associada | IRC_SEARCH_ACTIONS | 🟢 85% |
| 3 | DETAIL_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de detalhe | --- | 🟡 65% |
| 4 | DETAIL_VALUE | VARCHAR2(2000) | NULL | Dados | Valor do detalhe | --- | 🟡 65% |
| 5 | CANDIDATE_ID | NUMBER(18) | NULL | FK | ID do candidato envolvido | IRC_CANDIDATES | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_search_actions]] --- via `SEARCH_ACTION_ID` (acao de busca do detalhe)

### Tabelas-filha (FK de saída)
- --- Tabela de detalhe, sem filhas conhecidas

---

## 📎 Uso Típico

### Detalhes de uma acao de pesquisa
```sql
SELECT sad.ACTION_DETAIL_ID, sad.DETAIL_TYPE, sad.DETAIL_VALUE
FROM   IRC_SEARCH_ACTION_DETAILS sad
WHERE  sad.SEARCH_ACTION_ID = :p_action_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[searchactiondetailpvo|SearchActionDetailPVO]] (PO · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DETAIL_ID | ActionDetailId | ✅ |
| ACTION_ID | SearchActionDetailPEOActionId | — |
| CREATED_BY | SearchActionDetailPEOCreatedBy | — |
| CREATION_DATE | SearchActionDetailPEOCreationDate | — |
| LAST_UPDATE_DATE | SearchActionDetailPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SearchActionDetailPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SearchActionDetailPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SearchActionDetailPEOObjectVersionNumber | — |
| SEARCH_ID | SearchActionDetailPEOSearchId | — |
| SELECTED_ENTITY_ID | SearchActionDetailPEOSelectedEntityId | ✅ |
| TARGET_ENTITY_ID | SearchActionDetailPEOTargetEntityId | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_SEARCH_ACTION_DETAILS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsearchactiondetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
