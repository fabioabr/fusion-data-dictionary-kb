---
id: DOC-PO-139
doc_type: system-doc
title: "PO_NOTIFICATION_CONTROLS — Controles de Notificacao de Compras"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - notificacoes
  - workflow
  - alertas
aliases:
  - PO_NOTIFICATION_CONTROLS
  - po_notification_controls
  - po-notification-controls
  - po-notification
  - controles-de-notificacao-de-compras
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_NOTIFICATION_CONTROLS

## 📌 Visão Geral

Armazena as **regras de controle de notificacoes** do modulo Procurement.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Notificacoes automaticas:** Regras de envio de alertas.
- **Escalacao:** Notificacoes para POs pendentes.
- **Controle de prazo:** Alertas de vencimento.
- **Personalizacao:** Regras por organizacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | NOTIFICATION_ID | NUMBER(18) | NOT NULL | PK | ID da regra | — | 🟡 75% |
| 2 | DOCUMENT_TYPE | VARCHAR2(25) | NULL | Classificacao | PO, PA, REQ | — | 🟡 75% |
| 3 | NOTIFICATION_TYPE | VARCHAR2(25) | NULL | Classificacao | Tipo de notificacao | — | 🟡 70% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟡 75% |
| 5 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do controle de notificação de compras)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Notificacoes habilitadas
```sql
SELECT NOTIFICATION_ID, DOCUMENT_TYPE, NOTIFICATION_TYPE
FROM   PO_NOTIFICATION_CONTROLS
WHERE  ENABLED_FLAG = 'Y' AND ORG_ID = :p_org_id;
```

---

## 🔒 Observações

- Tabela de configuracao.
- Notificacoes via Oracle Workflow.
- Regras diferentes por organizacao.

---

## 🔗 PVOs Relacionados

### [[purchasingagreementnotificationcontrolextractpvo|PurchasingAgreementNotificationControlExtractPVO]] (PO · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NOTIFICATION_AMOUNT | NotificationAmount | ✅ |
| NOTIFICATION_CONDITION_CODE | NotificationConditionCode | ✅ |
| NOTIFICATION_ID | NotificationId | ✅ |
| NOTIFICATION_QTY_PERCENTAGE | NotificationQtyPercentage | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |

### [[purchasingagreementnotificationcontrolpvo|PurchasingAgreementNotificationControlPVO]] (PO · BICC: 11/68)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | AgreementNotificationControlAttribute1 | — |
| ATTRIBUTE10 | AgreementNotificationControlAttribute10 | — |
| ATTRIBUTE11 | AgreementNotificationControlAttribute11 | — |
| ATTRIBUTE12 | AgreementNotificationControlAttribute12 | — |
| ATTRIBUTE13 | AgreementNotificationControlAttribute13 | — |
| ATTRIBUTE14 | AgreementNotificationControlAttribute14 | — |
| ATTRIBUTE15 | AgreementNotificationControlAttribute15 | — |
| ATTRIBUTE16 | AgreementNotificationControlAttribute16 | — |
| ATTRIBUTE17 | AgreementNotificationControlAttribute17 | — |
| ATTRIBUTE18 | AgreementNotificationControlAttribute18 | — |
| ATTRIBUTE19 | AgreementNotificationControlAttribute19 | — |
| ATTRIBUTE2 | AgreementNotificationControlAttribute2 | — |
| ATTRIBUTE20 | AgreementNotificationControlAttribute20 | — |
| ATTRIBUTE3 | AgreementNotificationControlAttribute3 | — |
| ATTRIBUTE4 | AgreementNotificationControlAttribute4 | — |
| ATTRIBUTE5 | AgreementNotificationControlAttribute5 | — |
| ATTRIBUTE6 | AgreementNotificationControlAttribute6 | — |
| ATTRIBUTE7 | AgreementNotificationControlAttribute7 | — |
| ATTRIBUTE8 | AgreementNotificationControlAttribute8 | — |
| ATTRIBUTE9 | AgreementNotificationControlAttribute9 | — |
| ATTRIBUTE_CATEGORY | AgreementNotificationControlAttributeCategory | — |
| ATTRIBUTE_DATE1 | AgreementNotificationControlAttributeDate1 | — |
| ATTRIBUTE_DATE10 | AgreementNotificationControlAttributeDate10 | — |
| ATTRIBUTE_DATE2 | AgreementNotificationControlAttributeDate2 | — |
| ATTRIBUTE_DATE3 | AgreementNotificationControlAttributeDate3 | — |
| ATTRIBUTE_DATE4 | AgreementNotificationControlAttributeDate4 | — |
| ATTRIBUTE_DATE5 | AgreementNotificationControlAttributeDate5 | — |
| ATTRIBUTE_DATE6 | AgreementNotificationControlAttributeDate6 | — |
| ATTRIBUTE_DATE7 | AgreementNotificationControlAttributeDate7 | — |
| ATTRIBUTE_DATE8 | AgreementNotificationControlAttributeDate8 | — |
| ATTRIBUTE_DATE9 | AgreementNotificationControlAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AgreementNotificationControlAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AgreementNotificationControlAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AgreementNotificationControlAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AgreementNotificationControlAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AgreementNotificationControlAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AgreementNotificationControlAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AgreementNotificationControlAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AgreementNotificationControlAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AgreementNotificationControlAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AgreementNotificationControlAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AgreementNotificationControlAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AgreementNotificationControlAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AgreementNotificationControlAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AgreementNotificationControlAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AgreementNotificationControlAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AgreementNotificationControlAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AgreementNotificationControlAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AgreementNotificationControlAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AgreementNotificationControlAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AgreementNotificationControlAttributeTimestamp9 | — |
| CREATED_BY | AgreementNotificationControlCreatedBy | — |
| CREATION_DATE | AgreementNotificationControlCreationDate | — |
| END_DATE_ACTIVE | AgreementNotificationControlEndDateActive | ✅ |
| END_DATE_ACTIVE | AgreementNotificationControlEndDateActiveContract | ✅ |
| LAST_UPDATE_DATE | AgreementNotificationControlLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AgreementNotificationControlLastUpdateLogin | — |
| LAST_UPDATED_BY | AgreementNotificationControlLastUpdatedBy | — |
| NOTIFICATION_AMOUNT | AgreementNotificationControlNotificationAmount | ✅ |
| NOTIFICATION_CONDITION_CODE | AgreementNotificationControlNotificationConditionCode | ✅ |
| NOTIFICATION_CONDITION_CODE | AgreementNotificationControlNotificationConditionCodeContract | ✅ |
| NOTIFICATION_ID | AgreementNotificationControlNotificationId | ✅ |
| NOTIFICATION_QTY_PERCENTAGE | AgreementNotificationControlNotificationQtyPercentage | ✅ |
| NOTIFICATION_QTY_PERCENTAGE | AgreementNotificationControlNotificationQtyPercentageContract | ✅ |
| OBJECT_VERSION_NUMBER | AgreementNotificationControlObjectVersionNumber | — |
| PO_HEADER_ID | AgreementNotificationControlPoHeaderId | — |
| START_DATE_ACTIVE | AgreementNotificationControlStartDateActive | ✅ |
| START_DATE_ACTIVE | AgreementNotificationControlStartDateActiveContract | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_NOTIFICATION_CONTROLS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
