---
id: DOC-PO-116
doc_type: system-doc
title: "PO_DISTRIBUTIONS_ALL — Distribuicoes de Ordens de Compra"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_DISTRIBUTIONS_ALL
  - po_distributions_all
  - po-distributions-all
  - po-distributions
  - distribuicoes-de-ordens-de-compra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuicoes contabeis de linhas de ordens de compra**. Cada distribuicao define alocacao contabil — conta, centro de custo, projeto, percentual, quantidade e valores recebidos/faturados.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Contabilizacao:** Definicao de contas contabeis (CCID) para cada item.
- **Projetos:** Associacao de gastos a projetos e tarefas.
- **Encumbrances:** Reserva orcamentaria na aprovacao.
- **Matching:** Reconciliacao PO x Recebimento x Fatura (3-way match).
- **Relatorios financeiros:** Analise por conta, centro de custo, projeto.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | ID da distribuicao | — | 🟢 100% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho do PO | [[po_headers_all]] | 🟢 100% |
| 3 | PO_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha do PO | [[po_lines_all]] | 🟢 100% |
| 4 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | FK | Schedule (entrega) | [[po_line_locations_all]] | 🟢 100% |
| 5 | DISTRIBUTION_NUM | NUMBER | NOT NULL | Identificacao | Numero da distribuicao | — | 🟢 100% |
| 6 | QUANTITY_ORDERED | NUMBER | NULL | Quantidade | Quantidade ordenada | — | 🟢 100% |
| 7 | QUANTITY_DELIVERED | NUMBER | NULL | Quantidade | Quantidade recebida | — | 🟢 100% |
| 8 | QUANTITY_BILLED | NUMBER | NULL | Quantidade | Quantidade faturada | — | 🟢 100% |
| 9 | QUANTITY_CANCELLED | NUMBER | NULL | Quantidade | Quantidade cancelada | — | 🟢 100% |
| 10 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | CCID — conta contabil | [[gl_code_combinations]] | 🟢 100% |
| 11 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger | [[gl_ledgers]] | 🟢 95% |
| 12 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto | [[pjf_projects_all_b]] | 🟢 90% |
| 13 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 90% |
| 14 | ENCUMBERED_FLAG | VARCHAR2(1) | NULL | Flag | Reserva orcamentaria (Y/N) | — | 🟢 90% |
| 15 | ENCUMBERED_AMOUNT | NUMBER | NULL | Financeiro | Valor da reserva | — | 🟢 90% |
| 16 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra ao qual a distribuição pertence)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO à qual a distribuição pertence)
- [[po_line_locations_all]] — via `LINE_LOCATION_ID` (shipment do PO ao qual a distribuição pertence)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil de encargo da distribuição do PO)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil da distribuição do PO)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a distribuição do PO é imputada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Distribuicoes de um PO
```sql
SELECT PO_DISTRIBUTION_ID, DISTRIBUTION_NUM, QUANTITY_ORDERED,
       QUANTITY_DELIVERED, QUANTITY_BILLED, CODE_COMBINATION_ID
FROM   PO_DISTRIBUTIONS_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY PO_LINE_ID, DISTRIBUTION_NUM;
```


---

## 🔒 Observações

- Tabela central para 3-way matching.
- `ENCUMBERED_FLAG = 'Y'` indica reserva orcamentaria ativa.
- Cada linha pode ter multiplas distribuicoes (rateio contabil).
- Filtrar por `ORG_ID` em consultas multi-org.

---

## 📚 Referências

- [Oracle Docs — PO_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/podistributionsall-10187.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
