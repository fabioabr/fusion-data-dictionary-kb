---
id: DOC-PO-130
doc_type: system-doc
title: "PO_HEADERS_ARCHIVE_ALL — Arquivo de Cabecalhos de PO (Versionamento)"
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
  - PO_HEADERS_ARCHIVE_ALL
  - po_headers_archive_all
  - po-headers-archive-all
  - po-headers
  - arquivo-de-cabecalhos-de-po-(versio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HEADERS_ARCHIVE_ALL

## 📌 Visão Geral

Armazena **versoes arquivadas dos cabecalhos de PO**. Cada revisao gera copia do cabecalho anterior para rastreabilidade.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Versionamento:** Historico de alteracoes de cabecalho.
- **Auditoria:** Comparacao entre versoes.
- **Compliance:** Evidencia de alteracoes.
- **Rollback:** Referencia para reversao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID do cabecalho | [[po_headers_all]] | 🟢 100% |
| 2 | REVISION_NUM | NUMBER | NOT NULL | PK | Revisao arquivada | — | 🟢 100% |
| 3 | SEGMENT1 | VARCHAR2(20) | NOT NULL | Identificacao | Numero do PO | — | 🟢 100% |
| 4 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 5 | AUTHORIZATION_STATUS | VARCHAR2(25) | NULL | Status | Status na revisao | — | 🟢 100% |
| 6 | APPROVED_DATE | DATE | NULL | Data | Data de aprovacao | — | 🟢 95% |
| 7 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra original do registro arquivado)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do PO na versão arquivada)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versoes de um PO
```sql
SELECT REVISION_NUM, AUTHORIZATION_STATUS, APPROVED_DATE
FROM   PO_HEADERS_ARCHIVE_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY REVISION_NUM;
```


---

## 🔒 Observações

- PK composta: `PO_HEADER_ID` + `REVISION_NUM`.
- Estrutura espelha `PO_HEADERS_ALL`.
- Cada revisao gera novo registro.

---

## 📚 Referências

- [Oracle Docs — PO_HEADERS_ARCHIVE_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
