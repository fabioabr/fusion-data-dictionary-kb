---
id: DOC-HCM-282
doc_type: system-doc
title: "HR_ORG_CLASSIFICATIONS — Classificacoes de Organizacao"
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
  - org-classifications
  - estrutura
  - core-hr
aliases:
  - HR_ORG_CLASSIFICATIONS
  - hr_org_classifications
  - hr-org-classifications
  - org-classifications
  - classificacoes-organizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ORG_CLASSIFICATIONS

## 📌 Visao Geral

Armazena as **classificacoes** atribuidas a organizacoes — cada organizacao pode ter multiplas classificacoes (e.g., Entidade Legal, Business Unit, Departamento).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Classificacao:** Atribuir multiplos papeis a uma organizacao.
- **Filtro:** Identificar organizacoes por tipo/papel.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador da classificacao | — | 🟢 95% |
| 2 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Organizacao classificada | [[hr_all_organization_units_f]] | 🟢 100% |
| 3 | CLASSIFICATION_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Codigo da classificacao | — | 🟢 95% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificacao | Habilitada (Y/N) | — | 🟢 90% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao da classificacao)

### Tabelas-filha (FK de saida)
- [[hr_org_classifications_tl]] — via `ORG_CLASSIFICATION_ID` (traducoes multilingue do registro)

---

## 📎 Uso Tipico

### Classificacoes de uma organizacao
```sql
SELECT oc.CLASSIFICATION_CODE, oc.ENABLED_FLAG
FROM   HR_ORG_CLASSIFICATIONS oc
WHERE  oc.ORGANIZATION_ID = :p_org_id
  AND  oc.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observacoes

- Uma organizacao pode ter multiplas classificacoes habilitadas.
- Classificacoes comuns: HR_BU, HR_LEGAL_ENTITY, DEPARTMENT, HR_PAYROLL.

---

## 📚 Referencias

- [Oracle Docs — HR_ORG_CLASSIFICATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrorgclassifications.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[orgunitclassificationpvo|OrgUnitClassificationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | OrgClassificationPEOClassificationCode | — |
