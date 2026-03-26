---
id: DOC-HCM-198
doc_type: system-doc
title: "HRQ_RESPONSE_TYPES_B — Tipos de Resposta de Questionários (Base)"
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
  - questionnaires
  - response-types
aliases:
  - HRQ_RESPONSE_TYPES_B
  - hrq_response_types_b
  - tipos-de-resposta-de-questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_RESPONSE_TYPES_B

## 📌 Visão Geral

Tabela base dos **tipos de resposta** disponíveis (Likert, sim/não, texto livre).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Formatos:** Tipos padrão de resposta.
- **Reutilização:** Aplicáveis a múltiplas questões.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | RESPONSE_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟡 80% |
| 3 | FORMAT_TYPE | VARCHAR2(30) | NULL | Classificação | Formato (LIKERT, YES_NO, TEXT) | — | 🟡 75% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo (Y/N) | — | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas relacionadas

### Tabelas relacionadas

---

## 📎 Uso Típico

### Tipos ativos
```sql
SELECT rt.RESPONSE_TYPE_ID, rt.RESPONSE_TYPE_CODE, rt.FORMAT_TYPE
FROM   HRQ_RESPONSE_TYPES_B rt
WHERE  NVL(rt.ENABLED_FLAG,'Y') = 'Y';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_response_types_tl]].


---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
