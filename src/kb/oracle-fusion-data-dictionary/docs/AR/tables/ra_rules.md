---
id: DOC-AR-012
doc_type: system-doc
title: "RA_RULES — Regras de Reconhecimento de Receita"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - revenue-recognition
  - regras-receita
  - contabilidade
aliases:
  - RA_RULES
  - ra_rules
  - regras-reconhecimento-receita
  - invoicing-rules
  - accounting-rules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_RULES

## 📌 Visão Geral

Armazena as **regras de reconhecimento de receita** (invoicing rules e accounting rules) utilizadas pelo módulo Accounts Receivable. Cada registro define uma regra que determina **como e quando a receita é reconhecida contabilmente** — por exemplo, reconhecimento imediato no faturamento, rateado ao longo de um período ou diferido até o cumprimento de obrigações de performance.

Essas regras são referenciadas pelas transações AR (via `INVOICING_RULE_ID` em [[ra_customer_trx_all]]) e controlam a geração de distribuições contábeis e o timing do lançamento no GL.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconhecimento de receita:** Define se a receita é reconhecida antecipadamente (advance), posteriormente (arrears) ou rateada (prorate) ao longo de períodos contábeis.
- **Compliance contábil:** Suporte às normas ASC 606 (US GAAP) e IFRS 15, garantindo que a receita seja reconhecida de acordo com os critérios de performance obligation.
- **Configuração de faturamento:** Regras de invoicing (advance/arrears) determinam se a fatura é emitida antes ou depois da entrega do serviço.
- **Diferimento de receita:** Controle de receita diferida (deferred revenue) quando o faturamento ocorre antes da prestação do serviço.
- **Relatórios financeiros:** Base para reconciliação entre receita faturada e receita reconhecida.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra de reconhecimento de receita | — | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome da regra (ex.: ADVANCE INVOICE, ARREARS INVOICE) | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(80) | NULL | Identificação | Descrição textual da regra | — | 🟢 100% |
| 4 | TYPE | VARCHAR2(10) | NOT NULL | Classificação | Tipo da regra: A=Arrears (pós-entrega), I=Immediate, P=Prorate (rateio por período) | — | 🟢 100% |
| 5 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status da regra: A=Active, I=Inactive | — | 🟢 100% |
| 6 | FREQUENCY | VARCHAR2(15) | NULL | Configuração | Frequência de reconhecimento: DAILY, MONTHLY, SPECIFIC (apenas para accounting rules) | — | 🟢 100% |
| 7 | OCCURRENCES | NUMBER | NULL | Configuração | Número de períodos para reconhecimento rateado (usado com TYPE=P) | — | 🟢 100% |
| 8 | DEBIT_CREDIT_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se a regra gera débito (D) ou crédito (C) no reconhecimento | — | 🟡 70% |
| 9 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit associada à regra | [[hr_all_organization_units_f]] | 🟢 100% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista (OVN) | — | 🟢 100% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da regra de reconhecimento de receita)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `INVOICING_RULE_ID` → `RULE_ID` (transações que usam esta regra de faturamento)
- [[ra_customer_trx_lines_all]] — via `ACCOUNTING_RULE_ID` → `RULE_ID` (linhas que usam esta regra de contabilização)

---

## 📎 Uso Típico

### Consultar todas as regras ativas
```sql
SELECT RULE_ID, NAME, TYPE, FREQUENCY, OCCURRENCES
FROM   RA_RULES
WHERE  STATUS = 'A';
```

### Identificar transações por tipo de regra de faturamento
```sql
SELECT r.NAME AS regra, r.TYPE, COUNT(*) AS qtd_transacoes
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_RULES r ON r.RULE_ID = ct.INVOICING_RULE_ID
WHERE  ct.ORG_ID = :p_org_id
GROUP BY r.NAME, r.TYPE;
```

### Filtros comuns
- `TYPE = 'A'` — Regras de arrears (reconhecimento pós-entrega)
- `TYPE = 'I'` — Regras de reconhecimento imediato
- `TYPE = 'P'` — Regras de prorate (rateio por período)
- `STATUS = 'A'` — Apenas regras ativas

---

## 🔒 Observações

- No Oracle Fusion, as regras de faturamento (invoicing rules) e de contabilização (accounting rules) compartilham a mesma tabela, diferenciadas pelo campo `TYPE`.
- As regras do tipo **Arrears (A)** e **Advance (I)** são tipicamente usadas como invoicing rules em `RA_CUSTOMER_TRX_ALL.INVOICING_RULE_ID`.
- As regras do tipo **Prorate (P)** são tipicamente usadas como accounting rules em `RA_CUSTOMER_TRX_LINES_ALL.ACCOUNTING_RULE_ID`, com `FREQUENCY` e `OCCURRENCES` definindo o cronograma de reconhecimento.
- A tabela é pré-populada com regras seeded pela Oracle (ex.: `ADVANCE INVOICE`, `ARREARS INVOICE`). Regras customizadas podem ser criadas via setup.

---

## 📚 Referências

- [Oracle Docs — RA_RULES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/rarules-25262.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
