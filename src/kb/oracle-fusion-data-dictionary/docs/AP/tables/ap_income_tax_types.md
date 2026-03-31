---
id: DOC-AP-010
doc_type: system-doc
title: "AP_INCOME_TAX_TYPES — Tipos de Imposto de Renda de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, income-tax, tipos-imposto, withholding, tributacao]
aliases: [AP_INCOME_TAX_TYPES, ap_income_tax_types, income_tax_types, tipos_imposto_ap, tax_types_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INCOME_TAX_TYPES

## Visão Geral

Tabela de definição dos tipos de imposto de renda disponíveis no módulo de Contas a Pagar para classificação de retenções na fonte. Cada registro representa um tipo de imposto (ex.: rents, royalties, serviços, dividendos) que pode ser associado a fornecedores e faturas para fins de retenção e declarações fiscais.

## Propósito de Negócio

Os tipos de imposto de renda classificam a natureza dos pagamentos sujeitos a retenção na fonte, permitindo a correta apuração e declaração de impostos retidos. No Banco Patria, essa classificação é utilizada para identificar o tipo de rendimento pago a fornecedores (serviços profissionais, aluguéis, comissões) e aplicar as alíquotas de retenção adequadas conforme a legislação tributária brasileira.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INCOME_TAX_TYPE | VARCHAR2(10) | NOT NULL | PK | Chave primária. Código do tipo de imposto (ex.: MISC, NEC, RENTS). | — | 🟢 95% |
| 2 | DESCRIPTION | VARCHAR2(80) | NOT NULL | Negócio | Descrição do tipo de imposto. | — | 🟢 95% |
| 3 | INCOME_TAX_NAME | VARCHAR2(80) | NULL | Negócio | Nome completo do tipo de imposto. | — | 🟡 75% |
| 4 | REGION_SHORT_NAME | VARCHAR2(10) | NULL | FK | Região fiscal associada a este tipo de imposto. | [[ap_income_tax_regions]] | 🟡 70% |
| 5 | BOX_NUMBER | VARCHAR2(10) | NULL | Negócio | Número da caixa no formulário fiscal (ex.: Box 1, Box 7 do 1099). | — | 🟢 85% |
| 6 | TAX_RATE | NUMBER | NULL | Negócio | Alíquota padrão de retenção (percentual). | — | 🟡 70% |
| 7 | REPORTING_LIMIT | NUMBER | NULL | Negócio | Valor mínimo para obrigatoriedade de declaração. | — | 🟡 65% |
| 8 | INACTIVE_DATE | DATE | NULL | Controle | Data de inativação do tipo de imposto. | — | 🟢 90% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_income_tax_regions]]** — Região fiscal à qual este tipo de imposto pertence (via `REGION_SHORT_NAME`).

### Tabelas-filha

- **[[poz_suppliers]]** — Fornecedores classificados com este tipo de imposto (via `FEDERAL_REPORTABLE_TYPE` ou campo equivalente).
- **[[ap_invoices_all]]** — Faturas com classificação de tipo de imposto para retenção (via `INCOME_TAX_TYPE`).

## Uso Típico

```sql
-- Listar tipos de imposto ativos com suas regiões
SELECT itt.INCOME_TAX_TYPE,
       itt.DESCRIPTION,
       itt.BOX_NUMBER,
       itt.TAX_RATE,
       itr.REGION_LONG_NAME
  FROM AP_INCOME_TAX_TYPES itt
  LEFT JOIN AP_INCOME_TAX_REGIONS itr
    ON itr.REGION_SHORT_NAME = itt.REGION_SHORT_NAME
 WHERE (itt.INACTIVE_DATE IS NULL OR itt.INACTIVE_DATE > SYSDATE)
 ORDER BY itt.INCOME_TAX_TYPE;
```

## Observações

- Esta tabela é fortemente orientada ao modelo fiscal americano (1099-MISC, 1099-NEC); para o Brasil, a classificação de retenções pode exigir configuração complementar no Oracle Tax.
- O campo `BOX_NUMBER` refere-se à posição no formulário 1099 — no contexto brasileiro, pode ser mapeado para categorias da DIRF.
- Tipos de imposto inativos não aparecem em LOVs, mas mantêm referencial histórico para declarações anteriores.
- A alíquota (`TAX_RATE`) é referencial — a retenção efetiva pode ser calculada com base em regras mais complexas do módulo Tax.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud Tax — Withholding Tax Configuration Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[supplierpvo|SupplierPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | IncomeTaxTypeDescription | ✅ |
| INCOME_TAX_TYPE | IncomeTaxTypeIncomeTaxType1 | — |
