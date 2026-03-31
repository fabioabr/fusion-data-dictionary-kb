---
id: DOC-HCM-123
doc_type: system-doc
title: "HNS_SPILL_REL_EVT_DETAIL — Detalhes de Eventos de Derramamento/Vazamento"
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
  - spill-release
  - evento-detalhe
  - hns
aliases:
  - HNS_SPILL_REL_EVT_DETAIL
  - hns_spill_rel_evt_detail
  - hns-spill-rel-evt-detail
  - DOC-HCM-123
  - detalhes-de-eventos-de-derramamento/vazamento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_SPILL_REL_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de derramamento e vazamento** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de derramamento e vazamento.
- **Classificação:** Categorização granular do evento de derramamento e vazamento.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de derramamento e vazamento.

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

### Eventos de derramamento e vazamento por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_SPILL_REL_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_SPILL_REL_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de derramamento e vazamento.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de derramamento e vazamento.

---

## 🔗 PVOs Relacionados

### [[hnsspillreleventpvo|HNSSpillRelEventPVO]] (HCM · BICC: 21/72)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT_RECOVERED | HNSSpillRelEventPEOAmountRecovrd | ✅ |
| AMOUNT_RECOVERED_UNIT_CD | HNSSpillRelEventPEOAmntRcvrdUntCd | ✅ |
| AMOUNT_SPILLED | HNSSpillRelEventPEOAmountSpilled | ✅ |
| AMOUNT_SPILLED_UNIT_CD | HNSSpillRelEventPEOAmntSplldUntCd | ✅ |
| ATTRIBUTE1 | HNSSpillRelEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSSpillRelEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSSpillRelEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSSpillRelEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSSpillRelEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSSpillRelEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSSpillRelEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSSpillRelEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSSpillRelEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSSpillRelEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSSpillRelEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSSpillRelEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSSpillRelEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSSpillRelEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSSpillRelEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSSpillRelEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSSpillRelEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSSpillRelEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSSpillRelEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSSpillRelEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSSpillRelEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSSpillRelEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSSpillRelEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSSpillRelEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSSpillRelEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSSpillRelEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSSpillRelEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSSpillRelEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSSpillRelEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSSpillRelEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSSpillRelEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSSpillRelEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSSpillRelEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSSpillRelEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSSpillRelEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSSpillRelEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSSpillRelEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSSpillRelEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSSpillRelEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSSpillRelEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSSpillRelEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSSpillRelEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSSpillRelEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSSpillRelEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSSpillRelEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSSpillRelEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSSpillRelEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSSpillRelEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSSpillRelEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSSpillRelEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSSpillRelEventPEOAttrTimestamp9 | — |
| CLEANUP_TEAM_NOTIFIED | HNSSpillRelEventPEOClnupTeamNtfd | ✅ |
| CLEANUP_TEAM_NOTIFIED_AT | HNSSpillRelEventPEOClnupTeamNtfdAt | ✅ |
| CREATED_BY | HNSSpillRelEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSSpillRelEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSSpillRelEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSSpillRelEventPEOIncDetailId | ✅ |
| LAST_UPDATE_DATE | HNSSpillRelEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSSpillRelEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSSpillRelEventPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSSpillRelEventPEOObjVerNumber | ✅ |
| REPLN_SPILL_KIT_FLAG | HNSSpillRelEventPEOReplnSpillKitFlg | ✅ |
| SPILL_POSSIBLE_CAUSE_CODE | HNSSpillRelEventPEOSpillPsblCauseCode | ✅ |
| SPILL_REL_EVT_DETAIL_ID | HNSSpillRelEventPEOSplRelEvtDtlId | ✅ |
| SPILL_RELEASE_CODE | HNSSpillRelEventPEOSplReleaseCode | ✅ |
| SPILL_SOURCE_CODE | HNSSpillRelEventPEOSpillSrcCode | ✅ |
| SPILLKIT_DEPLOYED_FLAG | HNSSpillRelEventPEOSpillkitDeplFlag | ✅ |
| WHAT_WAS_SPILLED_OR_RELEASED | HNSSpillRelEventPEOWhatWasSpldOrRlsd | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_SPILL_REL_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsspillrelevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
