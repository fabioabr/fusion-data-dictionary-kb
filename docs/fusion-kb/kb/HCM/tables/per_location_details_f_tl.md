---
id: DOC-HCM-676
doc_type: system-doc
title: "PER_LOCATION_DETAILS_F_TL — Traduções de Detalhes de Localização"
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
  - per-locations
  - location-details-tl
  - traducao-localizacao
  - multilanguage
aliases:
  - PER_LOCATION_DETAILS_F_TL
  - per_location_details_f_tl
  - traducao-detalhes-localizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_LOCATION_DETAILS_F_TL

## Visao Geral

Armazena as **traduções** dos detalhes de localização em múltiplos idiomas. Cada registro contém a versão traduzida dos campos descritivos da tabela base `PER_LOCATION_DETAILS_F` para um idioma específico.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **tradução** — cada registro da tabela base possui N registros nesta tabela, um por idioma configurado.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte a operações multilíngues** — permite exibir nomes e descrições de localizações em diferentes idiomas
- **Relatórios internacionais** — geração de relatórios no idioma do usuário
- **Interfaces localizadas** — apresentação de dados na língua da subsidiária/filial
- **Compliance regulatório** — manter registros no idioma local exigido pela legislação

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOCATION_DETAILS_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do detalhe de localização | PER_LOCATION_DETAILS_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex: PT, EN) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | LOCATION_DETAILS_NAME | VARCHAR2(360) | NULL | Tradução | Nome traduzido do detalhe de localização | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida da localização | — | 🟡 70% |
| 6 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 90% |
| 7 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_location_details_f]] — via `LOCATION_DETAILS_ID` (tabela base dos detalhes da localização)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Obter nome traduzido de uma localização
```sql
SELECT tl.LOCATION_DETAILS_NAME, tl.DESCRIPTION, tl.LANGUAGE
FROM   PER_LOCATION_DETAILS_F_TL tl
WHERE  tl.LOCATION_DETAILS_ID = :p_location_details_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## Observações

- A chave primária é composta por `LOCATION_DETAILS_ID` + `LANGUAGE`.
- Sempre filtrar por `LANGUAGE` para obter a tradução desejada.
- `SOURCE_LANG` indica se a tradução é nativa ou herdada de outro idioma.

---

## Referências

- [Oracle Docs — PER_LOCATION_DETAILS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocationdetailsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[careerpreferencelocationpvo|CareerPreferenceLocationPVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[careerpreferencelocationpvo_viewall|CareerPreferenceLocationPVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[employeeexpensebusinessunitpvo|EmployeeExpenseBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[excludedlocation1pvo|ExcludedLocation1PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation1pvo_viewall|ExcludedLocation1PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation2pvo|ExcludedLocation2PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation2pvo_viewall|ExcludedLocation2PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation3pvo|ExcludedLocation3PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation3pvo_viewall|ExcludedLocation3PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation4pvo|ExcludedLocation4PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[excludedlocation4pvo_viewall|ExcludedLocation4PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | — |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDPEOLocationName | ✅ |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| CREATED_BY | LocationDetailsTranslationPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsTranslationPEOCreationDate | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | ✅ |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsTranslationPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| CREATED_BY | LocationDetailsTranslationPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsTranslationPEOCreationDate | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | ✅ |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsTranslationPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[locationdetailstranslationpvo|LocationDetailsTranslationPVO]] (HCM · BICC: 12/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| CREATED_BY | LocationDetailsTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | LocationDetailsTranslationPEOCreationDate | ✅ |
| DESCRIPTION | LocationDetailsTranslationPEODescription | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsTranslationPEOLastUpdatedBy | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | ✅ |

### [[locationdetailstranslationpvoviewall|LocationDetailsTranslationPVOViewAll]] (HCM · BICC: 7/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| CREATED_BY | LocationDetailsTranslationPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsTranslationPEOCreationDate | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsTranslationPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[locationrefpvo|LocationRefPVO]] (HCM · BICC: 6/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| CREATED_BY | LocationDetailsTranslationPEOCreatedBy | — |
| CREATION_DATE | LocationDetailsTranslationPEOCreationDate | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LocationDetailsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LocationDetailsTranslationPEOLastUpdatedBy | — |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsId | ✅ |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| OBJECT_VERSION_NUMBER | LocationDetailsTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[orderbusinessunitpvo|OrderBusinessUnitPVO]] (OTHER · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | ✅ |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | ✅ |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | ✅ |

### [[outstandingcardtransactionbusinessunitpvo|OutstandingCardTransactionBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[payablebusinessunitpvo|PayableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[preferredlocation1pvo|PreferredLocation1PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation1pvo_viewall|PreferredLocation1PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation2pvo|PreferredLocation2PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation2pvo_viewall|PreferredLocation2PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation3pvo|PreferredLocation3PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation3pvo_viewall|PreferredLocation3PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation4pvo|PreferredLocation4PVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[preferredlocation4pvo_viewall|PreferredLocation4PVO_Viewall]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_LOCATION_CODE | LocationDetailsTranslationPEOAcLocationCode | — |
| DESCRIPTION | LocationDetailsTranslationPEODescription | — |
| EFFECTIVE_END_DATE | LocationDetailsTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocationDetailsTranslationPEOEffectiveStartDate | ✅ |
| LANGUAGE | LocationDetailsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | LocationDetailsTranslationPEOLastUpdateDate | ✅ |
| LOCATION_CODE | LocationDetailsTranslationPEOLocationCode | — |
| LOCATION_DETAILS_ID | LocationDetailsTranslationPEOLocationDetailsId | — |
| LOCATION_NAME | LocationDetailsTranslationPEOLocationName | ✅ |
| SOURCE_LANG | LocationDetailsTranslationPEOSourceLang | — |

### [[projectcontractbusinessunitpvo|ProjectContractBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[projectcostingbusinessunitpvo|ProjectCostingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[projectinvoicingbusinessunitpvo|ProjectInvoicingBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[projectrevenuebusinessunitpvo|ProjectRevenueBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |

### [[receivablebusinessunitpvo|ReceivableBusinessUnitPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | LocDetailsDescription | — |
| EFFECTIVE_END_DATE | LocDetailsTLEffectiveEndDate | — |
| EFFECTIVE_START_DATE | LocDetailsTLEffectiveStartDate | — |
| LANGUAGE | LocDetailsTLLanguage | — |
| LOCATION_CODE | LocDetailsLocationCode | — |
| LOCATION_DETAILS_ID | LocDetailsTLLocationDetailsId | — |
| LOCATION_NAME | LocDetailsLocationName | — |
