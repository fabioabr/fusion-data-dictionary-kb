---
id: DOC-HCM-634
doc_type: system-doc
title: "PER_ASSIGNMENT_SUPERVISORS_F — Supervisores de Assignment"
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
  - supervisores
  - assignment-supervisors
aliases:
  - PER_ASSIGNMENT_SUPERVISORS_F
  - per_assignment_supervisors_f
  - per-assignment-supervisors-f
  - supervisores-de-assignment
  - per-assignment-super
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_SUPERVISORS_F

## 📌 Visão Geral

Armazena os **supervisores/gestores** associados a cada assignment, com vigência temporal. Permite múltiplos supervisores por assignment (direto, matricial, funcional).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Hierarquia de reporte** — define a cadeia de supervisão de cada colaborador.
- **Gestão matricial** — suporte a múltiplos tipos de supervisor por assignment.
- **Workflow de aprovação** — determina quem aprova solicitações do colaborador.
- **Relatórios gerenciais** — visualização de equipes por gestor.
- **Delegação** — registro de supervisores temporários.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_SUPERVISOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de supervisão | — | 🟢 95% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment supervisionado | PER_ALL_ASSIGNMENTS_M | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | SUPERVISOR_ID | NUMBER(18) | NOT NULL | FK | Pessoa supervisora | PER_ALL_PEOPLE_F | 🟢 90% |
| 6 | SUPERVISOR_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de supervisão (LINE_MANAGER, PROJECT_MANAGER, etc.) | — | 🟢 90% |
| 7 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | Supervisor primário (Y/N) | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (assignment supervisionado)
- [[per_all_people_f]] — via `SUPERVISOR_ID` (pessoa que atua como supervisor do vínculo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Supervisor atual de um assignment
```sql
SELECT pasf.SUPERVISOR_ID, pasf.SUPERVISOR_TYPE, pasf.PRIMARY_FLAG
FROM   PER_ASSIGNMENT_SUPERVISORS_F pasf
WHERE  pasf.ASSIGNMENT_ID = :p_assignment_id
  AND  pasf.PRIMARY_FLAG = 'Y'
  AND  SYSDATE BETWEEN pasf.EFFECTIVE_START_DATE AND pasf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SUPERVISOR_TYPE = 'LINE_MANAGER'` — Gestor direto
- `PRIMARY_FLAG = 'Y'` — Supervisor primário
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Suporta múltiplos supervisores por assignment (ex.: gestor direto + gestor de projeto).
- O campo `SUPERVISOR_TYPE` define o tipo de relação de supervisão.
- A flag `PRIMARY_FLAG` identifica o supervisor principal para workflows de aprovação.
---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_SUPERVISORS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentsupervisorsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
