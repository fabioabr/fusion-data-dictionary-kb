---
id: DOC-HCM-748
doc_type: system-doc
title: "WLF_RESOURCES_B — Recursos (Base) (Learning)"
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
  - learning
  - workforce-learning
  - recursos
aliases:
  - WLF_RESOURCES_B
  - wlf_resources_b
  - wlf-resources-b
  - recursos-base-learning
  - resources-learning
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_RESOURCES_B

## Visão Geral

Armazena os **recursos base** disponíveis para o módulo Workforce Learning, incluindo instrutores, salas, equipamentos e outros ativos utilizados em treinamentos. Tabela base (_B), independente de idioma.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de instrutores** — cadastro de instrutores internos e externos.
- **Gestão de salas/locais** — registro de espaços disponíveis para treinamento.
- **Alocação de recursos** — controle de disponibilidade de recursos para eventos.
- **Planejamento logístico** — base para agendar recursos para turmas/eventos.
- **Custos** — associação de recursos a componentes de custo.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESOURCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do recurso | — | 🟡 80% |
| 2 | RESOURCE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de recurso (INSTRUCTOR, VENUE, EQUIPMENT) | — | 🟡 75% |
| 3 | RESOURCE_CODE | VARCHAR2(30) | NULL | Identificação | Código do recurso | — | 🟡 70% |
| 4 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa vinculada (para instrutores) | PER_ALL_PEOPLE_F | 🟡 75% |
| 5 | CAPACITY | NUMBER(9) | NULL | Dados | Capacidade (para salas/locais) | — | 🟡 65% |
| 6 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização do recurso | — | 🟡 65% |
| 7 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o recurso está ativo (Y/N) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (instrutor vinculado)

### Tabelas-filha (FK de saída)
- [[wlf_resources_tl]] — via `RESOURCE_ID` (traduções do recurso)

---

## Uso Típico

### Instrutores ativos
```sql
SELECT rb.RESOURCE_CODE, rb.RESOURCE_TYPE, p.FULL_NAME
FROM   WLF_RESOURCES_B rb
JOIN   PER_ALL_PEOPLE_F p ON rb.PERSON_ID = p.PERSON_ID
WHERE  rb.RESOURCE_TYPE = 'INSTRUCTOR'
  AND  rb.ACTIVE_FLAG = 'Y';
```

### Filtros comuns
- `RESOURCE_TYPE = 'INSTRUCTOR'` — Apenas instrutores
- `ACTIVE_FLAG = 'Y'` — Apenas recursos ativos

---

## Observações

- Tabela base (_B) — contém dados independentes de idioma.
- Traduções disponíveis em WLF_RESOURCES_TL.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- PERSON_ID é preenchido apenas quando o recurso é uma pessoa (instrutor).

---

## Referências

