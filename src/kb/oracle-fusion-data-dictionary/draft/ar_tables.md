# Oracle Fusion — Accounts Receivable (AR) — Database Tables

> Referência de tabelas do módulo AR extraídas do BICC Database Mapping (Release 13/25A).
> Fonte: documentação oficial Oracle Fusion Cloud ERP.

---

## Sumário de Grupos

| Grupo | Qtd. | Prefixos |
|-------|------|----------|
| Transações (Invoices, Memos, Linhas) | 12 | `RA_` |
| Recebimentos (Receipts) | 8 | `AR_` |
| Ajustes e Distribuições | 6 | `AR_` |
| Aging, Cobranças e Disputas | 6 | `AR_` |
| Configuração e Parâmetros AR | 16 | `AR_` |
| Juros e Encargos | 5 | `AR_` |
| Reconciliação | 3 | `AR_` |
| Clientes e Partes (TCA) | 17 | `HZ_` |
| Pagamentos (Payments) | 9 | `IBY_` |
| Impostos (Tax) | 17 | `ZX_` |
| Contabilidade Geral (GL/XLA) | 5 | `GL_`, `XLA_`, `XLE_` |
| Cash Management / Bancos | 3 | `CE_` |
| Itens e Inventário | 6 | `EGP_`, `INV_` |
| RH e Organizações | 4 | `HR_` |
| Fundação / Infraestrutura | 4 | `FND_`, `FUN_`, `PER_` |
| Vendedores | 1 | `JTF_` |

---

## 1. Transações — Invoices, Memos e Linhas (`RA_`)

### RA_CUSTOMER_TRX_ALL
**Descrição:** Armazena o cabeçalho de faturas (invoices), notas de débito, notas de crédito e duplicatas a receber (bills receivable). Cada linha representa uma transação com informações como cliente, tipo de transação, data, moeda e instruções de impressão.
**Módulo:** Accounts Receivable
**Uso típico:** Extração de todas as transações AR; base para relatórios de faturamento, aging e reconciliação contábil.

### RA_CUSTOMER_TRX_LINES_ALL
**Descrição:** Armazena as linhas de detalhe das transações de clientes, incluindo valores, itens, quantidades e informações de receita. Cada linha pertence a um cabeçalho em `RA_CUSTOMER_TRX_ALL`.
**Módulo:** Accounts Receivable
**Uso típico:** Detalhamento de itens faturados; cálculo de receita por linha; análise de mix de produtos.

### RA_CUST_TRX_LINE_GL_DIST_ALL
**Descrição:** Armazena as distribuições contábeis (accounting distributions) das linhas de transação. Liga cada linha de transação às combinações de contas contábeis do General Ledger.
**Módulo:** Accounts Receivable
**Uso típico:** Reconciliação entre AR e GL; análise de receita por conta contábil; auditoria de lançamentos.

### RA_CUST_TRX_LINE_SALESREPS_ALL
**Descrição:** Armazena a atribuição de vendedores (sales credits) às linhas de transação. Permite que uma mesma linha tenha crédito de venda dividido entre múltiplos vendedores.
**Módulo:** Accounts Receivable
**Uso típico:** Comissionamento; relatórios de vendas por representante; análise de performance comercial.

### RA_CUST_TRX_TYPES_ALL
**Descrição:** Define os tipos de transação utilizados para faturas, duplicatas a receber e notas de crédito. Cada registro inclui configurações de AutoAccounting e valores padrão para transações.
**Módulo:** Accounts Receivable
**Uso típico:** Classificação de transações; configuração de regras de contabilização automática; filtros em relatórios.

### RA_BATCHES_ALL
**Descrição:** Armazena informações sobre lotes de transações de recebíveis. Cada lote agrupa transações criadas em conjunto para processamento.
**Módulo:** Accounts Receivable
**Uso típico:** Controle de lotes de entrada de faturas; rastreamento de importações em massa.

### RA_BATCH_SOURCES_ALL
**Descrição:** Define as origens (sources) de faturas, notas de crédito e compromissos. Cada registro contém configurações de numeração automática para faturas e lotes.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de fontes de transação; controle de sequenciamento de documentos.

### RA_CM_REQUESTS_ALL
**Descrição:** Armazena solicitações de notas de crédito (credit memo requests) geradas a partir de disputas ou processos de aprovação.
**Módulo:** Accounts Receivable
**Uso típico:** Workflow de aprovação de créditos; rastreamento de solicitações de estorno.

### RA_CUST_RECEIPT_METHODS
**Descrição:** Associa métodos de recebimento a contas de clientes, definindo como cada cliente pode efetuar pagamentos.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de formas de pagamento por cliente; automação de recebimentos.

### RA_REMIT_TOS_ALL
**Descrição:** Armazena os endereços de remessa (remit-to addresses) associados a transações, indicando para onde os pagamentos devem ser enviados.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de endereços de cobrança; impressão de faturas com destino de pagamento.

### RA_GROUPING_RULES
**Descrição:** Define regras de agrupamento para a geração automática de faturas (AutoInvoice). Determina quais linhas podem ser consolidadas em uma única fatura.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração do AutoInvoice; otimização do volume de faturas geradas.

### RA_RULES
**Descrição:** Define regras de reconhecimento de receita utilizadas pelo Accounts Receivable. Determina como e quando a receita é reconhecida contabilmente (ex.: imediato, rateado, por período).
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de regras de revenue recognition; compliance com normas contábeis (ASC 606, IFRS 15).

---

## 2. Condições de Pagamento (`RA_TERMS`)

### RA_TERMS_B
**Descrição:** Tabela base que armazena as condições de pagamento (payment terms) utilizadas em transações de recebíveis. Define prazos, percentuais de parcelas e descontos.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de prazos de pagamento (30/60/90 dias); cálculo de datas de vencimento.

