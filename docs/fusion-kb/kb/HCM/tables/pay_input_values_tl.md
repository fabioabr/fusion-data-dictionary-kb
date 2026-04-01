---
id: DOC-HCM-580
doc_type: system-doc
title: "PAY_INPUT_VALUES_TL — Valores de Entrada (Traducoes)"
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
  - input-values-tl
  - traducoes
  - pay-input-tl
aliases:
  - PAY_INPUT_VALUES_TL
  - pay_input_values_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_INPUT_VALUES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes dos input values para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para nomes de input values
- Exibicao localizada em interfaces de entrada de dados

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INPUT_VALUE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do input value (chave composta) | PAY_INPUT_VALUES_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 90% |
| 4 | NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido do input value | --- | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_input_values_f]] --- via `INPUT_VALUE_ID` (tabela base do valor de entrada)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao do input value
```sql
SELECT tl.NAME
FROM   PAY_INPUT_VALUES_TL tl
WHERE  tl.INPUT_VALUE_ID = :p_input_value_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[inputvalue|InputValue]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INPUT_VALUE_ID | InputValueTranslationPEOInputValueId | — |
| LANGUAGE | InputValueTranslationPEOLanguage | ✅ |
| NAME | InputValueTranslationPEOName | ✅ |
| SOURCE_LANG | InputValueTranslationPEOSourceLang | — |

### [[inputvaluepvo|InputValuePVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| INPUT_VALUE_ID | InputValueTranslationPEOInputValueId | — |
| LANGUAGE | InputValueTranslationPEOLanguage | ✅ |
| NAME | InputValueTranslationPEOName | ✅ |
| SOURCE_LANG | InputValueTranslationPEOSourceLang | — |

### [[offersalarypvo|OfferSalaryPVO]] (HCM · BICC: 1/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InputValueTranslationPEOCreatedBy3 | — |
| CREATION_DATE | InputValueTranslationPEOCreationDate3 | — |
| INPUT_VALUE_ID | InputValueTranslationPEOInputValueId1 | — |
| INPUT_VALUE_ID | InputValueTranslationPEOInputValueId2 | — |
| LANGUAGE | InputValueTranslationPEOLanguage2 | — |
| LANGUAGE | InputValueTranslationPEOLanguage3 | — |
| LAST_UPDATE_DATE | InputValueTranslationPEOLastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | InputValueTranslationPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | InputValueTranslationPEOLastUpdatedBy3 | — |
| NAME | InputValueTranslationPEOName1 | — |
| OBJECT_VERSION_NUMBER | InputValueTranslationPEOObjectVersionNumber3 | — |
| SOURCE_LANG | InputValueTranslationPEOSourceLang1 | — |

### [[salarypvo|SalaryPVO]] (HCM · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InputValueTranslationPEOCreatedBy | — |
| CREATION_DATE | InputValueTranslationPEOCreationDate | — |
| INPUT_VALUE_ID | InputValueTranslationPEOInputValueId | — |
| LANGUAGE | InputValueTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | InputValueTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InputValueTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InputValueTranslationPEOLastUpdatedBy | — |
| NAME | InputValueTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | InputValueTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | InputValueTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PAY_INPUT_VALUES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payinputvaluestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