- [Oracle Docs — WLF_RESOURCES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfresources.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[resourcepvo|ResourcePVO]] (HCM · BICC: 5/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | ResourcePEOAddressId | — |
| ATTRIBUTION_ID | ResourcePEOAttributionId | — |
| ATTRIBUTION_TYPE | ResourcePEOAttributionType | — |
| CAPACITY | ResourcePEOCapacity | ✅ |
| CONTACT_ID | ResourcePEOContactId | — |
| CREATED_BY | ResourcePEOCreatedBy | — |
| CREATION_DATE | ResourcePEOCreationDate | — |
| ENTERPRISE_ID | ResourcePEOEnterpriseId | — |
| LAST_UPDATE_DATE | ResourcePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ResourcePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResourcePEOLastUpdatedBy | — |
| LOCATION_ID | ResourcePEOLocationId | — |
| OBJECT_VERSION_NUMBER | ResourcePEOObjectVersionNumber | — |
| RESOURCE_ID | ResourcePEOResourceId | ✅ |
| RESOURCE_NUMBER | ResourcePEOResourceNumber | ✅ |
| RESOURCE_TYPE | ResourcePEOResourceType | ✅ |
| RS_ATTRIBUTE1 | ResourcePEORsAttribute1 | — |
| RS_ATTRIBUTE10 | ResourcePEORsAttribute10 | — |
| RS_ATTRIBUTE11 | ResourcePEORsAttribute11 | — |
| RS_ATTRIBUTE12 | ResourcePEORsAttribute12 | — |
| RS_ATTRIBUTE13 | ResourcePEORsAttribute13 | — |
| RS_ATTRIBUTE14 | ResourcePEORsAttribute14 | — |
| RS_ATTRIBUTE15 | ResourcePEORsAttribute15 | — |
| RS_ATTRIBUTE16 | ResourcePEORsAttribute16 | — |
| RS_ATTRIBUTE17 | ResourcePEORsAttribute17 | — |
| RS_ATTRIBUTE18 | ResourcePEORsAttribute18 | — |
| RS_ATTRIBUTE19 | ResourcePEORsAttribute19 | — |
| RS_ATTRIBUTE2 | ResourcePEORsAttribute2 | — |
| RS_ATTRIBUTE20 | ResourcePEORsAttribute20 | — |
| RS_ATTRIBUTE3 | ResourcePEORsAttribute3 | — |
| RS_ATTRIBUTE4 | ResourcePEORsAttribute4 | — |
| RS_ATTRIBUTE5 | ResourcePEORsAttribute5 | — |
| RS_ATTRIBUTE6 | ResourcePEORsAttribute6 | — |
| RS_ATTRIBUTE7 | ResourcePEORsAttribute7 | — |
| RS_ATTRIBUTE8 | ResourcePEORsAttribute8 | — |
| RS_ATTRIBUTE9 | ResourcePEORsAttribute9 | — |
| RS_ATTRIBUTE_CATEGORY | ResourcePEORsAttributeCategory | — |
| RS_ATTRIBUTE_DATE1 | ResourcePEORsAttributeDate1 | — |
| RS_ATTRIBUTE_DATE10 | ResourcePEORsAttributeDate10 | — |
| RS_ATTRIBUTE_DATE11 | ResourcePEORsAttributeDate11 | — |
| RS_ATTRIBUTE_DATE12 | ResourcePEORsAttributeDate12 | — |
| RS_ATTRIBUTE_DATE13 | ResourcePEORsAttributeDate13 | — |
| RS_ATTRIBUTE_DATE14 | ResourcePEORsAttributeDate14 | — |
| RS_ATTRIBUTE_DATE15 | ResourcePEORsAttributeDate15 | — |
| RS_ATTRIBUTE_DATE2 | ResourcePEORsAttributeDate2 | — |
| RS_ATTRIBUTE_DATE3 | ResourcePEORsAttributeDate3 | — |
| RS_ATTRIBUTE_DATE4 | ResourcePEORsAttributeDate4 | — |
| RS_ATTRIBUTE_DATE5 | ResourcePEORsAttributeDate5 | — |
| RS_ATTRIBUTE_DATE6 | ResourcePEORsAttributeDate6 | — |
| RS_ATTRIBUTE_DATE7 | ResourcePEORsAttributeDate7 | — |
| RS_ATTRIBUTE_DATE8 | ResourcePEORsAttributeDate8 | — |
| RS_ATTRIBUTE_DATE9 | ResourcePEORsAttributeDate9 | — |
| RS_ATTRIBUTE_NUMBER1 | ResourcePEORsAttributeNumber1 | — |
| RS_ATTRIBUTE_NUMBER10 | ResourcePEORsAttributeNumber10 | — |
| RS_ATTRIBUTE_NUMBER11 | ResourcePEORsAttributeNumber11 | — |
| RS_ATTRIBUTE_NUMBER12 | ResourcePEORsAttributeNumber12 | — |
| RS_ATTRIBUTE_NUMBER13 | ResourcePEORsAttributeNumber13 | — |
| RS_ATTRIBUTE_NUMBER14 | ResourcePEORsAttributeNumber14 | — |
| RS_ATTRIBUTE_NUMBER15 | ResourcePEORsAttributeNumber15 | — |
| RS_ATTRIBUTE_NUMBER16 | ResourcePEORsAttributeNumber16 | — |
| RS_ATTRIBUTE_NUMBER17 | ResourcePEORsAttributeNumber17 | — |
| RS_ATTRIBUTE_NUMBER18 | ResourcePEORsAttributeNumber18 | — |
| RS_ATTRIBUTE_NUMBER19 | ResourcePEORsAttributeNumber19 | — |
| RS_ATTRIBUTE_NUMBER2 | ResourcePEORsAttributeNumber2 | — |
| RS_ATTRIBUTE_NUMBER20 | ResourcePEORsAttributeNumber20 | — |
| RS_ATTRIBUTE_NUMBER3 | ResourcePEORsAttributeNumber3 | — |
| RS_ATTRIBUTE_NUMBER4 | ResourcePEORsAttributeNumber4 | — |
| RS_ATTRIBUTE_NUMBER5 | ResourcePEORsAttributeNumber5 | — |
| RS_ATTRIBUTE_NUMBER6 | ResourcePEORsAttributeNumber6 | — |
| RS_ATTRIBUTE_NUMBER7 | ResourcePEORsAttributeNumber7 | — |
| RS_ATTRIBUTE_NUMBER8 | ResourcePEORsAttributeNumber8 | — |
| RS_ATTRIBUTE_NUMBER9 | ResourcePEORsAttributeNumber9 | — |
| SOURCE_ID | ResourcePEOSourceId | — |
| SOURCE_TYPE | ResourcePEOSourceType | — |
| STATUS | ResourcePEOStatus | ✅ |
| TRAINING_VENDOR_RES_ID | ResourcePEOTrainingVendorResId | — |

### [[trainingsupplierresourcepvo|TrainingSupplierResourcePVO]] (HCM · BICC: 4/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | TrainingSupplierResourcePEOAddressId | — |
| ATTRIBUTION_ID | TrainingSupplierResourcePEOAttributionId | — |
| ATTRIBUTION_TYPE | TrainingSupplierResourcePEOAttributionType | — |
| CAPACITY | TrainingSupplierResourcePEOCapacity | — |
| CONTACT_ID | TrainingSupplierResourcePEOContactId | — |
| CREATED_BY | TrainingSupplierResourcePEOCreatedBy | — |
| CREATION_DATE | TrainingSupplierResourcePEOCreationDate | — |
| ENTERPRISE_ID | TrainingSupplierResourcePEOEnterpriseId | — |
| LAST_UPDATE_DATE | TrainingSupplierResourcePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | TrainingSupplierResourcePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TrainingSupplierResourcePEOLastUpdatedBy | — |
| LOCATION_ID | TrainingSupplierResourcePEOLocationId | — |
| OBJECT_VERSION_NUMBER | TrainingSupplierResourcePEOObjectVersionNumber | — |
| RESOURCE_ID | TrainingSupplierResourcePEOResourceId | ✅ |
| RESOURCE_NUMBER | TrainingSupplierResourcePEOResourceNumber | ✅ |
| RESOURCE_TYPE | TrainingSupplierResourcePEOResourceType | ✅ |
| RS_ATTRIBUTE1 | TrainingSupplierResourcePEORsAttribute1 | — |
| RS_ATTRIBUTE10 | TrainingSupplierResourcePEORsAttribute10 | — |
| RS_ATTRIBUTE11 | TrainingSupplierResourcePEORsAttribute11 | — |
| RS_ATTRIBUTE12 | TrainingSupplierResourcePEORsAttribute12 | — |
| RS_ATTRIBUTE13 | TrainingSupplierResourcePEORsAttribute13 | — |
| RS_ATTRIBUTE14 | TrainingSupplierResourcePEORsAttribute14 | — |
| RS_ATTRIBUTE15 | TrainingSupplierResourcePEORsAttribute15 | — |
| RS_ATTRIBUTE16 | TrainingSupplierResourcePEORsAttribute16 | — |
| RS_ATTRIBUTE17 | TrainingSupplierResourcePEORsAttribute17 | — |
| RS_ATTRIBUTE18 | TrainingSupplierResourcePEORsAttribute18 | — |
| RS_ATTRIBUTE19 | TrainingSupplierResourcePEORsAttribute19 | — |
| RS_ATTRIBUTE2 | TrainingSupplierResourcePEORsAttribute2 | — |
| RS_ATTRIBUTE20 | TrainingSupplierResourcePEORsAttribute20 | — |
| RS_ATTRIBUTE3 | TrainingSupplierResourcePEORsAttribute3 | — |
| RS_ATTRIBUTE4 | TrainingSupplierResourcePEORsAttribute4 | — |
| RS_ATTRIBUTE5 | TrainingSupplierResourcePEORsAttribute5 | — |
| RS_ATTRIBUTE6 | TrainingSupplierResourcePEORsAttribute6 | — |
| RS_ATTRIBUTE7 | TrainingSupplierResourcePEORsAttribute7 | — |
| RS_ATTRIBUTE8 | TrainingSupplierResourcePEORsAttribute8 | — |
| RS_ATTRIBUTE9 | TrainingSupplierResourcePEORsAttribute9 | — |
| RS_ATTRIBUTE_CATEGORY | TrainingSupplierResourcePEORsAttributeCategory | — |
| RS_ATTRIBUTE_DATE1 | TrainingSupplierResourcePEORsAttributeDate1 | — |
| RS_ATTRIBUTE_DATE10 | TrainingSupplierResourcePEORsAttributeDate10 | — |
| RS_ATTRIBUTE_DATE11 | TrainingSupplierResourcePEORsAttributeDate11 | — |
| RS_ATTRIBUTE_DATE12 | TrainingSupplierResourcePEORsAttributeDate12 | — |
| RS_ATTRIBUTE_DATE13 | TrainingSupplierResourcePEORsAttributeDate13 | — |
| RS_ATTRIBUTE_DATE14 | TrainingSupplierResourcePEORsAttributeDate14 | — |
| RS_ATTRIBUTE_DATE15 | TrainingSupplierResourcePEORsAttributeDate15 | — |
| RS_ATTRIBUTE_DATE2 | TrainingSupplierResourcePEORsAttributeDate2 | — |
| RS_ATTRIBUTE_DATE3 | TrainingSupplierResourcePEORsAttributeDate3 | — |
| RS_ATTRIBUTE_DATE4 | TrainingSupplierResourcePEORsAttributeDate4 | — |
| RS_ATTRIBUTE_DATE5 | TrainingSupplierResourcePEORsAttributeDate5 | — |
| RS_ATTRIBUTE_DATE6 | TrainingSupplierResourcePEORsAttributeDate6 | — |
| RS_ATTRIBUTE_DATE7 | TrainingSupplierResourcePEORsAttributeDate7 | — |
| RS_ATTRIBUTE_DATE8 | TrainingSupplierResourcePEORsAttributeDate8 | — |
| RS_ATTRIBUTE_DATE9 | TrainingSupplierResourcePEORsAttributeDate9 | — |
| RS_ATTRIBUTE_NUMBER1 | TrainingSupplierResourcePEORsAttributeNumber1 | — |
| RS_ATTRIBUTE_NUMBER10 | TrainingSupplierResourcePEORsAttributeNumber10 | — |
| RS_ATTRIBUTE_NUMBER11 | TrainingSupplierResourcePEORsAttributeNumber11 | — |
| RS_ATTRIBUTE_NUMBER12 | TrainingSupplierResourcePEORsAttributeNumber12 | — |
| RS_ATTRIBUTE_NUMBER13 | TrainingSupplierResourcePEORsAttributeNumber13 | — |
| RS_ATTRIBUTE_NUMBER14 | TrainingSupplierResourcePEORsAttributeNumber14 | — |
| RS_ATTRIBUTE_NUMBER15 | TrainingSupplierResourcePEORsAttributeNumber15 | — |
| RS_ATTRIBUTE_NUMBER16 | TrainingSupplierResourcePEORsAttributeNumber16 | — |
| RS_ATTRIBUTE_NUMBER17 | TrainingSupplierResourcePEORsAttributeNumber17 | — |
| RS_ATTRIBUTE_NUMBER18 | TrainingSupplierResourcePEORsAttributeNumber18 | — |
| RS_ATTRIBUTE_NUMBER19 | TrainingSupplierResourcePEORsAttributeNumber19 | — |
| RS_ATTRIBUTE_NUMBER2 | TrainingSupplierResourcePEORsAttributeNumber2 | — |
| RS_ATTRIBUTE_NUMBER20 | TrainingSupplierResourcePEORsAttributeNumber20 | — |
| RS_ATTRIBUTE_NUMBER3 | TrainingSupplierResourcePEORsAttributeNumber3 | — |
| RS_ATTRIBUTE_NUMBER4 | TrainingSupplierResourcePEORsAttributeNumber4 | — |
| RS_ATTRIBUTE_NUMBER5 | TrainingSupplierResourcePEORsAttributeNumber5 | — |
| RS_ATTRIBUTE_NUMBER6 | TrainingSupplierResourcePEORsAttributeNumber6 | — |
| RS_ATTRIBUTE_NUMBER7 | TrainingSupplierResourcePEORsAttributeNumber7 | — |
| RS_ATTRIBUTE_NUMBER8 | TrainingSupplierResourcePEORsAttributeNumber8 | — |
| RS_ATTRIBUTE_NUMBER9 | TrainingSupplierResourcePEORsAttributeNumber9 | — |
| SOURCE_ID | TrainingSupplierResourcePEOSourceId | — |
| SOURCE_TYPE | TrainingSupplierResourcePEOSourceType | — |
| STATUS | TrainingSupplierResourcePEOStatus | ✅ |
| TRAINING_VENDOR_RES_ID | TrainingSupplierResourcePEOTrainingVendorResId | — |