### RA_TERMS_LINES
**Descrição:** Armazena as linhas de detalhe de cada condição de pagamento, permitindo termos com múltiplas parcelas e percentuais diferentes.
**Módulo:** Accounts Receivable
**Uso típico:** Parcelamento de faturas; definição de cronogramas de pagamento.

### RA_TERMS_TL
**Descrição:** Tabela de traduções (translation) das condições de pagamento, armazenando nomes e descrições em múltiplos idiomas.
**Módulo:** Accounts Receivable
**Uso típico:** Suporte a ambientes multi-idioma; exibição de termos no idioma do usuário.

### RA_TERMS_VL
**Descrição:** View que combina `RA_TERMS_B` e `RA_TERMS_TL`, fornecendo os dados base junto com as traduções no idioma da sessão do usuário.
**Módulo:** Accounts Receivable
**Uso típico:** Consulta simplificada de condições de pagamento com descrições traduzidas.

---

## 3. Recebimentos — Receipts (`AR_`)

### AR_CASH_RECEIPTS_ALL
**Descrição:** Armazena um registro para cada recebimento (receipt) inserido no sistema. Inclui valor, moeda, data, status (APP=aplicado, UNAPP=não aplicado, UNID=não identificado, NSF=fundos insuficientes, REV=revertido, STOP=stop payment) e referência ao cliente.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de recebimentos; relatórios de caixa; reconciliação bancária; análise de inadimplência.

### AR_CASH_RECEIPT_HISTORY_ALL
**Descrição:** Contém o histórico do ciclo de vida de cada recebimento, com uma linha para cada etapa (criação, confirmação, remessa, compensação, reversão).
**Módulo:** Accounts Receivable
**Uso típico:** Auditoria de recebimentos; rastreamento de status; análise do fluxo de compensação.

### AR_CASH_REMIT_REFS_ALL
**Descrição:** Armazena referências de remessa associadas a recebimentos, vinculando pagamentos recebidos a identificadores bancários ou referências de transferência.
**Módulo:** Accounts Receivable
**Uso típico:** Conciliação bancária automática; matching de pagamentos eletrônicos.

### AR_RECEIVABLE_APPLICATIONS_ALL
**Descrição:** Armazena todas as aplicações de recebimentos e notas de crédito a faturas. O campo `APPLICATION_TYPE` indica se é aplicação de caixa (CASH) ou nota de crédito (CM). Registra também os lançamentos contábeis correspondentes.
**Módulo:** Accounts Receivable
**Uso típico:** Reconciliação de recebimentos; análise de aplicações; auditoria contábil de baixas.

### AR_PAYMENT_SCHEDULES_ALL
**Descrição:** Armazena os cronogramas de pagamento de todas as transações (exceto ajustes e recebimentos avulsos). Atualizada sempre que há atividade contra uma fatura, nota de crédito ou recebimento. Contém saldos em aberto, datas de vencimento e valores aplicados.
**Módulo:** Accounts Receivable
**Uso típico:** Aging de contas a receber; cálculo de saldo em aberto; relatórios de inadimplência e DSO.

### AR_MISC_CASH_DISTRIBUTIONS_ALL
**Descrição:** Armazena as distribuições contábeis de recebimentos avulsos (miscellaneous receipts), como juros recebidos, royalties ou outras receitas não vinculadas a faturas.
**Módulo:** Accounts Receivable
**Uso típico:** Contabilização de receitas diversas; reconciliação de recebimentos sem fatura.

### AR_BATCHES_ALL
**Descrição:** Armazena informações sobre lotes de recebimentos, agrupando receipts criados em conjunto para processamento em massa.
**Módulo:** Accounts Receivable
**Uso típico:** Controle de lotes de recebimento; importação de arquivos bancários.

### AR_TRANSMISSIONS_ALL
**Descrição:** Armazena informações sobre transmissões de remessas bancárias, incluindo arquivos enviados a bancos para cobrança automática (direct debit) ou confirmação de pagamento.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de remessas bancárias; rastreamento de arquivos CNAB/SEPA enviados.

---

## 4. Ajustes e Distribuições

### AR_ADJUSTMENTS_ALL
**Descrição:** Armazena ajustes de faturas, incluindo nome da atividade, valor, informações contábeis, motivo e tipo de ajuste. Cada linha representa um ajuste individual aplicado a uma transação.
**Módulo:** Accounts Receivable
**Uso típico:** Write-offs; ajustes de valor; reclassificações contábeis; análise de perdas.

### AR_REVENUE_ADJUSTMENTS_ALL
**Descrição:** Armazena ajustes de receita realizados sobre linhas de transação, permitindo redistribuição ou diferimento de receita entre períodos ou contas.
**Módulo:** Accounts Receivable
**Uso típico:** Revenue management; ajustes de reconhecimento de receita; compliance contábil.

### AR_RATE_ADJUSTMENTS_ALL
**Descrição:** Armazena ajustes de taxa de câmbio aplicados a transações em moeda estrangeira, registrando diferenças cambiais e reavaliações.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de variação cambial; reavaliação de saldos em moeda estrangeira.

### AR_DISTRIBUTIONS_ALL
**Descrição:** Armazena as distribuições contábeis de recebimentos, recebimentos avulsos, ajustes, aplicações de notas de crédito, aplicações de recebimentos e transações de duplicatas a receber. Liga-se às tabelas de origem via `SOURCE_TABLE` e `SOURCE_ID`.
**Módulo:** Accounts Receivable
**Uso típico:** Reconciliação contábil detalhada; auditoria de lançamentos; drill-down de GL para AR.

### AR_DISTRIBUTION_SETS_ALL
**Descrição:** Define conjuntos de distribuição contábil pré-configurados para recebimentos avulsos, especificando como os valores devem ser alocados entre contas contábeis.
**Módulo:** Accounts Receivable
**Uso típico:** Automação de contabilização de miscellaneous receipts; padronização de alocações.

