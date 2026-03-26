---
id: DOC-PO-067
doc_type: system-doc
title: "POR_REQ_DISTRIBUTIONS_ALL — Distribuições Contábeis de Requisições"
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
  - requisicoes
  - distribuicoes
  - contabilidade
aliases:
  - POR_REQ_DISTRIBUTIONS_ALL
  - por_req_distributions_all
  - distribuicoes-requisicao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_REQ_DISTRIBUTIONS_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** das linhas de requisição de compra. Cada distribuição define a combinação de contas contábeis (CCID) que será debitada quando a despesa for contabilizada, além do projeto, tarefa e percentual de distribuição quando aplicável. É filha de `POR_REQUISITION_LINES_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Alocação contábil:** Definição de para qual conta, centro de custo e segmento a despesa será alocada.
- **Distribuição multi-conta:** Divisão do custo de uma linha entre múltiplas contas contábeis (rateio).
- **Budgetary control:** Reserva de fundos (encumbrance) na conta contábil correspondente.
- **Project costing:** Associação de requisições a projetos e tarefas para controle de custos por projeto.
- **Reconciliação:** Rastreamento da distribuição contábil desde a requisição até a PO e o pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISTRIBUTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição | — | 🟢 100% |
| 2 | REQUISITION_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha de requisição associada | [[por_requisition_lines_all]] | 🟢 100% |
| 3 | DISTRIBUTION_NUM | NUMBER | NOT NULL | Identificação | Número sequencial da distribuição na linha | — | 🟢 95% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 5 | REQ_LINE_QUANTITY | NUMBER | NOT NULL | Quantitativo | Quantidade alocada nesta distribuição | — | 🟢 95% |
| 6 | REQ_LINE_AMOUNT | NUMBER | NULL | Financeiro | Valor alocado nesta distribuição | — | 🟢 90% |
| 7 | DISTRIBUTION_PERCENT | NUMBER | NULL | Percentual | Percentual de distribuição (quando rateio) | — | 🟡 80% |
| 8 | GL_ENCUMBERED_DATE | DATE | NULL | Contabilidade | Data de reserva de fundos (encumbrance) | — | 🟢 90% |
| 9 | GL_ENCUMBERED_PERIOD_NAME | VARCHAR2(15) | NULL | Contabilidade | Período contábil da reserva de fundos | — | 🟢 90% |
| 10 | ENCUMBERED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se os fundos foram reservados (Y/N) | — | 🟢 90% |
| 11 | ENCUMBERED_AMOUNT | NUMBER | NULL | Financeiro | Valor reservado (encumbered) | — | 🟢 90% |
| 12 | BUDGET_ACCOUNT_ID | NUMBER(18) | NULL | FK | Conta orçamentária | [[gl_code_combinations]] | 🟡 80% |
| 13 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto associado (Project Costing) | [[pjf_projects_all_b]] | 🟢 90% |
| 14 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_tasks_b]] | 🟢 90% |
| 15 | EXPENDITURE_TYPE | VARCHAR2(30) | NULL | Projeto | Tipo de despesa do projeto | — | 🟢 85% |
| 16 | EXPENDITURE_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização de despesa do projeto | [[hr_all_organization_units_f]] | 🟡 80% |
| 17 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | FK | Ledger (livro contábil) | [[gl_ledgers]] | 🟢 90% |
| 18 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[por_requisition_lines_all]] — via `REQUISITION_LINE_ID` (linha de requisição)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil de despesa)
- [[gl_code_combinations]] — via `BUDGET_ACCOUNT_ID` (conta orçamentária)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil da distribuição de requisição)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto ao qual a distribuição de requisição é imputada)
- [[pjf_tasks_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição de requisição)

### Tabelas-filha (FK de saída)
- Nenhuma direta — é o nível mais granular da hierarquia de requisição

---

## 📎 Uso Típico

### Distribuições contábeis de uma requisição
```sql
SELECT rd.DISTRIBUTION_NUM, rd.CODE_COMBINATION_ID,
       rd.REQ_LINE_QUANTITY, rd.REQ_LINE_AMOUNT,
       rd.ENCUMBERED_FLAG, rd.ENCUMBERED_AMOUNT
FROM   POR_REQ_DISTRIBUTIONS_ALL rd
JOIN   POR_REQUISITION_LINES_ALL rl ON rl.REQUISITION_LINE_ID = rd.REQUISITION_LINE_ID
WHERE  rl.REQUISITION_HEADER_ID = :p_req_header_id
ORDER BY rl.LINE_NUMBER, rd.DISTRIBUTION_NUM;
```

### Total encumbered por conta contábil
```sql
SELECT rd.CODE_COMBINATION_ID,
       SUM(rd.ENCUMBERED_AMOUNT) AS total_encumbered
FROM   POR_REQ_DISTRIBUTIONS_ALL rd
WHERE  rd.ENCUMBERED_FLAG = 'Y'
  AND  rd.ORG_ID = :p_org_id
GROUP BY rd.CODE_COMBINATION_ID;
```

---

## 🔒 Observações

- Uma linha de requisição pode ter múltiplas distribuições (rateio entre contas).
- A soma de `DISTRIBUTION_PERCENT` de todas as distribuições de uma linha deve ser 100%.
- O `ENCUMBERED_FLAG = 'Y'` indica que os fundos foram reservados no orçamento.
- Os campos de projeto (`PROJECT_ID`, `TASK_ID`, `EXPENDITURE_TYPE`) são preenchidos apenas quando a despesa é associada a um projeto no Oracle Projects.
- A conta contábil (`CODE_COMBINATION_ID`) é herdada pela PO e pela fatura do fornecedor, garantindo rastreabilidade end-to-end.

---

## 📚 Referências

- [Oracle Docs — POR_REQ_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/porreqdistributionsall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
