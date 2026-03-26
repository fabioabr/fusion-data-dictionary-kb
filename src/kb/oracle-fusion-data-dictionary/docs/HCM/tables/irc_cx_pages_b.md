---
id: DOC-HCM-470
doc_type: system-doc
title: "IRC_CX_PAGES_B — Paginas do Career Site (Base)"
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
  - cx-pages
  - irc-recruiting
aliases:
  - IRC_CX_PAGES_B
  - irc_cx_pages_b
  - cx-pages-b
  - cx-pages-hcm
  - irc-cx-pages-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CX_PAGES_B

## Visao Geral

Armazena **paginas** do portal de experiencia do candidato. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Career site:** Estrutura de paginas do portal.
- **Personalizacao:** Customizar experiencia por site/marca.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CX_PAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | CX_SITE_ID | NUMBER(18) | NOT NULL | FK | Site de carreiras | IRC_CX_SITES_B | 🟢 85% |
| 3 | PAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de pagina | — | 🟡 75% |
| 4 | PAGE_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
| 5 | TEMPLATE_ID | NUMBER(18) | NULL | FK | Template | IRC_CX_SITE_TEMPLATES_B | 🟡 70% |
| 6 | DISPLAY_ORDER | NUMBER | NULL | Dados | Ordem de exibicao | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cx_sites_b]] — via `CX_SITE_ID` (site de carreiras da pagina)
- [[irc_cx_site_templates_b]] — via `TEMPLATE_ID` (template da pagina do site de carreiras)

### Tabelas-filha (FK de saida)
- [[irc_cx_pages_tl]] — via `CX_PAGE_ID` (traducoes da pagina do site de carreiras)

---

## Uso Tipico

### Paginas ativas
```sql
SELECT p.CX_PAGE_ID, p.PAGE_TYPE, p.DISPLAY_ORDER
FROM   IRC_CX_PAGES_B p
WHERE  p.CX_SITE_ID = :p_site_id AND p.PAGE_STATUS = 'ACTIVE'
ORDER BY p.DISPLAY_ORDER;
```

### Filtros comuns
- `PAGE_STATUS = 'ACTIVE'` — Ativas
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_CX_PAGES_TL.
---

## Referencias

- [Oracle Docs -- IRC_CX_PAGES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccxpagesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
