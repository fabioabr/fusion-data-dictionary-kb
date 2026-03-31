---
id: DOC-HCM-747
doc_type: system-doc
title: "WLF_REQUEST_DETAILS — Detalhes de Solicitações (Learning)"
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
  - solicitações
aliases:
  - WLF_REQUEST_DETAILS
  - wlf_request_details
  - wlf-request-details
  - detalhes-solicitações-learning
  - request-details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_REQUEST_DETAILS

## Visão Geral

Armazena os **detalhes de solicitações** de aprendizado, incluindo pedidos de inscrição, aprovações pendentes e requisições de treinamento.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Fluxo de aprovação** — registra solicitações de treinamento pendentes de aprovação.
- **Self-service** — solicitações feitas pelos próprios colaboradores.
- **Gestão de demanda** — visibilidade sobre demandas de treinamento.
- **Workflow** — suporta o fluxo de aprovação gerencial.
- **Rastreabilidade** — histórico de solicitações e seus status.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUEST_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe da solicitação | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que fez a solicitação | PER_ALL_PEOPLE_F | 🟢 85% |
| 3 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado solicitado | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 4 | REQUEST_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de solicitação (enrollment, cancellation) | — | 🟡 70% |
| 5 | REQUEST_STATUS | VARCHAR2(30) | NULL | Status | Status da solicitação (pending, approved, rejected) | — | 🟡 75% |
| 6 | REQUEST_DATE | DATE | NULL | Data | Data da solicitação | — | 🟡 80% |
| 7 | APPROVAL_DATE | DATE | NULL | Data | Data da aprovação/rejeição | — | 🟡 70% |
| 8 | APPROVER_PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que aprovou/rejeitou | PER_ALL_PEOPLE_F | 🟡 70% |
| 9 | COMMENTS | VARCHAR2(2000) | NULL | Dados | Comentários/justificativa | — | 🟡 65% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa solicitante do aprendizado)
- [[per_all_people_f]] — via `APPROVER_PERSON_ID` (pessoa aprovadora da solicitação de aprendizado)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item solicitado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Solicitações pendentes de aprovação
```sql
SELECT rd.REQUEST_TYPE, rd.REQUEST_DATE, rd.COMMENTS,
       p.FULL_NAME AS solicitante, li.ITEM_NUMBER
FROM   WLF_REQUEST_DETAILS rd
JOIN   PER_ALL_PEOPLE_F p ON rd.PERSON_ID = p.PERSON_ID
JOIN   WLF_LEARNING_ITEMS_F li ON rd.LEARNING_ITEM_ID = li.LEARNING_ITEM_ID
WHERE  rd.REQUEST_STATUS = 'PENDING'
ORDER BY rd.REQUEST_DATE;
```

### Filtros comuns
- `REQUEST_STATUS = 'PENDING'` — Solicitações pendentes
- `PERSON_ID = :p_person_id` — Solicitações de um colaborador

---

## Observações

- Tabela transacional — sem sufixo _F (não é date-effective).
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Suporta o fluxo de self-service de aprendizado.
- COMMENTS pode conter justificativas do solicitante ou do aprovador.

---

## Referências

- [Oracle Docs — WLF_REQUEST_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfrequestdetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
