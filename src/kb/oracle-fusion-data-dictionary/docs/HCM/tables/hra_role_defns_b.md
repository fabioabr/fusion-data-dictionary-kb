---
id: DOC-HCM-111
doc_type: system-doc
title: "HRA_ROLE_DEFNS_B — Definições de Papéis de Avaliação (Base)"
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
  - performance-management
  - papéis
  - role-definitions
  - hra
aliases:
  - HRA_ROLE_DEFNS_B
  - hra_role_defns_b
  - hra-role-defns-b
  - DOC-HCM-111
  - definições-de-papéis-de-avaliação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_ROLE_DEFNS_B

## 📌 Visão Geral

Armazena as **definições base dos papéis** utilizados em processos de avaliação de performance. Tabela _B contendo códigos, status e configurações estruturais dos papéis (gestor, auto-avaliação, par, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de papéis:** Cadastro de papéis no processo de avaliação.
- **Configuracao de permissões:** Quais ações cada papel pode executar.
- **Workflow:** Papéis determinam o fluxo de aprovação.
- **Base para tradução:** Complementada por `HRA_ROLE_DEFNS_TL`.
- **Governança:** Controle de papéis auditável.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ROLE_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do papel | — | 🟢 90% |
| 2 | ROLE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do papel | — | 🟡 80% |
| 3 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (MANAGER, SELF, PEER, DIRECT_REPORT) | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versão do objeto | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_role_defns_tl]] — via `ROLE_DEFN_ID` (traducoes multilingue do registro)
- [[hra_eval_roles]] — via `ROLE_DEFN_ID` (papéis em avaliações)

---

## 📎 Uso Típico

### Papéis ativos
```sql
SELECT rd.ROLE_DEFN_ID, rd.ROLE_CODE, rd.ROLE_TYPE, rd.STATUS_CODE
FROM   HRA_ROLE_DEFNS_B rd
WHERE  rd.STATUS_CODE = 'ACTIVE';
```

### Papéis por tipo
```sql
SELECT rd.ROLE_TYPE, COUNT(*) AS qtd
FROM   HRA_ROLE_DEFNS_B rd
GROUP BY rd.ROLE_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- O `ROLE_TYPE` classifica: MANAGER, SELF, PEER, DIRECT_REPORT, etc.
- O `OBJECT_VERSION_NUMBER` e usado para controle de concorrência.
- Para nomes traduzidos, juntar com `HRA_ROLE_DEFNS_TL`.

---

## 📚 Referências

- [Oracle Docs — HRA_ROLE_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraroledefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
