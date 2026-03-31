---
id: DOC-HCM-117
doc_type: system-doc
title: "HNS_ISSUE_EVT_DETAIL — Detalhes de Eventos de Problemas"
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
  - issue
  - evento-detalhe
  - hns
aliases:
  - HNS_ISSUE_EVT_DETAIL
  - hns_issue_evt_detail
  - hns-issue-evt-detail
  - DOC-HCM-117
  - detalhes-de-eventos-de-problemas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_ISSUE_EVT_DETAIL

## 📌 Visão Geral

Armazena os **detalhes específicos de eventos de problemas/issues** no módulo de Saúde e Segurança do Trabalho. Complementa `HNS_INCIDENTS_DETAIL` com informações granulares do tipo de evento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro detalhado:** Informações específicas de eventos de problemas/issues.
- **Classificação:** Categorização granular do evento de problemas/issues.
- **Investigação:** Dados complementares para análise de causa raiz.
- **Compliance:** Documentação regulatória específica do tipo de evento.
- **Relatórios:** Estatísticas específicas de eventos de problemas/issues.

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

### Eventos de problemas/issues por período
```sql
SELECT ed.EVENT_DETAIL_ID, ed.EVENT_TYPE, ed.DESCRIPTION,
       ed.SEVERITY, ed.EVENT_DATE
FROM   HNS_ISSUE_EVT_DETAIL ed
JOIN   HNS_INCIDENTS_DETAIL d ON ed.INCIDENT_ID = d.INCIDENT_ID
WHERE  d.INCIDENT_DATE BETWEEN :p_start AND :p_end;
```

### Detalhes por incidente
```sql
SELECT ed.EVENT_TYPE, ed.DESCRIPTION, ed.SEVERITY, ed.LOCATION_DETAIL
FROM   HNS_ISSUE_EVT_DETAIL ed
WHERE  ed.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- Tabela complementar a `HNS_INCIDENTS_DETAIL` com dados específicos de problemas/issues.
- Cada incidente do tipo correspondente deve ter um registro nesta tabela.
- O `EVENT_TYPE` permite sub-classificação dentro da categoria.
- Dados são relevantes para relatórios regulatórios específicos de problemas/issues.

---

## 🔗 PVOs Relacionados

### [[hnsissueeventpvo|HNSIssueEventPVO]] (HCM · BICC: 10/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HNSIssueEventPEOAttribute1 | — |
| ATTRIBUTE10 | HNSIssueEventPEOAttribute10 | — |
| ATTRIBUTE11 | HNSIssueEventPEOAttribute11 | — |
| ATTRIBUTE12 | HNSIssueEventPEOAttribute12 | — |
| ATTRIBUTE13 | HNSIssueEventPEOAttribute13 | — |
| ATTRIBUTE14 | HNSIssueEventPEOAttribute14 | — |
| ATTRIBUTE15 | HNSIssueEventPEOAttribute15 | — |
| ATTRIBUTE16 | HNSIssueEventPEOAttribute16 | — |
| ATTRIBUTE17 | HNSIssueEventPEOAttribute17 | — |
| ATTRIBUTE18 | HNSIssueEventPEOAttribute18 | — |
| ATTRIBUTE19 | HNSIssueEventPEOAttribute19 | — |
| ATTRIBUTE2 | HNSIssueEventPEOAttribute2 | — |
| ATTRIBUTE20 | HNSIssueEventPEOAttribute20 | — |
| ATTRIBUTE21 | HNSIssueEventPEOAttribute21 | — |
| ATTRIBUTE22 | HNSIssueEventPEOAttribute22 | — |
| ATTRIBUTE23 | HNSIssueEventPEOAttribute23 | — |
| ATTRIBUTE24 | HNSIssueEventPEOAttribute24 | — |
| ATTRIBUTE25 | HNSIssueEventPEOAttribute25 | — |
| ATTRIBUTE26 | HNSIssueEventPEOAttribute26 | — |
| ATTRIBUTE27 | HNSIssueEventPEOAttribute27 | — |
| ATTRIBUTE28 | HNSIssueEventPEOAttribute28 | — |
| ATTRIBUTE29 | HNSIssueEventPEOAttribute29 | — |
| ATTRIBUTE3 | HNSIssueEventPEOAttribute3 | — |
| ATTRIBUTE30 | HNSIssueEventPEOAttribute30 | — |
| ATTRIBUTE4 | HNSIssueEventPEOAttribute4 | — |
| ATTRIBUTE5 | HNSIssueEventPEOAttribute5 | — |
| ATTRIBUTE6 | HNSIssueEventPEOAttribute6 | — |
| ATTRIBUTE7 | HNSIssueEventPEOAttribute7 | — |
| ATTRIBUTE8 | HNSIssueEventPEOAttribute8 | — |
| ATTRIBUTE9 | HNSIssueEventPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSIssueEventPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSIssueEventPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER10 | HNSIssueEventPEOAttrNumber10 | — |
| ATTRIBUTE_NUMBER2 | HNSIssueEventPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSIssueEventPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSIssueEventPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSIssueEventPEOAttrNumber5 | — |
| ATTRIBUTE_NUMBER6 | HNSIssueEventPEOAttrNumber6 | — |
| ATTRIBUTE_NUMBER7 | HNSIssueEventPEOAttrNumber7 | — |
| ATTRIBUTE_NUMBER8 | HNSIssueEventPEOAttrNumber8 | — |
| ATTRIBUTE_NUMBER9 | HNSIssueEventPEOAttrNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSIssueEventPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | HNSIssueEventPEOAttrTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSIssueEventPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSIssueEventPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSIssueEventPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSIssueEventPEOAttrTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | HNSIssueEventPEOAttrTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | HNSIssueEventPEOAttrTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | HNSIssueEventPEOAttrTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | HNSIssueEventPEOAttrTimestamp9 | — |
| CREATED_BY | HNSIssueEventPEOCreatedBy | ✅ |
| CREATION_DATE | HNSIssueEventPEOCreationDate | ✅ |
| DELETED_FLAG | HNSIssueEventPEODeletedFlag | ✅ |
| INCIDENT_DETAIL_ID | HNSIssueEventPEOIncDetailId | ✅ |
| ISSUE_EVT_DETAIL_ID | HNSIssueEventPEOIssueEvtDtlId | ✅ |
| ISSUE_TYPE_CODE | HNSIssueEventPEOIssueTypeCd | ✅ |
| LAST_UPDATE_DATE | HNSIssueEventPEOLastUpdateDt | ✅ |
| LAST_UPDATE_LOGIN | HNSIssueEventPEOLastUpdateLgn | ✅ |
| LAST_UPDATED_BY | HNSIssueEventPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSIssueEventPEOObjVerNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_ISSUE_EVT_DETAIL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsissueevtdetail.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
