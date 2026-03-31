---
id: DOC-HCM-182
doc_type: system-doc
title: "HRQ_CATEGORIES_B — Categorias de Questionários (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - questionnaires
  - categories
aliases:
  - HRQ_CATEGORIES_B
  - hrq_categories_b
  - categorias-de-questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_CATEGORIES_B

## 📌 Visão Geral

Tabela base das **categorias de questionários** HCM.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Organização:** Categoriza questionários por tema.
- **Navegação:** Facilita busca e filtragem.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | CATEGORY_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da categoria | — | 🟡 80% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativa (Y/N) | — | 🟡 75% |
| 4 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Categorias ativas
```sql
SELECT c.CATEGORY_ID, c.CATEGORY_CODE
FROM   HRQ_CATEGORIES_B c
WHERE  NVL(c.ENABLED_FLAG,'Y') = 'Y';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_categories_tl]].

---

## 🔗 PVOs Relacionados

### [[folderp1|FolderP1]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CategoryBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | CategoryBPEOCategoryId | ✅ |
| LAST_UPDATE_DATE | CategoryBPEOLastUpdateDate | ✅ |
| SUBSCRIBER_ID | CategoryBPEOSubscriberId | ✅ |

### [[questionnairequestionfolderpvo|QuestionnaireQuestionFolderPVO]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CategoryBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | CategoryBPEOCategoryId | ✅ |
| LAST_UPDATE_DATE | CategoryBPEOLastUpdateDate | ✅ |
| SUBSCRIBER_ID | CategoryBPEOSubscriberId | — |

### [[requisitionqstnrexternalviewallpvo|RequisitionQstnrExternalViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CategoryBPEOBusinessGroupId | — |
| CATEGORY_ID | CategoryBPEOCategoryId | — |

### [[requisitionqstnrinternalviewallpvo|RequisitionQstnrInternalViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CategoryBPEOBusinessGroupId | — |
| CATEGORY_ID | CategoryBPEOCategoryId | — |

### [[requisitionqstnrinterviewviewallpvo|RequisitionQstnrInterviewViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CategoryBPEOBusinessGroupId | — |
| CATEGORY_ID | CategoryBPEOCategoryId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
