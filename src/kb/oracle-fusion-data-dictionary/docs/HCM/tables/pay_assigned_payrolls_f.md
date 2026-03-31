---
id: DOC-HCM-550
doc_type: system-doc
title: "PAY_ASSIGNED_PAYROLLS_F — Folhas Atribuidas a Colaboradores"
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
  - assigned-payrolls
  - atribuicao
  - pay-assigned
aliases:
  - PAY_ASSIGNED_PAYROLLS_F
  - pay_assigned_payrolls_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ASSIGNED_PAYROLLS_F

## 📌 Visão Geral

Armazena a **atribuicao de folhas de pagamento** a colaboradores. Cada registro vincula um relacionamento de pagamento (payroll relationship) a uma folha especifica, com vigencia temporal (`_F`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Associacao de colaboradores a folhas de pagamento
- Controle de vigencia da atribuicao de payroll
- Historico de transferencias entre folhas

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNED_PAYROLL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da atribuicao | --- | 🟢 95% |
| 2 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 95% |
| 3 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | PAYROLL_TERM_ID | NUMBER(18) | NULL | FK | ID do termo de folha | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha do colaborador)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (definição da folha de pagamento)

### Tabelas-filha (FK de saída)
- [[pay_assigned_payrolls_dn]] --- via `ASSIGNED_PAYROLL_ID` (visão desnormalizada da folha atribuída)

---

## 📎 Uso Típico

### Folha atribuida vigente por relacionamento
```sql
SELECT ap.ASSIGNED_PAYROLL_ID, ap.PAYROLL_ID, ap.EFFECTIVE_START_DATE
FROM   PAY_ASSIGNED_PAYROLLS_F ap
WHERE  ap.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN ap.EFFECTIVE_START_DATE AND ap.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Um colaborador pode ter historico de multiplas folhas ao longo do tempo.
- Relaciona-se com `PAY_PAY_RELATIONSHIPS_F` que eh a entidade principal de vinculo de pagamento.

---

## 📚 Referências

- [Oracle Docs — PAY_ASSIGNED_PAYROLLS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payassignedpayrollsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
