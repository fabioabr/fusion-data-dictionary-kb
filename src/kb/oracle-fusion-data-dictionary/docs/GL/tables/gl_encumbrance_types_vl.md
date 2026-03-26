---
id: DOC-GL-013
doc_type: system-doc
title: "GL_ENCUMBRANCE_TYPES_VL — Tipos de Reserva (View com Tradução)"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - encumbrance
  - reservas
  - view-traduzida
aliases:
  - GL_ENCUMBRANCE_TYPES_VL
  - gl_encumbrance_types_vl
  - tipos-reserva-vl
  - encumbrance-types-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ENCUMBRANCE_TYPES_VL

## 📌 Visão Geral

View que combina a tabela base `GL_ENCUMBRANCE_TYPES_B` com a tabela de traduções `GL_ENCUMBRANCE_TYPES_TL`, retornando os **tipos de reserva (encumbrance)** com nome e descrição traduzidos para o idioma da sessão do usuário. É a view recomendada para consultas de front-end e relatórios que precisam exibir o nome do tipo de reserva no idioma correto.

> [!note] Sufixo _VL
> O sufixo `_VL` (View Layer) indica uma view que junta a tabela base (`_B`) com a tabela de traduções (`_TL`), filtrando pelo idioma da sessão (`USERENV('LANG')`).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Configuração de reservas:** Exibição dos tipos de encumbrance disponíveis com nome traduzido.
- **Relatórios financeiros:** Apresentação dos nomes de reservas em relatórios multi-idioma.
- **Consulta de saldos de reserva:** Resolução do nome do tipo de encumbrance referenciado em `GL_BALANCES`.
- **LOV (List of Values):** População de listas de seleção em interfaces de lançamento e consulta.
- **Auditoria:** Identificação legível dos tipos de reserva em análises contábeis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de reserva | — | 🟢 100% |
| 2 | ENCUMBRANCE_TYPE_KEY | VARCHAR2(30) | NOT NULL | Identificação | Chave alfanumérica do tipo de reserva | — | 🟡 75% |
| 3 | ENCUMBRANCE_TYPE | VARCHAR2(30) | NOT NULL | Identificação | Nome traduzido do tipo de reserva (idioma da sessão) | — | 🟢 95% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição traduzida do tipo de reserva | — | 🟢 95% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o tipo está ativo (Y/N) | — | 🟢 90% |
| 6 | LANGUAGE | VARCHAR2(4) | NOT NULL | i18n | Código do idioma da tradução | — | 🟢 95% |
| 7 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | i18n | Idioma de origem da tradução | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[gl_balances]] — via `ENCUMBRANCE_TYPE_ID` (saldos de reserva referenciam o tipo)

---

## 📎 Uso Típico

### Listar tipos de reserva ativos
```sql
SELECT et.ENCUMBRANCE_TYPE_ID,
       et.ENCUMBRANCE_TYPE,
       et.DESCRIPTION
FROM   GL_ENCUMBRANCE_TYPES_VL et
WHERE  et.ENABLED_FLAG = 'Y'
ORDER BY et.ENCUMBRANCE_TYPE;
```

### Saldos de reserva com nome do tipo
```sql
SELECT b.PERIOD_NAME,
       et.ENCUMBRANCE_TYPE,
       (b.BEGIN_BALANCE_DR + b.PERIOD_NET_DR) - (b.BEGIN_BALANCE_CR + b.PERIOD_NET_CR) AS saldo_reserva
FROM   GL_BALANCES b
JOIN   GL_ENCUMBRANCE_TYPES_VL et ON et.ENCUMBRANCE_TYPE_ID = b.ENCUMBRANCE_TYPE_ID
WHERE  b.ACTUAL_FLAG = 'E'
  AND  b.LEDGER_ID = :p_ledger_id
  AND  b.PERIOD_NAME = 'MAR-26';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Apenas tipos ativos
- `LANGUAGE = 'PTB'` — Tradução em português brasileiro

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física. Dados originam de `GL_ENCUMBRANCE_TYPES_B` (base) e `GL_ENCUMBRANCE_TYPES_TL` (traduções).
- O filtro de idioma é aplicado automaticamente pela view usando `USERENV('LANG')`.
- Tipos de encumbrance comuns incluem: **Commitment** (compromissos de compra), **Obligation** (obrigações) e tipos customizados por implementação.
- O `ENCUMBRANCE_TYPE_ID` é referenciado em `GL_BALANCES` quando `ACTUAL_FLAG = 'E'`.

---

## 📚 Referências

- [Oracle Docs — GL_ENCUMBRANCE_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glencumbrancetypes-25766.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
