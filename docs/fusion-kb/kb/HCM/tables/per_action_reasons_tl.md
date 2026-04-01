---
id: DOC-HCM-614
doc_type: system-doc
title: "PER_ACTION_REASONS_TL — Motivos de Ações de RH (Traduções)"
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
  - traducoes
  - action-reasons-tl
aliases:
  - PER_ACTION_REASONS_TL
  - per_action_reasons_tl
  - per-action-reasons-tl
  - motivos-de-ações-de-rh-(traduções)
  - per-action-reasons-t
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_REASONS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos motivos de ações de RH em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe motivos de ação no idioma do usuário.
- **Relatórios localizados** — suporte a relatórios multilíngues.
- **Self-service** — interface traduzida para colaboradores e gestores.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_REASON_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do motivo de ação | PER_ACTION_REASONS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | ACTION_REASON_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do motivo | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_action_reasons_b]] — via `ACTION_REASON_ID` (tabela base do motivo de ação de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Motivos de ação em português
```sql
SELECT tl.ACTION_REASON_ID, tl.ACTION_REASON_NAME
FROM   PER_ACTION_REASONS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `ACTION_REASON_ID` + `LANGUAGE`.
- Sempre usar JOIN com a tabela _B para obter dados completos.
---

## 🔗 PVOs Relacionados

### [[actionreasonspvo|ActionReasonsPVO]] (GL · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| BUSINESS_GROUP_ID | ActionReasonsTranslationPEOBusinessGroupId | — |
| CREATED_BY | ActionReasonsTranslationPEOCreatedBy | — |
| CREATION_DATE | ActionReasonsTranslationPEOCreationDate | — |
| DESCRIPTION | ActionReasonsTranslationPEODescription | ✅ |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionReasonsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionReasonsTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ActionReasonsTranslationPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | ActionReasonsTranslationPEOSeedDataSource | — |
| SOURCE_LANG | ActionReasonsTranslationPEOSourceLang | ✅ |

### [[actionreasonstranslationpvo|ActionReasonsTranslationPVO]] (GL · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonId | ✅ |
| BUSINESS_GROUP_ID | ActionReasonsTranslationPEOBusinessGroupId | — |
| CREATED_BY | ActionReasonsTranslationPEOCreatedBy | — |
| CREATION_DATE | ActionReasonsTranslationPEOCreationDate | — |
| DESCRIPTION | ActionReasonsTranslationPEODescription | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionReasonsTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionReasonsTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ActionReasonsTranslationPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | ActionReasonsTranslationPEOSeedDataSource | — |
| SOURCE_LANG | ActionReasonsTranslationPEOSourceLang | — |

### [[businessunitpvo|BusinessUnitPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[departmentpvo|DepartmentPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[departmentpvoviewall|DepartmentPVOViewAll]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[enterprisepvo|EnterprisePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[gradeladderpvo|GradeLadderPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ProgressionActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ProgressionActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ProgressionActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ProgressionActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[gradepvo|GradePVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTLPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTLPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTLPEOLanguage | — |

### [[gradesteppvo|GradeStepPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| SOURCE_LANG | ActionReasonsTranslationPEOSourceLang | — |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonTranslationPEOActionReasonId | ✅ |
| LANGUAGE | ActionReasonTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[legalemployerpvo|LegalEmployerPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[organizationpvo|OrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[payrollstatutoryunitpvo|PayrollStatutoryUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

### [[projectexpenditureorganizationpvo|ProjectExpenditureOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[projecttaskowningorganizationpvo|ProjectTaskOwningOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[projectunitclassificationpvo|ProjectUnitClassificationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[ratepvo|RatePVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonTranslationPEOActionReason | ✅ |
| ACTION_REASON_ID | ActionReasonTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonTranslationPEOLanguage | — |

### [[reportingestablishmentpvo|ReportingEstablishmentPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[reportingestablishmentpvoviewall|ReportingEstablishmentPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[taxreportingunitpvo|TaxReportingUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | — |

### [[unionpvo|UnionPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REASON | ActionReasonsTranslationPEOActionReason | — |
| ACTION_REASON_ID | ActionReasonsTranslationPEOActionReasonId | — |
| LANGUAGE | ActionReasonsTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ActionReasonsTranslationPEOLastUpdateDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ACTION_REASONS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionreasonstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
