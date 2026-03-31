---
id: DOC-HCM-734
doc_type: system-doc
title: "WLF_LEARNING_ITEMS_F — Itens de Aprendizado (Learning)"
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
  - learning
  - workforce-learning
  - itens-aprendizado
aliases:
  - WLF_LEARNING_ITEMS_F
  - wlf_learning_items_f
  - wlf-learning-items-f
  - itens-de-aprendizado
  - learning-items
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LEARNING_ITEMS_F

## Visão Geral

Armazena os **itens de aprendizado** (cursos, e-learnings, certificações, programas) disponíveis no catálogo de Workforce Learning. Tabela central do módulo de aprendizado. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Catálogo de treinamentos** — repositório central de todos os itens de aprendizado disponíveis.
- **Gestão de cursos** — definição de cursos, e-learnings, certificações e programas.
- **Planejamento de capacitação** — base para planos de desenvolvimento individual e organizacional.
- **Compliance** — cadastro de treinamentos obrigatórios regulatórios.
- **Análise de investimento** — custo e duração dos itens de aprendizado.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único do item de aprendizado | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | ITEM_NUMBER | VARCHAR2(30) | NULL | Identificação | Número/código do item | — | 🟡 80% |
| 5 | ITEM_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (COURSE, ELEARNING, CERTIFICATION, etc.) | — | 🟢 85% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status do item (active, inactive, retired) | — | 🟢 85% |
| 7 | DURATION_VALUE | NUMBER(10) | NULL | Dados | Duração estimada | — | 🟡 75% |
| 8 | DURATION_UNIT | VARCHAR2(30) | NULL | Dados | Unidade de duração (hours, days) | — | 🟡 75% |
| 9 | COST | NUMBER(15,2) | NULL | Financeiro | Custo do item de aprendizado | — | 🟡 70% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do custo | — | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai identificada (tabela raiz do domínio Learning).

### Tabelas-filha (FK de saída)
- [[wlf_learning_items_f_tl]] — via `LEARNING_ITEM_ID` (traduções do item de aprendizado)
- [[wlf_event_assignments_f]] — via `LEARNING_ITEM_ID` (atribuições de eventos do item de aprendizado)
- [[wlf_assignment_records_f]] — via `LEARNING_ITEM_ID` (registros de atribuição)
- [[wlf_li_activities_f]] — via `LEARNING_ITEM_ID` (atividades do item de aprendizado)
- [[wlf_li_classes_f]] — via `LEARNING_ITEM_ID` (turmas do item de aprendizado)
- [[wlf_li_content_f]] — via `LEARNING_ITEM_ID` (conteúdos do item de aprendizado)
- [[wlf_li_courses_f]] — via `LEARNING_ITEM_ID` (cursos do item de aprendizado)
- [[wlf_li_elearnings_f]] — via `LEARNING_ITEM_ID` (e-learnings do item de aprendizado)
- [[wlf_li_hierarchies_f]] — via `LEARNING_ITEM_ID` (hierarquias do item de aprendizado)

---

## Uso Típico

### Catálogo de itens de aprendizado ativos
```sql
SELECT li.ITEM_NUMBER, li.ITEM_TYPE, li.STATUS, li.DURATION_VALUE, li.DURATION_UNIT
FROM   WLF_LEARNING_ITEMS_F li
WHERE  li.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN li.EFFECTIVE_START_DATE AND li.EFFECTIVE_END_DATE
ORDER BY li.ITEM_TYPE, li.ITEM_NUMBER;
```

### Filtros comuns
- `ITEM_TYPE = 'COURSE'` — Apenas cursos
- `STATUS = 'ACTIVE'` — Apenas itens ativos

---

## Observações

- Tabela central do módulo Workforce Learning — a maioria das tabelas WLF_ referencia esta.
- Tabela date-effective (_F) — registros possuem vigência temporal.
- Traduções disponíveis em WLF_LEARNING_ITEMS_F_TL.
- Cada item pode ter múltiplas representações (curso, e-learning, etc.) nas tabelas especializadas.

---

## Referências

- [Oracle Docs — WLF_LEARNING_ITEMS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflearningitemsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
