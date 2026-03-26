---
id: DOC-HCM-284
doc_type: system-doc
title: "HR_ORG_UNIT_CLASSIFICATIONS_F — Classificacoes de Unidade Organizacional (Date-Effective)"
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
  - org-unit-classifications
  - estrutura
  - core-hr
aliases:
  - HR_ORG_UNIT_CLASSIFICATIONS_F
  - hr_org_unit_classifications_f
  - hr-org-unit-classifications-f
  - org-unit-classifications
  - classificacoes-unidade-org
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ORG_UNIT_CLASSIFICATIONS_F

## 📌 Visao Geral

Armazena as **classificacoes de unidades organizacionais** com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Classificacao temporal:** Classificacoes com datas de vigencia.
- **Historico:** Rastrear quando uma organizacao ganhou/perdeu uma classificacao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_UNIT_CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador da classificacao | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 95% |
| 4 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Organizacao | [[hr_all_organization_units_f]] | 🟢 100% |
| 5 | CLASSIFICATION_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Codigo da classificacao | — | 🟢 95% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificacao | Status (ACTIVE, INACTIVE) | — | 🟢 90% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao da classificacao de unidade)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Classificacoes ativas
```sql
SELECT ouc.CLASSIFICATION_CODE, ouc.STATUS
FROM   HR_ORG_UNIT_CLASSIFICATIONS_F ouc
WHERE  ouc.ORGANIZATION_ID = :p_org_id
  AND  ouc.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN ouc.EFFECTIVE_START_DATE AND ouc.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- Permite rastrear historicamente quando classificacoes foram ativadas/desativadas.

---

## 📚 Referencias

- [Oracle Docs — HR_ORG_UNIT_CLASSIFICATIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrorgunitclassificationsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
