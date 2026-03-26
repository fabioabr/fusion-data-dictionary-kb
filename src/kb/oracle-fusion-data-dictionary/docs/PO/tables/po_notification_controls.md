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

## 📚 Referências

- [Oracle Docs — PO_NOTIFICATION_CONTROLS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
