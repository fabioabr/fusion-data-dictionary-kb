---
id: DOC-HCM-619
doc_type: system-doc
title: "PER_ALLOCATED_CHECKLISTS — Checklists Alocados"
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
  - checklists
  - onboarding
aliases:
  - PER_ALLOCATED_CHECKLISTS
  - per_allocated_checklists
  - per-allocated-checklists
  - checklists-alocados
  - per-allocated-checkl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_CHECKLISTS

## 📌 Visão Geral

Armazena os **checklists alocados** a colaboradores para processos específicos (onboarding, offboarding, transferência). Cada registro representa uma instância de checklist atribuída a uma pessoa.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding** — acompanhamento de tarefas para novos colaboradores.
- **Offboarding** — checklist de desligamento com itens obrigatórios.
- **Transferências** — tarefas necessárias para mudança de área.
- **Compliance** — garantia de que todos os itens obrigatórios foram completados.
- **Gestão de progresso** — acompanhamento do status de cada checklist.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único do checklist alocado | — | 🟢 95% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Template de checklist | PER_CHECKLISTS_B | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador associado | PER_ALL_PEOPLE_F | 🟢 90% |
| 4 | CHECKLIST_STATUS | VARCHAR2(30) | NULL | Status | Status do checklist (NOT_STARTED, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 5 | ALLOCATION_DATE | DATE | NOT NULL | Período | Data de alocação do checklist | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (template de checklist)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador responsável pelo checklist)

### Tabelas-filha (FK de saída)
- [[per_allocated_checklists_tl]] — via `ALLOCATED_CHECKLIST_ID` (traduções do checklist alocado)
- [[per_allocated_tasks]] — via `ALLOCATED_CHECKLIST_ID` (tarefas alocadas)
- [[per_alloc_chklst_contacts]] — via `ALLOCATED_CHECKLIST_ID` (contatos do checklist alocado)
- [[per_alloc_chklst_contents]] — via `ALLOCATED_CHECKLIST_ID` (conteúdos do checklist alocado)

---

## 📎 Uso Típico

### Checklists em andamento de um colaborador
```sql
SELECT pac.ALLOCATED_CHECKLIST_ID, pac.CHECKLIST_STATUS, pac.ALLOCATION_DATE
FROM   PER_ALLOCATED_CHECKLISTS pac
WHERE  pac.PERSON_ID = :p_person_id
  AND  pac.CHECKLIST_STATUS != 'COMPLETED';
```

### Filtros comuns
- `CHECKLIST_STATUS = 'IN_PROGRESS'` — Checklists em andamento
- `ALLOCATION_DATE >= TRUNC(SYSDATE, 'MONTH')` — Alocados no mês corrente
---

## 🔒 Observações

- Cada checklist alocado é uma instância do template definido em PER_CHECKLISTS_B.
- O status do checklist é atualizado conforme as tarefas individuais são completadas.
- Contatos e conteúdos específicos podem ser adicionados a cada instância.
---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_CHECKLISTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedchecklists.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
