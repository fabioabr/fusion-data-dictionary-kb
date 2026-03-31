---
id: DOC-PO-126
doc_type: system-doc
title: "PO_HAZARD_CLASSES_B — Classes de Risco (Base)"
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
  - PO_HAZARD_CLASSES_B
  - po_hazard_classes_b
  - po-hazard-classes-b
  - po-hazard
  - classes-de-risco-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HAZARD_CLASSES_B

## 📌 Visão Geral

Armazena as **classes de risco** (Hazard Classes) para materiais perigosos, em conjunto com UN Numbers.

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (idioma base). Traducoes ficam na tabela correspondente `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificacao de risco:** Inflamavel, corrosivo, toxico, etc.
- **Compliance regulatorio:** DOT, IATA, IMO.
- **Logistica:** Restricoes de armazenamento e transporte.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | HAZARD_CLASS_ID | NUMBER(18) | NOT NULL | PK | ID da classe | — | 🟢 90% |
| 2 | HAZARD_CLASS | VARCHAR2(40) | NOT NULL | Classificacao | Codigo da classe | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao | — | 🟢 85% |
| 4 | INACTIVE_DATE | DATE | NULL | Status | Data de inativacao | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Classes ativas
```sql
SELECT HAZARD_CLASS_ID, HAZARD_CLASS, DESCRIPTION
FROM   PO_HAZARD_CLASSES_B
WHERE  INACTIVE_DATE IS NULL OR INACTIVE_DATE > SYSDATE;
```

---

## 🔒 Observações

- Classes seguem padrao internacional (UN GHS).
- Tabela de referencia; poucas linhas.

---

## 🔗 PVOs Relacionados

### [[purchasinghazardclassextractpvo|PurchasingHazardClassExtractPVO]] (PO · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PurchasingHazardClsCreatedBy | ✅ |
| CREATION_DATE | PurchasingHazardClsCreationDate | ✅ |
| HAZARD_CLASS_CODE | PurchasingHazardClsHazardClassCode | ✅ |
| HAZARD_CLASS_ID | HazardClassId | ✅ |
| INACTIVE_DATE | PurchasingHazardClsInactiveDate | ✅ |
| LAST_UPDATE_DATE | PurchasingHazardClsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingHazardClsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PurchasingHazardClsLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PurchasingHazardClsObjectVersionNumber | ✅ |

### [[purchasinghazardclasspvo|PurchasingHazardClassPVO]] (PO · BICC: 5/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PurchasingHazardClsCreatedBy | ✅ |
| CREATION_DATE | PurchasingHazardClsCreationDate | ✅ |
| HAZARD_CLASS_CODE | PurchasingHazardClsHazardClassCode | ✅ |
| HAZARD_CLASS_ID | HazardClassId | ✅ |
| INACTIVE_DATE | PurchasingHazardClsInactiveDate | — |
| LAST_UPDATE_DATE | PurchasingHazardClsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingHazardClsLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingHazardClsLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PurchasingHazardClsObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — PO_HAZARD_CLASSES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
