---
id: DOC-GL-011
doc_type: system-doc
title: "GL_ENCUMBRANCE_TYPES_B — Tipos de Reserva/Comprometimento (Base)"
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
  - reserva
  - comprometimento
aliases:
  - GL_ENCUMBRANCE_TYPES_B
  - gl_encumbrance_types_b
  - tipos-reserva-gl
  - encumbrance-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ENCUMBRANCE_TYPES_B

## Visao Geral

Armazena os **tipos de reserva/comprometimento** (Encumbrance Types) na tabela base (sufixo `_B`) do General Ledger. Cada registro define um tipo de encumbrance — como Commitment (compromisso), Obligation (obrigação) ou Budget Reservation — utilizado para controle orçamentário fundwise. As traduções (nomes em diferentes idiomas) ficam na tabela [[gl_encumbrance_types_tl]].

> [!note] Padrão _B / _TL
> O Oracle Fusion usa o padrão de tabelas base (`_B`) e tradução (`_TL`) para entidades com suporte a múltiplos idiomas. A tabela `_B` contém os dados independentes de idioma, enquanto `_TL` armazena `NAME` e `DESCRIPTION` em cada idioma instalado.

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Controle orçamentário (Budgetary Control):** Define os tipos de comprometimento usados para reservar orçamento antes da despesa efetiva.
- **Encumbrance Accounting:** Suporta contabilidade de reservas — valores comprometidos (PO, requisições) são lançados como encumbrances.
- **Relatórios de disponibilidade:** Permite distinguir entre commitment (pedido de compra), obligation (fatura recebida) e outros tipos.
- **Configuração de ledger:** Os tipos de encumbrance são associados ao ledger via [[gl_balances]] (`ACTUAL_FLAG = 'E'`).
- **Auditoria:** Rastreamento dos tipos de reserva configurados no ambiente.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de reserva | — | 🟢 95% |
| 2 | ENCUMBRANCE_TYPE_KEY | VARCHAR2(30) | NOT NULL | Identificação | Chave alternativa do tipo de reserva | — | 🟡 80% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o tipo está ativo (Y/N) | — | 🟢 90% |
| 4 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 9 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[gl_encumbrance_types_tl]] — via `ENCUMBRANCE_TYPE_ID` (traduções do nome e descrição)
- [[gl_balances]] — via `ENCUMBRANCE_TYPE_ID` (saldos de encumbrance)

---

## Uso Tipico

### Listar tipos de encumbrance ativos
```sql
SELECT b.ENCUMBRANCE_TYPE_ID, tl.NAME, tl.DESCRIPTION,
       b.ENCUMBRANCE_TYPE_KEY, b.ENABLED_FLAG
FROM   GL_ENCUMBRANCE_TYPES_B b
JOIN   GL_ENCUMBRANCE_TYPES_TL tl ON tl.ENCUMBRANCE_TYPE_ID = b.ENCUMBRANCE_TYPE_ID
                                  AND tl.LANGUAGE = USERENV('LANG')
WHERE  b.ENABLED_FLAG = 'Y'
ORDER BY tl.NAME;
```

### Saldos de encumbrance por tipo
```sql
SELECT tl.NAME AS tipo_reserva,
       SUM(bal.PERIOD_NET_DR - bal.PERIOD_NET_CR) AS saldo_reserva
FROM   GL_BALANCES bal
JOIN   GL_ENCUMBRANCE_TYPES_B b ON b.ENCUMBRANCE_TYPE_ID = bal.ENCUMBRANCE_TYPE_ID
JOIN   GL_ENCUMBRANCE_TYPES_TL tl ON tl.ENCUMBRANCE_TYPE_ID = b.ENCUMBRANCE_TYPE_ID
                                  AND tl.LANGUAGE = USERENV('LANG')
WHERE  bal.ACTUAL_FLAG = 'E'
  AND  bal.LEDGER_ID = :p_ledger_id
  AND  bal.PERIOD_NAME = :p_period
GROUP BY tl.NAME;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- Join com `GL_ENCUMBRANCE_TYPES_TL` usando `LANGUAGE = USERENV('LANG')` para obter nomes traduzidos

---

## Observacoes

- A tabela `_B` contém apenas colunas independentes de idioma (`ENCUMBRANCE_TYPE_ID`, `ENABLED_FLAG`, etc.). O `NAME` e `DESCRIPTION` ficam na tabela [[gl_encumbrance_types_tl]].
- Os tipos predefinidos pelo Oracle incluem: **Commitment** (compromissos de PO), **Obligation** (obrigações de fatura) e **Budget Reservation**.
- O `ENCUMBRANCE_TYPE_ID` é referenciado em [[gl_balances]] quando `ACTUAL_FLAG = 'E'`, permitindo consultar saldos de reserva por tipo.
- Para controle orçamentário fundwise, o Oracle Fusion utiliza esses tipos para registrar reservas em diferentes estágios do ciclo de compras (requisição → PO → fatura → pagamento).

---

## Referencias

- [Oracle Docs — GL_ENCUMBRANCE_TYPES_B](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glencumbrancetypesb-25086.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL

---

## 🔗 PVOs Relacionados

### [[journalencumbranceextractpvo|JournalEncumbranceExtractPVO]] (OTHER · BICC: 9/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENABLED_FLAG | EnabledFlag | ✅ |
| ENCUMBRANCE_TYPE_CODE | EncumbranceTypeCode | ✅ |
| ENCUMBRANCE_TYPE_ID | EncumbranceTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

### [[journalencumbrancepvo|JournalEncumbrancePVO]] (GL · BICC: 2/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| ENABLED_FLAG | EnabledFlag | — |
| ENCUMBRANCE_TYPE_CODE | EncumbranceTypeCode | — |
| ENCUMBRANCE_TYPE_ID | EncumbranceTypeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
