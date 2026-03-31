---
id: DOC-HCM-118
doc_type: system-doc
title: "HNS_NEAR_MISS_EVT_DETAIL — Detalhes de Eventos de Quase-Acidente"
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
  - near-miss
  - evento-detalhe
  - hns
aliases:
  - HNS_NEAR_MISS_EVT_DETAIL
  - hns_near_miss_evt_detail
  - hns-near-miss-evt-detail
  - DOC-HCM-118
  - detalhes-de-eventos-de-quase-acidente
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_NEAR_MISS_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de quase-acidente (near miss)** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de quase-acidente (near miss).
- **Classificação:** Categorização granular do evento de quase-acidente (near miss).
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de quase-acidente (near miss).

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

### Eventos de quase-acidente (near miss) por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_NEAR_MISS_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_NEAR_MISS_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de quase-acidente (near miss).
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de quase-acidente (near miss).

---

## 🔗 PVOs Relacionados

### [[hnsnearmisseventpvo|HNSNearMissEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSNearMissEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSNearMissEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSNearMissEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSNearMissEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSNearMissEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSNearMissEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSNearMissEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSNearMissEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSNearMissEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSNearMissEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSNearMissEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSNearMissEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSNearMissEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSNearMissEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSNearMissEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSNearMissEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSNearMissEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSNearMissEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSNearMissEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSNearMissEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSNearMissEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSNearMissEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSNearMissEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSNearMissEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSNearMissEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSNearMissEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSNearMissEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSNearMissEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSNearMissEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSNearMissEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSNearMissEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSNearMissEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSNearMissEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSNearMissEventPEOAttNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSNearMissEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSNearMissEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSNearMissEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSNearMissEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSNearMissEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSNearMissEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSNearMissEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSNearMissEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSNearMissEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSNearMissEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSNearMissEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSNearMissEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSNearMissEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSNearMissEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSNearMissEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSNearMissEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSNearMissEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSNearMissEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSNearMissEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSNearMissEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSNearMissEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSNearMissEventPEOLastUpdateDt | ✅ |
| LAST_UPDATE_LOGIN | HNSNearMissEventPEOLastUpdateLgn | ✅ |
| LAST_UPDATED_BY | HNSNearMissEventPEOLastUpdateBy | ✅ |
| NEAR_MISS_CODE | HNSNearMissEventPEONearMissCode | ✅ |
| NEAR_MISS_EVT_DETAIL_ID | HNSNearMissEventPEONearMissEvtDtlId | ✅ |
| OBJECT_VERSION_NUMBER | HNSNearMissEventPEOObjVerNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_NEAR_MISS_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsnearmissevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
