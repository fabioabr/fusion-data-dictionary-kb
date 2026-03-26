---
id: DOC-HCM-298
doc_type: system-doc
title: "HWM_FND_MESSAGES_VL — Mensagens do Foundation (View Linguistica)"
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
  - messages
  - workforce-management
  - foundation
aliases:
  - HWM_FND_MESSAGES_VL
  - hwm_fnd_messages_vl
  - hwm-fnd-messages-vl
  - fnd-messages
  - mensagens-foundation-wfm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_FND_MESSAGES_VL

## 📌 Visao Geral

View linguistica que expoe as **mensagens** do modulo Workforce Management registradas no framework Foundation (FND).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Troubleshooting:** Consultar mensagens de erro do sistema.
- **Localizacao:** Mensagens traduzidas para o idioma do usuario.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MESSAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador da mensagem | — | 🟡 80% |
| 2 | MESSAGE_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome/codigo da mensagem | — | 🟡 80% |
| 3 | MESSAGE_TEXT | VARCHAR2(4000) | NULL | Dados | Texto da mensagem (traduzido) | — | 🟡 80% |
| 4 | MESSAGE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo (ERROR, WARNING, INFO) | — | 🟡 75% |
| 5 | APPLICATION_ID | NUMBER(18) | NULL | FK | Aplicacao associada | — | 🟡 70% |
| 6 | LANGUAGE | VARCHAR2(4) | NULL | Controle | Idioma | — | 🟢 90% |
| 7 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data de criacao | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Mensagens de erro
```sql
SELECT m.MESSAGE_NAME, m.MESSAGE_TEXT
FROM   HWM_FND_MESSAGES_VL m
WHERE  m.MESSAGE_TYPE = 'ERROR';
```

---

## 🔒 Observacoes

- Sufixo `_VL` — View Linguistica.
- Util para diagnostico de erros no modulo WFM.

---

## 📚 Referencias

- [Oracle Docs — HWM_FND_MESSAGES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmfndmessagesvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
