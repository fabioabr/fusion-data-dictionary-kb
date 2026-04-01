---
id: DOC-HCM-481
doc_type: system-doc
title: "IRC_DESC_VERSIONS_TL — Versoes de Descricoes (Traducoes)"
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
  - desc-versions-tl
  - irc-recruiting
aliases:
  - IRC_DESC_VERSIONS_TL
  - irc_desc_versions_tl
  - desc-versions-tl
  - desc-versions-hcm
  - irc-desc-versions-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_DESC_VERSIONS_TL

## Visao Geral

Traducoes das versoes de descricoes. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao versionada:** Cada versao com traducoes independentes.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESC_VERSION_ID | NUMBER(18) | NOT NULL | PK/FK | Versao base | IRC_DESC_VERSIONS_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | VERSION_TEXT | CLOB | NULL | Dados | Texto traduzido | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_desc_versions_b]] — via `DESC_VERSION_ID` (registro base da versao de descricao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Texto da versao vigente em portugues
```sql
SELECT tl.VERSION_TEXT
FROM   IRC_DESC_VERSIONS_TL tl
JOIN   IRC_DESC_VERSIONS_B b ON b.DESC_VERSION_ID = tl.DESC_VERSION_ID
WHERE  tl.LANGUAGE = 'PT' AND b.VERSION_STATUS = 'CURRENT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- VERSION_TEXT e CLOB.
---

## Referencias

- [Oracle Docs -- IRC_DESC_VERSIONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircdescversionstl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[descriptionversionpvo|DescriptionVersionPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DESC_VERSION_ID | DescVersionId1 | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SHORT_DESCRIPTION | ShortDescription | ✅ |
| SOURCE_LANG | SourceLang | — |
| TXT_DESCRIPTION | DescVerTranslPEOTxtDecsription | ✅ |
