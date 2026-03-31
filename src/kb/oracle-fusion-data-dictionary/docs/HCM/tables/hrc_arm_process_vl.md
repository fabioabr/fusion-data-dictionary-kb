---
id: DOC-HCM-155
doc_type: system-doc
title: "HRC_ARM_PROCESS_VL — Processos ARM — Visão Traduzida"
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
  - transaction-console
  - arm
  - process
aliases:
  - HRC_ARM_PROCESS_VL
  - hrc_arm_process_vl
  - processos-armvisão-traduzida
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_ARM_PROCESS_VL

## 📌 Visão Geral

View traduzida dos **processos ARM (Approval Rules Manager)**. Consolida processos de aprovação com traduções. Sufixo `_VL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta de processos:** Visão consolidada de aprovações configuradas.
- **Interface:** Nomes e descrições traduzidos.
- **Relatórios:** Base para configuração de aprovações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROCESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do processo ARM | — | 🟢 90% |
| 2 | PROCESS_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do processo | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição traduzida | — | 🟡 80% |
| 4 | PROCESS_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código interno | — | 🟡 75% |
| 5 | MODULE_ID | VARCHAR2(30) | NULL | Classificação | Módulo ao qual pertence | — | 🟡 70% |
| 6 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas relacionadas

---

## 📎 Uso Típico

### Processos ARM ativos
```sql
SELECT p.PROCESS_ID, p.PROCESS_NAME, p.PROCESS_CODE
FROM   HRC_ARM_PROCESS_VL p
WHERE  p.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- View (sufixo `_VL`) — join automático entre base e traduções.
- Retorna dados no idioma da sessão.

---

## 🔗 PVOs Relacionados

### [[approvalprocessp1|ApprovalProcessP1]] (AP · BICC: 3/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE | ApprovalProcessPEOActive | — |
| ADDITIONAL_REST_RESOURCE | ApprovalProcessPEOAdditionalRestResource | — |
| BYPASS_SUPPORTED | ApprovalProcessPEOBypassSupported | — |
| CATEGORY_CODE | ApprovalProcessPEOCategoryCode | — |
| CATEGORY_NAME | ApprovalProcessPEOCategoryName | — |
| COMPOSITE_ID | ApprovalProcessPEOCompositeId | — |
| CREATED_BY | ApprovalProcessPEOCreatedBy | — |
| CREATION_DATE | ApprovalProcessPEOCreationDate | — |
| DESCRIPTION | ApprovalProcessPEODescription | — |
| ENTERPRISE_ID | ApprovalProcessPEOEnterpriseId | — |
| FAMILY | ApprovalProcessPEOFamily | — |
| IS_TXN_FRAMEWORK_PROCESS | ApprovalProcessPEOIsTxnFrameworkProcess | — |
| LAST_UPDATE_DATE | ApprovalProcessPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApprovalProcessPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApprovalProcessPEOLastUpdatedBy | — |
| MODULE_ID | ApprovalProcessPEOModuleId | — |
| NAME | ApprovalProcessPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ApprovalProcessPEOObjectVersionNumber | — |
| PROCESS_ID | ApprovalProcessPEOProcessId | ✅ |
| RESOURCE_CONTEXT_SHORT_NAME | ApprovalProcessPEOResourceContextShortName | — |
| REST_RESOURCE_KEY | ApprovalProcessPEORestResourceKey | — |
| RULE_FILE_NAME | ApprovalProcessPEORuleFileName | — |
| SUBCATEGORY_CODE | ApprovalProcessPEOSubcategoryCode | — |
| SUBCATEGORY_NAME | ApprovalProcessPEOSubcategoryName | — |
| TASK_FILE_NAME | ApprovalProcessPEOTaskFileName | ✅ |
| TXN_MODULE_IDENTIFIER | ApprovalProcessPEOTxnModuleIdentifier | — |

### [[transactionconsolep1|TransactionConsoleP1]] (AP · BICC: 2/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE | ApprovalProcessPEOActive | — |
| COMPOSITE_ID | ApprovalProcessPEOCompositeId | — |
| CREATED_BY | ApprovalProcessPEOCreatedBy3 | — |
| CREATION_DATE | ApprovalProcessPEOCreationDate4 | — |
| DESCRIPTION | ApprovalProcessPEODescription | — |
| ENTERPRISE_ID | ApprovalProcessPEOEnterpriseId | — |
| LAST_UPDATE_DATE | ApprovalProcessPEOLastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | ApprovalProcessPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | ApprovalProcessPEOLastUpdatedBy3 | — |
| MODULE_ID | ApprovalProcessPEOModuleId | — |
| NAME | ApprovalProcessPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ApprovalProcessPEOObjectVersionNumber2 | — |
| PROCESS_ID | ApprovalProcessPEOProcessId | — |
| RULE_FILE_NAME | ApprovalProcessPEORuleFileName | — |
| TASK_FILE_NAME | ApprovalProcessPEOTaskFileName | — |
| TXN_MODULE_IDENTIFIER | ApprovalProcessPEOTxnModuleIdentifier | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
