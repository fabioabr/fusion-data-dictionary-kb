---
id: DOC-HCM-737
doc_type: system-doc
title: "WLF_LI_ACTIVITIES_F — Atividades de Itens de Aprendizado"
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
  - atividades-aprendizado
aliases:
  - WLF_LI_ACTIVITIES_F
  - wlf_li_activities_f
  - wlf-li-activities-f
  - atividades-itens-aprendizado
  - li-activities
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_ACTIVITIES_F

## Visão Geral

Armazena as **atividades** que compõem um item de aprendizado, detalhando as tarefas ou módulos que o participante deve completar. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação de cursos** — define as atividades/módulos que compõem um treinamento.
- **Tracking de progresso** — base para acompanhamento de conclusão por atividade.
- **Sequenciamento** — define a ordem de execução das atividades.
- **Avaliação granular** — permite avaliar desempenho por atividade individual.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_ACTIVITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atividade | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 5 | ACTIVITY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da atividade (quiz, video, assignment) | — | 🟡 75% |
| 6 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem da atividade no item | — | 🟡 75% |
| 7 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Indica se a atividade é obrigatória (Y/N) | — | 🟡 70% |
| 8 | DURATION_MINUTES | NUMBER(10) | NULL | Dados | Duração estimada em minutos | — | 🟡 70% |
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

### Atividades de um item de aprendizado
```sql
SELECT la.ACTIVITY_TYPE, la.SEQUENCE, la.MANDATORY_FLAG, la.DURATION_MINUTES
FROM   WLF_LI_ACTIVITIES_F la
WHERE  la.LEARNING_ITEM_ID = :p_learning_item_id
  AND  SYSDATE BETWEEN la.EFFECTIVE_START_DATE AND la.EFFECTIVE_END_DATE
ORDER BY la.SEQUENCE;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Atividades de um item específico
- `MANDATORY_FLAG = 'Y'` — Apenas atividades obrigatórias

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Granularidade abaixo do item de aprendizado (LI = Learning Item).

---

## Referências

- [Oracle Docs — WLF_LI_ACTIVITIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfliactivitiesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
