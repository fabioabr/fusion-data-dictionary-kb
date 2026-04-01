---
id: DOC-HCM-109
doc_type: system-doc
title: "HNS_INVEST_FINDINGS — Achados de Investigações"
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
  - health-safety
  - achados
  - investigacao
  - hns
aliases:
  - HNS_INVEST_FINDINGS
  - hns_invest_findings
  - hns-invest-findings
  - DOC-HCM-109
  - achados-de-investigações
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INVEST_FINDINGS

## 📌 Visão Geral

Armazena os **achados (findings)** identificados durante investigações de incidentes de segurança — falhas de processo, condições inseguras, desvios de procedimento, etc.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Documentação de achados:** Registro de descobertas da investigação.
- **Análise de causa raiz:** Detalhamento de falhas identificadas.
- **Base para ações:** Cada achado pode gerar ações corretivas.
- **Aprendizado organizacional:** Lições aprendidas.
- **Compliance:** Documentação para auditorias.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVEST_FINDING_ID | NUMBER(18) | NOT NULL | PK | Identificador único do achado | — | 🟡 80% |
| 2 | INVESTIGATION_SUMMARY_ID | NUMBER(18) | NOT NULL | FK | Investigação associada | [[hns_investigations_summary]] | 🟢 90% |
| 3 | FINDING_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do achado | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição do achado | — | 🟡 80% |
| 5 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade do achado | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_investigations_summary]] — via `INVESTIGATION_SUMMARY_ID` (investigacao dos achados)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Achados por investigação
```sql
SELECT f.FINDING_TYPE, f.DESCRIPTION, f.SEVERITY
FROM   HNS_INVEST_FINDINGS f
WHERE  f.INVESTIGATION_SUMMARY_ID = :p_investigation_id;
```

### Achados críticos
```sql
SELECT f.INVESTIGATION_SUMMARY_ID, f.DESCRIPTION
FROM   HNS_INVEST_FINDINGS f
WHERE  f.SEVERITY = 'CRITICAL';
```

---

## 🔒 Observações

- Cada investigação pode gerar múltiplos achados.
- Achados com severidade alta devem gerar ações corretivas.
- O `FINDING_TYPE` categoriza o achado (ex: PROCEDURE, EQUIPMENT, TRAINING).
- Base para registro de lições aprendidas.

---

## 🔗 PVOs Relacionados

### [[hnsinvestigationpvo|HNSInvestigationPVO]] (HCM · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | HNSInvestFindingsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSInvestFindingsPEOCreationDate | ✅ |
| DELETED_FLAG | HNSInvestFindingsPEODeletedFlag | ✅ |
| FINDING_ID | HNSInvestFindingsPEOFindingId | ✅ |
| FINDING_ISSUE_FLAG | HNSInvestFindingsPEOFindingIssueFlag | ✅ |
| FINDING_NOTES | HNSInvestFindingsPEOFindingNotes | ✅ |
| FINDING_RESPONSE | HNSInvestFindingsPEOFindingResponse | ✅ |
| FINDING_SUMMARY | HNSInvestFindingsPEOFindingSummary | ✅ |
| INVESTIGATE_ID | HNSInvestFindingsPEOInvestigateId | ✅ |
| LAST_UPDATE_DATE | HNSInvestFindingsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSInvestFindingsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSInvestFindingsPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSInvestFindingsPEObjectVersionNumber | ✅ |
| SEVERITY_LEVEL_CODE | HNSInvestFindingsPEOSeverityLevelCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_INVEST_FINDINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinvestfindings.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
