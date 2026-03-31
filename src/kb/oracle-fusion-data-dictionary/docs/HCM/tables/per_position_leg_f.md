---
id: DOC-HCM-699
doc_type: system-doc
title: "PER_POSITION_LEG_F — Dados Legislativos de Posição"
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
  - posicao-legislativa
  - position-legislative
  - cargo
  - legislacao
aliases:
  - PER_POSITION_LEG_F
  - per_position_leg_f
  - dados-legislativos-posicao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POSITION_LEG_F

## Visão Geral

Armazena os **dados legislativos** associados a cada posição/cargo, específicos por país/legislação. Contém informações regulatórias exigidas pela legislação trabalhista para cada cargo. Tabela date-effective.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance trabalhista** — registrar dados exigidos por legislação para cada cargo
- **CBO (Classificação Brasileira de Ocupações)** — código CBO associado à posição
- **eSocial** — informações regulatórias do cargo para eventos trabalhistas
- **Relatórios regulatórios** — dados legislativos para RAIS, DIRF
- **Análise de cargos** — classificação legal de cada posição

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POSITION_LEG_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro legislativo | — | 🟡 80% |
| 2 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Referência à posição/cargo | HR_ALL_POSITIONS_F | 🟢 90% |
| 3 | LEGISLATION_CODE | VARCHAR2(4) | NOT NULL | Classificação | Código do país/legislação (BR, US, etc.) | — | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | PROBATION_PERIOD | NUMBER | NULL | Legislativo | Período de experiência (em unidades definidas) | — | 🟡 70% |
| 7 | PROBATION_UNIT | VARCHAR2(30) | NULL | Legislativo | Unidade do período de experiência (DAYS, MONTHS) | — | 🟡 70% |
| 8 | BARGAINING_UNIT_CODE | VARCHAR2(30) | NULL | Legislativo | Código da unidade de negociação sindical | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` (posição com dados legislativos)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Dados legislativos brasileiros de uma posição
```sql
SELECT pl.PROBATION_PERIOD, pl.PROBATION_UNIT, pl.BARGAINING_UNIT_CODE
FROM   PER_POSITION_LEG_F pl
WHERE  pl.POSITION_ID = :p_position_id
  AND  pl.LEGISLATION_CODE = 'BR'
  AND  SYSDATE BETWEEN pl.EFFECTIVE_START_DATE AND pl.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Os campos disponíveis e valores variam conforme a legislação.
- Para o Brasil, pode conter dados como código CBO via DFFs (Descriptive Flex Fields).

---

## Referências

- [Oracle Docs — PER_POSITION_LEG_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpositionlegf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
