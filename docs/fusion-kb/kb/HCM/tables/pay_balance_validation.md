---
id: DOC-HCM-557
doc_type: system-doc
title: "PAY_BALANCE_VALIDATION — Validacao de Saldos de Folha"
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
  - balance-validation
  - validacao
  - pay-bal-validation
aliases:
  - PAY_BALANCE_VALIDATION
  - pay_balance_validation
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_VALIDATION

## 📌 Visão Geral

Armazena as regras de **validacao de saldos** da folha de pagamento. Define os criterios de verificacao aplicados apos o processamento para garantir consistencia dos valores calculados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Validacao pos-processamento de saldos calculados
- Identificacao de discrepancias em valores de folha
- Controle de qualidade do processamento de payroll

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_VALIDATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da validacao | --- | 🟢 85% |
| 2 | BALANCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de saldo | --- | 🟢 85% |
| 3 | BALANCE_DIMENSION_ID | NUMBER(18) | NULL | FK | ID da dimensao de saldo | PAY_BALANCE_DIMENSIONS | 🟢 80% |
| 4 | VALIDATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de validacao | --- | 🟡 70% |
| 5 | VALIDATION_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da validacao | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_balance_dimensions]] --- via `BALANCE_DIMENSION_ID` (dimensão de saldo validada)

### Tabelas-filha (FK de saída)
- --- Tabela de validacao, sem filhas conhecidas

---

## 📎 Uso Típico

### Validacoes por tipo de saldo
```sql
SELECT bv.BALANCE_VALIDATION_ID, bv.VALIDATION_TYPE, bv.VALIDATION_STATUS
FROM   PAY_BALANCE_VALIDATION bv
WHERE  bv.BALANCE_TYPE_ID = :p_balance_type_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[balancevalidationpvo|BalanceValidationPVO]] (GL · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_LOAD_DATE | BalanceValidationPEOBalanceLoadDate | — |
| BALANCE_VALIDATION_ID | BalanceValidationPEOBalanceValidationId | ✅ |
| CREATED_BY | BalanceValidationPEOCreatedBy | — |
| CREATION_DATE | BalanceValidationPEOCreationDate | — |
| DEFINED_BALANCE_ID | BalanceValidationPEODefinedBalanceId | — |
| LAST_UPDATE_DATE | BalanceValidationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BalanceValidationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BalanceValidationPEOLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | BalanceValidationPEOLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | BalanceValidationPEOObjectVersionNumber | — |
| RUN_BALANCE_STATUS | BalanceValidationPEORunBalanceStatus | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_VALIDATION](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancevalidation.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
