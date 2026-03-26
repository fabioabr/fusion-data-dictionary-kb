---
id: DOC-HCM-119
doc_type: system-doc
title: "HNS_NOTES — Notas de Saúde e Segurança"
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
  - notas
  - comentarios
  - hns
aliases:
  - HNS_NOTES
  - hns_notes
  - hns-notes
  - DOC-HCM-119
  - notas-de-saúde-e-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_NOTES

## 📌 Visão Geral

Armazena as **notas e comentários** associados a incidentes, investigações e ações de saúde e segurança. Permite documentação livre e acompanhamento textual dos eventos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Documentação livre:** Registro de observações e comentários.
- **Histórico de comunicação:** Trilha de notas ao longo do processo.
- **Acompanhamento:** Atualizações textuais sobre o andamento.
- **Auditoria:** Registro de decisões e observações.
- **Colaboração:** Múltiplos participantes adicionando notas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | NOTE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da nota | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NULL | FK | Incidente associado | [[hns_incidents_detail]] | 🟡 80% |
| 3 | NOTE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da nota | — | 🟡 70% |
| 4 | NOTE_TEXT | VARCHAR2(4000) | NULL | Texto | Conteúdo da nota | — | 🟡 80% |
| 5 | CREATED_BY_PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que criou a nota | [[per_all_people_f]] | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente da nota registrada)
- [[per_all_people_f]] — via `CREATED_BY_PERSON_ID` (autor da nota do incidente)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Notas por incidente
```sql
SELECT n.NOTE_TYPE, n.NOTE_TEXT, n.CREATION_DATE
FROM   HNS_NOTES n
WHERE  n.INCIDENT_ID = :p_incident_id
ORDER BY n.CREATION_DATE DESC;
```

### Últimas notas registradas
```sql
SELECT n.INCIDENT_ID, n.NOTE_TEXT, n.CREATION_DATE
FROM   HNS_NOTES n
ORDER BY n.CREATION_DATE DESC
FETCH FIRST 20 ROWS ONLY;
```

---

## 🔒 Observações

- Notas são de texto livre — sem estrutura predefinida.
- Cada incidente pode ter múltiplas notas ao longo do tempo.
- O `NOTE_TYPE` pode categorizar: OBSERVATION, DECISION, UPDATE, etc.
- Notas servem como trilha de auditoria textual do processo.

---

## 📚 Referências

- [Oracle Docs — HNS_NOTES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsnotes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
