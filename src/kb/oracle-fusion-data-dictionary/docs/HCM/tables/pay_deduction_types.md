---
id: DOC-HCM-561
doc_type: system-doc
title: "PAY_DEDUCTION_TYPES — Tipos de Desconto de Folha"
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
  - deduction-types
  - descontos
  - pay-ded-types
aliases:
  - PAY_DEDUCTION_TYPES
  - pay_deduction_types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DEDUCTION_TYPES

## 📌 Visão Geral

Armazena os **tipos de desconto** (involuntarios e voluntarios) aplicaveis na folha de pagamento (ex.: pensao alimenticia, emprestimo consignado, contribuicao sindical).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de tipos de desconto para folha
- Configuracao de regras de calculo por tipo de desconto
- Base para lancamentos de descontos em entradas de elementos

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DEDUCTION_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de desconto | --- | 🟢 90% |
| 2 | DEDUCTION_TYPE_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de desconto | --- | 🟢 85% |
| 3 | DEDUCTION_CATEGORY | VARCHAR2(30) | NULL | Classificacao | Categoria (involuntary, voluntary, tax) | --- | 🟢 80% |
| 4 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 5 | PROCESSING_PRIORITY | NUMBER | NULL | Dados | Prioridade de processamento | --- | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_deduction_groups_vl]] --- via `DEDUCTION_GROUP_ID` (grupo ao qual pertence a dedução)

### Tabelas-filha (FK de saída)
- [[pay_deduction_types_tl]] --- via `DEDUCTION_TYPE_ID` (traduções do tipo de dedução)

---

## 📎 Uso Típico

### Tipos de desconto por grupo legislativo
```sql
SELECT dt.DEDUCTION_TYPE_ID, dt.DEDUCTION_TYPE_NAME, dt.DEDUCTION_CATEGORY
FROM   PAY_DEDUCTION_TYPES dt
WHERE  dt.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_DEDUCTION_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydeductiontypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
