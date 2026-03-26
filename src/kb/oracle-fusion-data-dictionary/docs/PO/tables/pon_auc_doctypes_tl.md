---
id: DOC-PO-008
doc_type: system-doc
title: "PON_AUC_DOCTYPES_TL — Tipos de Documento de Negociação (Traduções)"
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
  - traducoes
aliases:
  - PON_AUC_DOCTYPES_TL
  - pon_auc_doctypes_tl
  - traducoes-tipos-documento
  - sourcing-doctypes-tl
  - pon-doctypes-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUC_DOCTYPES_TL

## Visão Geral

Armazena as **traduções (nomes e descrições)** dos tipos de documento de negociação em múltiplos idiomas, seguindo o padrão Oracle MLS (Multi-Language Support). Cada registro contém a tradução de um tipo de documento (`PON_AUC_DOCTYPES_B`) para um idioma específico.

> [!note] Padrão Oracle MLS (_B/_TL/_VL)
> - `_B` — Dados base independentes de idioma → [[pon_auc_doctypes_b]]
> - `_TL` — Traduções por idioma (esta tabela)
> - `_VL` — View que combina _B + _TL → [[pon_auc_doctypes_vl]]

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização (i18n):** Suporte a múltiplos idiomas na interface de Sourcing.
- **Exibição localizada:** Nomes e descrições de tipos de documento no idioma do usuário logado.
- **Operações multi-país:** Bancos e empresas com operações internacionais visualizam o tipo de negociação no idioma local.
- **Relatórios multilíngues:** Geração de relatórios no idioma do destinatário.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCTYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Tipo de documento associado | [[pon_auc_doctypes_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex: US, PTBR, ES) | [[fnd_languages]] | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | [[fnd_languages]] | 🟢 90% |
| 4 | DOCTYPE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do tipo de documento traduzido | — | 🟢 95% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de documento traduzida | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auc_doctypes_b]] — via `DOCTYPE_ID` (dados base do tipo de documento)
- [[fnd_languages]] — via `LANGUAGE` (idioma da tradução)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha direta — tabela terminal de traduções.
- Consumida pela view [[pon_auc_doctypes_vl]] que junta `_B` + `_TL`.

---

## Uso Típico

### Traduções disponíveis para um tipo de documento
```sql
SELECT tl.DOCTYPE_ID, tl.LANGUAGE,
       tl.DOCTYPE_NAME, tl.DESCRIPTION
FROM   PON_AUC_DOCTYPES_TL tl
WHERE  tl.DOCTYPE_ID = :p_doctype_id
ORDER BY tl.LANGUAGE;
```

### Nome do tipo no idioma da sessão
```sql
SELECT tl.DOCTYPE_NAME, tl.DESCRIPTION
FROM   PON_AUC_DOCTYPES_TL tl
WHERE  tl.DOCTYPE_ID = :p_doctype_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

### Filtros comuns
- `LANGUAGE = 'US'` — Idioma inglês americano (base)
- `LANGUAGE = 'PTB'` — Português brasileiro
- `SOURCE_LANG = LANGUAGE` — Tradução direta (não herdada)

---

## Observações

- A chave primária é composta por `DOCTYPE_ID` + `LANGUAGE`.
- Quando `SOURCE_LANG <> LANGUAGE`, a tradução foi herdada de outro idioma e pode não estar validada.
- A view `PON_AUC_DOCTYPES_VL` é o método preferido para consulta — combina automaticamente `_B` + `_TL` no idioma corrente.
- Novos idiomas requerem inserção de registros nesta tabela; sem o registro, o tipo será exibido no idioma base (geralmente US/English).
- A Oracle recomenda uso da view `_VL` em relatórios e integrações, reservando acesso direto à `_TL` apenas para carga e manutenção de traduções.

---

## Referências

- [Oracle Docs — PON_AUC_DOCTYPES_TL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponaucdoctypestl.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
