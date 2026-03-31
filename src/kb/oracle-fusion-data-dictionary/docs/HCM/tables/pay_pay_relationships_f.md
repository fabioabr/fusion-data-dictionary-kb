---
id: DOC-HCM-591
doc_type: system-doc
title: "PAY_PAY_RELATIONSHIPS_F — Relacionamentos de Pagamento"
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
  - pay-relationships
  - relacionamento
  - pay-relationships
aliases:
  - PAY_PAY_RELATIONSHIPS_F
  - pay_pay_relationships_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAY_RELATIONSHIPS_F

## 📌 Visão Geral

Tabela central que armazena os **relacionamentos de pagamento** (payroll relationships) entre pessoas e a folha de pagamento. Eh a entidade principal que vincula um colaborador ao sistema de payroll, com vigencia temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Vinculacao de colaboradores ao sistema de folha de pagamento
- Controle de vigencia do relacionamento de pagamento
- Base para todas as transacoes de folha (entradas, cartoes, resultados)
- Entidade central do modelo de dados do Payroll

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do relacionamento | --- | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | ID da pessoa | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | PAYROLL_STAT_UNIT_ID | NUMBER(18) | NULL | FK | ID da unidade estatutaria | --- | 🟡 75% |
| 4 | RELATIONSHIP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de relacionamento | --- | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] --- via `PERSON_ID` (pessoa vinculada ao relacionamento de folha)

### Tabelas-filha (FK de saída)
- [[pay_assigned_payrolls_f]] --- via `PAYROLL_RELATIONSHIP_ID` (folhas atribuídas ao relacionamento)
- [[pay_element_entries_f]] --- via `PAYROLL_RELATIONSHIP_ID` (entradas de elemento do relacionamento de folha)
- [[pay_dir_cards_f]] --- via `PAYROLL_RELATIONSHIP_ID` (cartões de depósito direto do relacionamento)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_RELATIONSHIP_ID` (ações de folha do relacionamento)
- [[pay_person_pay_methods_f]] --- via `PAYROLL_RELATIONSHIP_ID` (métodos de pagamento pessoais do relacionamento)

---

## 📎 Uso Típico

### Relacionamento de pagamento vigente por pessoa
```sql
SELECT pr.PAYROLL_RELATIONSHIP_ID, pr.PERSON_ID, pr.RELATIONSHIP_TYPE
FROM   PAY_PAY_RELATIONSHIPS_F pr
WHERE  pr.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN pr.EFFECTIVE_START_DATE AND pr.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Entidade central do Payroll: todas as transacoes de folha se vinculam ao payroll relationship.
- Uma pessoa pode ter mais de um relacionamento de pagamento (ex.: empregado + diretor).

---

## 📚 Referências

- [Oracle Docs — PAY_PAY_RELATIONSHIPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrelationshipsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
