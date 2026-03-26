---
id: DOC-HCM-255
doc_type: system-doc
title: "HRT_PROFILE_TYP_SECTIONS_VL — Secoes de Tipo de Perfil (View Linguistica)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - profile-type-sections
  - configuracao
  - talent
aliases:
  - HRT_PROFILE_TYP_SECTIONS_VL
  - hrt_profile_typ_sections_vl
  - hrt-profile-typ-sections-vl
  - profile-typ-sections-vl
  - secoes-tipo-perfil-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TYP_SECTIONS_VL

## 📌 Visao Geral

View linguistica que combina dados base e traducoes das **secoes de tipo de perfil**. Cada secao representa uma categoria de conteudo dentro de um tipo de perfil.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir quais secoes compoem cada tipo de perfil.
- **Estruturacao:** Organizar os itens de perfil em categorias.
- **Exibicao:** Apresentar secoes com nomes traduzidos em UIs.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_TYPE_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da secao | — | 🟢 95% |
| 2 | PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de perfil | [[hrt_profile_types_b]] | 🟢 95% |
| 3 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo da secao | [[hrt_content_types_b]] | 🟢 95% |
| 4 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome da secao (traduzido) | — | 🟢 95% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao da secao | — | 🟢 90% |
| 6 | SECTION_SEQUENCE | NUMBER | NULL | Dados | Ordem de exibicao da secao | — | 🟡 80% |
| 7 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_types_b]] — via `PROFILE_TYPE_ID` (tipo de perfil da secao)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo da secao de perfil)

### Tabelas-filha (FK de saida)
- [[hrt_profile_tp_sc_prp_b]] — via `PROFILE_TYPE_SECTION_ID` (propriedades da secao do tipo de perfil)

---

## 📎 Uso Tipico

### Secoes de um tipo de perfil
```sql
SELECT pts.SECTION_NAME, pts.CONTENT_TYPE_ID, pts.SECTION_SEQUENCE
FROM   HRT_PROFILE_TYP_SECTIONS_VL pts
WHERE  pts.PROFILE_TYPE_ID = :p_profile_type_id
ORDER BY pts.SECTION_SEQUENCE;
```

---

## 🔒 Observacoes

- Sufixo `_VL` indica View Linguistica.
- Cada secao vincula um tipo de conteudo a um tipo de perfil.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TYP_SECTIONS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletypsectionsvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
