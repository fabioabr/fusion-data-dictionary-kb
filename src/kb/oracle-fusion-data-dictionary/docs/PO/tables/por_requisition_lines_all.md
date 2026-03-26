---
id: DOC-PO-066
doc_type: system-doc
title: "POR_REQUISITION_LINES_ALL — Linhas de Requisições de Compra"
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
  - linhas
  - purchase-requisition
aliases:
  - POR_REQUISITION_LINES_ALL
  - por_requisition_lines_all
  - linhas-requisicoes
  - requisicao-compra-lines
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_REQUISITION_LINES_ALL

## 📌 Visão Geral

Armazena as **linhas individuais** das requisições de compra. Cada linha representa um item ou serviço solicitado, com informações de quantidade, preço unitário, categoria, fornecedor sugerido, local de entrega e conta contábil. É filha de `POR_REQUISITION_HEADERS_ALL` e mãe de `POR_REQ_DISTRIBUTIONS_ALL`.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de demanda:** Especificação item a item do que está sendo requisitado.
- **Sourcing:** Identificação de fornecedor sugerido e contrato-quadro (blanket agreement).
- **Conversão para PO:** Cada linha pode ser convertida em uma ou mais linhas de Purchase Order.
- **Controle de recebimento:** Rastreamento de quantidade recebida versus requisitada.
- **Análise de gastos:** Base para relatórios de spend por categoria, fornecedor e item.
- **Workflow:** Aprovação pode ser definida a nível de linha em determinadas configurações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_LINE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha de requisição | — | 🟢 100% |
| 2 | REQUISITION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabeçalho da requisição | [[por_requisition_headers_all]] | 🟢 100% |
| 3 | LINE_NUMBER | NUMBER | NOT NULL | Identificação | Número sequencial da linha | — | 🟢 100% |
| 4 | ITEM_DESCRIPTION | VARCHAR2(240) | NOT NULL | Descrição | Descrição do item/serviço requisitado | — | 🟢 100% |
| 5 | ITEM_ID | NUMBER(18) | NULL | FK | Item do catálogo (se catalog-based) | [[egp_system_items_b]] | 🟢 95% |
| 6 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compra do item | [[egp_categories_b]] | 🟢 95% |
| 7 | QUANTITY | NUMBER | NOT NULL | Quantitativo | Quantidade requisitada | — | 🟢 100% |
| 8 | UNIT_MEAS_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Unidade de medida | — | 🟢 95% |
| 9 | UNIT_PRICE | NUMBER | NULL | Financeiro | Preço unitário estimado | — | 🟢 100% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | [[fnd_currencies]] | 🟢 95% |
| 11 | AMOUNT | NUMBER | NULL | Financeiro | Valor total da linha (quantidade × preço) | — | 🟢 95% |
| 12 | SUGGESTED_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor sugerido pelo requisitante | [[poz_suppliers]] | 🟡 80% |
| 13 | SUGGESTED_VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor sugerido | [[poz_supplier_sites_all_m]] | 🟡 80% |
| 14 | DELIVER_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega | [[hr_locations_all]] | 🟢 90% |
| 15 | DESTINATION_TYPE_CODE | VARCHAR2(25) | NULL | Classificação | Tipo de destino: EXPENSE, INVENTORY, SHOP_FLOOR | — | 🟢 90% |
| 16 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade | — | 🟢 95% |
| 17 | LINE_STATUS | VARCHAR2(25) | NULL | Status | Status da linha no ciclo de vida | — | 🟢 90% |
| 18 | CANCEL_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a linha foi cancelada (Y/N) | — | 🟢 90% |
| 19 | REQUESTER_ID | NUMBER(18) | NULL | FK | Pessoa que solicitou (pode diferir do preparador) | [[per_all_people_f]] | 🟢 90% |
| 20 | SOURCE_TYPE_CODE | VARCHAR2(25) | NULL | Classificação | Tipo de fonte: VENDOR (externo), INVENTORY (interno) | — | 🟢 90% |
| 21 | BLANKET_PO_HEADER_ID | NUMBER(18) | NULL | FK | Acordo-quadro (blanket agreement) referenciado | [[po_headers_all]] | 🟡 80% |
| 22 | BLANKET_PO_LINE_NUM | NUMBER | NULL | Referência | Linha do acordo-quadro | — | 🟡 80% |
| 23 | NEGOTIATED_BY_PREPARER_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o preço foi negociado pelo preparador | — | 🟡 70% |
| 24 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 25 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 26 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 27 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 28 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[por_requisition_headers_all]] — via `REQUISITION_HEADER_ID` (cabeçalho da requisição ao qual a linha pertence)
- [[egp_system_items_b]] — via `ITEM_ID` (item do catálogo)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de compra)
- [[poz_suppliers]] — via `SUGGESTED_VENDOR_ID` (fornecedor sugerido)
- [[per_all_people_f]] — via `REQUESTER_ID` (pessoa que solicitou o item na requisição)
- [[hr_locations_all]] — via `DELIVER_TO_LOCATION_ID` (local de entrega)
- [[po_headers_all]] — via `BLANKET_PO_HEADER_ID` (acordo-quadro referenciado na linha de requisição)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha de requisição)

