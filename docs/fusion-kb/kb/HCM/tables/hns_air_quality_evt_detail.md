---
id: DOC-HCM-099
doc_type: system-doc
title: "HNS_AIR_QUALITY_EVT_DETAIL — Detalhes de Eventos de Qualidade do Ar"
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
  - air-quality
  - evento-detalhe
  - hns
aliases:
  - HNS_AIR_QUALITY_EVT_DETAIL
  - hns_air_quality_evt_detail
  - hns-air-quality-evt-detail
  - DOC-HCM-099
  - detalhes-de-eventos-de-qualidade-do-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_AIR_QUALITY_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de qualidade do ar** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de qualidade do ar.
- **Classificação:** Categorização granular do evento de qualidade do ar.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de qualidade do ar.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe do evento | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | EVENT_TYPE | VARCHAR2(30) | NULL | Classificação | Subtipo do evento | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição detalhada do evento | — | 🟡 80% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade específica | — | 🟡 75% |
| 6 | LOCATION_DETAIL | VARCHAR2(240) | NULL | Localização | Detalhes do local do evento | — | 🟡 70% |
| 7 | EVENT_DATE | DATE | NULL | Data | Data do evento | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente principal)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Eventos de qualidade do ar por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_AIR_QUALITY_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_AIR_QUALITY_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de qualidade do ar.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de qualidade do ar.

---

## 🔗 PVOs Relacionados

### [[hnsairqualityeventpvo|HNSAirQualityEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AIR_QUALITY_EVT_DETAIL_ID | HNSAirQualityEventPEOAirQualEvtDtlId | ✅ |
| AIR_QUALITY_TYPE_CODE | HNSAirQualityEventPEOAirQualTypeCd | ✅ |
| ATTRIBUTE1 | HNSAirQualityEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSAirQualityEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSAirQualityEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSAirQualityEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSAirQualityEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSAirQualityEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSAirQualityEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSAirQualityEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSAirQualityEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSAirQualityEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSAirQualityEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSAirQualityEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSAirQualityEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSAirQualityEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSAirQualityEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSAirQualityEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSAirQualityEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSAirQualityEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSAirQualityEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSAirQualityEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSAirQualityEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSAirQualityEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSAirQualityEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSAirQualityEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSAirQualityEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSAirQualityEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSAirQualityEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSAirQualityEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSAirQualityEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSAirQualityEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSAirQualityEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSAirQualityEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSAirQualityEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSAirQualityEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSAirQualityEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSAirQualityEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSAirQualityEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSAirQualityEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSAirQualityEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSAirQualityEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSAirQualityEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSAirQualityEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSAirQualityEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSAirQualityEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSAirQualityEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSAirQualityEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSAirQualityEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSAirQualityEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSAirQualityEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSAirQualityEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSAirQualityEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSAirQualityEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSAirQualityEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSAirQualityEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSAirQualityEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSAirQualityEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSAirQualityEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSAirQualityEventPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSAirQualityEventPEOObjVerNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_AIR_QUALITY_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsairqualityevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
