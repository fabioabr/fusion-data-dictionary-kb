---
id: DOC-HCM-592
doc_type: system-doc
title: "PAY_PERSON_PAY_METHODS_F — Metodos de Pagamento Pessoais"
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
  - person-pay-methods
  - metodos-pessoais
  - pay-ppm
aliases:
  - PAY_PERSON_PAY_METHODS_F
  - pay_person_pay_methods_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PERSON_PAY_METHODS_F

## 📌 Visão Geral

Armazena os **metodos de pagamento pessoais** (PPM) de cada colaborador. Define como cada pessoa recebe seu pagamento (conta bancaria, percentual, prioridade). Date-effective (`_F`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Configuracao de contas bancarias de colaboradores para pagamento
- Distribuicao de pagamento em multiplas contas
- Controle de vigencia de dados bancarios

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSONAL_PAYMENT_METHOD_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do metodo pessoal | --- | 🟢 95% |
| 2 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 95% |
| 3 | ORG_PAYMENT_METHOD_ID | NUMBER(18) | NOT NULL | FK | ID do metodo organizacional | PAY_ORG_PAY_METHODS_F | 🟢 90% |
| 4 | AMOUNT | NUMBER | NULL | Dados | Valor fixo (se aplicavel) | --- | 🟡 80% |
| 5 | PERCENTAGE | NUMBER | NULL | Dados | Percentual (se aplicavel) | --- | 🟡 80% |
| 6 | PRIORITY | NUMBER | NULL | Dados | Prioridade de pagamento | --- | 🟡 80% |
| 7 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 8 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha do mÃ©todo pessoal)
- [[pay_org_pay_methods_f]] --- via `ORG_PAYMENT_METHOD_ID` (mÃ©todo organizacional base do mÃ©todo pessoal)

### Tabelas-filha (FK de saída)
- [[pay_pre_payments]] --- via `PERSONAL_PAYMENT_METHOD_ID` (prÃ©-pagamentos do mÃ©todo pessoal)

---

## 📎 Uso Típico

### Metodos de pagamento pessoais vigentes
```sql
SELECT ppm.PERSONAL_PAYMENT_METHOD_ID, ppm.AMOUNT, ppm.PERCENTAGE, ppm.PRIORITY
FROM   PAY_PERSON_PAY_METHODS_F ppm
WHERE  ppm.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN ppm.EFFECTIVE_START_DATE AND ppm.EFFECTIVE_END_DATE
ORDER BY ppm.PRIORITY;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Dados bancarios sensiveis; classificacao `restricted` ou `confidential` pode ser necessaria.
- Um colaborador pode ter multiplos PPMs com prioridades diferentes para split de pagamento.

---

## 📚 Referências

- [Oracle Docs — PAY_PERSON_PAY_METHODS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypersonpaymethodsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
