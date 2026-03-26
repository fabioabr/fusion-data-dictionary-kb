---
id: DOC-HCM-102
doc_type: system-doc
title: "HNS_INCIDENTS_DETAIL — Detalhes de Incidentes de Segurança"
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
  - incidentes
  - seguranca
  - hns
aliases:
  - HNS_INCIDENTS_DETAIL
  - hns_incidents_detail
  - hns-incidents-detail
  - DOC-HCM-102
  - detalhes-de-incidentes-de-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INCIDENTS_DETAIL

## 📌 Visão Geral

Armazena os **detalhes completos de incidentes** de saúde e segurança. Cada registro contém informações sobre o tipo de incidente, local, data/hora, descrição detalhada e classificação de severidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de incidentes:** Documentação completa de eventos de segurança.
- **Classificação de severidade:** Categorização por gravidade do incidente.
- **Investigação:** Base para processos de investigação de causas.
- **Compliance:** Documentação para atender requisitos regulatórios.
- **Estatísticas:** Dados para indicadores de segurança (taxa de frequência, gravidade).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCIDENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do incidente | — | 🟢 95% |
| 2 | INCIDENT_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do incidente | — | 🟢 90% |
| 3 | INCIDENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do incidente | — | 🟡 80% |
| 4 | INCIDENT_DATE | DATE | NOT NULL | Data | Data do incidente | — | 🟢 95% |
| 5 | INCIDENT_TIME | VARCHAR2(10) | NULL | Data | Hora do incidente | — | 🟡 80% |
| 6 | LOCATION_ID | NUMBER(18) | NULL | FK | Local do incidente | [[hr_locations_all]] | 🟡 80% |
| 7 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade (MINOR, MAJOR, CRITICAL, FATAL) | — | 🟡 80% |
| 8 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição detalhada | — | 🟢 90% |
| 9 | STATUS | VARCHAR2(30) | NULL | Status | Status do incidente (REPORTED, INVESTIGATING, CLOSED) | — | 🟡 80% |
| 10 | REPORTED_BY_PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que reportou | [[per_all_people_f]] | 🟡 80% |
| 11 | REPORTED_DATE | DATE | NULL | Data | Data do reporte | — | 🟡 80% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_locations_all]] — via `LOCATION_ID` (local de ocorrencia do incidente)
- [[per_all_people_f]] — via `REPORTED_BY_PERSON_ID` (pessoa que reportou o incidente)

### Tabelas-filha (FK de saída)
- [[hns_injured_persons]] — via `INCIDENT_ID` (pessoas lesionadas)
- [[hns_actions]] — via `INCIDENT_ID` (acoes corretivas do incidente)
- [[hns_investigations_summary]] — via `INCIDENT_ID` (investigacoes do incidente)
- [[hns_notes]] — via `INCIDENT_ID` (notas e observacoes do incidente)

---

## 📎 Uso Típico

### Incidentes por período
```sql
SELECT d.INCIDENT_NUMBER, d.INCIDENT_TYPE, d.INCIDENT_DATE,
       d.SEVERITY, d.STATUS
FROM   HNS_INCIDENTS_DETAIL d
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Incidentes críticos abertos
```sql
SELECT d.INCIDENT_NUMBER, d.DESCRIPTION, d.INCIDENT_DATE
FROM   HNS_INCIDENTS_DETAIL d
WHERE  d.SEVERITY IN ('CRITICAL', 'FATAL')
  AND  d.STATUS != 'CLOSED';
```

---

## 🔒 Observações

- Tabela central de incidentes — todas as outras tabelas HNS referenciam esta.
- A `SEVERITY` classifica: MINOR, MAJOR, CRITICAL, FATAL.
- O `STATUS` controla o fluxo: REPORTED -> INVESTIGATING -> CLOSED.
- Integra-se com tabelas de eventos específicos (fogo, veicular, ergonômico, etc.).

---

## 📚 Referências

- [Oracle Docs — HNS_INCIDENTS_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsincidentsdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
