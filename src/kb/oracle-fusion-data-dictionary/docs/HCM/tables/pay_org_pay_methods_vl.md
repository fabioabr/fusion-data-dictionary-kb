---
id: DOC-HCM-583
doc_type: system-doc
title: "PAY_ORG_PAY_METHODS_VL — Metodos de Pagamento Org (View Localizada)"
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
  - org-pay-methods-vl
  - view-localizada
  - pay-org-methods-vl
aliases:
  - PAY_ORG_PAY_METHODS_VL
  - pay_org_pay_methods_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ORG_PAY_METHODS_VL

## 📌 Visão Geral

**View localizada** que combina metodos de pagamento organizacionais com suas traducoes.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de metodos de pagamento com traducao
- Uso em LOVs de configuracao de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_PAYMENT_METHOD_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do metodo | --- | 🟢 95% |
| 2 | ORG_PAYMENT_METHOD_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome traduzido | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | PAYMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de pagamento | PAY_PAYMENT_TYPES | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Metodos de pagamento com nome traduzido
```sql
SELECT vl.ORG_PAYMENT_METHOD_ID, vl.ORG_PAYMENT_METHOD_NAME
FROM   PAY_ORG_PAY_METHODS_VL vl
WHERE  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.

---

## 🔗 PVOs Relacionados

### [[payrolldpvo|PayrollDPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_ORG_PAY_METHOD_NAME | BaseOrgPayMethodName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | OrgPaymentMethodId | — |

### [[payrollpvo|PayrollPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_ORG_PAY_METHOD_NAME | BaseOrgPayMethodName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | OrgPaymentMethodId | — |

### [[personalpaymentmethoddetailsdpvo|PersonalPaymentMethodDetailsDPVO]] (AP · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BANK_ACCOUNT_ID | PaymentSourceDPEOBankAccountId | — |
| CURRENCY_CODE | OrganizationPaymentMethodDPECurrencyCode | — |
| EFFECTIVE_END_DATE | OrganizationPaymentMethodDPEEffectiveEndDate | — |
| EFFECTIVE_END_DATE | PaymentSourceDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | OrganizationPaymentMethodDPEEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PaymentSourceDPEOEffectiveStartDate | ✅ |
| OBJECT_VERSION_NUMBER | OrganizationPaymentMethodDPEObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PaymentSourceDPEOObjectVersionNumber | — |
| ORG_PAYMENT_METHOD_ID | OrganizationPaymentMethodDPEOrgPaymentMethodId | — |
| ORG_PAYMENT_METHOD_ID | PaymentSourceDPEOOrgPaymentMethodId | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ORG_PAY_METHODS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payorgpaymethodsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
