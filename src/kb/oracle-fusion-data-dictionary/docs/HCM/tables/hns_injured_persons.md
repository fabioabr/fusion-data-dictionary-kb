---
id: DOC-HCM-105
doc_type: system-doc
title: "HNS_INJURED_PERSONS — Pessoas Lesionadas em Incidentes"
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
  - lesionados
  - acidente-trabalho
  - hns
aliases:
  - HNS_INJURED_PERSONS
  - hns_injured_persons
  - hns-injured-persons
  - DOC-HCM-105
  - pessoas-lesionadas-em-incidentes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INJURED_PERSONS

## 📌 Visão Geral

Armazena os **dados das pessoas lesionadas** em incidentes de saúde e segurança, incluindo tipo de lesão, parte do corpo afetada e severidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de lesões:** Documentação de todas as pessoas lesionadas.
- **Classificação de lesões:** Tipo e severidade da lesão.
- **CAT (Comunicação de Acidente de Trabalho):** Base para emissão da CAT.
- **Relatórios OSHA/NR:** Dados para relatórios regulatórios.
- **Análise estatística:** Indicadores de segurança por tipo de lesão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INJURED_PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 95% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa lesionada | [[per_all_people_f]] | 🟢 90% |
| 4 | INJURY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da lesão | — | 🟡 80% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade da lesão | — | 🟡 80% |
| 6 | BODY_PART | VARCHAR2(30) | NULL | Classificação | Parte do corpo afetada | — | 🟡 75% |
| 7 | TREATMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de tratamento (FIRST_AID, HOSPITAL, SURGERY) | — | 🟡 75% |
| 8 | DAYS_AWAY | NUMBER | NULL | Indicador | Dias de afastamento | — | 🟡 75% |
| 9 | HOSPITALIZED_FLAG | VARCHAR2(1) | NULL | Indicador | Indica se foi hospitalizado (Y/N) | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente da pessoa acidentada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa lesionada)

### Tabelas-filha (FK de saída)
- [[hns_injured_person_parts]] — via `INJURED_PERSON_ID` (partes do corpo detalhadas)
- [[hns_injured_persons_summary]] — via `INJURED_PERSON_ID` (resumo da pessoa acidentada)

---

## 📎 Uso Típico

### Lesionados por incidente
```sql
SELECT ip.PERSON_ID, ip.INJURY_TYPE, ip.SEVERITY,
       ip.BODY_PART, ip.DAYS_AWAY
FROM   HNS_INJURED_PERSONS ip
WHERE  ip.INCIDENT_ID = :p_incident_id;
```

### Total de dias perdidos
```sql
SELECT SUM(ip.DAYS_AWAY) AS total_dias, COUNT(*) AS total_lesionados
FROM   HNS_INJURED_PERSONS ip
JOIN   HNS_INCIDENTS_DETAIL d ON ip.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

---

## 🔒 Observações

- `DAYS_AWAY` é central para cálculo da taxa de gravidade (TG).
- O `TREATMENT_TYPE` indica o nível de atendimento necessário.
- Cada incidente pode ter múltiplas pessoas lesionadas.
- Dados são base para emissão da CAT no Brasil (Comunicação de Acidente de Trabalho).

---

## 📚 Referências

- [Oracle Docs — HNS_INJURED_PERSONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinjuredpersons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