### AR_DETAILED_DISTRIBUTIONS_ALL
**Descrição:** Armazena distribuições contábeis detalhadas em nível mais granular que `AR_DISTRIBUTIONS_ALL`, suportando subledger accounting (XLA).
**Módulo:** Accounts Receivable
**Uso típico:** Integração com Subledger Accounting; reconciliação detalhada; relatórios de auditoria.

---

## 5. Aging, Cobranças e Disputas

### AR_AGING_BUCKETS
**Descrição:** Define faixas de aging (ex.: 0-30 dias, 31-60 dias, 61-90 dias). Cada registro representa um conjunto de faixas de vencimento para análise de inadimplência.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de relatórios de aging; análise de risco de crédito.

### AR_AGING_BUCKET_LINES_B
**Descrição:** Armazena as linhas individuais de cada faixa de aging, definindo os intervalos de dias (ex.: de 180 a 270 dias vencidos).
**Módulo:** Accounts Receivable
**Uso típico:** Detalhamento das faixas de aging; customização de buckets.

### AR_AGING_BUCKET_LINES_TL
**Descrição:** Tabela de traduções das linhas de aging buckets, com descrições em múltiplos idiomas.
**Módulo:** Accounts Receivable
**Uso típico:** Suporte multi-idioma para relatórios de aging.

### AR_COLLECTORS
**Descrição:** Armazena informações sobre os cobradores (collectors) responsáveis pela cobrança de contas a receber. Cada registro define um cobrador com nome, descrição e status.
**Módulo:** Accounts Receivable / Collections
**Uso típico:** Atribuição de contas a cobradores; relatórios de performance de cobrança.

### AR_DISPUTE_HISTORY
**Descrição:** Registra o histórico de disputas de faturas, incluindo valores disputados, datas, motivos e resoluções. Rastreia o ciclo de vida de cada contestação.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de disputas; análise de motivos de contestação; KPIs de resolução.

### AR_STATEMENT_CYCLES
**Descrição:** Define os ciclos de emissão de extratos (statements) para clientes, determinando a periodicidade e datas de corte para geração de demonstrativos.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de ciclos de extrato; automação de envio de demonstrativos.

---

## 6. Juros e Encargos

### AR_INTEREST_HEADERS_ALL
**Descrição:** Armazena os cabeçalhos de cobranças de juros (late charges / finance charges) geradas pelo processo de cálculo de juros sobre faturas vencidas.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de juros de mora; relatórios de receita financeira.

### AR_INTEREST_LINES_ALL
**Descrição:** Armazena as linhas de detalhe dos juros calculados, vinculando cada cobrança de juros à fatura original e ao período de cálculo.
**Módulo:** Accounts Receivable
**Uso típico:** Detalhamento de juros por fatura; conciliação de encargos financeiros.

### AR_CHARGE_SCHEDULES
**Descrição:** Define os cronogramas de cobrança de encargos (charge schedules) aplicáveis a faturas vencidas.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de políticas de cobrança de encargos.

### AR_CHARGE_SCHEDULE_HDRS
**Descrição:** Armazena os cabeçalhos dos cronogramas de encargos, definindo nome, tipo e período de vigência.
**Módulo:** Accounts Receivable
**Uso típico:** Administração de tabelas de encargos; versionamento de políticas.

### AR_CHARGE_SCHEDULE_LINES
**Descrição:** Armazena as linhas de detalhe dos cronogramas de encargos, incluindo faixas de valor, percentuais e valores fixos aplicáveis.
**Módulo:** Accounts Receivable
**Uso típico:** Definição granular de taxas de juros/multas por faixa de atraso ou valor.

---

## 7. Faturamento Consolidado e Diferimentos

### AR_CONS_INV_ALL
**Descrição:** Armazena informações sobre faturamento consolidado (balance forward billing). Quando o processo de geração de faturamento consolidado é executado, todas as faturas de um período são agrupadas e registradas nesta tabela.
**Módulo:** Accounts Receivable
**Uso típico:** Faturamento consolidado mensal; gestão de clientes com billing consolidado.

### AR_DEFERRED_LINES_ALL
**Descrição:** Armazena linhas de receita diferida (deferred revenue), rastreando valores cuja receita ainda não foi reconhecida e aguarda cumprimento de critérios de reconhecimento.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de receita diferida; relatórios de revenue recognition; compliance ASC 606/IFRS 15.

---

## 8. Configuração e Parâmetros AR

### AR_SYSTEM_PARAMETERS_ALL
**Descrição:** Armazena os parâmetros de configuração do módulo Receivables por business unit. Contém opções de instalação como moeda funcional, métodos de aplicação automática, configurações de sequenciamento e padrões operacionais.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração do módulo AR; consulta de parâmetros operacionais por BU.

### AR_RECEIVABLES_TRX_ALL
**Descrição:** Define as atividades de recebíveis (receivables activities) utilizadas em ajustes, recebimentos avulsos e encargos financeiros. Cada registro associa uma atividade a contas contábeis específicas.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de atividades para write-offs, ajustes e miscellaneous receipts.

### AR_RECEIPT_CLASSES
**Descrição:** Define as classes de recebimento, que determinam o comportamento contábil dos receipts (ex.: confirmação manual ou automática, remessa ao banco, compensação).
**Módulo:** Accounts Receivable
**Uso típico:** Configuração do ciclo de vida de recebimentos; definição de métodos de compensação.

### AR_RECEIPT_METHODS
**Descrição:** Armazena os métodos de recebimento, que são atributos associados a classes de recebimento para definir como os receipts são contabilizados e suas aplicações processadas. Para recebimentos automáticos, define as regras de criação.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de formas de pagamento (boleto, TED, cartão); automação de recebimentos.

