---
id: DOC-PO-145
doc_type: system-doc
title: "PO_VERSIONS_UNPROCESSED_V — Versoes Nao Processadas de PO (View)"
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
  - PO_VERSIONS_UNPROCESSED_V
  - po_versions_unprocessed_v
  - po-versions-unprocessed-v
  - po-versions
  - versoes-nao-processadas-de-po-(view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_VERSIONS_UNPROCESSED_V

## 📌 Visão Geral

View com **versoes de PO nao processadas** por sistemas downstream. Identifica alteracoes pendentes de sincronizacao.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integracao:** Versoes pendentes de sincronizacao.
- **Notificacoes:** Alteracoes nao notificadas.
- **Processamento batch:** Fila de versoes a processar.

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
| 2 | VERSION_NUM | NUMBER | NULL | Identificacao | Versao | — | 🟡 75% |
| 3 | STATUS | VARCHAR2(25) | NULL | Status | Status de processamento | — | 🟡 70% |
| 4 | CREATION_DATE | TIMESTAMP | NULL | Data | Data de criacao | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (PO com versões ainda não processadas)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versoes pendentes
```sql
SELECT PO_HEADER_ID, VERSION_NUM, STATUS, CREATION_DATE
FROM   PO_VERSIONS_UNPROCESSED_V
ORDER BY CREATION_DATE;
```


---

## 🔒 Observações

- Utilizada por processos de integracao.
- Deve ser consultada periodicamente por jobs de sync.

---

## 📚 Referências

- [Oracle Docs — PO_VERSIONS_UNPROCESSED_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
