---
id: DOC-HCM-646
doc_type: system-doc
title: "PER_COL_AGREEMENTS_F — Acordos Coletivos"
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
  - workforce-management
  - acordos-coletivos
  - collective-agreements
aliases:
  - PER_COL_AGREEMENTS_F
  - per_col_agreements_f
  - per-col-agreements-f
  - acordos-coletivos
  - per-col-agreements-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_COL_AGREEMENTS_F

## 📌 Visão Geral

Armazena os **acordos coletivos de trabalho** (convenções e acordos sindicais), com vigência temporal. Define as condições negociadas entre empregador e sindicatos.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de acordos coletivos** — registro de convenções e acordos sindicais.
- **Compliance trabalhista** — garantia de conformidade com condições negociadas.
- **Integração com payroll** — regras de remuneração definidas em acordos coletivos.
- **Vigência** — controle de períodos de validade dos acordos.
- **Relatórios** — base para análise de impacto de negociações coletivas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COL_AGREEMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do acordo coletivo | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 85% |
| 5 | AGREEMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de acordo (CONVENTION, AGREEMENT) | — | 🟡 75% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status do acordo (ACTIVE, EXPIRED) | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de acordos coletivos.

### Tabelas-filha (FK de saída)
- [[per_col_agreements_f_tl]] — via `COL_AGREEMENT_ID` (traduções do acordo coletivo de trabalho)

---

## 📎 Uso Típico

### Acordos coletivos vigentes
```sql
SELECT pca.COL_AGREEMENT_ID, pca.AGREEMENT_TYPE, pca.STATUS
FROM   PER_COL_AGREEMENTS_F pca
WHERE  SYSDATE BETWEEN pca.EFFECTIVE_START_DATE AND pca.EFFECTIVE_END_DATE
  AND  pca.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Acordos ativos
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Acordos vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Acordos coletivos impactam diretamente regras de payroll (pisos salariais, adicionais).
- O `LEGISLATION_CODE` vincula o acordo à legislação do país.
---

## 📚 Referências

- [Oracle Docs — PER_COL_AGREEMENTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percolagreementsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
