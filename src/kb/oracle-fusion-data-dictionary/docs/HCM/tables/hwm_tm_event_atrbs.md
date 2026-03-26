---
id: DOC-HCM-376
doc_type: system-doc
title: "HWM_TM_EVENT_ATRBS — Atributos de Eventos de Time Management"
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
  - event-attributes
  - atributos-eventos-tempo
aliases:
  - HWM_TM_EVENT_ATRBS
  - hwm_tm_event_atrbs
  - hwm-tm-event-atrbs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_EVENT_ATRBS

## 📌 Visão Geral

Armazena os **atributos associados a eventos de gestão de tempo** (Time Management). Cada registro contém pares de atributo-valor vinculados a um evento de tempo específico, permitindo extensibilidade dos dados de eventos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Extensibilidade de eventos:** permite adicionar informações customizadas aos eventos de tempo.
- **Rastreabilidade:** mantém atributos adicionais para auditoria e conformidade.
- **Integração com payroll:** atributos utilizados para cálculos de folha de pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador único do atributo de evento | — | 🟡 70% |
| 2 | EVENT_ID | NUMBER(18) | NOT NULL | FK | Identificador do evento de tempo | HWM_TM_EVENTS | 🟡 70% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do atributo | — | 🟡 65% |
| 4 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 65% |
| 5 | ATTRIBUTE_CATEGORY | VARCHAR2(80) | NULL | Classificação | Categoria do atributo | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Típico

### Consultar atributos de eventos de tempo
```sql
SELECT ea.EVENT_ATRB_ID, ea.EVENT_ID,
       ea.ATTRIBUTE_NAME, ea.ATTRIBUTE_VALUE
FROM   HWM_TM_EVENT_ATRBS ea
WHERE  ea.EVENT_ID = :p_event_id;
```

### Filtros comuns
- `EVENT_ID = :p_event_id — Filtrar por evento específico`
- `ATTRIBUTE_NAME = :p_attr_name — Filtrar por nome do atributo`

---

## 🔒 Observações

- Tabela de extensibilidade para eventos de time management.
- A estrutura EAV (Entity-Attribute-Value) permite flexibilidade mas pode impactar performance.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_EVENT_ATRBS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmeventatrbs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
