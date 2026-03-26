---
id: DOC-PO-136
doc_type: system-doc
title: "PO_LINE_TYPES_B — Tipos de Linha de PO (Base)"
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
  - PO_LINE_TYPES_B
  - po_line_types_b
  - po-line-types-b
  - po-line
  - tipos-de-linha-de-po-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_TYPES_B

## 📌 Visão Geral

Armazena os **tipos de linha de PO**: Goods, Services, Fixed Price, Amount, Rate, etc.

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (idioma base). Traducoes ficam na tabela correspondente `_TL`.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao:** Tipos de linha disponiveis.
- **Regras:** Quantidade/preco vs apenas valor.
- **Matching:** Comportamento por tipo de linha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_TYPE_ID | NUMBER(18) | NOT NULL | PK | ID do tipo | — | 🟢 95% |
| 2 | ORDER_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificacao | QUANTITY, AMOUNT, FIXED PRICE, RATE | — | 🟢 95% |
| 3 | PURCHASE_BASIS | VARCHAR2(25) | NULL | Classificacao | GOODS, SERVICES, TEMP LABOR | — | 🟢 90% |
| 4 | MATCHING_BASIS | VARCHAR2(25) | NULL | Classificacao | QUANTITY ou AMOUNT | — | 🟢 90% |
| 5 | OUTSIDE_OPERATION_FLAG | VARCHAR2(1) | NULL | Flag | Operacao externa | — | 🟡 80% |
| 6 | RECEIVING_FLAG | VARCHAR2(1) | NULL | Flag | Requer recebimento | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Tipos de linha
```sql
SELECT LINE_TYPE_ID, ORDER_TYPE_LOOKUP_CODE, PURCHASE_BASIS, MATCHING_BASIS
FROM   PO_LINE_TYPES_B;
```


---

## 🔒 Observações

- Tabela de configuracao; poucas linhas seeded.
- O `PURCHASE_BASIS` define bens, servicos ou mao de obra.
- O `MATCHING_BASIS` controla matching por quantidade ou valor.

---

## 📚 Referências

- [Oracle Docs — PO_LINE_TYPES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
