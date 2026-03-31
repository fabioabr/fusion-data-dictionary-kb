---
id: DOC-HCM-542
doc_type: system-doc
title: "IRC_TP_CATEGORIES_B — Categorias de Parceiros de Recrutamento (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - tp-categories
  - parceiros
  - irc-tp-categories
aliases:
  - IRC_TP_CATEGORIES_B
  - irc_tp_categories_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_TP_CATEGORIES_B

## 📌 Visão Geral

Armazena as **categorias de parceiros terceirizados** (staffing agencies, job boards, etc.) utilizados no recrutamento. Tabela base com sufixo `_B`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Classificacao de parceiros de recrutamento por categoria
- Gestao de contratos e SLAs por tipo de parceiro
- Relatorios de desempenho por categoria de parceiro

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da categoria | --- | 🟢 90% |
| 2 | CATEGORY_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da categoria | --- | 🟢 85% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica se a categoria esta ativa (Y/N) | --- | 🟡 70% |
| 4 | DISPLAY_ORDER | NUMBER | NULL | Dados | Ordem de exibicao | --- | 🟡 65% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[irc_tp_categories_tl]] --- via `CATEGORY_ID` (traduções da categoria de parceiro terceiro)
- [[irc_tp_partners]] --- via `CATEGORY_ID` (parceiros terceiros da categoria)

---

## 📎 Uso Típico

### Categorias ativas de parceiros
```sql
SELECT cb.CATEGORY_ID, cb.CATEGORY_CODE
FROM   IRC_TP_CATEGORIES_B cb
WHERE  cb.ACTIVE_FLAG = 'Y'
ORDER BY cb.DISPLAY_ORDER;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_TP_CATEGORIES_B](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/irctpcategoriesb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