### AR_RECEIPT_METHOD_ACCOUNTS_ALL
**Descrição:** Armazena as contas contábeis associadas a cada método de recebimento por business unit, definindo as contas de compensação, remessa e confirmação.
**Módulo:** Accounts Receivable
**Uso típico:** Mapeamento contábil de recebimentos; configuração de contas bancárias por método.

### AR_AUTOCASH_HIERARCHIES
**Descrição:** Define os conjuntos de regras AutoCash (AutoCash rule sets), que determinam a sequência de aplicação automática de recebimentos a faturas em aberto.
**Módulo:** Accounts Receivable
**Uso típico:** Automação de aplicação de recebimentos; configuração de hierarquias de matching.

### AR_AUTOMATCH_RULES
**Descrição:** Define regras de correspondência automática (automatch) para vincular recebimentos a faturas usando critérios como número da fatura, valor e referência bancária.
**Módulo:** Accounts Receivable
**Uso típico:** Automação de reconciliação de recebimentos; redução de trabalho manual de aplicação.

### AR_APP_RULE_SETS
**Descrição:** Define conjuntos de regras de aplicação (application rule sets) que governam como os recebimentos são aplicados automaticamente.
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de prioridades de aplicação automática.

### AR_APP_EXCEPTION_RULES
**Descrição:** Define regras de exceção para o processo de aplicação automática de recebimentos, tratando casos especiais como diferenças de valor ou pagamentos parciais.
**Módulo:** Accounts Receivable
**Uso típico:** Tratamento de exceções no processo de cash application.

### AR_APPROVAL_ACTION_HISTORY
**Descrição:** Registra o histórico de ações de aprovação sobre transações e ajustes de recebíveis, incluindo aprovador, data e decisão.
**Módulo:** Accounts Receivable
**Uso típico:** Auditoria de aprovações; workflow de ajustes e créditos.

### AR_MEMO_LINES_ALL_B
**Descrição:** Define as linhas de memo padrão (standard memo lines) utilizadas como templates para criação rápida de notas de débito e crédito.
**Módulo:** Accounts Receivable
**Uso típico:** Padronização de itens recorrentes em memos; agilidade na criação de transações.

### AR_MEMO_LINES_ALL_TL
**Descrição:** Tabela de traduções das linhas de memo padrão, com descrições em múltiplos idiomas.
**Módulo:** Accounts Receivable
**Uso típico:** Suporte multi-idioma para memo lines.

### AR_LOOKUPS
**Descrição:** Armazena valores de lookup (listas de valores) específicos do módulo Accounts Receivable, como tipos de status, categorias e classificações.
**Módulo:** Accounts Receivable
**Uso típico:** Decodificação de códigos em relatórios; validação de dados.

### AR_SALES_CREDIT_TYPES
**Descrição:** Define os tipos de crédito de venda (sales credit types) disponíveis, como receita (revenue) e não-receita (non-revenue).
**Módulo:** Accounts Receivable
**Uso típico:** Classificação de comissões; relatórios de crédito de vendas.

### AR_STANDARD_TEXT_B
**Descrição:** Armazena textos padrão reutilizáveis para inclusão em faturas, dunning letters e correspondências com clientes.
**Módulo:** Accounts Receivable
**Uso típico:** Padronização de textos em documentos de cobrança.

### AR_STANDARD_TEXT_TL
**Descrição:** Tabela de traduções dos textos padrão, com versões em múltiplos idiomas.
**Módulo:** Accounts Receivable
**Uso típico:** Suporte multi-idioma para textos de cobrança e faturamento.

### AR_TRANSMISSION_FORMATS
**Descrição:** Define os formatos de transmissão utilizados para envio de remessas bancárias e arquivos de cobrança automática (direct debit).
**Módulo:** Accounts Receivable
**Uso típico:** Configuração de layouts de arquivo bancário; integração com sistemas de cobrança.

---

## 9. Reconciliação

### AR_RECON_SUMMARY_DETAILS
**Descrição:** Armazena os detalhes resumidos do processo de reconciliação entre AR e GL, incluindo saldos por conta e diferenças identificadas.
**Módulo:** Accounts Receivable
**Uso típico:** Reconciliação periódica AR vs. GL; identificação de discrepâncias.

### AR_RECON_DIFFERENCE_DETAILS
**Descrição:** Armazena os detalhes das diferenças encontradas durante o processo de reconciliação, permitindo drill-down nas divergências.
**Módulo:** Accounts Receivable
**Uso típico:** Investigação de diferenças de reconciliação; ajustes corretivos.

### AR_RECON_SUMMARY_PARAMETERS
**Descrição:** Armazena os parâmetros utilizados na execução do processo de reconciliação, como período, ledger e business unit.
**Módulo:** Accounts Receivable
**Uso típico:** Rastreamento de execuções de reconciliação; auditoria de parâmetros.

---

## 10. Histórico e Referências

### AR_TRANSACTION_HISTORY_ALL
**Descrição:** Contém o histórico detalhado de cada transação de duplicata a receber (bill receivable), registrando atividades e eventos do ciclo de vida como criação, aceite, remessa e compensação.
**Módulo:** Accounts Receivable
**Uso típico:** Rastreamento do ciclo de vida de bills receivable; auditoria de transações.

### AR_REF_ACCOUNTS_ALL
**Descrição:** Armazena contas contábeis de referência associadas a transações de recebíveis, utilizadas para distribuição automática de valores.
**Módulo:** Accounts Receivable
**Uso típico:** Mapeamento de contas de referência; configuração de AutoAccounting.

### AR_REMIT_TO_LOCS_ALL
**Descrição:** Armazena os locais de remessa (remit-to locations) disponíveis por business unit, definindo os endereços para os quais os clientes devem enviar pagamentos.
**Módulo:** Accounts Receivable
**Uso típico:** Gestão de endereços de cobrança por localidade ou business unit.

