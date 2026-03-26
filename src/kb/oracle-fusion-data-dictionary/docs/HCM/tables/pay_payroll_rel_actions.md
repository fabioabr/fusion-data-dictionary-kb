---
id: DOC-HCM-589
doc_type: system-doc
title: "PAY_PAYROLL_REL_ACTIONS — Acoes por Relacionamento de Folha"
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
  - rel-actions
  - acoes-relacionamento
  - pay-rel-actions
aliases:
  - PAY_PAYROLL_REL_ACTIONS
  - pay_payroll_rel_actions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYROLL_REL_ACTIONS

## 📌 Visão Geral

Armazena as **acoes de folha por relacionamento** de pagamento. Cada registro vincula uma acao de folha (processamento) a um relacionamento de pagamento especifico (colaborador), registrando o resultado individual.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Resultado individual de processamento por colaborador
- Rastreamento de status de calculo por pessoa
- Base para custos e resultados detalhados de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_REL_ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da acao por relacionamento | --- | 🟢 95% |
| 2 | PAYROLL_ACTION_ID | NUMBER(18) | NOT NULL | FK | ID da acao de folha | PAY_PAYROLL_ACTIONS | 🟢 95% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 95% |
| 4 | ACTION_STATUS | VARCHAR2(1) | NOT NULL | Classificacao | Status individual (C, E, U) | --- | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payroll_actions]] --- via `PAYROLL_ACTION_ID` (aÃ§Ã£o de folha principal do processamento)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha processado)

### Tabelas-filha (FK de saída)
- [[pay_costs]] --- via `PAYROLL_REL_ACTION_ID` (custos gerados pela aÃ§Ã£o de folha)
- [[pay_run_results]] --- via `PAYROLL_REL_ACTION_ID` (resultados de cÃ¡lculo por relacionamento)

---

## 📎 Uso Típico

### Acoes individuais de um processamento
```sql
SELECT pra.PAYROLL_REL_ACTION_ID, pra.PAYROLL_RELATIONSHIP_ID, pra.ACTION_STATUS
FROM   PAY_PAYROLL_REL_ACTIONS pra
WHERE  pra.PAYROLL_ACTION_ID = :p_action_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_PAYROLL_REL_ACTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrollrelactions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
