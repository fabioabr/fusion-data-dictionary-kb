---
id: DOC-PO-043
doc_type: system-doc
title: "POQ_QUAL_AREAS_VL — Áreas de Qualificação (View Traduzida)"
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
  - qualification-areas
  - view-traduzida
aliases:
  - POQ_QUAL_AREAS_VL
  - poq_qual_areas_vl
  - areas-qualificacao-vl
  - qualification-areas-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_AREAS_VL

## 📌 Visão Geral

View traduzida (sufixo `_VL`) que apresenta as **áreas de qualificação de fornecedores** com textos no idioma da sessão do usuário. Consolida dados da tabela base (`_B`) com a tabela de traduções (`_TL`), expondo nome e descrição da área de qualificação no idioma apropriado.

> [!note] Sufixo _VL
> O sufixo `_VL` (Value List) indica uma **view de conveniência** que faz JOIN entre a tabela base `_B` e a tabela de traduções `_TL`, filtrando pelo idioma da sessão (`USERENV('LANG')`). Não é uma tabela física.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Configuração de modelos:** Exibição das áreas de qualificação disponíveis para composição de modelos.
- **Questionários de fornecedores:** Apresentação dos nomes de áreas no idioma do fornecedor/avaliador.
- **Relatórios multilíngues:** Consultas que precisam do nome traduzido da área de qualificação.
- **LOVs (List of Values):** Alimentação de listas de seleção na interface do Supplier Qualification Management.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_AREA_ID | NUMBER(18) | NOT NULL | PK | Identificador único da área de qualificação | — | 🟢 90% |
| 2 | QUAL_AREA_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código interno da área de qualificação | — | 🟡 80% |
| 3 | QUAL_AREA_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome da área de qualificação no idioma da sessão | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição da área no idioma da sessão | — | 🟢 90% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Indicador de área ativa: Y/N | — | 🟡 80% |
| 6 | START_DATE_ACTIVE | DATE | NULL | Data | Data de início de validade | — | 🟡 75% |
| 7 | END_DATE_ACTIVE | DATE | NULL | Data | Data de fim de validade | — | 🟡 75% |
| 8 | SCORING_METHOD | VARCHAR2(30) | NULL | Classificação | Método de pontuação: MANUAL, WEIGHTED, PASS_FAIL | — | 🟡 65% |
| 9 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma (proveniente da _TL) | — | 🟢 90% |
| 10 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução | — | 🟢 90% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma direta — esta é uma view sobre tabelas base `_B` e `_TL`.

### Tabelas/Views relacionadas
- [[poq_qual_model_areas]] — via `QUAL_AREA_ID` (áreas associadas a modelos)
- [[poq_qual_area_questions]] — via `QUAL_AREA_ID` (perguntas da área)
- [[poq_qual_area_outcomes]] — via `QUAL_AREA_ID` (resultados da área)
- [[poq_qual_area_all_questions_v]] — via `QUAL_AREA_ID` (view consolidada de perguntas)

---

## 📎 Uso Típico

### Listar áreas de qualificação ativas
```sql
SELECT qa.QUAL_AREA_ID, qa.QUAL_AREA_CODE, qa.QUAL_AREA_NAME,
       qa.DESCRIPTION, qa.SCORING_METHOD
FROM   POQ_QUAL_AREAS_VL qa
WHERE  qa.ENABLED_FLAG = 'Y'
  AND  (qa.END_DATE_ACTIVE IS NULL OR qa.END_DATE_ACTIVE > SYSDATE);
```

### Áreas de qualificação por modelo
```sql
SELECT qa.QUAL_AREA_NAME, qma.WEIGHT_PERCENT
FROM   POQ_QUAL_AREAS_VL qa
JOIN   POQ_QUAL_MODEL_AREAS qma ON qma.QUAL_AREA_ID = qa.QUAL_AREA_ID
WHERE  qma.QUAL_MODEL_ID = :p_model_id;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Áreas ativas
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão (implícito na view)

---

## 🔒 Observações

- Por ser uma `_VL`, **não deve ser usada em INSERT/UPDATE/DELETE** — utilize as tabelas base `_B` e `_TL` para DML.
- A filtragem por idioma é automática via `USERENV('LANG')` na definição da view.
- Áreas de qualificação são reutilizáveis entre múltiplos modelos via [[poq_qual_model_areas]].
- Exemplos de áreas típicas: "Saúde Financeira", "Conformidade Regulatória", "Capacidade Técnica", "Responsabilidade Ambiental".

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
