---
id: DOC-PO-137
doc_type: system-doc
title: "PO_LINE_TYPES_TL — Tipos de Linha de PO (Traducoes)"
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
  - PO_LINE_TYPES_TL
  - po_line_types_tl
  - po-line-types-tl
  - po-line
  - tipos-de-linha-de-po-(traducoes)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_TYPES_TL

## 📌 Visão Geral

Armazena as **traducoes dos tipos de linha de PO**.

> [!note] Sufixo _TL
> O sufixo `_TL` indica a **tabela de traducoes**. Contem versoes traduzidas dos campos descritivos da tabela `_B` correspondente.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte multilingue:** Nomes traduzidos.
- **Interface:** Labels traduzidos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_TYPE_ID | NUMBER(18) | NOT NULL | PK | ID do tipo | [[po_line_types_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | LINE_TYPE | VARCHAR2(25) | NOT NULL | Descritivo | Nome traduzido | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao traduzida | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_line_types_b]] — via `LINE_TYPE_ID` (tradução do tipo de linha de compra)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Traducoes
```sql
SELECT LINE_TYPE_ID, LANGUAGE, LINE_TYPE, DESCRIPTION
FROM   PO_LINE_TYPES_TL
WHERE  LINE_TYPE_ID = :p_id;
```

---

## 🔒 Observações

- Uma linha por idioma.
- Complementa a tabela base.

---

## 🔗 PVOs Relacionados

### [[purchasinglinetypebp|PurchasingLineTypeBP]] (PO · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | POLineTypeTransDescription | ✅ |
| LANGUAGE | POLineTypeTransLanguage | — |
| LINE_TYPE | POLineTypeTransLineType | ✅ |
| LINE_TYPE_ID | POLineTypeTransLineTypeId | — |
| SOURCE_LANG | POLineTypeTransSourceLang | — |

### [[purchasinglinetypetranslationextractpvo|PurchasingLineTypeTranslationExtractPVO]] (PO · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | POLineTypeTransCreatedBy | ✅ |
| CREATION_DATE | POLineTypeTransCreationDate | ✅ |
| DESCRIPTION | POLineTypeTransDescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | POLineTypeTransLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POLineTypeTransLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | POLineTypeTransLastUpdatedBy | ✅ |
| LINE_TYPE | POLineTypeTransLineType | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| OBJECT_VERSION_NUMBER | POLineTypeTransObjectVersionNumber | ✅ |
| SOURCE_LANG | POLineTypeTransSourceLang | ✅ |

### [[purchasinglinetypetranslationp|PurchasingLineTypeTranslationP]] (PO · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | POLineTypeTransCreatedBy | ✅ |
| CREATION_DATE | POLineTypeTransCreationDate | ✅ |
| DESCRIPTION | POLineTypeTransDescription | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | POLineTypeTransLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POLineTypeTransLastUpdateLogin | — |
| LAST_UPDATED_BY | POLineTypeTransLastUpdatedBy | ✅ |
| LINE_TYPE | POLineTypeTransLineType | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| OBJECT_VERSION_NUMBER | POLineTypeTransObjectVersionNumber | — |
| SOURCE_LANG | POLineTypeTransSourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_LINE_TYPES_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
