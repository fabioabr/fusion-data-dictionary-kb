---
id: DOC-HCM-679
doc_type: system-doc
title: "PER_MANAGER_HRCHY_CF — Hierarquia de Gestores (Calculated/Flat)"
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
  - hierarquia-gestores
  - manager-hierarchy
  - organograma
  - calculated-flat
aliases:
  - PER_MANAGER_HRCHY_CF
  - per_manager_hrchy_cf
  - hierarquia-gestores-cf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_MANAGER_HRCHY_CF

## Visão Geral

Armazena a **hierarquia de gestores calculada e achatada** (flattened). Contém a cadeia completa de gestão para cada colaborador, desde o gestor direto até o topo da organização, pré-calculada para consultas rápidas.

> [!note] Sufixo _CF
> O sufixo `_CF` indica tabela **Calculated/Flat** — dados pré-calculados e desnormalizados para performance.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Navegação em organogramas** — visualizar a cadeia hierárquica completa
- **Controle de aprovações** — identificar todos os níveis de gestão acima de um colaborador
- **Relatórios gerenciais** — consolidar métricas por nível de gestão
- **Segurança por hierarquia** — conceder acessos com base na árvore de gestão
- **Análise de span of control** — medir amplitude de controle gerencial

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MANAGER_HRCHY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de hierarquia | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_PERSONS | 🟢 90% |
| 3 | MANAGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do gestor na cadeia | PER_PERSONS | 🟢 90% |
| 4 | MANAGER_LEVEL | NUMBER | NOT NULL | Hierarquia | Nível do gestor na cadeia (1=direto, 2=acima, etc.) | — | 🟡 80% |
| 5 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo/atribuição do colaborador | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 6 | MANAGER_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo/atribuição do gestor | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 7 | MANAGER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de gestão (LINE_MANAGER, PROJECT_MANAGER) | — | 🟡 70% |
| 8 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 9 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` e `MANAGER_ID` (pessoa na hierarquia gerencial)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` e `MANAGER_ASSIGNMENT_ID` (vínculo na hierarquia gerencial)

### Tabelas-filha (FK de saída)

---

## Uso Típico

### Cadeia hierárquica completa de um colaborador
```sql
SELECT mh.MANAGER_ID, mh.MANAGER_LEVEL, mh.MANAGER_TYPE
FROM   PER_MANAGER_HRCHY_CF mh
WHERE  mh.PERSON_ID = :p_person_id
ORDER BY mh.MANAGER_LEVEL;
```

---

## Observações

- Tabela pré-calculada: os dados são gerados por processos batch do Oracle Fusion.
- O `MANAGER_LEVEL` 1 indica o gestor direto (line manager imediato).
- Pode conter múltiplos tipos de hierarquia (linha, projeto, matriz).
- Dados podem ter defasagem em relação a alterações recentes de gestão.

---

## Referências

- [Oracle Docs — PER_MANAGER_HRCHY_CF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/permanagerhrhycf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[managerhrchybottomuppvolinemanager|ManagerHrchyBottomUpPVOLineManager]] (HCM · BICC: 6/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEVEL10_MANAGER_ASSIGNMENT_ID | Level10ManagerAssignmentId | — |
| LEVEL10_MANAGER_ID | Level10ManagerId | — |
| LEVEL11_MANAGER_ASSIGNMENT_ID | Level11ManagerAssignmentId | — |
| LEVEL11_MANAGER_ID | Level11ManagerId | — |
| LEVEL12_MANAGER_ASSIGNMENT_ID | Level12ManagerAssignmentId | — |
| LEVEL12_MANAGER_ID | Level12ManagerId | — |
| LEVEL13_MANAGER_ASSIGNMENT_ID | Level13ManagerAssignmentId | — |
| LEVEL13_MANAGER_ID | Level13ManagerId | — |
| LEVEL14_MANAGER_ASSIGNMENT_ID | Level14ManagerAssignmentId | — |
| LEVEL14_MANAGER_ID | Level14ManagerId | — |
| LEVEL15_MANAGER_ASSIGNMENT_ID | Level15ManagerAssignmentId | — |
| LEVEL15_MANAGER_ID | Level15ManagerId | — |
| LEVEL16_MANAGER_ASSIGNMENT_ID | Level16ManagerAssignmentId | — |
| LEVEL16_MANAGER_ID | Level16ManagerId | — |
| LEVEL17_MANAGER_ASSIGNMENT_ID | Level17ManagerAssignmentId | — |
| LEVEL17_MANAGER_ID | Level17ManagerId | — |
| LEVEL18_MANAGER_ASSIGNMENT_ID | Level18ManagerAssignmentId | — |
| LEVEL18_MANAGER_ID | Level18ManagerId | — |
| LEVEL19_MANAGER_ASSIGNMENT_ID | Level19ManagerAssignmentId | — |
| LEVEL19_MANAGER_ID | Level19ManagerId | — |
| LEVEL1_MANAGER_ASSIGNMENT_ID | Level1ManagerAssignmentId | — |
| LEVEL1_MANAGER_ID | Level1ManagerId | — |
| LEVEL20_MANAGER_ASSIGNMENT_ID | Level20ManagerAssignmentId | — |
| LEVEL20_MANAGER_ID | Level20ManagerId | — |
| LEVEL2_MANAGER_ASSIGNMENT_ID | Level2ManagerAssignmentId | — |
| LEVEL2_MANAGER_ID | Level2ManagerId | — |
| LEVEL3_MANAGER_ASSIGNMENT_ID | Level3ManagerAssignmentId | — |
| LEVEL3_MANAGER_ID | Level3ManagerId | — |
| LEVEL4_MANAGER_ASSIGNMENT_ID | Level4ManagerAssignmentId | — |
| LEVEL4_MANAGER_ID | Level4ManagerId | — |
| LEVEL5_MANAGER_ASSIGNMENT_ID | Level5ManagerAssignmentId | — |
| LEVEL5_MANAGER_ID | Level5ManagerId | — |
| LEVEL6_MANAGER_ASSIGNMENT_ID | Level6ManagerAssignmentId | — |
| LEVEL6_MANAGER_ID | Level6ManagerId | — |
| LEVEL7_MANAGER_ASSIGNMENT_ID | Level7ManagerAssignmentId | — |
| LEVEL7_MANAGER_ID | Level7ManagerId | — |
| LEVEL8_MANAGER_ASSIGNMENT_ID | Level8ManagerAssignmentId | — |
| LEVEL8_MANAGER_ID | Level8ManagerId | — |
| LEVEL9_MANAGER_ASSIGNMENT_ID | Level9ManagerAssignmentId | — |
| LEVEL9_MANAGER_ID | Level9ManagerId | — |
| MANAGER_TYPE | ManagerType | ✅ |
| PERSON_ID | PersonId | ✅ |
| REQUEST_ID | RequestId | — |
