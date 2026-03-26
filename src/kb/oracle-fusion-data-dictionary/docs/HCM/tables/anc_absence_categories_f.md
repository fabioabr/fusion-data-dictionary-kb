---
id: DOC-HCM-001
doc_type: system-doc
title: "ANC_ABSENCE_CATEGORIES_F — Categorias de Ausência"
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
  - categorias-ausencia
  - absence-categories
aliases:
  - ANC_ABSENCE_CATEGORIES_F
  - anc_absence_categories_f
  - categorias-ausencia-hcm
  - absence-categories
  - anc-abs-categories
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_CATEGORIES_F

## 📌 Visão Geral

Armazena as **categorias de ausência** do módulo Absence Management. Cada registro define uma categoria que agrupa tipos de ausência relacionados (ex.: doença, férias, licença maternidade), com datas de vigência controladas pelo sufixo `_F` (date-effective).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agrupamento de tipos de ausência:** Organiza os tipos de ausência em categorias lógicas para facilitar a gestão e o reporte.
- **Políticas por categoria:** Permite definir regras e configurações por categoria (ex.: categorias que impactam folha de pagamento vs. categorias informativas).
- **Relatórios gerenciais:** Base para dashboards de absenteísmo por categoria.
- **Configuração de elegibilidade:** Associação com planos de ausência e regras de acumulação.
- **Auditoria:** Controle de vigência temporal com histórico completo de alterações.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da categoria de ausência | — | 🟢 95% |
| 2 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 90% |
| 3 | ABSENCE_CATEGORY_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da categoria de ausência | — | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 6 | ABSENCE_CATEGORY_STATUS | VARCHAR2(30) | NULL | Classificação | Status da categoria (A — ativo, I — inativo) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[anc_absence_type_cate_f]] — via `ABSENCE_CATEGORY_ID` (associação tipo-categoria)
- [[anc_absence_categories_f_tl]] — via `ABSENCE_CATEGORY_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Categorias ativas por legislação
```sql
SELECT ac.ABSENCE_CATEGORY_ID, ac.ABSENCE_CATEGORY_NAME,
       ac.LEGISLATION_CODE, ac.EFFECTIVE_START_DATE
FROM   ANC_ABSENCE_CATEGORIES_F ac
WHERE  SYSDATE BETWEEN ac.EFFECTIVE_START_DATE AND ac.EFFECTIVE_END_DATE
  AND  ac.LEGISLATION_CODE = :p_legislation_code;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `LEGISLATION_CODE = 'BR'` — Categorias para legislação brasileira
---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- O campo `LEGISLATION_CODE` permite configurações específicas por país.
- A tabela de traduções (`_TL`) armazena o nome da categoria em múltiplos idiomas.
- Alterações são rastreadas via `OBJECT_VERSION_NUMBER` para controle de concorrência.
---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_CATEGORIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencecategoriesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
