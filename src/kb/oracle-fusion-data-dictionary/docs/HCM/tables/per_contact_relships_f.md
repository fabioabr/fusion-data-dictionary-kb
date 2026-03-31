---
id: DOC-HCM-648
doc_type: system-doc
title: "PER_CONTACT_RELSHIPS_F — Relacionamentos de Contatos/Dependentes"
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
  - dependentes
  - contatos
  - contact-relationships
aliases:
  - PER_CONTACT_RELSHIPS_F
  - per_contact_relships_f
  - per-contact-relships-f
  - relacionamentos-de-contatos/dependentes
  - per-contact-relships
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CONTACT_RELSHIPS_F

## 📌 Visão Geral

Armazena os **relacionamentos entre pessoas** (contatos e dependentes) no Oracle HCM, com vigência temporal. Define vínculos familiares, beneficiários e contatos de emergência.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de dependentes** — registro de cônjuge, filhos e outros dependentes.
- **Benefícios** — elegibilidade de dependentes a planos de saúde e outros benefícios.
- **Contatos de emergência** — informações para situações de emergência.
- **Compliance** — declaração de dependentes para fins fiscais e trabalhistas.
- **Relatórios de RH** — análise do perfil familiar da força de trabalho.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTACT_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do relacionamento | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador (pessoa principal) | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | CONTACT_PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa de contato/dependente | PER_ALL_PEOPLE_F | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 6 | CONTACT_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de relacionamento (SPOUSE, CHILD, EMERGENCY, etc.) | — | 🟢 90% |
| 7 | PRIMARY_CONTACT_FLAG | VARCHAR2(1) | NULL | Configuração | Contato primário (Y/N) | — | 🟢 85% |
| 8 | DEPENDENT_FLAG | VARCHAR2(1) | NULL | Classificação | Se é dependente (Y/N) | — | 🟢 85% |
| 9 | BENEFICIARY_FLAG | VARCHAR2(1) | NULL | Classificação | Se é beneficiário (Y/N) | — | 🟢 85% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador principal)
- [[per_all_people_f]] — via `CONTACT_PERSON_ID` (contato/dependente)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Dependentes de um colaborador
```sql
SELECT pcr.CONTACT_TYPE, ppf.FULL_NAME, pcr.DEPENDENT_FLAG
FROM   PER_CONTACT_RELSHIPS_F pcr
JOIN   PER_ALL_PEOPLE_F ppf ON pcr.CONTACT_PERSON_ID = ppf.PERSON_ID
WHERE  pcr.PERSON_ID = :p_person_id
  AND  pcr.DEPENDENT_FLAG = 'Y'
  AND  SYSDATE BETWEEN pcr.EFFECTIVE_START_DATE AND pcr.EFFECTIVE_END_DATE
  AND  SYSDATE BETWEEN ppf.EFFECTIVE_START_DATE AND ppf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `CONTACT_TYPE = 'SPOUSE'` — Cônjuge
- `DEPENDENT_FLAG = 'Y'` — Dependentes
- `BENEFICIARY_FLAG = 'Y'` — Beneficiários
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Tanto o colaborador quanto o contato são registrados em PER_ALL_PEOPLE_F.
- O `CONTACT_TYPE` define o grau de parentesco/relacionamento.
- Dados sensíveis (LGPD) — contém informações familiares protegidas.
---

## 🔗 PVOs Relacionados

### [[contactemailaddressespvo|ContactEmailAddressesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactpassportspvo|ContactPassportsPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactpersonaddresspvo|ContactPersonAddressPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactpersondisabilitypvo|ContactPersonDisabilityPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactpersonnationalidentifierpvo|ContactPersonNationalIdentifierPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactphonespvo|ContactPhonesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

### [[contactrelshipspvo|ContactRelshipsPVO]] (HCM · BICC: 21/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFICIARY_FLAG | ContactRelshipsPEOBeneficiaryFlag | ✅ |
| BONDHOLDER_FLAG | ContactRelshipsPEOBondholderFlag | ✅ |
| BUSINESS_GROUP_ID | ContactRelshipsPEOBusinessGroupId | — |
| CONTACT_PERSON_ID | ContactRelshipsPEOContactPersonId | ✅ |
| CONTACT_RELATIONSHIP_ID | ContactRelationshipId | ✅ |
| CONTACT_TYPE | ContactRelshipsPEOContactType | ✅ |
| CREATED_BY | ContactRelshipsPEOCreatedBy | ✅ |
| CREATION_DATE | ContactRelshipsPEOCreationDate | ✅ |
| DEPENDENT_FLAG | ContactRelshipsPEODependentFlag | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMERGENCY_CONTACT_FLAG | ContactRelshipsPEOEmergencyContactFlag | ✅ |
| END_LIFE_REASON_ID | ContactRelshipsPEOEndLifeReasonId | — |
| EXISTING_PERSON | ContactRelshipsPEOExistingPerson | ✅ |
| LAST_UPDATE_DATE | ContactRelshipsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContactRelshipsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContactRelshipsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ContactRelshipsPEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | ContactRelshipsPEOObjectVersionNumber | — |
| PERSON_ID | ContactRelshipsPEOPersonId | ✅ |
| PERSONAL_FLAG | ContactRelshipsPEOPersonalFlag | ✅ |
| PRIMARY_CONTACT_FLAG | ContactRelshipsPEOPrimaryContactFlag | ✅ |
| RLTD_PER_RSDS_W_DSGNTR_FLAG | ContactRelshipsPEORltdPerRsdsWDsgntrFlag | ✅ |
| SEQUENCE_NUMBER | ContactRelshipsPEOSequenceNumber | ✅ |
| START_LIFE_REASON_ID | ContactRelshipsPEOStartLifeReasonId | — |
| STATUTORY_DEPENDENT | ContactRelshipsPEOStatutoryDependent | ✅ |
| THIRD_PARTY_PAY_FLAG | ContactRelshipsPEOThirdPartyPayFlag | ✅ |

### [[contactrelshipspvoviewall|ContactRelshipsPVOViewAll]] (HCM · BICC: 24/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFICIARY_FLAG | ContactRelshipsPEOBeneficiaryFlag | ✅ |
| BONDHOLDER_FLAG | ContactRelshipsPEOBondholderFlag | ✅ |
| BUSINESS_GROUP_ID | ContactRelshipsPEOBusinessGroupId | ✅ |
| CONTACT_PERSON_ID | ContactRelshipsPEOContactPersonId | ✅ |
| CONTACT_RELATIONSHIP_ID | ContactRelationshipId | ✅ |
| CONTACT_TYPE | ContactRelshipsPEOContactType | ✅ |
| CREATED_BY | ContactRelshipsPEOCreatedBy | ✅ |
| CREATION_DATE | ContactRelshipsPEOCreationDate | ✅ |
| DEPENDENT_FLAG | ContactRelshipsPEODependentFlag | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMERGENCY_CONTACT_FLAG | ContactRelshipsPEOEmergencyContactFlag | ✅ |
| END_LIFE_REASON_ID | ContactRelshipsPEOEndLifeReasonId | ✅ |
| EXISTING_PERSON | ContactRelshipsPEOExistingPerson | ✅ |
| LAST_UPDATE_DATE | ContactRelshipsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContactRelshipsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ContactRelshipsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ContactRelshipsPEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | ContactRelshipsPEOObjectVersionNumber | — |
| PERSON_ID | ContactRelshipsPEOPersonId | ✅ |
| PERSONAL_FLAG | ContactRelshipsPEOPersonalFlag | ✅ |
| PRIMARY_CONTACT_FLAG | ContactRelshipsPEOPrimaryContactFlag | ✅ |
| RLTD_PER_RSDS_W_DSGNTR_FLAG | ContactRelshipsPEORltdPerRsdsWDsgntrFlag | ✅ |
| SEQUENCE_NUMBER | ContactRelshipsPEOSequenceNumber | ✅ |
| START_LIFE_REASON_ID | ContactRelshipsPEOStartLifeReasonId | — |
| STATUTORY_DEPENDENT | ContactRelshipsPEOStatutoryDependent | ✅ |
| THIRD_PARTY_PAY_FLAG | ContactRelshipsPEOThirdPartyPayFlag | ✅ |

### [[contactvisapermitpvo|ContactVisaPermitPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTACT_RELATIONSHIP_ID | ContactRelshipsPEOContactRelationshipId | — |
| EFFECTIVE_END_DATE | ContactRelshipsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactRelshipsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactRelshipsPEOPersonId | — |

---

## 📚 Referências

- [Oracle Docs — PER_CONTACT_RELSHIPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percontactrelshipsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
