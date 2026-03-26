---
id: DOC-PO-128
doc_type: system-doc
title: "PO_HAZARD_CLASSES_VL — Classes de Risco (View Multilingue)"
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
  - PO_HAZARD_CLASSES_VL
  - po_hazard_classes_vl
  - po-hazard-classes-vl
  - po-hazard
  - classes-de-risco-(view-multilingue)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HAZARD_CLASSES_VL

## 📌 Visão Geral

View que combina `PO_HAZARD_CLASSES_B` e `PO_HAZARD_CLASSES_TL` para **classes com descricoes traduzidas**.

> [!note] Sufixo _VL
> O sufixo `_VL` combina a tabela base `_B` com traducoes `_TL` em uma view multilingue.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta unificada:** Classes com traducao.
- **LOVs:** Listas de selecao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HAZARD_CLASS_ID | NUMBER(18) | NOT NULL | PK | ID | — | 🟢 90% |
| 2 | HAZARD_CLASS | VARCHAR2(40) | NOT NULL | Classificacao | Codigo | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao traduzida | — | 🟢 85% |
| 4 | INACTIVE_DATE | DATE | NULL | Status | Data de inativacao | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Classes traduzidas
```sql
SELECT HAZARD_CLASS_ID, HAZARD_CLASS, DESCRIPTION
FROM   PO_HAZARD_CLASSES_VL
WHERE  INACTIVE_DATE IS NULL OR INACTIVE_DATE > SYSDATE;
```


---

## 🔒 Observações

- View de conveniencia.
- Retorna traducao do idioma da sessao.

---

## 📚 Referências

- [Oracle Docs — PO_HAZARD_CLASSES_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
