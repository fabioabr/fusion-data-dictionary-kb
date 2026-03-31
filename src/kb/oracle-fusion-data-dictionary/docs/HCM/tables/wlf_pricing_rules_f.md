---
id: DOC-HCM-746
doc_type: system-doc
title: "WLF_PRICING_RULES_F — Regras de Precificação (Learning)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - learning
  - workforce-learning
  - regras-precificação
aliases:
  - WLF_PRICING_RULES_F
  - wlf_pricing_rules_f
  - wlf-pricing-rules-f
  - regras-precificação-learning
  - pricing-rules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_PRICING_RULES_F

## Visão Geral

Armazena as **regras de precificação** aplicáveis aos itens de aprendizado, definindo critérios para descontos, isenções e ajustes de preço. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Política de preços** — define regras de precificação por perfil, volume ou condição.
- **Descontos** — regras de desconto para grupos específicos de colaboradores.
- **Isenções** — critérios de isenção de custos (ex.: treinamentos obrigatórios).
- **Cobrança diferenciada** — preços diferentes por departamento ou filial.
- **Gestão financeira** — controle de políticas de custo de treinamento.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PRICING_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | RULE_NAME | VARCHAR2(240) | NULL | Identificação | Nome da regra de precificação | — | 🟡 75% |
| 5 | RULE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da regra (discount, exemption, surcharge) | — | 🟡 70% |
| 6 | DISCOUNT_PERCENTAGE | NUMBER(5,2) | NULL | Financeiro | Percentual de desconto | — | 🟡 65% |
| 7 | FIXED_AMOUNT | NUMBER(15,2) | NULL | Financeiro | Valor fixo de ajuste | — | 🟡 65% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 9 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a regra está ativa (Y/N) | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai direta identificada.

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Regras de precificação ativas
```sql
SELECT pr.RULE_NAME, pr.RULE_TYPE, pr.DISCOUNT_PERCENTAGE, pr.FIXED_AMOUNT
FROM   WLF_PRICING_RULES_F pr
WHERE  pr.ACTIVE_FLAG = 'Y'
  AND  SYSDATE BETWEEN pr.EFFECTIVE_START_DATE AND pr.EFFECTIVE_END_DATE
ORDER BY pr.RULE_NAME;
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Apenas regras ativas
- `RULE_TYPE = 'DISCOUNT'` — Apenas regras de desconto

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Regras podem ser aplicadas a itens específicos ou ao catálogo inteiro.
- DISCOUNT_PERCENTAGE e FIXED_AMOUNT podem ser mutuamente exclusivos.

---

## Referências

- [Oracle Docs — WLF_PRICING_RULES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfpricingrulesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[learningpricingrulespvo|LearningPricingRulesPVO]] (HCM · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | LearningPricingRulesDEOCreatedBy | — |
| CREATION_DATE | LearningPricingRulesDEOCreationDate | — |
| CURRENCY | LearningPricingRulesDEOCurrency | ✅ |
| DELIVERY_MODE | LearningPricingRulesDEODeliveryMode | — |
| EFFECTIVE_END_DATE | LearningPricingRulesDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | LearningPricingRulesDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | LearningPricingRulesDEOEnterpriseId | — |
| LAST_UPDATE_DATE | LearningPricingRulesDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LearningPricingRulesDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | LearningPricingRulesDEOLastUpdatedBy | — |
| LEARNING_ITEM_TYPE | LearningPricingRulesDEOLearningItemType | — |
| OBJECT_VERSION_NUMBER | LearningPricingRulesDEOObjectVersionNumber | — |
| PRICE_LOCK_TYPE | LearningPricingRulesDEOPriceLockType | — |
| PRICING_RULE_ID | LearningPricingRulesDEOPricingRuleId | ✅ |
| TOTAL_PRICE | LearningPricingRulesDEOTotalPrice | ✅ |
| USAGE | LearningPricingRulesDEOUsage | — |
| USES_PRICING | LearningPricingRulesDEOUsesPricing | — |
