---
id: DOC-HCM-352
doc_type: system-doc
title: "HWM_TM_ALLOW_EXPS_V — Exceções Permitidas em Time Management (View)"
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
  - time-management
  - excecoes
  - permitidas
  - view
aliases:
  - HWM_TM_ALLOW_EXPS_V
  - hwm_tm_allow_exps_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ALLOW_EXPS_V

## 📌 Visão Geral

View que lista as exceções de tempo permitidas conforme políticas configuradas, indicando quais desvios de horário são aceitos automaticamente.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de tempo:** Controle centralizado de registros de horas trabalhadas e ausências.
- **Fluxo de aprovação:** Suporte ao ciclo completo de submissão, aprovação e processamento.
- **Compliance:** Conformidade com políticas internas e regulamentações de jornada de trabalho.
- **Integração:** Conexão com Payroll, Project Costing e Absence Management.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | EXCEPTION_ID | NUMBER(18) | NOT NULL | PK | Identificador da exceção | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | EXCEPTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da exceção permitida | — | 🟡 75% |
| 4 | EXCEPTION_DATE | DATE | NULL | Dados | Data da exceção | — | 🟡 75% |
| 5 | REASON_CODE | VARCHAR2(30) | NULL | Classificação | Código do motivo da exceção | — | 🟡 70% |
| 6 | APPROVED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se foi aprovada (Y/N) | — | 🟡 70% |
| 7 | APPROVER_ID | NUMBER(18) | NULL | FK | ID do aprovador | PER_ALL_PEOPLE_F | 🟡 65% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data/hora de criação | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.PERSON_ID, t.EXCEPTION_TYPE, t.EXCEPTION_DATE, t.APPROVED_FLAG
FROM   HWM_TM_ALLOW_EXPS_V t
WHERE  t.APPROVED_FLAG = 'Y'
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ALLOW_EXPS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_allow_exps_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
