---
id: DOC-HCM-034
doc_type: system-doc
title: "BEN_BILL_PER_CREDIT — Créditos de Cobrança por Pessoa"
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
  - creditos
  - per-credit
  - devolucao
aliases:
  - BEN_BILL_PER_CREDIT
  - ben_bill_per_credit
  - creditos-cobranca-beneficios
  - bill-per-credit
  - ben-bill-per-credit
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_PER_CREDIT

## 📌 Visão Geral

Armazena os **créditos** aplicados a cobranças de benefícios por pessoa. Registra devoluções, descontos ou créditos que reduzem o valor devido pelo colaborador.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Créditos de Cobrança por Pessoa.
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
| 1 | BILL_PER_CREDIT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do crédito | — | 🟢 85% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | CREDIT_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do crédito | — | 🟢 85% |
| 4 | CREDIT_DATE | DATE | NOT NULL | Data | Data do crédito | — | 🟢 85% |
| 5 | CREDIT_REASON | VARCHAR2(240) | NULL | Classificação | Motivo do crédito | — | 🟡 75% |
| 6 | CREDIT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (APPLIED, PENDING) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do credito de beneficio)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Créditos por colaborador
```sql
SELECT pc.CREDIT_AMOUNT, pc.CREDIT_DATE, pc.CREDIT_REASON
FROM   BEN_BILL_PER_CREDIT pc
WHERE  pc.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `CREDIT_STATUS = 'APPLIED'` — Créditos já aplicados

---

## 🔒 Observações

- Créditos reduzem o valor devido em cobranças futuras ou atuais.
- Motivos comuns: mudança de plano, cancelamento antecipado, correção de cobrança.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_PER_CREDIT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillpercredit.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
