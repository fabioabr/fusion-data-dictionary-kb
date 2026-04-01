---
id: DOC-HCM-615
doc_type: system-doc
title: "PER_ACTION_REASON_USAGES — Uso de Motivos em Ações"
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
  - motivos-acoes
  - action-reason-usages
aliases:
  - PER_ACTION_REASON_USAGES
  - per_action_reason_usages
  - per-action-reason-usages
  - uso-de-motivos-em-ações
  - per-action-reason-us
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_REASON_USAGES

## 📌 Visão Geral

Armazena a **associação entre motivos e ações de RH**. Define quais motivos são válidos para cada ação, criando uma relação muitos-para-muitos entre ações e seus motivos permitidos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de elegibilidade** — define quais motivos são válidos para cada ação.
- **Validação de dados** — garante que apenas motivos válidos sejam selecionados.
- **Flexibilidade** — permite reutilizar motivos em múltiplas ações.
- **Governance** — controle centralizado das combinações ação-motivo permitidas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_REASON_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação | — | 🟢 90% |
| 2 | ACTION_ID | NUMBER(18) | NOT NULL | FK | Ação associada | PER_ACTIONS_B | 🟢 90% |
| 3 | ACTION_REASON_ID | NUMBER(18) | NOT NULL | FK | Motivo associado | PER_ACTION_REASONS_B | 🟢 90% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Status | Se a associação está ativa (Y/N) | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_actions_b]] — via `ACTION_ID` (ação de RH que usa o motivo)
- [[per_action_reasons_b]] — via `ACTION_REASON_ID` (motivo utilizado pela ação de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela de associação (junction table).

---

## 📎 Uso Típico

### Motivos válidos para uma ação
```sql
SELECT par.ACTION_REASON_CODE, tl.ACTION_REASON_NAME
FROM   PER_ACTION_REASON_USAGES paru
JOIN   PER_ACTION_REASONS_B par ON paru.ACTION_REASON_ID = par.ACTION_REASON_ID
JOIN   PER_ACTION_REASONS_TL tl ON par.ACTION_REASON_ID = tl.ACTION_REASON_ID AND tl.LANGUAGE = 'PTB'
WHERE  paru.ACTION_ID = :p_action_id
  AND  paru.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Associações ativas
---

## 🔒 Observações

- Tabela de associação (junction) — conecta PER_ACTIONS_B com PER_ACTION_REASONS_B.
- Permite que o mesmo motivo seja usado em múltiplas ações.
- A flag `ENABLED_FLAG` permite desativar associações sem excluí-las.
---

## 🔗 PVOs Relacionados

### [[actionreasonsusagespvo|ActionReasonsUsagesPVO]] (GL · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionReasonUsagesPEOActionCode | — |
| ACTION_ID | ActionReasonUsagesPEOActionId | ✅ |
| ACTION_REASON_CODE | ActionReasonUsagesPEOActionReasonCode | — |
| ACTION_REASON_ID | ActionReasonUsagesPEOActionReasonId | ✅ |
| ACTION_REASON_USAGE_ID | ActionReasonUsageId | ✅ |
| BUSINESS_GROUP_ID | ActionReasonUsagesPEOBusinessGroupId | — |
| CREATED_BY | ActionReasonUsagesPEOCreatedBy | — |
| CREATION_DATE | ActionReasonUsagesPEOCreationDate | — |
| END_DATE | ActionReasonUsagesPEOEndDate | — |
| LAST_UPDATE_DATE | ActionReasonUsagesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionReasonUsagesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionReasonUsagesPEOLastUpdatedBy | — |
| MODULE_ID | ActionReasonUsagesPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ActionReasonUsagesPEOObjectVersionNumber | — |
| START_DATE | ActionReasonUsagesPEOStartDate | — |

---

## 📚 Referências

- [Oracle Docs — PER_ACTION_REASON_USAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionreasonusages.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
