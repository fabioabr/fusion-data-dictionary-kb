---
id: DOC-HCM-104
doc_type: system-doc
title: "HNS_INCIDENT_AGENCIES_DTL — Detalhes de Agências em Incidentes"
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
  - agencias
  - compliance
  - hns
aliases:
  - HNS_INCIDENT_AGENCIES_DTL
  - hns_incident_agencies_dtl
  - hns-incident-agencies-dtl
  - DOC-HCM-104
  - detalhes-de-agências-em-incidentes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INCIDENT_AGENCIES_DTL

## 📌 Visão Geral

Armazena os **detalhes das agências reguladoras** ou externas envolvidas em incidentes de saúde e segurança — órgãos de fiscalização, bombeiros, defesa civil, etc.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de agências:** Documentação de órgãos envolvidos no incidente.
- **Compliance regulatório:** Rastreamento de notificações a órgãos competentes.
- **Acompanhamento:** Status de interação com cada agência.
- **Auditoria:** Documentação para fins legais e regulatórios.
- **Relatórios:** Análise de envolvimento de agências por tipo de incidente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCIDENT_AGENCY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | AGENCY_NAME | VARCHAR2(240) | NULL | Identificação | Nome da agência | — | 🟡 80% |
| 4 | AGENCY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da agência (REGULATORY, EMERGENCY, INSURANCE) | — | 🟡 75% |
| 5 | NOTIFICATION_DATE | DATE | NULL | Data | Data de notificação à agência | — | 🟡 75% |
| 6 | REFERENCE_NUMBER | VARCHAR2(100) | NULL | Identificação | Número de referência/protocolo | — | 🟡 70% |
| 7 | STATUS | VARCHAR2(30) | NULL | Status | Status da interação | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente reportado a agencia)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Agências por incidente
```sql
SELECT a.AGENCY_NAME, a.AGENCY_TYPE, a.NOTIFICATION_DATE, a.STATUS
FROM   HNS_INCIDENT_AGENCIES_DTL a
WHERE  a.INCIDENT_ID = :p_incident_id;
```

### Incidentes com notificação regulatória
```sql
SELECT a.INCIDENT_ID, a.AGENCY_NAME, a.REFERENCE_NUMBER
FROM   HNS_INCIDENT_AGENCIES_DTL a
WHERE  a.AGENCY_TYPE = 'REGULATORY';
```

---

## 🔒 Observações

- Cada incidente pode envolver múltiplas agências.
- O `NOTIFICATION_DATE` é crucial para compliance — muitas regulamentações exigem notificação em prazo.
- O `REFERENCE_NUMBER` armazena protocolos de órgãos externos.
- Tipos típicos: REGULATORY (fiscalização), EMERGENCY (bombeiros, SAMU), INSURANCE (seguradoras).

---

## 📚 Referências

- [Oracle Docs — HNS_INCIDENT_AGENCIES_DTL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsincidentagenciesdtl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
