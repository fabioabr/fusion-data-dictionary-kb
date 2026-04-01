---
id: DOC-HCM-126
doc_type: system-doc
title: "HNS_UNSAFE_COND_EVT_DETAIL — Detalhes de Eventos de Condição Insegura"
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
  - unsafe-condition
  - evento-detalhe
  - hns
aliases:
  - HNS_UNSAFE_COND_EVT_DETAIL
  - hns_unsafe_cond_evt_detail
  - hns-unsafe-cond-evt-detail
  - DOC-HCM-126
  - detalhes-de-eventos-de-condição-insegura
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_UNSAFE_COND_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de condições inseguras** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de condições inseguras.
- **Classificação:** Categorização granular do evento de condições inseguras.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de condições inseguras.

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

### Eventos de condições inseguras por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_UNSAFE_COND_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_UNSAFE_COND_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de condições inseguras.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de condições inseguras.

---

## 🔗 PVOs Relacionados

### [[hnsunsafecondeventpvo|HNSUnsafeCondEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSUnsafeCondEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSUnsafeCondEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSUnsafeCondEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSUnsafeCondEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSUnsafeCondEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSUnsafeCondEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSUnsafeCondEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSUnsafeCondEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSUnsafeCondEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSUnsafeCondEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSUnsafeCondEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSUnsafeCondEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSUnsafeCondEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSUnsafeCondEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSUnsafeCondEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSUnsafeCondEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSUnsafeCondEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSUnsafeCondEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSUnsafeCondEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSUnsafeCondEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSUnsafeCondEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSUnsafeCondEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSUnsafeCondEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSUnsafeCondEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSUnsafeCondEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSUnsafeCondEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSUnsafeCondEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSUnsafeCondEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSUnsafeCondEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSUnsafeCondEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSUnsafeCondEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSUnsafeCondEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSUnsafeCondEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSUnsafeCondEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSUnsafeCondEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSUnsafeCondEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSUnsafeCondEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSUnsafeCondEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSUnsafeCondEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSUnsafeCondEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSUnsafeCondEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSUnsafeCondEventPEOAttrTimstmp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSUnsafeCondEventPEOAttrTimstmp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSUnsafeCondEventPEOAttrTimstmp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSUnsafeCondEventPEOAttrTimstmp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSUnsafeCondEventPEOAttrTimstmp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSUnsafeCondEventPEOAttrTimstmp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSUnsafeCondEventPEOAttrTimstmp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSUnsafeCondEventPEOAttrTimstmp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSUnsafeCondEventPEOAttrTimstmp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSUnsafeCondEventPEOAttrTimstmp9 | — |
| CREATED_BY | HNSUnsafeCondEventPEOCrtdBy | ✅ |
| CREATION_DATE | HNSUnsafeCondEventPEOCrtnDt | ✅ |
| DELETED_FLAG | HNSUnsafeCondEventPEODelFlg | ✅ |
| INCIDENT_DETAIL_ID | HNSUnsafeCondEventPEOIncDtlId | ✅ |
| LAST_UPDATE_DATE | HNSUnsafeCondEventPEOLstUpdtDt | ✅ |
| LAST_UPDATE_LOGIN | HNSUnsafeCondEventPEOLstUpdtLgn | ✅ |
| LAST_UPDATED_BY | HNSUnsafeCondEventPEOLstUpdtdBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSUnsafeCondEventPEOObjVerNum | ✅ |
| UNSAFE_COND_EVT_DETAIL_ID | HNSUnsafeCondEventPEOUnsfCondEvtDetId | ✅ |
| UNSAFE_CONDITION_CODE | HNSUnsafeCondEventPEOUnsafeCondCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_UNSAFE_COND_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsunsafecondevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
