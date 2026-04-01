---
id: DOC-HCM-555
doc_type: system-doc
title: "PAY_BALANCE_TYPES_TL — Tipos de Saldo (Traducoes)"
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
  - balance-types-tl
  - traducoes
  - pay-bal-types-tl
aliases:
  - PAY_BALANCE_TYPES_TL
  - pay_balance_types_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_TYPES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes dos tipos de saldo para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para tipos de saldo
- Exibicao localizada em contracheques e relatorios de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo de saldo (chave composta) | --- | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 85% |
| 4 | BALANCE_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido do tipo de saldo | --- | 🟢 85% |
| 5 | REPORTING_NAME | VARCHAR2(80) | NULL | Identificacao | Nome para relatorios | --- | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela base de tipos de saldo (via `BALANCE_TYPE_ID`)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Traducao do tipo de saldo
```sql
SELECT tl.BALANCE_NAME, tl.REPORTING_NAME
FROM   PAY_BALANCE_TYPES_TL tl
WHERE  tl.BALANCE_TYPE_ID = :p_balance_type_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[balancetypetranslation|BalanceTypeTranslation]] (GL · BICC: 8/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_NAME | BalanceTypeTranslationPEOBalanceName | ✅ |
| BALANCE_TYPE_ID | BalanceTypeId | ✅ |
| CREATED_BY | BalanceTypeTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | BalanceTypeTranslationPEOCreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | BalanceTypeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BalanceTypeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BalanceTypeTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BalanceTypeTranslationPEOObjectVersionNumber | — |
| REPORTING_NAME | BalanceTypeTranslationPEOReportingName | — |
| SOURCE_LANG | BalanceTypeTranslationPEOSourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancetypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
