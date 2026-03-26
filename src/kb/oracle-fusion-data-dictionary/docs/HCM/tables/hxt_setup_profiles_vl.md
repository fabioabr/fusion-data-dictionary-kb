---
id: DOC-HCM-415
doc_type: system-doc
title: "HXT_SETUP_PROFILES_VL — View de Lookup de Perfis de Configuracao HXT"
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
  - lookup
  - view
aliases:
  - HXT_SETUP_PROFILES_VL
  - hxt_setup_profiles_vl
  - hxt-setup-profiles-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_PROFILES_VL

## 📌 Visao Geral

View que une a tabela base **HXT_SETUP_PROFILES_B** com as traducoes **HXT_SETUP_PROFILES_TL** no idioma da sessao do usuario. Fornece acesso simplificado aos perfis de configuracao com textos traduzidos.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view de lookup** que une a tabela base (_B) com traducoes (_TL) no idioma da sessao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Acesso simplificado:** retorna perfis com traducoes no idioma da sessao.
- **Lookups de interface:** alimenta dropdowns e listas na UI.
- **Relatorios:** fornece nomes traduzidos para relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador do perfil | — | 🟡 70% |
| 2 | PROFILE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do perfil | — | 🟡 70% |
| 3 | PROFILE_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome traduzido | — | 🟡 65% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 5 | PROFILE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do perfil | — | 🟡 60% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 65% |
| 7 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificacao | Legislacao | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Perfis de setup com nomes traduzidos
```sql
SELECT v.PROFILE_ID, v.PROFILE_CODE, v.PROFILE_NAME,
       v.DESCRIPTION, v.PROFILE_TYPE
FROM   HXT_SETUP_PROFILES_VL v
WHERE  v.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Perfis ativos`
- `PROFILE_CODE = :p_code — Por codigo`

---

## 🔒 Observacoes

- View somente leitura que une _B com _TL.
- Retorna traducoes no idioma da sessao (USERENV('LANG')).
- Preferir esta view para consultas que requerem nomes traduzidos.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_PROFILES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupprofilesvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
