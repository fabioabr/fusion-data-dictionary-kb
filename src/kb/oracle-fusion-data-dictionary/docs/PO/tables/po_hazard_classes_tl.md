---
id: DOC-PO-127
doc_type: system-doc
title: "PO_HAZARD_CLASSES_TL — Classes de Risco (Traducoes)"
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
  - PO_HAZARD_CLASSES_TL
  - po_hazard_classes_tl
  - po-hazard-classes-tl
  - po-hazard
  - classes-de-risco-(traducoes)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HAZARD_CLASSES_TL

## 📌 Visão Geral

Armazena as **traducoes das classes de risco**.

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
| 1 | HAZARD_CLASS_ID | NUMBER(18) | NOT NULL | PK | ID da classe | [[po_hazard_classes_b]] | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao traduzida | — | 🟢 85% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_hazard_classes_b]] — via `HAZARD_CLASS_ID` (tradução da classe de risco de material)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Traducoes
```sql
SELECT HAZARD_CLASS_ID, LANGUAGE, DESCRIPTION
FROM   PO_HAZARD_CLASSES_TL
WHERE  HAZARD_CLASS_ID = :p_id;
```


---

## 🔒 Observações

- Uma linha por idioma.
- Usada pela view `PO_HAZARD_CLASSES_VL`.

---

## 📚 Referências

- [Oracle Docs — PO_HAZARD_CLASSES_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
