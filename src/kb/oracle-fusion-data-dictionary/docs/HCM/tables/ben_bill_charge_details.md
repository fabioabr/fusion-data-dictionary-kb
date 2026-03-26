---
id: DOC-HCM-029
doc_type: system-doc
title: "BEN_BILL_CHARGE_DETAILS — Detalhes de Cobrança de Benefícios"
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
  - benefits
  - detalhes-cobranca
  - charge-details
aliases:
  - BEN_BILL_CHARGE_DETAILS
  - ben_bill_charge_details
  - detalhes-cobranca-beneficios
  - bill-charge-details
  - ben-bill-charge-details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CHARGE_DETAILS

## 📌 Visão Geral

Armazena os **detalhes** de cada cobrança de benefícios, discriminando os componentes do valor total (ex.: contribuição do empregado, contribuição do empregador, impostos).


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Detalhes de Cobrança de Benefícios.
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_CHARGE_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟢 90% |
| 2 | BILL_CHARGE_ID | NUMBER(18) | NOT NULL | FK | Cobrança principal | [[ben_bill_charges]] | 🟢 90% |
| 3 | COMPONENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de componente (EMPLOYEE, EMPLOYER, TAX) | — | 🟡 75% |
| 4 | COMPONENT_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do componente | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_bill_charges]] — via `BILL_CHARGE_ID` (cobranca de beneficio detalhada)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Detalhes por cobrança
```sql
SELECT cd.COMPONENT_TYPE, cd.COMPONENT_AMOUNT
FROM   BEN_BILL_CHARGE_DETAILS cd
WHERE  cd.BILL_CHARGE_ID = :p_charge_id;
```

### Filtros comuns
- `COMPONENT_TYPE = 'EMPLOYEE'` — Parcela do empregado

---

## 🔒 Observações

- Discrimina a composição do valor total da cobrança.
- A soma dos componentes deve coincidir com o `CHARGE_AMOUNT` da cobrança principal.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CHARGE_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillchargedetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
