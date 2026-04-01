---
id: DOC-HCM-657
doc_type: system-doc
title: "PER_ETHNICITIES — Etnias"
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
  - diversidade
  - etnias
  - ethnicities
aliases:
  - PER_ETHNICITIES
  - per_ethnicities
  - per-ethnicities
  - etnias
  - per-ethnicities
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ETHNICITIES

## 📌 Visão Geral

Armazena os registros de **etnia/raça** dos colaboradores. Utilizada para relatórios de diversidade e compliance com requisitos legais de declaração.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Diversidade e inclusão** — métricas de composição étnica da força de trabalho.
- **Compliance** — atendimento a requisitos legais de declaração (ex.: RAIS, EEO).
- **Relatórios** — dashboards de diversidade para liderança.
- **Políticas de equidade** — monitoramento de equilíbrio étnico em promoções e contratações.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ETHNICITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | ETHNICITY | VARCHAR2(30) | NOT NULL | Classificação | Código da etnia | — | 🟢 85% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação | — | 🟢 85% |
| 5 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | Etnia primária declarada (Y/N) | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador com registro de etnia)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Etnias declaradas
```sql
SELECT pe.ETHNICITY, pe.LEGISLATION_CODE
FROM   PER_ETHNICITIES pe
WHERE  pe.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PRIMARY_FLAG = 'Y'` — Etnia primária declarada
---

## 🔒 Observações

- No Brasil, a classificação segue o padrão IBGE: Branca, Preta, Parda, Amarela, Indígena.
- A declaração é voluntária em muitos contextos — pode haver registros nulos.
- Dados sensíveis (LGPD) — informação de categoria especial.
- Utilizada na declaração RAIS obrigatória no Brasil.
---

## 🔗 PVOs Relacionados

### [[personethinicitypvo|PersonEthinicityPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EthnicityPEOBusinessGroupId | ✅ |
| CREATED_BY | EthnicityPEOCreatedBy | ✅ |
| CREATION_DATE | EthnicityPEOCreationDate | ✅ |
| DECLARER_ID | EthnicityPEODeclarerId | ✅ |
| ETHNICITY | EthnicityPEOEthnicity | ✅ |
| ETHNICITY_ID | EthnicityId | ✅ |
| LAST_UPDATE_DATE | EthnicityPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EthnicityPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | EthnicityPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | EthnicityPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | EthnicityPEOObjectVersionNumber | ✅ |
| PERSON_ID | EthnicityPEOPersonId | ✅ |
| PRIMARY_FLAG | EthnicityPEOPrimaryFlag | ✅ |

### [[personethinicitypvoviewall|PersonEthinicityPVOViewAll]] (HCM · BICC: 9/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EthnicityPEOBusinessGroupId | — |
| CREATED_BY | EthnicityPEOCreatedBy | ✅ |
| CREATION_DATE | EthnicityPEOCreationDate | ✅ |
| DECLARER_ID | EthnicityPEODeclarerId | — |
| ETHNICITY | EthnicityPEOEthnicity | ✅ |
| ETHNICITY_ID | EthnicityId | ✅ |
| LAST_UPDATE_DATE | EthnicityPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EthnicityPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EthnicityPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | EthnicityPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | EthnicityPEOObjectVersionNumber | — |
| PERSON_ID | EthnicityPEOPersonId | ✅ |
| PRIMARY_FLAG | EthnicityPEOPrimaryFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ETHNICITIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perethnicities.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
