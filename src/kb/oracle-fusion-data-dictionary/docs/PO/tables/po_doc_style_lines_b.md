---
id: DOC-PO-122
doc_type: system-doc
title: "PO_DOC_STYLE_LINES_B — Estilos de Documento — Config de Linha (Base)"
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
  - PO_DOC_STYLE_LINES_B
  - po_doc_style_lines_b
  - po-doc-style-lines-b
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

# PO_DOC_STYLE_LINES_B

## 📌 Visão Geral

Armazena as **configuracoes de linha** dos estilos de documento de compras (tabela base).

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (idioma base). Traducoes ficam na tabela correspondente `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao de linhas:** Regras por tipo de linha.
- **Controle de campos:** Visibilidade/obrigatoriedade por tipo.
- **Validacao:** Regras de negocio por tipo de linha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOC_STYLE_LINE_ID | NUMBER(18) | NOT NULL | PK | ID da configuracao | — | 🟡 80% |
| 2 | STYLE_ID | NUMBER(18) | NOT NULL | FK | Estilo pai | [[po_doc_style_headers]] | 🟢 90% |
| 3 | LINE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de linha | [[po_line_types_b]] | 🟢 85% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_doc_style_headers]] — via `STYLE_ID` (estilo de documento ao qual a linha de estilo pertence)
- [[po_line_types_b]] — via `LINE_TYPE_ID` (tipo de linha permitido pelo estilo de documento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Tipos de linha por estilo
```sql
SELECT DOC_STYLE_LINE_ID, LINE_TYPE_ID, ENABLED_FLAG
FROM   PO_DOC_STYLE_LINES_B
WHERE  STYLE_ID = :p_style_id;
```

---

## 🔒 Observações

- Cada estilo pode ter multiplas config de linha.
- Tabela complementar ao cabecalho do estilo.

---

## 🔗 PVOs Relacionados

### [[purchasingdocumentstylelinebextractpvo|PurchasingDocumentStyleLineBExtractPVO]] (PO · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PODocumentStyleLineBCreatedBy | ✅ |
| CREATION_DATE | PODocumentStyleLineBCreationDate | ✅ |
| DOCUMENT_SUBTYPE | DocumentSubtype | ✅ |
| ENABLED_FLAG | PODocumentStyleLineBEnabledFlag | ✅ |
| LAST_UPDATE_DATE | PODocumentStyleLineBLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PODocumentStyleLineBLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PODocumentStyleLineBLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PODocumentStyleLineBObjectVersionNumber | ✅ |
| STYLE_ID | StyleId | ✅ |

### [[purchasingdocumentstylelinebp|PurchasingDocumentStyleLineBP]] (PO · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PODocumentStyleLineBCreatedBy | — |
| CREATION_DATE | PODocumentStyleLineBCreationDate | ✅ |
| DOCUMENT_SUBTYPE | DocumentSubtype | ✅ |
| ENABLED_FLAG | PODocumentStyleLineBEnabledFlag | — |
| LAST_UPDATE_DATE | PODocumentStyleLineBLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PODocumentStyleLineBLastUpdateLogin | — |
| LAST_UPDATED_BY | PODocumentStyleLineBLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PODocumentStyleLineBObjectVersionNumber | — |
| STYLE_ID | StyleId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_DOC_STYLE_LINES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
