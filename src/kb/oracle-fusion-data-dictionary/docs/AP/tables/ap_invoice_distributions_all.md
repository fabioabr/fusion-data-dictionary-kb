---
id: DOC-AP-012
doc_type: system-doc
title: "AP_INVOICE_DISTRIBUTIONS_ALL — Distribuições Contábeis de Faturas"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - distribuicoes
  - distributions
  - contabilidade
aliases:
  - AP_INVOICE_DISTRIBUTIONS_ALL
  - ap_invoice_distributions_all
  - distribuicoes-ap
  - invoice-distributions
  - distribuicoes-faturas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INVOICE_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** de cada fatura do módulo Accounts Payable. Cada linha representa uma alocação de valor a uma combinação de contas contábeis (code combination), definindo como o valor da fatura será contabilizado no General Ledger. Uma fatura pode ter múltiplas distribuições, permitindo rateio entre centros de custo, projetos ou contas diferentes.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilização de faturas:** Define as contas contábeis de débito para cada parcela da fatura, gerando os lançamentos no GL.
- **Rateio de custos:** Permite distribuir o valor de uma fatura entre múltiplos centros de custo, projetos ou departamentos.
- **Three-way matching:** Vinculação com PO distributions e recebimentos para validação de matching.
- **Retenções fiscais:** Suporte a withholding tax com distribuições específicas de tipo TAX e AWT.
- **Auditoria contábil:** Rastreabilidade da alocação contábil de cada fatura até o nível de code combination.
- **Integração com projetos:** Distribuições podem ser vinculadas a projetos e tarefas para capitalização ou custeio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 100% |
| 2 | INVOICE_ID | NUMBER(18) | NOT NULL | FK | Fatura à qual pertence a distribuição | [[ap_invoices_all]] | 🟢 100% |
| 3 | INVOICE_LINE_NUMBER | NUMBER | NOT NULL | FK | Número da linha da fatura | [[ap_invoice_lines_all]] | 🟢 100% |
| 4 | DISTRIBUTION_LINE_NUMBER | NUMBER | NOT NULL | Identificação | Número sequencial da distribuição na linha | — | 🟢 100% |
| 5 | LINE_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da distribuição (ITEM/TAX/FREIGHT/MISCELLANEOUS/AWT) | [[ap_lookup_codes]] | 🟢 100% |
| 6 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da distribuição na moeda da transação | — | 🟢 100% |
| 7 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger) | — | 🟢 100% |
| 8 | DIST_CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | Contabilidade | Conta contábil de débito (code combination) | [[gl_code_combinations]] | 🟢 100% |
| 9 | ACCOUNTING_DATE | DATE | NOT NULL | Contabilidade | Data contábil da distribuição | — | 🟢 100% |
| 10 | PERIOD_NAME | VARCHAR2(15) | NULL | Contabilidade | Nome do período contábil | [[gl_period_statuses]] | 🟢 100% |
| 11 | ACCRUAL_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se accrual foi lançado (Y/N) | — | 🟢 100% |
| 12 | CASH_POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se cash basis foi lançado (Y/N) | — | 🟢 100% |
| 13 | POSTED_FLAG | VARCHAR2(1) | NULL | Contabilidade | Indica se foi contabilizado no GL (Y/N) | — | 🟢 100% |
| 14 | MATCH_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status de matching (A=aprovado/T=testado/N=não testado) | — | 🟢 100% |
| 15 | QUANTITY_INVOICED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 16 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preço unitário | — | 🟢 100% |
| 17 | PO_DISTRIBUTION_ID | NUMBER(18) | NULL | Referência cruzada | Distribuição do PO vinculada (matching) | [[po_distributions_all]] | 🟢 100% |
| 18 | RCV_TRANSACTION_ID | NUMBER(18) | NULL | Referência cruzada | Transação de recebimento vinculada | [[rcv_transactions]] | 🟢 100% |
| 19 | ASSETS_TRACKING_FLAG | VARCHAR2(1) | NULL | Controle | Rastreamento de ativo fixo (Y/N) | — | 🟢 100% |
| 20 | ASSET_BOOK_TYPE_CODE | VARCHAR2(15) | NULL | Ativo fixo | Livro de ativos para capitalização | — | 🟡 75% |
| 21 | ASSET_CATEGORY_ID | NUMBER(18) | NULL | Ativo fixo | Categoria do ativo | — | 🟡 75% |
| 22 | PROJECT_ID | NUMBER(18) | NULL | Projetos | Projeto vinculado | [[pjf_projects_all_b]] | 🟢 100% |
| 23 | TASK_ID | NUMBER(18) | NULL | Projetos | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 100% |
| 24 | EXPENDITURE_TYPE | VARCHAR2(30) | NULL | Projetos | Tipo de despesa do projeto | — | 🟢 100% |
| 25 | EXPENDITURE_ORGANIZATION_ID | NUMBER(18) | NULL | Projetos | Organização de despesa | — | 🟢 100% |
| 26 | PA_ADDITION_FLAG | VARCHAR2(1) | NULL | Projetos | Indica se foi transferido para Projects (Y/N/T/Z) | — | 🟢 100% |
| 27 | AWT_GROUP_ID | NUMBER(18) | NULL | Fiscal | Grupo de withholding tax | — | 🟡 75% |
| 28 | WITHHOLDING_TAX_CODE_ID | NUMBER(18) | NULL | Fiscal | Código de retenção fiscal | — | 🟡 75% |
| 29 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Status | Indica se é distribuição de reversão (Y/N) | — | 🟢 100% |
| 30 | PARENT_REVERSAL_ID | NUMBER(18) | NULL | Referência cruzada | ID da distribuição original revertida | [[ap_invoice_distributions_all]] | 🟢 100% |
| 31 | CANCELLATION_FLAG | VARCHAR2(1) | NULL | Status | Indica se foi cancelada (Y/N) | — | 🟢 100% |
| 32 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 33 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 34 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 35 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 36 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 37 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 38 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 39 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura à qual a distribuição contábil pertence)
- [[ap_invoice_lines_all]] — via `INVOICE_ID` + `INVOICE_LINE_NUMBER` (linha da fatura)
- [[gl_code_combinations]] — via `DIST_CODE_COMBINATION_ID` (conta contábil da distribuição da fatura)
- [[po_distributions_all]] — via `PO_DISTRIBUTION_ID` (distribuição do PO)
- [[rcv_transactions]] — via `RCV_TRANSACTION_ID` (transação de recebimento vinculada à distribuição)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a despesa da distribuição é imputada)
- [[pjf_tasks_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição da fatura)

### Tabelas-filha (FK de saída)
- [[ap_payment_hist_dists]] — via `INVOICE_DISTRIBUTION_ID` (distribuições de pagamento)
- [[ap_invoice_distributions_all]] — via `PARENT_REVERSAL_ID` (auto-referência para reversões)

---

## 📎 Uso Típico

### Distribuições de uma fatura
```sql
SELECT aid.DISTRIBUTION_LINE_NUMBER, aid.LINE_TYPE_LOOKUP_CODE,
       aid.AMOUNT, gcc.SEGMENT1 || '-' || gcc.SEGMENT2 AS conta
FROM   AP_INVOICE_DISTRIBUTIONS_ALL aid
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = aid.DIST_CODE_COMBINATION_ID
WHERE  aid.INVOICE_ID = :p_invoice_id
ORDER BY aid.DISTRIBUTION_LINE_NUMBER;
```

### Total distribuído por conta contábil
```sql
SELECT gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3,
       SUM(aid.AMOUNT) AS total_distribuido
FROM   AP_INVOICE_DISTRIBUTIONS_ALL aid
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = aid.DIST_CODE_COMBINATION_ID
WHERE  aid.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
  AND  aid.ORG_ID = :p_org_id
  AND  aid.CANCELLATION_FLAG IS NULL
GROUP BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3;
```

### Filtros comuns
- `LINE_TYPE_LOOKUP_CODE = 'ITEM'` — Apenas distribuições de item
- `POSTED_FLAG = 'Y'` — Já contabilizadas no GL
- `MATCH_STATUS_FLAG = 'A'` — Aprovadas pelo matching
- `CANCELLATION_FLAG IS NULL` — Exclui canceladas

---

## 🔒 Observações

- O campo `LINE_TYPE_LOOKUP_CODE` classifica a distribuição: **ITEM** (valor do item), **TAX** (imposto), **FREIGHT** (frete), **MISCELLANEOUS** (diversos), **AWT** (withholding tax automático).
- Cada distribuição aponta para uma combinação de contas (`DIST_CODE_COMBINATION_ID`) que define onde o valor será debitado no GL.
- Distribuições vinculadas a PO (`PO_DISTRIBUTION_ID`) participam do processo de **matching** (2-way ou 3-way).
- O campo `REVERSAL_FLAG = 'Y'` indica uma distribuição de reversão, com `PARENT_REVERSAL_ID` apontando para a distribuição original.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 📚 Referências

- [Oracle Docs — AP_INVOICE_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvoicedistributionsall-10003.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
