---
id: DOC-HCM-103
doc_type: system-doc
title: "HNS_INCIDENTS_SUMMARY — Resumo de Incidentes de Segurança"
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
  - health-safety
  - resumo-incidentes
  - indicadores
  - hns
aliases:
  - HNS_INCIDENTS_SUMMARY
  - hns_incidents_summary
  - hns-incidents-summary
  - DOC-HCM-103
  - resumo-de-incidentes-de-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INCIDENTS_SUMMARY

## 📌 Visão Geral

Armazena o **resumo consolidado de incidentes** de saúde e segurança. Fornece uma visão sumarizada com contagens, classificações e indicadores agregados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Visão consolidada:** Resumo de dados de incidentes para gestão.
- **Indicadores KPI:** Base para cálculo de taxa de frequência e gravidade.
- **Relatórios executivos:** Dados agregados para alta gestão.
- **Benchmarking:** Comparação de indicadores entre períodos e unidades.
- **Compliance:** Dados para relatórios regulatórios periódicos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCIDENT_SUMMARY_ID | NUMBER(18) | NOT NULL | PK | Identificador do resumo | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente detalhado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | SUMMARY_TEXT | VARCHAR2(4000) | NULL | Texto | Texto resumido do incidente | — | 🟡 80% |
| 4 | TOTAL_INJURED | NUMBER | NULL | Indicador | Total de pessoas lesionadas | — | 🟡 75% |
| 5 | DAYS_LOST | NUMBER | NULL | Indicador | Dias perdidos | — | 🟡 75% |
| 6 | COST_ESTIMATE | NUMBER | NULL | Financeiro | Estimativa de custo | — | 🟡 70% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (detalhe do incidente resumido)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Resumos por período
```sql
SELECT s.INCIDENT_ID, s.SUMMARY_TEXT, s.TOTAL_INJURED, s.DAYS_LOST
FROM   HNS_INCIDENTS_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Custo total por período
```sql
SELECT SUM(s.COST_ESTIMATE) AS custo_total, SUM(s.DAYS_LOST) AS dias_perdidos
FROM   HNS_INCIDENTS_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- Complementa `HNS_INCIDENTS_DETAIL` com dados sumarizados.
- `DAYS_LOST` é fundamental para cálculo de taxa de gravidade.
- `COST_ESTIMATE` permite análise financeira do impacto de incidentes.
- Um incidente pode ter um ou mais registros de resumo dependendo das atualizações.

---

## 📚 Referências

- [Oracle Docs — HNS_INCIDENTS_SUMMARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsincidentssummary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
