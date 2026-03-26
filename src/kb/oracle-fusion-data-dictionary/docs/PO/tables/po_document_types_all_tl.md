---
id: DOC-PO-119
doc_type: system-doc
title: "PO_DOCUMENT_TYPES_ALL_TL — Tipos de Documento de Compras (Traducoes)"
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
  - PO_DOCUMENT_TYPES_ALL_TL
  - po_document_types_all_tl
  - po-document-types-all-tl
  - po-document
  - tipos-de-documento-de-compras-(trad
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOCUMENT_TYPES_ALL_TL

## 📌 Visão Geral

Armazena as **traducoes dos tipos de documento de compras** definidos em `PO_DOCUMENT_TYPES_ALL_B`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica a **tabela de traducoes**. Contem versoes traduzidas dos campos descritivos da tabela `_B` correspondente.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte multilingue:** Nomes de tipos traduzidos.
- **Relatorios:** Exibicao traduzida.
- **Interface:** Labels traduzidos na UI.

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
| 4 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 5 | TYPE_NAME | VARCHAR2(80) | NOT NULL | Descritivo | Nome traduzido | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_document_types_all_b]] — via `DOCUMENT_TYPE_CODE` + `DOCUMENT_SUBTYPE` + `ORG_ID` (tradução do tipo de documento de compras)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Tipos traduzidos
```sql
SELECT DOCUMENT_TYPE_CODE, LANGUAGE, TYPE_NAME
FROM   PO_DOCUMENT_TYPES_ALL_TL
WHERE  ORG_ID = :p_org_id AND LANGUAGE = 'PTB';
```


---

## 🔒 Observações

- Uma linha por idioma instalado.
- Usada pela view `PO_DOCUMENT_TYPES_VL`.

---

## 📚 Referências

- [Oracle Docs — PO_DOCUMENT_TYPES_ALL_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
