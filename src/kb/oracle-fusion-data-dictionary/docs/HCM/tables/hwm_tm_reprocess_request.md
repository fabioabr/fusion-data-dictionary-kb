---
id: DOC-HCM-384
doc_type: system-doc
title: "HWM_TM_REPROCESS_REQUEST — Requisições de Reprocessamento de Tempo"
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
  - time-management
  - reprocess
  - reprocessamento
aliases:
  - HWM_TM_REPROCESS_REQUEST
  - hwm_tm_reprocess_request
  - hwm-tm-reprocess-request
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REPROCESS_REQUEST

## 📌 Visão Geral

Armazena as **requisições de reprocessamento** de entradas de tempo. Quando entradas de tempo precisam ser recalculadas ou resubmetidas, um registro de reprocessamento é criado nesta tabela.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reprocessamento:** gerencia solicitações de recálculo de entradas de tempo.
- **Correção de erros:** permite reprocessar entradas com problemas.
- **Auditoria:** rastreia todas as solicitações de reprocessamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REPROCESS_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador da requisição | — | 🟡 70% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador afetado | PER_ALL_PEOPLE_F | 🟡 70% |
| 3 | REQUEST_DATE | DATE | NOT NULL | Período | Data da solicitação | — | 🟡 65% |
| 4 | REQUEST_STATUS | VARCHAR2(30) | NULL | Classificação | Status da requisição | — | 🟡 65% |
| 5 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Motivo do reprocessamento | — | 🟡 55% |
| 6 | START_DATE | DATE | NULL | Período | Início do período a reprocessar | — | 🟡 60% |
| 7 | END_DATE | DATE | NULL | Período | Fim do período a reprocessar | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa da solicitacao de reprocessamento)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Típico

### Requisições de reprocessamento pendentes
```sql
SELECT r.REPROCESS_REQUEST_ID, r.PERSON_ID,
       r.REQUEST_DATE, r.REQUEST_STATUS
FROM   HWM_TM_REPROCESS_REQUEST r
WHERE  r.REQUEST_STATUS = 'PENDING';
```

### Filtros comuns
- `REQUEST_STATUS = 'PENDING' — Requisições pendentes`
- `PERSON_ID = :p_person_id — Por colaborador`

---

## 🔒 Observações

- Utilizada para rastrear solicitações de reprocessamento de time entries.
- O reprocessamento pode impactar cálculos de payroll já realizados.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REPROCESS_REQUEST](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmreprocessrequest.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
