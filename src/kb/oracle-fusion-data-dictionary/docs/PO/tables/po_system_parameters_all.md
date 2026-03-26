---
id: DOC-PO-141
doc_type: system-doc
title: "PO_SYSTEM_PARAMETERS_ALL — Parametros de Sistema do Modulo PO"
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
  - parametros
  - configuracao
  - setup
aliases:
  - PO_SYSTEM_PARAMETERS_ALL
  - po_system_parameters_all
  - po-system-parameters-all
  - po-system
  - parametros-de-sistema-do-modulo-po
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_SYSTEM_PARAMETERS_ALL

## 📌 Visão Geral

Armazena os **parametros de configuracao do modulo Procurement** por business unit: numeracao, matching, accrual, aprovacao automatica.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao:** Parametros que controlam o comportamento.
- **Defaults:** Valores padrao para POs.
- **Matching rules:** Regras padrao por BU.
- **Aprovacao:** Controle de aprovacao automatica.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ORG_ID | NUMBER(18) | NOT NULL | PK | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 2 | RECEIVE_CLOSE_TOLERANCE | NUMBER | NULL | Configuracao | Tolerancia de fechamento por recebimento (%) | — | 🟢 90% |
| 3 | INVOICE_CLOSE_TOLERANCE | NUMBER | NULL | Configuracao | Tolerancia de fechamento por faturamento (%) | — | 🟢 90% |
| 4 | ACCRUE_ON_RECEIPT_FLAG | VARCHAR2(1) | NULL | Flag | Accrual no recebimento (Y/N) | — | 🟢 90% |
| 5 | DEFAULT_RATE_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa padrao | — | 🟡 80% |
| 6 | ENFORCE_BUYER_NAME_FLAG | VARCHAR2(1) | NULL | Flag | Obriga comprador | — | 🟡 75% |
| 7 | APPROVAL_REQUIRED_FLAG | VARCHAR2(1) | NULL | Flag | Aprovacao obrigatoria | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit dos parâmetros de sistema de compras)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Parametros de uma BU
```sql
SELECT ORG_ID, RECEIVE_CLOSE_TOLERANCE, INVOICE_CLOSE_TOLERANCE,
       ACCRUE_ON_RECEIPT_FLAG
FROM   PO_SYSTEM_PARAMETERS_ALL
WHERE  ORG_ID = :p_org_id;
```


---

## 🔒 Observações

- Uma linha por business unit.
- Alteracoes impactam todo o modulo na BU.
- Tolerancias controlam fechamento automatico de PO.
- Flag `ACCRUE_ON_RECEIPT_FLAG` define accrual no recebimento ou pagamento.

---

## 📚 Referências

- [Oracle Docs — PO_SYSTEM_PARAMETERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/posystemparametersall-10213.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
