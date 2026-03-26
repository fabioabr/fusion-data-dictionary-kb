---
id: DOC-HCM-031
doc_type: system-doc
title: "BEN_BILL_CYCLE — Ciclos de Cobrança de Benefícios"
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
  - ciclo-cobranca
  - bill-cycle
aliases:
  - BEN_BILL_CYCLE
  - ben_bill_cycle
  - ciclo-cobranca-beneficios
  - bill-cycle
  - ben-bill-cycle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CYCLE

## 📌 Visão Geral

Armazena os **ciclos de cobrança** (billing cycles) que definem a periodicidade e as regras de processamento de cobranças de benefícios.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Ciclos de Cobrança de Benefícios.
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
| 1 | BILL_CYCLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ciclo | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do ciclo de cobrança | — | 🟢 90% |
| 3 | CYCLE_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência do ciclo | — | 🟡 80% |
| 4 | CYCLE_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charges]] — via `BILL_CYCLE_ID` (cobranças do ciclo)

---

## 📎 Uso Típico

### Ciclos ativos
```sql
SELECT bc.BILL_CYCLE_ID, bc.NAME, bc.CYCLE_FREQUENCY
FROM   BEN_BILL_CYCLE bc
WHERE  bc.CYCLE_STATUS = 'ACTIVE';
```

### Filtros comuns
- `CYCLE_STATUS = 'ACTIVE'` — Ciclos ativos

---

## 🔒 Observações

- Define a periodicidade de processamento de cobranças.
- Vinculado ao calendário de cobrança para determinar datas específicas.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CYCLE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcycle.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
