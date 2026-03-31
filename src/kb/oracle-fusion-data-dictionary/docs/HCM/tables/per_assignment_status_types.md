---
id: DOC-HCM-632
doc_type: system-doc
title: "PER_ASSIGNMENT_STATUS_TYPES — Tipos de Status de Assignment"
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
  - status
  - assignment-status
aliases:
  - PER_ASSIGNMENT_STATUS_TYPES
  - per_assignment_status_types
  - per-assignment-status-types
  - tipos-de-status-de-assignment
  - per-assignment-statu
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_STATUS_TYPES

## 📌 Visão Geral

Armazena os **tipos de status** que um assignment pode assumir. Define o ciclo de vida do assignment (ativo, suspenso, encerrado, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de vida** — define os status válidos para assignments.
- **Controle de estado** — determina se o colaborador está ativo, em licença, desligado, etc.
- **Filtros de relatório** — base para segmentação de workforce por status.
- **Integração com payroll** — status determina se o assignment gera folha de pagamento.
- **Compliance** — rastreamento de transições de status.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_STATUS_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de status | — | 🟢 95% |
| 2 | USER_STATUS | VARCHAR2(80) | NOT NULL | Identificação | Nome do status (visível ao usuário) | — | 🟢 90% |
| 3 | PER_SYSTEM_STATUS | VARCHAR2(30) | NULL | Classificação | Status do sistema (ACTIVE_ASSIGN, SUSP_ASSIGN, etc.) | — | 🟢 90% |
| 4 | PAY_SYSTEM_STATUS | VARCHAR2(30) | NULL | Classificação | Status para payroll (P=Process, D=Do Not Process) | — | 🟢 85% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se o tipo de status está ativo (Y/N) | — | 🟢 85% |
| 6 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Configuração | Se é o status padrão (Y/N) | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela de referência de status.

### Tabelas-filha (FK de saída)
- [[per_assignment_status_types_tl]] — via `ASSIGNMENT_STATUS_TYPE_ID` (traduções do tipo de status de vínculo)
- [[per_all_assignments_m]] — via `ASSIGNMENT_STATUS_TYPE_ID` (assignments com este status)

---

## 📎 Uso Típico

### Status de assignment ativos
```sql
SELECT past.ASSIGNMENT_STATUS_TYPE_ID, past.USER_STATUS,
       past.PER_SYSTEM_STATUS, past.PAY_SYSTEM_STATUS
FROM   PER_ASSIGNMENT_STATUS_TYPES past
WHERE  past.ACTIVE_FLAG = 'Y'
ORDER BY past.PER_SYSTEM_STATUS;
```

### Filtros comuns
- `PER_SYSTEM_STATUS = 'ACTIVE_ASSIGN'` — Assignments ativos
- `PAY_SYSTEM_STATUS = 'P'` — Status que geram processamento de payroll
---

## 🔒 Observações

- O `PER_SYSTEM_STATUS` classifica o status em nível de sistema (ACTIVE_ASSIGN, SUSP_ASSIGN, TERM_ASSIGN).
- O `PAY_SYSTEM_STATUS` determina se o assignment será processado na folha (P) ou não (D).
- Tabela de referência — registros pré-configurados pelo Oracle.
- A flag `DEFAULT_FLAG` indica qual status é aplicado automaticamente em novas admissões.
---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_STATUS_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentstatustypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
