---
id: DOC-HCM-046
doc_type: system-doc
title: "BEN_OPT_F — Opções de Benefício"
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
  - opcoes-beneficio
  - benefit-options
aliases:
  - BEN_OPT_F
  - ben_opt_f
  - opcoes-beneficio-hcm
  - benefit-options
  - ben-opt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_OPT_F

## 📌 Visão Geral

Armazena as **opções de benefício** disponíveis (ex.: cobertura individual, familiar, com dependentes). Cada opção representa uma variante de cobertura dentro de um plano.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Variantes de cobertura:** Define as opções disponíveis por plano.
- **Seleção do participante:** Lista de opções apresentadas durante inscrição.
- **Precificação:** Cada opção pode ter taxa/premium diferente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_OPT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de opções de benefício
```sql
SELECT * FROM BEN_OPT_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Opções de Benefício).

---

## 🔗 PVOs Relacionados

### [[optionpvo|OptionPVO]] (HCM · BICC: 21/57)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CARRIER_OPT_NAME | CarrierOptName | ✅ |
| CMBN_PTIP_OPT_ID | CmbnPtipOptId | — |
| COMPONENT_REASON | ComponentReason | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GLOBAL_FLAG | GlobalFlag | ✅ |
| GROUP_OPT_ID | GroupOptId | — |
| INVK_WV_OPT_FLAG | InvkWvOptFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LEGISLATION_SUBGROUP | LegislationSubgroup | ✅ |
| MAPPING_TABLE_NAME | MappingTableName | ✅ |
| MAPPING_TABLE_PK_ID | MappingTablePkId | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPT_ATTRIBUTE1 | OptAttribute1 | — |
| OPT_ATTRIBUTE10 | OptAttribute10 | — |
| OPT_ATTRIBUTE11 | OptAttribute11 | — |
| OPT_ATTRIBUTE12 | OptAttribute12 | — |
| OPT_ATTRIBUTE13 | OptAttribute13 | — |
| OPT_ATTRIBUTE14 | OptAttribute14 | — |
| OPT_ATTRIBUTE15 | OptAttribute15 | — |
| OPT_ATTRIBUTE16 | OptAttribute16 | — |
| OPT_ATTRIBUTE17 | OptAttribute17 | — |
| OPT_ATTRIBUTE18 | OptAttribute18 | — |
| OPT_ATTRIBUTE19 | OptAttribute19 | — |
| OPT_ATTRIBUTE2 | OptAttribute2 | — |
| OPT_ATTRIBUTE20 | OptAttribute20 | — |
| OPT_ATTRIBUTE21 | OptAttribute21 | — |
| OPT_ATTRIBUTE22 | OptAttribute22 | — |
| OPT_ATTRIBUTE23 | OptAttribute23 | — |
| OPT_ATTRIBUTE24 | OptAttribute24 | — |
| OPT_ATTRIBUTE25 | OptAttribute25 | — |
| OPT_ATTRIBUTE26 | OptAttribute26 | — |
| OPT_ATTRIBUTE27 | OptAttribute27 | — |
| OPT_ATTRIBUTE28 | OptAttribute28 | — |
| OPT_ATTRIBUTE29 | OptAttribute29 | — |
| OPT_ATTRIBUTE3 | OptAttribute3 | — |
| OPT_ATTRIBUTE30 | OptAttribute30 | — |
| OPT_ATTRIBUTE4 | OptAttribute4 | — |
| OPT_ATTRIBUTE5 | OptAttribute5 | — |
| OPT_ATTRIBUTE6 | OptAttribute6 | — |
| OPT_ATTRIBUTE7 | OptAttribute7 | — |
| OPT_ATTRIBUTE8 | OptAttribute8 | — |
| OPT_ATTRIBUTE9 | OptAttribute9 | — |
| OPT_ATTRIBUTE_CATEGORY | OptAttributeCategory | ✅ |
| OPT_ID | OptId | ✅ |
| RQD_PERD_ENRT_NENRT_RL | RqdPerdEnrtNenrtRl | — |
| RQD_PERD_ENRT_NENRT_UOM | RqdPerdEnrtNenrtUom | ✅ |
| RQD_PERD_ENRT_NENRT_VAL | RqdPerdEnrtNenrtVal | ✅ |
| SHORT_CODE | ShortCode | ✅ |
| SHORT_NAME | ShortName | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_OPT_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benoptf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
