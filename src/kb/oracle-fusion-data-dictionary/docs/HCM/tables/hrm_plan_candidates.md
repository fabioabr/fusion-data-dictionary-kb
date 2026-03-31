---
id: DOC-HCM-178
doc_type: system-doc
title: "HRM_PLAN_CANDIDATES — Candidatos a Sucessão"
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
  - succession
  - candidates
aliases:
  - HRM_PLAN_CANDIDATES
  - hrm_plan_candidates
  - candidatos-a-sucessão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRM_PLAN_CANDIDATES

## 📌 Visão Geral

Armazena **candidatos a sucessão** vinculados a planos. Potenciais sucessores com classificação de prontidão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Pool de sucessores:** Candidatos para posições-chave.
- **Prontidão:** Classificação de quando estarão prontos.
- **Talent pipeline:** Pipeline para posições críticas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_CANDIDATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano | [[hrm_plans_v]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Candidato | [[per_all_people_f]] | 🟢 90% |
| 4 | READINESS_CODE | VARCHAR2(30) | NULL | Classificação | Prontidão (READY_NOW, READY_1_2_YEARS) | — | 🟡 80% |
| 5 | RANKING | NUMBER | NULL | Métrica | Classificação (1=melhor) | — | 🟡 70% |
| 6 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários | — | 🟡 65% |
| 7 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, REMOVED) | — | 🟡 70% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrm_plans_v]] — via `PLAN_ID` (plano de sucessao do candidato)
- [[per_all_people_f]] — via `PERSON_ID` (candidato ao plano de sucessao)

---

## 📎 Uso Típico

### Candidatos de um plano
```sql
SELECT pc.PERSON_ID, pc.READINESS_CODE, pc.RANKING
FROM   HRM_PLAN_CANDIDATES pc
WHERE  pc.PLAN_ID = :p_id AND pc.STATUS_CODE = 'ACTIVE'
ORDER BY pc.RANKING;
```

---

## 🔒 Observações

- Múltiplos candidatos classificados por prontidão e ranking.

---

## 🔗 PVOs Relacionados

### [[plancandidatespvo|PlanCandidatesPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CANDIDATE_SINCE | CandidateSince | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
