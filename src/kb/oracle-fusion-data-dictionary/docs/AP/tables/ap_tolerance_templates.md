---
id: DOC-AP-031
doc_type: system-doc
title: "AP_TOLERANCE_TEMPLATES — Templates de Tolerância de Pagamentos"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - tolerancia
  - tolerance
  - matching
aliases:
  - AP_TOLERANCE_TEMPLATES
  - ap_tolerance_templates
  - templates-tolerancia-ap
  - ap-tolerance-templates
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TOLERANCE_TEMPLATES

## 📌 Visão Geral

Armazena os **templates de tolerância** utilizados no processo de matching (conciliação) entre faturas, pedidos de compra e recebimentos no módulo Accounts Payable. Cada template define limites (percentual e/ou valor absoluto) de variação aceitável para preço, quantidade e valor total, determinando se uma fatura pode ser aprovada automaticamente ou requer ação manual.

> [!note] Matching e Tolerância
> Os templates de tolerância são associados a fornecedores ou sites de fornecedores para controlar o nível de rigor na validação de faturas contra POs/recebimentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Three-way / Four-way matching:** Definição dos limites aceitáveis de variação entre fatura × PO × recebimento × inspeção.
- **Controle de variação de preço:** Percentual e valor máximo de diferença permitida entre preço faturado e preço do PO.
- **Controle de variação de quantidade:** Limites de sobre/subfaturamento aceitos automaticamente.
- **Automação de aprovação:** Faturas dentro da tolerância podem ser aprovadas sem intervenção manual.
- **Configuração por fornecedor/site:** Templates associados a sites de fornecedores para políticas diferenciadas.
- **Auditoria:** Rastreamento das regras de tolerância vigentes em cada período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TOLERANCE_TEMPLATE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template de tolerância | — | 🟢 95% |
| 2 | TOLERANCE_NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome do template de tolerância | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do template | — | 🟢 90% |
| 4 | PRICE_TOLERANCE | NUMBER | NULL | Tolerância | Percentual de tolerância de preço (variação aceita em %) | — | 🟢 90% |
| 5 | QUANTITY_TOLERANCE | NUMBER | NULL | Tolerância | Percentual de tolerância de quantidade | — | 🟢 90% |
| 6 | AMOUNT_TOLERANCE | NUMBER | NULL | Tolerância | Valor absoluto de tolerância monetária | — | 🟡 75% |
| 7 | GOODS_SHIP_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância para variação de quantidade recebida (shipment) | — | 🟡 70% |
| 8 | GOODS_RATE_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância de taxa/câmbio sobre mercadorias | — | 🟡 65% |
| 9 | GOODS_TOTAL_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância do valor total de mercadorias | — | 🟡 65% |
| 10 | SERVICES_SHIP_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância de variação de quantidade para serviços | — | 🟡 65% |
| 11 | SERVICES_RATE_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância de taxa para serviços | — | 🟡 65% |
| 12 | SERVICES_TOTAL_TOLERANCE | NUMBER | NULL | Tolerância | Tolerância do valor total de serviços | — | 🟡 65% |
| 13 | TAX_TOLERANCE | NUMBER | NULL | Tolerância | Percentual de tolerância para impostos | — | 🟡 70% |
| 14 | FREIGHT_TOLERANCE | NUMBER | NULL | Tolerância | Percentual de tolerância para frete | — | 🟡 70% |
| 15 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Flag indicando se o template está ativo (Y/N) | — | 🟡 75% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada — tabela de configuração standalone.

### Tabelas-filha (FK de saída)
- [[poz_supplier_sites_all_m]] — via `TOLERANCE_TEMPLATE_ID` (sites de fornecedores que utilizam este template)

---

## 📎 Uso Típico

### Listar templates de tolerância ativos
```sql
SELECT tt.TOLERANCE_TEMPLATE_ID, tt.TOLERANCE_NAME,
       tt.PRICE_TOLERANCE, tt.QUANTITY_TOLERANCE,
       tt.AMOUNT_TOLERANCE
FROM   AP_TOLERANCE_TEMPLATES tt
WHERE  NVL(tt.ENABLED_FLAG, 'Y') = 'Y';
```

### Templates com tolerância de preço acima de 5%
```sql
SELECT tt.TOLERANCE_NAME, tt.PRICE_TOLERANCE,
       tt.QUANTITY_TOLERANCE
FROM   AP_TOLERANCE_TEMPLATES tt
WHERE  tt.PRICE_TOLERANCE > 5;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Templates ativos
- `PRICE_TOLERANCE IS NOT NULL` — Templates com limite de preço definido

---

## 🔒 Observações

- Templates de tolerância são tipicamente criados na configuração inicial do módulo AP e associados a sites de fornecedores.
- Quando não há template associado, o sistema utiliza os parâmetros de tolerância definidos em [[ap_system_parameters_all]].
- A tolerância pode ser definida em **percentual** (variação relativa) ou **valor absoluto** (variação monetária), ou ambos — o mais restritivo prevalece.
- Alterações em templates existentes **não retroagem** a faturas já validadas ou em holds.

---

## 📚 Referências

- [Oracle Docs — AP Tolerance Templates](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/aptolerancetemplates.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
