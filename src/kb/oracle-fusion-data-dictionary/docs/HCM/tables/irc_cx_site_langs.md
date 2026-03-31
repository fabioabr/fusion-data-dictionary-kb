---
id: DOC-HCM-474
doc_type: system-doc
title: "IRC_CX_SITE_LANGS — Idiomas de Sites de Carreiras"
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
  - site-languages
  - irc-recruiting
aliases:
  - IRC_CX_SITE_LANGS
  - irc_cx_site_langs
  - cx-site-langs
  - cx-site-hcm
  - irc-cx-site-langs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_SITE_LANGS

## Visao Geral

**Idiomas habilitados** para cada career site.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao multilingue:** Define idiomas suportados.
- **Experiencia:** Portal disponivel nos idiomas necessarios.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_SITE_LANG_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CX_SITE_ID | NUMBER(18) | NOT NULL | FK | Site | IRC_CX_SITES_B | 🟢 90% |
| 3 | LANGUAGE_CODE | VARCHAR2(4) | NOT NULL | Dados | Idioma habilitado | — | 🟢 90% |
| 4 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Classificacao | Idioma padrao (Y/N) | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cx_sites_b]] — via `CX_SITE_ID` (site de carreiras do idioma configurado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Idiomas de um site
```sql
SELECT sl.LANGUAGE_CODE, sl.DEFAULT_FLAG
FROM   IRC_CX_SITE_LANGS sl
WHERE  sl.CX_SITE_ID = :p_site_id;
```

### Filtros comuns
- `DEFAULT_FLAG = 'Y'` — Idioma padrao
---

## Observacoes

- Multiplos idiomas por site.
---

## Referencias

- [Oracle Docs -- IRC_CX_SITE_LANGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxsitelangs.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[careersitelanguagepvo|CareerSiteLanguagePVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SITE_ID | SiteId | ✅ |
| SITE_LANGUAGE | SiteLanguage | ✅ |
