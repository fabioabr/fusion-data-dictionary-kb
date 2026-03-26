---
id: DOC-PO-064
doc_type: system-doc
title: "POR_LINE_LOCATIONS_SUM_V — View Sumarizada de Locais de Entrega de Requisições"
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
  - entregas
  - view
  - sumarizacao
aliases:
  - POR_LINE_LOCATIONS_SUM_V
  - por_line_locations_sum_v
  - locais-entrega-sumarizado
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_LINE_LOCATIONS_SUM_V

## 📌 Visão Geral

View que fornece dados **sumarizados** dos locais de entrega (shipments/line locations) vinculados a linhas de requisição de compra. Consolida informações de quantidade, valor e status de entrega, permitindo visibilidade do progresso de atendimento das requisições.

> [!note] Sufixo _SUM_V
> O sufixo `_SUM_V` indica uma view sumarizada — agrega dados de múltiplos registros para facilitar consultas analíticas e de acompanhamento.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Acompanhamento de entregas:** Visão consolidada do status de entrega por linha de requisição.
- **Dashboards de procurement:** Indicadores de progresso de atendimento de requisições.
- **Análise de lead time:** Comparação entre datas solicitadas e datas efetivas de entrega.
- **Reconciliação:** Cruzamento entre quantidades requisitadas, pedidas e recebidas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Identificador do cabeçalho da requisição | [[por_requisition_headers_all]] | 🟡 80% |
| 2 | REQUISITION_LINE_ID | NUMBER(18) | NOT NULL | FK | Identificador da linha de requisição | [[por_requisition_lines_all]] | 🟡 80% |
| 3 | LINE_LOCATION_ID | NUMBER(18) | NOT NULL | PK | Identificador do local de entrega | — | 🟡 75% |
| 4 | QUANTITY | NUMBER | NULL | Quantitativo | Quantidade solicitada na entrega | — | 🟡 75% |
| 5 | QUANTITY_DELIVERED | NUMBER | NULL | Quantitativo | Quantidade já entregue | — | 🟡 70% |
| 6 | QUANTITY_CANCELLED | NUMBER | NULL | Quantitativo | Quantidade cancelada | — | 🟡 70% |
| 7 | AMOUNT | NUMBER | NULL | Financeiro | Valor total da entrega | — | 🟡 70% |
| 8 | NEED_BY_DATE | DATE | NULL | Data | Data de necessidade (quando o material é necessário) | — | 🟡 75% |
| 9 | DELIVER_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Local de entrega (endereço) | [[hr_locations_all]] | 🟡 70% |
| 10 | DESTINATION_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo de destino: EXPENSE, INVENTORY, SHOP_FLOOR | — | 🟡 70% |
| 11 | SHIPMENT_STATUS | VARCHAR2(30) | NULL | Status | Status da entrega | — | 🟡 65% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[por_requisition_headers_all]] — via `REQUISITION_HEADER_ID` (cabeçalho da requisição)
- [[por_requisition_lines_all]] — via `REQUISITION_LINE_ID` (linha da requisição)
- [[hr_locations_all]] — via `DELIVER_TO_LOCATION_ID` (local de entrega)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta)

---

## 📎 Uso Típico

### Progresso de entrega por requisição
```sql
SELECT lls.REQUISITION_LINE_ID,
       lls.QUANTITY,
       lls.QUANTITY_DELIVERED,
       lls.QUANTITY_CANCELLED,
       lls.NEED_BY_DATE
FROM   POR_LINE_LOCATIONS_SUM_V lls
WHERE  lls.REQUISITION_HEADER_ID = :p_req_header_id;
```

### Entregas pendentes (não totalmente atendidas)
```sql
SELECT lls.REQUISITION_LINE_ID,
       lls.QUANTITY - NVL(lls.QUANTITY_DELIVERED, 0) AS qty_pendente
FROM   POR_LINE_LOCATIONS_SUM_V lls
WHERE  lls.QUANTITY > NVL(lls.QUANTITY_DELIVERED, 0)
  AND  NVL(lls.QUANTITY_CANCELLED, 0) = 0;
```

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física — não aceita DML direto.
- Os dados são agregados a partir das tabelas de line locations do módulo PO.
- Útil para dashboards de acompanhamento sem necessidade de queries complexas nas tabelas-base.
- O campo `DESTINATION_TYPE_CODE` indica se a entrega vai para despesa direta, inventário ou chão de fábrica.

---

## 📚 Referências

- [Oracle Docs — POR Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/portables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
