---
id: DOC-HCM-028
doc_type: system-doc
title: "BEN_BILL_CHARGES — Cobranças de Benefícios"
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
  - cobrancas
  - bill-charges
  - premium
aliases:
  - BEN_BILL_CHARGES
  - ben_bill_charges
  - cobrancas-beneficios
  - bill-charges
  - ben-bill-charges
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CHARGES

## 📌 Visão Geral

Armazena as **cobranças individuais** de benefícios. Cada registro representa um valor cobrado de um participante referente a um plano de benefício em um período específico.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Cobranças de Benefícios.
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
| 1 | BILL_CHARGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da cobrança | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador cobrado | [[per_all_people_f]] | 🟢 90% |
| 3 | PL_ID | NUMBER(18) | NULL | FK | Plano de benefício | [[ben_pl_f]] | 🟡 80% |
| 4 | CHARGE_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da cobrança | — | 🟢 85% |
| 5 | CHARGE_STATUS | VARCHAR2(30) | NULL | Classificação | Status (PENDING, PAID, CANCELLED) | — | 🟡 80% |
| 6 | CHARGE_DATE | DATE | NOT NULL | Data | Data da cobrança | — | 🟢 85% |
| 7 | DUE_DATE | DATE | NULL | Data | Data de vencimento | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da cobranca de beneficio)
- [[ben_pl_f]] — via `PL_ID` (plano de beneficio da cobranca)

### Tabelas-filha (FK de saída)
- [[ben_bill_charge_details]] — via `BILL_CHARGE_ID` (detalhes da cobranca de beneficio)
- [[ben_bill_charge_payments]] — via `BILL_CHARGE_ID` (pagamentos da cobranca de beneficio)

---

## 📎 Uso Típico

### Cobranças pendentes
```sql
SELECT bc.BILL_CHARGE_ID, bc.PERSON_ID, bc.CHARGE_AMOUNT,
       bc.CHARGE_STATUS, bc.DUE_DATE
FROM   BEN_BILL_CHARGES bc
WHERE  bc.CHARGE_STATUS = 'PENDING';
```

### Filtros comuns
- `CHARGE_STATUS = 'PENDING'` — Cobranças pendentes
- `CHARGE_STATUS = 'PAID'` — Cobranças pagas

---

## 🔒 Observações

- Cada cobrança está vinculada a um plano e um colaborador.
- Detalhes da composição do valor estão em `BEN_BILL_CHARGE_DETAILS`.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CHARGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcharges.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
