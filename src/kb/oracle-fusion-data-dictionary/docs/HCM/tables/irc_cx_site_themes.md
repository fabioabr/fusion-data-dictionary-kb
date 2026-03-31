---
id: DOC-HCM-477
doc_type: system-doc
title: "IRC_CX_SITE_THEMES — Temas Visuais de Career Sites"
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
  - site-themes
  - irc-recruiting
aliases:
  - IRC_CX_SITE_THEMES
  - irc_cx_site_themes
  - cx-site-themes
  - cx-site-hcm
  - irc-cx-site-themes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_SITE_THEMES

## Visao Geral

**Temas visuais** aplicaveis aos career sites. Cores, fontes e estilos.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Branding:** Identidade visual por career site.
- **Personalizacao:** Temas customizaveis por marca.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_SITE_THEME_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | THEME_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do tema | — | 🟡 80% |
| 3 | THEME_NAME | VARCHAR2(240) | NULL | Dados | Nome do tema | — | 🟡 80% |
| 4 | PRIMARY_COLOR | VARCHAR2(30) | NULL | Configuracao | Cor primaria (hex) | — | 🟡 65% |
| 5 | SECONDARY_COLOR | VARCHAR2(30) | NULL | Configuracao | Cor secundaria (hex) | — | 🟡 65% |
| 6 | THEME_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[irc_cx_sites_b]] — via `THEME_ID` (sites de carreiras que usam o tema)

---

## Uso Tipico

### Temas ativos
```sql
SELECT t.THEME_CODE, t.THEME_NAME, t.PRIMARY_COLOR
FROM   IRC_CX_SITE_THEMES t
WHERE  t.THEME_STATUS = 'ACTIVE';
```

### Filtros comuns
- `THEME_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Cores em formato hexadecimal.
- Compartilhaveis entre sites.
---

## Referencias

- [Oracle Docs -- IRC_CX_SITE_THEMES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxsitethemes.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[careersitepagepvo|CareerSitePagePVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SiteThemePEOCreatedBy | — |
| CREATION_DATE | SiteThemePEOCreationDate | — |
| FOOTER_MODE | SiteThemePEOFooterMode | — |
| HEADER_MODE | SiteThemePEOHeaderMode | — |
| LAST_UPDATE_DATE | SiteThemePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SiteThemePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SiteThemePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SiteThemePEOObjectVersionNumber | — |
| TEMPLATE_ID | SiteThemePEOTemplateId | — |
| THEME_ID | SiteThemePEOThemeId | ✅ |
| THEME_NAME | SiteThemePEOThemeName | ✅ |
| THEME_NUMBER | SiteThemePEOThemeNumber | ✅ |

### [[careersitepvo|CareerSitePVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SiteThemePEOCreatedBy | — |
| CREATION_DATE | SiteThemePEOCreationDate | — |
| FOOTER_MODE | SiteThemePEOFooterMode | — |
| HEADER_MODE | SiteThemePEOHeaderMode | — |
| LAST_UPDATE_DATE | SiteThemePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SiteThemePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SiteThemePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SiteThemePEOObjectVersionNumber | — |
| TEMPLATE_ID | SiteThemePEOTemplateId | — |
| THEME_ID | SiteThemePEOThemeId | ✅ |
| THEME_NAME | SiteThemePEOThemeName | ✅ |
| THEME_NUMBER | SiteThemePEOThemeNumber | ✅ |
