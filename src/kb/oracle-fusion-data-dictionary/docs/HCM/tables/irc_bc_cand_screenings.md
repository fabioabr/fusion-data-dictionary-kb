---
id: DOC-HCM-445
doc_type: system-doc
title: "IRC_BC_CAND_SCREENINGS — Triagens de Background Check de Candidatos"
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
  - triagem
  - screening
aliases:
  - IRC_BC_CAND_SCREENINGS
  - irc_bc_cand_screenings
  - irc-bc-cand-screenings
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_BC_CAND_SCREENINGS

## 📌 Visao Geral

Armazena as **triagens de verificacao de antecedentes** (background check screenings) solicitadas para candidatos do modulo Recruiting (IRC).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Solicitacao de verificacao:** registra solicitacoes de background check.
- **Rastreamento:** acompanha o status de cada triagem solicitada.
- **Integracao:** gerencia comunicacao com fornecedores de screening.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCREENING_ID | NUMBER(18) | NOT NULL | PK | Identificador da triagem | — | 🟡 70% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato | — | 🟡 65% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | Requisicao de vaga | — | 🟡 60% |
| 4 | SCREENING_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de screening | — | 🟡 60% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da triagem | — | 🟡 65% |
| 6 | REQUEST_DATE | TIMESTAMP | NULL | Periodo | Data da solicitacao | — | 🟡 60% |
| 7 | PARTNER_ID | NUMBER(18) | NULL | FK | Parceiro de screening | — | 🟡 55% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_bc_cand_results]] — via `SCREENING_ID` (resultados da triagem de antecedentes)

---

## 📎 Uso Tipico

### Triagens pendentes de background check
```sql
SELECT s.SCREENING_ID, s.CANDIDATE_ID, s.SCREENING_TYPE,
       s.STATUS, s.REQUEST_DATE
FROM   IRC_BC_CAND_SCREENINGS s
WHERE  s.STATUS = 'PENDING';
```

### Filtros comuns
- `STATUS = 'PENDING' — Triagens pendentes`
- `CANDIDATE_ID = :p_candidate_id — Por candidato`
- `SCREENING_TYPE = :p_type — Por tipo`

---

## 🔒 Observacoes

- Gerencia solicitacoes de background check para candidatos.
- Status tipicos: PENDING, IN_PROGRESS, COMPLETED, CANCELLED.
- Dados sensiveis — sujeitos a politicas de privacidade.

---

## 📚 Referencias

- [Oracle Docs — IRC_BC_CAND_SCREENINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircbccandscreenings.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
