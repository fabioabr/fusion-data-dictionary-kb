---
id: DOC-HCM-691
doc_type: system-doc
title: "PER_PERSON_NAMES_F — Nomes de Pessoas"
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
  - person-names
  - nome-completo
  - core-hr
aliases:
  - PER_PERSON_NAMES_F
  - per_person_names_f
  - nomes-pessoas
  - person-names-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_NAMES_F

## Visão Geral

Armazena os **nomes** das pessoas no sistema com vigência temporal. Suporta múltiplos tipos de nome (legal, preferido, exibição) e legislações, permitindo rastrear mudanças de nome ao longo do tempo.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Identificação de colaboradores** — nome completo para exibição em sistemas
- **Documentos legais** — nome legal para contratos, holerites, eSocial
- **Alteração de nome** — casamento, divórcio, retificação
- **Relatórios regulatórios** — RAIS, DIRF, eSocial exigem nome legal vigente
- **Busca e pesquisa** — localizar pessoas por nome ou sobrenome

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_NAME_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de nome | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | NAME_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de nome (GLOBAL, LEGAL, PREFERRED) | — | 🟢 90% |
| 4 | LEGISLATION_CODE | VARCHAR2(4) | NULL | Classificação | Código do país/legislação | — | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | FIRST_NAME | VARCHAR2(150) | NULL | Nome | Primeiro nome | — | 🟢 95% |
| 8 | MIDDLE_NAMES | VARCHAR2(80) | NULL | Nome | Nomes do meio | — | 🟢 90% |
| 9 | LAST_NAME | VARCHAR2(150) | NOT NULL | Nome | Sobrenome | — | 🟢 95% |
| 10 | FULL_NAME | VARCHAR2(360) | NULL | Nome | Nome completo concatenado | — | 🟢 90% |
| 11 | DISPLAY_NAME | VARCHAR2(360) | NULL | Nome | Nome para exibição | — | 🟢 85% |
| 12 | LIST_NAME | VARCHAR2(360) | NULL | Nome | Nome para listas (sobrenome, nome) | — | 🟡 80% |
| 13 | TITLE | VARCHAR2(30) | NULL | Nome | Título (Sr., Sra., Dr.) | — | 🟡 80% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 18 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa titular do registro de nome)

### Tabelas-filha (FK de saída)

---

## Uso Típico

### Nome legal vigente de um colaborador
```sql
SELECT pn.FIRST_NAME, pn.LAST_NAME, pn.FULL_NAME
FROM   PER_PERSON_NAMES_F pn
WHERE  pn.PERSON_ID = :p_person_id
  AND  pn.NAME_TYPE = 'GLOBAL'
  AND  SYSDATE BETWEEN pn.EFFECTIVE_START_DATE AND pn.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência para obter o nome corrente.
- `NAME_TYPE = 'GLOBAL'` é o tipo padrão usado na maioria das consultas.
- `FULL_NAME` é calculado automaticamente a partir das partes do nome.
- Contém dados PII — sujeita a LGPD/GDPR.
- Alterações de nome (casamento, etc.) geram novos registros com novas datas de vigência.

---

## Referências

- [Oracle Docs — PER_PERSON_NAMES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersonnamesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
