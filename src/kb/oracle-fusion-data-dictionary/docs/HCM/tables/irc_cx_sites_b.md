---
id: DOC-HCM-472
doc_type: system-doc
title: "IRC_CX_SITES_B — Sites de Carreiras (Base)"
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
  - career-sites
  - irc-recruiting
aliases:
  - IRC_CX_SITES_B
  - irc_cx_sites_b
  - cx-sites-b
  - cx-sites-hcm
  - irc-cx-sites-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_SITES_B

## Visao Geral

Configuracao dos **career sites**. Tabela base (`_B`) com dominio, branding e configuracao.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de career sites:** Portais de carreiras.
- **Multi-marca:** Multiplos sites por marca/divisao.
- **Branding:** Identidade visual por site.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_SITE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | SITE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do site | — | 🟢 85% |
| 3 | SITE_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 80% |
| 4 | SITE_URL | VARCHAR2(500) | NULL | Dados | URL do site | — | 🟡 75% |
| 5 | DEFAULT_LANGUAGE | VARCHAR2(4) | NULL | Configuracao | Idioma padrao | — | 🟡 75% |
| 6 | THEME_ID | NUMBER(18) | NULL | FK | Tema visual | IRC_CX_SITE_THEMES | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cx_site_themes]] — via `THEME_ID` (tema visual do site de carreiras)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Sites ativos
```sql
SELECT s.CX_SITE_ID, s.SITE_CODE, s.SITE_URL
FROM   IRC_CX_SITES_B s
WHERE  s.SITE_STATUS = 'ACTIVE';
```

### Filtros comuns
- `SITE_STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_CX_SITES_TL.
- Suporta multiplos sites.
---

## Referencias

- [Oracle Docs -- IRC_CX_SITES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxsitesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
