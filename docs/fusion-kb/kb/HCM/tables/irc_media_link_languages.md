---
id: DOC-HCM-512
doc_type: system-doc
title: "IRC_MEDIA_LINK_LANGUAGES — Idiomas de Links de Midia"
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
  - media-link-languages
  - irc-recruiting
aliases:
  - IRC_MEDIA_LINK_LANGUAGES
  - irc_media_link_languages
  - media-link-languages
  - media-link-hcm
  - irc-media-link-languages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_MEDIA_LINK_LANGUAGES

## Visao Geral

**Idiomas disponiveis** para cada link de midia.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Disponibilidade:** Em quais idiomas o recurso existe.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEDIA_LINK_LANG_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | MEDIA_LINK_ID | NUMBER(18) | NOT NULL | FK | Link de midia | IRC_MEDIA_LINKS_B | 🟢 85% |
| 3 | LANGUAGE_CODE | VARCHAR2(4) | NOT NULL | Dados | Idioma disponivel | — | 🟢 90% |
| 4 | LOCALIZED_URL | VARCHAR2(500) | NULL | Dados | URL localizada | — | 🟡 65% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_media_links_b]] — via `MEDIA_LINK_ID` (link de midia do idioma configurado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Idiomas de uma midia
```sql
SELECT mll.LANGUAGE_CODE, mll.LOCALIZED_URL
FROM   IRC_MEDIA_LINK_LANGUAGES mll WHERE mll.MEDIA_LINK_ID = :p_id;
```

### Filtros comuns
- `MEDIA_LINK_ID = :id` — Por midia
---

## Observacoes

- LOCALIZED_URL permite URLs por idioma.
---

## Referencias

- [Oracle Docs -- IRC_MEDIA_LINK_LANGUAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircmedialinklanguages.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[requisitionmedialinkpvo|RequisitionMediaLinkPVO]] (PO · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE_CODE | MediaLinkLanguagePEOLanguageCode | ✅ |
| MEDIA_LINK_LANGUAGE_ID | MediaLinkLanguageId | ✅ |
