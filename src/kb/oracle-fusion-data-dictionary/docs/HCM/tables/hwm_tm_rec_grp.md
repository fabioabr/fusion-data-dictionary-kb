---
id: DOC-HCM-382
doc_type: system-doc
title: "HWM_TM_REC_GRP — Grupos de Registros de Time Management"
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
  - time-management
  - record-group
  - grupo-registros
aliases:
  - HWM_TM_REC_GRP
  - hwm_tm_rec_grp
  - hwm-tm-rec-grp
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REC_GRP

## 📌 Visão Geral

Armazena os **agrupamentos de registros de tempo** (time record groups). Permite organizar registros de tempo em grupos lógicos para processamento em lote.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Processamento em lote:** agrupa registros de tempo para submissão conjunta.
- **Organização:** facilita a gestão de múltiplos registros de tempo.
- **Workflow de aprovação:** permite aprovar grupos inteiros de registros.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REC_GRP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do grupo | — | 🟡 70% |
| 2 | GROUP_NAME | VARCHAR2(240) | NULL | Identificação | Nome do grupo de registros | — | 🟡 60% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 4 | GROUP_DATE | DATE | NULL | Período | Data do grupo | — | 🟡 60% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do grupo | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do grupo de registros de tempo)

### Tabelas-filha (FK de saída)
- [[hwm_tm_rec_grp_usages]] — via `REC_GRP_ID` (usos do grupo de registros de tempo)

---

## 📎 Uso Típico

### Grupos de registros por colaborador
```sql
SELECT g.REC_GRP_ID, g.GROUP_NAME, g.STATUS
FROM   HWM_TM_REC_GRP g
WHERE  g.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `STATUS = :p_status — Filtrar por status`

---

## 🔒 Observações

- Tabela de agrupamento para processamento em lote de time records.
- Grupos facilitam a submissão e aprovação de múltiplos registros.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REC_GRP](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrecgrp.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
