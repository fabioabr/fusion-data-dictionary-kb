---
id: DOC-AR-013
doc_type: system-doc
title: "RA_TERMS_B — Condições de Pagamento (Base)"
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
  - condicoes-pagamento
  - faturamento
aliases:
  - RA_TERMS_B
  - ra_terms_b
  - condicoes-pagamento-base
  - payment-terms-base
  - termos-pagamento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_TERMS_B

## 📌 Visão Geral

Armazena a **definição base das condições de pagamento** (payment terms) utilizadas em transações de recebíveis do módulo Accounts Receivable. Cada registro representa um termo de pagamento completo — por exemplo, "Net 30", "2/10 Net 30", "50/30 50/60" — com parâmetros que controlam o cálculo de datas de vencimento, descontos por antecipação e regras de parcelamento.

Esta é a tabela **base (B)** do padrão Oracle MLS (Multi-Language Support). Os nomes e descrições traduzidos ficam em [[ra_terms_tl]], e a view [[ra_terms_vl]] combina ambas para consultas no idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de prazos de pagamento:** Define termos padrão (30, 60, 90 dias) e termos customizados por cliente ou tipo de transação.
- **Cálculo de vencimento:** Alimenta o cálculo automático de `DUE_DATE` nas parcelas (payment schedules) de faturas AR.
- **Descontos por antecipação:** Suporta termos com desconto para pagamento antecipado (ex.: 2% se pago em 10 dias).
- **Parcelamento de faturas:** Termos com múltiplas linhas (via [[ra_terms_lines]]) permitem dividir o valor em parcelas.
- **Integração inter-módulos:** Compartilhada com AP (Accounts Payable) e Purchasing para padronizar condições de pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(18) | NOT NULL | PK | Identificador único da condição de pagamento | — | 🟢 100% |
| 2 | NAME | VARCHAR2(15) | NOT NULL | Identificação | Nome curto do termo (ex.: NET 30, IMMEDIATE, 2/10 NET 30) | — | 🟢 100% |
| 3 | DUE_CUTOFF_DAY | NUMBER | NULL | Configuração | Dia de corte para cálculo de vencimento (1-28); se a data calculada exceder este dia, avança para o próximo mês | — | 🟢 100% |
| 4 | PRINTING_LEAD_DAYS | NUMBER | NULL | Impressão | Dias de antecedência para impressão da fatura em relação ao vencimento | — | 🟢 100% |
| 5 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor base para cálculo de percentuais em termos com parcelas (geralmente 100) | — | 🟢 100% |
| 6 | CALC_DISCOUNT_ON_LINES_FLAG | VARCHAR2(1) | NULL | Desconto | Calcular desconto sobre o valor das linhas (Y) ou sobre o total da fatura (N) | — | 🟢 100% |
| 7 | PARTIAL_DISCOUNT_FLAG | VARCHAR2(1) | NULL | Desconto | Permite desconto em pagamento parcial (Y/N) | — | 🟢 100% |
| 8 | FIRST_INSTALLMENT_CODE | VARCHAR2(12) | NULL | Configuração | Como tratar valores residuais na primeira parcela: ALLOCATE (distribui proporcional) ou ABSORB (primeira parcela absorve) | — | 🟢 100% |
| 9 | IN_USE | VARCHAR2(1) | NULL | Classificação | Indica se o termo está em uso por alguma transação (Y/N) — preenchido automaticamente | — | 🟢 100% |
| 10 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início da vigência do termo | — | 🟢 100% |
| 11 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de fim da vigência (NULL = sem expiração) | — | 🟢 100% |
| 12 | PREPAYMENT_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é um termo de pré-pagamento (Y/N) | — | 🟢 100% |
| 13 | BILLING_CYCLE_ID | NUMBER(18) | NULL | Configuração | Ciclo de cobrança associado | — | 🟡 65% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista (OVN) | — | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta significativa — tabela de configuração raiz.

### Tabelas-filha (FK de saída)
- [[ra_terms_lines]] — via `TERM_ID` (linhas de parcelas do termo)
- [[ra_terms_tl]] — via `TERM_ID` (traduções do nome/descrição)
- [[ra_customer_trx_all]] — via `TERM_ID` (transações que utilizam este termo)
- [[ar_payment_schedules_all]] — via `TERM_ID` (parcelas de pagamento)

### Views relacionadas

---

## 📎 Uso Típico

### Listar todos os termos de pagamento ativos
```sql
SELECT TERM_ID, NAME, BASE_AMOUNT, START_DATE_ACTIVE, END_DATE_ACTIVE
FROM   RA_TERMS_B
WHERE  NVL(END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE
ORDER BY NAME;
```

### Consultar termos com desconto por antecipação
```sql
SELECT b.TERM_ID, b.NAME, l.DISCOUNT_PERCENT, l.DISCOUNT_DAYS
FROM   RA_TERMS_B b
JOIN   RA_TERMS_LINES l ON l.TERM_ID = b.TERM_ID
WHERE  l.DISCOUNT_PERCENT > 0;
```

### Identificar termos com múltiplas parcelas
```sql
SELECT b.TERM_ID, b.NAME, COUNT(*) AS qtd_parcelas
FROM   RA_TERMS_B b
JOIN   RA_TERMS_LINES l ON l.TERM_ID = b.TERM_ID
GROUP BY b.TERM_ID, b.NAME
HAVING COUNT(*) > 1;
```

### Filtros comuns
- `END_DATE_ACTIVE IS NULL` — Termos sem data de expiração (sempre ativos)
- `IN_USE = 'Y'` — Apenas termos referenciados por transações
- `PREPAYMENT_FLAG = 'Y'` — Termos de pré-pagamento

---

## 🔒 Observações

- Esta tabela segue o padrão Oracle **MLS (Multi-Language Support)**: `_B` (base), `_TL` (translation), `_VL` (view). Para consultas com nomes traduzidos, usar [[ra_terms_vl]].
- O campo `BASE_AMOUNT` é tipicamente 100, e os valores em [[ra_terms_lines]].`RELATIVE_AMOUNT` representam percentuais desse total.
- O campo `FIRST_INSTALLMENT_CODE` resolve diferenças de arredondamento quando o valor total não divide igualmente entre as parcelas.
- Termos de pagamento são **compartilhados entre módulos** (AR, AP, Purchasing) no Oracle Fusion — uma alteração afeta todos os módulos que referenciam o mesmo `TERM_ID`.

---

## 📚 Referências

- [Oracle Docs — RA_TERMS_B](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ratermsb-10075.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
