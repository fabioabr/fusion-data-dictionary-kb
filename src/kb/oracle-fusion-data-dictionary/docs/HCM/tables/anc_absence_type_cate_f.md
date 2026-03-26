---
id: DOC-HCM-009
doc_type: system-doc
title: "ANC_ABSENCE_TYPE_CATE_F — Associação Tipo-Categoria de Ausência"
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
  - absence-management
  - tipo-categoria
  - type-category
  - associacao
aliases:
  - ANC_ABSENCE_TYPE_CATE_F
  - anc_absence_type_cate_f
  - tipo-categoria-ausencia
  - absence-type-category
  - anc-abs-type-cate
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_TYPE_CATE_F

## 📌 Visão Geral

Armazena a **associação entre tipos e categorias de ausência**. Tabela de relação N:N que vincula cada tipo de ausência a uma ou mais categorias, permitindo agrupar tipos de ausência para fins de gestão e relatórios.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Organização hierárquica:** Permite categorizar tipos de ausência para navegação e filtragem.
- **Relatórios consolidados:** Agregação de ausências por categoria em dashboards gerenciais.
- **Regras por categoria:** Herança de configurações da categoria para os tipos associados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_TYPE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação | — | 🟢 90% |
| 2 | ABSENCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência | [[anc_absence_types_f]] | 🟢 95% |
| 3 | ABSENCE_CATEGORY_ID | NUMBER(18) | NOT NULL | FK | Categoria de ausência | [[anc_absence_categories_f]] | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausencia da categorizacao)
- [[anc_absence_categories_f]] — via `ABSENCE_CATEGORY_ID` (categoria de ausencia associada)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Tipos por categoria
```sql
SELECT cat.ABSENCE_CATEGORY_NAME, typ.ABSENCE_TYPE_NAME
FROM   ANC_ABSENCE_TYPE_CATE_F tc
JOIN   ANC_ABSENCE_CATEGORIES_F cat ON tc.ABSENCE_CATEGORY_ID = cat.ABSENCE_CATEGORY_ID
JOIN   ANC_ABSENCE_TYPES_F typ ON tc.ABSENCE_TYPE_ID = typ.ABSENCE_TYPE_ID
WHERE  SYSDATE BETWEEN tc.EFFECTIVE_START_DATE AND tc.EFFECTIVE_END_DATE
  AND  SYSDATE BETWEEN cat.EFFECTIVE_START_DATE AND cat.EFFECTIVE_END_DATE
  AND  SYSDATE BETWEEN typ.EFFECTIVE_START_DATE AND typ.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes

---

## 🔒 Observações

- Tabela de relação N:N entre tipos e categorias.
- Date-effective: a associação pode mudar ao longo do tempo.
- Um tipo pode pertencer a múltiplas categorias simultaneamente.

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_TYPE_CATE_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencetypecatef.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
