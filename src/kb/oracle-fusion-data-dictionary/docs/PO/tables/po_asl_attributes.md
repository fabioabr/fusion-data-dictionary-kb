---
id: DOC-PO-112
doc_type: system-doc
title: "PO_ASL_ATTRIBUTES — Atributos da Lista de Fornecedores Aprovados"
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
  - approved-supplier-list
  - asl
  - sourcing
aliases:
  - PO_ASL_ATTRIBUTES
  - po_asl_attributes
  - po-asl-attributes
  - po-asl
  - atributos-da-lista-de-fornecedores-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ASL_ATTRIBUTES

## 📌 Visão Geral

Armazena os **atributos detalhados das entradas ASL**, incluindo lead times, quantidades minimas/maximas e regras de sourcing.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento:** Lead times e quantidades minimas por fornecedor.
- **Sourcing rules:** Split percentual entre fornecedores.
- **AutoSource:** Regras automaticas de geracao de PO.
- **Analise:** Comparacao de atributos entre fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASL_ATTRIBUTE_ID | NUMBER(18) | NOT NULL | PK | ID dos atributos | — | 🟡 80% |
| 2 | ASL_ID | NUMBER(18) | NOT NULL | FK | Entrada ASL | [[po_approved_supplier_list]] | 🟢 95% |
| 3 | USING_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Org que utiliza | [[hr_all_organization_units_f]] | 🟢 90% |
| 4 | DOCUMENT_HEADER_ID | NUMBER(18) | NULL | FK | Agreement de referencia | [[po_headers_all]] | 🟡 80% |
| 5 | DOCUMENT_LINE_ID | NUMBER(18) | NULL | FK | Linha do agreement | [[po_lines_all]] | 🟡 80% |
| 6 | VENDOR_BUSINESS_TYPE | VARCHAR2(25) | NULL | Classificacao | DIRECT, DISTRIBUTOR | — | 🟡 75% |
| 7 | PROCESSING_LEAD_TIME | NUMBER | NULL | Planejamento | Lead time (dias) | — | 🟡 80% |
| 8 | MIN_ORDER_QTY | NUMBER | NULL | Planejamento | Quantidade minima | — | 🟡 80% |
| 9 | FIXED_LOT_MULTIPLE | NUMBER | NULL | Planejamento | Multiplo de lote fixo | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_approved_supplier_list]] — via `ASL_ID` (registro ASL ao qual os atributos pertencem)
- [[hr_all_organization_units_f]] — via `USING_ORGANIZATION_ID` (organização que utiliza o fornecedor aprovado)
- [[po_headers_all]] — via `DOCUMENT_HEADER_ID` (PO ou acordo vinculado ao atributo ASL)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Atributos ASL
```sql
SELECT ASL_ID, PROCESSING_LEAD_TIME, MIN_ORDER_QTY
FROM   PO_ASL_ATTRIBUTES
WHERE  ASL_ID = :p_asl_id;
```


---

## 🔒 Observações

- Cada ASL pode ter multiplos registros de atributos (um por org).
- Atributos alimentam MRP/Planning para lead times.
- O `DOCUMENT_HEADER_ID` referencia Blanket Agreement.

---

## 📚 Referências

- [Oracle Docs — PO_ASL_ATTRIBUTES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poaslattributes-10180.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
