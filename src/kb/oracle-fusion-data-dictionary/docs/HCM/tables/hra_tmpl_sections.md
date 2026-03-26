---
id: DOC-HCM-154
doc_type: system-doc
title: "HRA_TMPL_SECTIONS — Seções de Templates de Aprovação"
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
  - approval-template
  - sections
aliases:
  - HRA_TMPL_SECTIONS
  - hra_tmpl_sections
  - seções-de-templates-de-aprovação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_SECTIONS

## 📌 Visão Geral

Armazena as **seções de templates de aprovação**. Cada seção define um bloco de conteúdo dentro de um template, permitindo fluxos estruturados por etapas lógicas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação:** Seções lógicas dentro de templates.
- **Configuração modular:** Regras distintas por seção.
- **Visibilidade:** Controle de informações por etapa.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟢 95% |
| 2 | TEMPLATE_ID | NUMBER(18) | NOT NULL | FK | Template de aprovação | — | 🟢 90% |
| 3 | SECTION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da seção | — | 🟡 75% |
| 4 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da seção | — | 🟡 70% |
| 5 | DISPLAY_SEQUENCE | NUMBER | NULL | Ordenação | Ordem de exibição | — | 🟡 75% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativa (Y/N) | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Template de aprovação — via `TEMPLATE_ID`

### Tabelas relacionadas

---

## 📎 Uso Típico

### Seções ativas de um template
```sql
SELECT s.TMPL_SECTION_ID, s.SECTION_NAME, s.DISPLAY_SEQUENCE
FROM   HRA_TMPL_SECTIONS s
WHERE  s.TEMPLATE_ID = :p_template_id
  AND  NVL(s.ENABLED_FLAG, 'Y') = 'Y'
ORDER BY s.DISPLAY_SEQUENCE;
```

---

## 🔒 Observações

- Seções desabilitadas (`ENABLED_FLAG = 'N'`) não são apresentadas ao aprovador.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
