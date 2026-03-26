---
id: DOC-HCM-032
doc_type: system-doc
title: "BEN_BILL_ENRT_RSLT — Resultados de Inscrição para Cobrança"
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
  - inscricao-cobranca
  - bill-enrollment
aliases:
  - BEN_BILL_ENRT_RSLT
  - ben_bill_enrt_rslt
  - inscricao-cobranca-beneficios
  - bill-enrollment-result
  - ben-bill-enrt-rslt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_ENRT_RSLT

## 📌 Visão Geral

Armazena a **vinculação entre inscrições de benefícios e cobranças**. Conecta os resultados de inscrição (`BEN_PRTT_ENRT_RSLT`) ao sistema de billing.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Resultados de Inscrição para Cobrança.
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
| 1 | BILL_ENRT_RSLT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 85% |
| 2 | PRTT_ENRT_RSLT_ID | NUMBER(18) | NOT NULL | FK | Resultado de inscrição | [[ben_prtt_enrt_rslt]] | 🟢 90% |
| 3 | BILL_CHARGE_ID | NUMBER(18) | NULL | FK | Cobrança associada | [[ben_bill_charges]] | 🟡 80% |
| 4 | BILLING_STATUS | VARCHAR2(30) | NULL | Classificação | Status de cobrança da inscrição | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_prtt_enrt_rslt]] — via `PRTT_ENRT_RSLT_ID` (inscricao em beneficio da cobranca)
- [[ben_bill_charges]] — via `BILL_CHARGE_ID` (cobranca vinculada a inscricao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Inscrições com cobrança
```sql
SELECT be.PRTT_ENRT_RSLT_ID, be.BILLING_STATUS
FROM   BEN_BILL_ENRT_RSLT be;
```

### Filtros comuns
- `BILLING_STATUS = 'BILLED'` — Já cobrados

---

## 🔒 Observações

- Tabela de ligação entre inscrições e cobranças.
- Permite rastrear quais inscrições já foram cobradas.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_ENRT_RSLT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillenrtrslt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
