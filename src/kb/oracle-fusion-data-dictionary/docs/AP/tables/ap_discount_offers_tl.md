---
id: DOC-AP-005
doc_type: system-doc
title: "AP_DISCOUNT_OFFERS_TL — Traduções de Ofertas de Desconto de AP"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, discount, ofertas-desconto, traducao, multilanguage]
aliases: [AP_DISCOUNT_OFFERS_TL, ap_discount_offers_tl, discount_offers_tl, ofertas_desconto_traducao, descontos_ap_tl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_DISCOUNT_OFFERS_TL

## Visão Geral

Tabela de traduções (Translation Layer) das ofertas de desconto por pagamento antecipado no módulo de Contas a Pagar. Segue o padrão Oracle `_TL` para suporte multilíngue, armazenando nomes e descrições das ofertas de desconto em múltiplos idiomas. Cada registro é identificado pela combinação de `DISCOUNT_OFFER_ID` + `LANGUAGE`.

## Propósito de Negócio

As ofertas de desconto por pagamento antecipado são um mecanismo para incentivar fornecedores a oferecerem condições financeiras mais favoráveis em troca de antecipação de pagamento. A tabela TL permite que essas ofertas sejam exibidas no idioma local do usuário em ambientes multilíngue, garantindo clareza nas condições de desconto negociadas com fornecedores internacionais do Banco Patria.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DISCOUNT_OFFER_ID | NUMBER(15) | NOT NULL | PK/FK | Identificador da oferta de desconto. Compõe a PK com LANGUAGE. | [[ap_discount_offers_b]] | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex.: PT, US, ES). | [[fnd_languages]] | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução. | [[fnd_languages]] | 🟢 95% |
| 4 | NAME | VARCHAR2(80) | NOT NULL | Negócio | Nome da oferta de desconto no idioma especificado. | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Negócio | Descrição da oferta de desconto no idioma especificado. | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 7 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_discount_offers_b]]** — Tabela base das ofertas de desconto (via `DISCOUNT_OFFER_ID`).
- **[[fnd_languages]]** — Idiomas disponíveis no sistema (via `LANGUAGE`, `SOURCE_LANG`).

### Tabelas-filha

- Nenhuma tabela-filha conhecida.

## Uso Típico

```sql
-- Listar ofertas de desconto com nome em português
SELECT dob.DISCOUNT_OFFER_ID,
       dot.NAME,
       dot.DESCRIPTION
  FROM AP_DISCOUNT_OFFERS_B dob
  JOIN AP_DISCOUNT_OFFERS_TL dot
    ON dot.DISCOUNT_OFFER_ID = dob.DISCOUNT_OFFER_ID
   AND dot.LANGUAGE = USERENV('LANG')
 ORDER BY dot.NAME;
```

## Observações

- Tabelas `_TL` no Oracle Fusion sempre possuem registros para todos os idiomas instalados, mesmo que o conteúdo seja idêntico ao idioma-fonte.
- O campo `SOURCE_LANG` indica o idioma original; registros onde `LANGUAGE <> SOURCE_LANG` são traduções (possivelmente automáticas).
- Para consultas de usuário final, sempre filtrar por `LANGUAGE = USERENV('LANG')` para obter o idioma da sessão.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud Multilingual Architecture — TL Pattern Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISCOUNT_OFFER_ID | DiscOfferTransDiscountOfferId | — |
| LANGUAGE | DiscOfferTransLanguage | — |
| NAME | DiscountOffersTranslationName | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISCOUNT_OFFER_ID | DiscOfferTransDiscountOfferId | — |
| LANGUAGE | DiscOfferTransLanguage | — |
| NAME | DiscountOffersTranslationName | ✅ |
