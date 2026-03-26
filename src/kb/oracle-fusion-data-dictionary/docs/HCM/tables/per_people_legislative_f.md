---
id: DOC-HCM-686
doc_type: system-doc
title: "PER_PEOPLE_LEGISLATIVE_F — Dados Legislativos de Pessoas"
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
  - dados-legislativos
  - legislacao
  - people-legislative
  - compliance
aliases:
  - PER_PEOPLE_LEGISLATIVE_F
  - per_people_legislative_f
  - dados-legislativos-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PEOPLE_LEGISLATIVE_F

## Visão Geral

Armazena os **dados legislativos** associados a cada pessoa, específicos por país/legislação. Contém informações regulatórias como etnia, deficiência, veterano, entre outros atributos exigidos pela legislação trabalhista de cada país. Tabela date-effective.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance regulatório** — armazenar dados exigidos pela legislação local
- **Relatórios EEO (Equal Employment Opportunity)** — classificação para relatórios de diversidade
- **eSocial (Brasil)** — informações trabalhistas para o governo
- **Relatórios de diversidade e inclusão** — análise demográfica da força de trabalho
- **Obrigações fiscais** — dados legislativos para cálculos tributários

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PEOPLE_LEGISLATIVE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro legislativo | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(4) | NOT NULL | Classificação | Código do país/legislação (BR, US, etc.) | — | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | SEX | VARCHAR2(30) | NULL | Legislativo | Sexo legal do colaborador | — | 🟡 80% |
| 7 | MARITAL_STATUS | VARCHAR2(30) | NULL | Legislativo | Estado civil | — | 🟡 75% |
| 8 | HIGHEST_EDUCATION_LEVEL | VARCHAR2(30) | NULL | Legislativo | Nível de escolaridade mais alto | — | 🟡 70% |
| 9 | ETHNICITY | VARCHAR2(30) | NULL | Legislativo | Etnia/raça (conforme legislação local) | — | 🟡 70% |
| 10 | DISABILITY_FLAG | VARCHAR2(1) | NULL | Legislativo | Indicador de pessoa com deficiência (Y/N) | — | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa com dados legislativos)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Dados legislativos brasileiros de um colaborador
```sql
SELECT pl.SEX, pl.MARITAL_STATUS, pl.HIGHEST_EDUCATION_LEVEL, pl.ETHNICITY
FROM   PER_PEOPLE_LEGISLATIVE_F pl
WHERE  pl.PERSON_ID = :p_person_id
  AND  pl.LEGISLATION_CODE = 'BR'
  AND  SYSDATE BETWEEN pl.EFFECTIVE_START_DATE AND pl.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Os campos disponíveis e seus valores válidos variam por `LEGISLATION_CODE`.
- Contém dados sensíveis (etnia, deficiência) — sujeitos a LGPD/GDPR.
- Para o Brasil, inclui dados exigidos pelo eSocial.

---

## Referências

- [Oracle Docs — PER_PEOPLE_LEGISLATIVE_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpeoplelegislativef.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
