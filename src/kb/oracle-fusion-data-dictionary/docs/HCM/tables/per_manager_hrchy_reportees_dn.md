---
id: DOC-HCM-681
doc_type: system-doc
title: "PER_MANAGER_HRCHY_REPORTEES_DN — Subordinados na Hierarquia de Gestores"
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
  - reportees
  - subordinados
  - denormalized
aliases:
  - PER_MANAGER_HRCHY_REPORTEES_DN
  - per_manager_hrchy_reportees_dn
  - subordinados-hierarquia-gestores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_MANAGER_HRCHY_REPORTEES_DN

## Visão Geral

Armazena a lista desnormalizada de **subordinados** (reportees) de cada gestor na hierarquia. Enquanto as tabelas `_CF` e `_DN` focam na cadeia ascendente (quem são os gestores), esta tabela foca na cadeia descendente (quem são os subordinados diretos e indiretos).

> [!note] Sufixo _DN
> O sufixo `_DN` indica tabela **Denormalized** — dados pré-calculados para consultas diretas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Span of control** — medir o número de subordinados diretos e indiretos de cada gestor
- **Delegação de tarefas** — identificar todos os colaboradores sob responsabilidade de um gestor
- **Relatórios de headcount** — consolidar contagem de pessoas por gestor
- **Aprovações em cascata** — localizar substitutos ou escalações na cadeia de comando
- **Dashboards gerenciais** — exibir equipe completa de cada gestor

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MANAGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do gestor | PER_PERSONS | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do subordinado | PER_PERSONS | 🟢 90% |
| 3 | REPORTEE_LEVEL | NUMBER | NOT NULL | Hierarquia | Nível do subordinado (1=direto, 2=indireto, etc.) | — | 🟡 75% |
| 4 | MANAGER_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo do gestor | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 5 | PERSON_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo do subordinado | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 6 | MANAGER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de gestão (LINE_MANAGER, etc.) | — | 🟡 70% |
| 7 | PERSON_NAME | VARCHAR2(360) | NULL | Descritivo | Nome do subordinado | — | 🟡 70% |
| 8 | MANAGER_NAME | VARCHAR2(360) | NULL | Descritivo | Nome do gestor | — | 🟡 70% |
| 9 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 10 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `MANAGER_ID` e `PERSON_ID` (gestor dos subordinados na hierarquia)
- [[per_all_assignments_m]] — via `MANAGER_ASSIGNMENT_ID` e `PERSON_ASSIGNMENT_ID` (vínculo do gestor na hierarquia de subordinados)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Listar todos os subordinados diretos de um gestor
```sql
SELECT rdn.PERSON_ID, rdn.PERSON_NAME, rdn.REPORTEE_LEVEL
FROM   PER_MANAGER_HRCHY_REPORTEES_DN rdn
WHERE  rdn.MANAGER_ID = :p_manager_id
  AND  rdn.REPORTEE_LEVEL = 1
  AND  SYSDATE BETWEEN rdn.EFFECTIVE_START_DATE AND rdn.EFFECTIVE_END_DATE;
```

---

## Observações

- `REPORTEE_LEVEL` = 1 indica subordinado direto; valores maiores indicam subordinados indiretos.
- Tabela desnormalizada: dados são atualizados por processos batch.
- Útil para relatórios de headcount sem necessidade de recursão.

---

## Referências

