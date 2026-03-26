---
id: DOC-HCM-231
doc_type: system-doc
title: "HRT_BI_WORK_PREFERENCE_ITEMS_V — Itens de Preferencias de Trabalho (BI View)"
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
  - preferencias-trabalho
  - mobilidade
aliases:
  - HRT_BI_WORK_PREFERENCE_ITEMS_V
  - hrt_bi_work_preference_items_v
  - hrt-bi-work-preference-items-v
  - work-preference-bi
  - preferencias-trabalho-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_WORK_PREFERENCE_ITEMS_V

## 📌 Visao Geral

View BI que expoe as **preferencias de trabalho** dos colaboradores — disposicao para viagens, relocacao, modelo de trabalho (remoto/presencial) e outras preferencias registradas no perfil de talento.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Mobilidade:** Identificar colaboradores disponiveis para relocacao ou viagens.
- **Workforce Planning:** Considerar preferencias em planejamento de alocacao.
- **BI/Analytics:** Relatorios de preferencias de trabalho por departamento.

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
| 5 | WILLING_TO_RELOCATE | VARCHAR2(30) | NULL | Dados | Disposicao para relocacao (YES/NO) | — | 🟡 75% |
| 6 | WILLING_TO_TRAVEL | VARCHAR2(30) | NULL | Dados | Disposicao para viagens (frequencia) | — | 🟡 75% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da preferencia | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim da preferencia | — | 🟢 90% |
| 9 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Observacoes sobre preferencias | — | 🟡 70% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do registro | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com preferencia de trabalho registrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Colaboradores dispostos a relocacao
```sql
SELECT wp.PERSON_ID, wp.WILLING_TO_RELOCATE,
       wp.WILLING_TO_TRAVEL
FROM   HRT_BI_WORK_PREFERENCE_ITEMS_V wp
WHERE  wp.WILLING_TO_RELOCATE = 'YES';
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Preferencias sao autopreenchidas pelo colaborador via self-service.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_WORK_PREFERENCE_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbiworkpreferenceitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
