---
id: DOC-PO-019
doc_type: system-doc
title: "PON_DOCTYPE_STYLES_B — Estilos de Tipo de Documento de Negociação (Base)"
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
  - sourcing
  - doctype-styles
  - configuracao
aliases:
  - PON_DOCTYPE_STYLES_B
  - pon_doctype_styles_b
  - estilos-doctype-base
  - doctype-styles-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_DOCTYPE_STYLES_B

## 📌 Visão Geral

Armazena as **definições base dos estilos de tipo de documento** para negociações de Sourcing. Cada registro define um estilo que combina um tipo de documento de negociação (RFQ, RFI, Auction, etc.) com um estilo de negociação, determinando o comportamento e as funcionalidades habilitadas. É a tabela base (sufixo `_B`) do padrão multi-idioma Oracle — os dados traduzidos ficam em [[pon_doctype_styles_tl]].

> [!note] Sufixo _B
> O sufixo `_B` indica a tabela **base** do padrão Oracle de tradução (MLS — Multi-Language Support). Contém os dados não traduzíveis (IDs, flags, configurações). Os textos traduzíveis (nome, descrição) ficam em `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de negociações:** Define quais estilos estão disponíveis para criação de negociações (RFQ, Auction, RFI).
- **Controle de funcionalidades:** Cada estilo habilita/desabilita funcionalidades específicas (e.g., sealed bid, surrogate bidding, multi-round).
- **Padronização de processos:** Garante que negociações sigam templates corporativos predefinidos.
- **Governança de Sourcing:** Controle de quais tipos de negociação estão autorizados por categoria ou organização.
- **Setup administrativo:** Configuração do módulo de Sourcing pelo administrador funcional.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_STYLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do estilo de tipo de documento | — | 🟢 95% |
| 2 | DOCTYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de documento de negociação | [[pon_auc_doctypes_b]] | 🟢 90% |
| 3 | NEGOTIATION_STYLE_ID | NUMBER(18) | NOT NULL | FK | Estilo de negociação associado | [[pon_negotiation_styles_b]] | 🟢 90% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Estilo habilitado (Y/N) | — | 🟢 90% |
| 5 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Classificação | Estilo padrão para o tipo de documento (Y/N) | — | 🟡 80% |
| 6 | SEALED_BID_FLAG | VARCHAR2(1) | NULL | Configuração | Permite lance selado/lacrado (Y/N) | — | 🟡 75% |
| 7 | SURROGATE_BID_FLAG | VARCHAR2(1) | NULL | Configuração | Permite lance substituto (comprador em nome do fornecedor) (Y/N) | — | 🟡 75% |
| 8 | MULTI_ROUND_FLAG | VARCHAR2(1) | NULL | Configuração | Permite múltiplas rodadas de negociação (Y/N) | — | 🟡 75% |
| 9 | AWARD_APPROVAL_FLAG | VARCHAR2(1) | NULL | Configuração | Requer aprovação para adjudicação (Y/N) | — | 🟡 75% |
| 10 | LARGE_NEG_ENABLED_FLAG | VARCHAR2(1) | NULL | Configuração | Suporta negociações de grande porte (Y/N) | — | 🟡 70% |
| 11 | OUTCOME_CODE | VARCHAR2(30) | NULL | Classificação | Resultado esperado: PURCHASE_ORDER, BLANKET, CONTRACT, NONE | — | 🟡 75% |
| 12 | START_DATE | DATE | NULL | Data | Data de início de vigência do estilo | — | 🟡 70% |
| 13 | END_DATE | DATE | NULL | Data | Data de fim de vigência do estilo | — | 🟡 70% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auc_doctypes_b]] — via `DOCTYPE_ID` (tipo de documento de negociação)
- [[pon_negotiation_styles_b]] — via `NEGOTIATION_STYLE_ID` (estilo de negociação)

### Tabelas-filha (FK de saída)
- [[pon_doctype_styles_tl]] — via `DOCTYPE_STYLE_ID` (traduções do estilo)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Estilos habilitados por tipo de documento
```sql
SELECT ds.DOCTYPE_STYLE_ID, dt.DOCTYPE_NAME,
       ns.STYLE_NAME, ds.ENABLED_FLAG, ds.DEFAULT_FLAG,
       ds.OUTCOME_CODE
FROM   PON_DOCTYPE_STYLES_B ds
JOIN   PON_AUC_DOCTYPES_TL dt ON dt.DOCTYPE_ID = ds.DOCTYPE_ID
JOIN   PON_NEGOTIATION_STYLES_TL ns ON ns.NEGOTIATION_STYLE_ID = ds.NEGOTIATION_STYLE_ID
WHERE  ds.ENABLED_FLAG = 'Y'
  AND  dt.LANGUAGE = USERENV('LANG')
  AND  ns.LANGUAGE = USERENV('LANG')
ORDER BY dt.DOCTYPE_NAME, ns.STYLE_NAME;
```

### Configurações de funcionalidades por estilo
```sql
SELECT ds.DOCTYPE_STYLE_ID,
       ds.SEALED_BID_FLAG, ds.SURROGATE_BID_FLAG,
       ds.MULTI_ROUND_FLAG, ds.AWARD_APPROVAL_FLAG,
       ds.OUTCOME_CODE
FROM   PON_DOCTYPE_STYLES_B ds
WHERE  ds.DOCTYPE_ID = :p_doctype_id
  AND  ds.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- A combinação `DOCTYPE_ID` + `NEGOTIATION_STYLE_ID` define uma configuração única de comportamento de negociação.
- O `OUTCOME_CODE` determina o tipo de documento gerado após adjudicação: PURCHASE_ORDER, BLANKET (acordo), CONTRACT ou NONE (sem geração automática).
- Apenas um estilo pode ter `DEFAULT_FLAG = 'Y'` por `DOCTYPE_ID` — é o estilo pré-selecionado na criação de negociações.
- Os flags de configuração (`SEALED_BID_FLAG`, `SURROGATE_BID_FLAG`, etc.) são herdados pela negociação ao selecionar o estilo.
- Para obter o nome traduzido do estilo, utilizar a join com [[pon_doctype_styles_tl]].

---

## 📚 Referências

- [Oracle Docs — PON_DOCTYPE_STYLES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pondoctypestylesb.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
