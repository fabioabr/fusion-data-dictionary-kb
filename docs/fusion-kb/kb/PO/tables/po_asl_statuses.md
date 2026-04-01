---
id: DOC-PO-113
doc_type: system-doc
title: "PO_ASL_STATUSES — Status da Lista de Fornecedores Aprovados"
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
  - approved-supplier-list
  - asl
  - sourcing
aliases:
  - PO_ASL_STATUSES
  - po_asl_statuses
  - po-asl-statuses
  - po-asl
  - status-da-lista-de-fornecedores-apr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ASL_STATUSES

## 📌 Visão Geral

Armazena os **status possiveis para entradas da ASL**. Define valores como Aprovado, Desqualificado, Novo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definicao de status:** Configuracao dos status disponiveis para ASL.
- **Workflow:** Controle de ciclo de vida das entradas ASL.
- **Relatorios:** Classificacao por status de aprovacao.
- **Validacao:** Filtragem de fornecedores elegiveis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATUS_ID | NUMBER(18) | NOT NULL | PK | ID do status | — | 🟢 90% |
| 2 | STATUS | VARCHAR2(25) | NOT NULL | Classificacao | Codigo do status | — | 🟢 95% |
| 3 | STATUS_DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 90% |
| 4 | ASL_DEFAULT_FLAG | VARCHAR2(1) | NULL | Flag | Status padrao (Y/N) | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)
- [[po_approved_supplier_list]] — via `ASL_STATUS_ID` (registros ASL que possuem este status)

---

## 📎 Uso Típico

### Status disponiveis
```sql
SELECT STATUS_ID, STATUS, STATUS_DESCRIPTION
FROM   PO_ASL_STATUSES
ORDER BY STATUS;
```

---

## 🔒 Observações

- Valores tipicos: APPROVED, NEW, DISQUALIFIED, DEBARRED.
- Flag `ASL_DEFAULT_FLAG` define status automatico para novas entradas.
- Tabela de configuracao; poucas linhas, raramente alterada.

---

## 🔗 PVOs Relacionados

### [[purchasingaslextractpvo|PurchasingASLExtractPVO]] (PO · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS | Status | ✅ |
| STATUS_ID | StatusId | ✅ |

### [[purchasingaslpvo|PurchasingASLPVO]] (PO · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS | Status | ✅ |
| STATUS_ID | StatusId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_ASL_STATUSES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
