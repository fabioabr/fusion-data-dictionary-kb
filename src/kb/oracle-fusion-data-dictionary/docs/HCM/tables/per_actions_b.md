---
id: DOC-HCM-610
doc_type: system-doc
title: "PER_ACTIONS_B — Ações de RH (Base)"
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
  - workforce-management
  - acoes-rh
  - hr-actions
aliases:
  - PER_ACTIONS_B
  - per_actions_b
  - per-actions-b
  - ações-de-rh-(base)
  - per-actions-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTIONS_B

## 📌 Visão Geral

Armazena a definição das **ações de RH** disponíveis no sistema. Ações representam eventos do ciclo de vida do colaborador (admissão, promoção, transferência, desligamento, etc.).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão do ciclo de vida** — define cada tipo de ação (HIRE, PROMOTION, TRANSFER, TERMINATION).
- **Workflow de aprovação** — ações podem ter fluxos de aprovação distintos.
- **Auditoria** — rastreabilidade completa de todas as ações realizadas.
- **Compliance** — controle de ações requeridas por legislação.
- **Integração com payroll** — ações podem disparar recálculos de folha.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ação | — | 🟢 95% |
| 2 | ACTION_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ação associado | PER_ACTION_TYPES_B | 🟢 90% |
| 3 | ACTION_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da ação (HIRE, PROMOTION, etc.) | — | 🟢 90% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócio | — | 🟢 85% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Status | Se a ação está habilitada (Y/N) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_action_types_b]] — via `ACTION_TYPE_ID` (tipo da ação de RH)

### Tabelas-filha (FK de saída)
- [[per_actions_tl]] — via `ACTION_ID` (traduções da ação de RH)
- [[per_action_occurrences]] — via `ACTION_ID` (ocorrências da ação)
- [[per_action_reason_usages]] — via `ACTION_ID` (motivos associados)

---

## 📎 Uso Típico

### Ações habilitadas
```sql
SELECT pa.ACTION_ID, pa.ACTION_CODE, pa.ENABLED_FLAG
FROM   PER_ACTIONS_B pa
WHERE  pa.ENABLED_FLAG = 'Y'
ORDER BY pa.ACTION_CODE;
```

### Filtros comuns
- `ACTION_CODE = 'HIRE'` — Ação de admissão
- `ENABLED_FLAG = 'Y'` — Ações habilitadas
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Cada ação está associada a um tipo de ação (PER_ACTION_TYPES_B).
- Ações são a base para todas as movimentações do ciclo de vida do colaborador.
---

## 🔗 PVOs Relacionados

### [[actionoccurrencespvo|ActionOccurrencesPVO]] (GL · BICC: 1/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACT_INFORMATION1 | ActionsPEOActInformation1 | — |
| ACT_INFORMATION2 | ActionsPEOActInformation2 | — |
| ACTION_CODE | ActionsPEOActionCode | — |
| ACTION_ID | ActionsPEOActionId | — |
| ACTION_TYPE_CODE | ActionsPEOActionTypeCode | — |
| ACTION_TYPE_ID | ActionsPEOActionTypeId | — |
| BUSINESS_GROUP_ID | ActionsPEOBusinessGroupId | — |
| CREATED_BY | ActionsPEOCreatedBy | — |
| CREATION_DATE | ActionsPEOCreationDate | — |
| END_DATE | ActionsPEOEndDate | — |
| LAST_UPDATE_DATE | ActionsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionsPEOLastUpdatedBy | — |
| MODULE_ID | ActionsPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ActionsPEOObjectVersionNumber | — |
| START_DATE | ActionsPEOStartDate | — |

### [[actionspvo|ActionsPVO]] (GL · BICC: 18/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACT_INFORMATION1 | ActionsPEOActInformation1 | ✅ |
| ACT_INFORMATION2 | ActionsPEOActInformation2 | ✅ |
| ACTION_CODE | ActionsPEOActionCode | ✅ |
| ACTION_ID | ActionId | ✅ |
| ACTION_TYPE_CODE | ActionsPEOActionTypeCode | ✅ |
| ACTION_TYPE_ID | ActionsPEOActionTypeId | ✅ |
| ALL_ROLES | ActionsPEOAllRoles | ✅ |
| BUSINESS_GROUP_ID | ActionsPEOBusinessGroupId | ✅ |
| COUNTRY | ActionsPEOCountry | ✅ |
| CREATED_BY | ActionsPEOCreatedBy | ✅ |
| CREATION_DATE | ActionsPEOCreationDate | ✅ |
| DFLT_ASG_STATUS_TYPE_ID | ActionsPEODfltAsgStatusTypeId | ✅ |
| END_DATE | ActionsPEOEndDate | ✅ |
| IS_SYSTEM_ACTION | ActionsPEOIsSystemAction | ✅ |
| LAST_UPDATE_DATE | ActionsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionsPEOLastUpdatedBy | ✅ |
| MODULE_ID | ActionsPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ActionsPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | ActionsPEOSeedDataSource | — |
| SGUID | ActionsPEOSguid | — |
| START_DATE | ActionsPEOStartDate | ✅ |
| USED_IN_CONTRACT | ActionsPEOUsedInContract | ✅ |

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionsPEOActionCode | — |
| ACTION_ID | ActionsPEOActionId | — |
| ACTION_TYPE_CODE | ActionsPEOActionTypeCode | — |
| ACTION_TYPE_ID | ActionsPEOActionTypeId | — |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionsPEOActionCode | — |
| ACTION_ID | ActionsPEOActionId | — |
| ACTION_TYPE_CODE | ActionsPEOActionTypeCode | — |
| ACTION_TYPE_ID | ActionsPEOActionTypeId | — |

### [[contractpvo|ContractPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionsPEOActionCode | ✅ |
| ACTION_ID | ActionsPEOActionId | — |
| BUSINESS_GROUP_ID | ActionsPEOBusinessGroupId | — |

### [[contractpvoviewall|ContractPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionsPEOActionCode | — |
| ACTION_ID | ActionsPEOActionId | — |
| BUSINESS_GROUP_ID | ActionsPEOBusinessGroupId | — |

### [[gradeladderpvo|GradeLadderPVO]] (GL · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ProgressionActionsPEOActionId | — |
| LAST_UPDATE_DATE | ProgressionActionsPEOLastUpdateDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ACTIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
