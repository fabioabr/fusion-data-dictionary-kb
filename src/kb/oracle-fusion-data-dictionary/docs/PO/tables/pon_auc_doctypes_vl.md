---
id: DOC-PO-009
doc_type: system-doc
title: "PON_AUC_DOCTYPES_VL — Tipos de Documento de Negociação (View MLS)"
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
  - document-types
  - view-mls
aliases:
  - PON_AUC_DOCTYPES_VL
  - pon_auc_doctypes_vl
  - view-tipos-documento-negociacao
  - sourcing-doctypes-vl
  - pon-doctypes-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUC_DOCTYPES_VL

## Visão Geral

**View MLS (Multi-Language Support)** que combina os dados base da `PON_AUC_DOCTYPES_B` com as traduções da `PON_AUC_DOCTYPES_TL` no idioma da sessão do usuário. Fornece uma visão unificada dos tipos de documento de negociação com nomes e descrições traduzidos, sendo o ponto de acesso recomendado pela Oracle para consultas e relatórios.

> [!note] Padrão Oracle MLS (_B/_TL/_VL)
> - `_B` — Dados base independentes de idioma → [[pon_auc_doctypes_b]]
> - `_TL` — Traduções por idioma → [[pon_auc_doctypes_tl]]
> - `_VL` — View combinada (esta view)

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consultas de aplicação:** Ponto de acesso padrão para exibir tipos de documento na interface do Sourcing.
- **Relatórios e BI:** Fonte recomendada para relatórios que precisam de nomes traduzidos.
- **LOVs (List of Values):** Popula listas de seleção de tipo de negociação para o usuário.
- **Integrações:** Consumida por web services e APIs que retornam dados localizados.
- **Data dictionary unificado:** Combina configuração (regras) + apresentação (nomes traduzidos) em uma única fonte.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de documento | — | 🟢 95% |
| 2 | DOCTYPE_GROUP_NAME | VARCHAR2(30) | NOT NULL | Classificação | Grupo funcional: AUCTION, RFQ, RFI, BUYER_AUCTION (da _B) | — | 🟢 90% |
| 3 | TRANSACTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de transação (da _B) | — | 🟢 85% |
| 4 | OUTCOME | VARCHAR2(30) | NULL | Classificação | Resultado esperado: STANDARD_PO, BLANKET, CONTRACT, NONE (da _B) | — | 🟢 90% |
| 5 | DIRECTION | VARCHAR2(30) | NOT NULL | Classificação | Direção do lance (da _B) | — | 🟢 85% |
| 6 | INTERNAL_NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome interno não traduzível (da _B) | — | 🟢 85% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Flag | Tipo ativo (da _B) | — | 🟢 90% |
| 8 | DOCTYPE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome traduzido do tipo de documento (da _TL) | — | 🟢 95% |
| 9 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição traduzida (da _TL) | — | 🟢 90% |
| 10 | SCORING_FLAG | VARCHAR2(1) | NULL | Flag | Permite scoring (da _B) | — | 🟡 80% |
| 11 | BID_RANKING | VARCHAR2(30) | NULL | Regras | Critério de ranking (da _B) | — | 🟢 80% |
| 12 | PRICE_VISIBILITY_CODE | VARCHAR2(30) | NULL | Regras | Visibilidade de preços (da _B) | — | 🟢 85% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[pon_auction_headers_all]] — via `DOCTYPE_ID` (negociações que referenciam este tipo)

---

## Uso Típico

### Lista de tipos de documento ativos (traduzidos)
```sql
SELECT vl.DOCTYPE_ID, vl.DOCTYPE_NAME,
       vl.DESCRIPTION, vl.DOCTYPE_GROUP_NAME,
       vl.OUTCOME, vl.DIRECTION
FROM   PON_AUC_DOCTYPES_VL vl
WHERE  vl.ENABLED_FLAG = 'Y'
ORDER BY vl.DOCTYPE_GROUP_NAME, vl.DOCTYPE_NAME;
```

### Tipo de documento de uma negociação específica
```sql
SELECT vl.DOCTYPE_NAME, vl.DESCRIPTION,
       vl.OUTCOME, vl.BID_RANKING
FROM   PON_AUC_DOCTYPES_VL vl
JOIN   PON_AUCTION_HEADERS_ALL ah
  ON   ah.DOCTYPE_ID = vl.DOCTYPE_ID
WHERE  ah.AUCTION_HEADER_ID = :p_auction_header_id;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `DOCTYPE_GROUP_NAME = 'RFQ'` — Solicitações de cotação
- `OUTCOME = 'BLANKET'` — Tipos que geram acordo-quadro
- Idioma é filtrado automaticamente pela view (USERENV)

---

## Observações

- Esta é uma **view**, não uma tabela física — não possui storage próprio.
- A view filtra automaticamente pelo idioma da sessão (`USERENV('LANG')`), retornando apenas as traduções relevantes.
- Para consultas em idioma específico diferente da sessão, é necessário consultar diretamente `_B` + `_TL`.
- Em relatórios OTBI/BI Publisher, a Oracle recomenda uso da `_VL` ao invés de joins manuais entre `_B` e `_TL`.
- A view herda todas as colunas da `_B` e adiciona `DOCTYPE_NAME` e `DESCRIPTION` da `_TL`.
- Para migração/ETL, recomenda-se extrair a `_B` e `_TL` separadamente, já que a `_VL` depende do contexto de sessão.

---

## Referências

- [Oracle Docs — PON_AUC_DOCTYPES_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponaucdoctypesvl.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
