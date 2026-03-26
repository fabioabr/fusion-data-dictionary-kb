---
id: DOC-AR-064
doc_type: system-doc
title: "AR_REF_ACCOUNTS_ALL — Contas Contábeis de Referência para AutoAccounting"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, autoaccounting, contas-contabeis, referencia]
aliases: [AR_REF_ACCOUNTS_ALL, ar_ref_accounts_all, ref_accounts, contas_referencia, autoaccounting_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_REF_ACCOUNTS_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de contas contábeis de referência utilizadas pelo AutoAccounting do Accounts Receivable. Define as combinações contábeis padrão para diferentes tipos de conta (Receivable, Revenue, Tax, Freight, etc.) associadas a sites de clientes, tipos de transação e atividades de recebimento.

## 🧠 Propósito de Negócio

O AutoAccounting é o mecanismo que determina automaticamente as contas contábeis para transações de AR. Esta tabela armazena as referências que o motor de AutoAccounting consulta para derivar a combinação contábil correta com base no tipo de conta, site do cliente e tipo de transação. A configuração correta garante que receitas, recebíveis, impostos e fretes sejam contabilizados nas contas certas sem intervenção manual.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | REF_ACCOUNT_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único da conta de referência. | PK | 🟢 100% |
| 2 | CODE_COMBINATION_ID | NUMBER(15) | NOT NULL | FK para GL_CODE_COMBINATIONS. Combinação contábil de referência. | FK | 🟢 100% |
| 3 | ACCOUNT_TYPE | VARCHAR2(30) | NOT NULL | Tipo de conta (ex.: REC, REV, TAX, FREIGHT, UNEARNED, UNBILL). | Classificação | 🟢 100% |
| 4 | RECEIVABLES_TRX_ID | NUMBER(15) | NULL | FK para AR_RECEIVABLES_TRX_ALL. Atividade de recebimento associada. | FK | 🟢 100% |
| 5 | SITE_USE_ID | NUMBER(15) | NULL | FK para HZ_CUST_SITE_USES_ALL. Site de uso do cliente. | FK | 🟢 100% |
| 6 | INTERIM_TAX_CCID | NUMBER(15) | NULL | FK para combinação contábil de imposto intermediário. | FK | 🟢 100% |
| 7 | CUST_TRX_TYPE_ID | NUMBER(15) | NULL | FK para tipo de transação. | FK | 🟡 75% |
| 8 | MEMO_LINE_ID | NUMBER(15) | NULL | FK para linha de memo (standard memo lines). | FK | 🟡 75% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 10 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 11 | STATUS | VARCHAR2(1) | NULL | Status da conta de referência (A = Ativo, I = Inativo). | Controle | 🟡 75% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **GL_CODE_COMBINATIONS** — Combinação contábil de referência (N:1 via `CODE_COMBINATION_ID`).
- **AR_RECEIVABLES_TRX_ALL** — Atividade de recebimento (N:1 via `RECEIVABLES_TRX_ID`).
- **HZ_CUST_SITE_USES_ALL** — Site de uso do cliente (N:1 via `SITE_USE_ID`).

## 📎 Uso Típico

```sql
-- Contas de referência por tipo para uma business unit
SELECT ra.ACCOUNT_TYPE,
       ra.CODE_COMBINATION_ID,
       ra.SITE_USE_ID,
       ra.RECEIVABLES_TRX_ID
  FROM AR_REF_ACCOUNTS_ALL ra
 WHERE ra.ORG_ID = :p_org_id
   AND NVL(ra.STATUS, 'A') = 'A'
 ORDER BY ra.ACCOUNT_TYPE;
```

## 🔒 Observações

- `ACCOUNT_TYPE` define a natureza da conta: REC (Receivable), REV (Revenue), TAX (Tax), FREIGHT, UNEARNED (Receita não ganha), UNBILL (Receita não faturada).
- A combinação de `ACCOUNT_TYPE` + `SITE_USE_ID` + `RECEIVABLES_TRX_ID` determina a prioridade de busca do AutoAccounting.
- Alterações nas contas de referência afetam todas as novas transações; transações existentes mantêm a conta original.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — AutoAccounting Configuration Guide.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