### Tabelas-filha (FK de saída)
- [[por_req_distributions_all]] — via `REQUISITION_LINE_ID` (distribuições contábeis)
- [[por_line_locations_sum_v]] — via `REQUISITION_LINE_ID` (locais de entrega)

---

## 📎 Uso Típico

### Linhas de uma requisição com detalhes de item
```sql
SELECT rl.LINE_NUMBER, rl.ITEM_DESCRIPTION, rl.QUANTITY,
       rl.UNIT_PRICE, rl.AMOUNT, rl.NEED_BY_DATE,
       rl.LINE_STATUS
FROM   POR_REQUISITION_LINES_ALL rl
WHERE  rl.REQUISITION_HEADER_ID = :p_req_header_id
  AND  NVL(rl.CANCEL_FLAG, 'N') = 'N'
ORDER BY rl.LINE_NUMBER;
```

### Valor total de requisições por categoria
```sql
SELECT rl.CATEGORY_ID, cat.CATEGORY_NAME,
       SUM(rl.AMOUNT) AS total_valor,
       COUNT(*) AS qtd_linhas
FROM   POR_REQUISITION_LINES_ALL rl
JOIN   EGP_CATEGORIES_VL cat ON cat.CATEGORY_ID = rl.CATEGORY_ID
JOIN   POR_REQUISITION_HEADERS_ALL rh ON rh.REQUISITION_HEADER_ID = rl.REQUISITION_HEADER_ID
WHERE  rh.AUTHORIZATION_STATUS = 'APPROVED'
  AND  rh.REQUISITION_DATE BETWEEN :start_date AND :end_date
GROUP BY rl.CATEGORY_ID, cat.CATEGORY_NAME;
```

### Filtros comuns
- `CANCEL_FLAG = 'N'` ou `IS NULL` — Linhas ativas (não canceladas)
- `SOURCE_TYPE_CODE = 'VENDOR'` — Requisições externas
- `DESTINATION_TYPE_CODE = 'EXPENSE'` — Destino despesa

---

## 🔒 Observações

- O `REQUESTER_ID` pode diferir do `PREPARER_ID` do cabeçalho — o preparador digita a requisição, o requisitante é quem solicita o material.
- `SOURCE_TYPE_CODE = 'VENDOR'` gera POs externas; `INVENTORY` gera ordens de transferência interna.
- O campo `BLANKET_PO_HEADER_ID` conecta a linha a um acordo-quadro, garantindo preços pré-negociados.
- Linhas canceladas (`CANCEL_FLAG = 'Y'`) devem ser excluídas de análises de valor e volume.
- O `UNIT_PRICE` é estimativo na requisição; o preço final é definido na Purchase Order.

---

## 📚 Referências

- [Oracle Docs — POR_REQUISITION_LINES_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/porrequisitionlinesall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
