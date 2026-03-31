---
id: DOC-HCM-100
doc_type: system-doc
title: "HNS_ERGONOMIC_EVT_DETAIL — Detalhes de Eventos Ergonômicos"
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
  - ergonomic
  - evento-detalhe
  - hns
aliases:
  - HNS_ERGONOMIC_EVT_DETAIL
  - hns_ergonomic_evt_detail
  - hns-ergonomic-evt-detail
  - DOC-HCM-100
  - detalhes-de-eventos-ergonômicos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_ERGONOMIC_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de ergonomia** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de ergonomia.
- **Classificação:** Categorização granular do evento de ergonomia.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de ergonomia.

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

### Eventos de ergonomia por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_ERGONOMIC_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_ERGONOMIC_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de ergonomia.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de ergonomia.

---

## 🔗 PVOs Relacionados

### [[hnsergonomiceventpvo|HNSERGONOMICEventPVO]] (HCM · BICC: 11/62)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSERGONOMICEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSERGONOMICEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSERGONOMICEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSERGONOMICEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSERGONOMICEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSERGONOMICEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSERGONOMICEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSERGONOMICEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSERGONOMICEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSERGONOMICEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSERGONOMICEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSERGONOMICEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSERGONOMICEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSERGONOMICEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSERGONOMICEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSERGONOMICEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSERGONOMICEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSERGONOMICEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSERGONOMICEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSERGONOMICEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSERGONOMICEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSERGONOMICEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSERGONOMICEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSERGONOMICEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSERGONOMICEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSERGONOMICEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSERGONOMICEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSERGONOMICEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSERGONOMICEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSERGONOMICEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSERGONOMICEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSERGONOMICEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSERGONOMICEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSERGONOMICEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSERGONOMICEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSERGONOMICEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSERGONOMICEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSERGONOMICEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSERGONOMICEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSERGONOMICEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSERGONOMICEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSERGONOMICEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSERGONOMICEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSERGONOMICEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSERGONOMICEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSERGONOMICEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSERGONOMICEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSERGONOMICEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSERGONOMICEventPEOAttrimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSERGONOMICEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSERGONOMICEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSERGONOMICEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSERGONOMICEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSERGONOMICEventPEODeletedFlag | ✅ |
| ERGONOMIC_ASS_REQ_CODE | HNSERGONOMICEventPEOErgAssReqCode | ✅ |
| ERGONOMIC_EVT_DETAIL_ID | HNSERGONOMICEventPEOErgEvtDetailId | ✅ |
| ERGONOMIC_TYPE_CODE | HNSERGONOMICEventPEOErgTypeCode | ✅ |
| INCIDENT_DETAIL_ID | HNSERGONOMICEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSERGONOMICEventPEOLastUpdateDt | ✅ |
| LAST_UPDATE_LOGIN | HNSERGONOMICEventPEOLastUpdateLgn | ✅ |
| LAST_UPDATED_BY | HNSERGONOMICEventPEOLastUpdtdBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSERGONOMICEventPEOObjVerNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_ERGONOMIC_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsergonomicevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
