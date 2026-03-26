---
id: DOC-HCM-434
doc_type: system-doc
title: "IRC_AF_VERSIONS — Versoes de Fluxo de Candidatura"
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
  - versao
aliases:
  - IRC_AF_VERSIONS
  - irc_af_versions
  - irc-af-versions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_AF_VERSIONS

## 📌 Visao Geral

Armazena as **versoes dos fluxos de candidatura** (Apply Flow versions) do modulo Recruiting (IRC). Permite controle de versao e historico de alteracoes nos fluxos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Controle de versao:** rastreia alteracoes nos fluxos de candidatura.
- **Historico:** mantem versoes anteriores para auditoria.
- **Publicacao:** controla qual versao do fluxo esta ativa.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VERSION_ID | NUMBER(18) | NOT NULL | PK | Identificador da versao | — | 🟡 70% |
| 2 | APPLY_FLOW_ID | NUMBER(18) | NOT NULL | FK | Fluxo de candidatura | IRC_APPLY_FLOWS_B | 🟡 70% |
| 3 | VERSION_NUMBER | NUMBER | NOT NULL | Controle | Numero da versao | — | 🟡 65% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da versao (DRAFT, ACTIVE, ARCHIVED) | — | 🟡 65% |
| 5 | EFFECTIVE_START_DATE | DATE | NULL | Vigencia | Inicio da vigencia | — | 🟡 60% |
| 6 | EFFECTIVE_END_DATE | DATE | NULL | Vigencia | Fim da vigencia | — | 🟡 55% |
| 7 | PUBLISHED_DATE | TIMESTAMP | NULL | Periodo | Data de publicacao | — | 🟡 55% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_apply_flows_b]] — via `APPLY_FLOW_ID` (fluxo de candidatura da versao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Versoes de um fluxo de candidatura
```sql
SELECT v.VERSION_ID, v.VERSION_NUMBER, v.STATUS,
       v.EFFECTIVE_START_DATE, v.PUBLISHED_DATE
FROM   IRC_AF_VERSIONS v
WHERE  v.APPLY_FLOW_ID = :p_flow_id
ORDER BY v.VERSION_NUMBER DESC;
```

### Filtros comuns
- `APPLY_FLOW_ID = :p_flow_id — Por fluxo`
- `STATUS = 'ACTIVE' — Versao ativa`

---

## 🔒 Observacoes

- Controla o ciclo de vida de versoes dos fluxos de candidatura.
- Apenas uma versao pode estar ACTIVE por fluxo em dado momento.
- Versoes anteriores sao mantidas como ARCHIVED para historico.

---

## 📚 Referencias

- [Oracle Docs — IRC_AF_VERSIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircafversions.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
