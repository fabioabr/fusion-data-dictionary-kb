---
id: DOC-HCM-229
doc_type: system-doc
title: "HRT_BI_SPECIAL_PRJ_ITEMS_V — Itens de Projetos Especiais (BI View)"
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
  - bi-view
  - projetos-especiais
  - talent
aliases:
  - HRT_BI_SPECIAL_PRJ_ITEMS_V
  - hrt_bi_special_prj_items_v
  - hrt-bi-special-prj-items-v
  - special-projects-bi
  - projetos-especiais-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_SPECIAL_PRJ_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de projetos especiais** associados aos perfis de talento dos colaboradores. Registra participacoes em projetos estrategicos e iniciativas especiais.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Management:** Rastrear participacao em projetos estrategicos.
- **Desenvolvimento:** Avaliar exposicao a projetos de alto impacto.
- **BI/Analytics:** Relatorios de alocacao de talentos em iniciativas especiais.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de conteudo | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de talento associado | [[hrt_profiles_b]] | 🟢 90% |
| 4 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo | [[hrt_content_types_b]] | 🟢 90% |
| 5 | PROJECT_NAME | VARCHAR2(240) | NULL | Dados | Nome do projeto especial | — | 🟡 75% |
| 6 | PROJECT_ROLE | VARCHAR2(240) | NULL | Dados | Papel do colaborador no projeto | — | 🟡 70% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da participacao | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de termino da participacao | — | 🟢 90% |
| 9 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Observacoes sobre o projeto | — | 🟡 70% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do registro | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa participante do projeto especial)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Projetos especiais de um colaborador
```sql
SELECT sp.PROJECT_NAME, sp.PROJECT_ROLE,
       sp.DATE_FROM, sp.DATE_TO
FROM   HRT_BI_SPECIAL_PRJ_ITEMS_V sp
WHERE  sp.PERSON_ID = :p_person_id
ORDER BY sp.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Projetos especiais sao informados manualmente no perfil do colaborador.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_SPECIAL_PRJ_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbispecialprjitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
