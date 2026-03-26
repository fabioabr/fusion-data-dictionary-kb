---
id: DOC-HCM-510
doc_type: system-doc
title: "IRC_MEDIA_LINKS_B — Links de Midia (Base)"
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
  - media-links
  - irc-recruiting
aliases:
  - IRC_MEDIA_LINKS_B
  - irc_media_links_b
  - media-links-b
  - media-links-hcm
  - irc-media-links-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_MEDIA_LINKS_B

## Visao Geral

**Links de midia** associados a conteudo de recrutamento. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Conteudo rico:** Midias em vagas e career sites.
- **Experiencia do candidato:** Conteudo multimidia.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEDIA_LINK_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | MEDIA_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo (video, image, document) | — | 🟡 75% |
| 3 | MEDIA_URL | VARCHAR2(500) | NULL | Dados | URL do recurso | — | 🟡 75% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 70% |
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

### Links ativos
```sql
SELECT ml.MEDIA_TYPE, ml.MEDIA_URL FROM IRC_MEDIA_LINKS_B ml WHERE ml.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Ativos
---

## Observacoes

- Tabela base (_B).
---

## Referencias

- [Oracle Docs -- IRC_MEDIA_LINKS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircmedialinksb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
