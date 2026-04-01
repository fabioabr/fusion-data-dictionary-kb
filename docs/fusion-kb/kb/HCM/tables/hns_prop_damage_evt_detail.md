---
id: DOC-HCM-122
doc_type: system-doc
title: "HNS_PROP_DAMAGE_EVT_DETAIL — Detalhes de Eventos de Danos à Propriedade"
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
  - property-damage
  - evento-detalhe
  - hns
aliases:
  - HNS_PROP_DAMAGE_EVT_DETAIL
  - hns_prop_damage_evt_detail
  - hns-prop-damage-evt-detail
  - DOC-HCM-122
  - detalhes-de-eventos-de-danos-à-propriedade
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_PROP_DAMAGE_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de danos à propriedade** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de danos à propriedade.
- **Classificação:** Categorização granular do evento de danos à propriedade.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de danos à propriedade.

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

### Eventos de danos à propriedade por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_PROP_DAMAGE_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_PROP_DAMAGE_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de danos à propriedade.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de danos à propriedade.

---

## 🔗 PVOs Relacionados

### [[hnspropdamageeventpvo|HNSPropDamageEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSPropDamageEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSPropDamageEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSPropDamageEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSPropDamageEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSPropDamageEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSPropDamageEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSPropDamageEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSPropDamageEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSPropDamageEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSPropDamageEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSPropDamageEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSPropDamageEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSPropDamageEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSPropDamageEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSPropDamageEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSPropDamageEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSPropDamageEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSPropDamageEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSPropDamageEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSPropDamageEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSPropDamageEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSPropDamageEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSPropDamageEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSPropDamageEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSPropDamageEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSPropDamageEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSPropDamageEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSPropDamageEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSPropDamageEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSPropDamageEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSPropDamageEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSPropDamageEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSPropDamageEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSPropDamageEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSPropDamageEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSPropDamageEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSPropDamageEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSPropDamageEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSPropDamageEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSPropDamageEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSPropDamageEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSPropDamageEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSPropDamageEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSPropDamageEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSPropDamageEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSPropDamageEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSPropDamageEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSPropDamageEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSPropDamageEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSPropDamageEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSPropDamageEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSPropDamageEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSPropDamageEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSPropDamageEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSPropDamageEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSPropDamageEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSPropDamageEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSPropDamageEventPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSPropDamageEventPEOObjVerNumber | ✅ |
| PROP_DAMAGE_EVT_DETAIL_ID | HNSPropDamageEventPEOPropDmgEvtDtlId | ✅ |
| PROPERTY_DAMAGE_CODE | HNSPropDamageEventPEOPropDamageCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_PROP_DAMAGE_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnspropdamageevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
