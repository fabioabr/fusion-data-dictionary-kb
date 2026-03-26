---
id: DOC-HCM-225
doc_type: system-doc
title: "HRT_BI_MEMBERSHIP_ITEMS_V — Itens de Associações Profissionais — BI View"
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
  - memberships
aliases:
  - HRT_BI_MEMBERSHIP_ITEMS_V
  - hrt_bi_membership_items_v
  - itens-de-associações-profissionaisbi-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_MEMBERSHIP_ITEMS_V

## 📌 Visão Geral

View de BI com **associações profissionais** de colaboradores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Talent Analytics:** Participação em associações.
- **Perfil de talento:** Membros de organizações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEMBERSHIP_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | ORGANIZATION_NAME | VARCHAR2(240) | NULL | Descrição | Nome da organização | — | 🟡 70% |
| 4 | MEMBERSHIP_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de associação | — | 🟡 70% |
| 5 | START_DATE | DATE | NULL | Data | Início | — | 🟡 75% |
| 6 | END_DATE | DATE | NULL | Data | Término | — | 🟡 75% |
| 7 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular da filiacao profissional)

### Tabelas relacionadas
- Demais views HRT_BI_* do perfil de talento

---

## 📎 Uso Típico

### Itens por colaborador
```sql
SELECT * FROM HRT_BI_MEMBERSHIP_ITEMS_V WHERE PERSON_ID = :p_person_id;
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
