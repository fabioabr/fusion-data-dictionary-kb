---
id: DOC-HCM-435
doc_type: system-doc
title: "IRC_AGENT_REQUISITIONS — Requisicoes de Agentes de Recrutamento"
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
  - irc
  - agent
  - requisicao
  - agencia-recrutamento
aliases:
  - IRC_AGENT_REQUISITIONS
  - irc_agent_requisitions
  - irc-agent-requisitions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AGENT_REQUISITIONS

## 📌 Visao Geral

Armazena as **associacoes entre agentes de recrutamento e requisicoes** de vaga do modulo Recruiting (IRC). Permite rastrear quais agencias/recrutadores externos estao trabalhando em cada vaga.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de agencias:** rastreia quais agentes trabalham em cada requisicao.
- **Controle de acesso:** define quais vagas estao disponiveis para cada agencia.
- **Metricas de sourcing:** permite medir eficiencia por agente de recrutamento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AGENT_REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador da associacao | — | 🟡 70% |
| 2 | AGENT_ID | NUMBER(18) | NOT NULL | FK | Agente de recrutamento | — | 🟡 65% |
| 3 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao de vaga | — | 🟡 70% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da associacao | — | 🟡 65% |
| 5 | ASSIGNED_DATE | DATE | NULL | Periodo | Data da atribuicao | — | 🟡 60% |
| 6 | EXPIRY_DATE | DATE | NULL | Periodo | Data de expiracao | — | 🟡 55% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Requisicoes atribuidas a um agente
```sql
SELECT ar.REQUISITION_ID, ar.STATUS, ar.ASSIGNED_DATE
FROM   IRC_AGENT_REQUISITIONS ar
WHERE  ar.AGENT_ID = :p_agent_id
  AND  ar.STATUS = 'ACTIVE';
```

### Filtros comuns
- `AGENT_ID = :p_agent_id — Por agente`
- `REQUISITION_ID = :p_req_id — Por requisicao`
- `STATUS = 'ACTIVE' — Associacoes ativas`

---

## 🔒 Observacoes

- Vincula agentes de recrutamento externo a requisicoes de vaga.
- Utilizada para controle de sourcing e calculo de fees de agencia.

---

## 📚 Referencias

- [Oracle Docs — IRC_AGENT_REQUISITIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircagentrequisitions.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
