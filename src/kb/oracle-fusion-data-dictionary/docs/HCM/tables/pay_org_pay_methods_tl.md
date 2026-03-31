---
id: DOC-HCM-582
doc_type: system-doc
title: "PAY_ORG_PAY_METHODS_TL — Metodos de Pagamento Org (Traducoes)"
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
  - org-pay-methods-tl
  - traducoes
  - pay-org-methods-tl
aliases:
  - PAY_ORG_PAY_METHODS_TL
  - pay_org_pay_methods_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ORG_PAY_METHODS_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes dos metodos de pagamento organizacionais para multiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para metodos de pagamento organizacionais
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
| 1 | ORG_PAYMENT_METHOD_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do metodo (chave composta) | PAY_ORG_PAY_METHODS_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 90% |
| 4 | ORG_PAYMENT_METHOD_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido | --- | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_org_pay_methods_f]] --- via `ORG_PAYMENT_METHOD_ID` (tabela base do método de pagamento organizacional)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao do metodo de pagamento
```sql
SELECT tl.ORG_PAYMENT_METHOD_NAME
FROM   PAY_ORG_PAY_METHODS_TL tl
WHERE  tl.ORG_PAYMENT_METHOD_ID = :p_method_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[organizationpaymentmethoddpvo|OrganizationPaymentMethodDPVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | OrgnPaymentMethodTrasltnPEOLanguage | ✅ |
| ORG_PAYMENT_METHOD_ID | OrgnPaymentMethodTrasltnPEOOrgPaymentMethodId | — |
| ORG_PAYMENT_METHOD_NAME | OrgnPaymentMethodTrasltnPEOOrgPaymentMethodName | ✅ |
| SOURCE_LANG | OrgnPaymentMethodTrasltnPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ORG_PAY_METHODS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payorgpaymethodstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
