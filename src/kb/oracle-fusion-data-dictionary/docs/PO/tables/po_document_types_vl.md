---
id: DOC-PO-120
doc_type: system-doc
title: "PO_DOCUMENT_TYPES_VL — Tipos de Documento de Compras (View Multilingue)"
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
  - document-types
  - configuracao
  - po-setup
aliases:
  - PO_DOCUMENT_TYPES_VL
  - po_document_types_vl
  - po-document-types-vl
  - po-document
  - tipos-de-documento-de-compras-(view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOCUMENT_TYPES_VL

## 📌 Visão Geral

View que combina `PO_DOCUMENT_TYPES_ALL_B` e `PO_DOCUMENT_TYPES_ALL_TL` para **tipos de documento com nomes traduzidos**.

> [!note] Sufixo _VL
> O sufixo `_VL` combina a tabela base `_B` com traducoes `_TL` em uma view multilingue.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** Tipos com traducao em uma unica view.
- **LOVs:** Listas de selecao na interface.
- **Relatorios:** Nomes traduzidos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENT_TYPE_CODE | VARCHAR2(25) | NOT NULL | PK | Codigo do tipo | — | 🟢 95% |
| 2 | DOCUMENT_SUBTYPE | VARCHAR2(25) | NOT NULL | PK | Subtipo | — | 🟢 95% |
| 3 | ORG_ID | NUMBER(18) | NOT NULL | PK | Business unit | — | 🟢 95% |
| 4 | TYPE_NAME | VARCHAR2(80) | NULL | Descritivo | Nome traduzido | — | 🟢 95% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Tipos traduzidos habilitados
```sql
SELECT DOCUMENT_TYPE_CODE, DOCUMENT_SUBTYPE, TYPE_NAME
FROM   PO_DOCUMENT_TYPES_VL
WHERE  ORG_ID = :p_org_id AND ENABLED_FLAG = 'Y';
```


---

## 🔒 Observações

- Preferir sobre consultas diretas _B/_TL.
- Retorna traducao do idioma da sessao.

---

## 📚 Referências

- [Oracle Docs — PO_DOCUMENT_TYPES_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
