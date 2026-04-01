---
id: DOC-HCM-256
doc_type: system-doc
title: "HRT_QUALIFIERS_B — Qualificadores — Base"
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
  - qualifiers
  - talent
  - perfil
aliases:
  - HRT_QUALIFIERS_B
  - hrt_qualifiers_b
  - hrt-qualifiers-b
  - qualifiers-base
  - qualificadores-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_QUALIFIERS_B

## 📌 Visao Geral

Tabela base que armazena os **qualificadores** usados para refinar itens de perfil — como nivel de experiencia, contexto de uso de uma competencia ou especializacao dentro de uma habilidade.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Refinamento:** Adicionar contexto a itens de perfil.
- **Matching:** Qualificadores permitem matching mais preciso entre perfis.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUALIFIER_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do qualificador | — | 🟢 95% |
| 2 | QUALIFIER_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do qualificador | — | 🟢 90% |
| 3 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo ao qual se aplica | [[hrt_content_types_b]] | 🟢 90% |
| 4 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 90% |
| 5 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 90% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo do qualificador)

### Tabelas-filha (FK de saida)
- [[hrt_qualifiers_tl]] — via `QUALIFIER_ID` (traducoes do qualificador)

---

## 📎 Uso Tipico

### Qualificadores de um tipo
```sql
SELECT q.QUALIFIER_ID, q.QUALIFIER_CODE
FROM   HRT_QUALIFIERS_B q
WHERE  q.CONTENT_TYPE_ID = :p_content_type_id
  AND  SYSDATE BETWEEN q.DATE_FROM AND NVL(q.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hrt_qualifiers_tl]].
- Qualificadores adicionam dimensao extra ao item de perfil.

---

## 📚 Referencias

- [Oracle Docs — HRT_QUALIFIERS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtqualifiersb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QualifiersBEOBusinessGroupId9 | — |
| LAST_UPDATE_DATE | QualifiersBEOLastUpdateDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| QUALIFIER_CODE | QualifiersBEOQualifierCode | ✅ |
| QUALIFIER_ID | QualifiersBEOQualifierId | ✅ |
| QUALIFIER_SET_ID | QualifierSetId | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SBusinessGroupId | — |
| LAST_UPDATE_DATE | SourcesBPEOLastUpdateDate | ✅ |
| QUALIFIER_CODE | SourceCode | — |
| QUALIFIER_ID | SourceId1 | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SBusinessGroupId | — |
| LAST_UPDATE_DATE | SourcesBPEOLastUpdateDate | ✅ |
| QUALIFIER_CODE | SourceCode | — |
| QUALIFIER_ID | SourceId1 | — |

### [[qualifierspvo|QualifiersPVO]] (HCM · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QualifiersBPEOBusinessGroupId | ✅ |
| CREATED_BY | QualifiersBPEOCreatedBy | ✅ |
| CREATION_DATE | QualifiersBPEOCreationDate | ✅ |
| EMP_DEF_FLAG | QualifiersBPEOEmpDefFlag | ✅ |
| EMP_VIEW_FLAG | QualifiersBPEOEmpViewFlag | ✅ |
| LAST_UPDATE_DATE | QualifiersBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualifiersBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QualifiersBPEOLastUpdatedBy | ✅ |
| MGR_DEF_FLAG | QualifiersBPEOMgrDefFlag | ✅ |
| MGR_VIEW_FLAG | QualifiersBPEOMgrViewFlag | ✅ |
| MODULE_ID | QualifiersBPEOModuleId | ✅ |
| OBJECT_VERSION_NUMBER | QualifiersBPEOObjectVersionNumber | ✅ |
| QUALIFIER_CODE | QualifiersBPEOQualifierCode | ✅ |
| QUALIFIER_ID | QualifiersBPEOQualifierId | ✅ |
| QUALIFIER_SEQ_NUMBER | QualifiersBPEOQualifierSeqNumber | ✅ |
| QUALIFIER_SET_ID | QualifiersBPEOQualifierSetId | ✅ |
| SEARCH_FLAG | QualifiersBPEOSearchFlag | ✅ |

### [[riskpvo|RiskPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SBusinessGroupId | — |
| LAST_UPDATE_DATE | SourcesBPEOLastUpdateDate | ✅ |
| QUALIFIER_CODE | SourceCode | — |
| QUALIFIER_ID | SourceId1 | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SBusinessGroupId | — |
| LAST_UPDATE_DATE | SourcesBPEOLastUpdateDate | ✅ |
| QUALIFIER_CODE | SourceCode | — |
| QUALIFIER_ID | SourceId1 | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | SBPEOBusinessGroupId | — |
| EMP_DEF_FLAG | EmpDefFlag | — |
| EMP_VIEW_FLAG | EmpViewFlag | — |
| MGR_DEF_FLAG | MgrDefFlag | — |
| MGR_VIEW_FLAG | MgrViewFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| QUALIFIER_CODE | QualifierCode | — |
| QUALIFIER_CODE | SourcesBPEOSourceCode | ✅ |
| QUALIFIER_ID | QualifierId | — |
| QUALIFIER_ID | SourcesBPEOSourceId | — |
| QUALIFIER_SEQ_NUMBER | QualifierSeqNumber | — |
| QUALIFIER_SET_ID | QualifierSetId | — |
