---
id: DOC-HCM-303
doc_type: system-doc
title: "HWM_GRP_INCL_MEMBERS_VIEW — Membros Incluídos no Grupo (View)"
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
  - group-members
  - view
  - inclusao-manual
aliases:
  - HWM_GRP_INCL_MEMBERS_VIEW
  - hwm_grp_incl_members_view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRP_INCL_MEMBERS_VIEW

## 📌 Visão Geral

View que exibe os membros explicitamente incluídos em grupos de workforce. Diferente dos membros dinâmicos baseados em critérios, estes são adicionados manualmente ao grupo.

> [!note] Sufixo _VIEW
> O sufixo `_VIEW` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de grupos de workforce:** Organização de trabalhadores em grupos para planejamento e alocação de recursos.
- **Planejamento de força de trabalho:** Base para análises de capacidade e distribuição de equipes.
- **Relatórios gerenciais:** Consolidação de dados por grupo para dashboards de workforce.
- **Integração com módulos:** Compartilhamento de definições de grupo com Payroll, Time Management e Project Costing.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo | — | 🟡 75% |
| 4 | CODE | VARCHAR2(30) | NULL | Classificação | Código identificador | — | 🟡 70% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 70% |
| 6 | START_DATE | DATE | NULL | Período | Data de início | — | 🟡 75% |
| 7 | END_DATE | DATE | NULL | Período | Data de fim | — | 🟡 75% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data/hora de criação | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_grps_vl]] — via `GRP_ID` (grupo de workforce)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa/trabalhador)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.*
FROM   HWM_GRP_INCL_MEMBERS_VIEW t
WHERE  ROWNUM <= 100
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Workforce Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[groupinclmemberspvo|GroupInclMembersPVO]] (GL · BICC: 8/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| GRP_ID | GrpId | ✅ |
| GRP_INCL_MEMBER_ID | GrpInclMemberId | ✅ |
| INCL_FLAG | InclFlag | — |
| INCL_MEMBER_ID | InclMemberId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |

### [[labordemandpvo|LaborDemandPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| GRP_ID | GrpId | — |
| GRP_INCL_MEMBER_ID | GrpInclMemberId | — |
| INCL_MEMBER_ID | InclMemberId | — |

---

## 📚 Referências

- [Oracle Docs — HWM_GRP_INCL_MEMBERS_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_grp_incl_members_view.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
