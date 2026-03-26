---
id: DOC-HCM-569
doc_type: system-doc
title: "PAY_ELEMENT_CRITERIA — Criterios de Elementos de Folha"
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
  - element-criteria
  - criterios
  - pay-elem-criteria
aliases:
  - PAY_ELEMENT_CRITERIA
  - pay_element_criteria
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_CRITERIA

## 📌 Visão Geral

Armazena os **criterios de elegibilidade** que determinam quais colaboradores recebem um determinado elemento de folha. Define regras baseadas em atributos como cargo, departamento, localizacao, etc.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de criterios de elegibilidade por elemento
- Controle de distribuicao automatica de elementos
- Configuracao de regras de inclusao/exclusao

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_CRITERIA_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do criterio | --- | 🟢 85% |
| 2 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 90% |
| 3 | CRITERIA_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de criterio (job, department, grade) | --- | 🟡 75% |
| 4 | CRITERIA_VALUE | VARCHAR2(240) | NULL | Dados | Valor do criterio | --- | 🟡 70% |
| 5 | INCLUSION_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica inclusao (Y) ou exclusao (N) | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tipo de elemento ao qual o critÃ©rio se aplica)

### Tabelas-filha (FK de saída)
- --- Tabela de criterio, sem filhas conhecidas

---

## 📎 Uso Típico

### Criterios de um tipo de elemento
```sql
SELECT ec.ELEMENT_CRITERIA_ID, ec.CRITERIA_TYPE, ec.CRITERIA_VALUE
FROM   PAY_ELEMENT_CRITERIA ec
WHERE  ec.ELEMENT_TYPE_ID = :p_element_type_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_CRITERIA](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelementcriteria.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
