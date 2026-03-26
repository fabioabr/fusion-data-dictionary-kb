---
id: DOC-HCM-279
doc_type: system-doc
title: "HR_DOR_REPORTING_LIST_V — Lista de Relatorios de Documentos de Registro (View)"
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
  - reporting
  - compliance
aliases:
  - HR_DOR_REPORTING_LIST_V
  - hr_dor_reporting_list_v
  - hr-dor-reporting-list-v
  - dor-reporting-list
  - relatorio-documentos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOR_REPORTING_LIST_V

## 📌 Visao Geral

View que consolida dados de **documentos de registro** para fins de reporting. Combina informacoes de documentos, pessoas e tipos de documento.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Relatorios:** Extracao consolidada de documentos para relatorios gerenciais.
- **Compliance:** Monitorar documentos vencidos ou pendentes.
- **BI/Analytics:** Fonte para dashboards de compliance documental.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENTS_OF_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador do documento | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de documento | [[hr_document_types_b]] | 🟢 95% |
| 4 | DOCUMENT_TYPE_NAME | VARCHAR2(240) | NULL | Dados | Nome do tipo de documento | — | 🟢 90% |
| 5 | DOCUMENT_NUMBER | VARCHAR2(150) | NULL | Dados | Numero do documento | — | 🟢 90% |
| 6 | DATE_FROM | DATE | NULL | Data | Data de emissao | — | 🟢 90% |
| 7 | DATE_TO | DATE | NULL | Data | Data de vencimento | — | 🟢 90% |
| 8 | PERSON_NAME | VARCHAR2(360) | NULL | Dados | Nome do colaborador | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador na lista de documentos obrigatorios)
- [[hr_document_types_b]] — via `DOCUMENT_TYPE_ID` (tipo de documento na lista obrigatoria)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Documentos vencidos
```sql
SELECT v.PERSON_NAME, v.DOCUMENT_TYPE_NAME,
       v.DOCUMENT_NUMBER, v.DATE_TO
FROM   HR_DOR_REPORTING_LIST_V v
WHERE  v.DATE_TO < SYSDATE;
```

---

## 🔒 Observacoes

- Sufixo `_V` indica view — somente leitura.
- Pode conter dados sensiveis (PII).

---

## 📚 Referencias

- [Oracle Docs — HR_DOR_REPORTING_LIST_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdorreportinglistv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
