---
id: DOC-HCM-478
doc_type: system-doc
title: "IRC_DESCRIPTIONS_B — Descricoes de Recrutamento (Base)"
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
  - descriptions
  - irc-recruiting
aliases:
  - IRC_DESCRIPTIONS_B
  - irc_descriptions_b
  - descriptions-b
  - descriptions-b-hcm
  - irc-descriptions-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_DESCRIPTIONS_B

## Visao Geral

**Descricoes** reutilizaveis para recrutamento. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Padronizacao:** Descricoes reutilizaveis para vagas.
- **Versionamento:** Via IRC_DESC_VERSIONS_B.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESCRIPTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | DESCRIPTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de descricao | — | 🟡 75% |
| 3 | DESCRIPTION_CODE | VARCHAR2(30) | NULL | Identificacao | Codigo | — | 🟡 70% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Descricoes ativas
```sql
SELECT d.DESCRIPTION_ID, d.DESCRIPTION_TYPE, d.DESCRIPTION_CODE
FROM   IRC_DESCRIPTIONS_B d WHERE d.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Ativas
---

## Observacoes

- Tabela base (_B).
- Versionamento por IRC_DESC_VERSIONS_B.
---

## Referencias

- [Oracle Docs -- IRC_DESCRIPTIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircdescriptionsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
