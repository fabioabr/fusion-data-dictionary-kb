---
id: DOC-HCM-051
doc_type: system-doc
title: "BEN_PER_LE_HABITS_COV_F — Cobertura de Hábitos por Evento de Vida"
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
  - habitos-cobertura
  - habits-coverage
aliases:
  - BEN_PER_LE_HABITS_COV_F
  - ben_per_le_habits_cov_f
  - habitos-cobertura-beneficios
  - habits-coverage
  - ben-per-le-habits-cov
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PER_LE_HABITS_COV_F

## 📌 Visão Geral

Armazena informações sobre **hábitos pessoais** (ex.: tabagismo) que impactam a cobertura de benefícios, vinculados a eventos de vida.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Fatores de risco:** Registra hábitos que impactam premiação.
- **Underwriting:** Base para cálculo de risco em seguros de vida.
- **Compliance:** Atende requisitos de disclosure de hábitos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de cobertura de hábitos por evento de vida
```sql
SELECT * FROM BEN_PER_LE_HABITS_COV_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Cobertura de Hábitos por Evento de Vida).

---

## 🔗 PVOs Relacionados

### [[benefitemployeehabitspvo|BenefitEmployeeHabitsPVO]] (HCM · BICC: 30/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| COORD_MED_CVG_END_DT | CoordMedCvgEndDt | ✅ |
| COORD_MED_CVG_STRT_DT | CoordMedCvgStrtDt | ✅ |
| COORD_MED_EXT_ER | CoordMedExtEr | ✅ |
| COORD_MED_INSR_CRR_IDENT | CoordMedInsrCrrIdent | ✅ |
| COORD_MED_INSR_CRR_NAM | CoordMedInsrCrrNam | ✅ |
| COORD_MED_PL_NAME | CoordMedPlName | ✅ |
| COORD_MED_PLN_NO | CoordMedPlnNo | ✅ |
| COORD_NO_CVG_FLAG | CoordNoCvgFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CVRD_IN_ANTHR_PL | CvrdInAnthrPl | ✅ |
| DISABILITY_STATUS | DisabilityStatus | ✅ |
| DPDNT_ADOPTION_DATE | DpdntAdoptionDate | ✅ |
| DPDNT_VLNTRY_SVCE_FLAG | DpdntVlntrySvceFlag | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LE_HABITS_COV_ID | LeHabitsCovId | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ON_MILITARY_SERVICE | OnMilitaryService | ✅ |
| PERSON_ID | PersonId | ✅ |
| RECEIPT_OF_DEATH_CERT_DATE | ReceiptOfDeathCertDate | ✅ |
| REGISTERED_DISABLED_FLAG | RegisteredDisabledFlag | ✅ |
| STUDENT_STATUS | StudentStatus | ✅ |
| TOBACCO_TYPE_USAGE | TobaccoTypeUsage | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PER_LE_HABITS_COV_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benperlehabitscovf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
