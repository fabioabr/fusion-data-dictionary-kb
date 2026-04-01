---
id: DOC-HCM-125
doc_type: system-doc
title: "HNS_UNSAFE_ACT_EVT_DETAIL — Detalhes de Eventos de Ato Inseguro"
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
  - unsafe-act
  - evento-detalhe
  - hns
aliases:
  - HNS_UNSAFE_ACT_EVT_DETAIL
  - hns_unsafe_act_evt_detail
  - hns-unsafe-act-evt-detail
  - DOC-HCM-125
  - detalhes-de-eventos-de-ato-inseguro
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_UNSAFE_ACT_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de atos inseguros** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de atos inseguros.
- **Classificação:** Categorização granular do evento de atos inseguros.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de atos inseguros.

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

### Eventos de atos inseguros por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_UNSAFE_ACT_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_UNSAFE_ACT_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de atos inseguros.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de atos inseguros.

---

## 🔗 PVOs Relacionados

### [[hnsunsafeacteventpvo|HNSUnsafeActEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSUnsafeActEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSUnsafeActEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSUnsafeActEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSUnsafeActEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSUnsafeActEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSUnsafeActEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSUnsafeActEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSUnsafeActEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSUnsafeActEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSUnsafeActEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSUnsafeActEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSUnsafeActEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSUnsafeActEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSUnsafeActEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSUnsafeActEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSUnsafeActEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSUnsafeActEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSUnsafeActEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSUnsafeActEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSUnsafeActEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSUnsafeActEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSUnsafeActEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSUnsafeActEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSUnsafeActEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSUnsafeActEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSUnsafeActEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSUnsafeActEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSUnsafeActEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSUnsafeActEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSUnsafeActEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSUnsafeActEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSUnsafeActEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSUnsafeActEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSUnsafeActEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSUnsafeActEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSUnsafeActEventPEOAttrumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSUnsafeActEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSUnsafeActEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSUnsafeActEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSUnsafeActEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSUnsafeActEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSUnsafeActEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSUnsafeActEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSUnsafeActEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSUnsafeActEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSUnsafeActEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSUnsafeActEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSUnsafeActEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSUnsafeActEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSUnsafeActEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSUnsafeActEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSUnsafeActEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSUnsafeActEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSUnsafeActEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSUnsafeActEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSUnsafeActEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSUnsafeActEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSUnsafeActEventPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSUnsafeActEventPEOObjVerNumber | ✅ |
| UNSAFE_ACT_EVT_DETAIL_ID | HNSUnsafeActEventPEOUnsafActEvtDtlId | ✅ |
| UNSAFE_ACT_TYPE_CODE | HNSUnsafeActEventPEOUnsafeActTypeCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_UNSAFE_ACT_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsunsafeactevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
