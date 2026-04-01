---
id: DOC-AR-014
doc_type: system-doc
title: "RA_TERMS_LINES — Linhas das Condições de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - payment-terms
  - parcelas
  - cronograma-pagamento
aliases:
  - RA_TERMS_LINES
  - ra_terms_lines
  - linhas-condicoes-pagamento
  - payment-terms-lines
  - parcelas-pagamento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_TERMS_LINES

## 📌 Visão Geral

Armazena as **linhas de detalhe de cada condição de pagamento**, permitindo que um único termo possua **múltiplas parcelas** com percentuais, prazos e descontos distintos. Cada registro representa uma parcela (installment) do termo de pagamento definido em [[ra_terms_b]].

Por exemplo, um termo "50/30 50/60" terá duas linhas: uma com 50% do valor vencendo em 30 dias e outra com 50% vencendo em 60 dias.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Parcelamento de faturas:** Define o cronograma de parcelas — cada linha gera uma entrada em [[ar_payment_schedules_all]] quando a transação é criada.
- **Cálculo de datas de vencimento:** Cada parcela pode ter sua própria regra de vencimento (dias corridos, dia fixo do mês, meses adiante).
- **Descontos por antecipação:** Cada parcela pode oferecer um desconto diferente com prazo próprio.
- **Distribuição de valores:** O campo `RELATIVE_AMOUNT` define o percentual do valor total alocado a cada parcela.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da condição de pagamento (parte da PK composta) | [[ra_terms_b]] | 🟢 100% |
| 2 | SEQUENCE_NUM | NUMBER | NOT NULL | PK | Número sequencial da parcela (parte da PK composta; 1, 2, 3…) | — | 🟢 100% |
| 3 | RELATIVE_AMOUNT | NUMBER | NOT NULL | Financeiro | Percentual relativo ao `BASE_AMOUNT` de [[ra_terms_b]] — ex.: 50 = 50% do valor total | — | 🟢 100% |
| 4 | DUE_DAYS | NUMBER | NULL | Vencimento | Dias corridos após a data da transação para vencimento desta parcela | — | 🟢 100% |
| 5 | DUE_DATE | DATE | NULL | Vencimento | Data fixa de vencimento (usado quando o vencimento não é relativo) | — | 🟡 75% |
| 6 | DUE_MONTHS_FORWARD | NUMBER | NULL | Vencimento | Meses à frente da data da transação para cálculo de vencimento | — | 🟢 100% |
| 7 | DUE_DAY_OF_MONTH | NUMBER | NULL | Vencimento | Dia fixo do mês para vencimento (1-31); combinado com `DUE_MONTHS_FORWARD` | — | 🟢 100% |
| 8 | DISCOUNT_DAYS | NUMBER | NULL | Desconto | Dias corridos para elegibilidade ao desconto por antecipação | — | 🟢 100% |
| 9 | DISCOUNT_MONTHS_FORWARD | NUMBER | NULL | Desconto | Meses à frente para prazo de desconto | — | 🟢 100% |
| 10 | DISCOUNT_DAY_OF_MONTH | NUMBER | NULL | Desconto | Dia fixo do mês para limite do desconto | — | 🟢 100% |
| 11 | DISCOUNT_PERCENT | NUMBER | NULL | Desconto | Percentual de desconto por pagamento antecipado (ex.: 2 = 2%) | — | 🟢 100% |
| 12 | DISCOUNT_PERCENT_2 | NUMBER | NULL | Desconto | Segundo nível de desconto (menor percentual, prazo mais longo) | — | 🟢 100% |
| 13 | DISCOUNT_DAYS_2 | NUMBER | NULL | Desconto | Dias corridos para o segundo nível de desconto | — | 🟢 100% |
| 14 | DISCOUNT_PERCENT_3 | NUMBER | NULL | Desconto | Terceiro nível de desconto | — | 🟢 100% |
| 15 | DISCOUNT_DAYS_3 | NUMBER | NULL | Desconto | Dias corridos para o terceiro nível de desconto | — | 🟢 100% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista (OVN) | — | 🟢 100% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 21 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_terms_b]] — via `TERM_ID` (condição de pagamento à qual esta linha pertence)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consultar o cronograma completo de um termo de pagamento
```sql
SELECT b.NAME, l.SEQUENCE_NUM, l.RELATIVE_AMOUNT,
       l.DUE_DAYS, l.DUE_MONTHS_FORWARD, l.DUE_DAY_OF_MONTH,
       l.DISCOUNT_PERCENT, l.DISCOUNT_DAYS
FROM   RA_TERMS_B b
JOIN   RA_TERMS_LINES l ON l.TERM_ID = b.TERM_ID
WHERE  b.NAME = 'NET 30'
ORDER BY l.SEQUENCE_NUM;
```

### Listar todos os termos que oferecem desconto
```sql
SELECT DISTINCT b.TERM_ID, b.NAME, l.DISCOUNT_PERCENT, l.DISCOUNT_DAYS
FROM   RA_TERMS_B b
JOIN   RA_TERMS_LINES l ON l.TERM_ID = b.TERM_ID
WHERE  l.DISCOUNT_PERCENT > 0
ORDER BY b.NAME;
```

