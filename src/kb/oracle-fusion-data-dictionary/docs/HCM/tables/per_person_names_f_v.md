---
id: DOC-HCM-692
doc_type: system-doc
title: "PER_PERSON_NAMES_F_V — View de Nomes de Pessoas"
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
  - nomes-pessoas
  - person-names-view
  - view
aliases:
  - PER_PERSON_NAMES_F_V
  - per_person_names_f_v
  - view-nomes-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_NAMES_F_V

## Visão Geral

**View** que apresenta os nomes de pessoas com filtros pré-aplicados para facilitar consultas. Combina dados da tabela `PER_PERSON_NAMES_F` com regras de negócio simplificadas, evitando joins complexos.

> [!note] Sufixo _V
> O sufixo `_V` indica **View** — consulta pré-definida sobre uma ou mais tabelas base.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consultas simplificadas de nomes** — acesso direto sem necessidade de filtros de vigência manuais
- **Relatórios e dashboards** — fonte otimizada para BI
- **Integrações** — ponto de acesso padronizado para nomes
- **APIs e interfaces** — consumo por telas de busca de pessoas

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_NAME_ID | NUMBER(18) | NOT NULL | PK | Identificador do registro de nome | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | NAME_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de nome (GLOBAL, LEGAL, etc.) | — | 🟢 90% |
| 4 | FIRST_NAME | VARCHAR2(150) | NULL | Nome | Primeiro nome | — | 🟢 95% |
| 5 | LAST_NAME | VARCHAR2(150) | NOT NULL | Nome | Sobrenome | — | 🟢 95% |
| 6 | FULL_NAME | VARCHAR2(360) | NULL | Nome | Nome completo | — | 🟢 90% |
| 7 | DISPLAY_NAME | VARCHAR2(360) | NULL | Nome | Nome para exibição | — | 🟢 85% |
| 8 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 90% |
| 9 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa na visÃ£o de nomes)

### Tabelas-filha (FK de saída)
- Nenhuma — views não possuem FKs diretas.

---

## Uso Típico

### Buscar nome de exibição de uma pessoa
```sql
SELECT v.DISPLAY_NAME, v.FULL_NAME
FROM   PER_PERSON_NAMES_F_V v
WHERE  v.PERSON_ID = :p_person_id
  AND  v.NAME_TYPE = 'GLOBAL'
  AND  SYSDATE BETWEEN v.EFFECTIVE_START_DATE AND v.EFFECTIVE_END_DATE;
```

---

## Observações

- Por ser uma view, não aceita DML direto.
- Pode incluir filtros pré-aplicados que diferem da tabela base.
- Preferir esta view para consultas simples de nomes.

---

## Referências

- [Oracle Docs — PER_PERSON_NAMES_F_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersonnamesfv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
