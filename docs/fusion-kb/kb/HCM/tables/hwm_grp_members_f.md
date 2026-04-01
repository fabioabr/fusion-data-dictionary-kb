---
id: DOC-HCM-305
doc_type: system-doc
title: "HWM_GRP_MEMBERS_F — Membros de Grupo de Workforce"
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
  - date-effective
aliases:
  - HWM_GRP_MEMBERS_F
  - hwm_grp_members_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRP_MEMBERS_F

## 📌 Visão Geral

Tabela date-effective que armazena a associação de trabalhadores como membros de grupos de workforce, com controle de vigência temporal para rastreamento histórico.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

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
| 1 | GRP_MEMBERS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo do registro | — | 🟡 80% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 75% |
| 6 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

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
FROM   HWM_GRP_MEMBERS_F t
WHERE  SYSDATE BETWEEN t.EFFECTIVE_START_DATE AND t.EFFECTIVE_END_DATE
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- Área funcional: Workforce Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[groupmemberspvo|GroupMembersPVO]] (GL · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GroupMembersDPEOCreatedBy | ✅ |
| CREATION_DATE | GroupMembersDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | GroupMembersDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | GroupMembersDPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | GroupMembersDPEOEnterpriseId | ✅ |
| GRP_EVAL_PROCESS_ID | GroupMembersDPEOGroupEvaluateProcessId | ✅ |
| GRP_ID | GroupMembersDPEOGroupId | ✅ |
| GRP_MEMBER_ID | GroupMembersDPEOGroupMemberId | ✅ |
| LAST_UPDATE_DATE | GroupMembersDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupMembersDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupMembersDPEOLastUpdatedBy | ✅ |
| MEMBER_ID | GroupMembersDPEOMemberId | ✅ |
| OBJECT_VERSION_NUMBER | GroupMembersDPEOObjectVersionNumber | ✅ |
| REMARKS | GroupMembersDPEORemarks | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_GRP_MEMBERS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_grp_members_f.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
