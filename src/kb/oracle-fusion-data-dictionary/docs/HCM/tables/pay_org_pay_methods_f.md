---
id: DOC-HCM-581
doc_type: system-doc
title: "PAY_ORG_PAY_METHODS_F — Metodos de Pagamento Organizacionais"
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
  - org-pay-methods
  - metodos-pagamento
  - pay-org-methods
aliases:
  - PAY_ORG_PAY_METHODS_F
  - pay_org_pay_methods_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ORG_PAY_METHODS_F

## 📌 Visão Geral

Armazena os **metodos de pagamento organizacionais** (OPM) configurados para a empresa. Define como a organizacao efetua pagamentos (transferencia bancaria, cheque, deposito direto, etc.). Date-effective (`_F`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de metodos de pagamento da organizacao
- Configuracao de contas bancarias para pagamento
- Base para associacao de metodos de pagamento pessoais

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
| 2 | ORG_PAYMENT_METHOD_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do metodo de pagamento | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | PAYMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de pagamento | PAY_PAYMENT_TYPES | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payment_types]] --- via `PAYMENT_TYPE_ID` (tipo de pagamento do método organizacional)

### Tabelas-filha (FK de saída)
- [[pay_org_pay_methods_tl]] --- via `ORG_PAYMENT_METHOD_ID` (traduções do método de pagamento organizacional)
- [[pay_org_pay_method_usages_f]] --- via `ORG_PAYMENT_METHOD_ID` (usos do método de pagamento nas folhas)
- [[pay_person_pay_methods_f]] --- via `ORG_PAYMENT_METHOD_ID` (métodos pessoais vinculados ao método organizacional)

---

## 📎 Uso Típico

### Metodos de pagamento organizacionais vigentes
```sql
SELECT opm.ORG_PAYMENT_METHOD_ID, opm.ORG_PAYMENT_METHOD_NAME
FROM   PAY_ORG_PAY_METHODS_F opm
WHERE  SYSDATE BETWEEN opm.EFFECTIVE_START_DATE AND opm.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- OPMs sao pré-requisito para configuracao de metodos de pagamento pessoais (PPM).

---

## 📚 Referências

- [Oracle Docs — PAY_ORG_PAY_METHODS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payorgpaymethodsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
