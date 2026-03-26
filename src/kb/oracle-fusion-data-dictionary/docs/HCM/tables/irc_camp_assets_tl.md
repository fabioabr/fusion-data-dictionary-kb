---
id: DOC-HCM-450
doc_type: system-doc
title: "IRC_CAMP_ASSETS_TL — Traducoes de Ativos de Campanhas de Recrutamento"
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
  - irc
  - campanha
  - ativos-campanha
  - traducao
aliases:
  - IRC_CAMP_ASSETS_TL
  - irc_camp_assets_tl
  - irc-camp-assets-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_ASSETS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** dos ativos de campanhas de recrutamento do modulo Recruiting (IRC) em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** titulos e descricoes de ativos em multiplos idiomas.
- **Campanhas globais:** suporta conteudo localizado por idioma/regiao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSET_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do ativo | IRC_CAMP_ASSETS_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | ASSET_TITLE | VARCHAR2(240) | NOT NULL | Identificacao | Titulo traduzido do ativo | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CONTENT_TEXT | CLOB | NULL | Dados | Conteudo textual traduzido | — | 🟡 50% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_camp_assets_b]] — via `ASSET_ID` (registro base do ativo de campanha)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de um ativo de campanha
```sql
SELECT tl.LANGUAGE, tl.ASSET_TITLE, tl.DESCRIPTION
FROM   IRC_CAMP_ASSETS_TL tl
WHERE  tl.ASSET_ID = :p_asset_id;
```

### Filtros comuns
- `ASSET_ID = :p_asset_id — Por ativo`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: ASSET_ID + LANGUAGE.
- CONTENT_TEXT (CLOB) pode conter HTML ou texto formatado.

---

## 📚 Referencias

- [Oracle Docs — IRC_CAMP_ASSETS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampassetstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
