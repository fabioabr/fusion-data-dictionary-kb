---
id: DOC-HCM-074
doc_type: system-doc
title: "CMP_CWB_PERSON_INFO — Informações de Pessoa no CWB"
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
  - cwb-person-info
  - compensacao-pessoa
  - salario
  - bonus
aliases:
  - CMP_CWB_PERSON_INFO
  - cmp_cwb_person_info
  - cwb-person-info-compensacao
  - cwb-person-info
  - cmp-cwb-person-info
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PERSON_INFO

## 📌 Visão Geral

Armazena as **informações consolidadas de compensação por pessoa** no Compensation Workbench. Contém salário atual, salário proposto, bônus, budget alocado e outros dados do ciclo de revisão. É a **tabela transacional principal** do CWB.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de compensação:** Dados consolidados por pessoa para cada ciclo de revisão.
- **Distribuição de compensação:** Valores propostos pelo gestor (salário, bônus, stock).
- **Orçamento:** Controle de uso do budget pool por gestor.
- **Workflow de aprovação:** Status de submissão/aprovação das propostas.
- **Relatórios analíticos:** Base para análise de compensação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CWB_PERSON_INFO_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de compensação | — | 🟢 90% |
| 4 | MANAGER_ID | NUMBER(18) | NULL | FK | Gestor responsável | [[per_all_people_f]] | 🟢 85% |
| 5 | CURRENT_SALARY | NUMBER | NULL | Financeiro | Salário atual | — | 🟢 85% |
| 6 | PROPOSED_SALARY | NUMBER | NULL | Financeiro | Salário proposto | — | 🟢 85% |
| 7 | MERIT_PERCENT | NUMBER | NULL | Percentual | Percentual de merit increase | — | 🟡 80% |
| 8 | BONUS_AMOUNT | NUMBER | NULL | Financeiro | Valor de bônus proposto | — | 🟡 80% |
| 9 | STOCK_AMOUNT | NUMBER | NULL | Financeiro | Valor de stock proposto | — | 🟡 75% |
| 10 | COMPA_RATIO | NUMBER | NULL | Indicador | Compa-ratio (salário/midpoint da faixa) | — | 🟡 80% |
| 11 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Workflow | Status (DRAFT, SUBMITTED, APPROVED, REJECTED) | — | 🟡 80% |
| 12 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda | — | 🟢 85% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 17 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` e `MANAGER_ID` (colaborador no workbench de compensacao)

### Tabelas-filha (FK de saída)
- [[cmp_cwb_alerts]] — via `CWB_PERSON_INFO_ID` (alertas do colaborador no workbench)

---

## 📎 Uso Típico

### Propostas de compensação por gestor
```sql
SELECT pi.PERSON_ID, pi.CURRENT_SALARY, pi.PROPOSED_SALARY,
       pi.MERIT_PERCENT, pi.BONUS_AMOUNT, pi.APPROVAL_STATUS
FROM   CMP_CWB_PERSON_INFO pi
WHERE  pi.MANAGER_ID = :p_manager_id
  AND  pi.PLAN_ID = :p_plan_id;
```

### Filtros comuns
- `APPROVAL_STATUS = 'SUBMITTED'` — Propostas submetidas
- `APPROVAL_STATUS = 'APPROVED'` — Propostas aprovadas
- `COMPA_RATIO < 0.8` — Colaboradores abaixo de 80% do midpoint

---

## 🔒 Observações

- Tabela transacional principal do CWB — contém dados de compensação sensíveis.
- `COMPA_RATIO` = salário / midpoint da faixa salarial (< 1.0 = abaixo do midpoint).
- Classificar como `restricted` ou `confidential` no Neo4j.
- O ciclo de vida: DRAFT → SUBMITTED → APPROVED/REJECTED.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PERSON_INFO](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbpersoninfo.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
