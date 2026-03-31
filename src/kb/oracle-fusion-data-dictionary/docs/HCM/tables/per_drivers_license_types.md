---
id: DOC-HCM-655
doc_type: system-doc
title: "PER_DRIVERS_LICENSE_TYPES — Tipos de Carteira de Motorista"
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
  - license-types
aliases:
  - PER_DRIVERS_LICENSE_TYPES
  - per_drivers_license_types
  - per-drivers-license-types
  - tipos-de-carteira-de-motorista
  - per-drivers-license-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DRIVERS_LICENSE_TYPES

## 📌 Visão Geral

Armazena os **tipos/categorias de carteira de motorista** disponíveis no sistema. Define as categorias de habilitação válidas por legislação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração** — define as categorias de CNH disponíveis.
- **Validação** — garante que apenas categorias válidas sejam registradas.
- **Compliance** — categorias conforme legislação de cada país.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LICENSE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo | — | 🟢 90% |
| 2 | LICENSE_TYPE | VARCHAR2(30) | NOT NULL | Identificação | Código do tipo (A, B, C, D, E) | — | 🟢 85% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição do tipo de CNH | — | 🟢 85% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela de referência de tipos de CNH.

### Tabelas-filha (FK de saída)
- [[per_drivers_licenses]] — via `LICENSE_TYPE_ID` (CNHs deste tipo)

---

## 📎 Uso Típico

### Tipos de CNH disponíveis
```sql
SELECT pdlt.LICENSE_TYPE, pdlt.DESCRIPTION
FROM   PER_DRIVERS_LICENSE_TYPES pdlt
WHERE  pdlt.LEGISLATION_CODE = 'BR'
ORDER BY pdlt.LICENSE_TYPE;
```

### Filtros comuns
- `LEGISLATION_CODE = 'BR'` — Categorias brasileiras
---

## 🔒 Observações

- Tabela de referência (lookup) — registros pré-configurados por legislação.
- No Brasil: A (moto), B (carro), C (caminhão), D (ônibus), E (veículos articulados).
---

## 🔗 PVOs Relacionados

### [[driverslicensespvo|DriversLicensesPVO]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | DriversLicenseTypesPEOBusinessGroupId | — |
| CREATED_BY | DriversLicenseTypesPEOCreatedBy | — |
| CREATION_DATE | DriversLicenseTypesPEOCreationDate | — |
| DRIVERS_LICENSE_ID | DriversLicenseTypesPEODriversLicenseId | — |
| DRIVERS_LICENSE_TYPE_ID | DriversLicenseTypesPEODriversLicenseTypeId | — |
| LAST_UPDATE_DATE | DriversLicenseTypesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DriversLicenseTypesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DriversLicenseTypesPEOLastUpdatedBy | — |
| LICENSE_TYPE | DriversLicenseTypesPEOLicenseType | ✅ |
| OBJECT_VERSION_NUMBER | DriversLicenseTypesPEOObjectVersionNumber | — |

### [[driverslicensespvoviewall|DriversLicensesPVOViewAll]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | DriversLicenseTypesPEOBusinessGroupId | — |
| CREATED_BY | DriversLicenseTypesPEOCreatedBy | — |
| CREATION_DATE | DriversLicenseTypesPEOCreationDate | — |
| DRIVERS_LICENSE_ID | DriversLicenseTypesPEODriversLicenseId | — |
| DRIVERS_LICENSE_TYPE_ID | DriversLicenseTypesPEODriversLicenseTypeId | — |
| LAST_UPDATE_DATE | DriversLicenseTypesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DriversLicenseTypesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DriversLicenseTypesPEOLastUpdatedBy | — |
| LICENSE_TYPE | DriversLicenseTypesPEOLicenseType | ✅ |
| OBJECT_VERSION_NUMBER | DriversLicenseTypesPEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — PER_DRIVERS_LICENSE_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdriverslicensetypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
