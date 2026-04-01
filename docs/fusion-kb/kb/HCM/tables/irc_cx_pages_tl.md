---
id: DOC-HCM-471
doc_type: system-doc
title: "IRC_CX_PAGES_TL — Paginas do Career Site (Traducoes)"
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
  - cx-pages-tl
  - irc-recruiting
aliases:
  - IRC_CX_PAGES_TL
  - irc_cx_pages_tl
  - cx-pages-tl
  - cx-pages-hcm
  - irc-cx-pages-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_PAGES_TL

## Visao Geral

Traducoes das paginas do career site. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Titulos e descricoes multilingues.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_PAGE_ID | NUMBER(18) | NOT NULL | PK/FK | Pagina base | IRC_CX_PAGES_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | PAGE_TITLE | VARCHAR2(240) | NULL | Dados | Titulo traduzido | — | 🟡 80% |
| 5 | PAGE_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cx_pages_b]] — via `CX_PAGE_ID` (registro base da pagina do site)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Titulos em portugues
```sql
SELECT tl.PAGE_TITLE, tl.PAGE_DESCRIPTION
FROM   IRC_CX_PAGES_TL tl
WHERE  tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: CX_PAGE_ID + LANGUAGE.
---

## Referencias

- [Oracle Docs -- IRC_CX_PAGES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxpagestl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[careersitepagepvo|CareerSitePagePVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SitePageTranslationPEOCreatedBy | — |
| CREATION_DATE | SitePageTranslationPEOCreationDate | — |
| LANGUAGE | SitePageTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | SitePageTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SitePageTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SitePageTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber6 | — |
| OG_DESCRIPTION | SitePageTranslationPEOOgDescription | — |
| OG_IMAGE_SRC | SitePageTranslationPEOOgImageSrc | — |
| PAGE_ID | PageId1 | — |
| SEO_DESCRIPTION | SitePageTranslationPEOSeoDescription | — |
| SOURCE_LANG | SitePageTranslationPEOSourceLang | — |
| TITLE | SitePageTranslationPEOTitle | ✅ |
