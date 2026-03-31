---
id: DOC-HCM-060
doc_type: system-doc
title: "BEN_PRTT_ENRT_CTFN_PRVDD — Certificações Fornecidas na Inscrição"
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
  - benefits
  - certificacoes-inscricao
  - enrollment-certifications
aliases:
  - BEN_PRTT_ENRT_CTFN_PRVDD
  - ben_prtt_enrt_ctfn_prvdd
  - certificacoes-inscricao-beneficios
  - enrollment-certifications
  - ben-prtt-enrt-ctfn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRTT_ENRT_CTFN_PRVDD

## 📌 Visão Geral

Armazena as **certificações/documentos fornecidos** durante o processo de inscrição de benefícios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comprovação:** Documenta certificações exigidas para inscrição.
- **Workflow:** Status de validação de documentos.
- **Compliance:** Atende requisitos de comprovação documental.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PRTT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de certificações fornecidas na inscrição
```sql
SELECT * FROM BEN_PRTT_ENRT_CTFN_PRVDD
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Certificações Fornecidas na Inscrição).

---

## 🔗 PVOs Relacionados

### [[participantcertificationpvo|ParticipantCertificationPVO]] (HCM · BICC: 10/56)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ParticipantCertificationPEOBusinessGroupId | — |
| CREATED_BY | ParticipantCertificationPEOCreatedBy | — |
| CREATION_DATE | ParticipantCertificationPEOCreationDate | — |
| CTFN_DETERMINE_LVL_CD | ParticipantCertificationPEOCtfnDetermineLvlCd | ✅ |
| CVRD_ENRT_CTFN_DND_DT | ParticipantCertificationPEOCvrdEnrtCtfnDndDt | ✅ |
| CVRD_ENRT_CTFN_RECD_DT | ParticipantCertificationPEOCvrdEnrtCtfnRecdDt | ✅ |
| ENDED_PER_IN_LER_ID | ParticipantCertificationPEOEndedPerInLerId | — |
| ENRT_CTFN_DND_DT | ParticipantCertificationPEOEnrtCtfnDndDt | ✅ |
| ENRT_CTFN_RECD_DT | ParticipantCertificationPEOEnrtCtfnRecdDt | ✅ |
| ENRT_CTFN_RQD_FLAG | ParticipantCertificationPEOEnrtCtfnRqdFlag | ✅ |
| ENRT_CTFN_TYP_CD | ParticipantCertificationPEOEnrtCtfnTypCd | ✅ |
| JOB_DEFINITION_NAME | ParticipantCertificationPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ParticipantCertificationPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ParticipantCertificationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ParticipantCertificationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ParticipantCertificationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ParticipantCertificationPEOObjectVersionNumber | — |
| PCS_ATTRIBUTE1 | ParticipantCertificationPEOPcsAttribute1 | — |
| PCS_ATTRIBUTE10 | ParticipantCertificationPEOPcsAttribute10 | — |
| PCS_ATTRIBUTE11 | ParticipantCertificationPEOPcsAttribute11 | — |
| PCS_ATTRIBUTE12 | ParticipantCertificationPEOPcsAttribute12 | — |
| PCS_ATTRIBUTE13 | ParticipantCertificationPEOPcsAttribute13 | — |
| PCS_ATTRIBUTE14 | ParticipantCertificationPEOPcsAttribute14 | — |
| PCS_ATTRIBUTE15 | ParticipantCertificationPEOPcsAttribute15 | — |
| PCS_ATTRIBUTE16 | ParticipantCertificationPEOPcsAttribute16 | — |
| PCS_ATTRIBUTE17 | ParticipantCertificationPEOPcsAttribute17 | — |
| PCS_ATTRIBUTE18 | ParticipantCertificationPEOPcsAttribute18 | — |
| PCS_ATTRIBUTE19 | ParticipantCertificationPEOPcsAttribute19 | — |
| PCS_ATTRIBUTE2 | ParticipantCertificationPEOPcsAttribute2 | — |
| PCS_ATTRIBUTE20 | ParticipantCertificationPEOPcsAttribute20 | — |
| PCS_ATTRIBUTE21 | ParticipantCertificationPEOPcsAttribute21 | — |
| PCS_ATTRIBUTE22 | ParticipantCertificationPEOPcsAttribute22 | — |
| PCS_ATTRIBUTE23 | ParticipantCertificationPEOPcsAttribute23 | — |
| PCS_ATTRIBUTE24 | ParticipantCertificationPEOPcsAttribute24 | — |
| PCS_ATTRIBUTE25 | ParticipantCertificationPEOPcsAttribute25 | — |
| PCS_ATTRIBUTE26 | ParticipantCertificationPEOPcsAttribute26 | — |
| PCS_ATTRIBUTE27 | ParticipantCertificationPEOPcsAttribute27 | — |
| PCS_ATTRIBUTE28 | ParticipantCertificationPEOPcsAttribute28 | — |
| PCS_ATTRIBUTE29 | ParticipantCertificationPEOPcsAttribute29 | — |
| PCS_ATTRIBUTE3 | ParticipantCertificationPEOPcsAttribute3 | — |
| PCS_ATTRIBUTE30 | ParticipantCertificationPEOPcsAttribute30 | — |
| PCS_ATTRIBUTE4 | ParticipantCertificationPEOPcsAttribute4 | — |
| PCS_ATTRIBUTE5 | ParticipantCertificationPEOPcsAttribute5 | — |
| PCS_ATTRIBUTE6 | ParticipantCertificationPEOPcsAttribute6 | — |
| PCS_ATTRIBUTE7 | ParticipantCertificationPEOPcsAttribute7 | — |
| PCS_ATTRIBUTE8 | ParticipantCertificationPEOPcsAttribute8 | — |
| PCS_ATTRIBUTE9 | ParticipantCertificationPEOPcsAttribute9 | — |
| PCS_ATTRIBUTE_CATEGORY | ParticipantCertificationPEOPcsAttributeCategory | — |
| PER_IN_LER_ID | ParticipantCertificationPEOPerInLerId | — |
| PROGRAM_APP_NAME | ParticipantCertificationPEOProgramAppName | — |
| PROGRAM_NAME | ParticipantCertificationPEOProgramName | — |
| PROGRAM_UPDATE_DATE | ParticipantCertificationPEOProgramUpdateDate | — |
| PRTT_ENRT_ACTN_ID | ParticipantCertificationPEOPrttEnrtActnId | ✅ |
| PRTT_ENRT_CTFN_PRVDD_ID | ParticipantCertificationPEOPrttEnrtCtfnPrvddId | ✅ |
| PRTT_ENRT_RSLT_ID | ParticipantCertificationPEOPrttEnrtRsltId | — |
| REQUEST_ID | ParticipantCertificationPEORequestId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PRTT_ENRT_CTFN_PRVDD](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprttenrtctfnprvdd.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
