---
id: DOC-HCM-741
doc_type: system-doc
title: "WLF_LI_ELEARNINGS_F — E-Learnings (Learning)"
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
  - e-learning
aliases:
  - WLF_LI_ELEARNINGS_F
  - wlf_li_elearnings_f
  - wlf-li-elearnings-f
  - e-learnings-learning
  - li-elearnings
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_ELEARNINGS_F

## Visão Geral

Armazena os **atributos específicos de e-learnings**, complementando WLF_LEARNING_ITEMS_F com informações de treinamentos online auto-instruídos (SCORM, xAPI, vídeo). Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de e-learning** — dados específicos de treinamentos online.
- **Tracking de progresso** — integração com padrões SCORM/xAPI para rastreamento.
- **Disponibilidade** — controle de acesso e disponibilidade de conteúdo digital.
- **Relatórios de conclusão** — análise de taxa de conclusão por e-learning.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_ELEARNING_ID | NUMBER(18) | NOT NULL | PK | Identificador único do e-learning | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 5 | PLAYER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de player (SCORM, xAPI, native) | — | 🟡 70% |
| 6 | LAUNCH_URL | VARCHAR2(2000) | NULL | Dados | URL de lançamento do e-learning | — | 🟡 70% |
| 7 | MASTERY_SCORE | NUMBER(5,2) | NULL | Regra | Nota mínima para aprovação | — | 🟡 65% |
| 8 | MAX_ATTEMPTS | NUMBER(5) | NULL | Regra | Número máximo de tentativas permitidas | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### E-learnings SCORM disponíveis
```sql
SELECT le.PLAYER_TYPE, le.LAUNCH_URL, le.MASTERY_SCORE, le.MAX_ATTEMPTS,
       li.ITEM_NUMBER
FROM   WLF_LI_ELEARNINGS_F le
JOIN   WLF_LEARNING_ITEMS_F li ON le.LEARNING_ITEM_ID = li.LEARNING_ITEM_ID
WHERE  le.PLAYER_TYPE = 'SCORM'
  AND  SYSDATE BETWEEN le.EFFECTIVE_START_DATE AND le.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `PLAYER_TYPE = 'SCORM'` — Apenas conteúdos SCORM
- `LEARNING_ITEM_ID = :p_item_id` — E-learning de um item específico

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Especialização de WLF_LEARNING_ITEMS_F para conteúdo e-learning.
- LAUNCH_URL pode referenciar plataformas externas de conteúdo.
- LI = Learning Item.

---

## Referências

- [Oracle Docs — WLF_LI_ELEARNINGS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflielearningsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[sectionhierarchypvo|SectionHierarchyPVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ELearningDEOCreatedBy | — |
| CREATED_BY_ID | ELearningDEOCreatedById | — |
| CREATION_DATE | ELearningDEOCreationDate | — |
| EFFECTIVE_END_DATE | ELearningDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ELearningDEOEffectiveStartDate | ✅ |
| ELEARNING_ID | ELearningDEOElearningId | ✅ |
| ELEARNING_TYPE | ELearningDEOElearningType | — |
| ENTERPRISE_ID | ELearningDEOEnterpriseId | — |
| LAST_UPDATE_DATE | ELearningDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ELearningDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ELearningDEOLastUpdatedBy | — |
| LEARNING_ITEM_ID | ELearningDEOLearningItemId | — |
| OBJECT_VERSION_NUMBER | ELearningDEOObjectVersionNumber | — |
| RELATED_CONTENT_ID | ELearningDEORelatedContentId | — |
