---
id: DOC-PO-021
doc_type: system-doc
title: "PON_DOCTYPE_STYLES_VL — Estilos de Tipo de Documento de Negociação (View Traduzida)"
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
  - negotiation
  - document-type-styles
  - sourcing
aliases:
  - PON_DOCTYPE_STYLES_VL
  - pon_doctype_styles_vl
  - estilos-tipo-documento-negociacao
  - doctype-styles-vl
  - pon-doctype-styles
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_DOCTYPE_STYLES_VL

## 📌 Visão Geral

View traduzida que combina informações de **estilos de tipo de documento de negociação** com seus respectivos textos traduzidos (idioma do usuário logado). Fornece uma visão desnormalizada dos estilos que definem o comportamento e layout dos documentos de sourcing — RFQ, RFI, Auction, etc.

> [!note] Sufixo _VL
> O sufixo `_VL` indica uma **View Language** — junção automática da tabela base `_B` com a tabela de tradução `_TL`, retornando registros no idioma da sessão do usuário.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Configuração de sourcing:** Define quais estilos de documento estão disponíveis ao criar negociações.
- **Customização de comportamento:** Cada estilo determina atributos como tipo de resposta, regras de lance, visibilidade de preços e funcionalidades habilitadas.
- **Interface de usuário:** Fornece nomes traduzidos dos estilos para exibição em telas de criação e consulta de negociações.
- **Relatórios OTBI:** Base para análises de negociações por estilo de documento.
- **Integração:** Referência para integrações que precisam identificar o tipo/estilo de uma negociação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de documento | — | 🟢 95% |
| 2 | STYLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do estilo | — | 🟢 95% |
| 3 | STYLE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do estilo de negociação | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida do estilo | — | 🟢 90% |
| 5 | DOCTYPE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do tipo de documento | — | 🟡 75% |
| 6 | NEGOTIATION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de negociação: RFQ, RFI, AUCTION, BUYER_AUCTION | — | 🟢 90% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o estilo está habilitado (Y/N) | — | 🟢 90% |
| 8 | ALLOW_MULTIPLE_ROUNDS_FLAG | VARCHAR2(1) | NULL | Configuração | Permite múltiplas rodadas de negociação (Y/N) | — | 🟡 70% |
| 9 | PRICE_VISIBILITY_CODE | VARCHAR2(30) | NULL | Configuração | Visibilidade de preços: OPEN, SEALED, BLIND | — | 🟡 70% |
| 10 | BID_RANKING_CODE | VARCHAR2(30) | NULL | Configuração | Critério de ranking dos lances: PRICE_ONLY, MULTI_ATTRIBUTE | — | 🟡 70% |
| 11 | LINE_ATTRIBUTE_ENABLED_FLAG | VARCHAR2(1) | NULL | Configuração | Habilita atributos em nível de linha (Y/N) | — | 🟡 65% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_negotiation_styles_b]] — via `STYLE_ID` (definição base do estilo)
- [[pon_negotiation_styles_tl]] — via `STYLE_ID` + `LANGUAGE` (tradução do estilo)

### Tabelas-filha (FK de saída)
- Utilizada como referência por telas de criação de negociações no módulo Sourcing

---

## 📎 Uso Típico

### Listar estilos de negociação habilitados
```sql
SELECT ds.STYLE_ID, ds.STYLE_NAME, ds.DOCTYPE_NAME,
       ds.NEGOTIATION_TYPE, ds.DESCRIPTION
FROM   PON_DOCTYPE_STYLES_VL ds
WHERE  ds.ENABLED_FLAG = 'Y'
ORDER BY ds.NEGOTIATION_TYPE, ds.STYLE_NAME;
```

### Estilos disponíveis para RFQ
```sql
SELECT ds.STYLE_ID, ds.STYLE_NAME, ds.PRICE_VISIBILITY_CODE,
       ds.BID_RANKING_CODE
FROM   PON_DOCTYPE_STYLES_VL ds
WHERE  ds.NEGOTIATION_TYPE = 'RFQ'
  AND  ds.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- Esta é uma **view desnormalizada** — não possui dados próprios; é a junção de `PON_NEGOTIATION_STYLES_B` (base) com `PON_NEGOTIATION_STYLES_TL` (tradução) e a tabela de tipos de documento.
- O idioma retornado depende da variável `USERENV('LANG')` da sessão Oracle.
- Os estilos definem o comportamento geral das negociações: se permitem lances selados, múltiplas rodadas, ranking multi-atributo, etc.
- Alterações nos estilos afetam apenas **novas** negociações; negociações existentes mantêm o estilo vigente no momento de sua criação.

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