---

## 11. Clientes e Partes — Trading Community Architecture (`HZ_`)

> **Nota:** As tabelas com prefixo `HZ_` pertencem ao módulo **Trading Community Architecture (TCA)** e são referenciadas pelo AR para dados de clientes, contatos, endereços e relacionamentos.

### HZ_PARTIES
**Descrição:** Tabela central do TCA que armazena todas as partes (parties) — organizações e pessoas. Cada registro representa uma entidade única com nome, tipo (ORGANIZATION, PERSON) e atributos gerais.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Identificação de clientes; base para todos os relacionamentos comerciais.

### HZ_CUST_ACCOUNTS
**Descrição:** Armazena as contas de cliente criadas a partir de parties. Um mesmo party pode ter múltiplas contas de cliente com configurações distintas de crédito, faturamento e cobrança.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Gestão de contas de cliente; associação de transações AR a contas.

### HZ_CUST_ACCT_SITES_ALL
**Descrição:** Armazena os sites (endereços) associados a contas de cliente, vinculando cada conta a um ou mais endereços físicos (party sites).
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Gestão de endereços de faturamento e entrega por conta de cliente.

### HZ_CUST_SITE_USES_ALL
**Descrição:** Define os usos (purposes) de cada site de conta de cliente — como Bill-To, Ship-To ou Statements — e armazena configurações específicas por uso.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Determinação de endereço de cobrança (Bill-To) em transações AR.

### HZ_CUST_ACCOUNT_ROLES
**Descrição:** Armazena os papéis (roles) atribuídos a contatos dentro de contas de cliente, como responsável por pagamento ou contato de cobrança.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Identificação de contatos para envio de faturas e cobranças.

### HZ_CUSTOMER_PROFILES_F
**Descrição:** Armazena perfis de crédito de clientes com efetividade temporal (date-effective), incluindo limites de crédito, termos de pagamento padrão e configurações de cobrança.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Análise de crédito; definição de políticas de cobrança por cliente.

### HZ_CUST_PROFILE_AMTS_F
**Descrição:** Armazena os limites de crédito por moeda para cada perfil de cliente, com efetividade temporal.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Controle de exposição de crédito por moeda; análise de risco.

### HZ_CUST_PROFILE_CLASSES
**Descrição:** Define classes de perfil de cliente (profile classes) que servem como templates com configurações padrão de crédito, cobrança e termos de pagamento.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Padronização de políticas de crédito; classificação de clientes por risco.

### HZ_LOCATIONS
**Descrição:** Armazena endereços físicos (logradouro, cidade, estado, CEP, país, coordenadas). Cada registro representa um endereço único reutilizável por múltiplos party sites.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Gestão centralizada de endereços; validação de localidades.

### HZ_PARTY_SITES
**Descrição:** Associa parties (HZ_PARTIES) a endereços físicos (HZ_LOCATIONS), criando um "site" que representa a presença de uma parte em um local específico.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Vinculação de clientes a endereços; base para sites de conta.

### HZ_PARTY_SITE_USES
**Descrição:** Define os usos (purposes) de cada party site, como escritório, fábrica ou depósito.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Classificação de locais por finalidade comercial.

### HZ_ORGANIZATION_PROFILES
**Descrição:** Armazena atributos detalhados de organizações (parties do tipo ORGANIZATION), como CNPJ/tax ID, setor de atuação, porte e informações financeiras.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Análise de perfil de clientes corporativos; due diligence.

### HZ_ORG_CONTACTS
**Descrição:** Armazena informações sobre contatos dentro de organizações, incluindo cargo, departamento e papel do contato.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Gestão de contatos para cobrança e comunicação comercial.

### HZ_CONTACT_POINTS
**Descrição:** Armazena pontos de contato (telefone, e-mail, URL) associados a parties, party sites ou contatos.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Comunicação com clientes; envio eletrônico de faturas.

### HZ_RELATIONSHIPS
**Descrição:** Armazena relacionamentos entre parties, como "subsidiária de", "controladora de" ou "contato de".
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Mapeamento de estruturas societárias; análise de grupos econômicos.

### HZ_RELATIONSHIP_TYPES
**Descrição:** Define os tipos de relacionamento disponíveis entre parties (ex.: empregado de, subsidiária de, parceiro de).
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Configuração de tipos de vínculo entre entidades.

### HZ_CODE_ASSIGNMENTS
**Descrição:** Armazena atribuições de códigos de classificação a parties, permitindo categorização por setor, porte, região e outros critérios.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Segmentação de clientes; filtros em relatórios.

### HZ_CLASS_CATEGORY_CODES_V
**Descrição:** View que apresenta as categorias e códigos de classificação disponíveis no TCA para categorização de parties.
**Módulo:** Trading Community Architecture (referenciada por AR)
**Uso típico:** Consulta de classificações disponíveis; validação de códigos.

---

## 12. Pagamentos — Oracle Payments (`IBY_`)

> **Nota:** As tabelas com prefixo `IBY_` pertencem ao módulo **Oracle Payments** e são referenciadas pelo AR para processamento de pagamentos eletrônicos, cartões de crédito e débito automático.

### IBY_CREDITCARD
**Descrição:** Armazena informações de cartões de crédito de clientes, incluindo dados do cartão registrados manualmente ou importados via API.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Processamento de pagamentos com cartão; tokenização de dados sensíveis.

### IBY_EXT_BANK_ACCOUNTS
**Descrição:** Define contas bancárias externas (de clientes ou fornecedores), armazenando banco, agência, número da conta e dados de validação.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Débito automático (direct debit); cobrança bancária; conciliação.

