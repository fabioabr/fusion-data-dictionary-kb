---
id: DOC-PO-124
doc_type: system-doc
title: "PO_DOC_STYLE_LINES_VL — Estilos de Documento — Config de Linha (View Multilingue)"
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
  - PO_DOC_STYLE_LINES_VL
  - po_doc_style_lines_vl
  - po-doc-style-lines-vl
  - po-doc
  - estilos-de-documento-—-config-de-li
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOC_STYLE_LINES_VL

## 📌 Visão Geral

View que combina `PO_DOC_STYLE_LINES_B` e `PO_DOC_STYLE_LINES_TL` para **configuracoes com nomes traduzidos**.

> [!note] Sufixo _VL
> O sufixo `_VL` combina a tabela base `_B` com traducoes `_TL` em uma view multilingue.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta unificada:** Config de linha com traducao.
- **LOVs:** Listas de selecao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOC_STYLE_LINE_ID | NUMBER(18) | NOT NULL | PK | ID da config | — | 🟡 80% |
| 2 | STYLE_ID | NUMBER(18) | NOT NULL | FK | Estilo | [[po_doc_style_headers]] | 🟢 90% |
| 3 | LINE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de linha | [[po_line_types_b]] | 🟢 85% |
| 4 | DISPLAY_NAME | VARCHAR2(240) | NULL | Descritivo | Nome traduzido | — | 🟡 75% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_doc_style_headers]] — via `STYLE_ID` (estilo de documento da view multilíngue)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Config traduzidas
```sql
SELECT DOC_STYLE_LINE_ID, DISPLAY_NAME, ENABLED_FLAG
FROM   PO_DOC_STYLE_LINES_VL
WHERE  STYLE_ID = :p_style_id;
```


---

## 🔒 Observações

- View de conveniencia; preferir sobre joins _B/_TL.
- Retorna traducao do idioma da sessao.

---

## 📚 Referências

- [Oracle Docs — PO_DOC_STYLE_LINES_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
