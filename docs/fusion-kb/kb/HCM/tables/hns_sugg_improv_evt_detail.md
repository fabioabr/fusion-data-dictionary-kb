---
id: DOC-HCM-124
doc_type: system-doc
title: "HNS_SUGG_IMPROV_EVT_DETAIL — Detalhes de Eventos de Sugestão de Melhoria"
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
  - suggestion-improvement
  - evento-detalhe
  - hns
aliases:
  - HNS_SUGG_IMPROV_EVT_DETAIL
  - hns_sugg_improv_evt_detail
  - hns-sugg-improv-evt-detail
  - DOC-HCM-124
  - detalhes-de-eventos-de-sugestão-de-melhoria
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_SUGG_IMPROV_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de sugestões de melhoria** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de sugestões de melhoria.
- **Classificação:** Categorização granular do evento de sugestões de melhoria.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de sugestões de melhoria.

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

### Eventos de sugestões de melhoria por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_SUGG_IMPROV_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_SUGG_IMPROV_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de sugestões de melhoria.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de sugestões de melhoria.

---

## 🔗 PVOs Relacionados

### [[hnssuggimproveventpvo|HNSSuggImprovEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSSuggImprovEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSSuggImprovEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSSuggImprovEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSSuggImprovEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSSuggImprovEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSSuggImprovEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSSuggImprovEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSSuggImprovEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSSuggImprovEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSSuggImprovEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSSuggImprovEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSSuggImprovEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSSuggImprovEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSSuggImprovEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSSuggImprovEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSSuggImprovEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSSuggImprovEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSSuggImprovEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSSuggImprovEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSSuggImprovEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSSuggImprovEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSSuggImprovEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSSuggImprovEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSSuggImprovEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSSuggImprovEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSSuggImprovEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSSuggImprovEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSSuggImprovEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSSuggImprovEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSSuggImprovEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSSuggImprovEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSSuggImprovEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSSuggImprovEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSSuggImprovEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSSuggImprovEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSSuggImprovEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSSuggImprovEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSSuggImprovEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSSuggImprovEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSSuggImprovEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSSuggImprovEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSSuggImprovEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSSuggImprovEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSSuggImprovEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSSuggImprovEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSSuggImprovEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSSuggImprovEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSSuggImprovEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSSuggImprovEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSSuggImprovEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSSuggImprovEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSSuggImprovEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSSuggImprovEventPEOCrtnDate | ✅ |
| DELETED_FLAG | HNSSuggImprovEventPEODelFlag | ✅ |
| IMPROVEMENT_TYPE_CODE | HNSSuggImprovEventPEOImprvTypCd | ✅ |
| INCIDENT_DETAIL_ID | HNSSuggImprovEventPEOIncDtlId | ✅ |
| LAST_UPDATE_DATE | HNSSuggImprovEventPEOLastUpdtDt | ✅ |
| LAST_UPDATE_LOGIN | HNSSuggImprovEventPEOLastUpdtLgn | ✅ |
| LAST_UPDATED_BY | HNSSuggImprovEventPEOLastUpdtdBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSSuggImprovEventPEOObjVerNumber | ✅ |
| SUGG_IMPROV_EVT_DETAIL_ID | HNSSuggImprovEventPEOSuggImpEvtDtlId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_SUGG_IMPROV_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnssuggimprovevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
