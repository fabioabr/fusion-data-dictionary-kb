---
id: DOC-HCM-534
doc_type: system-doc
title: "IRC_SEARCH_ACTIONS — Acoes de Pesquisa de Recrutamento"
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
  - search-actions
  - acoes-pesquisa
  - irc-search-actions
aliases:
  - IRC_SEARCH_ACTIONS
  - irc_search_actions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SEARCH_ACTIONS

## 📌 Visão Geral

Registra as **acoes** executadas a partir de resultados de pesquisa no modulo Recruiting (ex.: adicionar candidato a pipeline, enviar mensagem, agendar entrevista).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Rastreamento de acoes tomadas apos pesquisas de candidatos
- Analise de efetividade de acoes de sourcing
- Auditoria de interacoes com candidatos via pesquisa

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SEARCH_ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da acao | --- | 🟢 85% |
| 2 | SEARCH_ID | NUMBER(18) | NOT NULL | FK | ID da pesquisa associada | IRC_SEARCHES | 🟢 85% |
| 3 | ACTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de acao executada | --- | 🟡 70% |
| 4 | TARGET_ID | NUMBER(18) | NULL | FK | ID do objeto alvo da acao | --- | 🟡 65% |
| 5 | ACTION_DATE | TIMESTAMP | NULL | Dados | Data/hora da acao | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_searches]] --- via `SEARCH_ID` (busca da acao de recrutamento)

### Tabelas-filha (FK de saída)
- [[irc_search_action_details]] --- via `SEARCH_ACTION_ID` (detalhes da acao de busca)

---

## 📎 Uso Típico

### Acoes por pesquisa
```sql
SELECT sa.SEARCH_ACTION_ID, sa.ACTION_TYPE, sa.ACTION_DATE
FROM   IRC_SEARCH_ACTIONS sa
WHERE  sa.SEARCH_ID = :p_search_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_SEARCH_ACTIONS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsearchactions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
