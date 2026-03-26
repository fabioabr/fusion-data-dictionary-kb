---
id: DOC-PO-144
doc_type: system-doc
title: "PO_VERSIONS_INIT_SEQUENCE_V — Sequencia Inicial de Versoes de PO (View)"
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
  - versionamento
  - change-tracking
  - versoes
aliases:
  - PO_VERSIONS_INIT_SEQUENCE_V
  - po_versions_init_sequence_v
  - po-versions-init-sequence-v
  - po-versions
  - sequencia-inicial-de-versoes-de-po-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_VERSIONS_INIT_SEQUENCE_V

## 📌 Visão Geral

View com a **sequencia inicial de versoes** de documentos de compras. Identifica a versao baseline.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Baseline:** Versao inicial de cada PO.
- **Auditoria:** Referencia para comparacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟡 80% |
| 2 | INIT_VERSION_NUM | NUMBER | NULL | Identificacao | Versao inicial | — | 🟡 75% |
| 3 | INIT_CREATION_DATE | TIMESTAMP | NULL | Data | Data da versao inicial | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (PO da sequência inicial de versões)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versao inicial
```sql
SELECT PO_HEADER_ID, INIT_VERSION_NUM, INIT_CREATION_DATE
FROM   PO_VERSIONS_INIT_SEQUENCE_V
WHERE  PO_HEADER_ID = :p_po_header_id;
```


---

## 🔒 Observações

- View derivada de `PO_VERSIONS`.
- Util para identificar a baseline.

---

## 📚 Referências

- [Oracle Docs — PO_VERSIONS_INIT_SEQUENCE_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