### IBY_EXTERNAL_PAYERS_ALL
**Descrição:** Armazena atributos de pagamento de clientes (payers), definindo preferências e configurações de cobrança eletrônica por conta de cliente.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Configuração de débito automático por cliente; gestão de autorizações.

### IBY_DEBIT_AUTHORIZATIONS_F
**Descrição:** Armazena autorizações de débito automático (direct debit mandates) com efetividade temporal, incluindo dados do mandato, datas de vigência e status.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Gestão de mandatos SEPA/débito automático; compliance regulatório.

### IBY_PMT_INSTR_USES_ALL
**Descrição:** Associa instrumentos de pagamento (cartões, contas bancárias) a entidades pagadoras/recebedoras, definindo o uso de cada instrumento.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Vinculação de instrumentos de pagamento a contas de cliente.

### IBY_FNDCPT_TX_EXTENSIONS
**Descrição:** Armazena atributos de pagamento para transações de captura de fundos (funds capture), incluindo extensões específicas de cada transação.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Rastreamento de detalhes de transações de pagamento eletrônico.

### IBY_FNDCPT_PMT_CHNNLS_VL
**Descrição:** View que apresenta os canais de pagamento (payment channels) disponíveis, como cartão de crédito, débito automático e transferência bancária.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Consulta de canais de pagamento configurados.

### IBY_PAYMENT_CODES_VL
**Descrição:** View que apresenta os códigos de pagamento disponíveis, utilizados para classificação e roteamento de transações de pagamento.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Classificação de tipos de pagamento em relatórios.

### IBY_TRXN_SUMMARIES_ALL
**Descrição:** Armazena resumos de transações de pagamento processadas, incluindo status, valores, datas e resultados de autorização.
**Módulo:** Oracle Payments (referenciada por AR)
**Uso típico:** Monitoramento de transações de pagamento; relatórios de processamento.

---

## 13. Impostos — Oracle Tax (`ZX_`)

> **Nota:** As tabelas com prefixo `ZX_` pertencem ao módulo **Oracle Tax (E-Business Tax)** e são referenciadas pelo AR para cálculo, isenção e reporting de impostos sobre transações de recebíveis.

### ZX_LINES
**Descrição:** Armazena as linhas de imposto calculadas para transações de múltiplas classes de eventos. Cada registro representa um imposto específico aplicado a uma linha de transação.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Detalhamento de impostos por transação; relatórios fiscais; reconciliação tributária.

### ZX_EXEMPTIONS
**Descrição:** Armazena isenções fiscais — exclusões totais ou parciais de impostos dentro de um período determinado. Cada registro contém o percentual de isenção de uma taxa específica para uma parte, site ou item.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Gestão de isenções fiscais de clientes; compliance tributário.

### ZX_REGISTRATIONS
**Descrição:** Armazena registros fiscais (tax registrations) de partes junto a autoridades tributárias, conferindo direitos e obrigações fiscais.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Validação de inscrições estaduais/municipais; determinação de regime tributário.

### ZX_PARTY_TAX_PROFILE
**Descrição:** Armazena o perfil tributário de cada parte (party), incluindo configurações fiscais, regime de tributação e atributos para cálculo de impostos.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Determinação de regras fiscais por cliente; classificação tributária.

### ZX_PARTY_TAXPAYER_IDNTFS
**Descrição:** Armazena identificadores de contribuinte (taxpayer identifiers) associados a parties, como CNPJ, CPF, VAT number ou Tax ID.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Validação fiscal; emissão de documentos fiscais com identificação do contribuinte.

### ZX_REGIMES_VL
**Descrição:** View que apresenta os regimes fiscais (tax regimes) definidos no sistema, com traduções. Cada regime representa uma jurisdição tributária ou conjunto de regras fiscais.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Consulta de regimes fiscais configurados; filtros em relatórios tributários.

### ZX_JURISDICTIONS_VL
**Descrição:** View que apresenta as jurisdições fiscais, definindo as autoridades tributárias e áreas geográficas onde impostos são aplicáveis.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Determinação de jurisdição tributária por transação; relatórios por localidade.

### ZX_SCO_RATES
**Descrição:** Armazena as alíquotas (tax rates) associadas a condições fiscais específicas, incluindo taxas por regime, jurisdição e período de vigência.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Consulta de alíquotas aplicáveis; cálculo de impostos.

### ZX_FC_TYPES_VL
**Descrição:** View que apresenta os tipos de classificações fiscais (fiscal classification types) disponíveis no sistema.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Configuração de categorias de classificação fiscal.

### ZX_FC_BUSINESS_CATEGORIES_V
**Descrição:** View que apresenta as categorias de negócio fiscais (business categories) para classificação tributária de transações.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Classificação fiscal de transações por natureza de negócio.

### ZX_FC_INTENDED_USE_V
**Descrição:** View que apresenta os usos pretendidos (intended use) de produtos/serviços para fins de determinação fiscal.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Classificação de uso final para cálculo de impostos diferenciados.

### ZX_FC_PRODUCT_CATEGORIES_V
**Descrição:** View que apresenta as categorias de produto para classificação fiscal.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Classificação fiscal de produtos; determinação de NCM/HS Code.

### ZX_FC_PRODUCT_FISCAL_V
**Descrição:** View que apresenta classificações fiscais de produtos, incluindo códigos fiscais específicos por jurisdição.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Determinação de tributação por classificação fiscal do produto.

### ZX_FC_USER_DEFINED_V
**Descrição:** View que apresenta classificações fiscais definidas pelo usuário (user-defined fiscal classifications) para cenários tributários customizados.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Classificações fiscais personalizadas para atender requisitos locais.

### ZX_PRODUCT_TYPES_V
**Descrição:** View que apresenta os tipos de produto (goods, services) para fins de determinação fiscal.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Distinção entre bens e serviços para aplicação de regras fiscais.

