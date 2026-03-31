---
id: DOC-HCM-654
doc_type: system-doc
title: "PER_DRIVERS_LICENSES — Carteiras de Motorista"
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
  - cnh
  - drivers-licenses
aliases:
  - PER_DRIVERS_LICENSES
  - per_drivers_licenses
  - per-drivers-licenses
  - carteiras-de-motorista
  - per-drivers-licenses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DRIVERS_LICENSES

## 📌 Visão Geral

Armazena os registros de **carteiras de motorista (CNH)** dos colaboradores. Contém informações sobre categorias, validade e restrições.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de CNH** — registro e controle de validade de habilitações.
- **Compliance** — garantia de que motoristas possuem CNH válida e na categoria correta.
- **Benefícios** — elegibilidade a benefícios como auxílio-combustível.
- **Segurança** — verificação de habilitação para funções que exigem direção.
- **Alertas** — notificação de CNHs próximas ao vencimento.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DRIVERS_LICENSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | LICENSE_NUMBER | VARCHAR2(60) | NULL | Identificação | Número da CNH | — | 🟢 85% |
| 4 | LICENSE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo/categoria da CNH | PER_DRIVERS_LICENSE_TYPES | 🟢 85% |
| 5 | DATE_FROM | DATE | NULL | Período | Data de emissão | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Período | Data de validade | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador titular da carteira de habilitação)
- [[per_drivers_license_types]] — via `LICENSE_TYPE_ID` (tipo/categoria da carteira de habilitação)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### CNHs válidas
```sql
SELECT pdl.LICENSE_NUMBER, pdl.DATE_FROM, pdl.DATE_TO
FROM   PER_DRIVERS_LICENSES pdl
WHERE  pdl.PERSON_ID = :p_person_id
  AND  pdl.DATE_TO >= SYSDATE;
```

### Filtros comuns
- `DATE_TO >= SYSDATE` — CNHs válidas
- `DATE_TO < SYSDATE` — CNHs vencidas
---

## 🔒 Observações

- No Brasil, as categorias de CNH são: A, B, C, D, E (motocicleta a veículos especiais).
- O campo `DATE_TO` permite monitorar vencimentos e gerar alertas.
- Dados pessoais sujeitos a LGPD.
---

## 🔗 PVOs Relacionados

### [[driverslicensespvo|DriversLicensesPVO]] (HCM · BICC: 18/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | DriversLicensesPEOBusinessGroupId | — |
| CREATED_BY | DriversLicensesPEOCreatedBy | ✅ |
| CREATION_DATE | DriversLicensesPEOCreationDate | ✅ |
| DATE_FROM | DriversLicensesPEODateFrom | ✅ |
| DATE_TO | DriversLicensesPEODateTo | ✅ |
| DRIVERS_LICENSE_ID | DriversLicenseId | ✅ |
| ISSUING_AUTHORITY | DriversLicensesPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | DriversLicensesPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | DriversLicensesPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | DriversLicensesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DriversLicensesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DriversLicensesPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | DriversLicensesPEOLegislationCode | ✅ |
| LICENSE_NUMBER | DriversLicensesPEOLicenseNumber | ✅ |
| LICENSE_SUSPENDED | DriversLicensesPEOLicenseSuspended | ✅ |
| NUMBER_OF_POINTS | DriversLicensesPEONumberOfPoints | ✅ |
| OBJECT_VERSION_NUMBER | DriversLicensesPEOObjectVersionNumber | — |
| PERSON_ID | DriversLicensesPEOPersonId | ✅ |
| SUSPENDED_FROM_DATE | DriversLicensesPEOSuspendedFromDate | ✅ |
| SUSPENDED_TO_DATE | DriversLicensesPEOSuspendedToDate | ✅ |
| VIOLATIONS | DriversLicensesPEOViolations | ✅ |

### [[driverslicensespvoviewall|DriversLicensesPVOViewAll]] (HCM · BICC: 18/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | DriversLicensesPEOBusinessGroupId | — |
| CREATED_BY | DriversLicensesPEOCreatedBy | ✅ |
| CREATION_DATE | DriversLicensesPEOCreationDate | ✅ |
| DATE_FROM | DriversLicensesPEODateFrom | ✅ |
| DATE_TO | DriversLicensesPEODateTo | ✅ |
| DRIVERS_LICENSE_ID | DriversLicenseId | ✅ |
| ISSUING_AUTHORITY | DriversLicensesPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | DriversLicensesPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | DriversLicensesPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | DriversLicensesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DriversLicensesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DriversLicensesPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | DriversLicensesPEOLegislationCode | ✅ |
| LICENSE_NUMBER | DriversLicensesPEOLicenseNumber | ✅ |
| LICENSE_SUSPENDED | DriversLicensesPEOLicenseSuspended | ✅ |
| NUMBER_OF_POINTS | DriversLicensesPEONumberOfPoints | ✅ |
| OBJECT_VERSION_NUMBER | DriversLicensesPEOObjectVersionNumber | — |
| PERSON_ID | DriversLicensesPEOPersonId | ✅ |
| SUSPENDED_FROM_DATE | DriversLicensesPEOSuspendedFromDate | ✅ |
| SUSPENDED_TO_DATE | DriversLicensesPEOSuspendedToDate | ✅ |
| VIOLATIONS | DriversLicensesPEOViolations | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_DRIVERS_LICENSES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdriverslicenses.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
