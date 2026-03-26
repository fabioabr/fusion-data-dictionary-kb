---
id: DOC-HCM-725
doc_type: system-doc
title: "WLF_ASSIGNMENT_RECORDS_F — Registros de Atribuição (Learning)"
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
  - learning
  - workforce-learning
  - registros-atribuição
aliases:
  - WLF_ASSIGNMENT_RECORDS_F
  - wlf_assignment_records_f
  - wlf-assignment-records-f
  - registros-de-atribuição-learning
  - assignment-records
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_ASSIGNMENT_RECORDS_F

## Visão Geral

Armazena os **registros individuais de atribuição de aprendizado**, representando a inscrição/participação de um colaborador em um item de aprendizado. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inscrição em treinamentos** — registra a participação de cada colaborador.
- **Tracking de progresso** — acompanha o status de conclusão de cada atribuição.
- **Compliance** — evidência de conclusão de treinamentos obrigatórios.
- **Relatórios de desempenho** — análise de taxa de conclusão por pessoa/departamento.
- **Certificações** — vinculação de atribuições concluídas a certificações.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de atribuição | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa inscrita no aprendizado | PER_ALL_PEOPLE_F | 🟢 85% |
| 5 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado atribuído | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 6 | ASSIGNMENT_STATUS | VARCHAR2(30) | NULL | Status | Status da atribuição (enrolled, completed, etc.) | — | 🟡 80% |
| 7 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão | — | 🟡 80% |
| 8 | SCORE | NUMBER(5,2) | NULL | Dados | Nota/pontuação obtida | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa inscrita)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- [[wlf_ar_relations_f]] — via `ASSIGNMENT_RECORD_ID` (relações do registro)

---

## Uso Típico

### Atribuições concluídas por colaborador
```sql
SELECT ar.LEARNING_ITEM_ID, ar.COMPLETION_DATE, ar.SCORE, ar.ASSIGNMENT_STATUS
FROM   WLF_ASSIGNMENT_RECORDS_F ar
WHERE  ar.PERSON_ID = :p_person_id
  AND  ar.ASSIGNMENT_STATUS = 'COMPLETED'
  AND  SYSDATE BETWEEN ar.EFFECTIVE_START_DATE AND ar.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Atribuições de um colaborador
- `ASSIGNMENT_STATUS = 'COMPLETED'` — Apenas concluídos

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Cada registro representa uma inscrição individual em um item de aprendizado.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Relações com outros objetos são mantidas em WLF_AR_RELATIONS_F.

---

## Referências

- [Oracle Docs — WLF_ASSIGNMENT_RECORDS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfassignmentrecordsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
