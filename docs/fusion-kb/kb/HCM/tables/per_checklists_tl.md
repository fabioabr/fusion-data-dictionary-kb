---
id: DOC-HCM-640
doc_type: system-doc
title: "PER_CHECKLISTS_TL — Templates de Checklist (Traduções)"
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
  - PER_CHECKLISTS_TL
  - per_checklists_tl
  - per-checklists-tl
  - templates-de-checklist-(traduções)
  - per-checklists-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHECKLISTS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos templates de checklist em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe nomes de checklists no idioma do usuário.
- **Consistência** — tradução centralizada dos templates.
- **Self-service** — interface traduzida para colaboradores e gestores.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECKLIST_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do template | PER_CHECKLISTS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | CHECKLIST_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do checklist | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(600) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (tabela base do template de checklist)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Templates de checklist em português
```sql
SELECT tl.CHECKLIST_ID, tl.CHECKLIST_NAME
FROM   PER_CHECKLISTS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `CHECKLIST_ID` + `LANGUAGE`.
---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHECKLIST_DETAILS | ChecklistTemplateTranslationPEOChecklistDetails | ✅ |
| CHECKLIST_ID | ChecklistTemplateTranslationPEOChecklistId | — |
| DESCRIPTION | ChecklistTemplateTranslationPEODescription | ✅ |
| LANGUAGE | ChecklistTemplateTranslationPEOLanguage | — |
| MESSAGE_TEXT | ChecklistTemplateTranslationPEOMessageText | ✅ |
| MESSAGE_TITLE | ChecklistTemplateTranslationPEOMessageTitle | ✅ |
| NAME | ChecklistTemplateTranslationPEOName | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHECKLIST_DETAILS | ChecklistTemplateTranslationPEOChecklistDetails | ✅ |
| CHECKLIST_ID | ChecklistTemplateTranslationPEOChecklistId | — |
| DESCRIPTION | ChecklistTemplateTranslationPEODescription | ✅ |
| LANGUAGE | ChecklistTemplateTranslationPEOLanguage | — |
| MESSAGE_TEXT | ChecklistTemplateTranslationPEOMessageText | ✅ |
| MESSAGE_TITLE | ChecklistTemplateTranslationPEOMessageTitle | ✅ |
| NAME | ChecklistTemplateTranslationPEOName | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_CHECKLISTS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percheckliststl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
