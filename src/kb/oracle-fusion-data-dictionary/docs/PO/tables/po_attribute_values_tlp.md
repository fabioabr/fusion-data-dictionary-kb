---
id: DOC-PO-115
doc_type: system-doc
title: "PO_ATTRIBUTE_VALUES_TLP — Traducoes de Atributos de Itens em POs"
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
  - atributos
  - flexfields
  - customizacao
aliases:
  - PO_ATTRIBUTE_VALUES_TLP
  - po_attribute_values_tlp
  - po-attribute-values-tlp
  - po-attribute
  - traducoes-de-atributos-de-itens-em-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ATTRIBUTE_VALUES_TLP

## 📌 Visão Geral

Armazena as **traducoes dos valores de atributos de itens** em linhas de PO para suporte multilingue.

> [!note] Sufixo _TLP
> O sufixo `_TLP` indica a **tabela de traducoes predefinidas** (Translation Layer - Predefined).


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte multilingue:** Traducoes de descricoes e atributos.
- **Catalogo internacional:** Atributos em multiplos idiomas.
- **Relatorios:** Exibicao no idioma do usuario.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ATTRIBUTE_VALUES_TLP_ID | NUMBER(18) | NOT NULL | PK | ID unico | — | 🟡 75% |
| 2 | ATTRIBUTE_VALUES_ID | NUMBER(18) | NOT NULL | FK | Atributo original | [[po_attribute_values]] | 🟢 90% |
| 3 | LANGUAGE | VARCHAR2(4) | NOT NULL | Classificacao | Codigo do idioma | — | 🟢 90% |
| 4 | DESCRIPTION_TLP | VARCHAR2(240) | NULL | Descritivo | Descricao traduzida | — | 🟡 75% |
| 5 | LONG_DESCRIPTION_TLP | CLOB | NULL | Descritivo | Descricao longa traduzida | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_attribute_values]] — via `ATTRIBUTE_VALUES_ID` (tradução dos valores de atributo do PO)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Traducoes de um atributo
```sql
SELECT LANGUAGE, DESCRIPTION_TLP
FROM   PO_ATTRIBUTE_VALUES_TLP
WHERE  ATTRIBUTE_VALUES_ID = :p_attr_id;
```


---

## 🔒 Observações

- Cada atributo pode ter multiplas traducoes (uma por idioma).
- Idioma base normalmente US.
- Populada automaticamente em ambientes multilingues.

---

## 📚 Referências

- [Oracle Docs — PO_ATTRIBUTE_VALUES_TLP](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
