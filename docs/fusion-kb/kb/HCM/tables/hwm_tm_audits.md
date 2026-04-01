---
id: DOC-HCM-361
doc_type: system-doc
title: "HWM_TM_AUDITS — Auditorias de Time Management"
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
  - time-management
  - auditoria
  - compliance
aliases:
  - HWM_TM_AUDITS
  - hwm_tm_audits
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_AUDITS

## 📌 Visão Geral

Armazena registros de auditoria do módulo de Time Management, rastreando alterações em cartões de ponto, aprovações e ajustes para fins de compliance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de time management:** Rastreamento completo de alterações em registros de tempo para compliance.
- **Conformidade regulatória:** Atendimento a requisitos legais de registro de jornada.
- **Investigação de discrepâncias:** Base para análise de alterações suspeitas ou incorretas.
- **Relatórios de auditoria:** Geração de trilhas de auditoria para revisão gerencial.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | AUDIT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de auditoria | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | AUDIT_ACTION | VARCHAR2(30) | NULL | Classificação | Ação auditada (INSERT/UPDATE/DELETE) | — | 🟡 75% |
| 4 | AUDIT_DATE | TIMESTAMP | NOT NULL | Dados | Data/hora da ação auditada | — | 🟡 80% |
| 5 | OLD_VALUE | VARCHAR2(2000) | NULL | Dados | Valor anterior à alteração | — | 🟡 70% |
| 6 | NEW_VALUE | VARCHAR2(2000) | NULL | Dados | Novo valor após a alteração | — | 🟡 70% |
| 7 | TABLE_NAME | VARCHAR2(30) | NULL | Referência | Tabela auditada | — | 🟡 70% |
| 8 | COLUMN_NAME | VARCHAR2(30) | NULL | Referência | Coluna auditada | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_tm_audit_atrbs]] — via `AUDIT_ID` (atributos de auditoria)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.AUDIT_ID, t.PERSON_ID, t.AUDIT_ACTION, t.AUDIT_DATE
FROM   HWM_TM_AUDITS t
WHERE  t.AUDIT_DATE >= TRUNC(SYSDATE) - 30
ORDER BY t.AUDIT_DATE DESC
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Registros de auditoria são gerados automaticamente pelo sistema e não devem ser alterados manualmente.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[changeauditattributepvo|ChangeAuditAttributePVO]] (HCM · BICC: 11/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_TYPE | ChangeAuditPEOActionType1 | ✅ |
| CREATED_BY | ChangeAuditPEOCreatedBy1 | ✅ |
| CREATION_DATE | ChangeAuditPEOCreationDate1 | ✅ |
| ENTERPRISE_ID | ChangeAuditPEOEnterpriseId1 | — |
| LAST_UPDATE_DATE | ChangeAuditPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | ChangeAuditPEOLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | ChangeAuditPEOLastUpdatedBy1 | ✅ |
| OBJECT_VERSION_NUMBER | ChangeAuditPEOObjectVersionNumber1 | — |
| ORIG_AUDIT_ID | ChangeAuditPEOOrigAuditId | — |
| REASON_CODE | ChangeAuditPEOReasonCode1 | ✅ |
| REF_DATE | ChangeAuditPEORefDate | ✅ |
| TM_AUDIT_ID | ChangeAuditPEOTmAuditId1 | ✅ |
| TM_BLK_ID | ChangeAuditPEOTmBlkId | ✅ |
| TM_BLK_VERSION | ChangeAuditPEOTmBlkVersion | — |
| TM_NEW_BLK_ID | ChangeAuditPEOTmNewBlkId | — |
| TM_NEW_BLK_VERSION | ChangeAuditPEOTmNewBlkVersion | — |
| TM_RECORD_GRP_ID | ChangeAuditPEOTmRecordGrpId | ✅ |
| USAGES_TYPE | ChangeAuditPEOUsagesType | — |

### [[changeauditpvo|ChangeAuditPVO]] (HCM · BICC: 11/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_TYPE | ActionType | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORIG_AUDIT_ID | OrigAuditId | — |
| REASON_CODE | ReasonCode | ✅ |
| REF_DATE | RefDate | ✅ |
| TM_AUDIT_ID | TmAuditId | ✅ |
| TM_BLK_ID | TmBlkId | ✅ |
| TM_BLK_VERSION | TmBlkVersion | — |
| TM_NEW_BLK_ID | TmNewBlkId | — |
| TM_NEW_BLK_VERSION | TmNewBlkVersion | — |
| TM_RECORD_GRP_ID | TmRecordGrpId | ✅ |
| USAGES_TYPE | UsagesType | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_AUDITS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_audits.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
