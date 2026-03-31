---
id: DOC-HCM-575
doc_type: system-doc
title: "PAY_ELE_CLASSIFICATIONS — Classificacoes de Elementos de Folha"
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
  - ele-classifications
  - classificacoes
  - pay-classifications
aliases:
  - PAY_ELE_CLASSIFICATIONS
  - pay_ele_classifications
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELE_CLASSIFICATIONS

## 📌 Visão Geral

Armazena as **classificacoes** de elementos de folha de pagamento (ex.: Regular Earnings, Supplemental Earnings, Voluntary Deductions, Tax Deductions, Employer Charges). Define o comportamento contabil e de processamento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Classificacao de elementos por natureza (provento, desconto, imposto)
- Definicao de comportamento contabil por classificacao
- Base para relatorios de folha por agrupamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da classificacao | --- | 🟢 95% |
| 2 | CLASSIFICATION_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome da classificacao | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | PARENT_CLASSIFICATION_ID | NUMBER(18) | NULL | FK | ID da classificacao pai (hierarquia) | PAY_ELE_CLASSIFICATIONS | 🟡 80% |
| 5 | COSTING_DEBIT_OR_CREDIT | VARCHAR2(1) | NULL | Classificacao | Natureza contabil (D=Debito, C=Credito) | --- | 🟡 80% |
| 6 | DEFAULT_PRIORITY | NUMBER | NULL | Dados | Prioridade padrao de processamento | --- | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz (ou auto-referencia via `PARENT_CLASSIFICATION_ID`)

### Tabelas-filha (FK de saída)
- [[pay_element_types_f]] --- via `CLASSIFICATION_ID` (tipos de elemento da classificação)
- [[pay_ele_classifications_tl]] --- via `CLASSIFICATION_ID` (traduções da classificação de elemento)

---

## 📎 Uso Típico

### Classificacoes de elementos por grupo legislativo
```sql
SELECT ec.CLASSIFICATION_ID, ec.CLASSIFICATION_NAME, ec.COSTING_DEBIT_OR_CREDIT
FROM   PAY_ELE_CLASSIFICATIONS ec
WHERE  ec.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_ELE_CLASSIFICATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payeleclassifications.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
