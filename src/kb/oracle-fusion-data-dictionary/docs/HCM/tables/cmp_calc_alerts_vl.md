---
id: DOC-HCM-067
doc_type: system-doc
title: "CMP_CALC_ALERTS_VL — Alertas de Cálculo de Compensação (View)"
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
  - alertas-calculo
  - calc-alerts
  - cwb
aliases:
  - CMP_CALC_ALERTS_VL
  - cmp_calc_alerts_vl
  - alertas-calculo-compensacao
  - calc-alerts
  - cmp-calc-alerts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CALC_ALERTS_VL

## 📌 Visão Geral

View que apresenta os **alertas gerados durante cálculos de compensação** com traduções no idioma da sessão. Inclui violações de faixas salariais, tetos orçamentários e outras regras.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view de lookup** — combina tabela base + traduções para acesso simplificado.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Monitoramento:** Alertas sobre valores fora de faixas salariais.
- **Compliance:** Identificação de violações de política.
- **Suporte ao gestor:** Informações de alerta no Compensation Workbench.
- **Auditoria:** Registro de alertas para revisão.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CALC_ALERT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do alerta | — | 🟡 80% |
| 2 | ALERT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de alerta (RANGE, BUDGET, POLICY) | — | 🟡 75% |
| 3 | ALERT_NAME | VARCHAR2(240) | NULL | Tradução | Nome traduzido do alerta | — | 🟡 80% |
| 4 | ALERT_DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 75% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade (WARNING, ERROR, INFO) | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta (view de configuração).

### Tabelas-filha (FK de saída)
- [[cmp_cwb_alerts]] — via `CALC_ALERT_ID` (alertas por ciclo CWB)

---

## 📎 Uso Típico

### Alertas por tipo
```sql
SELECT ca.CALC_ALERT_ID, ca.ALERT_TYPE, ca.ALERT_NAME, ca.SEVERITY
FROM   CMP_CALC_ALERTS_VL ca
ORDER BY ca.SEVERITY;
```

### Filtros comuns
- `ALERT_TYPE = 'RANGE'` — Alertas de faixa salarial
- `SEVERITY = 'ERROR'` — Alertas críticos

---

## 🔒 Observações

- View com traduções no idioma da sessão.
- Alertas são gerados automaticamente durante o processamento de compensação.
- Usados no CWB para orientar gestores sobre violações de política.

---

## 🔗 PVOs Relacionados

### [[alertspvo|AlertsPVO]] (HCM · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALERT_DESCRIPTION | CalcAlertsPEOAlertDescription | ✅ |
| ALERT_ID | CalcAlertsPEOAlertId | — |
| ALERT_KEY | CalcAlertsPEOAlertKey | — |
| ALERT_NAME | CalcAlertsPEOAlertName | ✅ |
| ALERT_TYPE | CalcAlertsPEOAlertType | ✅ |
| BUSINESS_GROUP_ID | CalcAlertsPEOBusinessGroupId | — |
| CREATED_BY | CalcAlertsPEOCreatedBy | — |
| CREATION_DATE | CalcAlertsPEOCreationDate | — |
| ENABLED_FLAG | CalcAlertsPEOEnabledFlag | ✅ |
| KEY_TYPE | CalcAlertsPEOKeyType | — |
| LAST_UPDATE_DATE | CalcAlertsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CalcAlertsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CalcAlertsPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CalcAlertsPEOObjectVersionNumber | — |
| PARTI_PROCESS_ENA | CalcAlertsPEOPartiProcessEna | — |
| QUICK_ALERT_CODE | CalcAlertsPEOQuickAlertCode | — |
| QUICK_ALERT_FLAG | CalcAlertsPEOQuickAlertFlag | — |
| REFRESH_PROCESS_ENA | CalcAlertsPEORefreshProcessEna | — |
| WRKSHT_SAVE_ENA | CalcAlertsPEOWrkshtSaveEna | — |
| WRKSHT_TAB_OUT_ENA | CalcAlertsPEOWrkshtTabOutEna | — |

---

## 📚 Referências

- [Oracle Docs — CMP_CALC_ALERTS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcalcalertsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
