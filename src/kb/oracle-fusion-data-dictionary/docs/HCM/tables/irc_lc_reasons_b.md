---
id: DOC-HCM-506
doc_type: system-doc
title: "IRC_LC_REASONS_B — Motivos do Ciclo de Vida (Base)"
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
  - lc-reasons
  - irc-recruiting
aliases:
  - IRC_LC_REASONS_B
  - irc_lc_reasons_b
  - lc-reasons-b
  - lc-reasons-hcm
  - irc-lc-reasons-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_REASONS_B

## Visao Geral

**Motivos** para transicoes no ciclo de vida. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Categorizacao:** Padroniza motivos de acoes.
- **Root cause:** Razoes mais comuns de rejeicao/desistencia.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_REASON_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | REASON_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do motivo | — | 🟡 80% |
| 3 | REASON_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de motivos | — | 🟡 70% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Motivos ativos
```sql
SELECT r.REASON_CODE FROM IRC_LC_REASONS_B r WHERE r.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela base (_B).
- Motivos configuraveis por organizacao.
---

## Referencias

- [Oracle Docs -- IRC_LC_REASONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclcreasonsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
