---
id: DOC-HCM-742
doc_type: system-doc
title: "WLF_LI_HIERARCHIES_F — Hierarquias de Itens de Aprendizado"
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
  - hierarquias
aliases:
  - WLF_LI_HIERARCHIES_F
  - wlf_li_hierarchies_f
  - wlf-li-hierarchies-f
  - hierarquias-itens-aprendizado
  - li-hierarchies
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_HIERARCHIES_F

## Visão Geral

Armazena as **relações hierárquicas entre itens de aprendizado**, permitindo organizar cursos em categorias, temas ou trilhas aninhadas. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Categorização** — organiza itens de aprendizado em estruturas hierárquicas.
- **Trilhas de aprendizado** — define relações pai-filho entre cursos e programas.
- **Navegação no catálogo** — suporta navegação por categorias/temas.
- **Pré-requisitos estruturais** — define dependências hierárquicas entre itens.
- **Relatórios por categoria** — análise de treinamentos por área temática.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_HIERARCHY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da relação hierárquica | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | PARENT_LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 5 | CHILD_LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado filho | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 6 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem do filho dentro do pai | — | 🟡 75% |
| 7 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Item filho é obrigatório (Y/N) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `PARENT_LEARNING_ITEM_ID` (item pai)
- [[wlf_learning_items_f]] — via `CHILD_LEARNING_ITEM_ID` (item filho)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Itens filhos de um programa de aprendizado
```sql
SELECT lh.CHILD_LEARNING_ITEM_ID, li.ITEM_NUMBER, lh.SEQUENCE, lh.MANDATORY_FLAG
FROM   WLF_LI_HIERARCHIES_F lh
JOIN   WLF_LEARNING_ITEMS_F li ON lh.CHILD_LEARNING_ITEM_ID = li.LEARNING_ITEM_ID
WHERE  lh.PARENT_LEARNING_ITEM_ID = :p_parent_item_id
  AND  SYSDATE BETWEEN lh.EFFECTIVE_START_DATE AND lh.EFFECTIVE_END_DATE
ORDER BY lh.SEQUENCE;
```

### Filtros comuns
- `PARENT_LEARNING_ITEM_ID = :p_parent_id` — Itens filhos de um pai
- `MANDATORY_FLAG = 'Y'` — Apenas itens obrigatórios

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Relacionamento auto-referencial via WLF_LEARNING_ITEMS_F.
- Permite estruturas multinível (programas > módulos > cursos).
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- LI = Learning Item.

---

## Referências

- [Oracle Docs — WLF_LI_HIERARCHIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflihierarchiesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[coursepvo|CoursePVO]] (HCM · BICC: 8/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHILD_LEARNING_ITEM_ID | LearningItemHierarchyDEOChildLearningItemId | ✅ |
| EFFECTIVE_END_DATE | LearningItemHierarchyDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LearningItemHierarchyDEOEffectiveStartDate | ✅ |
| HIERARCHY_ID | LearningItemHierarchyDEOHierarchyId | ✅ |
| LEARNING_ITEM_ID | LearningItemHierarchyDEOLearningItemId | ✅ |
| MANDATORY_FLAG | LearningItemHierarchyDEOMandatoryFlag | ✅ |
| OBJECT_VERSION_NUMBER | LearningItemHierarchyDEOObjectVersionNumber | ✅ |
| POSITION | LearningItemHierarchyDEOPosition | ✅ |

### [[hierarchygrandparenttochildpvo|HierarchyGrandParentToChildPVO]] (HCM · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHILD_LEARNING_ITEM_ID | ChildLearningItemHierarchyEOChildLearningItemId | ✅ |
| CHILD_LEARNING_ITEM_ID | GParentLearningItemHierarchyChildLearningItemId | ✅ |
| EFFECTIVE_END_DATE | ChildLearningItemHierarchyEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | GParentLearningItemHierarchyEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ChildLearningItemHierarchyEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | GParentLearningItemHierarchyEffectiveStartDate | ✅ |
| HIERARCHY_ID | ChildLearningItemHierarchyEOHierarchyId | — |
| HIERARCHY_ID | GParentLearningItemHierarchyHierarchyId | ✅ |
| LEARNING_ITEM_ID | ChildLearningItemHierarchyEOLearningItemId | — |
| LEARNING_ITEM_ID | GParentLearningItemHierarchyLearningItemId | — |
| OBJECT_VERSION_NUMBER | ChildLearningItemHierarchyEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | GParentLearningItemHierarchyObjectVersionNumber | — |

### [[sectionhierarchypvo|SectionHierarchyPVO]] (HCM · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHILD_LEARNING_ITEM_ID | LearningItemHierarchyDEOChildLearningItemId | ✅ |
| CREATED_BY | LearningItemHierarchyDEOCreatedBy | — |
| CREATION_DATE | LearningItemHierarchyDEOCreationDate | — |
| EFFECTIVE_END_DATE | LearningItemHierarchyDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LearningItemHierarchyDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | LearningItemHierarchyDEOEnterpriseId | — |
| HIERARCHY_ID | LearningItemHierarchyDEOHierarchyId | ✅ |
| LAST_UPDATE_DATE | LearningItemHierarchyDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LearningItemHierarchyDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LearningItemHierarchyDEOLastUpdatedBy | — |
| LEARNING_ITEM_ID | LearningItemHierarchyDEOLearningItemId | — |
| MANDATORY_FLAG | LearningItemHierarchyDEOMandatoryFlag | — |
| OBJECT_VERSION_NUMBER | LearningItemHierarchyDEOObjectVersionNumber | — |
| POSITION | LearningItemHierarchyDEOPosition | — |
