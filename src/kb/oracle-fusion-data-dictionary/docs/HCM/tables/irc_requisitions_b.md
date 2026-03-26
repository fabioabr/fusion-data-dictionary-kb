---
id: DOC-HCM-522
doc_type: system-doc
title: "IRC_REQUISITIONS_B — Requisicoes de Vaga (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - requisitions
  - irc-recruiting
aliases:
  - IRC_REQUISITIONS_B
  - irc_requisitions_b
  - requisitions-b
  - requisitions-b-hcm
  - irc-requisitions-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQUISITIONS_B

## Visao Geral

**Requisicoes de vaga** (job requisitions). Tabela base (`_B`) central do processo de recrutamento.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de vagas:** Registro central de requisicoes.
- **Fluxo de aprovacao:** Status desde criacao ate preenchimento.
- **Headcount:** Dimensionamento de equipe.
- **Metricas:** Time-to-fill, custo por vaga.
- **Integracao:** Candidatos, ofertas, publicacoes, campanhas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 95% |
| 2 | REQUISITION_NUMBER | VARCHAR2(30) | NOT NULL | Identificacao | Numero visivel | — | 🟢 90% |
| 3 | REQUISITION_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟢 85% |
| 4 | HIRING_MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | PER_ALL_PEOPLE_F | 🟢 85% |
| 5 | RECRUITER_ID | NUMBER(18) | NULL | FK | Recrutador | PER_ALL_PEOPLE_F | 🟡 80% |
| 6 | NUMBER_OF_OPENINGS | NUMBER | NULL | Dados | Posicoes abertas | — | 🟡 80% |
| 7 | OPEN_DATE | DATE | NULL | Dados | Data de abertura | — | 🟡 80% |
| 8 | TARGET_CLOSE_DATE | DATE | NULL | Dados | Data-alvo | — | 🟡 75% |
| 9 | PROCESS_ID | NUMBER(18) | NULL | FK | Processo seletivo | IRC_PROCESSES_B | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `HIRING_MANAGER_ID` / `RECRUITER_ID` (gestor responsavel pela contratacao)
- [[irc_processes_b]] — via `PROCESS_ID` (processo seletivo da requisicao)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Vagas abertas
```sql
SELECT r.REQUISITION_NUMBER, r.REQUISITION_STATUS,
       r.NUMBER_OF_OPENINGS, r.OPEN_DATE
FROM   IRC_REQUISITIONS_B r WHERE r.REQUISITION_STATUS = 'OPEN'
ORDER BY r.OPEN_DATE;
```

### Filtros comuns
- `REQUISITION_STATUS = 'OPEN'` — Abertas
- `HIRING_MANAGER_ID = :id` — Por gestor
---

## Observacoes

- Tabela central do Recruiting.
- REQUISITION_NUMBER e o identificador visivel.
---

## Referencias

- [Oracle Docs -- IRC_REQUISITIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircrequisitionsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
