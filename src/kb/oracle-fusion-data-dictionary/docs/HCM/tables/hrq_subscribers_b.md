---
id: DOC-HCM-200
doc_type: system-doc
title: "HRQ_SUBSCRIBERS_B — Assinantes de Questionários (Base)"
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
  - questionnaires
  - subscribers
aliases:
  - HRQ_SUBSCRIBERS_B
  - hrq_subscribers_b
  - assinantes-de-questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_SUBSCRIBERS_B

## 📌 Visão Geral

Tabela base dos **assinantes (subscribers)** de questionários. Módulos consumidores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integração modular:** Módulos que utilizam questionários.
- **Controle de acesso:** Restrição por módulo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUBSCRIBER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | SUBSCRIBER_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟡 80% |
| 3 | MODULE_CODE | VARCHAR2(30) | NULL | Classificação | Módulo consumidor | — | 🟡 70% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo (Y/N) | — | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas relacionadas

### Tabelas relacionadas

---

## 📎 Uso Típico

### Assinantes ativos
```sql
SELECT s.SUBSCRIBER_ID, s.SUBSCRIBER_CODE, s.MODULE_CODE
FROM   HRQ_SUBSCRIBERS_B s
WHERE  NVL(s.ENABLED_FLAG,'Y') = 'Y';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_subscribers_tl]].

---

## 🔗 PVOs Relacionados

### [[questionnairequestionsubscriberpvo|QuestionnaireQuestionSubscriberPVO]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SubscriberBPEOBusinessGroupId | ✅ |
| LAST_UPDATE_DATE | SubscriberBPEOLastUpdateDate | ✅ |
| SUBSCRIBER_CODE | SubscriberBPEOSubscriberCode | — |
| SUBSCRIBER_ID | SubscriberBPEOSubscriberId | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
