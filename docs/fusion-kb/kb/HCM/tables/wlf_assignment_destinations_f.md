---
id: DOC-HCM-724
doc_type: system-doc
title: "WLF_ASSIGNMENT_DESTINATIONS_F — Destinos de Atribuição (Learning)"
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
  - destinos-atribuição
aliases:
  - WLF_ASSIGNMENT_DESTINATIONS_F
  - wlf_assignment_destinations_f
  - wlf-assignment-destinations-f
  - destinos-de-atribuição-learning
  - assignment-destinations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_ASSIGNMENT_DESTINATIONS_F

## Visão Geral

Armazena os **destinos das atribuições de aprendizado**, definindo para quais entidades (pessoas, departamentos, organizações) um item de aprendizado foi atribuído. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Distribuição de treinamentos** — define quem recebe cada atribuição de aprendizado.
- **Atribuição em massa** — suporta distribuição para departamentos/organizações inteiras.
- **Tracking de compliance** — rastreia quais unidades receberam treinamentos obrigatórios.
- **Relatórios de cobertura** — análise de penetração dos treinamentos na organização.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_DESTINATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único do destino | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | EVENT_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição de evento associada | WLF_EVENT_ASSIGNMENTS_F | 🟡 80% |
| 5 | DESTINATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de destino (PERSON, DEPT, ORG) | — | 🟡 75% |
| 6 | DESTINATION_ID | NUMBER(18) | NULL | FK | ID da entidade destino | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_event_assignments_f]] — via `EVENT_ASSIGNMENT_ID` (atribuição de evento)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Destinos de uma atribuição de aprendizado
```sql
SELECT ad.DESTINATION_TYPE, ad.DESTINATION_ID
FROM   WLF_ASSIGNMENT_DESTINATIONS_F ad
WHERE  ad.EVENT_ASSIGNMENT_ID = :p_event_assignment_id
  AND  SYSDATE BETWEEN ad.EFFECTIVE_START_DATE AND ad.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `DESTINATION_TYPE = 'PERSON'` — Apenas destinos individuais
- `EVENT_ASSIGNMENT_ID = :p_id` — Destinos de uma atribuição específica

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- O campo DESTINATION_ID é polimórfico — o tipo é definido por DESTINATION_TYPE.
- Faz parte do módulo Workforce Learning (prefixo WLF_).

---

## Referências

- [Oracle Docs — WLF_ASSIGNMENT_DESTINATIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfassignmentdestinationsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[eventassignmentdestinationpvo|EventAssignmentDestinationPVO]] (HCM · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNED_TO_ID | EventAssignmentDestinationDEOAssignedToId | — |
| ASSIGNED_TO_TYPE | EventAssignmentDestinationDEOAssignedToType | ✅ |
| ASSIGNMENT_DESTINATION_ID | EventAssignmentDestinationDEOAssignmentDestinationId | ✅ |
| CREATED_BY | EventAssignmentDestinationDEOCreatedBy | — |
| CREATION_DATE | EventAssignmentDestinationDEOCreationDate | — |
| EFFECTIVE_END_DATE | EventAssignmentDestinationDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EventAssignmentDestinationDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | EventAssignmentDestinationDEOEnterpriseId | — |
| EVENT_ASSIGNMENT_ID | EventAssignmentDestinationDEOEventAssignmentId | — |
| LAST_UPDATE_DATE | EventAssignmentDestinationDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EventAssignmentDestinationDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EventAssignmentDestinationDEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EventAssignmentDestinationDEOObjectVersionNumber | — |
| OPERATION | EventAssignmentDestinationDEOOperation | ✅ |
