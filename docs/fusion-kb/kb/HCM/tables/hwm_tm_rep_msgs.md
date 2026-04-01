---
id: DOC-HCM-391
doc_type: system-doc
title: "HWM_TM_REP_MSGS — Mensagens de Entradas Reportadas de Tempo"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-management
  - reported-messages
  - mensagens-reportadas
aliases:
  - HWM_TM_REP_MSGS
  - hwm_tm_rep_msgs
  - hwm-tm-rep-msgs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_MSGS

## 📌 Visao Geral

Armazena as **mensagens associadas a entradas reportadas** de tempo. Contém mensagens de validação, erros, warnings e informações geradas durante o processamento de entradas reportadas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreamento de erros:** registra mensagens de erro durante processamento de tempo.
- **Validação:** armazena resultados de validações aplicadas às entradas.
- **Troubleshooting:** facilita diagnóstico de problemas no processamento de time entries.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_MSG_ID | NUMBER(18) | NOT NULL | PK | Identificador único da mensagem | — | 🟡 70% |
| 2 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada associada | — | 🟡 70% |
| 3 | MESSAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da mensagem (ERROR, WARNING, INFO) | — | 🟡 65% |
| 4 | MESSAGE_CODE | VARCHAR2(80) | NULL | Identificação | Código da mensagem | — | 🟡 60% |
| 5 | MESSAGE_TEXT | VARCHAR2(2000) | NULL | Dados | Texto da mensagem | — | 🟡 65% |
| 6 | MESSAGE_SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade da mensagem | — | 🟡 55% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Mensagens de erro de entradas reportadas
```sql
SELECT m.MESSAGE_TYPE, m.MESSAGE_CODE, m.MESSAGE_TEXT
FROM   HWM_TM_REP_MSGS m
WHERE  m.REP_ENTRY_ID = :p_rep_entry_id
  AND  m.MESSAGE_TYPE = 'ERROR';
```

### Filtros comuns
- `REP_ENTRY_ID = :p_entry_id — Por entrada reportada`
- `MESSAGE_TYPE = 'ERROR' — Apenas erros`

---

## 🔒 Observacoes

- Utilizada para diagnóstico de problemas no processamento de time entries.
- Mensagens do tipo ERROR geralmente impedem o processamento da entrada no payroll.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_REP_MSGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepmsgs.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[compliancemessagepvo|ComplianceMessagePVO]] (HCM · BICC: 11/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | TimeRepositoryMessagePEOApplicationId | — |
| APPLICATION_SHORT_NAME | TimeRepositoryMessagePEOApplicationShortName | ✅ |
| CREATED_BY | TimeRepositoryMessagePEOCreatedBy | ✅ |
| CREATION_DATE | TimeRepositoryMessagePEOCreationDate | ✅ |
| DATE_FROM | TimeRepositoryMessagePEODateFrom | ✅ |
| DATE_TO | TimeRepositoryMessagePEODateTo | ✅ |
| ENTERPRISE_ID | TimeRepositoryMessagePEOEnterpriseId | — |
| LAST_UPDATE_DATE | TimeRepositoryMessagePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeRepositoryMessagePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TimeRepositoryMessagePEOLastUpdatedBy | ✅ |
| MESSAGE_FIELD | TimeRepositoryMessagePEOMessageField | — |
| MESSAGE_LEVEL | TimeRepositoryMessagePEOMessageLevel | ✅ |
| MESSAGE_NAME | TimeRepositoryMessagePEOMessageName | ✅ |
| OBJECT_VERSION_NUMBER | TimeRepositoryMessagePEOObjectVersionNumber | — |
| TM_EVENT_ID | TimeRepositoryMessagePEOTimeEventId | — |
| TM_REC_GRP_ID | TimeRepositoryMessagePEOTimeRecordGroupId | — |
| TM_REC_GRP_VERSION | TimeRepositoryMessagePEOTimeRecordGroupVersion | — |
| TM_REC_ID | TimeRepositoryMessagePEOTimeRecordId | — |
| TM_REC_VERSION | TimeRepositoryMessagePEOTimeRecordVersion | — |
| TM_REP_ATRB_USAGE_ID | TimeRepositoryMessagePEOTimeRepositoryAttributeUsageId | — |
| TM_REP_MSGS_ID | TimeRepositoryMessageId | ✅ |
| TRN_ID | TimeRepositoryMessagePEOTransactionId | — |
