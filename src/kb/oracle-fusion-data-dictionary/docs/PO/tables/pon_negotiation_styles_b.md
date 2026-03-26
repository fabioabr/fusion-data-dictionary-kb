---
id: DOC-PO-022
doc_type: system-doc
title: "PON_NEGOTIATION_STYLES_B — Estilos de Negociação (Tabela Base)"
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
  - negotiation-styles
  - sourcing
  - base-table
aliases:
  - PON_NEGOTIATION_STYLES_B
  - pon_negotiation_styles_b
  - estilos-negociacao-base
  - negotiation-styles-base
  - pon-neg-styles-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_NEGOTIATION_STYLES_B

## 📌 Visão Geral

Tabela base que armazena a **definição dos estilos de negociação** do módulo Oracle Sourcing. Cada estilo configura o comportamento padrão de uma negociação — regras de lance, visibilidade de preços, critérios de avaliação, permissões de fornecedores e funcionalidades habilitadas. Os textos traduzidos ficam em [[pon_negotiation_styles_tl]].

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (Base), contendo colunas independentes de idioma. Os nomes e descrições traduzidos ficam na tabela `_TL` correspondente.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de estilos de sourcing:** Configura templates reutilizáveis que determinam como cada negociação se comporta.
- **Controle de funcionalidades:** Define quais funcionalidades estão habilitadas (múltiplas rodadas, lances parciais, resposta obrigatória, etc.).
- **Regras de lances:** Configura visibilidade de preços (aberto, selado, cego), ranking e critérios de desempate.
- **Avaliação multi-atributo:** Define se a negociação permite scoring baseado em múltiplos atributos além do preço.
- **Governança de procurement:** Garante padronização dos processos de sourcing conforme políticas corporativas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STYLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do estilo de negociação | — | 🟢 95% |
| 2 | STYLE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código interno do estilo | — | 🟢 90% |
| 3 | NEGOTIATION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de negociação: RFQ, RFI, AUCTION, BUYER_AUCTION | — | 🟢 90% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o estilo está habilitado (Y/N) | — | 🟢 90% |
| 5 | PRICE_VISIBILITY_CODE | VARCHAR2(30) | NULL | Configuração | Visibilidade de preços: OPEN, SEALED, BLIND | — | 🟢 85% |
| 6 | BID_RANKING_CODE | VARCHAR2(30) | NULL | Configuração | Critério de ranking: PRICE_ONLY, MULTI_ATTRIBUTE | — | 🟢 85% |
| 7 | ALLOW_MULTIPLE_ROUNDS_FLAG | VARCHAR2(1) | NULL | Configuração | Permite múltiplas rodadas (Y/N) | — | 🟡 75% |
| 8 | ALLOW_WITHDRAW_FLAG | VARCHAR2(1) | NULL | Configuração | Permite que fornecedor retire lance (Y/N) | — | 🟡 70% |
| 9 | MANUAL_CLOSE_FLAG | VARCHAR2(1) | NULL | Configuração | Exige fechamento manual (Y/N) | — | 🟡 70% |
| 10 | ALLOW_NEGOTIATION_FLAG | VARCHAR2(1) | NULL | Configuração | Permite negociação/contra-oferta (Y/N) | — | 🟡 70% |
| 11 | DISPLAY_BEST_PRICE_FLAG | VARCHAR2(1) | NULL | Configuração | Exibe melhor preço para fornecedores (Y/N) | — | 🟡 70% |
| 12 | REQUIRE_RESPONSE_FLAG | VARCHAR2(1) | NULL | Configuração | Resposta obrigatória para todas as linhas (Y/N) | — | 🟡 65% |
| 13 | LINE_ATTRIBUTE_ENABLED_FLAG | VARCHAR2(1) | NULL | Configuração | Habilita atributos em nível de linha (Y/N) | — | 🟡 65% |
| 14 | TWO_PART_FLAG | VARCHAR2(1) | NULL | Configuração | Negociação em duas partes — técnica e comercial (Y/N) | — | 🟡 65% |
| 15 | SEED_DATA_FLAG | VARCHAR2(1) | NULL | Sistema | Indica dado semente (seed data) do Oracle (Y/N) | — | 🟡 60% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK explícita — tabela raiz de configuração.

### Tabelas-filha (FK de saída)
- [[pon_negotiation_styles_tl]] — via `STYLE_ID` (traduções do estilo)
- [[pon_doctype_styles_vl]] — via `STYLE_ID` (view consolidada com tipo de documento)

---

## 📎 Uso Típico

### Listar todos os estilos habilitados
```sql
SELECT s.STYLE_ID, s.STYLE_CODE, s.NEGOTIATION_TYPE,
       s.PRICE_VISIBILITY_CODE, s.BID_RANKING_CODE
FROM   PON_NEGOTIATION_STYLES_B s
WHERE  s.ENABLED_FLAG = 'Y'
ORDER BY s.NEGOTIATION_TYPE;
```

### Estilos com avaliação multi-atributo
```sql
SELECT s.STYLE_ID, s.STYLE_CODE, s.TWO_PART_FLAG,
       s.ALLOW_MULTIPLE_ROUNDS_FLAG
FROM   PON_NEGOTIATION_STYLES_B s
WHERE  s.BID_RANKING_CODE = 'MULTI_ATTRIBUTE'
  AND  s.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- Esta tabela contém apenas dados independentes de idioma. Para obter nomes e descrições traduzidos, é necessário fazer JOIN com [[pon_negotiation_styles_tl]] ou utilizar a view [[pon_doctype_styles_vl]].
- Os registros com `SEED_DATA_FLAG = 'Y'` são dados padrão do Oracle e **não devem ser alterados** — customizações devem criar novos estilos.
- O `NEGOTIATION_TYPE` define a categoria geral; o estilo adiciona configurações específicas dentro dessa categoria.
- Estilos desabilitados (`ENABLED_FLAG = 'N'`) não aparecem nas telas de criação de negociação, mas negociações existentes que os utilizam permanecem inalteradas.

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
