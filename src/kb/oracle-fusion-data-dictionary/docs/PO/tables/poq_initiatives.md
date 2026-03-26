---
id: DOC-PO-041
doc_type: system-doc
title: "POQ_INITIATIVES — Iniciativas de Qualificação de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - qualificacao
  - supplier-qualification
  - initiatives
aliases:
  - POQ_INITIATIVES
  - poq_initiatives
  - iniciativas-qualificacao
  - supplier-qualification-initiatives
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_INITIATIVES

## 📌 Visão Geral

Armazena as **iniciativas de qualificação de fornecedores** no módulo de Procurement. Cada registro representa uma iniciativa (campanha/evento) de avaliação em massa de fornecedores, vinculada a um modelo de qualificação. A iniciativa agrupa as avaliações individuais de cada fornecedor participante.

> [!note] Prefixo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Supplier Qualification Management** (SQM) do Oracle Fusion Procurement.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Qualificação periódica:** Criação de rodadas de avaliação de fornecedores (anual, semestral, por evento).
- **Onboarding de fornecedores:** Iniciativas de qualificação inicial para novos fornecedores.
- **Requalificação:** Reavaliação de fornecedores após não conformidades ou mudanças contratuais.
- **Compliance:** Registro auditável de todas as iniciativas de qualificação conduzidas pela organização.
- **Análise de risco:** Base para relatórios de cobertura de qualificação do supply base.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INITIATIVE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da iniciativa de qualificação | — | 🟢 95% |
| 2 | INITIATIVE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome descritivo da iniciativa | — | 🟢 90% |
| 3 | INITIATIVE_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da iniciativa visível ao usuário | — | 🟡 75% |
| 4 | QUAL_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de qualificação utilizado na iniciativa | [[poq_qual_models]] | 🟢 90% |
| 5 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status da iniciativa: DRAFT, ACTIVE, CLOSED, CANCELED | — | 🟢 90% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada da iniciativa | — | 🟢 90% |
| 7 | START_DATE | DATE | NULL | Data | Data de início da iniciativa | — | 🟢 90% |
| 8 | END_DATE | DATE | NULL | Data | Data de encerramento da iniciativa | — | 🟢 90% |
| 9 | OWNER_ID | NUMBER(18) | NULL | Referência | Usuário responsável pela iniciativa | — | 🟡 75% |
| 10 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (procurement BU) | [[hr_all_organization_units_f]] | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 17 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 18 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da iniciativa de qualificação)

### Tabelas-filha (FK de saída)
- [[poq_initiative_suppliers]] — via `INITIATIVE_ID` (fornecedores participantes da iniciativa)

---

## 📎 Uso Típico

### Iniciativas ativas com modelo de qualificação
```sql
SELECT ini.INITIATIVE_ID, ini.INITIATIVE_NAME, ini.STATUS_CODE,
       ini.START_DATE, ini.END_DATE, qm.QUAL_MODEL_NAME
FROM   POQ_INITIATIVES ini
JOIN   POQ_QUAL_MODELS qm ON qm.QUAL_MODEL_ID = ini.QUAL_MODEL_ID
WHERE  ini.STATUS_CODE = 'ACTIVE';
```

### Contagem de iniciativas por status
```sql
SELECT ini.STATUS_CODE, COUNT(*) AS qtd_iniciativas
FROM   POQ_INITIATIVES ini
GROUP  BY ini.STATUS_CODE
ORDER  BY qtd_iniciativas DESC;
```

### Filtros comuns
- `STATUS_CODE = 'ACTIVE'` — Iniciativas em andamento
- `STATUS_CODE = 'CLOSED'` — Iniciativas encerradas
- `STATUS_CODE = 'DRAFT'` — Iniciativas em preparação

---

## 🔒 Observações

- Cada iniciativa está vinculada a exatamente um modelo de qualificação (`QUAL_MODEL_ID`).
- Os fornecedores participantes são registrados na tabela filha [[poq_initiative_suppliers]].
- O ciclo de vida típico é: DRAFT → ACTIVE → CLOSED (ou CANCELED).
- A iniciativa é o ponto de entrada para execução de avaliações em massa no Supplier Qualification Management.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
