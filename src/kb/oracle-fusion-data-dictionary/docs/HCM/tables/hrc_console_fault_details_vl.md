---
id: DOC-HCM-156
doc_type: system-doc
title: "HRC_CONSOLE_FAULT_DETAILS_VL — Detalhes de Falhas do Console — Visão Traduzida"
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
  - fault
  - details
aliases:
  - HRC_CONSOLE_FAULT_DETAILS_VL
  - hrc_console_fault_details_vl
  - detalhes-de-falhas-do-consolevisão-traduzida
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_CONSOLE_FAULT_DETAILS_VL

## 📌 Visão Geral

View traduzida com **detalhes de falhas** do console de transações HCM. Erros durante processamento de transações de RH.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Diagnóstico de erros:** Detalha falhas em transações HCM.
- **Suporte técnico:** Informações para resolução.
- **Monitoramento:** Acompanhamento de transações com erro.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FAULT_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | CONSOLE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada do console | [[hrc_txn_console_entry]] | 🟢 85% |
| 3 | FAULT_CODE | VARCHAR2(240) | NULL | Classificação | Código da falha | — | 🟡 75% |
| 4 | FAULT_MESSAGE | VARCHAR2(4000) | NULL | Descrição | Mensagem de erro traduzida | — | 🟡 75% |
| 5 | FAULT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (SYSTEM, BUSINESS, VALIDATION) | — | 🟡 70% |
| 6 | FAULT_TIMESTAMP | TIMESTAMP | NULL | Data | Data/hora da ocorrência | — | 🟡 75% |
| 7 | STACK_TRACE | CLOB | NULL | Técnico | Rastreamento de pilha | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_console_entry]] — via `CONSOLE_ENTRY_ID` (entrada de console do detalhe de falha)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Falhas recentes
```sql
SELECT f.FAULT_CODE, f.FAULT_MESSAGE, f.FAULT_TYPE, f.FAULT_TIMESTAMP
FROM   HRC_CONSOLE_FAULT_DETAILS_VL f
WHERE  f.CREATION_DATE >= SYSDATE - 7
ORDER BY f.FAULT_TIMESTAMP DESC;
```

---

## 🔒 Observações

- View traduzida (sufixo `_VL`).
- Falhas SYSTEM = infraestrutura; BUSINESS = regras violadas.
- `STACK_TRACE` útil para diagnóstico avançado.

---

## 🔗 PVOs Relacionados

### [[consoleissuefaultdetailsp1|ConsoleIssueFaultDetailsP1]] (AP · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ConsoleIssueFaultDetailsPEOCreatedBy | — |
| CREATION_DATE | ConsoleIssueFaultDetailsPEOCreationDate | — |
| DESCRIPTION | ConsoleIssueFaultDetailsPEODescription | ✅ |
| ENTERPRISE_ID | ConsoleIssueFaultDetailsPEOEnterpriseId | — |
| ERROR_CODE | ConsoleIssueFaultDetailsPEOErrorCode | — |
| FAULT_CODE | ConsoleIssueFaultDetailsPEOFaultCode | — |
| FAULT_DETAILS_ID | ConsoleIssueFaultDetailsPEOFaultDetailsId | ✅ |
| ISSUE_TITLE | ConsoleIssueFaultDetailsPEOIssueTitle | ✅ |
| ISSUE_TYPE | ConsoleIssueFaultDetailsPEOIssueType | ✅ |
| ISSUE_TYPE_CODE | ConsoleIssueFaultDetailsPEOIssueTypeCode | — |
| LAST_UPDATE_DATE | ConsoleIssueFaultDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ConsoleIssueFaultDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ConsoleIssueFaultDetailsPEOLastUpdatedBy | — |
| MODULE_ID | ConsoleIssueFaultDetailsPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ConsoleIssueFaultDetailsPEOObjectVersionNumber | — |
| RESOLUTION | ConsoleIssueFaultDetailsPEOResolution | ✅ |
| SGUID | ConsoleIssueFaultDetailsPEOSguid | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
