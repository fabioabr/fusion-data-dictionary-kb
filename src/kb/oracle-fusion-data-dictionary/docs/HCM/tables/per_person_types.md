---
id: DOC-HCM-693
doc_type: system-doc
title: "PER_PERSON_TYPES — Tipos de Pessoa"
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
  - tipos-pessoa
  - person-types
  - classificacao
  - core-hr
aliases:
  - PER_PERSON_TYPES
  - per_person_types
  - tipos-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_TYPES

## Visão Geral

Armazena os **tipos de pessoa** definidos no sistema. Classifica cada pessoa conforme sua categoria (empregado, contingente, candidato, contato, dependente, etc.). Tabela de referência/configuração.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de pessoas** — distinguir empregados, contingentes, candidatos, etc.
- **Controle de acesso** — tipos diferentes possuem permissões distintas
- **Relatórios de headcount** — segregar contagem por tipo de pessoa
- **Folha de pagamento** — determinar regras de processamento por tipo
- **Compliance trabalhista** — tipos de pessoa impactam obrigações legais

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de pessoa | — | 🟢 95% |
| 2 | SYSTEM_PERSON_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de sistema (EMP, CWK, APL, OTHER) | — | 🟢 90% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NOT NULL | Flag | Indica se o tipo está ativo (Y/N) | — | 🟡 80% |
| 4 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o tipo padrão (Y/N) | — | 🟡 75% |
| 5 | LEGISLATION_CODE | VARCHAR2(4) | NULL | Classificação | Código do país/legislação | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — tabela de configuração/referência.

### Tabelas-filha (FK de saída)
- [[per_person_types_tl]] — via `PERSON_TYPE_ID` (traduções do tipo de pessoa)
- [[per_person_type_usages_m]] — via `PERSON_TYPE_ID` (usos do tipo de pessoa nos registros)
- [[per_periods_of_service]] — via `PERSON_TYPE_ID` (períodos de serviço com este tipo de pessoa)

---

## Uso Típico

### Listar tipos de pessoa ativos
```sql
SELECT pt.PERSON_TYPE_ID, pt.SYSTEM_PERSON_TYPE
FROM   PER_PERSON_TYPES pt
WHERE  pt.ACTIVE_FLAG = 'Y';
```

---

## Observações

- `SYSTEM_PERSON_TYPE` é o código de sistema: EMP (empregado), CWK (contingente), APL (candidato), OTHER.
- Tabela de configuração — alterações impactam classificação de todas as pessoas.
- Nomes descritivos estão na tabela de tradução `PER_PERSON_TYPES_TL`.

---

## Referências

- [Oracle Docs — PER_PERSON_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersontypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[persontypesextractpvo|PersonTypesExtractPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEFAULT_FLAG | DefaultFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_TYPE_ID | PersonTypeId | ✅ |
| SEEDED_PERSON_TYPE_KEY | SeededPersonTypeKey | ✅ |
| SYSTEM_PERSON_TYPE | SystemPersonType | ✅ |

### [[persontypespvo|PersonTypesPVO]] (HCM · BICC: 8/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | PersonTypesPEOActiveFlag | ✅ |
| BUSINESS_GROUP_ID | PersonTypesPEOBusinessGroupId | — |
| CREATED_BY | PersonTypesPEOCreatedBy | ✅ |
| CREATION_DATE | PersonTypesPEOCreationDate | ✅ |
| DEFAULT_FLAG | PersonTypesPEODefaultFlag | ✅ |
| LAST_UPDATE_DATE | PersonTypesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonTypesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonTypesPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PersonTypesPEOObjectVersionNumber | — |
| PERSON_TYPE_ID | PersonTypeId | ✅ |
| SYSTEM_PERSON_TYPE | PersonTypesPEOSystemPersonType | ✅ |
