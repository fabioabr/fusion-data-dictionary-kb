---
id: DOC-HCM-626
doc_type: system-doc
title: "PER_ALL_ASSIGNMENTS_M — Atribuições/Designações (Materializada)"
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
  - workforce-management
  - assignments
  - designacoes
  - workforce
aliases:
  - PER_ALL_ASSIGNMENTS_M
  - per_all_assignments_m
  - per-all-assignments-m
  - atribuições/designações-(materializada)
  - per-all-assignments-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALL_ASSIGNMENTS_M

## 📌 Visão Geral

Tabela **materializada** que armazena todas as **atribuições (assignments)** de colaboradores. Contém informações sobre cargo, departamento, localização, grade, gerente e status de cada designação. É a tabela central para dados de workforce.

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **materializada** — combina dados de múltiplas fontes para otimização de consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de workforce** — dados centrais de cada vínculo empregatício/designação.
- **Hierarquia organizacional** — relaciona colaborador com departamento, cargo e gerente.
- **Folha de pagamento** — base para cálculos de remuneração por assignment.
- **Relatórios de headcount** — fonte principal para contagem de colaboradores.
- **Movimentações** — histórico completo de mudanças no assignment do colaborador.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do assignment | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | ASSIGNMENT_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número do assignment (ex.: E12345) | — | 🟢 95% |
| 6 | ASSIGNMENT_TYPE | VARCHAR2(1) | NOT NULL | Classificação | Tipo (E=Employee, C=Contingent, N=Non-worker) | — | 🟢 95% |
| 7 | ASSIGNMENT_STATUS_TYPE_ID | NUMBER(18) | NOT NULL | FK | Status do assignment | PER_ASSIGNMENT_STATUS_TYPES | 🟢 90% |
| 8 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Departamento/Organização | — | 🟢 90% |
| 9 | JOB_ID | NUMBER(18) | NULL | FK | Cargo (Job) | PER_JOBS_F | 🟢 90% |
| 10 | POSITION_ID | NUMBER(18) | NULL | FK | Posição | — | 🟢 90% |
| 11 | GRADE_ID | NUMBER(18) | NULL | FK | Grade salarial | PER_GRADES_F | 🟢 90% |
| 12 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização | PER_LOCATIONS | 🟢 90% |
| 13 | MANAGER_ID | NUMBER(18) | NULL | FK | Gerente direto | PER_ALL_PEOPLE_F | 🟢 85% |
| 14 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | FK | Entidade legal | — | 🟢 90% |
| 15 | BUSINESS_UNIT_ID | NUMBER(18) | NULL | FK | Unidade de negócio | — | 🟢 90% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 20 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador titular do vínculo empregatício)
- [[per_assignment_status_types]] — via `ASSIGNMENT_STATUS_TYPE_ID` (status do vínculo empregatício)
- [[per_jobs_f]] — via `JOB_ID` (cargo do vínculo empregatício)
- [[per_grades_f]] — via `GRADE_ID` (grade salarial do vínculo)
- [[per_locations]] — via `LOCATION_ID` (localização de trabalho do vínculo)

### Tabelas-filha (FK de saída)
- [[per_assignment_extra_info_m]] — via `ASSIGNMENT_ID` (informações extras)
- [[per_asg_responsibilities]] — via `ASSIGNMENT_ID` (responsabilidades)
- [[per_assignment_supervisors_f]] — via `ASSIGNMENT_ID` (supervisores do vínculo empregatício)
- [[per_assign_grade_steps_f]] — via `ASSIGNMENT_ID` (steps de grade salarial do vínculo)
- [[per_assign_work_measures_f]] — via `ASSIGNMENT_ID` (medidas de trabalho)

---

## 📎 Uso Típico

### Colaboradores ativos com cargo e departamento
```sql
SELECT paam.ASSIGNMENT_NUMBER, paam.ASSIGNMENT_TYPE,
       paam.ORGANIZATION_ID, paam.JOB_ID, paam.GRADE_ID
FROM   PER_ALL_ASSIGNMENTS_M paam
WHERE  paam.PERSON_ID = :p_person_id
  AND  paam.ASSIGNMENT_TYPE = 'E'
  AND  SYSDATE BETWEEN paam.EFFECTIVE_START_DATE AND paam.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ASSIGNMENT_TYPE = 'E'` — Empregados
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `ASSIGNMENT_STATUS_TYPE_ID` com status ACTIVE_ASSIGN — Assignments ativos
---

## 🔒 Observações

- Tabela materializada (_M) — combina dados de múltiplas fontes para performance.
- É a tabela mais consultada do HCM — base para praticamente todos os relatórios de workforce.
- Um colaborador pode ter múltiplos assignments simultaneamente (ex.: empregado + consultor).
- O `ASSIGNMENT_TYPE` é fundamental: E=Employee, C=Contingent Worker, N=Non-Worker.
- Sempre filtrar por vigência para obter o assignment corrente.
---

## 📚 Referências

- [Oracle Docs — PER_ALL_ASSIGNMENTS_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallassignmentsm.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
