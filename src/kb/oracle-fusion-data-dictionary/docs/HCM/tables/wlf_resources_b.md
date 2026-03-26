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
