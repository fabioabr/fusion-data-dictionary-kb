---
id: DOC-PO-123
doc_type: system-doc
title: "PO_DOC_STYLE_LINES_TL — Estilos de Documento — Config de Linha (Traducoes)"
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
  - PO_DOC_STYLE_LINES_TL
  - po_doc_style_lines_tl
  - po-doc-style-lines-tl
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

# PO_DOC_STYLE_LINES_TL

## 📌 Visão Geral

Armazena as **traducoes das configuracoes de linha** dos estilos de documento.

> [!note] Sufixo _TL
> O sufixo `_TL` indica a **tabela de traducoes**. Contem versoes traduzidas dos campos descritivos da tabela `_B` correspondente.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte multilingue:** Descricoes traduzidas.
- **Relatorios:** Labels traduzidos.

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
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | DISPLAY_NAME | VARCHAR2(240) | NULL | Descritivo | Nome traduzido | — | 🟡 75% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_doc_style_lines_b]] — via `DOC_STYLE_LINE_ID` (tradução da linha de estilo de documento)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Traducoes
```sql
SELECT DOC_STYLE_LINE_ID, LANGUAGE, DISPLAY_NAME
FROM   PO_DOC_STYLE_LINES_TL
WHERE  DOC_STYLE_LINE_ID = :p_id;
```

---

## 🔒 Observações

- Uma linha por idioma instalado.
- Usada pela view `PO_DOC_STYLE_LINES_VL`.

---

## 🔗 PVOs Relacionados

### [[purchasingdocumentstylelinebextractpvo|PurchasingDocumentStyleLineBExtractPVO]] (PO · BICC: 5/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | PODocumentStyleLineTransDisplayName | ✅ |
| DOCUMENT_SUBTYPE | PODocumentStyleLineTransDocumentSubtype | ✅ |
| LANGUAGE | PODocumentStyleLineTransLanguage | ✅ |
| SOURCE_LANG | PODocumentStyleLineTransSourceLang | ✅ |
| STYLE_ID | PODocumentStyleLineTransStyleId | ✅ |

### [[purchasingdocumentstylelinebp|PurchasingDocumentStyleLineBP]] (PO · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | PODocumentStyleLineTransDisplayName | ✅ |
| DOCUMENT_SUBTYPE | PODocumentStyleLineTransDocumentSubtype | — |
| LANGUAGE | PODocumentStyleLineTransLanguage | — |
| SOURCE_LANG | PODocumentStyleLineTransSourceLang | — |
| STYLE_ID | PODocumentStyleLineTransStyleId | — |

### [[purchasingdocumentstylelinetranslationextractpvo|PurchasingDocumentStyleLineTranslationExtractPVO]] (PO · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PODocumentStyleLineTransCreatedBy | ✅ |
| CREATION_DATE | PODocumentStyleLineTransCreationDate | ✅ |
| DISPLAY_NAME | PODocumentStyleLineTransDisplayName | ✅ |
| DOCUMENT_SUBTYPE | DocumentSubtype | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | PODocumentStyleLineTransLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PODocumentStyleLineTransLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PODocumentStyleLineTransLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PODocumentStyleLineTransObjectVersionNumber | ✅ |
| SOURCE_LANG | PODocumentStyleLineTransSourceLang | ✅ |
| STYLE_ID | StyleId | ✅ |

### [[purchasingdocumentstylelinetranslationp|PurchasingDocumentStyleLineTranslationP]] (PO · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PODocumentStyleLineTransCreatedBy | ✅ |
| CREATION_DATE | PODocumentStyleLineTransCreationDate | ✅ |
| DISPLAY_NAME | PODocumentStyleLineTransDisplayName | ✅ |
| DOCUMENT_SUBTYPE | DocumentSubtype | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | PODocumentStyleLineTransLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PODocumentStyleLineTransLastUpdateLogin | — |
| LAST_UPDATED_BY | PODocumentStyleLineTransLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PODocumentStyleLineTransObjectVersionNumber | — |
| SOURCE_LANG | PODocumentStyleLineTransSourceLang | ✅ |
| STYLE_ID | StyleId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_DOC_STYLE_LINES_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
