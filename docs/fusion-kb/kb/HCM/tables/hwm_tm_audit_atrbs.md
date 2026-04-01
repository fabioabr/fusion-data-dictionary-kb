---
id: DOC-HCM-362
doc_type: system-doc
title: "HWM_TM_AUDIT_ATRBS — Atributos de Auditoria de Time Management"
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
  - atributos
  - detalhes
aliases:
  - HWM_TM_AUDIT_ATRBS
  - hwm_tm_audit_atrbs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_AUDIT_ATRBS

## 📌 Visão Geral

Armazena os atributos detalhados de cada registro de auditoria de Time Management, incluindo valores anteriores e posteriores das alterações rastreadas.

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
| 1 | AUDIT_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador do atributo de auditoria | — | 🟡 80% |
| 2 | AUDIT_ID | NUMBER(18) | NOT NULL | FK | Referência ao registro de auditoria | HWM_TM_AUDITS | 🟡 80% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(240) | NULL | Identificação | Nome do atributo alterado | — | 🟡 75% |
| 4 | OLD_VALUE | VARCHAR2(2000) | NULL | Dados | Valor anterior à alteração | — | 🟡 70% |
| 5 | NEW_VALUE | VARCHAR2(2000) | NULL | Dados | Novo valor após a alteração | — | 🟡 70% |
| 6 | CHANGE_DATE | TIMESTAMP | NULL | Auditoria | Data/hora da alteração | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_audits]] — via `AUDIT_ID` (registro de auditoria)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT a.AUDIT_ID, a.ATTRIBUTE_NAME, a.OLD_VALUE, a.NEW_VALUE
FROM   HWM_TM_AUDIT_ATRBS a
JOIN   HWM_TM_AUDITS aud ON a.AUDIT_ID = aud.AUDIT_ID
WHERE  a.CHANGE_DATE >= TRUNC(SYSDATE) - 30
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Registros de auditoria são gerados automaticamente pelo sistema e não devem ser alterados manualmente.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[changeauditattributepvo|ChangeAuditAttributePVO]] (HCM · BICC: 17/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_TYPE | ChangeAuditAttributePEOActionType | ✅ |
| CREATED_BY | ChangeAuditAttributePEOCreatedBy | ✅ |
| CREATION_DATE | ChangeAuditAttributePEOCreationDate | ✅ |
| ENTERPRISE_ID | ChangeAuditAttributePEOEnterpriseId | — |
| LAST_UPDATE_DATE | ChangeAuditAttributePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ChangeAuditAttributePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ChangeAuditAttributePEOLastUpdatedBy | ✅ |
| NEW_DATE | ChangeAuditAttributePEONewDate | ✅ |
| NEW_GMT_OFFSET | ChangeAuditAttributePEONewGmtOffset | — |
| NEW_NUMBER | ChangeAuditAttributePEONewNumber | ✅ |
| NEW_TIMESTAMP | ChangeAuditAttributePEONewTimestamp | ✅ |
| NEW_TIMEZONE_CODE | ChangeAuditAttributePEONewTimezoneCode | — |
| NEW_VARCHAR | ChangeAuditAttributePEONewVarchar | ✅ |
| NEW_ZONE_TYPE | ChangeAuditAttributePEONewZoneType | — |
| OBJECT_VERSION_NUMBER | ChangeAuditAttributePEOObjectVersionNumber | — |
| OLD_DATE | ChangeAuditAttributePEOOldDate | ✅ |
| OLD_GMT_OFFSET | ChangeAuditAttributePEOOldGmtOffset | — |
| OLD_NUMBER | ChangeAuditAttributePEOOldNumber | ✅ |
| OLD_TIMESTAMP | ChangeAuditAttributePEOOldTimestamp | ✅ |
| OLD_TIMEZONE_CODE | ChangeAuditAttributePEOOldTimezoneCode | — |
| OLD_VARCHAR | ChangeAuditAttributePEOOldVarchar | ✅ |
| OLD_ZONE_TYPE | ChangeAuditAttributePEOOldZoneType | — |
| ORIG_AUDIT_ATRB_ID | ChangeAuditAttributePEOOrigAuditAtrbId | — |
| REASON_CODE | ChangeAuditAttributePEOReasonCode | ✅ |
| TM_ATRB_FLD_ID | ChangeAuditAttributePEOTmAtrbFldId | ✅ |
| TM_ATTRIBUTE_TYPE | ChangeAuditAttributePEOTmAttributeType | — |
| TM_AUDIT_ATRB_ID | ChangeAuditAttributePEOTmAuditAtrbId | ✅ |
| TM_AUDIT_ID | ChangeAuditAttributePEOTmAuditId | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_AUDIT_ATRBS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_audit_atrbs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
