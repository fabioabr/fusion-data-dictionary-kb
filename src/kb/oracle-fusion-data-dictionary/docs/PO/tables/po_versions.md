---
id: DOC-PO-143
doc_type: system-doc
title: "PO_VERSIONS — Versoes de Documentos de Compras"
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
  - PO_VERSIONS
  - po_versions
  - po-versions
  - po-versions
  - versoes-de-documentos-de-compras
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_VERSIONS

## 📌 Visão Geral

Armazena as **versoes de documentos de compras**. Cada alteracao aprovada gera nova versao para rastreamento.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Versionamento:** Controle de versoes.
- **Auditoria:** Rastreamento de alteracoes.
- **Compliance:** Evidencia para auditorias.
- **Comparacao:** Base para diff entre versoes.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VERSION_ID | NUMBER(18) | NOT NULL | PK | ID da versao | — | 🟡 80% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟢 95% |
| 3 | VERSION_NUM | NUMBER | NOT NULL | Identificacao | Numero da versao | — | 🟢 95% |
| 4 | STATUS | VARCHAR2(25) | NULL | Status | Status da versao | — | 🟡 80% |
| 5 | CHANGE_DESCRIPTION | VARCHAR2(2000) | NULL | Descritivo | Descricao da alteracao | — | 🟡 75% |
| 6 | APPROVED_DATE | DATE | NULL | Data | Data de aprovacao | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra versionado)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versoes de um PO
```sql
SELECT VERSION_ID, VERSION_NUM, STATUS, CHANGE_DESCRIPTION, APPROVED_DATE
FROM   PO_VERSIONS
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY VERSION_NUM;
```


---

## 🔒 Observações

- Cada aprovacao incrementa `VERSION_NUM`.
- Complementa `PO_HEADERS_ARCHIVE_ALL`.
- O `CHANGE_DESCRIPTION` contem resumo das alteracoes.

---

## 📚 Referências

- [Oracle Docs — PO_VERSIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
