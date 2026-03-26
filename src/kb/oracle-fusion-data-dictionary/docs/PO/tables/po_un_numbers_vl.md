---
id: DOC-PO-142
doc_type: system-doc
title: "PO_UN_NUMBERS_VL — Numeros UN de Materiais Perigosos (View Multilingue)"
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
  - hazard-classes
  - seguranca
  - compliance
aliases:
  - PO_UN_NUMBERS_VL
  - po_un_numbers_vl
  - po-un-numbers-vl
  - po-un
  - numeros-un-de-materiais-perigosos-(
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_UN_NUMBERS_VL

## 📌 Visão Geral

View com **numeros UN** para classificacao de materiais perigosos, combinando dados base e traducoes.

> [!note] Sufixo _VL
> O sufixo `_VL` combina a tabela base `_B` com traducoes `_TL` em uma view multilingue.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificacao UN:** Identificacao de materiais perigosos.
- **Compliance regulatorio:** DOT/IATA/IMO.
- **Logistica:** Requisitos de embalagem e transporte.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | UN_NUMBER_ID | NUMBER(18) | NOT NULL | PK | ID do numero UN | — | 🟢 90% |
| 2 | UN_NUMBER | VARCHAR2(25) | NOT NULL | Classificacao | Numero UN (ex.: UN1203) | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 85% |
| 4 | HAZARD_CLASS_ID | NUMBER(18) | NULL | FK | Classe de risco | [[po_hazard_classes_b]] | 🟢 85% |
| 5 | INACTIVE_DATE | DATE | NULL | Status | Data de inativacao | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_hazard_classes_b]] — via `HAZARD_CLASS_ID` (classe de risco associada ao número ONU)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Materiais perigosos ativos
```sql
SELECT UN_NUMBER_ID, UN_NUMBER, DESCRIPTION
FROM   PO_UN_NUMBERS_VL
WHERE  INACTIVE_DATE IS NULL OR INACTIVE_DATE > SYSDATE;
```


---

## 🔒 Observações

- Numeros UN seguem classificacao da ONU.
- View combinando _B e _TL.
- Dados seeded.

---

## 📚 Referências

- [Oracle Docs — PO_UN_NUMBERS_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
