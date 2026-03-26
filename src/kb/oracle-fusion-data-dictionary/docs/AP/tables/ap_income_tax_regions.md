---
id: DOC-AP-009
doc_type: system-doc
title: "AP_INCOME_TAX_REGIONS — Regiões de Imposto de Renda de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, income-tax, regioes-imposto, withholding, tributacao]
aliases: [AP_INCOME_TAX_REGIONS, ap_income_tax_regions, income_tax_regions, regioes_imposto_ap, tax_regions_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INCOME_TAX_REGIONS

## Visão Geral

Tabela de definição das regiões fiscais de imposto de renda utilizadas no módulo de Contas a Pagar para fins de retenção na fonte (withholding tax) e geração de declarações fiscais (ex.: 1099 nos EUA, DIRF no Brasil). Cada registro representa uma região ou jurisdição fiscal com suas regras de retenção aplicáveis.

## Propósito de Negócio

As regiões de imposto de renda são essenciais para o cumprimento das obrigações acessórias de retenção na fonte. No contexto do Banco Patria, as regiões fiscais são utilizadas para classificar pagamentos a fornecedores conforme a jurisdição tributária, possibilitando a correta retenção de IR, CSLL, PIS, COFINS e geração de declarações como DIRF e EFD-Reinf. A configuração correta garante compliance com a Receita Federal.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REGION_SHORT_NAME | VARCHAR2(10) | NOT NULL | PK | Chave primária. Código abreviado da região fiscal (ex.: SP, RJ, MG). | — | 🟢 95% |
| 2 | REGION_LONG_NAME | VARCHAR2(80) | NOT NULL | Negócio | Nome completo da região fiscal. | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Negócio | Descrição da região fiscal. | — | 🟢 90% |
| 4 | NUM_OF_WAGE_BRACKET_ROWS | NUMBER(5) | NULL | Negócio | Número de faixas salariais/valores para cálculo. | — | 🟡 65% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a região está ativa (Y/N). | — | 🟡 75% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 7 | ATTRIBUTE1 | VARCHAR2(150) | NULL | DFF | Atributo descritivo flexível 1. | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 9 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- Nenhuma FK direta conhecida. Tabela raiz de configuração fiscal.

### Tabelas-filha

- **[[ap_income_tax_types]]** — Tipos de imposto de renda associados a esta região (via `REGION_SHORT_NAME`).
- **[[poz_supplier_sites_all]]** — Sites de fornecedores que referenciam a região fiscal (via `INCOME_TAX_REGION`).

## Uso Típico

```sql
-- Listar regiões fiscais ativas
SELECT itr.REGION_SHORT_NAME,
       itr.REGION_LONG_NAME,
       itr.DESCRIPTION
  FROM AP_INCOME_TAX_REGIONS itr
 WHERE NVL(itr.ACTIVE_FLAG, 'Y') = 'Y'
 ORDER BY itr.REGION_SHORT_NAME;
```

## Observações

- A estrutura desta tabela é fortemente orientada ao modelo fiscal americano (1099/1042-S); para o Brasil, funcionalidades de withholding tax podem estar em módulos complementares (Oracle Tax).
- As regiões fiscais são associadas a sites de fornecedores, não diretamente a faturas.
- Alterações em regiões fiscais podem impactar retroativamente relatórios de compliance fiscal — recomenda-se cautela.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud Tax — Income Tax Regions Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
