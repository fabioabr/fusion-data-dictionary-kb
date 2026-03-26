---
id: DOC-PO-121
doc_type: system-doc
title: "PO_DOC_STYLE_HEADERS — Estilos de Documento de Compras (Cabecalho)"
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
  - PO_DOC_STYLE_HEADERS
  - po_doc_style_headers
  - po-doc-style-headers
  - po-doc
  - estilos-de-documento-de-compras-(ca
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOC_STYLE_HEADERS

## 📌 Visão Geral

Armazena os **estilos de documento de compras** (Document Styles). Define templates de comportamento para POs controlando campos e funcionalidades habilitados.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Templates de PO:** Funcionalidades por estilo (retro-pricing, price break).
- **Simplificacao:** Oculta campos desnecessarios.
- **Padronizacao:** Uniformidade na criacao de documentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STYLE_ID | NUMBER(18) | NOT NULL | PK | ID do estilo | — | 🟢 95% |
| 2 | STYLE_NAME | VARCHAR2(240) | NULL | Descritivo | Nome do estilo | — | 🟢 90% |
| 3 | STATUS | VARCHAR2(25) | NULL | Status | ACTIVE/INACTIVE | — | 🟢 85% |
| 4 | STYLE_TYPE | VARCHAR2(25) | NULL | Classificacao | PO ou PA | — | 🟡 80% |
| 5 | ADVANCES_FLAG | VARCHAR2(1) | NULL | Flag | Permite adiantamentos | — | 🟡 75% |
| 6 | RETRO_PRICING_FLAG | VARCHAR2(1) | NULL | Flag | Permite retro-pricing | — | 🟡 75% |
| 7 | PRICE_BREAKS_FLAG | VARCHAR2(1) | NULL | Flag | Permite price breaks | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Estilos ativos
```sql
SELECT STYLE_ID, STYLE_NAME, STYLE_TYPE
FROM   PO_DOC_STYLE_HEADERS
WHERE  STATUS = 'ACTIVE';
```


---

## 🔒 Observações

- Estilo atribuido ao PO na criacao e controla comportamento.
- Flags controlam funcionalidades disponiveis.
- Tabela de configuracao; poucas linhas.

---

## 📚 Referências

- [Oracle Docs — PO_DOC_STYLE_HEADERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
