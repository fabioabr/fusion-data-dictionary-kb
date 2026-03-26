---
id: DOC-HCM-132
doc_type: system-doc
title: "HMO_MODEL_PLAN_DETAILS — Detalhes de Planos de Modelo Organizacional"
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
  - workforce-modeling
  - detalhes-modelo
  - headcount
  - hmo
aliases:
  - HMO_MODEL_PLAN_DETAILS
  - hmo_model_plan_details
  - hmo-model-plan-details
  - DOC-HCM-132
  - detalhes-de-planos-de-modelo-organizacional
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HMO_MODEL_PLAN_DETAILS

## 📌 Visão Geral

Armazena os **detalhes granulares** dos planos de modelo organizacional — as mudanças propostas em departamentos, posições, headcount e hierarquias.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhes de mudanças:** Propostas específicas de cada reorganização.
- **Impacto em posições:** Criação, eliminação ou transferência de posições.
- **Headcount planejado:** Projeção de quantidade de colaboradores.
- **Análise de impacto:** Avaliação de efeitos da reorganização.
- **Simulação:** Cenários hipotéticos antes da efetivação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MODEL_PLAN_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟡 80% |
| 2 | MODEL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de modelo | [[hmo_model_plans_b]] | 🟢 90% |
| 3 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento afetado | [[per_departments]] | 🟡 80% |
| 4 | POSITION_ID | NUMBER(18) | NULL | FK | Posição afetada | [[hr_all_positions_f]] | 🟡 75% |
| 5 | CHANGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de mudança (ADD, REMOVE, TRANSFER, MODIFY) | — | 🟡 75% |
| 6 | PLANNED_HEADCOUNT | NUMBER | NULL | Indicador | Headcount planejado | — | 🟡 70% |
| 7 | CURRENT_HEADCOUNT | NUMBER | NULL | Indicador | Headcount atual | — | 🟡 70% |
| 8 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade planejada | — | 🟡 75% |
| 9 | NOTES | VARCHAR2(2000) | NULL | Texto | Observações sobre a mudança | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hmo_model_plans_b]] — via `MODEL_PLAN_ID` (plano do modelo de headcount)
- [[per_departments]] — via `DEPARTMENT_ID` (departamento do detalhe do modelo)
- [[hr_all_positions_f]] — via `POSITION_ID` (posicao no detalhe do modelo de headcount)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Detalhes de um plano de modelo
```sql
SELECT d.DEPARTMENT_ID, d.POSITION_ID, d.CHANGE_TYPE,
       d.PLANNED_HEADCOUNT, d.CURRENT_HEADCOUNT
FROM   HMO_MODEL_PLAN_DETAILS d
WHERE  d.MODEL_PLAN_ID = :p_plan_id;
```

### Mudanças de headcount
```sql
SELECT d.DEPARTMENT_ID, d.CURRENT_HEADCOUNT, d.PLANNED_HEADCOUNT,
       (d.PLANNED_HEADCOUNT - d.CURRENT_HEADCOUNT) AS delta
FROM   HMO_MODEL_PLAN_DETAILS d
WHERE  d.MODEL_PLAN_ID = :p_plan_id
  AND  d.PLANNED_HEADCOUNT != d.CURRENT_HEADCOUNT;
```

---

## 🔒 Observações

- Cada plano de modelo pode ter múltiplos detalhes (um por mudança proposta).
- O `CHANGE_TYPE` classifica: ADD (nova posição), REMOVE (eliminar), TRANSFER, MODIFY.
- A diferença entre `PLANNED_HEADCOUNT` e `CURRENT_HEADCOUNT` indica o delta.
- Detalhes são referência para efetivação das mudanças após aprovação do plano.

---

## 📚 Referências

- [Oracle Docs — HMO_MODEL_PLAN_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hmomodelplandetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
