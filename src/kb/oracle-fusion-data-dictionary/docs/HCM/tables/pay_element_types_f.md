---
id: DOC-HCM-573
doc_type: system-doc
title: "PAY_ELEMENT_TYPES_F — Tipos de Elementos de Folha"
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
  - element-types
  - tipos-elementos
  - pay-elem-types
aliases:
  - PAY_ELEMENT_TYPES_F
  - pay_element_types_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_TYPES_F

## 📌 Visão Geral

Tabela central que armazena as **definicoes de tipos de elementos** de folha de pagamento (proventos, descontos, impostos, informacoes). Cada tipo de elemento define um componente de remuneracao com suas regras de calculo e classificacao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de elementos de folha (salario base, adicional noturno, INSS, etc.)
- Configuracao de regras de processamento por tipo
- Classificacao de elementos por categoria (earnings, deductions, etc.)
- Base para criacao de entradas de elementos

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de elemento | --- | 🟢 95% |
| 2 | ELEMENT_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de elemento | --- | 🟢 95% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 90% |
| 4 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | FK | ID da classificacao do elemento | PAY_ELE_CLASSIFICATIONS | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | PROCESSING_PRIORITY | NUMBER | NULL | Dados | Prioridade de processamento | --- | 🟢 85% |
| 8 | PROCESSING_TYPE | VARCHAR2(1) | NULL | Classificacao | Tipo de processamento (R=Recurring, N=Nonrecurring) | --- | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_ele_classifications]] --- via `CLASSIFICATION_ID` (classificaÃ§Ã£o do tipo de elemento de folha)

### Tabelas-filha (FK de saída)
- [[pay_element_entries_f]] --- via `ELEMENT_TYPE_ID` (entradas de folha do tipo de elemento)
- [[pay_input_values_f]] --- via `ELEMENT_TYPE_ID` (valores de entrada do tipo de elemento)
- [[pay_element_types_tl]] --- via `ELEMENT_TYPE_ID` (traduÃ§Ãµes do tipo de elemento de folha)
- [[pay_element_criteria]] --- via `ELEMENT_TYPE_ID` (critÃ©rios de elegibilidade do tipo de elemento)

---

## 📎 Uso Típico

### Tipos de elementos vigentes por grupo legislativo
```sql
SELECT et.ELEMENT_TYPE_ID, et.ELEMENT_NAME, et.PROCESSING_TYPE
FROM   PAY_ELEMENT_TYPES_F et
WHERE  et.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id
  AND  SYSDATE BETWEEN et.EFFECTIVE_START_DATE AND et.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Processing Type: R=Recorrente (todo periodo), N=Nao recorrente (pontual).
- Tabela fundamental do Payroll; todos os calculos de folha se baseiam em element types.

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_TYPES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelementtypesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
