---
id: DOC-GL-009
doc_type: system-doc
title: "GL_DAILY_CONVERSION_TYPES — Tipos de Conversão Cambial Diária"
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
  - cambio
  - conversao
  - moeda
aliases:
  - GL_DAILY_CONVERSION_TYPES
  - gl_daily_conversion_types
  - tipos-conversao-cambial
  - daily-conversion-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_DAILY_CONVERSION_TYPES

## Visao Geral

Armazena os **tipos de conversão cambial** disponíveis para taxas de câmbio diárias no General Ledger. Cada registro define um tipo de taxa (Spot, Corporate, User, etc.) que pode ser utilizado na conversão de transações entre moedas. Esses tipos são referenciados pela tabela [[gl_daily_rates]] e por todas as transações multi-moeda do ERP.

> [!note] Tipos predefinidos
> O Oracle Fusion inclui tipos de conversão padrão como **Spot**, **Corporate** e **User**. A organização pode criar tipos adicionais conforme suas necessidades (ex: "BACEN" para taxa do Banco Central).

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Conversão de moedas:** Define quais tipos de taxa estão disponíveis para conversão de transações (AP, AR, GL).
- **Cotação diária:** Cada tipo pode ter taxas diferentes carregadas diariamente na [[gl_daily_rates]].
- **Política cambial:** Permite definir tipos corporativos (taxa interna) vs. tipos de mercado (spot).
- **Relatórios multi-moeda:** Referência para revalorizações e translations de saldos.
- **Integração:** Tipos de conversão são usados por todos os módulos financeiros (AP, AR, FA, etc.).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONVERSION_TYPE | VARCHAR2(30) | NOT NULL | PK | Código do tipo de conversão (ex: Spot, Corporate, User) | — | 🟢 95% |
| 2 | USER_CONVERSION_TYPE | VARCHAR2(30) | NOT NULL | Identificação | Nome amigável do tipo de conversão | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de conversão | — | 🟢 90% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o tipo está ativo (Y/N) | — | 🟢 85% |
| 5 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟡 70% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[gl_daily_rates]] — via `CONVERSION_TYPE` (taxas de câmbio diárias associadas)

---

## Uso Tipico

### Listar tipos de conversão ativos
```sql
SELECT dct.CONVERSION_TYPE, dct.USER_CONVERSION_TYPE,
       dct.DESCRIPTION
FROM   GL_DAILY_CONVERSION_TYPES dct
WHERE  dct.ENABLED_FLAG = 'Y'
ORDER BY dct.USER_CONVERSION_TYPE;
```

### Verificar se existe tipo corporativo
```sql
SELECT dct.CONVERSION_TYPE, dct.USER_CONVERSION_TYPE
FROM   GL_DAILY_CONVERSION_TYPES dct
WHERE  dct.CONVERSION_TYPE = 'Corporate'
  AND  dct.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `CONVERSION_TYPE = 'Spot'` — Taxa spot (mercado)
- `CONVERSION_TYPE = 'Corporate'` — Taxa corporativa (interna)
- `CONVERSION_TYPE = 'User'` — Taxa definida pelo usuário na transação

---

## Observacoes

- Os tipos **Spot**, **Corporate** e **User** são predefinidos pelo Oracle e não devem ser removidos.
- O tipo **User** é especial — permite que o usuário informe a taxa manualmente na transação, sem depender de taxas carregadas na [[gl_daily_rates]].
- Tipos customizados (ex: "BACEN", "ECB") podem ser criados para representar fontes específicas de cotação.
- O `CONVERSION_TYPE` é o código interno (usado em joins), enquanto `USER_CONVERSION_TYPE` é o nome exibido na interface.
- Todos os módulos financeiros (AP, AR, FA, Projects) referenciam esta tabela para conversão de moedas em transações.

---

## Referencias

- [Oracle Docs — GL_DAILY_CONVERSION_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gldailyconversiontypes-25080.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
