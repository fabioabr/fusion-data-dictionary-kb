---
id: DOC-HCM-584
doc_type: system-doc
title: "PAY_ORG_PAY_METHOD_USAGES_F — Usos de Metodos de Pagamento Org"
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
  - method-usages
  - usos-metodo
  - pay-method-usages
aliases:
  - PAY_ORG_PAY_METHOD_USAGES_F
  - pay_org_pay_method_usages_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ORG_PAY_METHOD_USAGES_F

## 📌 Visão Geral

Armazena os **usos** (associacoes) de metodos de pagamento organizacionais a folhas de pagamento especificas. Define quais metodos estao disponiveis em cada folha.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Associacao de metodos de pagamento a folhas especificas
- Controle de disponibilidade de metodos por payroll
- Vigencia temporal da associacao metodo-folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_PAY_METHOD_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do uso | --- | 🟢 85% |
| 2 | ORG_PAYMENT_METHOD_ID | NUMBER(18) | NOT NULL | FK | ID do metodo de pagamento | PAY_ORG_PAY_METHODS_F | 🟢 90% |
| 3 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_org_pay_methods_f]] --- via `ORG_PAYMENT_METHOD_ID` (método de pagamento organizacional utilizado)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento que usa o método)

### Tabelas-filha (FK de saída)
- --- Tabela de associacao, sem filhas conhecidas

---

## 📎 Uso Típico

### Metodos de pagamento disponiveis por folha
```sql
SELECT omu.ORG_PAYMENT_METHOD_ID, omu.PAYROLL_ID
FROM   PAY_ORG_PAY_METHOD_USAGES_F omu
WHERE  omu.PAYROLL_ID = :p_payroll_id
  AND  SYSDATE BETWEEN omu.EFFECTIVE_START_DATE AND omu.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_ORG_PAY_METHOD_USAGES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payorgpaymethodusagesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
