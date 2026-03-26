---
id: DOC-HCM-274
doc_type: system-doc
title: "HR_ALL_POSITIONS_F — Posicoes"
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
  - positions
  - workforce
  - core-hr
aliases:
  - HR_ALL_POSITIONS_F
  - hr_all_positions_f
  - hr-all-positions-f
  - all-positions
  - posicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ALL_POSITIONS_F

## 📌 Visao Geral

Tabela principal que armazena todas as **posicoes** (positions) da organizacao com versionamento date-effective. Uma posicao representa um lugar especifico dentro de uma organizacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Workforce Planning:** Gerenciar posicoes e headcount.
- **Recrutamento:** Posicoes abertas geram requisicoes.
- **Orcamento:** Controlar custos por posicao.
- **Hierarquia:** Posicoes formam a hierarquia de reporte.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POSITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da posicao | — | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 100% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 100% |
| 4 | BUSINESS_UNIT_ID | NUMBER(18) | NOT NULL | FK | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 5 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento | [[hr_all_organization_units_f]] | 🟢 95% |
| 6 | JOB_ID | NUMBER(18) | NULL | FK | Job (cargo generico) associado | — | 🟢 90% |
| 7 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao | — | 🟢 90% |
| 8 | MAX_HEAD_COUNT | NUMBER | NULL | Dados | Headcount maximo (FTE) | — | 🟢 90% |
| 9 | STATUS | VARCHAR2(30) | NOT NULL | Classificacao | Status da posicao | — | 🟢 95% |
| 10 | POSITION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de posicao (SINGLE, SHARED, POOLED) | — | 🟢 90% |
| 11 | MANAGER_POSITION_ID | NUMBER(18) | NULL | FK | Posicao do gestor (hierarquia) | [[hr_all_positions_f]] | 🟢 90% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `MANAGER_POSITION_ID` (auto-referencia)

### Tabelas-filha (FK de saida)
- [[hr_all_positions_f_tl]] — via `POSITION_ID` (traducoes multilingue do registro)
- [[hrt_profiles_b]] — via `POSITION_ID` (perfil de talento da posicao)

---

## 📎 Uso Tipico

### Posicoes ativas
```sql
SELECT p.POSITION_ID, p.DEPARTMENT_ID, p.JOB_ID,
       p.MAX_HEAD_COUNT, p.STATUS
FROM   HR_ALL_POSITIONS_F p
WHERE  p.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN p.EFFECTIVE_START_DATE AND p.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective — PK (POSITION_ID, EFFECTIVE_START_DATE).
- MANAGER_POSITION_ID cria hierarquia de reporte posicional.
- MAX_HEAD_COUNT controla quantos colaboradores podem ocupar a posicao.

---

## 📚 Referencias

- [Oracle Docs — HR_ALL_POSITIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrallpositionsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
