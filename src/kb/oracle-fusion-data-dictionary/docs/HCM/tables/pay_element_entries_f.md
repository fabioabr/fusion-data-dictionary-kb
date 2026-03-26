---
id: DOC-HCM-570
doc_type: system-doc
title: "PAY_ELEMENT_ENTRIES_F — Entradas de Elementos de Folha"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - element-entries
  - entradas
  - pay-elem-entries
aliases:
  - PAY_ELEMENT_ENTRIES_F
  - pay_element_entries_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_ENTRIES_F

## 📌 Visão Geral

Tabela central que armazena as **entradas de elementos** (element entries) da folha de pagamento. Cada entrada vincula um elemento (provento ou desconto) a um colaborador com vigencia temporal. Eh o registro que efetivamente gera valores no calculo de folha.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Lancamento de proventos e descontos por colaborador
- Controle de vigencia de cada entrada de elemento
- Base para o calculo de folha de pagamento
- Historico de alteracoes em entradas

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da entrada | --- | 🟢 95% |
| 2 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 90% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | ID do assignment | PER_ALL_ASSIGNMENTS_M | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | ENTRY_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de entrada (E, D, A, R, B) | --- | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tipo de elemento da entrada de folha)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha da entrada de elemento)

### Tabelas-filha (FK de saída)
- [[pay_element_entry_values_f]] --- via `ELEMENT_ENTRY_ID` (valores das entradas)

---

## 📎 Uso Típico

### Entradas vigentes por relacionamento de folha
```sql
SELECT ee.ELEMENT_ENTRY_ID, ee.ELEMENT_TYPE_ID, ee.ENTRY_TYPE
FROM   PAY_ELEMENT_ENTRIES_F ee
WHERE  ee.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN ee.EFFECTIVE_START_DATE AND ee.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Os valores efetivos de cada entrada estao em `PAY_ELEMENT_ENTRY_VALUES_F`.
- Tipos de entrada: E=Regular, D=Deducao adicional, A=Ajuste, R=Retroativo, B=Saldo inicial.

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_ENTRIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelemententriesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
