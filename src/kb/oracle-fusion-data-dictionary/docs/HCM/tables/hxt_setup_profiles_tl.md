---
id: DOC-HCM-414
doc_type: system-doc
title: "HXT_SETUP_PROFILES_TL — Traducoes de Perfis de Configuracao HXT"
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
  - time-labor
  - hxt
  - setup-profile
  - traducao
  - translation
aliases:
  - HXT_SETUP_PROFILES_TL
  - hxt_setup_profiles_tl
  - hxt-setup-profiles-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_PROFILES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** dos perfis de configuracao do modulo Time & Labor (HXT) em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** armazena nomes e descricoes de perfis em multiplos idiomas.
- **Interface multilingual:** alimenta a UI com textos no idioma do usuario.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do perfil | HXT_SETUP_PROFILES_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | PROFILE_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome traduzido do perfil | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_setup_profiles_b]] — via `PROFILE_ID` (registro base do perfil de configuracao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de um perfil de setup
```sql
SELECT tl.LANGUAGE, tl.PROFILE_NAME, tl.DESCRIPTION
FROM   HXT_SETUP_PROFILES_TL tl
WHERE  tl.PROFILE_ID = :p_profile_id;
```

### Filtros comuns
- `PROFILE_ID = :p_profile_id — Traducoes de um perfil`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: PROFILE_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_PROFILES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupprofilestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