- [Oracle Docs — PER_MANAGER_HRCHY_REPORTEES_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/permanagerhrhyreporteesdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[managerhierarchycfdndpvo|ManagerHierarchyCFDNDPVO]] (HCM · BICC: 36/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
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
| LEVEL10_REPORTEE_ASSIGNMENT_ID | Level10ReporteeAsgId | ✅ |
| LEVEL10_REPORTEE_PERSON_ID | Level10ReporteePersonId | ✅ |
| LEVEL11_REPORTEE_ASSIGNMENT_ID | Level11ReporteeAsgId | ✅ |
| LEVEL11_REPORTEE_PERSON_ID | Level11ReporteePersonId | ✅ |
| LEVEL12_REPORTEE_ASSIGNMENT_ID | Level12ReporteeAsgId | ✅ |
| LEVEL12_REPORTEE_PERSON_ID | Level12ReporteePersonId | ✅ |
| LEVEL13_REPORTEE_ASSIGNMENT_ID | Level13ReporteeAsgId | ✅ |
| LEVEL13_REPORTEE_PERSON_ID | Level13ReporteePersonId | ✅ |
| LEVEL14_REPORTEE_ASSIGNMENT_ID | Level14ReporteeAsgId | ✅ |
| LEVEL14_REPORTEE_PERSON_ID | Level14ReporteePersonId | ✅ |
| LEVEL15_REPORTEE_ASSIGNMENT_ID | Level15ReporteeAsgId | ✅ |
| LEVEL15_REPORTEE_PERSON_ID | Level15ReporteePersonId | ✅ |
| LEVEL16_REPORTEE_ASSIGNMENT_ID | Level16ReporteeAsgId | — |
| LEVEL16_REPORTEE_PERSON_ID | Level16ReporteePersonId | — |
| LEVEL17_REPORTEE_ASSIGNMENT_ID | Level17ReporteeAsgId | — |
| LEVEL17_REPORTEE_PERSON_ID | Level17ReporteePersonId | — |
| LEVEL18_REPORTEE_ASSIGNMENT_ID | Level18ReporteeAsgId | — |
| LEVEL18_REPORTEE_PERSON_ID | Level18ReporteePersonId | — |
| LEVEL19_REPORTEE_ASSIGNMENT_ID | Level19ReporteeAsgId | — |
| LEVEL19_REPORTEE_PERSON_ID | Level19ReporteePersonId | — |
| LEVEL1_REPORTEE_ASSIGNMENT_ID | Level1ReporteeAsgId | ✅ |
| LEVEL1_REPORTEE_PERSON_ID | Level1ReporteePersonId | ✅ |
| LEVEL20_REPORTEE_ASSIGNMENT_ID | Level20ReporteeAsgId | — |
| LEVEL20_REPORTEE_PERSON_ID | Level20ReporteePersonId | — |
| LEVEL2_REPORTEE_ASSIGNMENT_ID | Level2ReporteeAsgId | ✅ |
| LEVEL2_REPORTEE_PERSON_ID | Level2ReporteePersonId | ✅ |
| LEVEL3_REPORTEE_ASSIGNMENT_ID | Level3ReporteeAsgId | ✅ |
| LEVEL3_REPORTEE_PERSON_ID | Level3ReporteePersonId | ✅ |
| LEVEL4_REPORTEE_ASSIGNMENT_ID | Level4ReporteeAsgId | ✅ |
| LEVEL4_REPORTEE_PERSON_ID | Level4ReporteePersonId | ✅ |
| LEVEL5_REPORTEE_ASSIGNMENT_ID | Level5ReporteeAsgId | ✅ |
| LEVEL5_REPORTEE_PERSON_ID | Level5ReporteePersonId | ✅ |
| LEVEL6_REPORTEE_ASSIGNMENT_ID | Level6ReporteeAsgId | ✅ |
| LEVEL6_REPORTEE_PERSON_ID | Level6ReporteePersonId | ✅ |
| LEVEL7_REPORTEE_ASSIGNMENT_ID | Level7ReporteeAsgId | ✅ |
| LEVEL7_REPORTEE_PERSON_ID | Level7ReporteePersonId | ✅ |
| LEVEL8_REPORTEE_ASSIGNMENT_ID | Level8ReporteeAsgId | ✅ |
| LEVEL8_REPORTEE_PERSON_ID | Level8ReporteePersonId | ✅ |
| LEVEL9_REPORTEE_ASSIGNMENT_ID | Level9ReporteeAsgId | ✅ |
| LEVEL9_REPORTEE_PERSON_ID | Level9ReporteePersonId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MANAGER_TYPE | Level10ReporteeManagerType | — |
| MANAGER_TYPE | Level11ReporteeManagerType | — |
| MANAGER_TYPE | Level12ReporteeManagerType | — |
| MANAGER_TYPE | Level13ReporteeManagerType | — |
| MANAGER_TYPE | Level14ReporteeManagerType | — |
| MANAGER_TYPE | Level15ReporteeManagerType | — |
| MANAGER_TYPE | Level16ReporteeManagerType | — |
| MANAGER_TYPE | Level17ReporteeManagerType | — |
| MANAGER_TYPE | Level18ReporteeManagerType | — |
| MANAGER_TYPE | Level19ReporteeManagerType | — |
| MANAGER_TYPE | Level1ReporteeManagerType | — |
| MANAGER_TYPE | Level20ReporteeManagerType | — |
| MANAGER_TYPE | Level2ReporteeManagerType | — |
| MANAGER_TYPE | Level3ReporteeManagerType | — |
| MANAGER_TYPE | Level4ReporteeManagerType | — |
| MANAGER_TYPE | Level5ReporteeManagerType | — |
| MANAGER_TYPE | Level6ReporteeManagerType | — |
| MANAGER_TYPE | Level7ReporteeManagerType | — |
| MANAGER_TYPE | Level8ReporteeManagerType | — |
| MANAGER_TYPE | Level9ReporteeManagerType | — |
| MANAGER_TYPE | ManagerType | — |
| REQUEST_ID | RequestId | — |

### [[managerhrchyreporteesdnextractpvo|ManagerHrchyReporteesDNExtractPVO]] (HCM · BICC: 55/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEVEL10_REPORTEE_ASSIGNMENT_ID | Level10ReporteeAssignmentId | ✅ |
| LEVEL10_REPORTEE_PERSON_ID | Level10ReporteePersonId | ✅ |
| LEVEL11_REPORTEE_ASSIGNMENT_ID | Level11ReporteeAssignmentId | ✅ |
| LEVEL11_REPORTEE_PERSON_ID | Level11ReporteePersonId | ✅ |
| LEVEL12_REPORTEE_ASSIGNMENT_ID | Level12ReporteeAssignmentId | ✅ |
| LEVEL12_REPORTEE_PERSON_ID | Level12ReporteePersonId | ✅ |
| LEVEL13_REPORTEE_ASSIGNMENT_ID | Level13ReporteeAssignmentId | ✅ |
| LEVEL13_REPORTEE_PERSON_ID | Level13ReporteePersonId | ✅ |
| LEVEL14_REPORTEE_ASSIGNMENT_ID | Level14ReporteeAssignmentId | ✅ |
| LEVEL14_REPORTEE_PERSON_ID | Level14ReporteePersonId | ✅ |
| LEVEL15_REPORTEE_ASSIGNMENT_ID | Level15ReporteeAssignmentId | ✅ |
| LEVEL15_REPORTEE_PERSON_ID | Level15ReporteePersonId | ✅ |
| LEVEL16_REPORTEE_ASSIGNMENT_ID | Level16ReporteeAssignmentId | ✅ |
| LEVEL16_REPORTEE_PERSON_ID | Level16ReporteePersonId | ✅ |
| LEVEL17_REPORTEE_ASSIGNMENT_ID | Level17ReporteeAssignmentId | ✅ |
| LEVEL17_REPORTEE_PERSON_ID | Level17ReporteePersonId | ✅ |
| LEVEL18_REPORTEE_ASSIGNMENT_ID | Level18ReporteeAssignmentId | ✅ |
| LEVEL18_REPORTEE_PERSON_ID | Level18ReporteePersonId | ✅ |
| LEVEL19_REPORTEE_ASSIGNMENT_ID | Level19ReporteeAssignmentId | ✅ |
| LEVEL19_REPORTEE_PERSON_ID | Level19ReporteePersonId | ✅ |
| LEVEL1_REPORTEE_ASSIGNMENT_ID | Level1ReporteeAssignmentId | ✅ |
| LEVEL1_REPORTEE_PERSON_ID | Level1ReporteePersonId | ✅ |
| LEVEL20_REPORTEE_ASSIGNMENT_ID | Level20ReporteeAssignmentId | ✅ |
| LEVEL20_REPORTEE_PERSON_ID | Level20ReporteePersonId | ✅ |
| LEVEL2_REPORTEE_ASSIGNMENT_ID | Level2ReporteeAssignmentId | ✅ |
| LEVEL2_REPORTEE_PERSON_ID | Level2ReporteePersonId | ✅ |
| LEVEL3_REPORTEE_ASSIGNMENT_ID | Level3ReporteeAssignmentId | ✅ |
| LEVEL3_REPORTEE_PERSON_ID | Level3ReporteePersonId | ✅ |
| LEVEL4_REPORTEE_ASSIGNMENT_ID | Level4ReporteeAssignmentId | ✅ |
| LEVEL4_REPORTEE_PERSON_ID | Level4ReporteePersonId | ✅ |
| LEVEL5_REPORTEE_ASSIGNMENT_ID | Level5ReporteeAssignmentId | ✅ |
| LEVEL5_REPORTEE_PERSON_ID | Level5ReporteePersonId | ✅ |
| LEVEL6_REPORTEE_ASSIGNMENT_ID | Level6ReporteeAssignmentId | ✅ |
| LEVEL6_REPORTEE_PERSON_ID | Level6ReporteePersonId | ✅ |
| LEVEL7_REPORTEE_ASSIGNMENT_ID | Level7ReporteeAssignmentId | ✅ |
| LEVEL7_REPORTEE_PERSON_ID | Level7ReporteePersonId | ✅ |
| LEVEL8_REPORTEE_ASSIGNMENT_ID | Level8ReporteeAssignmentId | ✅ |
| LEVEL8_REPORTEE_PERSON_ID | Level8ReporteePersonId | ✅ |
| LEVEL9_REPORTEE_ASSIGNMENT_ID | Level9ReporteeAssignmentId | ✅ |
| LEVEL9_REPORTEE_PERSON_ID | Level9ReporteePersonId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MANAGER_TYPE | ManagerType | ✅ |
| REQUEST_ID | RequestId | ✅ |

### [[matrixmanagerhierarchycfdndpvo|MatrixManagerHierarchyCFDNDPVO]] (HCM · BICC: 23/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
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
| LEVEL10_REPORTEE_ASSIGNMENT_ID | Level10ReporteeAsgId | — |
| LEVEL10_REPORTEE_PERSON_ID | Level10ReporteePersonId | — |
| LEVEL11_REPORTEE_ASSIGNMENT_ID | Level11ReporteeAsgId | — |
| LEVEL11_REPORTEE_PERSON_ID | Level11ReporteePersonId | — |
| LEVEL12_REPORTEE_ASSIGNMENT_ID | Level12ReporteeAsgId | — |
| LEVEL12_REPORTEE_PERSON_ID | Level12ReporteePersonId | — |
| LEVEL13_REPORTEE_ASSIGNMENT_ID | Level13ReporteeAsgId | — |
| LEVEL13_REPORTEE_PERSON_ID | Level13ReporteePersonId | — |
| LEVEL14_REPORTEE_ASSIGNMENT_ID | Level14ReporteeAsgId | — |
| LEVEL14_REPORTEE_PERSON_ID | Level14ReporteePersonId | — |
| LEVEL15_REPORTEE_ASSIGNMENT_ID | Level15ReporteeAsgId | ✅ |
| LEVEL15_REPORTEE_PERSON_ID | Level15ReporteePersonId | — |
| LEVEL16_REPORTEE_ASSIGNMENT_ID | Level16ReporteeAsgId | — |
| LEVEL16_REPORTEE_PERSON_ID | Level16ReporteePersonId | — |
| LEVEL17_REPORTEE_ASSIGNMENT_ID | Level17ReporteeAsgId | — |
| LEVEL17_REPORTEE_PERSON_ID | Level17ReporteePersonId | — |
| LEVEL18_REPORTEE_ASSIGNMENT_ID | Level18ReporteeAsgId | — |
| LEVEL18_REPORTEE_PERSON_ID | Level18ReporteePersonId | — |
| LEVEL19_REPORTEE_ASSIGNMENT_ID | Level19ReporteeAsgId | — |
| LEVEL19_REPORTEE_PERSON_ID | Level19ReporteePersonId | — |
| LEVEL1_REPORTEE_ASSIGNMENT_ID | Level1ReporteeAsgId | — |
| LEVEL1_REPORTEE_PERSON_ID | Level1ReporteePersonId | — |
| LEVEL20_REPORTEE_ASSIGNMENT_ID | Level20ReporteeAsgId | — |
| LEVEL20_REPORTEE_PERSON_ID | Level20ReporteePersonId | — |
| LEVEL2_REPORTEE_ASSIGNMENT_ID | Level2ReporteeAsgId | — |
| LEVEL2_REPORTEE_PERSON_ID | Level2ReporteePersonId | — |
| LEVEL3_REPORTEE_ASSIGNMENT_ID | Level3ReporteeAsgId | — |
| LEVEL3_REPORTEE_PERSON_ID | Level3ReporteePersonId | — |
| LEVEL4_REPORTEE_ASSIGNMENT_ID | Level4ReporteeAsgId | — |
| LEVEL4_REPORTEE_PERSON_ID | Level4ReporteePersonId | — |
| LEVEL5_REPORTEE_ASSIGNMENT_ID | Level5ReporteeAsgId | — |
| LEVEL5_REPORTEE_PERSON_ID | Level5ReporteePersonId | — |
| LEVEL6_REPORTEE_ASSIGNMENT_ID | Level6ReporteeAsgId | — |
| LEVEL6_REPORTEE_PERSON_ID | Level6ReporteePersonId | — |
| LEVEL7_REPORTEE_ASSIGNMENT_ID | Level7ReporteeAsgId | — |
| LEVEL7_REPORTEE_PERSON_ID | Level7ReporteePersonId | — |
| LEVEL8_REPORTEE_ASSIGNMENT_ID | Level8ReporteeAsgId | — |
| LEVEL8_REPORTEE_PERSON_ID | Level8ReporteePersonId | — |
| LEVEL9_REPORTEE_ASSIGNMENT_ID | Level9ReporteeAsgId | — |
| LEVEL9_REPORTEE_PERSON_ID | Level9ReporteePersonId | — |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MANAGER_TYPE | Level10ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level11ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level12ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level13ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level14ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level15ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level16ReporteeManagerType | — |
| MANAGER_TYPE | Level17ReporteeManagerType | — |
| MANAGER_TYPE | Level18ReporteeManagerType | — |
| MANAGER_TYPE | Level19ReporteeManagerType | — |
| MANAGER_TYPE | Level1ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level20ReporteeManagerType | — |
| MANAGER_TYPE | Level2ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level3ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level4ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level5ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level6ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level7ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level8ReporteeManagerType | ✅ |
| MANAGER_TYPE | Level9ReporteeManagerType | ✅ |
| MANAGER_TYPE | ManagerType | ✅ |
| REQUEST_ID | RequestId | — |

### [[unsecuredmanagerhierarchycfdndpvo|UnsecuredManagerHierarchyCFDNDPVO]] (HCM · BICC: 35/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
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
| LEVEL10_REPORTEE_ASSIGNMENT_ID | Level10ReporteeAsgId | ✅ |
| LEVEL10_REPORTEE_PERSON_ID | Level10ReporteePersonId | ✅ |
| LEVEL11_REPORTEE_ASSIGNMENT_ID | Level11ReporteeAsgId | ✅ |
| LEVEL11_REPORTEE_PERSON_ID | Level11ReporteePersonId | ✅ |
| LEVEL12_REPORTEE_ASSIGNMENT_ID | Level12ReporteeAsgId | ✅ |
| LEVEL12_REPORTEE_PERSON_ID | Level12ReporteePersonId | ✅ |
| LEVEL13_REPORTEE_ASSIGNMENT_ID | Level13ReporteeAsgId | ✅ |
| LEVEL13_REPORTEE_PERSON_ID | Level13ReporteePersonId | ✅ |
| LEVEL14_REPORTEE_ASSIGNMENT_ID | Level14ReporteeAsgId | ✅ |
| LEVEL14_REPORTEE_PERSON_ID | Level14ReporteePersonId | ✅ |
| LEVEL15_REPORTEE_ASSIGNMENT_ID | Level15ReporteeAsgId | ✅ |
| LEVEL15_REPORTEE_PERSON_ID | Level15ReporteePersonId | ✅ |
| LEVEL16_REPORTEE_ASSIGNMENT_ID | Level16ReporteeAsgId | — |
| LEVEL16_REPORTEE_PERSON_ID | Level16ReporteePersonId | — |
| LEVEL17_REPORTEE_ASSIGNMENT_ID | Level17ReporteeAsgId | — |
| LEVEL17_REPORTEE_PERSON_ID | Level17ReporteePersonId | — |
| LEVEL18_REPORTEE_ASSIGNMENT_ID | Level18ReporteeAsgId | — |
| LEVEL18_REPORTEE_PERSON_ID | Level18ReporteePersonId | — |
| LEVEL19_REPORTEE_ASSIGNMENT_ID | Level19ReporteeAsgId | — |
| LEVEL19_REPORTEE_PERSON_ID | Level19ReporteePersonId | — |
| LEVEL1_REPORTEE_ASSIGNMENT_ID | Level1ReporteeAsgId | ✅ |
| LEVEL1_REPORTEE_PERSON_ID | Level1ReporteePersonId | ✅ |
| LEVEL20_REPORTEE_ASSIGNMENT_ID | Level20ReporteeAsgId | — |
| LEVEL20_REPORTEE_PERSON_ID | Level20ReporteePersonId | — |
| LEVEL2_REPORTEE_ASSIGNMENT_ID | Level2ReporteeAsgId | ✅ |
| LEVEL2_REPORTEE_PERSON_ID | Level2ReporteePersonId | ✅ |
| LEVEL3_REPORTEE_ASSIGNMENT_ID | Level3ReporteeAsgId | ✅ |
| LEVEL3_REPORTEE_PERSON_ID | Level3ReporteePersonId | ✅ |
| LEVEL4_REPORTEE_ASSIGNMENT_ID | Level4ReporteeAsgId | ✅ |
| LEVEL4_REPORTEE_PERSON_ID | Level4ReporteePersonId | ✅ |
| LEVEL5_REPORTEE_ASSIGNMENT_ID | Level5ReporteeAsgId | ✅ |
| LEVEL5_REPORTEE_PERSON_ID | Level5ReporteePersonId | ✅ |
| LEVEL6_REPORTEE_ASSIGNMENT_ID | Level6ReporteeAsgId | ✅ |
| LEVEL6_REPORTEE_PERSON_ID | Level6ReporteePersonId | ✅ |
| LEVEL7_REPORTEE_ASSIGNMENT_ID | Level7ReporteeAsgId | ✅ |
| LEVEL7_REPORTEE_PERSON_ID | Level7ReporteePersonId | ✅ |
| LEVEL8_REPORTEE_ASSIGNMENT_ID | Level8ReporteeAsgId | ✅ |
| LEVEL8_REPORTEE_PERSON_ID | Level8ReporteePersonId | ✅ |
| LEVEL9_REPORTEE_ASSIGNMENT_ID | Level9ReporteeAsgId | ✅ |
| LEVEL9_REPORTEE_PERSON_ID | Level9ReporteePersonId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MANAGER_LEVEL | ManagerLevel | — |
| MANAGER_TYPE | Level10ReporteeManagerType | — |
| MANAGER_TYPE | Level11ReporteeManagerType | — |
| MANAGER_TYPE | Level12ReporteeManagerType | — |
| MANAGER_TYPE | Level13ReporteeManagerType | — |
| MANAGER_TYPE | Level14ReporteeManagerType | — |
| MANAGER_TYPE | Level15ReporteeManagerType | — |
| MANAGER_TYPE | Level16ReporteeManagerType | — |
| MANAGER_TYPE | Level17ReporteeManagerType | — |
| MANAGER_TYPE | Level18ReporteeManagerType | — |
| MANAGER_TYPE | Level19ReporteeManagerType | — |
| MANAGER_TYPE | Level1ReporteeManagerType | — |
| MANAGER_TYPE | Level20ReporteeManagerType | — |
| MANAGER_TYPE | Level2ReporteeManagerType | — |
| MANAGER_TYPE | Level3ReporteeManagerType | — |
| MANAGER_TYPE | Level4ReporteeManagerType | — |
| MANAGER_TYPE | Level5ReporteeManagerType | — |
| MANAGER_TYPE | Level6ReporteeManagerType | — |
| MANAGER_TYPE | Level7ReporteeManagerType | — |
| MANAGER_TYPE | Level8ReporteeManagerType | — |
| MANAGER_TYPE | Level9ReporteeManagerType | — |
| MANAGER_TYPE | ManagerType | — |
| REQUEST_ID | RequestId | — |
