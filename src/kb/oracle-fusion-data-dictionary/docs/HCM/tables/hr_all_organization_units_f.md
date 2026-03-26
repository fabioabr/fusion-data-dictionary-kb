---
id: DOC-HCM-273
doc_type: system-doc
title: "HR_ALL_ORGANIZATION_UNITS_F — Unidades Organizacionais"
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
  - organization
  - estrutura
  - core-hr
aliases:
  - HR_ALL_ORGANIZATION_UNITS_F
  - hr_all_organization_units_f
  - hr-all-organization-units-f
  - all-organization-units
  - unidades-organizacionais
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ALL_ORGANIZATION_UNITS_F

## 📌 Visao Geral

Tabela principal que armazena todas as **unidades organizacionais** (departments, business units, legal entities, etc.) com versionamento date-effective. E uma das tabelas mais referenciadas do HCM.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Estrutura organizacional:** Registrar todos os tipos de organizacao.
- **Hierarquia:** Base para construcao de arvores organizacionais.
- **Multi-org:** Filtro por ORG_ID em tabelas transacionais.
- **Relatorios:** Base para todos os relatorios organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da organizacao | — | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao (date-effective) | — | 🟢 100% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 100% |
| 4 | ORGANIZATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de organizacao (DEPARTMENT, BU, LE) | — | 🟢 95% |
| 5 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negocios pai | — | 🟢 90% |
| 6 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao principal | — | 🟢 90% |
| 7 | STATUS | VARCHAR2(30) | NOT NULL | Classificacao | Status (A = Ativo, I = Inativo) | — | 🟢 95% |
| 8 | INTERNAL_EXTERNAL_FLAG | VARCHAR2(1) | NULL | Classificacao | Interna (I) ou Externa (E) | — | 🟢 90% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hr_organization_units_f_tl]] — via `ORGANIZATION_ID` (traducoes multilingue do registro)
- [[hr_org_unit_classifications_f]] — via `ORGANIZATION_ID` (classificacoes da unidade organizacional)
- [[hr_organization_information_f]] — via `ORGANIZATION_ID` (informacoes adicionais da organizacao)

---

## 📎 Uso Tipico

### Departamentos ativos
```sql
SELECT o.ORGANIZATION_ID, o.ORGANIZATION_TYPE, o.STATUS
FROM   HR_ALL_ORGANIZATION_UNITS_F o
WHERE  o.STATUS = 'A'
  AND  SYSDATE BETWEEN o.EFFECTIVE_START_DATE AND o.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica tabela date-effective (versionada por data).
- PK composta: (ORGANIZATION_ID, EFFECTIVE_START_DATE).
- Uma das tabelas mais referenciadas — usada como ORG_ID em quase todas as tabelas transacionais.

---

## 📚 Referencias

- [Oracle Docs — HR_ALL_ORGANIZATION_UNITS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrallorganizationunitsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
