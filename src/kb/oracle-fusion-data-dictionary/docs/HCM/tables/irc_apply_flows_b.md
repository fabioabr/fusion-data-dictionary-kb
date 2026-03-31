---
id: DOC-HCM-436
doc_type: system-doc
title: "IRC_APPLY_FLOWS_B — Fluxos de Candidatura (Base)"
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
  - apply-flow
  - fluxo-candidatura
  - base
aliases:
  - IRC_APPLY_FLOWS_B
  - irc_apply_flows_b
  - irc-apply-flows-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_APPLY_FLOWS_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de fluxos de candidatura** (Apply Flows) do modulo Recruiting (IRC). Cada fluxo define a experiencia completa do candidato ao se candidatar a uma vaga.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Definicao de fluxos:** configura o processo completo de candidatura online.
- **Personalizacao:** permite diferentes fluxos para diferentes tipos de vaga.
- **Experiencia do candidato:** controla toda a jornada de candidatura.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLY_FLOW_ID | NUMBER(18) | NOT NULL | PK | Identificador do fluxo | — | 🟡 70% |
| 2 | FLOW_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do fluxo | — | 🟡 65% |
| 3 | FLOW_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do fluxo | — | 🟡 60% |
| 4 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Controle | Fluxo padrao (Y/N) | — | 🟡 55% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_apply_flows_tl]] — via `APPLY_FLOW_ID` (traducoes do fluxo de candidatura)
- [[irc_af_versions]] — via `APPLY_FLOW_ID` (traducoes do fluxo de candidatura)

---

## 📎 Uso Tipico

### Listar fluxos de candidatura ativos
```sql
SELECT f.APPLY_FLOW_ID, f.FLOW_CODE, f.FLOW_TYPE, f.DEFAULT_FLAG
FROM   IRC_APPLY_FLOWS_B f
WHERE  f.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Fluxos ativos`
- `DEFAULT_FLAG = 'Y' — Fluxo padrao`
- `FLOW_TYPE = :p_type — Por tipo`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_APPLY_FLOWS_TL.
- Define a experiencia de candidatura de ponta a ponta.
- Cada fluxo pode ter multiplas versoes (IRC_AF_VERSIONS).

---

## 📚 Referencias

- [Oracle Docs — IRC_APPLY_FLOWS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircapplyflowsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[applyflowpvo|ApplyFlowPVO]] (HCM · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AF_CODE | ApplyFlowBPEOAfCode | ✅ |
| AF_STATUS_CODE | ApplyFlowBPEOAfStatusCode | — |
| AF_TYPE_CODE | ApplyFlowBPEOAfTypeCode | — |
| APPLY_FLOW_ID | ApplyFlowId | ✅ |
| CREATED_BY | ApplyFlowBPEOCreatedBy | — |
| CREATION_DATE | ApplyFlowBPEOCreationDate | — |
| LAST_UPDATE_DATE | ApplyFlowBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApplyFlowBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApplyFlowBPEOLastUpdatedBy | — |

### [[applyflowversionpvo|ApplyFlowVersionPVO]] (HCM · BICC: 5/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AF_CODE | ApplyFlowBPEOAfCode | ✅ |
| AF_STATUS_CODE | ApplyFlowBPEOAfStatusCode | ✅ |
| AF_TYPE_CODE | ApplyFlowBPEOAfTypeCode | ✅ |
| APPLY_FLOW_ID | ApplyFlowBPEOApplyFlowId | ✅ |
| CREATED_BY | ApplyFlowBPEOCreatedBy | — |
| CREATION_DATE | ApplyFlowBPEOCreationDate | — |
| LAST_UPDATE_DATE | ApplyFlowBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApplyFlowBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApplyFlowBPEOLastUpdatedBy | — |
