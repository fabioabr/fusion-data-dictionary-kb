---
id: DOC-HCM-013
doc_type: system-doc
title: "ANC_PER_ABS_CERTS — Certificados de Ausência por Pessoa"
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
  - absence-management
  - certificados
  - certificates
  - atestado
  - comprovante
aliases:
  - ANC_PER_ABS_CERTS
  - anc_per_abs_certs
  - certificados-ausencia
  - absence-certificates
  - anc-per-abs-certs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_CERTS

## 📌 Visão Geral

Armazena os **certificados/atestados fornecidos pelos colaboradores** para comprovar ausências. Cada registro vincula um documento comprobatório a uma entrada de ausência específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comprovação de ausência:** Registra o fornecimento de atestados médicos, declarações e outros comprovantes.
- **Compliance trabalhista:** Documenta a entrega de certificados exigidos pela legislação.
- **Auditoria:** Rastreabilidade completa de comprovantes por ausência.
- **Workflow de aprovação:** Status do certificado pode impactar a aprovação da ausência.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_CERT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do certificado | — | 🟢 90% |
| 2 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de ausência associada | [[anc_per_abs_entries]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 4 | CERTIFICATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de certificação fornecida | — | 🟡 75% |
| 5 | CERTIFICATION_STATUS | VARCHAR2(30) | NULL | Classificação | Status (SUBMITTED, APPROVED, REJECTED) | — | 🟡 75% |
| 6 | DATE_RECEIVED | DATE | NULL | Data | Data de recebimento do certificado | — | 🟡 75% |
| 7 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários sobre o certificado | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia do certificado)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do certificado de ausencia)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Certificados por ausência
```sql
SELECT pc.PER_ABS_CERT_ID, pc.CERTIFICATION_TYPE,
       pc.CERTIFICATION_STATUS, pc.DATE_RECEIVED
FROM   ANC_PER_ABS_CERTS pc
WHERE  pc.ABSENCE_ENTRY_ID = :p_absence_entry_id;
```

### Filtros comuns
- `CERTIFICATION_STATUS = 'APPROVED'` — Certificados aprovados
- `CERTIFICATION_STATUS = 'SUBMITTED'` — Certificados pendentes de revisão

---

## 🔒 Observações

- Vinculada a entradas de ausência específicas (`ANC_PER_ABS_ENTRIES`).
- O status do certificado pode impactar a aprovação ou rejeição da ausência.
- Documentos físicos ou digitais podem ser anexados via integração com UCM (Universal Content Management).

---

## 🔗 PVOs Relacionados

### [[personabscertificationspvo|PersonAbsCertificationsPVO]] (GL · BICC: 25/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_CERTIFICATION_ID | AbsenceCertificationId | — |
| ACCEPTED_BY | AcceptedBy | ✅ |
| ACCEPTED_DATE | AcceptedDate | ✅ |
| ACCEPTED_YN | AcceptedYn | ✅ |
| CASE_ID | PersonAbsCertificationsPEOCaseId | — |
| CERT_CREATION_DATE | CertCreationDate | ✅ |
| COMMENTS | Comments | ✅ |
| COMPLETE_YN | CompleteYn | ✅ |
| COMPLETED_DATE | CompletedDate | ✅ |
| CONFIRM_RSN_CD | ConfirmRsnCd | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CTFN_CREATION_MODE | CtfnCreationMode | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| EVIDENCE_SOURCE | EvidenceSource | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LATE_REASON | LateReason | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_ABSENCE_ENTRY_ID | PerAbsenceEntryId | — |
| PER_CERT_ID | PerCertId | ✅ |
| RECEIVED_DATE | ReceivedDate | ✅ |
| RECEIVED_LATE_YN | ReceivedLateYn | ✅ |
| RECEIVED_YN | ReceivedYn | ✅ |
| REQUIRED_BY_DATE | RequiredByDate | ✅ |
| REV_PAY_END_DT | RevPayEndDt | ✅ |
| REV_PAY_PCT | RevPayPct | ✅ |
| REV_PAY_START_DT | RevPayStartDt | ✅ |
| STATUS | Status | ✅ |
| TARGET_PLAN_ID | TargetPlanId | ✅ |
| VALID_UPTO_DATE | ValidUptoDate | ✅ |
| VOID_RSN_CD | VoidRsnCd | ✅ |
| VOID_YN | VoidYn | ✅ |
| VOIDED_DATE | VoidedDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_CERTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabscerts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