### ZX_REPORTING_TYPES_VL
**Descrição:** View que apresenta os tipos de reporting fiscal disponíveis, definindo categorias de informações fiscais obrigatórias.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Configuração de obrigações fiscais acessórias.

### ZX_REPORTING_CODES_VL
**Descrição:** View que apresenta os códigos de reporting fiscal, utilizados para classificação de transações em declarações fiscais.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Mapeamento de códigos para SPED, DIRF e outras obrigações acessórias.

### ZX_REPORT_CODES_ASSOC
**Descrição:** Armazena as associações entre códigos de reporting fiscal e entidades tributárias (regimes, impostos, jurisdições), definindo quais códigos se aplicam a cada contexto.
**Módulo:** Oracle Tax (referenciada por AR)
**Uso típico:** Vinculação de códigos de reporting a configurações fiscais; automação de obrigações.

---

## 14. Contabilidade Geral e Subledger (`GL_`, `XLA_`, `XLE_`)

> **Nota:** Tabelas referenciadas pelo AR para integração contábil com General Ledger e Subledger Accounting.

### GL_CODE_COMBINATIONS
**Descrição:** Armazena as combinações válidas de segmentos contábeis (chart of accounts) para cada estrutura de accounting flexfield. Cada registro representa uma conta contábil completa.
**Módulo:** General Ledger (referenciada por AR)
**Uso típico:** Validação de contas contábeis em distribuições AR; relatórios por conta.

### GL_LEDGERS
**Descrição:** Armazena informações sobre os ledgers (razões contábeis) e ledger sets definidos no sistema, incluindo nome, moeda, calendário, plano de contas e período contábil.
**Módulo:** General Ledger (referenciada por AR)
**Uso típico:** Identificação do ledger associado a transações AR; configuração multi-ledger.

### GL_DAILY_CONVERSION_TYPES
**Descrição:** Define os tipos de conversão de moeda disponíveis para taxas de câmbio diárias (ex.: Corporate, Spot, User).
**Módulo:** General Ledger (referenciada por AR)
**Uso típico:** Conversão de transações em moeda estrangeira; reavaliação cambial.

### XLA_EVENTS
**Descrição:** Armazena eventos contábeis do Subledger Accounting (SLA). Cada evento representa uma ação de negócio que gera lançamentos contábeis (ex.: criação de fatura, aplicação de recebimento).
**Módulo:** Subledger Accounting (referenciada por AR)
**Uso típico:** Rastreamento de eventos contábeis; auditoria de lançamentos; reconciliação SLA vs. GL.

### XLE_ENTITY_PROFILES
**Descrição:** Armazena perfis de entidades legais (legal entities), incluindo nome, jurisdição, identificadores fiscais e atributos regulatórios.
**Módulo:** Legal Entity Configurator (referenciada por AR)
**Uso típico:** Identificação da entidade legal em transações AR; compliance regulatório.

---

## 15. Cash Management / Bancos (`CE_`)

> **Nota:** Tabelas do módulo **Cash Management** referenciadas pelo AR para gestão de contas bancárias e reconciliação.

### CE_BANK_ACCT_USES_ALL
**Descrição:** Armazena os usos (purposes) de contas bancárias internas por business unit, definindo para quais finalidades cada conta pode ser utilizada (recebimentos, pagamentos, etc.).
**Módulo:** Cash Management (referenciada por AR)
**Uso típico:** Vinculação de métodos de recebimento a contas bancárias.

### CE_BANK_BRANCHES_V
**Descrição:** View que apresenta informações de agências bancárias, incluindo código do banco, número da agência, nome e endereço.
**Módulo:** Cash Management (referenciada por AR)
**Uso típico:** Identificação de agências bancárias em recebimentos e remessas.

### CE_INTERNAL_BANK_ACCTS_V
**Descrição:** View que apresenta as contas bancárias internas da organização, incluindo banco, agência, número da conta, moeda e status.
**Módulo:** Cash Management (referenciada por AR)
**Uso típico:** Consulta de contas bancárias disponíveis para recebimentos; reconciliação bancária.

---

## 16. Itens e Inventário (`EGP_`, `INV_`)

> **Nota:** Tabelas dos módulos **Product Information Management** e **Inventory** referenciadas pelo AR para informações de itens faturados.

### EGP_SYSTEM_ITEMS_B_V
**Descrição:** View baseada na tabela `EGP_SYSTEM_ITEMS_B` que armazena informações gerais de itens, como número do item, descrição, atributos operacionais e configurações de inventário.
**Módulo:** Product Information Management (referenciada por AR)
**Uso típico:** Identificação de itens em linhas de transação AR.

### EGP_SYSTEM_ITEMS_VL
**Descrição:** View que combina dados base de itens com traduções, fornecendo número do item e descrição no idioma da sessão.
**Módulo:** Product Information Management (referenciada por AR)
**Uso típico:** Exibição de descrições de itens em relatórios AR.

### EGP_CATEGORIES_VL
**Descrição:** View que apresenta as categorias de itens com traduções, utilizadas para classificação de produtos em hierarchias de catálogo.
**Módulo:** Product Information Management (referenciada por AR)
**Uso típico:** Classificação de itens faturados por categoria; análise de receita por grupo de produto.

### INV_ORG_PARAMETERS
**Descrição:** Armazena parâmetros de configuração por organização de inventário, incluindo organização mestre, controles de lote/série e opções de rastreamento.
**Módulo:** Inventory Management (referenciada por AR)
**Uso típico:** Identificação da organização de inventário associada a transações AR.

### INV_UNITS_OF_MEASURE_B
**Descrição:** Tabela base que armazena as unidades de medida (UoM) definidas no sistema, com código e classe de unidade.
**Módulo:** Inventory Management (referenciada por AR)
**Uso típico:** Validação de unidades de medida em linhas de transação.

