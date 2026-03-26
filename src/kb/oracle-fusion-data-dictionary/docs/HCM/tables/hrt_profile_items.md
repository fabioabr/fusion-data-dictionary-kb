---
id: DOC-HCM-247
doc_type: system-doc
title: "HRT_PROFILE_ITEMS — Itens de Perfil de Talento"
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
  - profile-items
  - competencias
  - talent
aliases:
  - HRT_PROFILE_ITEMS
  - hrt_profile_items
  - hrt-profile-items
  - profile-items
  - itens-perfil-talento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_ITEMS

## 📌 Visao Geral

Armazena os **itens associados a perfis de talento** — cada registro vincula um item de conteudo (competencia, habilidade, certificacao) a um perfil, com rating, nivel de proficiencia e datas de vigencia.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Competencias:** Registrar competencias e seus niveis de proficiencia por colaborador.
- **Gap analysis:** Comparar itens de perfil de pessoa vs. posicao.
- **Desenvolvimento:** Identificar gaps de competencias para planos de desenvolvimento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de perfil | — | 🟢 100% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de talento | [[hrt_profiles_b]] | 🟢 100% |
| 3 | CONTENT_ITEM_ID | NUMBER(18) | NULL | FK | Item de conteudo associado | [[hrt_content_items_b]] | 🟢 95% |
| 4 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo | [[hrt_content_types_b]] | 🟢 100% |
| 5 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating | [[hrt_rating_models_b]] | 🟢 90% |
| 6 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de rating/proficiencia | [[hrt_rating_levels_b]] | 🟢 90% |
| 7 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 9 | INTEREST_LEVEL | VARCHAR2(30) | NULL | Classificacao | Nivel de interesse do colaborador | — | 🟡 75% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do item (MANUAL, SYSTEM) | — | 🟡 75% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento do item)
- [[hrt_content_items_b]] — via `CONTENT_ITEM_ID` (item de conteudo vinculado ao perfil)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo do item de perfil)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de classificacao do item de perfil)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de classificacao do item de perfil)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Competencias de um colaborador
```sql
SELECT pi.CONTENT_ITEM_ID, pi.RATING_LEVEL_ID,
       pi.DATE_FROM, pi.DATE_TO
FROM   HRT_PROFILE_ITEMS pi
       JOIN HRT_PROFILES_B p ON p.PROFILE_ID = pi.PROFILE_ID
WHERE  p.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN pi.DATE_FROM AND NVL(pi.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Tabela central para dados de competencias/habilidades associados a perfis.
- O RATING_LEVEL_ID indica o nivel de proficiencia.
- Itens podem ser adicionados via self-service pelo colaborador ou pelo gestor.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_ITEMS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofileitems.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