### Simular datas de vencimento para uma transação
```sql
SELECT l.SEQUENCE_NUM AS parcela,
       l.RELATIVE_AMOUNT AS pct_valor,
       :p_trx_date + l.DUE_DAYS AS data_vencimento,
       l.DISCOUNT_PERCENT AS desconto_pct,
       :p_trx_date + l.DISCOUNT_DAYS AS limite_desconto
FROM   RA_TERMS_LINES l
WHERE  l.TERM_ID = :p_term_id
ORDER BY l.SEQUENCE_NUM;
```

### Filtros comuns
- `TERM_ID = :p_term_id` — Linhas de um termo específico
- `DISCOUNT_PERCENT > 0` — Apenas parcelas com desconto
- `SEQUENCE_NUM = 1` — Primeira parcela (termos simples têm apenas esta)

---

## 🔒 Observações

- A chave primária é composta: (`TERM_ID`, `SEQUENCE_NUM`). Cada combinação representa uma parcela única do termo.
- A soma de `RELATIVE_AMOUNT` de todas as linhas de um `TERM_ID` deve ser igual ao `BASE_AMOUNT` em [[ra_terms_b]] (tipicamente 100).
- Os campos de vencimento são mutuamente exclusivos por abordagem: use `DUE_DAYS` para dias corridos **ou** `DUE_MONTHS_FORWARD` + `DUE_DAY_OF_MONTH` para dia fixo do mês.
- O Oracle suporta até **três níveis de desconto** por parcela (DISCOUNT_PERCENT, DISCOUNT_PERCENT_2, DISCOUNT_PERCENT_3), cada um com seu próprio prazo.
- Termos simples (ex.: "NET 30") possuem apenas uma linha com `SEQUENCE_NUM = 1` e `RELATIVE_AMOUNT = 100`.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PaymentTermLineObjectVersionNumber9 | — |
| SEQUENCE_NUM | PaymentTermLineSequenceNum | ✅ |
| TERM_ID | PaymentTermBPEOTermId | — |
| TERM_ID | PaymentTermLineTermId1 | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PaymentTermLineObjectVersionNumber6 | — |
| SEQUENCE_NUM | PaymentTermLineSequenceNum | ✅ |
| TERM_ID | PaymentTermBPEOTermId | — |

### [[paymenttermlineextractpvo|PaymentTermLineExtractPVO]] (OTHER · BICC: 15/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | RaTermsLineAttribute1 | — |
| ATTRIBUTE10 | RaTermsLineAttribute10 | — |
| ATTRIBUTE11 | RaTermsLineAttribute11 | — |
| ATTRIBUTE12 | RaTermsLineAttribute12 | — |
| ATTRIBUTE13 | RaTermsLineAttribute13 | — |
| ATTRIBUTE14 | RaTermsLineAttribute14 | — |
| ATTRIBUTE15 | RaTermsLineAttribute15 | — |
| ATTRIBUTE2 | RaTermsLineAttribute2 | — |
| ATTRIBUTE3 | RaTermsLineAttribute3 | — |
| ATTRIBUTE4 | RaTermsLineAttribute4 | — |
| ATTRIBUTE5 | RaTermsLineAttribute5 | — |
| ATTRIBUTE6 | RaTermsLineAttribute6 | — |
| ATTRIBUTE7 | RaTermsLineAttribute7 | — |
| ATTRIBUTE8 | RaTermsLineAttribute8 | — |
| ATTRIBUTE9 | RaTermsLineAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaTermsLineAttributeCategory | — |
| CREATED_BY | RaTermsLineCreatedBy | ✅ |
| CREATION_DATE | RaTermsLineCreationDate | ✅ |
| DUE_DATE | RaTermsLineDueDate | ✅ |
| DUE_DAY_OF_MONTH | RaTermsLineDueDayOfMonth | ✅ |
| DUE_DAYS | RaTermsLineDueDays | ✅ |
| DUE_MONTHS_FORWARD | RaTermsLineDueMonthsForward | ✅ |
| LAST_UPDATE_DATE | RaTermsLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaTermsLineLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaTermsLineLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | RaTermsLineObjectVersionNumber | ✅ |
| RELATIVE_AMOUNT | RaTermsLineRelativeAmount | ✅ |
| SEED_DATA_SOURCE | RaTermsLineSeedDataSource | ✅ |
| SEQUENCE_NUM | RaTermsLineSequenceNum | ✅ |
| SET_ID | RaTermsLineSetId | ✅ |
| TERM_ID | RaTermsLineTermId | ✅ |

### [[paymenttermlinepvo|PaymentTermLinePVO]] (AR · BICC: 8/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PaymentTermLineCreatedBy | — |
| CREATION_DATE | PaymentTermLineCreationDate | — |
| DUE_DATE | PaymentTermLineDueDate | — |
| DUE_DAY_OF_MONTH | PaymentTermLineDueDayOfMonth | ✅ |
| DUE_DAYS | PaymentTermLineDueDays | ✅ |
| DUE_MONTHS_FORWARD | PaymentTermLineDueMonthsForward | ✅ |
| LAST_UPDATE_DATE | PaymentTermLineLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentTermLineLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentTermLineLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PaymentTermLineObjectVersionNumber | — |
| RELATIVE_AMOUNT | PaymentTermLineRelativeAmount | ✅ |
| SEQUENCE_NUM | SequenceNum | ✅ |
| SET_ID | PaymentTermLineSetId | ✅ |
| TERM_ID | TermId | ✅ |

---

## 📚 Referências

- [Oracle Docs — RA_TERMS_LINES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ratermslines-25284.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
