---
id: DOC-HCM-551
doc_type: system-doc
title: "PAY_BALANCE_CATEGORIES_F — Categorias de Saldo de Folha"
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
  - balance-categories
  - categorias-saldo
  - pay-bal-categories
aliases:
  - PAY_BALANCE_CATEGORIES_F
  - pay_balance_categories_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_CATEGORIES_F

## 📌 Visão Geral

Armazena as **categorias de saldo** (balance categories) utilizadas para classificar tipos de saldo na folha de pagamento. Categorias agrupam saldos logicamente (ex.: proventos, descontos, impostos).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Classificacao de tipos de saldo por categoria
- Configuracao de relatorios de folha por agrupamento
- Base para resumos de folha de pagamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da categoria | --- | 🟢 90% |
| 2 | CATEGORY_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome da categoria de saldo | --- | 🟢 85% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz de categorias de saldo

### Tabelas-filha (FK de saída)
- [[pay_balance_categories_tl]] --- via `BALANCE_CATEGORY_ID` (traduções da categoria de saldo de folha)

---

## 📎 Uso Típico

### Categorias de saldo vigentes
```sql
SELECT bc.BALANCE_CATEGORY_ID, bc.CATEGORY_NAME
FROM   PAY_BALANCE_CATEGORIES_F bc
WHERE  SYSDATE BETWEEN bc.EFFECTIVE_START_DATE AND bc.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[balancecategory|BalanceCategory]] (GL · BICC: 9/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_CATEGORY_ID | BalanceCategoryId | ✅ |
| BASE_BALANCE_CATEGORY_ID | BalanceCategoryBaseDPEOBaseBalanceCategoryId | ✅ |
| BASE_CATEGORY_NAME | BalanceCategoryBaseDPEOBaseCategoryName | ✅ |
| CREATED_BY | BalanceCategoryBaseDPEOCreatedBy | ✅ |
| CREATION_DATE | BalanceCategoryBaseDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | BalanceCategoryBaseDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BalanceCategoryBaseDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BalanceCategoryBaseDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | BalanceCategoryBaseDPEOLegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | BalanceCategoryBaseDPEOLegislativeDataGroupId | — |
| MODULE_ID | BalanceCategoryBaseDPEOModuleId | — |
| OBJECT_VERSION_NUMBER | BalanceCategoryBaseDPEOObjectVersionNumber | — |
| PBC_INFORMATION_CATEGORY | BalanceCategoryBaseDPEOPbcInformationCategory | — |
| SAVE_RUN_BALANCE_ENABLED | BalanceCategoryBaseDPEOSaveRunBalanceEnabled | — |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_CATEGORIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancecategoriesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
