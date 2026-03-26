---
id: DOC-HCM-446
doc_type: system-doc
title: "IRC_BC_REQ_SP_ASSGMNTS — Atribuicoes de Provedores de Screening por Requisicao"
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
  - background-check
  - provedor-screening
  - atribuicao
aliases:
  - IRC_BC_REQ_SP_ASSGMNTS
  - irc_bc_req_sp_assgmnts
  - irc-bc-req-sp-assgmnts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_BC_REQ_SP_ASSGMNTS

## 📌 Visao Geral

Armazena as **atribuicoes de provedores de screening** (service providers) a requisicoes de vaga do modulo Recruiting (IRC). Define quais fornecedores de background check sao utilizados por requisicao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Atribuicao de provedores:** vincula fornecedores de screening a requisicoes.
- **Configuracao por vaga:** permite diferentes provedores por tipo de vaga.
- **Gestao de fornecedores:** controla quais provedores estao autorizados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador da atribuicao | — | 🟡 70% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | Requisicao de vaga | — | 🟡 70% |
| 3 | SERVICE_PROVIDER_ID | NUMBER(18) | NOT NULL | FK | Provedor de screening | — | 🟡 65% |
| 4 | SCREENING_PACKAGE_ID | NUMBER(18) | NULL | FK | Pacote de screening | — | 🟡 55% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da atribuicao | — | 🟡 60% |
| 6 | PRIORITY | NUMBER | NULL | Controle | Prioridade do provedor | — | 🟡 50% |
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

### Provedores de screening por requisicao
```sql
SELECT a.SERVICE_PROVIDER_ID, a.SCREENING_PACKAGE_ID,
       a.STATUS, a.PRIORITY
FROM   IRC_BC_REQ_SP_ASSGMNTS a
WHERE  a.REQUISITION_ID = :p_req_id;
```

### Filtros comuns
- `REQUISITION_ID = :p_req_id — Por requisicao`
- `STATUS = 'ACTIVE' — Atribuicoes ativas`

---

## 🔒 Observacoes

- Vincula provedores de background check a requisicoes de vaga.
- Permite configurar diferentes provedores e pacotes por requisicao.

---

## 📚 Referencias

- [Oracle Docs — IRC_BC_REQ_SP_ASSGMNTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircbcreqspassgmnts.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
