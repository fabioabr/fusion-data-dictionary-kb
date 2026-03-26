---
id: DOC-HCM-022
doc_type: system-doc
title: "ANC_PER_ACRL_ENTRY_DTLS — Detalhes de Entrada de Acumulação"
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
  - absence-management
  - detalhes-acumulacao
  - accrual-details
aliases:
  - ANC_PER_ACRL_ENTRY_DTLS
  - anc_per_acrl_entry_dtls
  - detalhes-acumulacao-ausencia
  - accrual-entry-details
  - anc-per-acrl-entry-dtls
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ACRL_ENTRY_DTLS

## 📌 Visão Geral

Armazena os **detalhes das entradas de acumulação** de ausência. Contém informações adicionais sobre cada movimentação de saldo (ex.: base de cálculo, faixa aplicada, fator proporcional).


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento do cálculo:** Mostra como cada valor de acumulação foi calculado.
- **Auditoria:** Rastreabilidade completa do cálculo de saldo.
- **Depuração:** Permite verificar se as regras de acumulação estão sendo aplicadas corretamente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ACRL_ENTRY_DTL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟢 85% |
| 2 | PER_ACCRUAL_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de acumulação | [[anc_per_accrual_entries]] | 🟢 90% |
| 3 | DETAIL_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de detalhe | — | 🟡 70% |
| 4 | DETAIL_VALUE | VARCHAR2(2000) | NULL | Dados | Valor do detalhe | — | 🟡 70% |
| 5 | ACCRUAL_BAND_ID | NUMBER(18) | NULL | FK | Faixa de acumulação aplicada | [[anc_accrual_bands_f]] | 🟡 70% |
| 6 | RATE_APPLIED | NUMBER | NULL | Cálculo | Taxa de acumulação aplicada | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_accrual_entries]] — via `PER_ACCRUAL_ENTRY_ID` (lancamento de acumulo detalhado)
- [[anc_accrual_bands_f]] — via `ACCRUAL_BAND_ID` (faixa de acumulo do detalhe)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Detalhes de cálculo de acumulação
```sql
SELECT d.DETAIL_TYPE, d.DETAIL_VALUE, d.RATE_APPLIED
FROM   ANC_PER_ACRL_ENTRY_DTLS d
WHERE  d.PER_ACCRUAL_ENTRY_ID = :p_accrual_entry_id;
```

### Filtros comuns
- `PER_ACCRUAL_ENTRY_ID = :p_entry_id` — Detalhes de uma entrada específica

---

## 🔒 Observações

- Contém o detalhamento do cálculo de cada movimentação de saldo.
- O campo `ACCRUAL_BAND_ID` indica qual faixa de acumulação foi utilizada no cálculo.
- `RATE_APPLIED` mostra a taxa efetiva aplicada ao cálculo.

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ACRL_ENTRY_DTLS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperacrlentrdtls.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
