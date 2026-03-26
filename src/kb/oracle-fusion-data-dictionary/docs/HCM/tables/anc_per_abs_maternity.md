---
id: DOC-HCM-017
doc_type: system-doc
title: "ANC_PER_ABS_MATERNITY — Dados de Maternidade por Ausência"
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
  - maternidade
  - maternity
  - licenca-maternidade
  - paternidade
aliases:
  - ANC_PER_ABS_MATERNITY
  - anc_per_abs_maternity
  - maternidade-ausencia
  - absence-maternity
  - anc-per-abs-maternity
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_MATERNITY

## 📌 Visão Geral

Armazena **informações específicas de licença maternidade/paternidade** vinculadas a entradas de ausência. Contém dados como data prevista do parto, data real do nascimento, tipo de parto, etc.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Licença maternidade/paternidade:** Dados específicos para gestão de licenças parentais.
- **Compliance trabalhista:** Atende requisitos legais de registro de informações de maternidade (CLT Art. 392).
- **Cálculo de duração:** Base para determinar a duração da licença conforme tipo de parto e legislação.
- **Programa Empresa Cidadã:** Suporte a extensão de licença maternidade.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_MATERNITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de ausência | [[anc_per_abs_entries]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaboradora | [[per_all_people_f]] | 🟢 90% |
| 4 | EXPECTED_DUE_DATE | DATE | NULL | Data | Data prevista do parto | — | 🟡 80% |
| 5 | ACTUAL_BIRTH_DATE | DATE | NULL | Data | Data real do nascimento | — | 🟡 80% |
| 6 | BIRTH_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de parto (NORMAL, CESAREAN, etc.) | — | 🟡 70% |
| 7 | NUMBER_OF_BABIES | NUMBER | NULL | Dados | Número de bebês (para partos múltiplos) | — | 🟡 70% |
| 8 | STILLBORN_FLAG | VARCHAR2(1) | NULL | Classificação | Indica natimorto (Y/N) | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia da licenca maternidade)
- [[per_all_people_f]] — via `PERSON_ID` (colaboradora da licenca maternidade)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Licenças maternidade com data de nascimento
```sql
SELECT m.PERSON_ID, m.EXPECTED_DUE_DATE, m.ACTUAL_BIRTH_DATE,
       m.BIRTH_TYPE, m.NUMBER_OF_BABIES
FROM   ANC_PER_ABS_MATERNITY m
JOIN   ANC_PER_ABS_ENTRIES e ON m.ABSENCE_ENTRY_ID = e.ABSENCE_ENTRY_ID
WHERE  e.ABSENCE_STATUS = 'APPROVED';
```

### Filtros comuns
- `e.ABSENCE_STATUS = 'APPROVED'` — Licenças aprovadas
- `m.ACTUAL_BIRTH_DATE IS NOT NULL` — Nascimentos já registrados

---

## 🔒 Observações

- Contém dados sensíveis (PII) — classificar como `restricted` ou `confidential` no Neo4j.
- A duração da licença pode variar conforme `BIRTH_TYPE` e legislação (ex.: CLT 120 dias normal, 180 dias Empresa Cidadã).
- `STILLBORN_FLAG = 'Y'` pode disparar regras específicas de licença.

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_MATERNITY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsmaternity.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
