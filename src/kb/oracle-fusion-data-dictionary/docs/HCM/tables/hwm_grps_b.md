---
id: DOC-HCM-299
doc_type: system-doc
title: "HWM_GRPS_B — Grupos de Workforce Management — Base"
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
  - groups
  - workforce-management
  - configuracao
aliases:
  - HWM_GRPS_B
  - hwm_grps_b
  - hwm-grps-b
  - wfm-groups-base
  - grupos-workforce-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRPS_B

## 📌 Visao Geral

Tabela base que define os **grupos** do modulo Workforce Management. Grupos organizam colaboradores, regras ou configuracoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Agrupamento:** Organizar colaboradores em grupos de workforce.
- **Configuracao:** Associar regras e politicas a grupos.
- **Scheduling:** Agrupar trabalhadores para escalas de trabalho.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRP_ID | NUMBER(18) | NOT NULL | PK | Identificador do grupo | — | 🟢 90% |
| 2 | GRP_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do grupo | — | 🟢 85% |
| 3 | GRP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do grupo | — | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inicio | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim | — | 🟢 85% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hwm_grps_tl]] — via `GRP_ID` (traducoes do grupo de trabalho)

---

## 📎 Uso Tipico

### Grupos ativos
```sql
SELECT g.GRP_ID, g.GRP_CODE, g.GRP_TYPE, g.STATUS
FROM   HWM_GRPS_B g
WHERE  g.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN NVL(g.DATE_FROM, SYSDATE) AND NVL(g.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hwm_grps_tl]].
- Grupos sao usados para organizar recursos de workforce management.

---

## 📚 Referencias

- [Oracle Docs — HWM_GRPS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmgrpsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[groupmemberspvo|GroupMembersPVO]] (GL · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPL_USG_CD | GroupsPEOApplicationUsageCd | ✅ |
| APPLIES_TO_CD | GroupsPEOAppliesToCd | ✅ |
| ASSIGNMENT_TO_USE_CD | GroupsPEOAssignmentToUseCd | ✅ |
| CREATED_BY | GroupsPEOCreatedBy | ✅ |
| CREATION_DATE | GroupsPEOCreationDate | ✅ |
| ENTERPRISE_ID | GroupsPEOEnterpriseId | ✅ |
| EVAL_STATUS_CD | GroupsPEOEvaluateStatusCd | ✅ |
| FREEZE_FLAG | GroupsPEOFreezeFlag | ✅ |
| GRP_CODE | GroupsPEOGroupCode | ✅ |
| GRP_ID | GroupsPEOGroupId | ✅ |
| LAST_REFRESH_DT | GroupsPEOLastRefreshDate | ✅ |
| LAST_UPDATE_DATE | GroupsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupsPEOLastUpdatedBy | ✅ |
| MASS_EVAL_FLAG | GroupsPEOMassEvalFlag | ✅ |
| MEM_TYPE_CD | GroupsPEOMemTypeCd | ✅ |
| MODULE_ID | GroupsPEOModuleId | ✅ |
| NEXT_REFRESH_DT | GroupsPEONextRefreshDate | ✅ |
| NUM_DAYS_NEXT | GroupsPEONumberDaysNext | ✅ |
| NUM_DAYS_PREV | GroupsPEONumberDaysPrev | ✅ |
| OBJECT_VERSION_NUMBER | GroupsPEOObjectVersionNumber | ✅ |
| ONLINE_EVAL_FLAG | GroupsPEOOnlineEvaluateFlag | ✅ |
| RUN_TYPE | GroupsPEORunType | ✅ |

### [[groupspvo|GroupsPVO]] (GL · BICC: 23/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPL_USG_CD | GroupsPEOApplUsgCd | ✅ |
| APPLIES_TO_CD | GroupsPEOAppliesToCd | ✅ |
| ASSIGNMENT_TO_USE_CD | GroupsPEOAssignmentToUseCd | ✅ |
| CREATED_BY | GroupsPEOCreatedBy | ✅ |
| CREATION_DATE | GroupsPEOCreationDate | ✅ |
| ENTERPRISE_ID | GroupsPEOEnterpriseId | ✅ |
| EVAL_STATUS_CD | GroupsPEOEvalStatusCd | ✅ |
| FREEZE_FLAG | GroupsPEOFreezeFlag | ✅ |
| GRP_CODE | GroupsPEOGroupCode | ✅ |
| GRP_ID | GroupsPEOGroupId | ✅ |
| LAST_REFRESH_DT | GroupsPEOLastRefreshDt | ✅ |
| LAST_UPDATE_DATE | GroupsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupsPEOLastUpdatedBy | ✅ |
| MASS_EVAL_FLAG | GroupsPEOMassEvalFlag | ✅ |
| MEM_TYPE_CD | GroupsPEOMemTypeCd | ✅ |
| MODULE_ID | GroupsPEOModuleId | ✅ |
| NEXT_REFRESH_DT | GroupsPEONextRefreshDt | ✅ |
| NUM_DAYS_NEXT | GroupsPEONumberDaysNext | ✅ |
| NUM_DAYS_PREV | GroupsPEONumberDaysPrev | ✅ |
| OBJECT_VERSION_NUMBER | GroupsPEOObjectVersionNumber | ✅ |
| ONLINE_EVAL_FLAG | GroupsPEOOnlineEvaluateFlag | ✅ |
| RUN_TYPE | GroupsPEORunType | ✅ |
