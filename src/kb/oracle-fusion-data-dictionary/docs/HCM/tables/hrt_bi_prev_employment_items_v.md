---
id: DOC-HCM-227
doc_type: system-doc
title: "HRT_BI_PREV_EMPLOYMENT_ITEMS_V — Itens de Emprego Anterior (BI View)"
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
  - emprego-anterior
  - talent
aliases:
  - HRT_BI_PREV_EMPLOYMENT_ITEMS_V
  - hrt_bi_prev_employment_items_v
  - hrt-bi-prev-employment-items-v
  - previous-employment-bi
  - emprego-anterior-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_PREV_EMPLOYMENT_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de emprego anterior** dos colaboradores. Permite analise de historico profissional previo para fins de talent management e compliance.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Analise de historico:** Consulta de experiencias profissionais anteriores dos colaboradores.
- **Talent Management:** Avaliacao de experiencia previa em processos de promocao e sucessao.
- **Compliance:** Verificacao de historico profissional para requisitos regulatorios.

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
| 5 | EMPLOYER_NAME | VARCHAR2(240) | NULL | Dados | Nome do empregador anterior | — | 🟡 75% |
| 6 | JOB_TITLE | VARCHAR2(240) | NULL | Dados | Cargo exercido no emprego anterior | — | 🟡 75% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio do emprego anterior | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de termino do emprego anterior | — | 🟢 90% |
| 9 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Observacoes sobre o emprego anterior | — | 🟡 70% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do registro | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com historico de emprego anterior)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Empregos anteriores de um colaborador
```sql
SELECT pi.EMPLOYER_NAME, pi.JOB_TITLE,
       pi.DATE_FROM, pi.DATE_TO
FROM   HRT_BI_PREV_EMPLOYMENT_ITEMS_V pi
WHERE  pi.PERSON_ID = :p_person_id
ORDER BY pi.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Pode incluir empregos informados pelo colaborador via self-service.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_PREV_EMPLOYMENT_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbiprevemploymentitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
