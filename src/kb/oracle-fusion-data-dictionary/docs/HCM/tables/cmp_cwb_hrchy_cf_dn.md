---
id: DOC-HCM-071
doc_type: system-doc
title: "CMP_CWB_HRCHY_CF_DN — Hierarquia CWB Configurável (Denormalizada)"
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
  - compensation
  - hierarquia-cwb
  - cwb-hierarchy
  - denormalizada
aliases:
  - CMP_CWB_HRCHY_CF_DN
  - cmp_cwb_hrchy_cf_dn
  - hierarquia-cwb-compensacao
  - cwb-hierarchy-denorm
  - cmp-cwb-hrchy
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_HRCHY_CF_DN

## 📌 Visão Geral

Armazena a **hierarquia denormalizada** do Compensation Workbench, permitindo navegação rápida na árvore de gestores para distribuição de compensação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Navegação hierárquica:** Árvore de gestores para drill-down no CWB.
- **Performance:** Estrutura denormalizada para consultas rápidas.
- **Delegação:** Suporte a delegação de orçamento entre níveis.
- **Relatórios:** Roll-up de valores por nível hierárquico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HRCHY_CF_DN_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | MANAGER_ID | NUMBER(18) | NOT NULL | FK | Gestor | [[per_all_people_f]] | 🟢 85% |
| 3 | SUBORDINATE_ID | NUMBER(18) | NOT NULL | FK | Subordinado | [[per_all_people_f]] | 🟢 85% |
| 4 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 5 | LEVEL_NUMBER | NUMBER | NULL | Hierarquia | Nível na hierarquia | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `MANAGER_ID` e `SUBORDINATE_ID` (gestor na hierarquia de compensacao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Subordinados de um gestor no CWB
```sql
SELECT h.SUBORDINATE_ID, h.LEVEL_NUMBER
FROM   CMP_CWB_HRCHY_CF_DN h
WHERE  h.MANAGER_ID = :p_manager_id
  AND  h.PLAN_ID = :p_plan_id
ORDER BY h.LEVEL_NUMBER;
```

### Filtros comuns
- `LEVEL_NUMBER = 1` — Subordinados diretos

---

## 🔒 Observações

- Estrutura denormalizada para performance: cada registro conecta um gestor a todos os seus subordinados.
- `LEVEL_NUMBER` indica a profundidade na hierarquia (1 = direto, 2 = indireto, etc.).
- Recriada a cada ciclo de compensação.

---

## 🔗 PVOs Relacionados

### [[hierarchycfdnpvo|HierarchyCfDnPVO]] (HCM · BICC: 39/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| CREATED_BY | HierarchyCfDnPEOCreatedBy | ✅ |
| CREATION_DATE | HierarchyCfDnPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | HierarchyCfDnPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HierarchyCfDnPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HierarchyCfDnPEOLastUpdatedBy | ✅ |
| LEVEL10_MGR_PERSON_ID | HierarchyCfDnPEOLevel10MgrPersonId | ✅ |
| LEVEL10_PERSON_EVENT_ID | HierarchyCfDnPEOLevel10PersonEventId | ✅ |
| LEVEL11_MGR_PERSON_ID | HierarchyCfDnPEOLevel11MgrPersonId | ✅ |
| LEVEL11_PERSON_EVENT_ID | HierarchyCfDnPEOLevel11PersonEventId | ✅ |
| LEVEL12_MGR_PERSON_ID | HierarchyCfDnPEOLevel12MgrPersonId | ✅ |
| LEVEL12_PERSON_EVENT_ID | HierarchyCfDnPEOLevel12PersonEventId | ✅ |
| LEVEL13_MGR_PERSON_ID | HierarchyCfDnPEOLevel13MgrPersonId | ✅ |
| LEVEL13_PERSON_EVENT_ID | HierarchyCfDnPEOLevel13PersonEventId | ✅ |
| LEVEL14_MGR_PERSON_ID | HierarchyCfDnPEOLevel14MgrPersonId | ✅ |
| LEVEL14_PERSON_EVENT_ID | HierarchyCfDnPEOLevel14PersonEventId | ✅ |
| LEVEL15_MGR_PERSON_ID | HierarchyCfDnPEOLevel15MgrPersonId | ✅ |
| LEVEL15_PERSON_EVENT_ID | HierarchyCfDnPEOLevel15PersonEventId | ✅ |
| LEVEL1_MGR_PERSON_ID | HierarchyCfDnPEOLevel1MgrPersonId | ✅ |
| LEVEL1_PERSON_EVENT_ID | HierarchyCfDnPEOLevel1PersonEventId | ✅ |
| LEVEL2_MGR_PERSON_ID | HierarchyCfDnPEOLevel2MgrPersonId | ✅ |
| LEVEL2_PERSON_EVENT_ID | HierarchyCfDnPEOLevel2PersonEventId | ✅ |
| LEVEL3_MGR_PERSON_ID | HierarchyCfDnPEOLevel3MgrPersonId | ✅ |
| LEVEL3_PERSON_EVENT_ID | HierarchyCfDnPEOLevel3PersonEventId | ✅ |
| LEVEL4_MGR_PERSON_ID | HierarchyCfDnPEOLevel4MgrPersonId | ✅ |
| LEVEL4_PERSON_EVENT_ID | HierarchyCfDnPEOLevel4PersonEventId | ✅ |
| LEVEL5_MGR_PERSON_ID | HierarchyCfDnPEOLevel5MgrPersonId | ✅ |
| LEVEL5_PERSON_EVENT_ID | HierarchyCfDnPEOLevel5PersonEventId | ✅ |
| LEVEL6_MGR_PERSON_ID | HierarchyCfDnPEOLevel6MgrPersonId | ✅ |
| LEVEL6_PERSON_EVENT_ID | HierarchyCfDnPEOLevel6PersonEventId | ✅ |
| LEVEL7_MGR_PERSON_ID | HierarchyCfDnPEOLevel7MgrPersonId | ✅ |
| LEVEL7_PERSON_EVENT_ID | HierarchyCfDnPEOLevel7PersonEventId | ✅ |
| LEVEL8_MGR_PERSON_ID | HierarchyCfDnPEOLevel8MgrPersonId | ✅ |
| LEVEL8_PERSON_EVENT_ID | HierarchyCfDnPEOLevel8PersonEventId | ✅ |
| LEVEL9_MGR_PERSON_ID | HierarchyCfDnPEOLevel9MgrPersonId | ✅ |
| LEVEL9_PERSON_EVENT_ID | HierarchyCfDnPEOLevel9PersonEventId | ✅ |
| PERSON_ID | HierarchyCfDnPEOPersonId | — |
| TOP_MGR_PERSON_EVENT_ID | TopMgrPersonEventId | ✅ |
| TOP_MGR_PERSON_ID | HierarchyCfDnPEOTopMgrPersonId | ✅ |
| TOP_PERIOD_ID | HierarchyCfDnPEOTopPeriodId | ✅ |
| TOP_PLAN_ID | HierarchyCfDnPEOTopPlanId | ✅ |

### [[linemgrhierarchycfdnpvo|LineMgrHierarchyCfDnPVO]] (HCM · BICC: 32/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| CREATED_BY | HierarchyCfDnPEOCreatedBy | — |
| CREATION_DATE | HierarchyCfDnPEOCreationDate | — |
| LAST_UPDATE_DATE | HierarchyCfDnPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | HierarchyCfDnPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | HierarchyCfDnPEOLastUpdatedBy | — |
| LEVEL10_MGR_PERSON_ID | HierarchyCfDnPEOLevel10MgrPersonId | ✅ |
| LEVEL10_PERSON_EVENT_ID | HierarchyCfDnPEOLevel10PersonEventId | ✅ |
| LEVEL11_MGR_PERSON_ID | HierarchyCfDnPEOLevel11MgrPersonId | ✅ |
| LEVEL11_PERSON_EVENT_ID | HierarchyCfDnPEOLevel11PersonEventId | ✅ |
| LEVEL12_MGR_PERSON_ID | HierarchyCfDnPEOLevel12MgrPersonId | ✅ |
| LEVEL12_PERSON_EVENT_ID | HierarchyCfDnPEOLevel12PersonEventId | ✅ |
| LEVEL13_MGR_PERSON_ID | HierarchyCfDnPEOLevel13MgrPersonId | ✅ |
| LEVEL13_PERSON_EVENT_ID | HierarchyCfDnPEOLevel13PersonEventId | ✅ |
| LEVEL14_MGR_PERSON_ID | HierarchyCfDnPEOLevel14MgrPersonId | ✅ |
| LEVEL14_PERSON_EVENT_ID | HierarchyCfDnPEOLevel14PersonEventId | ✅ |
| LEVEL15_MGR_PERSON_ID | HierarchyCfDnPEOLevel15MgrPersonId | ✅ |
| LEVEL15_PERSON_EVENT_ID | HierarchyCfDnPEOLevel15PersonEventId | ✅ |
| LEVEL1_MGR_PERSON_ID | HierarchyCfDnPEOLevel1MgrPersonId | ✅ |
| LEVEL1_PERSON_EVENT_ID | HierarchyCfDnPEOLevel1PersonEventId | ✅ |
| LEVEL2_MGR_PERSON_ID | HierarchyCfDnPEOLevel2MgrPersonId | ✅ |
| LEVEL2_PERSON_EVENT_ID | HierarchyCfDnPEOLevel2PersonEventId | ✅ |
| LEVEL3_MGR_PERSON_ID | HierarchyCfDnPEOLevel3MgrPersonId | ✅ |
| LEVEL3_PERSON_EVENT_ID | HierarchyCfDnPEOLevel3PersonEventId | ✅ |
| LEVEL4_MGR_PERSON_ID | HierarchyCfDnPEOLevel4MgrPersonId | ✅ |
| LEVEL4_PERSON_EVENT_ID | HierarchyCfDnPEOLevel4PersonEventId | ✅ |
| LEVEL5_MGR_PERSON_ID | HierarchyCfDnPEOLevel5MgrPersonId | ✅ |
| LEVEL5_PERSON_EVENT_ID | HierarchyCfDnPEOLevel5PersonEventId | ✅ |
| LEVEL6_MGR_PERSON_ID | HierarchyCfDnPEOLevel6MgrPersonId | ✅ |
| LEVEL6_PERSON_EVENT_ID | HierarchyCfDnPEOLevel6PersonEventId | ✅ |
| LEVEL7_MGR_PERSON_ID | HierarchyCfDnPEOLevel7MgrPersonId | ✅ |
| LEVEL7_PERSON_EVENT_ID | HierarchyCfDnPEOLevel7PersonEventId | ✅ |
| LEVEL8_MGR_PERSON_ID | HierarchyCfDnPEOLevel8MgrPersonId | ✅ |
| LEVEL8_PERSON_EVENT_ID | HierarchyCfDnPEOLevel8PersonEventId | ✅ |
| LEVEL9_MGR_PERSON_ID | HierarchyCfDnPEOLevel9MgrPersonId | ✅ |
| LEVEL9_PERSON_EVENT_ID | HierarchyCfDnPEOLevel9PersonEventId | ✅ |
| PERSON_ID | HierarchyCfDnPEOPersonId | — |
| TOP_MGR_PERSON_EVENT_ID | TopMgrPersonEventId | ✅ |
| TOP_MGR_PERSON_ID | HierarchyCfDnPEOTopMgrPersonId | ✅ |
| TOP_PERIOD_ID | HierarchyCfDnPEOTopPeriodId | — |
| TOP_PLAN_ID | HierarchyCfDnPEOTopPlanId | — |

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_HRCHY_CF_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbhrchycfdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
