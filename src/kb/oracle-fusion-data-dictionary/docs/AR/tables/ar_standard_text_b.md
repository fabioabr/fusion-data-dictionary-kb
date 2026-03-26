---
id: DOC-AR-058
doc_type: system-doc
title: "AR_STANDARD_TEXT_B — Textos Padrão do AR"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, standard-text, textos-padrao, dunning]
aliases: [AR_STANDARD_TEXT_B, ar_standard_text_b, standard_text_b, textos_padrao_ar, ar_std_text]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_STANDARD_TEXT_B

## 📌 Visão Geral

Tabela base (sufixo `_B`) de **textos padrão** do AR. Armazena blocos de texto reutilizáveis para inclusão em faturas, dunning letters (cartas de cobrança), statements e outros documentos gerados pelo módulo.

## 🧠 Propósito de Negócio

Os textos padrão eliminam a necessidade de redigir textos repetitivos a cada documento. São especialmente úteis em cartas de cobrança progressiva (dunning letters), onde cada nível de cobrança tem um texto diferente — do lembrete gentil à notificação de protesto.

Casos de uso principais:
- Textos para dunning letters (1a, 2a, 3a cobrança)
- Notas em faturas (termos e condições)
- Mensagens em statements de cliente
- Textos de comunicação padronizados

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | STANDARD_TEXT_ID | NUMBER | PK. Identificador único do texto padrão. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome do texto padrão (identificador legível). | Identificação | 🟢 100% |
| 3 | TEXT | CLOB/VARCHAR2 | Conteúdo do texto padrão. | Conteúdo | 🟢 100% |
| 4 | START_DATE | DATE | Data de início de vigência. | Vigência | 🟢 100% |
| 5 | END_DATE | DATE | Data de fim de vigência (nulo = sem expiração). | Vigência | 🟢 100% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 7 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 9 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_standard_text_tl]] | STANDARD_TEXT_ID | Referenciada por | Traduções do texto padrão |
| [[ar_dunning_letter_sets]] | — | Referência | Conjuntos de dunning usam textos padrão |

## 📎 Uso Típico

```sql
-- Listar textos padrão ativos
SELECT standard_text_id,
       name,
       text,
       start_date,
       end_date
  FROM ar_standard_text_b
 WHERE (end_date IS NULL OR end_date > SYSDATE)
 ORDER BY name;
```

```sql
-- Buscar texto padrão por nome
SELECT standard_text_id,
       name,
       text
  FROM ar_standard_text_b
 WHERE UPPER(name) LIKE '%COBRANCA%'
   AND (end_date IS NULL OR end_date > SYSDATE);
```

## 🔒 Observações

- A tabela `_B` contém os dados base. Para textos traduzidos, consultar [[ar_standard_text_tl]].
- O campo `TEXT` pode conter **variáveis de substituição** (merge fields) que são resolvidas em tempo de impressão (ex: nome do cliente, valor da fatura).
- Textos padrão são **compartilhados** entre todas as BUs (não particionados por ORG_ID).
- Desativar um texto (`END_DATE` no passado) impede novos usos mas não afeta documentos já gerados.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Standard Text View Object
- Oracle Fusion Cloud — Setting Up Standard Messages (Configuration Guide)
