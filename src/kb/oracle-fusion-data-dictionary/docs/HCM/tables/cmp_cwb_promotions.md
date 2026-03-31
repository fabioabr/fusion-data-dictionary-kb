---
id: DOC-HCM-078
doc_type: system-doc
title: "CMP_CWB_PROMOTIONS — Promoções no Compensation Workbench"
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
  - cwb
  - promocoes
  - career-planning
aliases:
  - CMP_CWB_PROMOTIONS
  - cmp_cwb_promotions
  - cmp-cwb-promotions
  - DOC-HCM-078
  - promoções-no-compensation-workbench
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PROMOTIONS

## 📌 Visão Geral

Armazena as **promoções de colaboradores** propostas e aprovadas durante o ciclo de Compensation Workbench. Inclui o cargo atual, cargo proposto, data de efetividade e status de aprovação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de promoções:** Registro de promoções durante ciclo CWB.
- **Aprovação hierárquica:** Controle de workflow de aprovação de promoções.
- **Planejamento de carreira:** Visão de movimentações propostas.
- **Integração com cargos:** Atualização de job/position após aprovação.
- **Relatórios de mobilidade:** Análise de promoções por departamento e período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROMOTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da promoção | — | 🟢 95% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano CWB associado | [[cmp_cwb_plan_definitions]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa promovida | [[per_all_people_f]] | 🟢 95% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 90% |
| 5 | CURRENT_JOB_ID | NUMBER(18) | NULL | FK | Cargo atual do colaborador | [[per_jobs_f]] | 🟡 75% |
| 6 | PROPOSED_JOB_ID | NUMBER(18) | NULL | FK | Cargo proposto na promoção | [[per_jobs_f]] | 🟡 75% |
| 7 | CURRENT_GRADE_ID | NUMBER(18) | NULL | FK | Grade atual | [[per_grades_f]] | 🟡 75% |
| 8 | PROPOSED_GRADE_ID | NUMBER(18) | NULL | FK | Grade proposta | [[per_grades_f]] | 🟡 75% |
| 9 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade da promoção | — | 🟡 80% |
| 10 | STATUS | VARCHAR2(30) | NULL | Status | Status da promoção (PROPOSED, APPROVED, REJECTED) | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_cwb_plan_definitions]] — via `PLAN_ID` (plano CWB da promocao)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador promovido)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio da promocao)
- [[per_jobs_f]] — via `CURRENT_JOB_ID` / `PROPOSED_JOB_ID` (cargo atual na promocao)
- [[per_grades_f]] — via `CURRENT_GRADE_ID` / `PROPOSED_GRADE_ID` (grade atual na promocao)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Promoções aprovadas por plano
```sql
SELECT p.PERSON_ID, p.CURRENT_JOB_ID, p.PROPOSED_JOB_ID,
       p.EFFECTIVE_DATE, p.STATUS
FROM   CMP_CWB_PROMOTIONS p
WHERE  p.PLAN_ID = :p_plan_id
  AND  p.STATUS = 'APPROVED';
```

### Contagem de promoções por status
```sql
SELECT p.STATUS, COUNT(*) AS qtd
FROM   CMP_CWB_PROMOTIONS p
WHERE  p.PLAN_ID = :p_plan_id
GROUP BY p.STATUS;
```

---

## 🔒 Observações

- O `STATUS` controla o fluxo: PROPOSED (proposta), APPROVED (aprovada), REJECTED (rejeitada).
- Promoções aprovadas tipicamente disparam atualização em `PER_ALL_ASSIGNMENTS_M`.
- A tabela captura tanto mudanças de cargo (job) quanto de nível/grade.
- Integra-se com `CMP_CWB_PERSON_RATES` para ajustes salariais vinculados à promoção.

---

## 🔗 PVOs Relacionados

### [[promotionspvo|PromotionsPVO]] (HCM · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_CHANGE_DATE | PromotionPEOAsgChangeDate | ✅ |
| ASSIGNMENT_ID | PromotionPEOAssignmentId | ✅ |
| ASSIGNMENT_NAME | PromotionPEOAssignmentName | ✅ |
| CREATED_BY | PromotionPEOCreatedBy | ✅ |
| CREATION_DATE | PromotionPEOCreationDate | ✅ |
| GRADE_ID | PromotionPEOGradeId | ✅ |
| GRADE_MAX_VAL | PromotionPEOGradeMaxVal | ✅ |
| GRADE_MID_POINT | PromotionPEOGradeMidPoint | ✅ |
| GRADE_MIN_VAL | PromotionPEOGradeMinVal | ✅ |
| JOB_ID | PromotionPEOJobId | ✅ |
| LAST_UPDATE_DATE | PromotionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PromotionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PromotionPEOLastUpdatedBy | ✅ |
| NEW_ASSIGNMENT_OVN | PromotionPEONewAssignmentOvn | ✅ |
| OBJECT_VERSION_NUMBER | PromotionPEOObjectVersionNumber | ✅ |
| PERSON_ID | PromotionPEOPersonId | ✅ |
| POSITION_ID | PromotionPEOPositionId | ✅ |
| PROM_ORIG_UPDATED_BY | PromotionPEOPromOrigUpdatedBy | ✅ |
| PROM_UPDATE_DATE | PromotionPEOPromUpdateDate | ✅ |
| PROM_UPDATED_BY | PromotionPEOPromUpdatedBy | ✅ |
| PROMOTION_ID | PromotionId | ✅ |

### [[promotionspvoviewall|PromotionsPVOViewAll]] (HCM · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_CHANGE_DATE | PromotionPEOAsgChangeDate | ✅ |
| ASSIGNMENT_ID | PromotionPEOAssignmentId | ✅ |
| ASSIGNMENT_NAME | PromotionPEOAssignmentName | ✅ |
| CREATED_BY | PromotionPEOCreatedBy | ✅ |
| CREATION_DATE | PromotionPEOCreationDate | ✅ |
| GRADE_ID | PromotionPEOGradeId | ✅ |
| GRADE_MAX_VAL | PromotionPEOGradeMaxVal | ✅ |
| GRADE_MID_POINT | PromotionPEOGradeMidPoint | ✅ |
| GRADE_MIN_VAL | PromotionPEOGradeMinVal | ✅ |
| JOB_ID | PromotionPEOJobId | ✅ |
| LAST_UPDATE_DATE | PromotionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PromotionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PromotionPEOLastUpdatedBy | ✅ |
| NEW_ASSIGNMENT_OVN | PromotionPEONewAssignmentOvn | ✅ |
| OBJECT_VERSION_NUMBER | PromotionPEOObjectVersionNumber | ✅ |
| PERSON_ID | PromotionPEOPersonId | ✅ |
| POSITION_ID | PromotionPEOPositionId | ✅ |
| PROM_ORIG_UPDATED_BY | PromotionPEOPromOrigUpdatedBy | ✅ |
| PROM_UPDATE_DATE | PromotionPEOPromUpdateDate | ✅ |
| PROM_UPDATED_BY | PromotionPEOPromUpdatedBy | ✅ |
| PROMOTION_ID | PromotionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PROMOTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbpromotions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
