---
id: DOC-HCM-587
doc_type: system-doc
title: "PAY_PAYMENT_TYPES_TL — Tipos de Pagamento (Traducoes)"
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
  - payment-types-tl
  - traducoes
  - pay-payment-types-tl
aliases:
  - PAY_PAYMENT_TYPES_TL
  - pay_payment_types_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYMENT_TYPES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes dos tipos de pagamento para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para tipos de pagamento
- Exibicao localizada em interfaces de configuracao

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo (chave composta) | PAY_PAYMENT_TYPES | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 90% |
| 4 | PAYMENT_TYPE_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido | --- | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payment_types]] --- via `PAYMENT_TYPE_ID` (tabela base do tipo de pagamento)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao do tipo de pagamento
```sql
SELECT tl.PAYMENT_TYPE_NAME
FROM   PAY_PAYMENT_TYPES_TL tl
WHERE  tl.PAYMENT_TYPE_ID = :p_type_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[organizationpaymentmethoddpvo|OrganizationPaymentMethodDPVO]] (AP · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | PaymentTypeTranslationPEODescription | ✅ |
| LANGUAGE | PaymentTypeTranslationPEOLanguage | ✅ |
| PAYMENT_TYPE_ID | PaymentTypeTranslationPEOPaymentTypeId | — |
| PAYMENT_TYPE_NAME | PaymentTypeTranslationPEOPaymentTypeName | ✅ |
| SOURCE_LANG | PaymentTypeTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PAY_PAYMENT_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypaymenttypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
