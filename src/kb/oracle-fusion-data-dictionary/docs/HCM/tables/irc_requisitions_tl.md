---
id: DOC-HCM-523
doc_type: system-doc
title: "IRC_REQUISITIONS_TL — Requisicoes de Vaga (Traducoes)"
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
  - requisitions-tl
  - irc-recruiting
aliases:
  - IRC_REQUISITIONS_TL
  - irc_requisitions_tl
  - requisitions-tl
  - requisitions-tl-hcm
  - irc-requisitions-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQUISITIONS_TL

## Visao Geral

Traducoes das requisicoes. Tabela `_TL` com titulo e descricao multilingues.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Publicacao multilingue:** Vagas em multiplos idiomas.
- **Career site:** Titulo traduzido por idioma.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_ID | NUMBER(18) | NOT NULL | PK/FK | Requisicao base | IRC_REQUISITIONS_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | REQUISITION_TITLE | VARCHAR2(240) | NULL | Dados | Titulo traduzido | — | 🟢 85% |
| 5 | REQUISITION_DESCRIPTION | CLOB | NULL | Dados | Descricao traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] — via `REQUISITION_ID` (registro base da requisicao de vaga)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Titulos de vagas abertas em portugues
```sql
SELECT b.REQUISITION_NUMBER, tl.REQUISITION_TITLE
FROM   IRC_REQUISITIONS_B b
JOIN   IRC_REQUISITIONS_TL tl ON tl.REQUISITION_ID = b.REQUISITION_ID
WHERE  tl.LANGUAGE = 'PT' AND b.REQUISITION_STATUS = 'OPEN';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- REQUISITION_DESCRIPTION e CLOB — pode conter HTML.
---

## Referencias

- [Oracle Docs -- IRC_REQUISITIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircrequisitionstl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