### INV_UNITS_OF_MEASURE_TL
**Descrição:** Tabela de traduções das unidades de medida, com nomes e descrições em múltiplos idiomas.
**Módulo:** Inventory Management (referenciada por AR)
**Uso típico:** Exibição de unidades de medida no idioma do usuário.

---

## 17. RH e Organizações (`HR_`)

> **Nota:** Tabelas do módulo **Human Resources** referenciadas pelo AR para estrutura organizacional e business units.

### HR_ALL_ORGANIZATION_UNITS_F
**Descrição:** Armazena todas as unidades organizacionais com efetividade temporal (date-effective), incluindo business units, departamentos e organizações de inventário.
**Módulo:** Human Resources (referenciada por AR)
**Uso típico:** Identificação de business units associadas a transações AR.

### HR_ALL_ORGANIZATION_UNITS_F_VL
**Descrição:** View que combina dados organizacionais com traduções, fornecendo nomes de organizações no idioma da sessão.
**Módulo:** Human Resources (referenciada por AR)
**Uso típico:** Exibição de nomes de business units em relatórios.

### HR_ORGANIZATION_INFORMATION_F
**Descrição:** Armazena informações complementares de organizações com efetividade temporal, como classificações, atributos fiscais e configurações específicas por tipo de organização.
**Módulo:** Human Resources (referenciada por AR)
**Uso típico:** Consulta de atributos adicionais de business units.

### HR_ORGANIZATION_UNITS_F_TL
**Descrição:** Tabela de traduções dos nomes de unidades organizacionais em múltiplos idiomas.
**Módulo:** Human Resources (referenciada por AR)
**Uso típico:** Suporte multi-idioma para nomes de organizações.

---

## 18. Fundação, Business Units e Usuários (`FND_`, `FUN_`, `PER_`)

> **Nota:** Tabelas de infraestrutura e configuração referenciadas pelo AR.

### FND_DOCUMENT_SEQUENCES
**Descrição:** Armazena as definições de sequências de documentos (document sequences), utilizadas para numeração automática e controlada de transações, recebimentos e outros documentos.
**Módulo:** Application Object Library (referenciada por AR)
**Uso típico:** Numeração sequencial de faturas e recebimentos; compliance com requisitos de auditoria.

### FND_TERRITORIES_VL
**Descrição:** View que apresenta os territórios (países e regiões) definidos no sistema com traduções, incluindo códigos ISO e nomes.
**Módulo:** Application Object Library (referenciada por AR)
**Uso típico:** Identificação de países em endereços de clientes; relatórios por território.

### FUN_BU_PERF_V
**Descrição:** View de performance que apresenta as business units configuradas no sistema, otimizada para consultas frequentes com dados de nome, status e ledger associado.
**Módulo:** Financials Common (referenciada por AR)
**Uso típico:** Consulta rápida de business units; filtros em relatórios financeiros.

### PER_USERS
**Descrição:** Armazena informações sobre os usuários do sistema, vinculando credenciais de acesso a registros de pessoa (person records).
**Módulo:** Human Resources / Security (referenciada por AR)
**Uso típico:** Identificação de usuários que criaram ou modificaram transações; auditoria.

### PER_PERSON_NAMES_F_V
**Descrição:** View que apresenta os nomes de pessoas com efetividade temporal, incluindo nome completo, primeiro nome e sobrenome no formato adequado à legislação local.
**Módulo:** Human Resources (referenciada por AR)
**Uso típico:** Exibição de nomes de usuários e contatos em relatórios AR.

---

## 19. Vendedores (`JTF_`)

> **Nota:** Tabela do módulo **Resource Management** referenciada pelo AR para atribuição de crédito de venda.

### JTF_RS_SALESREPS
**Descrição:** Armazena informações sobre os representantes de vendas (salesreps), incluindo nome, número, status, datas de vigência e organização de vendas associada.
**Módulo:** Resource Management (referenciada por AR)
**Uso típico:** Atribuição de crédito de venda em transações AR; relatórios de comissão.

---

## Referências

- [Oracle Fusion Cloud Financials — Receivables Tables](https://docs.oracle.com/en/cloud/saas/financials/25d/faofc/receivables-tables.html)
- [Oracle Fusion Cloud — Tables and Views for Financials (OEDMF)](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/financials-tables-and-views.html)
- [RA_CUSTOMER_TRX_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/racustomertrxall-5191.html)
- [AR_CASH_RECEIPTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/arcashreceiptsall-22922.html)
- [AR_PAYMENT_SCHEDULES_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/arpaymentschedulesall-26032.html)
- [AR_RECEIVABLE_APPLICATIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/arreceivableapplicationsall-29439.html)
- [AR_ADJUSTMENTS_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/aradjustmentsall-6572.html)
- [AR_DISTRIBUTIONS_ALL](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/ardistributionsall-17923.html)
- [AR_AGING_BUCKETS](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/aragingbuckets-13098.html)
- [GL_CODE_COMBINATIONS](https://docs.oracle.com/en/cloud/saas/financials/25d/oedmf/glcodecombinations-22130.html)
- [GL_LEDGERS](https://docs.oracle.com/en/cloud/saas/financials/24a/oedmf/glledgers-25401.html)
- [ZX_LINES](https://docs.oracle.com/en/cloud/saas/financials/24b/oedmf/zxlines-12467.html)
- [ZX_EXEMPTIONS](https://docs.oracle.com/cd/E51367_01/financialsop_gs/OEDMF/ZX_EXEMPTIONS_tbl.htm)
- [ZX_REGISTRATIONS](https://docs.oracle.com/en/cloud/saas/financials/24a/oedmf/zxregistrations-26635.html)
- [Oracle Trading Community Architecture Reference](https://docs.oracle.com/cd/E18727_01/doc.121/e13569/T169891T392486.htm)
