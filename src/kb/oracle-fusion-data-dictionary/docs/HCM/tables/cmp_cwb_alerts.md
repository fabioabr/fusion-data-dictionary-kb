---
id: DOC-HCM-070
doc_type: system-doc
title: "CMP_CWB_ALERTS — Alertas do Compensation Workbench"
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
  - compensation
  - alertas-cwb
  - cwb-alerts
  - compensacao
aliases:
  - CMP_CWB_ALERTS
  - cmp_cwb_alerts
  - alertas-cwb-compensacao
  - cwb-alerts
  - cmp-cwb-alerts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_ALERTS

## 📌 Visão Geral

Armazena os **alertas gerados no Compensation Workbench (CWB)** durante ciclos de revisão de compensação. Inclui violações de faixa salarial, estouros de orçamento e outras regras de negócio.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Monitoramento em tempo real:** Alertas exibidos ao gestor durante o processo de distribuição.
- **Compliance:** Identifica valores fora de faixas salariais aprovadas.
- **Controle orçamentário:** Alerta quando o orçamento do pool está sendo excedido.
- **Auditoria:** Registro de todos os alertas gerados por ciclo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CWB_ALERT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do alerta | — | 🟢 85% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador alvo do alerta | [[per_all_people_f]] | 🟢 90% |
| 3 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 4 | CALC_ALERT_ID | NUMBER(18) | NULL | FK | Tipo de alerta | [[cmp_calc_alerts_vl]] | 🟡 75% |
| 5 | ALERT_VALUE | NUMBER | NULL | Financeiro | Valor que gerou o alerta | — | 🟡 75% |
| 6 | ALERT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (OPEN, RESOLVED, OVERRIDDEN) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do alerta de compensacao)
- [[cmp_calc_alerts_vl]] — via `CALC_ALERT_ID` (definicao do alerta de compensacao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Alertas abertos por plano
```sql
SELECT a.CWB_ALERT_ID, a.PERSON_ID, a.ALERT_VALUE, a.ALERT_STATUS
FROM   CMP_CWB_ALERTS a
WHERE  a.ALERT_STATUS = 'OPEN'
  AND  a.PLAN_ID = :p_plan_id;
```

### Filtros comuns
- `ALERT_STATUS = 'OPEN'` — Alertas não resolvidos
- `ALERT_STATUS = 'OVERRIDDEN'` — Alertas ignorados pelo gestor

---

## 🔒 Observações

- Alertas são gerados automaticamente durante o cálculo de compensação no CWB.
- O status `OVERRIDDEN` indica que o gestor reconheceu e ignorou o alerta (com justificativa).
- Alertas `OPEN` podem bloquear a aprovação do ciclo dependendo da configuração.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_ALERTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbalerts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
