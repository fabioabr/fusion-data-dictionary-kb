---
id: DOC-PO-118
doc_type: system-doc
title: "PO_DOCUMENT_TYPES_ALL_B — Tipos de Documento de Compras (Base)"
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
  - PO_DOCUMENT_TYPES_ALL_B
  - po_document_types_all_b
  - po-document-types-all-b
  - po-document
  - tipos-de-documento-de-compras-(base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOCUMENT_TYPES_ALL_B

## 📌 Visão Geral

Armazena os **tipos de documento de compras** disponiveis no modulo Procurement. Define STANDARD, BLANKET, CONTRACT, PLANNED com regras de processamento.

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (idioma base). Traducoes ficam na tabela correspondente `_TL`.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao:** Tipos de documento disponiveis.
- **Regras:** Comportamento de aprovacao, numeracao e matching.
- **Validacao:** Restricao a tipos configurados.

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
| 3 | ORG_ID | NUMBER(18) | NOT NULL | PK/Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado (Y/N) | — | 🟢 90% |
| 5 | FORWARDING_MODE_CODE | VARCHAR2(25) | NULL | Classificacao | Modo de encaminhamento | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do tipo de documento de compras)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Tipos habilitados
```sql
SELECT DOCUMENT_TYPE_CODE, DOCUMENT_SUBTYPE, ENABLED_FLAG
FROM   PO_DOCUMENT_TYPES_ALL_B
WHERE  ORG_ID = :p_org_id AND ENABLED_FLAG = 'Y';
```


---

## 🔒 Observações

- PK composta: `DOCUMENT_TYPE_CODE` + `DOCUMENT_SUBTYPE` + `ORG_ID`.
- Tipos comuns: STANDARD, BLANKET, CONTRACT, PLANNED.
- Tabela de configuracao; raramente alterada.

---

## 📚 Referências

- [Oracle Docs — PO_DOCUMENT_TYPES_ALL_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
