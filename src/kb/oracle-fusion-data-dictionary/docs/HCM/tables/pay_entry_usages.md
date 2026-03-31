---
id: DOC-HCM-577
doc_type: system-doc
title: "PAY_ENTRY_USAGES — Usos de Entradas de Elementos"
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
  - entry-usages
  - usos
  - pay-entry-usages
aliases:
  - PAY_ENTRY_USAGES
  - pay_entry_usages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ENTRY_USAGES

## 📌 Visão Geral

Armazena os **usos** (usages) de entradas de elementos, controlando como cada entrada eh processada em execucoes especificas de folha. Define se uma entrada deve ser incluida, excluida ou ajustada em um processamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Controle de inclusao/exclusao de entradas por processamento
- Ajustes retroativos e correcoes de folha
- Rastreamento de processamento por entrada

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ENTRY_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do uso | --- | 🟢 85% |
| 2 | ELEMENT_ENTRY_ID | NUMBER(18) | NOT NULL | FK | ID da entrada de elemento | PAY_ELEMENT_ENTRIES_F | 🟢 85% |
| 3 | PAYROLL_ACTION_ID | NUMBER(18) | NULL | FK | ID da acao de folha | PAY_PAYROLL_ACTIONS | 🟡 75% |
| 4 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de uso | --- | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_entries_f]] --- via `ELEMENT_ENTRY_ID` (entrada de elemento utilizada no processamento)
- [[pay_payroll_actions]] --- via `PAYROLL_ACTION_ID` (ação de folha que consumiu a entrada)

### Tabelas-filha (FK de saída)
- --- Tabela de controle, sem filhas conhecidas

---

## 📎 Uso Típico

### Usos de uma entrada de elemento
```sql
SELECT eu.ENTRY_USAGE_ID, eu.USAGE_TYPE
FROM   PAY_ENTRY_USAGES eu
WHERE  eu.ELEMENT_ENTRY_ID = :p_entry_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_ENTRY_USAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payentryusages.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
