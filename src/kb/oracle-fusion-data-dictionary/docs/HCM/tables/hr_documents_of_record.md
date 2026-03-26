---
id: DOC-HCM-276
doc_type: system-doc
title: "HR_DOCUMENTS_OF_RECORD — Documentos de Registro"
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
  - documents
  - compliance
  - pessoal
aliases:
  - HR_DOCUMENTS_OF_RECORD
  - hr_documents_of_record
  - hr-documents-of-record
  - documents-of-record
  - documentos-registro
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOCUMENTS_OF_RECORD

## 📌 Visao Geral

Armazena os **documentos de registro** (documents of record) dos colaboradores — carteira de identidade, passaporte, certidoes, diplomas e outros documentos legais/pessoais.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Compliance:** Manter documentos obrigatorios de colaboradores.
- **Vencimento:** Controlar validade de documentos.
- **Auditoria:** Rastrear documentos entregues por colaboradores.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENTS_OF_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador do documento | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador proprietario | [[per_all_people_f]] | 🟢 95% |
| 3 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de documento | [[hr_document_types_b]] | 🟢 95% |
| 4 | DOCUMENT_NUMBER | VARCHAR2(150) | NULL | Dados | Numero do documento | — | 🟢 90% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de emissao | — | 🟢 90% |
| 6 | DATE_TO | DATE | NULL | Data | Data de vencimento | — | 🟢 90% |
| 7 | ISSUING_AUTHORITY | VARCHAR2(240) | NULL | Dados | Autoridade emissora | — | 🟡 80% |
| 8 | ISSUING_COUNTRY | VARCHAR2(30) | NULL | Dados | Pais de emissao | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do documento registrado)
- [[hr_document_types_b]] — via `DOCUMENT_TYPE_ID` (tipo do documento registrado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Documentos de um colaborador
```sql
SELECT dor.DOCUMENT_NUMBER, dor.DATE_FROM, dor.DATE_TO
FROM   HR_DOCUMENTS_OF_RECORD dor
WHERE  dor.PERSON_ID = :p_person_id;
```

---

## 🔒 Observacoes

- Pode conter dados sensiveis (PII) — aplicar controle de acesso.
- DATE_TO indica vencimento — documentos vencidos devem gerar alertas.

---

## 📚 Referencias

- [Oracle Docs — HR_DOCUMENTS_OF_RECORD](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdocumentsofrecord.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
