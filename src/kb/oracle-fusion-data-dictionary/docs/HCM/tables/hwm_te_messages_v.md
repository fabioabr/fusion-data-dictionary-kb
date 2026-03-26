---
id: DOC-HCM-349
doc_type: system-doc
title: "HWM_TE_MESSAGES_V — Mensagens de Entrada de Tempo (View)"
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
  - time-entry
  - mensagens
  - validacao
  - view
aliases:
  - HWM_TE_MESSAGES_V
  - hwm_te_messages_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TE_MESSAGES_V

## 📌 Visão Geral

View que exibe as mensagens de validação, erro e informação associadas a entradas de tempo, facilitando o diagnóstico de problemas no processamento.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de entradas de tempo:** Captura e gestão de registros individuais de horas trabalhadas.
- **Nomes alternativos:** Suporte a múltiplas nomenclaturas para integração com diferentes interfaces.
- **Validação de entradas:** Mensagens de erro e conformidade durante o processamento.
- **Controle de versão:** Rastreamento do ciclo de vida de cada entrada de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | MESSAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da mensagem | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | MESSAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da mensagem (ERROR/WARNING/INFO) | — | 🟡 75% |
| 4 | MESSAGE_TEXT | VARCHAR2(2000) | NULL | Dados | Texto da mensagem | — | 🟡 75% |
| 5 | MESSAGE_CODE | VARCHAR2(30) | NULL | Identificação | Código da mensagem | — | 🟡 70% |
| 6 | SOURCE_TABLE | VARCHAR2(30) | NULL | Referência | Tabela de origem da mensagem | — | 🟡 65% |
| 7 | SOURCE_ID | NUMBER(18) | NULL | Referência | ID do registro de origem | — | 🟡 65% |
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
SELECT t.*
FROM   HWM_TE_MESSAGES_V t
WHERE  ROWNUM <= 100
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Entry dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TE_MESSAGES_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_te_messages_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
