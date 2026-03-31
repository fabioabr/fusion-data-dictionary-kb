---
id: DOC-HCM-106
doc_type: system-doc
title: "HNS_INJURED_PERSONS_SUMMARY — Resumo de Pessoas Lesionadas"
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
  - resumo-lesionados
  - indicadores
  - hns
aliases:
  - HNS_INJURED_PERSONS_SUMMARY
  - hns_injured_persons_summary
  - hns-injured-persons-summary
  - DOC-HCM-106
  - resumo-de-pessoas-lesionadas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INJURED_PERSONS_SUMMARY

## 📌 Visão Geral

Armazena o **resumo consolidado** das informações de pessoas lesionadas em incidentes, com dados agregados e classificações para relatórios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Resumo de lesionados:** Visão consolidada por incidente.
- **Relatórios regulatórios:** Dados agregados para OSHA/NRs.
- **KPIs de segurança:** Indicadores de pessoas afetadas.
- **Análise gerencial:** Dados sumarizados para decisores.
- **Compliance:** Documentação para auditorias.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INJURED_PERSON_SUMMARY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | INJURED_PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa lesionada | [[hns_injured_persons]] | 🟡 80% |
| 3 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente | [[hns_incidents_detail]] | 🟢 90% |
| 4 | OUTCOME | VARCHAR2(30) | NULL | Classificação | Resultado (RECOVERED, PERMANENT_DISABILITY, FATALITY) | — | 🟡 75% |
| 5 | RETURN_TO_WORK_DATE | DATE | NULL | Data | Data de retorno ao trabalho | — | 🟡 75% |
| 6 | TOTAL_DAYS_AWAY | NUMBER | NULL | Indicador | Total de dias de afastamento | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_injured_persons]] — via `INJURED_PERSON_ID` (pessoa acidentada do resumo)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente do resumo de acidentado)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Resumo por incidente
```sql
SELECT s.OUTCOME, s.RETURN_TO_WORK_DATE, s.TOTAL_DAYS_AWAY
FROM   HNS_INJURED_PERSONS_SUMMARY s
WHERE  s.INCIDENT_ID = :p_incident_id;
```

### Fatalidades no período
```sql
SELECT s.INJURED_PERSON_ID, s.INCIDENT_ID
FROM   HNS_INJURED_PERSONS_SUMMARY s
JOIN   HNS_INCIDENTS_DETAIL d ON s.INCIDENT_ID = d.INCIDENT_ID
WHERE  s.OUTCOME = 'FATALITY'
  AND  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- O `OUTCOME` classifica o resultado final: RECOVERED, PERMANENT_DISABILITY, FATALITY.
- O `RETURN_TO_WORK_DATE` é essencial para cálculo de dias perdidos.
- Complementa `HNS_INJURED_PERSONS` com dados de acompanhamento.
- Dados são input para relatórios anuais de segurança (PPRA, PCMSO).

---

## 🔗 PVOs Relacionados

### [[hnsinjuredpersonspvo|HNSInjuredPersonsPVO]] (HCM · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | HNSInjuredPersonSummaryPEOCreatedBy | — |
| CREATION_DATE | HNSInjuredPersonSummaryPEOCreationDate | — |
| DATE_TIME_NOTIFIED | HNSInjuredPersonSummaryPEODtTmNtfd | ✅ |
| DELETED_FLAG | HNSInjuredPersonSummaryPEODeletedFlag | ✅ |
| HR_NOTIFIED_FLAG | HNSInjuredPersonSummaryPEOHrNtfdFlg | ✅ |
| INCIDENT_DETAIL_ID | HNSInjuredPersonSummaryPEOIncDtlId | — |
| INJ_PERSON_SUMMARY_ID | HNSInjuredPersonSummaryPEOInjPerSumId | ✅ |
| LAST_UPDATE_DATE | HNSInjuredPersonSummaryPEOLstUpdtDt | — |
| LAST_UPDATE_LOGIN | HNSInjuredPersonSummaryPEOLstUpdtLgn | — |
| LAST_UPDATED_BY | HNSInjuredPersonSummaryPEOLstUpdtdBy | — |
| OBJECT_VERSION_NUMBER | HNSInjuredPersonSummaryPEOObjVersNum | — |

---

## 📚 Referências

- [Oracle Docs — HNS_INJURED_PERSONS_SUMMARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinjuredpersonssummary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
