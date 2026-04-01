---
id: DOC-HCM-475
doc_type: system-doc
title: "IRC_CX_SITE_TEMPLATES_B — Templates de Career Site (Base)"
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
  - site-templates
  - irc-recruiting
aliases:
  - IRC_CX_SITE_TEMPLATES_B
  - irc_cx_site_templates_b
  - cx-site-templates-b
  - cx-site-hcm
  - irc-cx-site-templates-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_SITE_TEMPLATES_B

## Visao Geral

**Templates** para configuracao de career sites. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Padronizacao visual:** Templates reutilizaveis.
- **Agilidade:** Novos sites a partir de templates.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_SITE_TEMPLATE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | TEMPLATE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do template | — | 🟡 80% |
| 3 | TEMPLATE_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 75% |
| 4 | TEMPLATE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de template | — | 🟡 70% |
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

### Templates ativos
```sql
SELECT st.CX_SITE_TEMPLATE_ID, st.TEMPLATE_CODE, st.TEMPLATE_TYPE
FROM   IRC_CX_SITE_TEMPLATES_B st
WHERE  st.TEMPLATE_STATUS = 'ACTIVE';
```

### Filtros comuns
- `TEMPLATE_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_CX_SITE_TEMPLATES_TL.
---

## Referencias

- [Oracle Docs -- IRC_CX_SITE_TEMPLATES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxsitetemplatesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[careersitepagepvo|CareerSitePagePVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SiteTemplateBPEOCreatedBy | — |
| CREATION_DATE | SiteTemplateBPEOCreationDate | — |
| IS_ACTIVE_FLAG | SiteTemplateBPEOIsActiveFlag | — |
| LAST_UPDATE_DATE | SiteTemplateBPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SiteTemplateBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SiteTemplateBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SiteTemplateBPEOObjectVersionNumber | — |
| SITE_NUMBER | SiteTemplateBPEOSiteNumber | — |
| SPLASH_PAGE_NUMBER | SiteTemplateBPEOSplashPageNumber | — |
| TEMPLATE_ID | SiteTemplateBPEOTemplateId | ✅ |
| TEMPLATE_NUMBER | SiteTemplateBPEOTemplateNumber | ✅ |

### [[careersitepvo|CareerSitePVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | SiteTemplatePEOCreatedBy | — |
| CREATION_DATE | SiteTemplatePEOCreationDate | — |
| IS_ACTIVE_FLAG | SiteTemplatePEOIsActiveFlag | — |
| LAST_UPDATE_DATE | SiteTemplatePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | SiteTemplatePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SiteTemplatePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SiteTemplatePEOObjectVersionNumber | — |
| SITE_NUMBER | SiteTemplatePEOSiteNumber | — |
| SPLASH_PAGE_NUMBER | SiteTemplatePEOSplashPageNumber | — |
| TEMPLATE_ID | SiteTemplatePEOTemplateId | ✅ |
| TEMPLATE_NUMBER | SiteTemplatePEOTemplateNumber | ✅ |
