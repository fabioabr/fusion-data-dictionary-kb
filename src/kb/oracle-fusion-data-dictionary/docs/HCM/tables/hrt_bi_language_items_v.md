---
id: DOC-HCM-224
doc_type: system-doc
title: "HRT_BI_LANGUAGE_ITEMS_V — Itens de Idiomas — BI View"
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
  - talent-profile
  - bi
  - languages
aliases:
  - HRT_BI_LANGUAGE_ITEMS_V
  - hrt_bi_language_items_v
  - itens-de-idiomasbi-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_LANGUAGE_ITEMS_V

## 📌 Visão Geral

View de BI com **proficiência linguística** de colaboradores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Talent Analytics:** Idiomas e níveis.
- **Perfil de talento:** Habilidades linguísticas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LANGUAGE_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | LANGUAGE_CODE | VARCHAR2(30) | NULL | Classificação | Código do idioma | — | 🟡 75% |
| 4 | READING_LEVEL | VARCHAR2(30) | NULL | Classificação | Nível de leitura | — | 🟡 70% |
| 5 | WRITING_LEVEL | VARCHAR2(30) | NULL | Classificação | Nível de escrita | — | 🟡 70% |
| 6 | SPEAKING_LEVEL | VARCHAR2(30) | NULL | Classificação | Nível de conversão | — | 🟡 70% |
| 7 | NATIVE_FLAG | VARCHAR2(1) | NULL | Controle | Idioma nativo (Y/N) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do registro de idioma)

### Tabelas relacionadas
- Demais views HRT_BI_* do perfil de talento

---

## 📎 Uso Típico

### Itens por colaborador
```sql
SELECT * FROM HRT_BI_LANGUAGE_ITEMS_V WHERE PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- View de BI (sufixo `_V`) — otimizada para relatórios.
- Parte do conjunto HRT_BI_* do Talent Profile.
- Utilizada pelo Oracle Transactional BI (OTBI).

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
