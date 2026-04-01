---
id: DOC-HCM-562
doc_type: system-doc
title: "PAY_DEDUCTION_TYPES_TL — Tipos de Desconto (Traducoes)"
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
  - deduction-types-tl
  - traducoes
  - pay-ded-types-tl
aliases:
  - PAY_DEDUCTION_TYPES_TL
  - pay_deduction_types_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DEDUCTION_TYPES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes dos tipos de desconto para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para tipos de desconto
- Exibicao localizada em contracheques

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DEDUCTION_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo (chave composta) | PAY_DEDUCTION_TYPES | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 85% |
| 4 | DEDUCTION_TYPE_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido | --- | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_deduction_types]] --- via `DEDUCTION_TYPE_ID` (tabela base do tipo de dedução)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao do tipo de desconto
```sql
SELECT tl.DEDUCTION_TYPE_NAME
FROM   PAY_DEDUCTION_TYPES_TL tl
WHERE  tl.DEDUCTION_TYPE_ID = :p_type_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[deductiontype|DeductionType]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DEDUCTION_TYPE_ID | DeductionTypeTranslationPEODeductionTypeId | — |
| LANGUAGE | DeductionTypeTranslationPEOLanguage | ✅ |
| NAME | DeductionTypeTranslationPEOName | ✅ |
| SOURCE_LANG | DeductionTypeTranslationPEOSourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_DEDUCTION_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydeductiontypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
