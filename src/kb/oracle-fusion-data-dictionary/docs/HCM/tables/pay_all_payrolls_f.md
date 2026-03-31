---
id: DOC-HCM-548
doc_type: system-doc
title: "PAY_ALL_PAYROLLS_F — Todas as Folhas de Pagamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - all-payrolls
  - folha-pagamento
  - pay-all-payrolls
aliases:
  - PAY_ALL_PAYROLLS_F
  - pay_all_payrolls_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ALL_PAYROLLS_F

## 📌 Visão Geral

Tabela central que armazena a **definicao de todas as folhas de pagamento** configuradas na organizacao. Cada registro representa uma folha (mensal, quinzenal, semanal, etc.) com suas datas de vigencia (`_F` = date-effective).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao e configuracao de folhas de pagamento
- Controle de vigencia temporal de cada payroll
- Base para associacao de colaboradores a folhas
- Relatorios de folhas ativas por periodo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da folha de pagamento | --- | 🟢 95% |
| 2 | PAYROLL_NAME | VARCHAR2(100) | NOT NULL | Identificacao | Nome da folha de pagamento | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | PERIOD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de periodo (Monthly, Semi-Monthly, Weekly) | --- | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | PAYROLL_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da folha (Open, Closed) | --- | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela raiz de configuracao de payroll

### Tabelas-filha (FK de saída)
- [[pay_assigned_payrolls_f]] --- via `PAYROLL_ID` (folhas de pagamento atribuídas ao payroll)
- [[pay_time_periods]] --- via `PAYROLL_ID` (períodos de tempo do ciclo de folha)
- [[pay_assigned_payrolls_dn]] --- via `PAYROLL_ID` (visão desnormalizada das folhas atribuídas)

---

## 📎 Uso Típico

### Folhas de pagamento vigentes
```sql
SELECT p.PAYROLL_ID, p.PAYROLL_NAME, p.PERIOD_TYPE, p.PAYROLL_STATUS
FROM   PAY_ALL_PAYROLLS_F p
WHERE  SYSDATE BETWEEN p.EFFECTIVE_START_DATE AND p.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia para obter o registro corrente.
- O campo `PERIOD_TYPE` determina a frequencia de processamento da folha.
- Cada folha pode ter multiplos periodos de pagamento associados via `PAY_TIME_PERIODS`.

---

## 📚 Referências

- [Oracle Docs — PAY_ALL_PAYROLLS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payallpayrollsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
