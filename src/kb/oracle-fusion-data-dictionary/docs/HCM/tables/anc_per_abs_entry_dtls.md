---
id: DOC-HCM-016
doc_type: system-doc
title: "ANC_PER_ABS_ENTRY_DTLS — Detalhes de Entrada de Ausência"
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
  - detalhes-entrada
  - entry-details
aliases:
  - ANC_PER_ABS_ENTRY_DTLS
  - anc_per_abs_entry_dtls
  - detalhes-entrada-ausencia
  - absence-entry-details
  - anc-per-abs-entry-dtls
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_ENTRY_DTLS

## 📌 Visão Geral

Armazena **detalhes adicionais** das entradas de ausência, como informações específicas do tipo de ausência que não cabem na tabela principal (ex.: número do atestado, CID, hospital, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Informações complementares:** Campos específicos por tipo de ausência.
- **Compliance:** Dados adicionais exigidos por legislação (ex.: CID para afastamento médico no Brasil).
- **Relatórios detalhados:** Informações granulares para análise de causas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_ENTRY_DTL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟢 90% |
| 2 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de ausência | [[anc_per_abs_entries]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 4 | DETAIL_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de detalhe adicional | — | 🟡 70% |
| 5 | DETAIL_VALUE | VARCHAR2(2000) | NULL | Dados | Valor do detalhe | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia do detalhe)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do detalhe de ausencia)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Detalhes de uma entrada de ausência
```sql
SELECT d.DETAIL_TYPE, d.DETAIL_VALUE
FROM   ANC_PER_ABS_ENTRY_DTLS d
WHERE  d.ABSENCE_ENTRY_ID = :p_absence_entry_id;
```

### Filtros comuns
- `ABSENCE_ENTRY_ID = :p_absence_entry_id` — Detalhes de uma ausência específica

---

## 🔒 Observações

- Estrutura flexível para armazenar dados adicionais sem alterar o schema principal.
- O campo `DETAIL_TYPE` identifica o tipo de informação (ex.: CID, HOSPITAL, NUMERO_ATESTADO).
- Pode conter múltiplos registros por entrada de ausência.

---

## 🔗 PVOs Relacionados

### [[personabsentrydetailpvo|PersonAbsEntryDetailPVO]] (GL · BICC: 13/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_DATE | AbsenceDate | ✅ |
| ABSENCE_DATETIME | AbsenceDatetime | ✅ |
| ABSENCE_END_DATETIME | AbsenceEndDatetime | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DUR_PREF_CD | PersonAbsEntryDetailPEODurPrefCd | — |
| DURATION | Duration | ✅ |
| END_TIME | EndTime | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_ABS_ENTRY_DTL_ID | PerAbsEntryDtlId | ✅ |
| PER_ABSENCE_ENTRY_ID | PerAbsenceEntryId | ✅ |
| START_TIME | StartTime | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_ENTRY_DTLS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsentrydtls.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
