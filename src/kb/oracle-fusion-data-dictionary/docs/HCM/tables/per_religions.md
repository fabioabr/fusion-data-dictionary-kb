---
id: DOC-HCM-706
doc_type: system-doc
title: "PER_RELIGIONS — Religiões de Pessoas"
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
  - religiao
  - dados-pessoais
  - diversidade
aliases:
  - PER_RELIGIONS
  - per_religions
  - religioes-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_RELIGIONS

## Visão Geral

Armazena a informação de **religião** das pessoas no sistema. Dado utilizado em contextos regulatórios ou de diversidade, dependendo da legislação do país.

> [!warning] Dados Sensíveis
> Esta tabela contém **dados pessoais sensíveis** (PII/dados sensíveis LGPD). Acesso deve ser restrito conforme legislação.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance regulatório** — legislações de alguns países exigem registro de religião
- **Diversidade e inclusão** — análises demográficas (quando autorizado)
- **Feriados religiosos** — suporte a políticas de folga por motivo religioso
- **Relatórios governamentais** — quando exigido por regulamentação local

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RELIGION_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 90% |
| 3 | RELIGION | VARCHAR2(30) | NOT NULL | Classificação | Código da religião | — | 🟡 75% |
| 4 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é a religião principal (Y/N) | — | 🟡 65% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa com registro de religiÃ£o)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Religião de uma pessoa
```sql
SELECT r.RELIGION
FROM   PER_RELIGIONS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## Observações

- Dado sensível (LGPD Art. 5º, II) — requer consentimento específico para coleta.
- Nem todos os países utilizam este campo — disponibilidade varia por legislação.
- O preenchimento é geralmente opcional e autoidentificado.

---

## Referências

- [Oracle Docs — PER_RELIGIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perreligions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
