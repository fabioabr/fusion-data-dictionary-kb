# Oracle Fusion — Accounts Payable (AP) — Database Tables

> Referência de tabelas do módulo AP extraídas do BICC Database Mapping (Release 13/25A).
> Fonte: documentação oficial Oracle Fusion Cloud ERP.

---

## Sumário de Grupos

| Grupo | Qtd | Prefixo Principal |
|-------|-----|--------------------|
| [Faturas (Invoices)](#1-faturas-invoices) | 7 | `AP_INVOICE*`, `AP_INV_*` |
| [Pagamentos (Payments)](#2-pagamentos-payments) | 6 | `AP_CHECKS*`, `AP_PAYMENT*` |
| [Holds e Aprovações](#3-holds-e-aprovações) | 3 | `AP_HOLDS*`, `AP_HOLD_*`, `AP_INV_APRVL*` |
| [Pré-pagamento (Prepayment)](#4-pré-pagamento-prepayment) | 1 | `AP_PREPAY*` |
| [Condições de Pagamento (Payment Terms)](#5-condições-de-pagamento-payment-terms) | 4 | `AP_TERMS*` |
| [Aging e Trial Balance](#6-aging-e-trial-balance) | 3 | `AP_AGING*`, `AP_TRIAL*` |
| [Configuração e Parâmetros](#7-configuração-e-parâmetros) | 4 | `AP_SYSTEM*`, `AP_DISTRIBUTION*`, `AP_LOOKUP*`, `AP_BATCHES*` |
| [Reconciliação](#8-reconciliação) | 3 | `AP_RECON*` |
| [Impostos (Tax — E-Business Tax)](#9-impostos-tax--e-business-tax) | 22 | `ZX_*` |
| [Despesas (Expenses)](#10-despesas-expenses) | 5 | `EXM_*` |
| [Fornecedores (Suppliers)](#11-fornecedores-suppliers) | 2 | `POZ_*` |
| [Pedidos de Compra (Purchase Orders)](#12-pedidos-de-compra-purchase-orders) | 8 | `PO_*` |
| [Requisições (Requisitions)](#13-requisições-requisitions) | 3 | `POR_*` |
| [Recebimento (Receiving)](#14-recebimento-receiving) | 3 | `RCV_*` |
| [Pagamentos Bancários (Payments — IBY)](#15-pagamentos-bancários-payments--iby) | 6 | `IBY_*` |
| [Bancos e Caixa (Cash Management)](#16-bancos-e-caixa-cash-management) | 4 | `CE_*` |
| [Partes e Localizações (TCA)](#17-partes-e-localizações-tca) | 4 | `HZ_*` |
| [Contabilidade Geral (General Ledger)](#18-contabilidade-geral-general-ledger) | 2 | `GL_*` |
| [Subledger Accounting](#19-subledger-accounting) | 1 | `XLA_*` |
| [Projetos (Projects)](#20-projetos-projects) | 6 | `PJF_*` |
| [RH e Pessoas (HR/HCM)](#21-rh-e-pessoas-hrhcm) | 5 | `HR_*`, `PER_*` |
| [Outras Referências Cruzadas](#22-outras-referências-cruzadas) | 12 | `FA_*`, `FND_*`, `FUN_*`, `GMS_*`, `EGP_*`, `INV_*`, `OKC_*`, `PON_*`, `RA_*` |

---

## 1. Faturas (Invoices)

### AP_INVOICES_ALL
**Descrição:** Armazena os cabeçalhos das faturas de contas a pagar. Cada linha representa uma fatura inserida manualmente, importada via interface ou gerada automaticamente. Contém informações como fornecedor, valor total, moeda, data da fatura e termos de pagamento.
**Módulo:** Accounts Payable
**Uso típico:** Extração de todas as faturas AP para relatórios de aging, análise de saldos a pagar e reconciliação com o razão geral.

### AP_INVOICE_LINES_ALL
**Descrição:** Contém as linhas de cada fatura AP. Cada registro representa uma linha inserida manualmente, gerada automaticamente (ex.: rateio de impostos) ou importada pela interface aberta. Inclui descrição do item, quantidade, valor unitário e informações de matching com PO.
**Módulo:** Accounts Payable
**Uso típico:** Detalhamento das faturas por item/serviço, análise de matching com ordens de compra e validação de valores.

### AP_INVOICE_DISTRIBUTIONS_ALL
**Descrição:** Armazena as distribuições contábeis das faturas. Cada registro representa uma linha de distribuição associada a uma linha de fatura, contendo conta contábil, centro de custo, projeto e valor distribuído. Pode ser inserida manualmente ou gerada pelo sistema.
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento contábil das faturas, conciliação com o GL e análise de despesas por centro de custo ou projeto.

### AP_INVOICE_PAYMENTS_ALL
**Descrição:** Registra os pagamentos realizados para cada fatura. Cada linha associa um pagamento (check) a uma fatura, informando o valor pago, data do pagamento e método utilizado.
**Módulo:** Accounts Payable
**Uso típico:** Conciliação de pagamentos com faturas, relatórios de status de pagamento e auditoria de desembolsos.

### AP_INV_APRVL_HIST_ALL
**Descrição:** Contém o histórico de aprovação e rejeição de faturas que passaram pelo workflow de aprovação (Invoice Approval Workflow). Cada registro representa uma ação de um aprovador — aprovação, rejeição ou delegação.
**Módulo:** Accounts Payable
**Uso típico:** Auditoria do processo de aprovação, análise de SLA de aprovação e identificação de gargalos no fluxo.

### AP_INV_SELECTION_CRITERIA_ALL
**Descrição:** Armazena os critérios utilizados para seleção de faturas em processos de pagamento em lote (payment batch / pay run). Inclui filtros como fornecedor, data de vencimento, moeda e business unit.
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento dos parâmetros utilizados em cada execução de pagamento automático.

### AP_SELF_ASSESSED_TAX_DIST_ALL
**Descrição:** Armazena distribuições de impostos auto-avaliados (self-assessed tax) associados a faturas AP. Utilizada em cenários de reverse charge ou uso tributário onde o comprador calcula e recolhe o imposto.
**Módulo:** Accounts Payable
**Uso típico:** Relatórios fiscais de impostos auto-avaliados e conciliação tributária.

---

## 2. Pagamentos (Payments)

### AP_CHECKS_ALL
**Descrição:** Armazena informações sobre pagamentos emitidos a fornecedores ou reembolsos recebidos. Cada registro representa um cheque, transferência eletrônica ou outro instrumento de pagamento. Contém número do pagamento, valor, data, conta bancária e status.
**Módulo:** Accounts Payable
**Uso típico:** Relatórios de pagamentos emitidos, conciliação bancária e rastreamento de desembolsos.

### AP_PAYMENT_SCHEDULES_ALL
**Descrição:** Contém as parcelas de pagamento programadas para cada fatura. Cada registro representa uma parcela com data de vencimento, valor, desconto disponível e status (pago/pendente). Gerada automaticamente com base nos termos de pagamento da fatura.
**Módulo:** Accounts Payable
**Uso típico:** Relatórios de aging (vencidos/a vencer), projeção de fluxo de caixa e análise de prazos de pagamento.

### AP_PAYMENT_HISTORY_ALL
**Descrição:** Armazena o histórico de eventos contábeis dos pagamentos, incluindo compensação (clearing), estorno (unclearing) e maturidade de pagamentos futuros (future-dated payments). Cada registro representa um evento na vida contábil do pagamento.
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento do ciclo de vida contábil dos pagamentos e reconciliação com extratos bancários.

### AP_PAYMENT_HIST_DISTS
**Descrição:** Contém as distribuições contábeis associadas aos eventos de pagamento registrados em `AP_PAYMENT_HISTORY_ALL`. Cada evento contábil pode ter múltiplas distribuições (débito/crédito em diferentes contas).
**Módulo:** Accounts Payable
**Uso típico:** Conciliação contábil detalhada dos pagamentos e integração com o Subledger Accounting (XLA).

### AP_DISCOUNT_OFFERS_TL
**Descrição:** Armazena as traduções (nomes e descrições) das ofertas de desconto por pagamento antecipado. Tabela de tradução (_TL) vinculada às condições de desconto.
**Módulo:** Accounts Payable
**Uso típico:** Configuração e relatórios multilíngues de descontos por antecipação de pagamento.

### AP_INCOME_TAX_REGIONS
**Descrição:** Armazena as regiões fiscais de imposto de renda utilizadas para retenção de impostos sobre pagamentos (withholding tax). Define jurisdições fiscais para fins de reporting tributário.
**Módulo:** Accounts Payable
**Uso típico:** Configuração de retenções fiscais e geração de relatórios de imposto de renda retido na fonte.

---

## 3. Holds e Aprovações

### AP_HOLDS_ALL
**Descrição:** Contém informações sobre bloqueios (holds) aplicados às faturas, seja manualmente pelo usuário ou automaticamente pelo sistema (ex.: discrepância de matching, limite de tolerância). Para holds de matching, há um registro por combinação fatura-shipment.
**Módulo:** Accounts Payable
**Uso típico:** Análise de faturas bloqueadas, identificação de causas de bloqueio e relatórios de produtividade do processo de AP.

### AP_HOLD_CODES
**Descrição:** Tabela de configuração que define os códigos de bloqueio (hold codes) disponíveis no sistema. Cada registro contém o código, descrição, tipo (manual ou automático) e se o hold impede pagamento e/ou contabilização.
**Módulo:** Accounts Payable
**Uso típico:** Referência para decodificação dos tipos de hold aplicados nas faturas.

### AP_INCOME_TAX_TYPES
**Descrição:** Armazena os tipos de imposto de renda utilizados para classificação de retenções fiscais em pagamentos a fornecedores.
**Módulo:** Accounts Payable
**Uso típico:** Configuração e classificação de tipos de retenção de imposto de renda.

---

## 4. Pré-pagamento (Prepayment)

### AP_PREPAY_APP_DISTS
**Descrição:** Detalha a distribuição contábil da aplicação de pré-pagamentos (adiantamentos) contra faturas regulares. Cada registro associa uma distribuição do pré-pagamento a uma distribuição da fatura destinatária. Os registros são criados durante o pré-processamento de extração de AP para o Subledger Accounting (SLA).
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento contábil de aplicações de adiantamento e conciliação de saldos de prepayment.

---

## 5. Condições de Pagamento (Payment Terms)

### AP_TERMS_B
**Descrição:** Armazena o cabeçalho das condições de pagamento (payment terms). Cada registro define um tipo de condição de pagamento utilizado para gerar parcelas programadas nas faturas (ex.: Net 30, 2/10 Net 30).
**Módulo:** Accounts Payable
**Uso típico:** Referência para cálculo de datas de vencimento e descontos por antecipação.

### AP_TERMS_LINES
**Descrição:** Contém as linhas de detalhe de cada condição de pagamento definida em `AP_TERMS_B`. Cada linha especifica o percentual do valor, dias para vencimento e percentual de desconto para uma parcela.
**Módulo:** Accounts Payable
**Uso típico:** Configuração detalhada de parcelamentos e regras de desconto.

### AP_TERMS_TL
**Descrição:** Tabela de tradução para os nomes e descrições das condições de pagamento. Permite suporte multilíngue para os termos definidos em `AP_TERMS_B`.
**Módulo:** Accounts Payable
**Uso típico:** Exibição de nomes de condições de pagamento no idioma do usuário.

### AP_TERMS_VL
**Descrição:** View que combina `AP_TERMS_B` (dados base) com `AP_TERMS_TL` (traduções) para fornecer uma visão consolidada das condições de pagamento no idioma da sessão do usuário.
**Módulo:** Accounts Payable
**Uso típico:** Consultas e relatórios que necessitam do nome traduzido das condições de pagamento.

---

## 6. Aging e Trial Balance

### AP_AGING_PERIODS
**Descrição:** Armazena os períodos de aging (envelhecimento de saldos) definidos pelo usuário para uso no relatório de Invoice Aging. Cada registro representa um período configurado (ex.: 0-30 dias, 31-60 dias).
**Módulo:** Accounts Payable
**Uso típico:** Configuração dos intervalos de aging para relatórios de contas a pagar vencidas.

### AP_AGING_PERIOD_LINES
**Descrição:** Contém as linhas de detalhe de cada período de aging definido em `AP_AGING_PERIODS`. Especifica os limites inferior e superior (em dias) de cada faixa de envelhecimento.
**Módulo:** Accounts Payable
**Uso típico:** Definição granular das faixas de dias para o relatório de aging.

### AP_TRIAL_BALANCES
**Descrição:** Armazena dados do balancete de verificação (trial balance) do módulo AP. Contém saldos de faturas e pagamentos por período contábil, utilizados para conciliação com o razão geral.
**Módulo:** Accounts Payable
**Uso típico:** Reconciliação de saldos AP com o General Ledger e geração do relatório Payables Trial Balance.

---

## 7. Configuração e Parâmetros

### AP_SYSTEM_PARAMETERS_ALL
**Descrição:** Contém os parâmetros e valores padrão para operação do módulo AP por business unit. Inclui informações como ledger, moeda funcional, conta bancária padrão, termos de pagamento padrão e opções de processamento.
**Módulo:** Accounts Payable
**Uso típico:** Referência para entender a configuração do AP de cada business unit.

### AP_DISTRIBUTION_SETS_ALL
**Descrição:** Armazena os conjuntos de distribuição (distribution sets) predefinidos, que permitem automatizar a criação de distribuições contábeis em faturas sem referência a PO. Cada set define uma combinação de contas e percentuais.
**Módulo:** Accounts Payable
**Uso típico:** Automatização da entrada de distribuições contábeis para faturas recorrentes.

### AP_LOOKUP_CODES
**Descrição:** Tabela de lookup codes (valores de domínio) específicos do módulo AP. Contém listas de valores utilizadas em campos como tipo de fatura, tipo de hold, tipo de pagamento, entre outros.
**Módulo:** Accounts Payable
**Uso típico:** Referência para decodificação de códigos utilizados nas tabelas transacionais do AP.

### AP_BATCHES_ALL
**Descrição:** Armazena informações de cabeçalho dos lotes de faturas quando o controle por lote (Batch Control) está habilitado. Cada registro representa um lote com nome, data de criação e totais de controle.
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento de faturas por lote de entrada e controle de integridade.

---

## 8. Reconciliação

### AP_RECON_SUMMARY_PARAMETERS
**Descrição:** Armazena os parâmetros utilizados na execução do relatório de reconciliação do AP (Payables-to-Ledger Reconciliation). Inclui filtros como período, ledger e business unit.
**Módulo:** Accounts Payable
**Uso típico:** Rastreamento dos critérios de cada execução de reconciliação.

### AP_RECON_SUMMARY_DETAILS
**Descrição:** Contém os detalhes sumarizados do resultado da reconciliação entre AP e o razão geral. Apresenta os saldos por categoria (faturas, pagamentos, prepayments) e as diferenças identificadas.
**Módulo:** Accounts Payable
**Uso típico:** Análise de diferenças entre o subledger AP e o General Ledger.

### AP_RECON_DIFFERENCE_DETAILS
**Descrição:** Armazena o detalhamento das diferenças encontradas durante o processo de reconciliação AP-GL. Cada registro representa uma transação que contribui para a diferença entre os saldos.
**Módulo:** Accounts Payable
**Uso típico:** Investigação e resolução de discrepâncias entre AP e GL.

---

## 9. Impostos (Tax — E-Business Tax)

> Tabelas com prefixo `ZX_` pertencem ao módulo **Oracle Tax (E-Business Tax)** e aparecem no contexto AP como referência cruzada para cálculo, retenção e reporting de impostos sobre faturas e pagamentos.

### ZX_REGIMES_B
**Descrição:** Armazena os regimes tributários e seus atributos. Cada registro representa um regime fiscal distinto (ex.: ICMS, ISS, IVA). Contém colunas de valores padrão para facilitar a entrada de dados.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Configuração da hierarquia tributária — regime é o nível mais alto da estrutura de impostos.

### ZX_REGIMES_TL
**Descrição:** Tabela de tradução para os nomes e descrições dos regimes tributários definidos em `ZX_REGIMES_B`.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos regimes fiscais.

### ZX_TAXES_B
**Descrição:** Armazena os impostos e seus atributos para múltiplos configuradores (configuration owners). Cada registro representa um imposto específico dentro de um regime fiscal (ex.: ICMS-SP dentro do regime ICMS).
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Definição dos impostos aplicáveis a transações de compra e venda.

### ZX_TAXES_TL
**Descrição:** Tabela de tradução para os nomes e descrições dos impostos definidos em `ZX_TAXES_B`.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos nomes de impostos.

### ZX_STATUS_B
**Descrição:** Armazena os status fiscais (tax status) associados a impostos. Cada status define uma classificação ou condição do imposto (ex.: tributado, isento, suspenso).
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Classificação do tratamento fiscal aplicado a transações.

### ZX_STATUS_TL
**Descrição:** Tabela de tradução para os status fiscais definidos em `ZX_STATUS_B`.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos status fiscais.

### ZX_JURISDICTIONS_B
**Descrição:** Armazena as jurisdições fiscais — regiões geográficas ou autoridades tributárias onde os impostos são aplicáveis. Cada registro define uma jurisdição com vigência temporal.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Determinação da jurisdição tributária aplicável a transações por localidade.

### ZX_JURISDICTIONS_TL
**Descrição:** Tabela de tradução para as jurisdições fiscais definidas em `ZX_JURISDICTIONS_B`.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue das jurisdições fiscais.

### ZX_RATES_TL
**Descrição:** Tabela de tradução para as alíquotas fiscais. Contém nomes e descrições traduzidos das taxas definidas na tabela base de rates.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue das alíquotas de impostos.

### ZX_RATES_VL
**Descrição:** View que combina dados base das alíquotas com suas traduções. Cada registro representa uma alíquota efetiva para um período específico, aplicável a um status fiscal ou jurisdição.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Consultas e relatórios que necessitam da alíquota com nome traduzido.

### ZX_LINES
**Descrição:** Armazena as linhas de imposto calculadas para transações de múltiplas classes de evento (faturas AP, invoices AR, etc.). Cada registro contém o imposto calculado, base de cálculo, alíquota aplicada e referências à transação origem.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Detalhamento dos impostos calculados por linha de transação.

### ZX_LINES_SUMMARY
**Descrição:** Contém um resumo consolidado das linhas de imposto por transação. Agrupa os valores de `ZX_LINES` em nível de cabeçalho para facilitar consultas e relatórios.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Visão sumarizada dos impostos por transação para relatórios fiscais.

### ZX_REC_NREC_DIST
**Descrição:** Armazena as distribuições de imposto recuperável e não recuperável para cada linha de imposto de uma fatura. Cada registro representa uma distribuição de crédito fiscal (recuperável) ou custo fiscal (não recuperável).
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Contabilização de créditos fiscais e análise de impostos recuperáveis vs. não recuperáveis.

### ZX_BUCKETS_F
**Descrição:** Armazena os buckets (faixas/categorias) de apuração fiscal. Utilizada para agrupamento de valores tributários em categorias definidas pela legislação.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Classificação de valores fiscais em categorias para apuração e reporting.

### ZX_CONDITION_GROUPS_B
**Descrição:** Define grupos de condições utilizados nas regras de determinação de impostos. Cada grupo reúne condições que, quando atendidas, determinam o tratamento fiscal aplicável.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Configuração de regras de determinação automática de impostos.

### ZX_CONDITION_GROUPS_TL
**Descrição:** Tabela de tradução para os grupos de condições fiscais definidos em `ZX_CONDITION_GROUPS_B`.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos grupos de condições.

### ZX_CONDITION_GROUPS_VL
**Descrição:** View que combina `ZX_CONDITION_GROUPS_B` com `ZX_CONDITION_GROUPS_TL`, fornecendo dados base e traduções em uma única visão.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Consultas de grupos de condições com nomes traduzidos.

### ZX_FC_CODES_TL
**Descrição:** Tabela de tradução para os códigos de classificação fiscal (fiscal classification codes). Esses códigos classificam itens, fornecedores ou transações para fins de determinação tributária.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos códigos de classificação fiscal.

### ZX_FC_CODES_VL
**Descrição:** View que combina dados base dos códigos de classificação fiscal com suas traduções.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Consultas de classificação fiscal com nomes traduzidos.

### ZX_PARTY_TAX_PROFILE
**Descrição:** Armazena o perfil tributário de partes (fornecedores, clientes, estabelecimentos). Contém informações como regime de tributação, isenções e registros fiscais associados a cada parte.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Determinação do tratamento fiscal baseado no perfil do fornecedor ou comprador.

### ZX_REGISTRATIONS
**Descrição:** Armazena os registros fiscais (tax registrations) das partes — como inscrições estaduais, CNPJ, números de IVA. Cada registro vincula uma parte a uma jurisdição e regime tributário.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Validação de registros fiscais de fornecedores e determinação de jurisdição aplicável.

### ZX_TAX_SETTLEMENT_AUTHS_F
**Descrição:** Armazena as autoridades de liquidação fiscal (tax settlement authorities) — entidades governamentais para as quais os impostos são recolhidos.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Configuração de recolhimento de impostos por autoridade fiscal.

### ZX_WHT_LINES_SUMMARY
**Descrição:** Contém um resumo das linhas de retenção na fonte (withholding tax) por transação. Armazena os valores de retenção calculados sobre pagamentos a fornecedores.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Relatórios de retenção na fonte e conciliação de valores retidos.

### ZX_WHT_TAX_CLASSIFICATION_V
**Descrição:** View que apresenta as classificações de retenção na fonte (withholding tax classification). Utilizada para categorizar os tipos de retenção aplicáveis a transações e fornecedores.
**Módulo:** Tax (referência cruzada com AP)
**Uso típico:** Referência para classificação de retenções fiscais em faturas e pagamentos.

---

## 10. Despesas (Expenses)

> Tabelas com prefixo `EXM_` pertencem ao módulo **Oracle Expenses** e aparecem no contexto AP porque relatórios de despesas geram faturas no Accounts Payable.

### EXM_EXPENSE_REPORTS
**Descrição:** Armazena as informações de cabeçalho dos relatórios de despesas, incluindo número do relatório, propósito, funcionário responsável, data de submissão e status de aprovação.
**Módulo:** Expenses (referência cruzada com AP)
**Uso típico:** Rastreamento de relatórios de despesas por funcionário e análise de status de processamento.

### EXM_EXPENSES
**Descrição:** Contém as linhas individuais de despesa dentro de cada relatório. Cada registro representa um item de despesa com tipo, data, valor, moeda e justificativa.
**Módulo:** Expenses (referência cruzada com AP)
**Uso típico:** Detalhamento de despesas por tipo, período e funcionário.

### EXM_EXPENSE_DISTS
**Descrição:** Armazena as distribuições contábeis de cada linha de despesa. Define a alocação de valores por conta contábil, centro de custo e projeto. Tabela multi-org.
**Módulo:** Expenses (referência cruzada com AP)
**Uso típico:** Contabilização de despesas e análise por centro de custo ou projeto.

### EXM_EXPENSE_TEMPLATES
**Descrição:** Armazena os templates (modelos) de relatório de despesas predefinidos, que padronizam os tipos de despesa e campos disponíveis para preenchimento.
**Módulo:** Expenses (referência cruzada com AP)
**Uso típico:** Configuração de modelos de relatório de despesas por política corporativa.

### EXM_EXPENSE_TYPES
**Descrição:** Define os tipos de despesa disponíveis no sistema (ex.: passagem aérea, hospedagem, alimentação, táxi). Cada registro contém o código, descrição, categoria e regras de política aplicáveis.
**Módulo:** Expenses (referência cruzada com AP)
**Uso típico:** Configuração e categorização de tipos de despesa para controle de políticas.

---

## 11. Fornecedores (Suppliers)

> Tabelas com prefixo `POZ_` pertencem ao módulo **Oracle Procurement — Supplier Management** e são referenciadas no AP para identificação dos fornecedores nas faturas e pagamentos.

### POZ_SUPPLIERS_V
**Descrição:** View consolidada de fornecedores que combina dados de cadastro com informações traduzidas. Apresenta nome, número do fornecedor, tipo, status e dados de classificação.
**Módulo:** Procurement — Suppliers (referência cruzada com AP)
**Uso típico:** Consulta de dados cadastrais de fornecedores vinculados a faturas e pagamentos AP.

### POZ_SUPPLIER_SITES_ALL_M
**Descrição:** Armazena os sites (endereços/estabelecimentos) dos fornecedores, com informações de pagamento, impostos, moeda e business unit associada. Cada fornecedor pode ter múltiplos sites.
**Módulo:** Procurement — Suppliers (referência cruzada com AP)
**Uso típico:** Identificação do site do fornecedor para direcionamento de pagamentos e configuração fiscal.

---

## 12. Pedidos de Compra (Purchase Orders)

> Tabelas com prefixo `PO_` pertencem ao módulo **Oracle Purchasing** e são referenciadas no AP para matching de faturas com ordens de compra e recebimentos.

### PO_HEADERS_ALL
**Descrição:** Armazena os cabeçalhos de todos os documentos de compra — ordens de compra padrão, contratos (blanket/planned), cotações e RFQs. Contém fornecedor, comprador, valor total, status e tipo de documento.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Referência para matching de faturas AP com ordens de compra.

### PO_LINES_ALL
**Descrição:** Contém as linhas de cada documento de compra, com informações de item, descrição, quantidade, preço unitário e categoria. Cada linha pertence a um cabeçalho em `PO_HEADERS_ALL`.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Detalhamento de itens comprados para matching com linhas de fatura.

### PO_LINE_LOCATIONS_ALL
**Descrição:** Armazena os shipment schedules (programações de entrega) e price breaks de ordens de compra e contratos. Cada registro define quantidade, data de entrega, local de destino e tipo de destino (estoque, despesa, etc.).
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Matching 3-way (fatura × PO × recebimento) e rastreamento de entregas programadas.

### PO_DISTRIBUTIONS_ALL
**Descrição:** Contém as distribuições contábeis de cada shipment schedule de PO. Cada registro define conta contábil, centro de custo, projeto e quantidade distribuída. Uma linha de PO pode ter múltiplas distribuições.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Referência contábil para distribuições de faturas com matching a PO.

### PO_SYSTEM_PARAMETERS_ALL
**Descrição:** Armazena os parâmetros de configuração do módulo de Purchasing por business unit, incluindo opções de numeração, aprovação, matching e recebimento.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Referência para entender as regras de configuração do módulo de compras.

### PO_ATTRIBUTE_VALUES
**Descrição:** Armazena atributos descritivos adicionais (DFF — Descriptive Flexfields) associados a linhas de pedidos de compra. Permite extensão de dados além das colunas padrão.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Extração de campos customizados associados a pedidos de compra.

### PO_UN_NUMBERS_VL
**Descrição:** View de números UN (United Nations) utilizados para classificação de itens perigosos em ordens de compra.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Classificação regulatória de materiais perigosos em compras.

### PO_VERSIONS
**Descrição:** Armazena o histórico de versões dos documentos de compra. Cada registro representa uma versão de um pedido de compra, permitindo rastreamento de alterações ao longo do tempo.
**Módulo:** Purchasing (referência cruzada com AP)
**Uso típico:** Auditoria de alterações em pedidos de compra.

---

## 13. Requisições (Requisitions)

> Tabelas com prefixo `POR_` pertencem ao módulo **Oracle Self-Service Procurement (Requisitions)**.

### POR_REQUISITION_HEADERS_ALL
**Descrição:** Armazena os cabeçalhos das requisições de compra. Contém número, requisitante, data, status de aprovação e business unit.
**Módulo:** Procurement — Requisitions (referência cruzada com AP)
**Uso típico:** Rastreamento de requisições que originaram ordens de compra e, subsequentemente, faturas AP.

### POR_REQUISITION_LINES_ALL
**Descrição:** Contém as linhas individuais de cada requisição, com item, descrição, quantidade solicitada, preço estimado e fornecedor sugerido.
**Módulo:** Procurement — Requisitions (referência cruzada com AP)
**Uso típico:** Detalhamento de itens requisitados para análise de demanda e rastreabilidade.

### POR_REQ_DISTRIBUTIONS_ALL
**Descrição:** Armazena as distribuições contábeis das linhas de requisição, definindo conta contábil, centro de custo e projeto para cada distribuição.
**Módulo:** Procurement — Requisitions (referência cruzada com AP)
**Uso típico:** Alocação orçamentária de requisições e rastreamento de encargos.

---

## 14. Recebimento (Receiving)

> Tabelas com prefixo `RCV_` pertencem ao módulo **Oracle Receiving (SCM)** e são referenciadas no AP para matching de faturas com recebimentos físicos.

### RCV_SHIPMENT_HEADERS
**Descrição:** Armazena informações comuns sobre a origem dos recebimentos ou recebimentos esperados. Suporta dois tipos de fonte: Supplier (recebimento contra PO de fornecedor externo) e Internal Order (transferências interorganizacionais ou requisições internas).
**Módulo:** Receiving / SCM (referência cruzada com AP)
**Uso típico:** Referência para matching 3-way e rastreamento de remessas recebidas.

### RCV_SHIPMENT_LINES
**Descrição:** Contém informações sobre itens que foram enviados e/ou recebidos de uma fonte específica. Cada registro detalha item, quantidade enviada, quantidade recebida e destino padrão.
**Módulo:** Receiving / SCM (referência cruzada com AP)
**Uso típico:** Detalhamento de itens recebidos para matching com faturas e análise de recebimentos parciais.

### RCV_TRANSACTIONS
**Descrição:** Armazena as transações de recebimento — cada ação executada sobre um recebimento (receber, inspecionar, transferir, devolver, entregar). Contém quantidade, data da transação e referências à PO e shipment line.
**Módulo:** Receiving / SCM (referência cruzada com AP)
**Uso típico:** Matching de faturas com recebimentos e rastreamento do fluxo logístico de entrada.

---

## 15. Pagamentos Bancários (Payments — IBY)

> Tabelas com prefixo `IBY_` pertencem ao módulo **Oracle Payments (IBY)** e são referenciadas no AP para processamento e rastreamento de pagamentos eletrônicos.

### IBY_PAYMENTS_ALL
**Descrição:** Armazena informações de pagamentos processados, onde cada registro representa uma transação de pagamento individual (cheque, transferência eletrônica) entre o pagador (first party) e o beneficiário (third party payee).
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Rastreamento de pagamentos emitidos e conciliação com extratos bancários.

### IBY_PAY_INSTRUCTIONS_ALL
**Descrição:** Armazena as instruções de pagamento — agrupamentos de pagamentos enviados ao banco para processamento. Cada instrução pode conter múltiplos pagamentos e é associada a um perfil de pagamento e formato de arquivo.
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Rastreamento de remessas de pagamento enviadas aos bancos.

### IBY_EXT_BANK_ACCOUNTS
**Descrição:** Define as contas bancárias externas (de terceiros — fornecedores, funcionários). Contém número da conta, banco, agência, moeda e titular. Utilizada para direcionar pagamentos eletrônicos.
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Referência de contas bancárias de fornecedores para pagamentos eletrônicos.

### IBY_ACCT_PMT_PROFILES_TL
**Descrição:** Tabela de tradução para os perfis de pagamento de contas (account payment profiles). Esses perfis definem como os pagamentos são processados para uma conta bancária interna específica.
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Referência multilíngue dos perfis de pagamento.

### IBY_PAYMENT_METHODS_TL
**Descrição:** Tabela de tradução para os métodos de pagamento (ex.: cheque, transferência eletrônica, boleto). Define os nomes e descrições traduzidos de cada método disponível.
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Referência de métodos de pagamento para relatórios e configurações.

### IBY_PAYMENT_CODES_VL
**Descrição:** View que apresenta os códigos de pagamento com traduções. Códigos de pagamento categorizam instruções especiais associadas a pagamentos (ex.: urgente, consolidado).
**Módulo:** Oracle Payments (referência cruzada com AP)
**Uso típico:** Classificação de pagamentos por tipo de instrução especial.

---

## 16. Bancos e Caixa (Cash Management)

> Tabelas com prefixo `CE_` pertencem ao módulo **Oracle Cash Management** e são referenciadas no AP para gestão de contas bancárias internas e documentos de pagamento.

### CE_BANK_ACCT_USES_ALL
**Descrição:** Armazena os usos (purposes) das contas bancárias internas — define para quais finalidades cada conta é utilizada (AP, AR, Payroll, etc.) e por qual business unit.
**Módulo:** Cash Management (referência cruzada com AP)
**Uso típico:** Identificação das contas bancárias habilitadas para pagamentos AP por business unit.

### CE_INTERNAL_BANK_ACCTS_V
**Descrição:** View que apresenta as contas bancárias internas (da empresa) com informações consolidadas de banco, agência, número da conta, moeda e saldo.
**Módulo:** Cash Management (referência cruzada com AP)
**Uso típico:** Consulta de contas bancárias internas disponíveis para emissão de pagamentos.

### CE_ALL_BANK_BRANCHES_V
**Descrição:** View que lista todas as agências bancárias cadastradas no sistema, incluindo agências de bancos internos e externos, com código, nome e endereço.
**Módulo:** Cash Management (referência cruzada com AP)
**Uso típico:** Referência de agências bancárias para pagamentos e recebimentos.

### CE_PAYMENT_DOCUMENTS
**Descrição:** Armazena os documentos de pagamento (ex.: talões de cheques, sequências de transferências) associados a contas bancárias internas. Define faixas de numeração e formato dos instrumentos de pagamento.
**Módulo:** Cash Management (referência cruzada com AP)
**Uso típico:** Controle de numeração de cheques e instrumentos de pagamento.

---

## 17. Partes e Localizações (TCA)

> Tabelas com prefixo `HZ_` pertencem ao módulo **Oracle Trading Community Architecture (TCA)** e são utilizadas no AP para dados de partes (fornecedores, contatos) e endereços.

### HZ_PARTIES
**Descrição:** Armazena informações básicas sobre partes (parties). Cada registro representa uma parte única que pode ser do tipo Organization (empresa), Person (pessoa física) ou Group (grupo). Múltiplas partes podem ter o mesmo nome.
**Módulo:** TCA (referência cruzada com AP)
**Uso típico:** Referência de dados cadastrais de fornecedores como partes no modelo unificado TCA.

### HZ_PARTY_SITES
**Descrição:** Armazena os sites (endereços associados) de cada parte. Vincula uma parte (`HZ_PARTIES`) a uma localização (`HZ_LOCATIONS`), definindo o uso do endereço (comercial, entrega, cobrança).
**Módulo:** TCA (referência cruzada com AP)
**Uso típico:** Identificação dos endereços de fornecedores para envio de pagamentos e correspondência.

### HZ_LOCATIONS
**Descrição:** Contém os endereços físicos (logradouro, cidade, estado, país, CEP) utilizados por party sites. Cada registro representa um endereço único.
**Módulo:** TCA (referência cruzada com AP)
**Uso típico:** Dados de endereço de fornecedores para relatórios fiscais e logísticos.

### HZ_CONTACT_POINTS
**Descrição:** Armazena os pontos de contato das partes — telefones, e-mails, URLs e outros meios de comunicação. Cada registro é vinculado a uma parte ou party site.
**Módulo:** TCA (referência cruzada com AP)
**Uso típico:** Dados de contato de fornecedores para comunicação e notificações.

---

## 18. Contabilidade Geral (General Ledger)

> Tabelas com prefixo `GL_` pertencem ao módulo **Oracle General Ledger** e são referenciadas no AP para definições contábeis e conversão de moedas.

### GL_LEDGERS
**Descrição:** Armazena informações sobre os ledgers (livros contábeis) e ledger sets definidos no Accounting Setup Manager. Cada registro inclui nome, moeda, calendário contábil, plano de contas e configurações de período.
**Módulo:** General Ledger (referência cruzada com AP)
**Uso típico:** Referência para identificação do ledger associado às transações AP.

### GL_DAILY_CONVERSION_TYPES
**Descrição:** Define os tipos de conversão cambial diária utilizados para converter valores entre moedas (ex.: Corporate, Spot, User). Cada tipo determina como as taxas de câmbio são aplicadas.
**Módulo:** General Ledger (referência cruzada com AP)
**Uso típico:** Referência de tipos de conversão cambial em faturas AP com moeda estrangeira.

---

## 19. Subledger Accounting

### XLA_EVENTS
**Descrição:** Armazena os eventos contábeis do Subledger Accounting (SLA). Cada registro representa um evento que gera lançamentos contábeis — como validação de fatura, pagamento, cancelamento. Contém tipo de evento, data, status de contabilização e referências à transação origem.
**Módulo:** Subledger Accounting (referência cruzada com AP)
**Uso típico:** Rastreamento de eventos contábeis AP e auditoria da contabilização de transações.

---

## 20. Projetos (Projects)

> Tabelas com prefixo `PJF_` pertencem ao módulo **Oracle Project Financial Management** e são referenciadas no AP quando faturas e despesas são alocadas a projetos.

### PJF_PROJECTS_ALL_B
**Descrição:** Armazena os dados base dos projetos. Cada registro representa um projeto com número, status, datas, organização responsável e tipo de projeto.
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Referência de projetos associados a distribuições de faturas e despesas AP.

### PJF_PROJECTS_ALL_TL
**Descrição:** Tabela de tradução para os nomes e descrições dos projetos definidos em `PJF_PROJECTS_ALL_B`.
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos nomes de projetos.

### PJF_PROJ_ELEMENTS_B
**Descrição:** Armazena os elementos de projeto (tasks/WBS) — tarefas e atividades que compõem a estrutura analítica do projeto. Cada registro representa um nó na hierarquia do projeto.
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Identificação da task de projeto associada a distribuições de faturas AP.

### PJF_PROJ_ELEMENTS_TL
**Descrição:** Tabela de tradução para os nomes e descrições dos elementos de projeto definidos em `PJF_PROJ_ELEMENTS_B`.
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Exibição multilíngue dos nomes de tasks de projeto.

### PJF_EXP_TYPES_TL
**Descrição:** Tabela de tradução para os tipos de despesa de projeto (expenditure types). Define nomes e descrições traduzidos para as categorias de despesa utilizadas em projetos.
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Classificação de despesas por tipo em relatórios de projeto.

### PJF_WORK_TYPES_VL
**Descrição:** View que apresenta os tipos de trabalho (work types) de projetos com traduções. Classifica a natureza do trabalho realizado (ex.: horas regulares, horas extras, materiais).
**Módulo:** Project Financial Management (referência cruzada com AP)
**Uso típico:** Classificação do tipo de trabalho em transações de projeto referenciadas pelo AP.

---

## 21. RH e Pessoas (HR/HCM)

> Tabelas com prefixo `HR_` e `PER_` pertencem ao módulo **Oracle Human Capital Management (HCM)** e são referenciadas no AP para dados de funcionários, organizações e localizações.

### HR_ALL_ORGANIZATION_UNITS_F_VL
**Descrição:** View que apresenta todas as unidades organizacionais (business units, departamentos, centros de custo) com nomes traduzidos e vigência temporal.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Referência de business units e departamentos associados a transações AP.

### HR_ORGANIZATION_INFORMATION_F
**Descrição:** Armazena informações adicionais e classificações das organizações. Contém dados como tipo de organização, hierarquia e atributos configuráveis por classificação.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Detalhamento de atributos organizacionais para regras de negócio no AP.

### HR_LOCATIONS
**Descrição:** Armazena as localizações definidas no módulo de RH — endereços de escritórios, fábricas, centros de distribuição da empresa.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Referência de localizações para ship-to e bill-to em transações de compra.

### HR_LOCATIONS_ALL_X
**Descrição:** Tabela estendida de localizações com campos adicionais (DFF) e dados multi-org. Complementa `HR_LOCATIONS` com atributos configuráveis.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Consulta de atributos estendidos de localizações.

### PER_PERSON_NAMES_F_V
**Descrição:** View que apresenta os nomes de pessoas (funcionários) com vigência temporal. Contém nome completo, nome e sobrenome em formato estruturado.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Identificação de nomes de aprovadores, requisitantes e preparadores de faturas.

### PER_USERS
**Descrição:** Armazena os registros de usuários do sistema vinculados a pessoas (funcionários). Contém username, data de criação e associação ao registro de pessoa.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Vínculo entre usuários do sistema e transações AP (criação, aprovação).

### PER_LOCATION_DETAILS_F_VL
**Descrição:** View que apresenta detalhes de localizações de pessoas com tradução e vigência temporal. Complementa HR_LOCATIONS com informações adicionais específicas de jurisdição.
**Módulo:** HCM (referência cruzada com AP)
**Uso típico:** Detalhes de localização para regras fiscais e alocações.

---

## 22. Outras Referências Cruzadas

### FA_BOOK_CONTROLS
**Descrição:** Armazena as definições dos livros de ativos (asset books) no módulo de Ativo Fixo. Cada registro define um livro com suas regras de depreciação, calendário e ledger associado. Referenciado no AP quando faturas são capitalizadas como ativos.
**Módulo:** Fixed Assets (referência cruzada com AP)
**Uso típico:** Identificação do asset book de destino para faturas de aquisição de ativos.

### FND_ATTACHED_DOCUMENTS
**Descrição:** Armazena os metadados de documentos anexados a transações em qualquer módulo. No contexto AP, registra anexos (PDFs, imagens, notas) vinculados a faturas e pagamentos.
**Módulo:** Foundation / Platform (referência cruzada com AP)
**Uso típico:** Rastreamento de documentos comprobatórios anexados a faturas AP.

### FND_DOCUMENT_SEQUENCES
**Descrição:** Define as sequências de numeração de documentos utilizadas pelo sistema. Cada registro configura uma sequência com prefixo, faixa numérica e regras de atribuição.
**Módulo:** Foundation / Platform (referência cruzada com AP)
**Uso típico:** Controle de numeração sequencial de faturas (voucher numbers) e pagamentos.

### FND_DOC_SEQUENCE_CATEGORIES
**Descrição:** Define as categorias de sequência de documentos — associa tabelas e tipos de transação a sequências de numeração específicas.
**Módulo:** Foundation / Platform (referência cruzada com AP)
**Uso típico:** Configuração de categorias de numeração para transações AP.

### FUN_BU_PERF_V
**Descrição:** View que apresenta as business units com informações de performance e configuração. Utilizada para identificar BUs ativas e seus atributos organizacionais.
**Módulo:** Financials Common (referência cruzada com AP)
**Uso típico:** Referência de business units para filtros e segmentação de dados AP.

### GMS_FUNDING_SOURCES_VL
**Descrição:** View que apresenta as fontes de financiamento (funding sources) de grants/subvenções com traduções. Utilizada quando despesas AP são alocadas a projetos financiados por grants.
**Módulo:** Grants Management (referência cruzada com AP)
**Uso típico:** Identificação da fonte de financiamento associada a despesas de projetos.

### EGP_CATEGORIES_VL
**Descrição:** View que apresenta as categorias de produto/item com traduções. Utilizada para classificação de itens em ordens de compra e faturas.
**Módulo:** Product Management (referência cruzada com AP)
**Uso típico:** Classificação de itens comprados por categoria para análise de spend.

### INV_UNITS_OF_MEASURE_B
**Descrição:** Armazena as unidades de medida (UOM) base utilizadas em transações de inventário, compras e faturamento. Cada registro define uma UOM com código e classe.
**Módulo:** Inventory (referência cruzada com AP)
**Uso típico:** Referência de unidades de medida em linhas de fatura e PO.

### INV_UNITS_OF_MEASURE_TL
**Descrição:** Tabela de tradução para as unidades de medida definidas em `INV_UNITS_OF_MEASURE_B`.
**Módulo:** Inventory (referência cruzada com AP)
**Uso típico:** Exibição multilíngue das unidades de medida.

### INV_CONS_ADVICE_TXNS_V
**Descrição:** View de transações de aviso de consignação (consignment advice). Apresenta transações relacionadas a inventário em consignação que impactam o processo de contas a pagar.
**Módulo:** Inventory (referência cruzada com AP)
**Uso típico:** Rastreamento de transações de consignação que geram faturas AP.

### OKC_K_HEADERS_VL
**Descrição:** View que apresenta os cabeçalhos de contratos do módulo Oracle Contracts com traduções. Contém número do contrato, tipo, partes envolvidas, datas de vigência e status.
**Módulo:** Contracts (referência cruzada com AP)
**Uso típico:** Referência de contratos associados a ordens de compra e faturas AP.

### PON_AUCTION_ITEM_PRICES_ALL
**Descrição:** Armazena os itens e preços de leilões/negociações eletrônicas (sourcing events). Cada registro detalha um item ofertado em um evento de negociação com preço-alvo e especificações.
**Módulo:** Sourcing (referência cruzada com AP)
**Uso típico:** Rastreabilidade de preços negociados que originaram ordens de compra.

### PON_BID_ITEM_PRICES
**Descrição:** Contém os preços ofertados pelos fornecedores (bids/lances) para cada item de um evento de sourcing. Cada registro representa a proposta de preço de um fornecedor para um item.
**Módulo:** Sourcing (referência cruzada com AP)
**Uso típico:** Comparação de preços negociados com valores faturados.

### RA_CUSTOMER_TRX_ALL
**Descrição:** Armazena as transações de clientes do módulo de Contas a Receber (AR) — faturas de venda, notas de crédito e débito. Referenciada no contexto AP para transações intercompany ou debit memos de fornecedores.
**Módulo:** Accounts Receivable (referência cruzada com AP)
**Uso típico:** Referência cruzada para transações intercompany entre AP e AR.

---

## Referências

- [Oracle Fusion Cloud Financials — Tables and Views](https://docs.oracle.com/en/cloud/saas/financials/25d/oedmf/)
- [Oracle Fusion Cloud Procurement — Tables and Views](https://docs.oracle.com/en/cloud/saas/procurement/25d/oedmp/)
- [Oracle Fusion Cloud SCM — Tables and Views](https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/24b/oedsc/)
- [Oracle Payables Reference Guide (E-Business Suite)](https://docs.oracle.com/cd/E18727_01/doc.121/e12796/T434602T367248.htm)
