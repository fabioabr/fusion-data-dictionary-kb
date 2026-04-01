---
id: DOC-HCM-620
doc_type: system-doc
title: "PER_ALLOCATED_CHECKLISTS_TL — Checklists Alocados (Traduções)"
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
  - workforce-management
  - traducoes
  - checklists-tl
aliases:
  - PER_ALLOCATED_CHECKLISTS_TL
  - per_allocated_checklists_tl
  - per-allocated-checklists-tl
  - checklists-alocados-(traduções)
  - per-allocated-checkl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_CHECKLISTS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos checklists alocados em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe checklists no idioma do colaborador.
- **Self-service** — interface traduzida para o usuário final.
- **Consistência** — tradução centralizada dos nomes de checklist.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do checklist alocado | PER_ALLOCATED_CHECKLISTS | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | CHECKLIST_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do checklist | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_checklists]] — via `ALLOCATED_CHECKLIST_ID` (tabela base do checklist alocado)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Checklists alocados em português
```sql
SELECT tl.ALLOCATED_CHECKLIST_ID, tl.CHECKLIST_NAME
FROM   PER_ALLOCATED_CHECKLISTS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ALLOCATED_CHECKLIST_ID` + `LANGUAGE`.
- Sempre usar JOIN com a tabela principal para dados completos.
---

## 🔗 PVOs Relacionados

### [[allocatedchecklistspvo|AllocatedChecklistsPVO]] (HCM · BICC: 4/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistranslationAllocatedChecklistId | — |
| BUSINESS_GROUP_ID | AllocatedChecklistranslationBusinessGroupId | — |
| CHECKLIST_DETAILS | AllocatedChecklistranslationChecklistDetails | — |
| CHECKLIST_NAME | AllocatedChecklistranslationChecklistName | — |
| CHECKLIST_NAME | AllocatedChecklistsPEOChecklistName | ✅ |
| CREATED_BY | AllocatedChecklistranslationCreatedBy | — |
| CREATION_DATE | AllocatedChecklistranslationCreationDate | — |
| DESCRIPTION | AllocatedChecklistranslationDescription | — |
| DESCRIPTION | AllocatedChecklistsPEODescription | ✅ |
| LANGUAGE | AllocatedChecklistranslationLanguage | — |
| LAST_UPDATE_DATE | AllocatedChecklistranslationLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | AllocatedChecklistranslationLastUpdatedBy | — |
| MESSAGE_TEXT | AllocatedChecklistranslationMessageText | ✅ |
| MESSAGE_TITLE | AllocatedChecklistranslationMessageTitle | ✅ |
| OBJECT_VERSION_NUMBER | AllocatedChecklistranslationObjectVersionNumber | — |
| SOURCE_LANG | AllocatedChecklistranslationSourceLang | — |

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 4/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistranslationAllocatedChecklistId | — |
| BUSINESS_GROUP_ID | AllocatedChecklistranslationBusinessGroupId | — |
| CHECKLIST_DETAILS | AllocatedChecklistranslationChecklistDetails | — |
| CHECKLIST_NAME | AllocatedChecklistranslationChecklistName | — |
| CHECKLIST_NAME | AllocatedChecklistsPEOChecklistName | ✅ |
| CREATED_BY | AllocatedChecklistranslationCreatedBy | — |
| CREATION_DATE | AllocatedChecklistranslationCreationDate1 | — |
| DESCRIPTION | AllocatedChecklistranslationDescription | — |
| DESCRIPTION | AllocatedChecklistsPEODescription | ✅ |
| LANGUAGE | AllocatedChecklistranslationLanguage | — |
| LAST_UPDATE_DATE | AllocatedChecklistranslationLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AllocatedChecklistranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | AllocatedChecklistranslationLastUpdatedBy | — |
| MESSAGE_TEXT | AllocatedChecklistranslationMessageText | ✅ |
| MESSAGE_TITLE | AllocatedChecklistranslationMessageTitle | ✅ |
| OBJECT_VERSION_NUMBER | AllocatedChecklistranslationObjectVersionNumber | — |
| SOURCE_LANG | AllocatedChecklistranslationSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_CHECKLISTS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedcheckliststl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
