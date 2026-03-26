---
id: DOC-HCM-277
doc_type: system-doc
title: "HR_DOCUMENT_TYPES_B — Tipos de Documento — Base"
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
  - document-types
  - configuracao
  - compliance
aliases:
  - HR_DOCUMENT_TYPES_B
  - hr_document_types_b
  - hr-document-types-b
  - document-types-base
  - tipos-documento-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOCUMENT_TYPES_B

## 📌 Visao Geral

Tabela base que define os **tipos de documento** disponiveis para registro de colaboradores (e.g., Passaporte, RG, CPF, Diploma, Certificacao).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir tipos de documento por legislacao.
- **Compliance:** Controlar quais documentos sao obrigatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador do tipo | — | 🟢 100% |
| 2 | DOCUMENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do tipo | — | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificacao | Legislacao aplicavel | — | 🟢 90% |
| 4 | CATEGORY_CODE | VARCHAR2(30) | NULL | Classificacao | Categoria do documento | — | 🟡 80% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NOT NULL | Classificacao | Ativo (Y/N) | — | 🟢 90% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hr_document_types_tl]] — via `DOCUMENT_TYPE_ID` (traducoes multilingue do registro)
- [[hr_documents_of_record]] — via `DOCUMENT_TYPE_ID` (documentos registrados do tipo)

---

## 📎 Uso Tipico

### Tipos de documento ativos
```sql
SELECT dt.DOCUMENT_TYPE_ID, dt.DOCUMENT_TYPE_CODE, dt.LEGISLATION_CODE
FROM   HR_DOCUMENT_TYPES_B dt
WHERE  dt.ACTIVE_FLAG = 'Y';
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hr_document_types_tl]].
- Tipos podem ser especificos por legislacao (LEGISLATION_CODE).

---

## 📚 Referencias

- [Oracle Docs — HR_DOCUMENT_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdocumenttypesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
