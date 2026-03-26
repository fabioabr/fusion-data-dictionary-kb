---
id: DOC-HCM-280
doc_type: system-doc
title: "HR_ORGANIZATION_INFORMATION_F — Informacoes de Organizacao (Date-Effective)"
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
  - organization-info
  - configuracao
  - eav
aliases:
  - HR_ORGANIZATION_INFORMATION_F
  - hr_organization_information_f
  - hr-organization-information-f
  - org-information
  - informacoes-organizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ORGANIZATION_INFORMATION_F

## 📌 Visao Geral

Armazena **informacoes adicionais** de unidades organizacionais em formato EAV (Entity-Attribute-Value) com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Armazenar atributos especificos por tipo de organizacao.
- **Legal:** Informacoes de entidade legal (CNPJ, inscricao estadual).
- **HR:** Configuracoes de payroll, benefits e workforce por organizacao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_INFORMATION_ID | NUMBER(18) | NOT NULL | PK | Identificador da informacao | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 95% |
| 4 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Organizacao | [[hr_all_organization_units_f]] | 🟢 100% |
| 5 | ORG_INFORMATION_CONTEXT | VARCHAR2(30) | NOT NULL | Classificacao | Contexto/tipo da informacao | — | 🟢 95% |
| 6 | ORG_INFORMATION1 | VARCHAR2(240) | NULL | Dados | Valor do atributo 1 | — | 🟢 90% |
| 7 | ORG_INFORMATION2 | VARCHAR2(240) | NULL | Dados | Valor do atributo 2 | — | 🟢 90% |
| 8 | ORG_INFORMATION3 | VARCHAR2(240) | NULL | Dados | Valor do atributo 3 | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao das informacoes adicionais)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Informacoes por contexto
```sql
SELECT oi.ORG_INFORMATION_CONTEXT,
       oi.ORG_INFORMATION1, oi.ORG_INFORMATION2
FROM   HR_ORGANIZATION_INFORMATION_F oi
WHERE  oi.ORGANIZATION_ID = :p_org_id
  AND  SYSDATE BETWEEN oi.EFFECTIVE_START_DATE AND oi.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Estrutura EAV — o significado de ORG_INFORMATION1..N depende do ORG_INFORMATION_CONTEXT.
- Sufixo `_F` indica date-effective.

---

## 📚 Referencias

- [Oracle Docs — HR_ORGANIZATION_INFORMATION_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrorganizationinformationf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
