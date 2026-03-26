# Oracle Fusion — Human Capital Management (HCM) — Database Tables

> Referência de tabelas do módulo HCM extraídas do BICC Database Mapping (Release 13/25A).
> Fonte: documentação oficial Oracle Fusion Cloud ERP.
> Total: **804 tabelas** organizadas por área funcional.

---

## Sumário

1. [Ausências (ANC\_*)](#1-ausências-anc)
2. [Benefícios (BEN\_*)](#2-benefícios-ben)
3. [Remuneração e Compensação (CMP\_*)](#3-remuneração-e-compensação-cmp)
4. [Fast Formula e Tabelas de Usuário (FF\_*)](#4-fast-formula-e-tabelas-de-usuário-ff)
5. [Fundação / Infraestrutura (FND\_*)](#5-fundação--infraestrutura-fnd)
6. [Business Units e Funções (FUN\_*)](#6-business-units-e-funções-fun)
7. [HCM Lookups e Configuração (HCM\_*)](#7-hcm-lookups-e-configuração-hcm)
8. [Modelagem de Força de Trabalho (HMO\_*)](#8-modelagem-de-força-de-trabalho-hmo)
9. [Saúde e Segurança do Trabalho (HNS\_*)](#9-saúde-e-segurança-do-trabalho-hns)
10. [Desempenho e Avaliações (HRA\_*)](#10-desempenho-e-avaliações-hra)
11. [Transações e Console HR (HRC\_*)](#11-transações-e-console-hr-hrc)
12. [Desenvolvimento e Intenções de Carreira (HRD\_*)](#12-desenvolvimento-e-intenções-de-carreira-hrd)
13. [Metas e Objetivos (HRG\_*)](#13-metas-e-objetivos-hrg)
14. [Planos de Sucessão (HRM\_*)](#14-planos-de-sucessão-hrm)
15. [Questionários (HRQ\_*)](#15-questionários-hrq)
16. [Talent Review / Reuniões de Calibração (HRR\_*)](#16-talent-review--reuniões-de-calibração-hrr)
17. [Perfis de Talento e Competências (HRT\_*)](#17-perfis-de-talento-e-competências-hrt)
18. [Integração de Dados de Pessoa (HRY\_*)](#18-integração-de-dados-de-pessoa-hry)
19. [Organizações e Posições (HR\_*)](#19-organizações-e-posições-hr)
20. [Demanda de Mão de Obra e Escalas (HTS\_*)](#20-demanda-de-mão-de-obra-e-escalas-hts)
21. [Gestão de Tempo e Ponto (HWM\_*)](#21-gestão-de-tempo-e-ponto-hwm)
22. [Configuração de Timecard / Layout (HXT\_*)](#22-configuração-de-timecard--layout-hxt)
23. [Geografia e Localização (HZ\_*)](#23-geografia-e-localização-hz)
24. [Organizações de Inventário (INV\_*)](#24-organizações-de-inventário-inv)
25. [Recrutamento (IRC\_*)](#25-recrutamento-irc)
26. [Recursos e Gerentes (JTF\_*)](#26-recursos-e-gerentes-jtf)
27. [Folha de Pagamento (PAY\_*)](#27-folha-de-pagamento-pay)
28. [Pessoa e Dados Básicos (PER\_*)](#28-pessoa-e-dados-básicos-per)
29. [Aprendizado / Learning (WLF\_*)](#29-aprendizado--learning-wlf)
30. [Entidades Legais (XLE\_*)](#30-entidades-legais-xle)
31. [Escalas e Padrões de Trabalho (ZMM\_*)](#31-escalas-e-padrões-de-trabalho-zmm)

---

## 1. Ausências (ANC)

Tabelas do módulo **Absence Management** — gestão de ausências, acúmulos, planos e registros de afastamento.

### ANC_ABSENCE_CATEGORIES_F
**Descrição:** Categorias de ausência (ex.: doença, férias, licença). Classificação de alto nível para agrupar tipos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Extração de categorias para dashboards de absenteísmo e parametrização de regras.

### ANC_ABSENCE_CATEGORIES_F_TL
**Descrição:** Traduções das categorias de ausência para múltiplos idiomas.
**Módulo:** HCM - Absence Management
**Uso típico:** Suporte a relatórios multilíngues.

### ANC_ABSENCE_PLANS_F
**Descrição:** Planos de ausência que definem regras de acúmulo, elegibilidade e limites de saldo.
**Módulo:** HCM - Absence Management
**Uso típico:** Configuração e auditoria de planos de férias, licenças e bancos de horas.

### ANC_ABSENCE_PLANS_F_TL
**Descrição:** Traduções dos planos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Relatórios multilíngues de planos de ausência.

### ANC_ABSENCE_REASONS_F
**Descrição:** Motivos de ausência disponíveis para justificativa (ex.: consulta médica, emergência familiar).
**Módulo:** HCM - Absence Management
**Uso típico:** Análise de motivos de absenteísmo.

### ANC_ABSENCE_REASONS_F_TL
**Descrição:** Traduções dos motivos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Suporte multilíngue.

### ANC_ABSENCE_TYPES_F
**Descrição:** Tipos de ausência (ex.: férias, licença médica, licença maternidade). Define regras específicas de cada tipo.
**Módulo:** HCM - Absence Management
**Uso típico:** Parametrização de tipos de ausência, relatórios de absenteísmo por tipo.

### ANC_ABSENCE_TYPES_F_TL
**Descrição:** Traduções dos tipos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Suporte multilíngue.

### ANC_ABSENCE_TYPE_CATE_F
**Descrição:** Associação entre tipos de ausência e suas categorias.
**Módulo:** HCM - Absence Management
**Uso típico:** Mapeamento tipo↔categoria para relatórios consolidados.

### ANC_ABSENCE_TYPE_REASONS_F
**Descrição:** Associação entre tipos de ausência e motivos válidos para cada tipo.
**Módulo:** HCM - Absence Management
**Uso típico:** Validação de motivos por tipo de ausência.

### ANC_ABS_CERTIFICATIONS_F_TL
**Descrição:** Traduções das certificações de ausência (ex.: atestado médico obrigatório).
**Módulo:** HCM - Absence Management
**Uso típico:** Suporte multilíngue para requisitos de certificação.

### ANC_ACCRUAL_BANDS_F
**Descrição:** Faixas de acúmulo de ausência — define quantidade de dias/horas acumulados por faixa de tempo de serviço.
**Módulo:** HCM - Absence Management
**Uso típico:** Cálculo de saldos de férias/licenças progressivas.

### ANC_PER_ABS_CERTS
**Descrição:** Certificações de ausência fornecidas pelos colaboradores (ex.: atestados médicos anexados).
**Módulo:** HCM - Absence Management
**Uso típico:** Auditoria de documentos comprobatórios de ausências.

### ANC_PER_ABS_DAILY_DTLS
**Descrição:** Detalhes diários das ausências individuais — breakdown dia a dia de cada registro de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Relatórios detalhados de ausência por dia, cálculo de horas parciais.

### ANC_PER_ABS_ENTRIES
**Descrição:** Registros de ausência individuais dos colaboradores — tabela principal de lançamento de ausências.
**Módulo:** HCM - Absence Management
**Uso típico:** Extração de todas as ausências registradas; base para relatórios de absenteísmo.

### ANC_PER_ABS_ENTRY_DTLS
**Descrição:** Detalhes complementares dos registros de ausência (duração, período, informações adicionais).
**Módulo:** HCM - Absence Management
**Uso típico:** Enriquecimento dos dados de ausências com detalhes operacionais.

### ANC_PER_ABS_MATERNITY
**Descrição:** Registros específicos de licença-maternidade com informações de datas previstas e efetivas.
**Módulo:** HCM - Absence Management
**Uso típico:** Gestão de licenças maternidade, relatórios legais.

### ANC_PER_ABS_PLAN_ENTRIES
**Descrição:** Inscrição de colaboradores em planos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Identificação de quais planos cada colaborador está inscrito.

### ANC_PER_ABS_PLN_SUMM_ENT
**Descrição:** Sumário consolidado de saldos por plano de ausência por colaborador.
**Módulo:** HCM - Absence Management
**Uso típico:** Consulta de saldos de férias, licenças e bancos de horas.

### ANC_PER_ABS_TYPE_ENTRIES
**Descrição:** Entradas de ausência por tipo — visão consolidada por tipo de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Relatórios de ausência agrupados por tipo.

### ANC_PER_ACCRUAL_ENTRIES
**Descrição:** Lançamentos de acúmulo (accrual) de ausência — créditos e débitos no saldo de cada colaborador.
**Módulo:** HCM - Absence Management
**Uso típico:** Rastreamento de movimentação de saldos de ausência.

### ANC_PER_ACRL_ENTRY_DTLS
**Descrição:** Detalhes dos lançamentos de acúmulo de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Auditoria detalhada de cálculos de acúmulo.

### ANC_PER_PLAN_ENROLLMENT
**Descrição:** Inscrição/enrollment de colaboradores nos planos de ausência.
**Módulo:** HCM - Absence Management
**Uso típico:** Gestão de elegibilidade e inscrição em planos.

---

## 2. Benefícios (BEN)

Tabelas do módulo **Benefits** — planos de benefícios, elegibilidade, enrollment e administração.

### BEN_ACTN_TYP_VL
**Descrição:** View de tipos de ação de benefícios com tradução (value list). Define ações possíveis no processo de enrollment.
**Módulo:** HCM - Benefits
**Uso típico:** Referência de ações de benefícios.

### BEN_BENEFIT_RELATIONS_F
**Descrição:** Relações de benefícios por pessoa — vincula colaboradores ao contexto de elegibilidade de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Base para determinação de elegibilidade.

### BEN_BENFTS_GRP
**Descrição:** Grupos de benefícios — classificação usada para regras de elegibilidade e cálculo de taxas.
**Módulo:** HCM - Benefits
**Uso típico:** Segmentação de colaboradores em grupos para aplicação de regras de benefícios.

### BEN_BILL_CALENDAR
**Descrição:** Calendário de faturamento de benefícios — define ciclos de cobrança.
**Módulo:** HCM - Benefits
**Uso típico:** Configuração de ciclos de billing.

### BEN_BILL_CHARGES
**Descrição:** Cobranças de benefícios — valores a cobrar por participante.
**Módulo:** HCM - Benefits
**Uso típico:** Extração de valores cobrados.

### BEN_BILL_CHARGE_DETAILS
**Descrição:** Detalhes das cobranças de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Breakdown de cobranças individuais.

### BEN_BILL_CHARGE_PAYMENTS
**Descrição:** Pagamentos vinculados às cobranças de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Reconciliação de pagamentos de benefícios.

### BEN_BILL_CYCLE
**Descrição:** Ciclos de faturamento para administração de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Configuração de periodicidade de cobranças.

### BEN_BILL_ENRT_RSLT
**Descrição:** Resultados de enrollment vinculados ao faturamento.
**Módulo:** HCM - Benefits
**Uso típico:** Cruzamento entre inscrição e cobrança.

### BEN_BILL_PAYMENTS
**Descrição:** Pagamentos de faturamento de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Controle de pagamentos recebidos.

### BEN_BILL_PER_CREDIT
**Descrição:** Créditos por pessoa no faturamento de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Ajustes e créditos em contas de benefícios.

### BEN_CRT_ORDR_F
**Descrição:** Ordens judiciais relacionadas a benefícios (ex.: pensão alimentícia, ordens de cobertura).
**Módulo:** HCM - Benefits
**Uso típico:** Compliance com ordens judiciais de cobertura de dependentes.

### BEN_CRT_ORDR_PL_DPNT
**Descrição:** Dependentes cobertos por ordens judiciais vinculados a planos de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Gestão de dependentes por determinação judicial.

### BEN_DOCS_PRVDD_DTLS
**Descrição:** Detalhes de documentos fornecidos no processo de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Rastreamento de documentação comprobatória.

### BEN_ELIGY_PRFL
**Descrição:** Perfis de elegibilidade — define critérios para elegibilidade a planos de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Configuração de regras de elegibilidade.

### BEN_ELIG_CVRD_DPNT
**Descrição:** Dependentes elegíveis cobertos por planos de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Relatórios de dependentes com cobertura ativa.

### BEN_ELIG_OBJ_ELIG_PROFL_F
**Descrição:** Associação entre objetos de elegibilidade e perfis de elegibilidade.
**Módulo:** HCM - Benefits
**Uso típico:** Configuração avançada de regras de elegibilidade.

### BEN_ELIG_OBJ_F
**Descrição:** Objetos de elegibilidade — entidades avaliadas nas regras de elegibilidade.
**Módulo:** HCM - Benefits
**Uso típico:** Definição de critérios de elegibilidade.

### BEN_ELIG_PERSON_DETAILS_V
**Descrição:** View de detalhes de elegibilidade por pessoa — consolida dados de elegibilidade.
**Módulo:** HCM - Benefits
**Uso típico:** Consulta rápida de elegibilidade de colaboradores.

### BEN_ELIG_RSLT_F
**Descrição:** Resultados de elegibilidade — registro de quem é elegível a quais planos.
**Módulo:** HCM - Benefits
**Uso típico:** Relatórios de elegibilidade processada.

### BEN_LEGAL_DISCLAIMER
**Descrição:** Disclaimers legais apresentados durante o enrollment de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Compliance e auditoria de aceite de termos.

### BEN_LER_F
**Descrição:** Life Events (eventos de vida) — define eventos que disparam reavaliação de benefícios (casamento, nascimento, etc.).
**Módulo:** HCM - Benefits
**Uso típico:** Configuração de eventos de vida para reprocessamento de elegibilidade.

### BEN_OPT_F
**Descrição:** Opções de planos de benefícios (ex.: cobertura individual, familiar, etc.).
**Módulo:** HCM - Benefits
**Uso típico:** Definição de opções dentro de cada plano.

### BEN_PER_BENEFIT_GROUP_F
**Descrição:** Grupo de benefícios atribuído a cada colaborador.
**Módulo:** HCM - Benefits
**Uso típico:** Segmentação de benefícios por grupo.

### BEN_PER_BILL_INFO_F
**Descrição:** Informações de faturamento por pessoa.
**Módulo:** HCM - Benefits
**Uso típico:** Dados de cobrança individual.

### BEN_PER_BNF_ORG
**Descrição:** Beneficiários organizacionais — entidades beneficiárias de planos (ex.: seguros).
**Módulo:** HCM - Benefits
**Uso típico:** Gestão de beneficiários designados.

### BEN_PER_IN_LER
**Descrição:** Eventos de vida por pessoa — registra quais life events foram processados para cada colaborador.
**Módulo:** HCM - Benefits
**Uso típico:** Rastreamento de eventos de vida processados.

### BEN_PER_LE_HABITS_COV_F
**Descrição:** Hábitos e cobertura de estilo de vida por pessoa (ex.: fumante, prática de exercícios).
**Módulo:** HCM - Benefits
**Uso típico:** Dados para cálculo de taxas de benefícios baseadas em estilo de vida.

### BEN_PGM_F
**Descrição:** Programas de benefícios — agrupamento de planos de benefícios em um programa.
**Módulo:** HCM - Benefits
**Uso típico:** Hierarquia de benefícios: Programa → Plano → Opção.

### BEN_PIL_ELCTBL_CHC_POPL
**Descrição:** Escolhas elegíveis por população — opções de enrollment disponíveis durante janela aberta.
**Módulo:** HCM - Benefits
**Uso típico:** Processo de open enrollment.

### BEN_PL_BNF
**Descrição:** Beneficiários designados nos planos de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Gestão de beneficiários de seguros e planos.

### BEN_PL_F
**Descrição:** Planos de benefícios — tabela principal de definição de planos (saúde, dental, vida, etc.).
**Módulo:** HCM - Benefits
**Uso típico:** Cadastro e consulta de planos de benefícios.

### BEN_PL_TYP_F
**Descrição:** Tipos de planos de benefícios (ex.: médico, odontológico, seguro de vida).
**Módulo:** HCM - Benefits
**Uso típico:** Classificação de planos.

### BEN_PRMRY_CARE_PRVDR
**Descrição:** Provedores de cuidados primários designados pelo colaborador.
**Módulo:** HCM - Benefits
**Uso típico:** Gestão de médicos/provedores de referência.

### BEN_PROGRAM_HIERARCHY_V
**Descrição:** View hierárquica de programas de benefícios (Programa → Plano → Opção).
**Módulo:** HCM - Benefits
**Uso típico:** Visualização da estrutura completa de benefícios.

### BEN_PRTT_ENRT_ACTN
**Descrição:** Ações de enrollment pendentes para participantes de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Workflow de enrollment.

### BEN_PRTT_ENRT_CTFN_PRVDD
**Descrição:** Certificações fornecidas durante o enrollment de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Rastreamento de documentos de enrollment.

### BEN_PRTT_ENRT_RSLT
**Descrição:** Resultados de enrollment de participantes — tabela principal de inscrições ativas/históricas em benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Extração de inscrições de benefícios; relatórios de cobertura ativa.

### BEN_PRTT_LEG_DISCMR_ACTN
**Descrição:** Ações de aceite de disclaimers legais por participante.
**Módulo:** HCM - Benefits
**Uso típico:** Auditoria de conformidade.

### BEN_PRTT_RT_VAL
**Descrição:** Valores de taxa/contribuição por participante de benefícios.
**Módulo:** HCM - Benefits
**Uso típico:** Extração de valores de contribuição para folha de pagamento.

### BEN_PTNL_LER_FOR_PER
**Descrição:** Eventos de vida potenciais (pending) por pessoa — eventos ainda não processados.
**Módulo:** HCM - Benefits
**Uso típico:** Fila de processamento de eventos de vida.

---

## 3. Remuneração e Compensação (CMP)

Tabelas do módulo **Compensation** — salários, planos de compensação, orçamentos e workforce compensation.

### CMP_BUDGET_POOLS_B
**Descrição:** Pools de orçamento de compensação — define alocações orçamentárias para ciclos de mérito/bônus.
**Módulo:** HCM - Compensation
**Uso típico:** Gestão de orçamento de compensação.

### CMP_BUDGET_POOLS_TL
**Descrição:** Traduções dos pools de orçamento.
**Módulo:** HCM - Compensation
**Uso típico:** Suporte multilíngue.

### CMP_CALC_ALERTS_VL
**Descrição:** Alertas de cálculo de compensação — notificações de problemas em cálculos.
**Módulo:** HCM - Compensation
**Uso típico:** Monitoramento de processamento de compensação.

### CMP_COMPONENTS_B
**Descrição:** Componentes de compensação (ex.: salário base, bônus, allowances).
**Módulo:** HCM - Compensation
**Uso típico:** Definição de componentes salariais.

### CMP_COMPONENTS_TL
**Descrição:** Traduções dos componentes de compensação.
**Módulo:** HCM - Compensation
**Uso típico:** Suporte multilíngue.

### CMP_CWB_ALERTS
**Descrição:** Alertas do Compensation Workbench (CWB) — notificações durante ciclos de compensação.
**Módulo:** HCM - Compensation
**Uso típico:** Monitoramento de ciclos de mérito/bônus.

### CMP_CWB_HRCHY_CF_DN
**Descrição:** Hierarquia do Compensation Workbench — denormalized/cross-functional para navegação de aprovações.
**Módulo:** HCM - Compensation
**Uso típico:** Estrutura de aprovação de compensação.

### CMP_CWB_HRCHY_V
**Descrição:** View da hierarquia do Compensation Workbench.
**Módulo:** HCM - Compensation
**Uso típico:** Consulta de estrutura hierárquica de compensação.

### CMP_CWB_PERF_RATINGS
**Descrição:** Ratings de desempenho utilizados no ciclo de Compensation Workbench.
**Módulo:** HCM - Compensation
**Uso típico:** Vinculação desempenho↔compensação.

### CMP_CWB_PERSON_INFO
**Descrição:** Informações do colaborador no contexto do Compensation Workbench — dados consolidados para decisão de compensação.
**Módulo:** HCM - Compensation
**Uso típico:** Tela de decisão de mérito/bônus; extração para analytics de compensação.

### CMP_CWB_PERSON_INFO_V
**Descrição:** View consolidada de informações de pessoa para o Compensation Workbench.
**Módulo:** HCM - Compensation
**Uso típico:** Relatórios de compensação.

### CMP_CWB_PERSON_RATES
**Descrição:** Taxas e valores por pessoa no Compensation Workbench (salário atual, proposed, etc.).
**Módulo:** HCM - Compensation
**Uso típico:** Extração de propostas salariais em ciclos de mérito.

### CMP_CWB_PLAN_DEFINITIONS
**Descrição:** Definições de planos do Compensation Workbench — configuração dos ciclos.
**Módulo:** HCM - Compensation
**Uso típico:** Setup de planos de mérito/bônus.

### CMP_CWB_PROMOTIONS
**Descrição:** Promoções registradas no contexto do Compensation Workbench.
**Módulo:** HCM - Compensation
**Uso típico:** Rastreamento de promoções durante ciclos de compensação.

### CMP_CWB_XCHG
**Descrição:** Taxas de câmbio utilizadas no Compensation Workbench para conversão de moedas.
**Módulo:** HCM - Compensation
**Uso típico:** Compensação multicurrency.

### CMP_PERSON_BUDGETS_V
**Descrição:** View de orçamentos de compensação por pessoa.
**Módulo:** HCM - Compensation
**Uso típico:** Consulta de alocação orçamentária individual.

### CMP_PLANS_B
**Descrição:** Planos de compensação — define tipos de plano (mérito, bônus, equity, etc.).
**Módulo:** HCM - Compensation
**Uso típico:** Cadastro de planos de compensação.

### CMP_PLANS_TL
**Descrição:** Traduções dos planos de compensação.
**Módulo:** HCM - Compensation
**Uso típico:** Suporte multilíngue.

### CMP_PLAN_PERIODS
**Descrição:** Períodos dos planos de compensação — define vigência e ciclos.
**Módulo:** HCM - Compensation
**Uso típico:** Controle de ciclos de compensação.

### CMP_PRE_SALARY_V
**Descrição:** View de salário pré-processamento — salário vigente antes de alterações.
**Módulo:** HCM - Compensation
**Uso típico:** Comparação before/after em ciclos de mérito.

### CMP_PROFILE_VALUES
**Descrição:** Valores de perfil de compensação — taxas, ranges e valores por perfil.
**Módulo:** HCM - Compensation
**Uso típico:** Configuração de faixas salariais.

### CMP_SALARY
**Descrição:** **Tabela principal de salários** — armazena o salário atual e histórico de cada colaborador, incluindo valor, moeda, frequência e base salarial.
**Módulo:** HCM - Compensation
**Uso típico:** Extração de salários para analytics, folha de pagamento e relatórios de equidade salarial.

### CMP_SALARY_BASES
**Descrição:** Bases salariais — define tipos de base (anual, mensal, horária) e seus parâmetros.
**Módulo:** HCM - Compensation
**Uso típico:** Configuração de bases de cálculo salarial.

### CMP_SALARY_BASES_TL
**Descrição:** Traduções das bases salariais.
**Módulo:** HCM - Compensation
**Uso típico:** Suporte multilíngue.

### CMP_SALARY_COMPONENTS
**Descrição:** Componentes individuais que compõem o salário (ex.: base, adicional, gratificação).
**Módulo:** HCM - Compensation
**Uso típico:** Decomposição da remuneração total.

### CMP_SALARY_HISTORY_V
**Descrição:** View do histórico salarial — evolução salarial do colaborador ao longo do tempo.
**Módulo:** HCM - Compensation
**Uso típico:** Análise de progressão salarial, equity analytics.

### CMP_STOCK_DETAILS
**Descrição:** Detalhes de stock options/equity por colaborador.
**Módulo:** HCM - Compensation
**Uso típico:** Gestão de compensação em ações.

---

## 4. Fast Formula e Tabelas de Usuário (FF)

Tabelas do **Fast Formula** — motor de fórmulas configuráveis do Oracle para cálculos de payroll, benefícios e compensação.

### FF_FORMULAS_VL
**Descrição:** Fórmulas Fast Formula — lógicas de cálculo configuráveis usadas em folha, benefícios e ausências.
**Módulo:** HCM - Fast Formula
**Uso típico:** Referência de fórmulas utilizadas em processamentos.

### FF_USER_COLUMNS_VL
**Descrição:** Colunas de tabelas de usuário do Fast Formula.
**Módulo:** HCM - Fast Formula
**Uso típico:** Definição de estrutura de tabelas de lookup.

### FF_USER_COLUMN_INSTANCES_F
**Descrição:** Instâncias de colunas de tabelas de usuário — valores efetivos por combinação linha/coluna com data efetiva.
**Módulo:** HCM - Fast Formula
**Uso típico:** Valores de referência usados em cálculos de folha.

### FF_USER_ROWS_F
**Descrição:** Linhas das tabelas de usuário do Fast Formula.
**Módulo:** HCM - Fast Formula
**Uso típico:** Chaves de lookup em tabelas de referência.

### FF_USER_ROWS_TL
**Descrição:** Traduções das linhas de tabelas de usuário.
**Módulo:** HCM - Fast Formula
**Uso típico:** Suporte multilíngue.

### FF_USER_TABLES_VL
**Descrição:** Tabelas de usuário do Fast Formula — tabelas de referência configuráveis.
**Módulo:** HCM - Fast Formula
**Uso típico:** Cadastro de tabelas auxiliares para cálculos.

---

## 5. Fundação / Infraestrutura (FND)

Tabelas de infraestrutura compartilhada — lookups, documentos, calendários, moedas e territórios.

### FND_APPL_TAXONOMY_VL
**Descrição:** Taxonomia de aplicações Oracle Fusion — classificação hierárquica de módulos e aplicações.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de módulos e aplicações.

### FND_ATTACHED_DOCUMENTS
**Descrição:** Documentos anexados a registros do sistema (attachments).
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Rastreamento de anexos em processos de HR.

### FND_BPM_TASK_ASSIGNEE
**Descrição:** Atribuições de tarefas BPM (Business Process Management) — quem está designado para aprovar/executar.
**Módulo:** Foundation / Workflow
**Uso típico:** Rastreamento de aprovações e workflows.

### FND_BPM_TASK_ATTACHMENT
**Descrição:** Anexos de tarefas BPM.
**Módulo:** Foundation / Workflow
**Uso típico:** Documentação de processos de aprovação.

### FND_BPM_TASK_COMMENT
**Descrição:** Comentários em tarefas BPM.
**Módulo:** Foundation / Workflow
**Uso típico:** Auditoria de comunicações em workflows.

### FND_BPM_TASK_HISTORY_VL
**Descrição:** Histórico de tarefas BPM — rastreamento completo de ações em workflows.
**Módulo:** Foundation / Workflow
**Uso típico:** Auditoria de workflows de aprovação.

### FND_CAL_DAY
**Descrição:** Calendário de dias — tabela dimensional de datas.
**Módulo:** Foundation / Calendário
**Uso típico:** Dimensão de tempo para relatórios.

### FND_CAL_MONTH
**Descrição:** Calendário de meses.
**Módulo:** Foundation / Calendário
**Uso típico:** Dimensão de tempo mensal.

### FND_CAL_QUARTER
**Descrição:** Calendário de trimestres.
**Módulo:** Foundation / Calendário
**Uso típico:** Dimensão de tempo trimestral.

### FND_CAL_WEEK
**Descrição:** Calendário de semanas.
**Módulo:** Foundation / Calendário
**Uso típico:** Dimensão de tempo semanal.

### FND_CAL_YEAR
**Descrição:** Calendário de anos.
**Módulo:** Foundation / Calendário
**Uso típico:** Dimensão de tempo anual.

### FND_CONSOLE_ISSUE
**Descrição:** Issues registrados no console de administração.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Monitoramento de problemas do sistema.

### FND_CONSOLE_TRANSACTION_INFO
**Descrição:** Informações de transações do console.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Rastreamento de transações administrativas.

### FND_CURRENCIES_B
**Descrição:** Moedas — tabela base com códigos ISO de moedas.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de moedas para conversão.

### FND_CURRENCIES_TL
**Descrição:** Traduções dos nomes de moedas.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Suporte multilíngue.

### FND_CURRENCIES_VL
**Descrição:** View de moedas com tradução.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Consulta consolidada de moedas.

### FND_DF_CONTEXTS_VL
**Descrição:** Contextos de Descriptive Flexfields — define segmentos adicionais configuráveis.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de campos customizados (DFF).

### FND_DOCUMENTS
**Descrição:** Documentos do sistema — registro de documentos anexáveis.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Gestão de documentos.

### FND_DOCUMENTS_TL
**Descrição:** Traduções de documentos do sistema.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Suporte multilíngue.

### FND_DOCUMENTS_VL
**Descrição:** View de documentos com tradução.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Consulta consolidada.

### FND_FLEX_VALUES_VL
**Descrição:** Valores de flexfields — valores configuráveis de segmentos de flexfield.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de valores de campos configuráveis.

### FND_KF_STR_INSTANCES_VL
**Descrição:** Instâncias de estruturas de Key Flexfields.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Configuração de flexfields chave.

### FND_LOOKUPS
**Descrição:** **Tabela principal de lookups** — armazena tipos de lookup (listas de valores) do sistema.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência para decodificação de códigos em todo o sistema.

### FND_LOOKUP_VALUES_B
**Descrição:** Valores de lookups — cada código individual dentro de um tipo de lookup.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Decodificação de campos codificados.

### FND_LOOKUP_VALUES_TL
**Descrição:** Traduções dos valores de lookups.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Descrições traduzidas de valores codificados.

### FND_NODE_TL
**Descrição:** Traduções de nós (tree nodes).
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Suporte a árvores hierárquicas.

### FND_SETID_SETS_VL
**Descrição:** Conjuntos de referência (Set ID) — define escopos de compartilhamento de dados entre business units.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Gestão de compartilhamento de dados.

### FND_TERRITORIES_B
**Descrição:** Territórios/países — tabela base com códigos de países e territórios.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de países.

### FND_TERRITORIES_TL
**Descrição:** Traduções de nomes de territórios/países.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Nomes de países em múltiplos idiomas.

### FND_TREE_VERSION_TL
**Descrição:** Traduções de versões de árvores hierárquicas.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Suporte multilíngue para hierarquias.

### FND_TREE_VERSION_VL
**Descrição:** View de versões de árvores hierárquicas com tradução.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Consulta de versões de hierarquias.

### FND_TREE_VL
**Descrição:** View de árvores hierárquicas — estruturas de árvore usadas em organizações, posições, etc.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Referência de árvores hierárquicas.

### FND_VS_VALUE_SETS
**Descrição:** Value sets — conjuntos de valores usados em flexfields e validações.
**Módulo:** Foundation / Infraestrutura
**Uso típico:** Configuração de validações de campos.

---

## 6. Business Units e Funções (FUN)

Tabelas de configuração de Business Units e funções de negócio.

### FUN_ALL_BUSINESS_UNITS_V
**Descrição:** View de todas as Business Units — unidades de negócio configuradas no sistema.
**Módulo:** Foundation / Business Units
**Uso típico:** Referência de BUs para segmentação de dados.

### FUN_BUSINESS_FUNCTIONS_B
**Descrição:** Funções de negócio atribuídas a Business Units (ex.: HR, Payroll, Benefits).
**Módulo:** Foundation / Business Units
**Uso típico:** Configuração de funcionalidades por BU.

### FUN_BUSINESS_FUNCTIONS_TL
**Descrição:** Traduções das funções de negócio.
**Módulo:** Foundation / Business Units
**Uso típico:** Suporte multilíngue.

### FUN_BU_USAGES_V
**Descrição:** View de usos de Business Units — quais módulos estão habilitados por BU.
**Módulo:** Foundation / Business Units
**Uso típico:** Mapeamento de módulos por Business Unit.

---

## 7. HCM Lookups e Configuração (HCM)

### HCM_EXTENDED_LOOKUP_CODES_VL
**Descrição:** Códigos de lookup estendidos do HCM — lookups específicos com atributos adicionais.
**Módulo:** HCM - Configuração
**Uso típico:** Referência de valores codificados estendidos.

### HCM_LOOKUPS
**Descrição:** Lookups específicos do módulo HCM — complementa FND_LOOKUPS com tipos de lookup exclusivos de HR.
**Módulo:** HCM - Configuração
**Uso típico:** Decodificação de campos específicos de HR.

---

## 8. Modelagem de Força de Trabalho (HMO)

Tabelas de **Workforce Modeling** — planejamento e modelagem de headcount e estrutura organizacional.

### HMO_MODEL_PLANS_B
**Descrição:** Planos de modelagem de força de trabalho — cenários de planejamento organizacional.
**Módulo:** HCM - Workforce Modeling
**Uso típico:** Planejamento de headcount e orçamento de pessoal.

### HMO_MODEL_PLANS_TL
**Descrição:** Traduções dos planos de modelagem.
**Módulo:** HCM - Workforce Modeling
**Uso típico:** Suporte multilíngue.

### HMO_MODEL_PLAN_DETAILS
**Descrição:** Detalhes dos planos de modelagem — posições, headcount e custos projetados.
**Módulo:** HCM - Workforce Modeling
**Uso típico:** Análise detalhada de cenários de workforce planning.

---

## 9. Saúde e Segurança do Trabalho (HNS)

Tabelas do módulo **Health and Safety** — incidentes, investigações, pessoas envolvidas e ações corretivas.

### HNS_ACTIONS
**Descrição:** Ações corretivas/preventivas registradas após incidentes de saúde e segurança.
**Módulo:** HCM - Health and Safety
**Uso típico:** Rastreamento de ações corretivas.

### HNS_AIR_QUALITY_EVT_DETAIL
**Descrição:** Detalhes de eventos de qualidade do ar.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de incidentes ambientais.

### HNS_ERGONOMIC_EVT_DETAIL
**Descrição:** Detalhes de eventos ergonômicos.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de incidentes ergonômicos.

### HNS_FIRE_INC_EVENT_DETAIL
**Descrição:** Detalhes de incidentes de incêndio.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de ocorrências de incêndio.

### HNS_INCIDENTS_DETAIL
**Descrição:** Detalhes de incidentes de saúde e segurança — informações completas sobre cada ocorrência.
**Módulo:** HCM - Health and Safety
**Uso típico:** Relatórios detalhados de incidentes.

### HNS_INCIDENTS_SUMMARY
**Descrição:** Sumário de incidentes — visão consolidada para dashboards.
**Módulo:** HCM - Health and Safety
**Uso típico:** KPIs de segurança do trabalho.

### HNS_INCIDENT_AGENCIES_DTL
**Descrição:** Agências reguladoras envolvidas nos incidentes.
**Módulo:** HCM - Health and Safety
**Uso típico:** Compliance regulatório.

### HNS_INJURED_PERSONS
**Descrição:** Pessoas lesionadas em incidentes.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de vítimas de acidentes.

### HNS_INJURED_PERSONS_SUMMARY
**Descrição:** Sumário de pessoas lesionadas.
**Módulo:** HCM - Health and Safety
**Uso típico:** Estatísticas de acidentes.

### HNS_INJURED_PERSON_PARTS
**Descrição:** Partes do corpo afetadas em lesões.
**Módulo:** HCM - Health and Safety
**Uso típico:** Análise de tipos de lesão.

### HNS_INVESTIGATIONS_SUMMARY
**Descrição:** Sumário de investigações de incidentes.
**Módulo:** HCM - Health and Safety
**Uso típico:** Acompanhamento de investigações.

### HNS_INVEST_FINDINGS
**Descrição:** Achados das investigações de incidentes.
**Módulo:** HCM - Health and Safety
**Uso típico:** Documentação de causas-raiz.

### HNS_INVEST_RECOMMENDS
**Descrição:** Recomendações das investigações.
**Módulo:** HCM - Health and Safety
**Uso típico:** Planos de ação pós-investigação.

### HNS_ISSUE_EVT_DETAIL
**Descrição:** Detalhes de eventos de issue/problema.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de problemas gerais de segurança.

### HNS_NEAR_MISS_EVT_DETAIL
**Descrição:** Detalhes de quase-acidentes (near miss).
**Módulo:** HCM - Health and Safety
**Uso típico:** Prevenção proativa de acidentes.

### HNS_NOTES
**Descrição:** Notas e observações em registros de saúde e segurança.
**Módulo:** HCM - Health and Safety
**Uso típico:** Documentação adicional.

### HNS_NOTICE_VIO_EVT_DETAIL
**Descrição:** Detalhes de eventos de notificação/violação regulatória.
**Módulo:** HCM - Health and Safety
**Uso típico:** Compliance regulatório.

### HNS_PERSONS
**Descrição:** Pessoas envolvidas em eventos de saúde e segurança (testemunhas, envolvidos, etc.).
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de envolvidos em incidentes.

### HNS_PROP_DAMAGE_EVT_DETAIL
**Descrição:** Detalhes de eventos de dano a propriedade.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de danos materiais.

### HNS_SPILL_REL_EVT_DETAIL
**Descrição:** Detalhes de eventos de derramamento/vazamento.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de incidentes ambientais.

### HNS_SUGG_IMPROV_EVT_DETAIL
**Descrição:** Detalhes de sugestões de melhoria em segurança.
**Módulo:** HCM - Health and Safety
**Uso típico:** Programa de sugestões de segurança.

### HNS_UNSAFE_ACT_EVT_DETAIL
**Descrição:** Detalhes de eventos de atos inseguros.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro comportamental de segurança.

### HNS_UNSAFE_COND_EVT_DETAIL
**Descrição:** Detalhes de eventos de condições inseguras.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de condições de risco.

### HNS_VEH_INC_EVENT_DETAIL
**Descrição:** Detalhes de incidentes veiculares.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de acidentes com veículos.

### HNS_VEH_INC_EVENT_PASSENGERS
**Descrição:** Passageiros envolvidos em incidentes veiculares.
**Módulo:** HCM - Health and Safety
**Uso típico:** Registro de ocupantes envolvidos.

### HNS_VEH_INC_EVENT_SUMMARY
**Descrição:** Sumário de incidentes veiculares.
**Módulo:** HCM - Health and Safety
**Uso típico:** Estatísticas de acidentes veiculares.

---

## 10. Desempenho e Avaliações (HRA)

Tabelas do módulo **Performance Management** — avaliações de desempenho, check-ins, feedback e configuração de templates.

### HRA_CHECK_IN_MEETINGS
**Descrição:** Reuniões de check-in entre gestor e colaborador — conversas contínuas de desempenho.
**Módulo:** HCM - Performance Management
**Uso típico:** Rastreamento de check-ins periódicos.

### HRA_CHECK_IN_TMPLS_B
**Descrição:** Templates de check-in — modelos pré-definidos para reuniões.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de templates de check-in.

### HRA_CHECK_IN_TMPLS_TL
**Descrição:** Traduções dos templates de check-in.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_CHECK_IN_TMPLS_VL
**Descrição:** View de templates de check-in com tradução.
**Módulo:** HCM - Performance Management
**Uso típico:** Consulta consolidada.

### HRA_DOC_TYPES_B
**Descrição:** Tipos de documentos de avaliação de desempenho.
**Módulo:** HCM - Performance Management
**Uso típico:** Classificação de documentos de performance.

### HRA_DOC_TYPES_TL
**Descrição:** Traduções dos tipos de documentos.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_EVALUATIONS
**Descrição:** **Tabela principal de avaliações de desempenho** — registra cada avaliação com status, período, avaliado e resultado.
**Módulo:** HCM - Performance Management
**Uso típico:** Extração de avaliações de desempenho; relatórios de performance review.

### HRA_EVAL_ITEMS
**Descrição:** Itens individuais dentro de uma avaliação (competências, metas, comportamentos avaliados).
**Módulo:** HCM - Performance Management
**Uso típico:** Detalhamento de itens avaliados.

### HRA_EVAL_PARTICIPANTS
**Descrição:** Participantes de uma avaliação (avaliador, avaliado, pares, etc.).
**Módulo:** HCM - Performance Management
**Uso típico:** Rastreamento de participantes em avaliações 360°.

### HRA_EVAL_RATINGS
**Descrição:** Ratings/notas atribuídas nas avaliações de desempenho.
**Módulo:** HCM - Performance Management
**Uso típico:** Extração de notas de desempenho.

### HRA_EVAL_ROLES
**Descrição:** Papéis dos participantes na avaliação (gestor, par, subordinado, auto-avaliação).
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de papéis em avaliações.

### HRA_EVAL_ROLE_ACTIONS
**Descrição:** Ações permitidas por papel na avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Permissões de workflow de avaliação.

### HRA_EVAL_SECTIONS
**Descrição:** Seções das avaliações de desempenho (ex.: metas, competências, desenvolvimento).
**Módulo:** HCM - Performance Management
**Uso típico:** Estrutura do formulário de avaliação.

### HRA_EVAL_STEPS
**Descrição:** Etapas do processo de avaliação (auto-avaliação, avaliação do gestor, calibração, etc.).
**Módulo:** HCM - Performance Management
**Uso típico:** Workflow de avaliação.

### HRA_FEEDBACK_REQUEST
**Descrição:** Solicitações de feedback — pedidos de feedback sobre colaboradores.
**Módulo:** HCM - Performance Management
**Uso típico:** Processo de coleta de feedback.

### HRA_FEEDBACK_REQUEST_OBJECTS
**Descrição:** Objetos vinculados a solicitações de feedback.
**Módulo:** HCM - Performance Management
**Uso típico:** Contexto das solicitações de feedback.

### HRA_PF_TASK_ROLES_B
**Descrição:** Papéis em tarefas de performance.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de papéis em tarefas de desempenho.

### HRA_PF_TASK_ROLES_TL
**Descrição:** Traduções dos papéis em tarefas de performance.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_ROLE_DEFNS_B
**Descrição:** Definições de papéis de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de papéis.

### HRA_ROLE_DEFNS_TL
**Descrição:** Traduções das definições de papéis.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_SECTION_DEFNS_B
**Descrição:** Definições de seções do template de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de seções.

### HRA_SECTION_DEFNS_TL
**Descrição:** Traduções das definições de seções.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_TMPL_DEFNS_B
**Descrição:** Definições de templates de avaliação de desempenho — modelos de formulário.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de templates de performance review.

### HRA_TMPL_DEFNS_TL
**Descrição:** Traduções dos templates de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_TMPL_PERIODS_B
**Descrição:** Períodos de avaliação definidos nos templates.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de ciclos de avaliação.

### HRA_TMPL_PERIODS_TL
**Descrição:** Traduções dos períodos de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Suporte multilíngue.

### HRA_TMPL_ROLES
**Descrição:** Papéis atribuídos nos templates de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Configuração de participantes por template.

### HRA_TMPL_SECTIONS
**Descrição:** Seções definidas nos templates de avaliação.
**Módulo:** HCM - Performance Management
**Uso típico:** Estruturação do formulário de avaliação por template.

---

## 11. Transações e Console HR (HRC)

Tabelas de transações de HR e console de monitoramento.

### HRC_ARM_PROCESS_VL
**Descrição:** Processos de ARM (Action Reason Manager) — processos de ações de HR.
**Módulo:** HCM - Core HR / Transactions
**Uso típico:** Referência de processos transacionais.

### HRC_CONSOLE_FAULT_DETAILS_VL
**Descrição:** Detalhes de falhas no console de transações HR.
**Módulo:** HCM - Core HR / Console
**Uso típico:** Diagnóstico de erros em transações.

### HRC_CONSOLE_ISSUE_ASSIGNMENT
**Descrição:** Atribuição de issues no console HR a responsáveis.
**Módulo:** HCM - Core HR / Console
**Uso típico:** Gestão de incidentes de transações.

### HRC_CONSOLE_ISSUE_COMMENTS
**Descrição:** Comentários em issues do console HR.
**Módulo:** HCM - Core HR / Console
**Uso típico:** Comunicação sobre problemas transacionais.

### HRC_TXN_CONSOLE_ENTRY
**Descrição:** Entradas do console de transações — registro de transações HR pendentes/com erro.
**Módulo:** HCM - Core HR / Console
**Uso típico:** Monitoramento de transações HR.

### HRC_TXN_DATA
**Descrição:** Dados das transações HR — payload das alterações.
**Módulo:** HCM - Core HR / Transactions
**Uso típico:** Auditoria de dados de transações.

### HRC_TXN_FND_BPM_TASK_VL
**Descrição:** View de tarefas BPM vinculadas a transações HR.
**Módulo:** HCM - Core HR / Transactions
**Uso típico:** Rastreamento de workflows de transações.

### HRC_TXN_HEADER
**Descrição:** Cabeçalho de transações HR — informação resumida de cada transação (tipo, status, datas).
**Módulo:** HCM - Core HR / Transactions
**Uso típico:** Consulta de transações HR pendentes e processadas.

---

## 12. Desenvolvimento e Intenções de Carreira (HRD)

### HRD_GOAL_INTENTS
**Descrição:** Intenções de metas — registra intenções de desenvolvimento vinculadas a metas.
**Módulo:** HCM - Career Development
**Uso típico:** Planejamento de carreira.

### HRD_PERSONAL_INTENTS
**Descrição:** Intenções pessoais de carreira — registra aspirações e objetivos de carreira do colaborador.
**Módulo:** HCM - Career Development
**Uso típico:** Análise de intenções de carreira para talent planning.

---

## 13. Metas e Objetivos (HRG)

Tabelas do módulo **Goal Management** — definição, acompanhamento e alinhamento de metas.

### HRG_GOALS
**Descrição:** **Tabela principal de metas** — registra metas individuais e organizacionais com descrição, status e prazo.
**Módulo:** HCM - Goal Management
**Uso típico:** Extração de metas para relatórios de desempenho e OKRs.

### HRG_GOAL_ACTIONS
**Descrição:** Ações registradas em metas (atualização, conclusão, cancelamento).
**Módulo:** HCM - Goal Management
**Uso típico:** Histórico de ações em metas.

### HRG_GOAL_ALIGNMENTS
**Descrição:** Alinhamentos entre metas — cascateamento de metas organizacionais para individuais.
**Módulo:** HCM - Goal Management
**Uso típico:** Visualização de cascateamento de metas (strategy alignment).

### HRG_GOAL_MEASUREMENTS
**Descrição:** Medições/métricas de progresso das metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Acompanhamento quantitativo de metas.

### HRG_GOAL_PLANS_B
**Descrição:** Planos de metas — define ciclos/períodos de metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Configuração de planos de metas.

### HRG_GOAL_PLANS_TL
**Descrição:** Traduções dos planos de metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Suporte multilíngue.

### HRG_GOAL_PLAN_GOALS
**Descrição:** Metas vinculadas a planos de metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Associação meta↔plano.

### HRG_GOAL_PLAN_SETS_B
**Descrição:** Conjuntos de planos de metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Agrupamento de planos de metas.

### HRG_GOAL_PLAN_SETS_TL
**Descrição:** Traduções dos conjuntos de planos.
**Módulo:** HCM - Goal Management
**Uso típico:** Suporte multilíngue.

### HRG_GOAL_PLAN_SET_PLANS
**Descrição:** Associação entre conjuntos e planos de metas.
**Módulo:** HCM - Goal Management
**Uso típico:** Estruturação de conjuntos de planos.

### HRG_GOAL_PLN_ASSIGNMENTS
**Descrição:** Atribuições de planos de metas a colaboradores/populações.
**Módulo:** HCM - Goal Management
**Uso típico:** Gestão de quem participa de quais planos.

### HRG_GOAL_TARGET_OUTCOMES
**Descrição:** Resultados alvo das metas — outcomes esperados.
**Módulo:** HCM - Goal Management
**Uso típico:** Definição de resultados esperados.

---

## 14. Planos de Sucessão (HRM)

Tabelas do módulo **Succession Management** — planos de sucessão e candidatos.

### HRM_PLANS_V
**Descrição:** View de planos de sucessão — define posições/cargos críticos com planos de sucessão.
**Módulo:** HCM - Succession Management
**Uso típico:** Relatórios de sucessão organizacional.

### HRM_PLAN_CANDIDATES
**Descrição:** Candidatos a posições em planos de sucessão — colaboradores identificados como possíveis sucessores.
**Módulo:** HCM - Succession Management
**Uso típico:** Extração de pipeline de sucessão.

### HRM_PLAN_CANDIDATES_V
**Descrição:** View de candidatos de planos de sucessão com dados enriquecidos.
**Módulo:** HCM - Succession Management
**Uso típico:** Relatórios de readiness de sucessão.

### HRM_PLAN_OWNERS
**Descrição:** Proprietários/responsáveis pelos planos de sucessão.
**Módulo:** HCM - Succession Management
**Uso típico:** Gestão de responsabilidade de planos.

---

## 15. Questionários (HRQ)

Tabelas do módulo **Questionnaires** — questionários configuráveis para avaliações, pesquisas e processos de HR.

### HRQ_ALL_QSTN_RESPONSES_V
**Descrição:** View consolidada de todas as respostas a questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Extração de respostas para análise.

### HRQ_CATEGORIES_B
**Descrição:** Categorias de questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Classificação de questionários.

### HRQ_CATEGORIES_TL
**Descrição:** Traduções das categorias.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_EVAL_PTCPNT_QUESTIONS_V
**Descrição:** View de perguntas por participante de avaliação.
**Módulo:** HCM - Questionnaires
**Uso típico:** Perguntas no contexto de avaliações de desempenho.

### HRQ_QSTNR_ANSWERS
**Descrição:** Respostas registradas em questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Coleta de respostas.

### HRQ_QSTNR_PARTICIPANTS
**Descrição:** Participantes/respondentes de questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Rastreamento de quem respondeu.

### HRQ_QSTNR_QUESTIONS
**Descrição:** Perguntas atribuídas a questionários específicos.
**Módulo:** HCM - Questionnaires
**Uso típico:** Estrutura de questionários.

### HRQ_QSTNR_RESPONSES
**Descrição:** Respostas a questionários por participante.
**Módulo:** HCM - Questionnaires
**Uso típico:** Dados de respostas individuais.

### HRQ_QSTNR_SECTIONS_B
**Descrição:** Seções de questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Organização de perguntas em seções.

### HRQ_QSTNR_SECTIONS_TL
**Descrição:** Traduções das seções.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_QSTN_ANSWERS_B
**Descrição:** Opções de resposta para perguntas (gabarito).
**Módulo:** HCM - Questionnaires
**Uso típico:** Definição de opções de resposta.

### HRQ_QSTN_ANSWERS_TL
**Descrição:** Traduções das opções de resposta.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_QSTN_RESPONSES
**Descrição:** Respostas individuais a perguntas.
**Módulo:** HCM - Questionnaires
**Uso típico:** Análise de respostas por pergunta.

### HRQ_QUESTIONNAIRES_B
**Descrição:** Questionários — definição de questionários configuráveis.
**Módulo:** HCM - Questionnaires
**Uso típico:** Cadastro de questionários.

### HRQ_QUESTIONNAIRES_TL
**Descrição:** Traduções dos questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_QUESTIONS_B
**Descrição:** Perguntas — banco de perguntas reutilizáveis.
**Módulo:** HCM - Questionnaires
**Uso típico:** Cadastro de perguntas.

### HRQ_QUESTIONS_TL
**Descrição:** Traduções das perguntas.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_RESPONSE_TYPES_B
**Descrição:** Tipos de resposta (texto livre, múltipla escolha, escala, etc.).
**Módulo:** HCM - Questionnaires
**Uso típico:** Configuração de tipos de resposta.

### HRQ_RESPONSE_TYPES_TL
**Descrição:** Traduções dos tipos de resposta.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

### HRQ_SUBSCRIBERS_B
**Descrição:** Assinantes/consumidores de questionários — módulos que utilizam os questionários.
**Módulo:** HCM - Questionnaires
**Uso típico:** Integração de questionários com outros módulos.

### HRQ_SUBSCRIBERS_TL
**Descrição:** Traduções dos assinantes.
**Módulo:** HCM - Questionnaires
**Uso típico:** Suporte multilíngue.

---

## 16. Talent Review / Reuniões de Calibração (HRR)

Tabelas do módulo **Talent Review** — reuniões de calibração, dashboards de talento e análise de potencial.

### HRR_DASHBOARDS
**Descrição:** Dashboards de Talent Review configurados para reuniões de calibração.
**Módulo:** HCM - Talent Review
**Uso típico:** Configuração de dashboards para talent review.

### HRR_DASHBOARD_TMPLS_B
**Descrição:** Templates de dashboards de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Configuração de modelos de dashboard.

### HRR_DASHBOARD_TMPLS_TL
**Descrição:** Traduções dos templates de dashboard.
**Módulo:** HCM - Talent Review
**Uso típico:** Suporte multilíngue.

### HRR_MEETINGS
**Descrição:** Reuniões de Talent Review — sessões de calibração de desempenho e potencial.
**Módulo:** HCM - Talent Review
**Uso típico:** Rastreamento de reuniões de calibração.

### HRR_MEETING_FACILITATORS
**Descrição:** Facilitadores das reuniões de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Gestão de participantes.

### HRR_MEETING_PARTICIPANTS
**Descrição:** Participantes (gestores) das reuniões de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Controle de presença.

### HRR_MEETING_REVIEWEES
**Descrição:** Colaboradores sendo avaliados nas reuniões de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Lista de avaliados por reunião.

### HRR_MEETING_REVW_CONTENT
**Descrição:** Conteúdo/dados revisados nas reuniões de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Documentação de decisões de calibração.

### HRR_TMPL_ANALYTIC_TYPES_B
**Descrição:** Tipos analíticos nos templates de Talent Review (ex.: 9-box, performance vs. potential).
**Módulo:** HCM - Talent Review
**Uso típico:** Configuração de analytics de talento.

### HRR_TMPL_ANALYTIC_TYPES_TL
**Descrição:** Traduções dos tipos analíticos.
**Módulo:** HCM - Talent Review
**Uso típico:** Suporte multilíngue.

### HRR_TMPL_ANLYT_BOX_LBLS_B
**Descrição:** Rótulos dos boxes em matrizes de talento (ex.: rótulos do 9-box).
**Módulo:** HCM - Talent Review
**Uso típico:** Configuração de labels do 9-box.

### HRR_TMPL_ANLYT_BOX_LBLS_TL
**Descrição:** Traduções dos rótulos dos boxes.
**Módulo:** HCM - Talent Review
**Uso típico:** Suporte multilíngue.

### HRR_TMPL_ANLYT_BOX_RATINGS
**Descrição:** Ratings atribuídos a cada box da matriz de talento.
**Módulo:** HCM - Talent Review
**Uso típico:** Mapeamento de ratings para posição no 9-box.

### HRR_TMPL_METRIC_CONFIG
**Descrição:** Configuração de métricas nos templates de Talent Review.
**Módulo:** HCM - Talent Review
**Uso típico:** Configuração de indicadores de talento.

---

## 17. Perfis de Talento e Competências (HRT)

Tabelas do módulo **Talent Profile** — competências, habilidades, certificações, ratings e perfis de talento.

### HRT_BI_ADV_READINESS_ITEMS_V
**Descrição:** View BI de itens de prontidão para avanço (readiness para promoção).
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de readiness para promoção.

### HRT_BI_CAREER_POTN_ITEMS_V
**Descrição:** View BI de itens de potencial de carreira.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de potencial.

### HRT_BI_CAREER_PRF_ITEMS_V
**Descrição:** View BI de itens de preferência de carreira.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de preferências de carreira.

### HRT_BI_CERTIF_ITEMS_V
**Descrição:** View BI de certificações dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Relatórios de certificações.

### HRT_BI_COMPETENCY_ITEMS_V
**Descrição:** View BI de competências — itens de competência avaliados por colaborador.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de gap de competências.

### HRT_BI_CRITICALITY_ITEMS_V
**Descrição:** View BI de criticidade (impacto da saída do colaborador).
**Módulo:** HCM - Talent Profile
**Uso típico:** Identificação de colaboradores críticos.

### HRT_BI_EDUCATION_ITEMS_V
**Descrição:** View BI de formação educacional dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Relatórios de escolaridade.

### HRT_BI_HONOR_ITEMS_V
**Descrição:** View BI de honrarias e prêmios dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Reconhecimentos e prêmios.

### HRT_BI_LANGUAGE_ITEMS_V
**Descrição:** View BI de idiomas dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de proficiência linguística.

### HRT_BI_MEMBERSHIP_ITEMS_V
**Descrição:** View BI de memberships e associações profissionais.
**Módulo:** HCM - Talent Profile
**Uso típico:** Associações profissionais.

### HRT_BI_PERF_RATING_ITEMS_V
**Descrição:** View BI de ratings de desempenho.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de performance ratings.

### HRT_BI_PREV_EMPLOYMENT_ITEMS_V
**Descrição:** View BI de empregos anteriores dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Histórico profissional.

### HRT_BI_RISK_ITEMS_V
**Descrição:** View BI de risco de perda (loss risk / flight risk).
**Módulo:** HCM - Talent Profile
**Uso típico:** Identificação de risco de turnover.

### HRT_BI_SPECIAL_PRJ_ITEMS_V
**Descrição:** View BI de projetos especiais dos colaboradores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Experiências de projetos.

### HRT_BI_TALENT_RATING_ITEMS_V
**Descrição:** View BI de ratings de talento.
**Módulo:** HCM - Talent Profile
**Uso típico:** Classificação de talento.

### HRT_BI_WORK_PREFERENCE_ITEMS_V
**Descrição:** View BI de preferências de trabalho (localização, viagem, realocação).
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de mobilidade e preferências.

### HRT_CONTENT_ITEMS_B
**Descrição:** Itens de conteúdo de perfil de talento — competências, habilidades, certificações cadastradas.
**Módulo:** HCM - Talent Profile
**Uso típico:** Catálogo de competências e habilidades.

### HRT_CONTENT_ITEMS_TL
**Descrição:** Traduções dos itens de conteúdo.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_CONTENT_SOURCE_RLATS
**Descrição:** Relações de origem de conteúdo — de onde cada item de competência foi importado.
**Módulo:** HCM - Talent Profile
**Uso típico:** Rastreamento de origem de dados.

### HRT_CONTENT_TYPES_B
**Descrição:** Tipos de conteúdo de perfil (competência, certificação, educação, idioma, etc.).
**Módulo:** HCM - Talent Profile
**Uso típico:** Classificação de tipos de conteúdo de talento.

### HRT_CONTENT_TYPES_TL
**Descrição:** Traduções dos tipos de conteúdo.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_ESTABLISHMENTS_B
**Descrição:** Estabelecimentos — unidades físicas/legais para fins regulatórios de HR.
**Módulo:** HCM - Talent Profile / Core HR
**Uso típico:** Referência de estabelecimentos.

### HRT_ESTABLISHMENTS_TL
**Descrição:** Traduções dos estabelecimentos.
**Módulo:** HCM - Talent Profile / Core HR
**Uso típico:** Suporte multilíngue.

### HRT_NOTES
**Descrição:** Notas em perfis de talento.
**Módulo:** HCM - Talent Profile
**Uso típico:** Comentários qualitativos sobre talentos.

### HRT_OBJ_RATING_DIST_B
**Descrição:** Distribuição de ratings por objeto — distribuição estatística de ratings.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de distribuição de avaliações.

### HRT_POOLS_VL
**Descrição:** Pools de talento — grupos de colaboradores identificados para programas especiais.
**Módulo:** HCM - Talent Profile
**Uso típico:** Gestão de pools de talento (high potential, sucessão, etc.).

### HRT_POOL_ASSOCIATIONS
**Descrição:** Associações de pools de talento com entidades (posições, cargos, etc.).
**Módulo:** HCM - Talent Profile
**Uso típico:** Vinculação de pools a posições.

### HRT_POOL_MEMBERS
**Descrição:** Membros de pools de talento — colaboradores em cada pool.
**Módulo:** HCM - Talent Profile
**Uso típico:** Extração de membros de pools de talento.

### HRT_POOL_OWNERS
**Descrição:** Proprietários/responsáveis pelos pools de talento.
**Módulo:** HCM - Talent Profile
**Uso típico:** Gestão de responsabilidade.

### HRT_PROFILES_B
**Descrição:** **Perfis de talento** — tabela principal que define perfis de pessoa, cargo ou posição com suas competências esperadas.
**Módulo:** HCM - Talent Profile
**Uso típico:** Definição de perfis de competência; análise de gaps.

### HRT_PROFILES_TL
**Descrição:** Traduções dos perfis.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_PROFILE_ITEMS
**Descrição:** Itens de perfil de talento — competências, habilidades, certificações atribuídas a um perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Detalhamento de perfis de competência.

### HRT_PROFILE_RELATIONS
**Descrição:** Relações entre perfis (ex.: perfil de pessoa vinculado a perfil de cargo).
**Módulo:** HCM - Talent Profile
**Uso típico:** Mapeamento pessoa↔cargo para gap analysis.

### HRT_PROFILE_TP_SC_PRP_B
**Descrição:** Propriedades de seções de tipos de perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Configuração avançada de perfis.

### HRT_PROFILE_TP_SC_PRP_TL
**Descrição:** Traduções das propriedades.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_PROFILE_TYPES_B
**Descrição:** Tipos de perfil de talento (pessoa, cargo, posição, modelo).
**Módulo:** HCM - Talent Profile
**Uso típico:** Classificação de perfis.

### HRT_PROFILE_TYPES_TL
**Descrição:** Traduções dos tipos de perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_PROFILE_TYPE_RELS
**Descrição:** Relações entre tipos de perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Configuração de relações entre tipos.

### HRT_PROFILE_TYP_SECTIONS_TL
**Descrição:** Traduções das seções de tipos de perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_PROFILE_TYP_SECTIONS_VL
**Descrição:** View de seções de tipos de perfil com tradução.
**Módulo:** HCM - Talent Profile
**Uso típico:** Consulta consolidada.

### HRT_QUALIFIERS_B
**Descrição:** Qualificadores de itens de perfil (ex.: nível de proficiência, certificação ativa/expirada).
**Módulo:** HCM - Talent Profile
**Uso típico:** Qualificação de competências.

### HRT_QUALIFIERS_TL
**Descrição:** Traduções dos qualificadores.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_RATING_CATEGORIES_B
**Descrição:** Categorias de rating (ex.: desempenho, potencial, competência).
**Módulo:** HCM - Talent Profile
**Uso típico:** Classificação de escalas de avaliação.

### HRT_RATING_CATEGORIES_TL
**Descrição:** Traduções das categorias de rating.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_RATING_DISTRIBUTIONS
**Descrição:** Distribuição de ratings — análise estatística de como os ratings estão distribuídos.
**Módulo:** HCM - Talent Profile
**Uso típico:** Análise de calibração e distribuição forçada.

### HRT_RATING_LEVELS_B
**Descrição:** Níveis de rating (ex.: 1-5, Exceeds/Meets/Below).
**Módulo:** HCM - Talent Profile
**Uso típico:** Definição de escalas de avaliação.

### HRT_RATING_LEVELS_TL
**Descrição:** Traduções dos níveis de rating.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_RATING_MODELS_B
**Descrição:** Modelos de rating — define escalas de avaliação reutilizáveis.
**Módulo:** HCM - Talent Profile
**Uso típico:** Cadastro de modelos de escala (ex.: escala 1-5).

### HRT_RATING_MODELS_TL
**Descrição:** Traduções dos modelos de rating.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_RELATION_CONFIG_B
**Descrição:** Configuração de relações de perfil.
**Módulo:** HCM - Talent Profile
**Uso típico:** Setup de relações entre perfis.

### HRT_RELATION_CONFIG_TL
**Descrição:** Traduções da configuração de relações.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_REVIEW_PERIODS_B
**Descrição:** Períodos de revisão de perfis de talento.
**Módulo:** HCM - Talent Profile
**Uso típico:** Configuração de ciclos de revisão.

### HRT_REVIEW_PERIODS_TL
**Descrição:** Traduções dos períodos de revisão.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_SOURCES_B
**Descrição:** Fontes de dados de perfis de talento (manual, importação, integração).
**Módulo:** HCM - Talent Profile
**Uso típico:** Rastreamento de origem de dados.

### HRT_SOURCES_TL
**Descrição:** Traduções das fontes.
**Módulo:** HCM - Talent Profile
**Uso típico:** Suporte multilíngue.

### HRT_TASK_OBJ_RELATIONS
**Descrição:** Relações entre tarefas e objetos de perfil de talento.
**Módulo:** HCM - Talent Profile
**Uso típico:** Vinculação de tarefas a perfis.

---

## 18. Integração de Dados de Pessoa (HRY)

### HRY_PI_INBD_RECORDS
**Descrição:** Registros inbound de informações pessoais — dados recebidos de integrações externas.
**Módulo:** HCM - Integration
**Uso típico:** Monitoramento de integrações de dados de pessoa.

---

## 19. Organizações e Posições (HR)

Tabelas de **Core HR** — organizações, posições, classificações e documentos organizacionais.

### HR_ALL_ORGANIZATION_UNITS_F
**Descrição:** **Tabela principal de organizações** — todas as unidades organizacionais (departamentos, divisões, unidades de negócio) com data efetiva. Contém nome, tipo, classificação e hierarquia.
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Extração da estrutura organizacional; base para hierarquias; dimensão organizacional em relatórios.

### HR_ALL_POSITIONS_F
**Descrição:** **Tabela principal de posições** — todas as posições definidas na organização, com cargo, departamento, localização, headcount aprovado e data efetiva.
**Módulo:** HCM - Core HR / Positions
**Uso típico:** Extração de posições para relatórios de headcount, vacâncias e estrutura organizacional.

### HR_ALL_POSITIONS_F_TL
**Descrição:** Traduções dos nomes e descrições de posições.
**Módulo:** HCM - Core HR / Positions
**Uso típico:** Nomes de posições em múltiplos idiomas.

### HR_DOCUMENTS_OF_RECORD
**Descrição:** Documentos de registro (Document of Record) — documentos obrigatórios/opcionais armazenados por colaborador (ex.: contratos, certificados).
**Módulo:** HCM - Core HR / Documents
**Uso típico:** Gestão de documentos pessoais e compliance.

### HR_DOCUMENT_TYPES_B
**Descrição:** Tipos de documentos de registro (ex.: contrato de trabalho, certidão, diploma).
**Módulo:** HCM - Core HR / Documents
**Uso típico:** Configuração de tipos de documentos.

### HR_DOCUMENT_TYPES_TL
**Descrição:** Traduções dos tipos de documentos.
**Módulo:** HCM - Core HR / Documents
**Uso típico:** Suporte multilíngue.

### HR_DOR_REPORTING_LIST_V
**Descrição:** View de lista de reportes de Documents of Record.
**Módulo:** HCM - Core HR / Documents
**Uso típico:** Relatórios de compliance de documentos.

### HR_ORGANIZATION_INFORMATION_F
**Descrição:** Informações adicionais de organizações — atributos extras configuráveis por tipo de organização (ex.: CNPJ, código, endereço).
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Extração de atributos customizados de organizações.

### HR_ORGANIZATION_UNITS_F_TL
**Descrição:** Traduções dos nomes de unidades organizacionais.
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Nomes de organizações em múltiplos idiomas.

### HR_ORG_CLASSIFICATIONS
**Descrição:** Classificações de organizações — tipos como departamento, legal entity, business unit, etc.
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Tipificação de organizações.

### HR_ORG_CLASSIFICATIONS_TL
**Descrição:** Traduções das classificações de organizações.
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Suporte multilíngue.

### HR_ORG_UNIT_CLASSIFICATIONS_F
**Descrição:** Classificações atribuídas a unidades organizacionais com data efetiva.
**Módulo:** HCM - Core HR / Organizations
**Uso típico:** Histórico de classificações por organização.

---

## 20. Demanda de Mão de Obra e Escalas (HTS)

Tabelas de **Scheduling / Labor Demand** — demanda de mão de obra e definição de escalas.

### HTS_LABOR_DEMAND_PRFL_DEFS
**Descrição:** Definições de perfis de demanda de mão de obra.
**Módulo:** HCM - Scheduling
**Uso típico:** Configuração de perfis de demanda.

### HTS_LABOR_DEMAND_PRFL_DEFSETS
**Descrição:** Conjuntos de definições de perfis de demanda.
**Módulo:** HCM - Scheduling
**Uso típico:** Agrupamento de perfis de demanda.

### HTS_LABOR_DEMAND_PRFL_VALS
**Descrição:** Valores dos perfis de demanda de mão de obra.
**Módulo:** HCM - Scheduling
**Uso típico:** Parâmetros de demanda.

### HTS_LABOR_DEMAND_VIEW
**Descrição:** View de demanda de mão de obra — visão consolidada de necessidades de pessoal.
**Módulo:** HCM - Scheduling
**Uso típico:** Planejamento de escalas baseado em demanda.

### HTS_SCHEDULES_ATRBS_VIEW
**Descrição:** View de atributos de escalas.
**Módulo:** HCM - Scheduling
**Uso típico:** Consulta de propriedades de escalas.

### HTS_SCHEDULES_DAY_SHIFT_VIEW
**Descrição:** View de escalas por dia e turno.
**Módulo:** HCM - Scheduling
**Uso típico:** Visualização de escalas diárias.

---

## 21. Gestão de Tempo e Ponto (HWM)

Tabelas do módulo **Time and Labor / Workforce Management** — gestão de tempo, cartões de ponto, regras e categorias de tempo.

### HWM_ALLOCATIONS_HDR_F
**Descrição:** Cabeçalho de alocações de tempo — distribuição de horas por projeto/atividade.
**Módulo:** HCM - Time and Labor
**Uso típico:** Alocação de tempo para custos.

### HWM_ALLOCATIONS_HDR_TL
**Descrição:** Traduções dos cabeçalhos de alocação.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_ALLOCATIONS_HDR_VL
**Descrição:** View de cabeçalhos de alocação com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_ALLOCATION_LINES_F
**Descrição:** Linhas de alocação de tempo — detalhes de distribuição.
**Módulo:** HCM - Time and Labor
**Uso típico:** Detalhamento de alocações.

### HWM_ALLOCATION_LN_ATRBS_F
**Descrição:** Atributos das linhas de alocação.
**Módulo:** HCM - Time and Labor
**Uso típico:** Atributos adicionais de alocações.

### HWM_ALLOCATION_RULES_F
**Descrição:** Regras de alocação de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de regras automáticas.

### HWM_DATA_SOURCE_USAGES_V
**Descrição:** View de usos de fontes de dados de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de fontes de dados.

### HWM_FND_MESSAGES_VL
**Descrição:** Mensagens do sistema de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Mensagens de erro/informação.

### HWM_GRPS_B
**Descrição:** Grupos de workforce management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Agrupamento de colaboradores para gestão de tempo.

### HWM_GRPS_TL
**Descrição:** Traduções dos grupos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_GRPS_VL
**Descrição:** View de grupos com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_GRP_CRITERIA
**Descrição:** Critérios de pertencimento a grupos de workforce management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de regras de inclusão em grupos.

### HWM_GRP_INCL_MEMBERS_VIEW
**Descrição:** View de membros incluídos em grupos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de membros de grupos.

### HWM_GRP_INCL_OBJECTS_V
**Descrição:** View de objetos incluídos em grupos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de objetos de grupo.

### HWM_GRP_MEMBERS_F
**Descrição:** Membros de grupos de workforce management com data efetiva.
**Módulo:** HCM - Time and Labor
**Uso típico:** Gestão de membros de grupos.

### HWM_GRP_TYPE
**Descrição:** Tipos de grupos de workforce management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Classificação de grupos.

### HWM_LAYER
**Descrição:** Camadas de processamento de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de camadas de cálculo.

### HWM_RP_TM_PERIODS_B
**Descrição:** Períodos de tempo para relatórios de ponto.
**Módulo:** HCM - Time and Labor
**Uso típico:** Definição de períodos de reporting.

### HWM_RP_TM_PERIODS_TL
**Descrição:** Traduções dos períodos de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_RP_TM_PERIODS_VL
**Descrição:** View de períodos com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_RP_TM_RESOLVED
**Descrição:** Registros de tempo resolvidos/processados.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de tempo após processamento de regras.

### HWM_RULES
**Descrição:** Regras de processamento de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de regras de cálculo de horas.

### HWM_RULE_INPUTS
**Descrição:** Inputs das regras de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Parâmetros de entrada de regras.

### HWM_RULE_OUTPUTS
**Descrição:** Outputs das regras de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Resultados de processamento de regras.

### HWM_RULE_SETS_F
**Descrição:** Conjuntos de regras de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Agrupamento de regras.

### HWM_RULE_SET_MBRS
**Descrição:** Membros de conjuntos de regras.
**Módulo:** HCM - Time and Labor
**Uso típico:** Composição de conjuntos de regras.

### HWM_RULE_TMPLTS
**Descrição:** Templates de regras de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Modelos de regras reutilizáveis.

### HWM_RULE_TMPLTS_TL
**Descrição:** Traduções dos templates de regras.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_RULE_TMPLT_INPUTS
**Descrição:** Inputs dos templates de regras.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de entradas de templates.

### HWM_RULE_TMPLT_INPUTS_TL
**Descrição:** Traduções dos inputs de templates.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_RULE_TMPLT_USAGES
**Descrição:** Usos de templates de regras.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de onde templates são utilizados.

### HWM_RULE_TMPLT_USAGES_TL
**Descrição:** Traduções dos usos de templates.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCATS_B
**Descrição:** Categorias de tempo (time categories) — classificação de tipos de hora (regular, extra, noturno, etc.).
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de categorias de tempo.

### HWM_TCATS_TL
**Descrição:** Traduções das categorias de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCATS_VL
**Descrição:** View de categorias de tempo com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_TCAT_EXPR_RESULTS_B
**Descrição:** Resultados de expressões de categorias de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Avaliação de expressões de categorias.

### HWM_TCAT_EXPR_RESULTS_TL
**Descrição:** Traduções dos resultados de expressões.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCD_EXP_DATA_DEF_B
**Descrição:** Definições de dados de exportação de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de exportação.

### HWM_TCD_EXP_DATA_DEF_TL
**Descrição:** Traduções das definições de exportação.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCD_MAPPINGS_B
**Descrição:** Mapeamentos de time card — regras de mapeamento de dados de ponto.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de transformação de dados.

### HWM_TCD_MAPPINGS_TL
**Descrição:** Traduções dos mapeamentos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCD_MAPPING_DTLS
**Descrição:** Detalhes dos mapeamentos de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração detalhada.

### HWM_TCD_MAPPING_SETS_B
**Descrição:** Conjuntos de mapeamentos de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Agrupamento de mapeamentos.

### HWM_TCD_MAPPING_SETS_TL
**Descrição:** Traduções dos conjuntos de mapeamentos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCD_MAPPING_SET_DTLS
**Descrição:** Detalhes dos conjuntos de mapeamentos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração detalhada de conjuntos.

### HWM_TCSMRS_B
**Descrição:** Consumers de time card (time card summary consumers).
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de consumidores de dados de ponto.

### HWM_TCSMRS_TL
**Descrição:** Traduções dos consumers.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCSMRS_VL
**Descrição:** View de consumers com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_TCSMR_CONFIGS
**Descrição:** Configurações de consumers de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Setup de integrações de tempo.

### HWM_TCSMR_CONFIG_SETS_B
**Descrição:** Conjuntos de configurações de consumers.
**Módulo:** HCM - Time and Labor
**Uso típico:** Agrupamento de configurações.

### HWM_TCSMR_CONFIG_SETS_TL
**Descrição:** Traduções dos conjuntos de configurações.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TCSMR_XFR_CONFIGS
**Descrição:** Configurações de transferência de consumers de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Setup de transferência de dados de ponto.

### HWM_TCSMR_XFR_PROCESSES_VL
**Descrição:** View de processos de transferência de consumers.
**Módulo:** HCM - Time and Labor
**Uso típico:** Monitoramento de transferências.

### HWM_TC_VERSION_STATUS_V
**Descrição:** View de status de versão de time card.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de status de cartões de ponto.

### HWM_TE_ALT_NAMES
**Descrição:** Nomes alternativos de elementos de tempo (time elements).
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de aliases.

### HWM_TE_ALT_NAME_VALS_B
**Descrição:** Valores de nomes alternativos de elementos de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de valores de aliases.

### HWM_TE_ALT_NAME_VALS_TL
**Descrição:** Traduções dos valores de nomes alternativos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TE_ALT_NAME_VALS_VL
**Descrição:** View de valores de nomes alternativos com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_TE_MESSAGES_V
**Descrição:** View de mensagens de elementos de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Mensagens de erro/validação.

### HWM_TE_VERSION_STATUS_V
**Descrição:** View de status de versão de elementos de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de status.

### HWM_TM_ABS_ENTRY_V
**Descrição:** View de entradas de ausência no contexto de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Integração ausências↔tempo.

### HWM_TM_ALLOW_EXPS_V
**Descrição:** View de exceções permitidas no time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Gestão de exceções.

### HWM_TM_APPROVED_TS_V
**Descrição:** View de timesheets aprovados.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de cartões aprovados.

### HWM_TM_ATRB_FLDS_B
**Descrição:** Campos de atributos de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de atributos.

### HWM_TM_ATRB_FLDS_TL
**Descrição:** Traduções dos campos de atributos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TM_ATRB_FLDS_VL
**Descrição:** View de campos de atributos com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_TM_ATRB_FLD_MSTR_REF_B
**Descrição:** Referências master de campos de atributos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de referências.

### HWM_TM_ATRB_FLD_MSTR_REF_TL
**Descrição:** Traduções das referências master.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TM_ATRB_FLD_MSTR_REF_VL
**Descrição:** View de referências master com tradução.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta consolidada.

### HWM_TM_ATRB_FLD_SET_CMPS
**Descrição:** Componentes de conjuntos de campos de atributos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de conjuntos de campos.

### HWM_TM_AUDITS
**Descrição:** Registros de auditoria de time management — log de alterações em dados de ponto.
**Módulo:** HCM - Time and Labor
**Uso típico:** Auditoria de alterações em timesheets.

### HWM_TM_AUDIT_ATRBS
**Descrição:** Atributos dos registros de auditoria de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Detalhamento de auditoria.

### HWM_TM_A_ANC_APP_STATUS_V
**Descrição:** View de status de aprovação de ausências no contexto de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Monitoramento de aprovações.

### HWM_TM_A_APP_STATUS_PJC_V
**Descrição:** View de status de aprovação de projetos no time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Status de aprovação por projeto.

### HWM_TM_A_APP_STATUS_PYR_V
**Descrição:** View de status de aprovação de folha no time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Status de aprovação para payroll.

### HWM_TM_A_TE_COMPLETED_V
**Descrição:** View de elementos de tempo completados.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de elementos finalizados.

### HWM_TM_A_TR_ERR_STATUS_V
**Descrição:** View de status de erro de transferência.
**Módulo:** HCM - Time and Labor
**Uso típico:** Monitoramento de erros.

### HWM_TM_A_USER_STATUS_V
**Descrição:** View de status do usuário no time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Status de cartões por usuário.

### HWM_TM_A_XFR_STATUS_PJC_V
**Descrição:** View de status de transferência para projetos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Monitoramento de transferência para Project Costing.

### HWM_TM_A_XFR_STATUS_PYR_V
**Descrição:** View de status de transferência para folha de pagamento.
**Módulo:** HCM - Time and Labor
**Uso típico:** Monitoramento de transferência para Payroll.

### HWM_TM_COMP_MSGS_V
**Descrição:** View de mensagens de compensação de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Mensagens de processamento.

### HWM_TM_D_TM_UI_STATUS_V
**Descrição:** View de status da interface de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Status de apresentação na UI.

### HWM_TM_D_XFR_STATUS_PJC_V
**Descrição:** View de status detalhado de transferência para projetos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Detalhamento de transferências.

### HWM_TM_D_XFR_STATUS_PYR_V
**Descrição:** View de status detalhado de transferência para payroll.
**Módulo:** HCM - Time and Labor
**Uso típico:** Detalhamento de transferências.

### HWM_TM_EVENTS_V
**Descrição:** View de eventos de time management (clock-in, clock-out, etc.).
**Módulo:** HCM - Time and Labor
**Uso típico:** Extração de eventos de ponto.

### HWM_TM_EVENT_ATRBS
**Descrição:** Atributos de eventos de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados adicionais de eventos.

### HWM_TM_HIS_ABS_ENTRY_V
**Descrição:** View histórica de entradas de ausência no time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Histórico de ausências integradas.

### HWM_TM_HIS_ENTRY_V
**Descrição:** View histórica de entradas de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Histórico de registros de ponto.

### HWM_TM_HIS_RPT_ENTRY_V
**Descrição:** View histórica de entradas de tempo reportadas.
**Módulo:** HCM - Time and Labor
**Uso típico:** Histórico de tempo reportado.

### HWM_TM_OPM_MEANING_V
**Descrição:** View de significados OPM (Oracle Process Manufacturing) no contexto de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de significados.

### HWM_TM_REC
**Descrição:** Registros de tempo (time records) — lançamentos individuais no timesheet.
**Módulo:** HCM - Time and Labor
**Uso típico:** Extração de registros de ponto.

### HWM_TM_REC_GRP
**Descrição:** Grupos de registros de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Agrupamento de registros.

### HWM_TM_REC_GRP_USAGES
**Descrição:** Usos de grupos de registros de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de usos.

### HWM_TM_REPROCESS_REQUEST
**Descrição:** Solicitações de reprocessamento de dados de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Gestão de reprocessamentos.

### HWM_TM_REP_ATRBS
**Descrição:** Atributos de reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de atributos de relatório.

### HWM_TM_REP_ATRB_DATE_VAL_V
**Descrição:** View de valores de data de atributos de reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Valores de atributos tipo data.

### HWM_TM_REP_ATRB_NUM_VAL_V
**Descrição:** View de valores numéricos de atributos de reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Valores de atributos tipo número.

### HWM_TM_REP_ATRB_TS_VAL_V
**Descrição:** View de valores timestamp de atributos de reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Valores de atributos tipo timestamp.

### HWM_TM_REP_ATRB_USAGES
**Descrição:** Usos de atributos de reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Referência de usos.

### HWM_TM_REP_ATRB_VARCHAR_VAL_V
**Descrição:** View de valores texto de atributos de reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Valores de atributos tipo texto.

### HWM_TM_REP_MSGS
**Descrição:** Mensagens de reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Mensagens de processamento.

### HWM_TM_REP_M_ANC_ATRBS_V
**Descrição:** View de atributos de ausência no reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Integração ausência↔tempo.

### HWM_TM_REP_M_COMP_TOIL_ATRBS_V
**Descrição:** View de atributos de compensação/TOIL (time off in lieu) no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de banco de horas.

### HWM_TM_REP_M_CUST_ATRB_VAL_V
**Descrição:** View de valores de atributos customizados no reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Atributos configuráveis.

### HWM_TM_REP_M_PJC_DOC_ATRBS_V
**Descrição:** View de atributos de documentos de projeto no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de projeto em timesheets.

### HWM_TM_REP_M_PJC_EXP_ATRBS_V
**Descrição:** View de atributos de despesas de projeto no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Despesas de projeto em timesheets.

### HWM_TM_REP_M_PTT_ATRBS_V
**Descrição:** View de atributos de padrões de tempo no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Padrões de trabalho.

### HWM_TM_REP_S_ABS_HP_ATRBS_V
**Descrição:** View de atributos de ausência (half pay) no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Ausências com meio pagamento.

### HWM_TM_REP_S_ABS_TEP_ATRBS_V
**Descrição:** View de atributos de ausência (time entry period) no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Ausências por período de entrada.

### HWM_TM_REP_S_COMMON_ATRBS_V
**Descrição:** View de atributos comuns no reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Atributos compartilhados.

### HWM_TM_REP_S_HXT_ATRBS_V
**Descrição:** View de atributos HXT (timecard layout) no reporting.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de layout de timecard.

### HWM_TM_REP_S_PJC_ATRBS_V
**Descrição:** View de atributos de projeto no reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de projeto.

### HWM_TM_REP_S_SEC_ATRBS_V
**Descrição:** View de atributos de segurança no reporting de tempo.
**Módulo:** HCM - Time and Labor
**Uso típico:** Dados de segurança.

### HWM_TM_RPT_ENTRY_V
**Descrição:** View de entradas de tempo para reporting — visão consolidada de horas reportadas.
**Módulo:** HCM - Time and Labor
**Uso típico:** Extração principal de dados de ponto para relatórios.

### HWM_TM_SOURCES
**Descrição:** Fontes de dados de tempo (relógio de ponto, entrada manual, integração).
**Módulo:** HCM - Time and Labor
**Uso típico:** Rastreamento de origem dos registros.

### HWM_TM_STATUSES
**Descrição:** Status de registros de tempo (submetido, aprovado, rejeitado, transferido).
**Módulo:** HCM - Time and Labor
**Uso típico:** Workflow de aprovação de ponto.

### HWM_TM_STATUS_DEF_B
**Descrição:** Definições de status de time management.
**Módulo:** HCM - Time and Labor
**Uso típico:** Configuração de status.

### HWM_TM_STATUS_DEF_TL
**Descrição:** Traduções das definições de status.
**Módulo:** HCM - Time and Labor
**Uso típico:** Suporte multilíngue.

### HWM_TM_SUBMITTED_TS_V
**Descrição:** View de timesheets submetidos.
**Módulo:** HCM - Time and Labor
**Uso típico:** Consulta de cartões submetidos para aprovação.

---

## 22. Configuração de Timecard / Layout (HXT)

Tabelas de configuração de **Timecard Layout** — definição de layouts e perfis de entrada de ponto.

### HXT_SCH_ASGS_DEFAULT_VIEW
**Descrição:** View de atribuições padrão de escalas.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta de escalas padrão.

### HXT_SCH_PROF_DEFAULT_VIEW
**Descrição:** View de perfis de escala padrão.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta de perfis de escala.

### HXT_SETUP_OPTION_VALS
**Descrição:** Valores de opções de configuração de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Configuração de opções.

### HXT_SETUP_PROFILES_B
**Descrição:** Perfis de configuração de timecard — define regras de entrada de ponto.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Configuração de perfis de entrada.

### HXT_SETUP_PROFILES_TL
**Descrição:** Traduções dos perfis de configuração.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Suporte multilíngue.

### HXT_SETUP_PROFILES_VL
**Descrição:** View de perfis com tradução.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta consolidada.

### HXT_SETUP_PROFILE_ASGS
**Descrição:** Atribuições de perfis de configuração a colaboradores/grupos.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Vinculação de perfis a populações.

### HXT_TCLAYFLD_DEFNS_B
**Descrição:** Definições de campos de layout de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Configuração de campos na tela de ponto.

### HXT_TCLAYFLD_DEFNS_TL
**Descrição:** Traduções das definições de campos de layout.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Suporte multilíngue.

### HXT_TCLAYFLD_DEFNS_VL
**Descrição:** View de definições de campos com tradução.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta consolidada.

### HXT_TCLAYST_B
**Descrição:** Layouts de timecard — define a estrutura visual do cartão de ponto.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Configuração de layouts de entrada.

### HXT_TCLAYST_PROP
**Descrição:** Propriedades dos layouts de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Configuração avançada de layouts.

### HXT_TCLAYST_TL
**Descrição:** Traduções dos layouts de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Suporte multilíngue.

### HXT_TCLAY_REGION_V
**Descrição:** View de regiões de layout de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta de regiões de layout.

### HXT_TCLAY_V
**Descrição:** View de layouts de timecard.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Consulta consolidada de layouts.

### HXT_TM_HEADER
**Descrição:** Cabeçalho de timecard — registro principal do cartão de ponto por período.
**Módulo:** HCM - Time and Labor / Timecard
**Uso típico:** Extração de cabeçalhos de cartões de ponto.

---

## 23. Geografia e Localização (HZ)

Tabelas de **Trading Community Architecture (TCA)** — dados geográficos, parties e estruturas de endereço.

### HZ_GEOGRAPHIES
**Descrição:** Geografias — hierarquia de regiões geográficas (país, estado, cidade, CEP).
**Módulo:** Foundation / Geography
**Uso típico:** Referência geográfica para endereços.

### HZ_GEOGRAPHY_TYPES_B
**Descrição:** Tipos de geografia (país, estado, município, etc.).
**Módulo:** Foundation / Geography
**Uso típico:** Classificação de níveis geográficos.

### HZ_GEOGRAPHY_TYPES_TL
**Descrição:** Traduções dos tipos de geografia.
**Módulo:** Foundation / Geography
**Uso típico:** Suporte multilíngue.

### HZ_GEO_STRUCTURE_LEVELS
**Descrição:** Níveis de estrutura geográfica — define a hierarquia (país → estado → cidade).
**Módulo:** Foundation / Geography
**Uso típico:** Configuração de hierarquia geográfica.

### HZ_PARTIES
**Descrição:** **Tabela de parties (partes)** — entidade central do TCA que representa pessoas, organizações e grupos.
**Módulo:** Foundation / TCA
**Uso típico:** Referência cruzada de entidades; base para dados de pessoa e organização.

### HZ_PARTY_USG_ASSIGNMENTS
**Descrição:** Atribuições de uso de parties — define como cada party é usada (empregado, candidato, fornecedor, etc.).
**Módulo:** Foundation / TCA
**Uso típico:** Classificação de parties por uso.

---

## 24. Organizações de Inventário (INV)

### INV_ORGANIZATION_DEFINITIONS_V
**Descrição:** View de definições de organizações de inventário — unidades organizacionais no contexto de supply chain.
**Módulo:** SCM / Inventory
**Uso típico:** Referência cruzada de organizações de inventário com organizações de HR.

---

## 25. Recrutamento (IRC)

Tabelas do módulo **Recruiting / iRecruitment** — requisições, candidatos, processos seletivos, ofertas e campanhas.

### IRC_AF_BLOCKS_B
**Descrição:** Blocos de fluxos de candidatura (Application Flow blocks).
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de formulários de candidatura.

### IRC_AF_BLOCKS_TL
**Descrição:** Traduções dos blocos de fluxo.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_AF_PAGES_B
**Descrição:** Páginas de fluxos de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de páginas.

### IRC_AF_PAGES_TL
**Descrição:** Traduções das páginas.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_AF_PAGE_BLOCKS_B
**Descrição:** Blocos dentro de páginas de fluxo de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Composição de páginas.

### IRC_AF_PAGE_BLOCKS_TL
**Descrição:** Traduções dos blocos de página.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_AF_SECTIONS_B
**Descrição:** Seções dos fluxos de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Estruturação de formulários.

### IRC_AF_SECTIONS_TL
**Descrição:** Traduções das seções.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_AF_VERSIONS
**Descrição:** Versões dos fluxos de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Versionamento de formulários.

### IRC_AGENT_REQUISITIONS
**Descrição:** Requisições atribuídas a agentes de recrutamento (agências externas).
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de agências de recrutamento.

### IRC_APPLY_FLOWS_B
**Descrição:** Fluxos de candidatura — define o processo de application dos candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de fluxos de candidatura.

### IRC_APPLY_FLOWS_TL
**Descrição:** Traduções dos fluxos de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_ASMT_ACCT_PACKAGES
**Descrição:** Pacotes de assessment por conta (parceiro de avaliação).
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de assessments externos.

### IRC_ASMT_PACKAGE_RESULTS
**Descrição:** Resultados de pacotes de assessment.
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de resultados de testes.

### IRC_ASMT_PARTNER_CONFIG
**Descrição:** Configuração de parceiros de assessment.
**Módulo:** HCM - Recruiting
**Uso típico:** Setup de integrações com ferramentas de avaliação.

### IRC_ASMT_REQ_CONFIG
**Descrição:** Configuração de assessments por requisição.
**Módulo:** HCM - Recruiting
**Uso típico:** Vinculação de testes a vagas.

### IRC_ASMT_REQ_PACKAGES
**Descrição:** Pacotes de assessment por requisição.
**Módulo:** HCM - Recruiting
**Uso típico:** Testes vinculados a vagas.

### IRC_ASMT_RESULTS
**Descrição:** Resultados individuais de assessments de candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de resultados de testes.

### IRC_BC_CAND_RESULTS
**Descrição:** Resultados de background check de candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Verificação de antecedentes.

### IRC_BC_CAND_SCREENINGS
**Descrição:** Screenings de background check por candidato.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de verificações.

### IRC_BC_REQ_SP_ASSGMNTS
**Descrição:** Atribuições de provedores de screening por requisição.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de background check por vaga.

### IRC_CAMPAIGNS_B
**Descrição:** Campanhas de recrutamento — iniciativas de atração de candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de campanhas de employer branding.

### IRC_CAMPAIGNS_TL
**Descrição:** Traduções das campanhas.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CAMP_ASSETS_B
**Descrição:** Assets/materiais de campanhas de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de materiais de marketing.

### IRC_CAMP_ASSETS_TL
**Descrição:** Traduções dos assets de campanha.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CAMP_AUDIENCE
**Descrição:** Audiência/público-alvo das campanhas de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Segmentação de público.

### IRC_CAMP_CONVERSIONS
**Descrição:** Conversões de campanhas — candidatos que se candidataram via campanha.
**Módulo:** HCM - Recruiting
**Uso típico:** Métricas de conversão de campanhas.

### IRC_CAMP_GOALS_B
**Descrição:** Metas das campanhas de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Definição de objetivos de campanha.

### IRC_CAMP_GOALS_TL
**Descrição:** Traduções das metas de campanha.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CAMP_GOAL_RESP_B
**Descrição:** Respostas às metas de campanha.
**Módulo:** HCM - Recruiting
**Uso típico:** Acompanhamento de metas.

### IRC_CAMP_GOAL_RESP_TL
**Descrição:** Traduções das respostas de metas.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CAMP_REQUISITIONS
**Descrição:** Requisições vinculadas a campanhas de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Associação vaga↔campanha.

### IRC_CAMP_TRACK_RESPONSE
**Descrição:** Rastreamento de respostas a campanhas.
**Módulo:** HCM - Recruiting
**Uso típico:** Analytics de engajamento.

### IRC_CANDIDATES
**Descrição:** **Tabela principal de candidatos** — dados de todos os candidatos do sistema de recrutamento, incluindo status, fonte e dados de contato.
**Módulo:** HCM - Recruiting
**Uso típico:** Extração de base de candidatos; relatórios de pipeline de recrutamento.

### IRC_CANDIDATE_ADDRESS_V
**Descrição:** View de endereços dos candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Dados de localização de candidatos.

### IRC_CANDIDATE_SEARCH_TRACKING
**Descrição:** Rastreamento de buscas de candidatos — log de pesquisas realizadas.
**Módulo:** HCM - Recruiting
**Uso típico:** Analytics de busca de candidatos.

### IRC_CAND_LAST_INTERACTION_V
**Descrição:** View da última interação com cada candidato.
**Módulo:** HCM - Recruiting
**Uso típico:** Monitoramento de engajamento.

### IRC_CAND_POOL_MEMBERS
**Descrição:** Membros de pools de candidatos — candidatos agrupados em pools temáticos.
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de talent pools de recrutamento.

### IRC_CAND_PREFERENCES
**Descrição:** Preferências dos candidatos (tipo de trabalho, salário desejado, etc.).
**Módulo:** HCM - Recruiting
**Uso típico:** Matching de candidatos com vagas.

### IRC_CAND_PREF_JOB_FAMILY
**Descrição:** Preferências de família de cargo dos candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Matching por área de interesse.

### IRC_CAND_PREF_LOCATIONS
**Descrição:** Preferências de localização dos candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Matching por localização.

### IRC_CAND_PROFILE_USAGES_M
**Descrição:** Usos de perfil de candidatos — vinculação do perfil de talento ao candidato.
**Módulo:** HCM - Recruiting
**Uso típico:** Integração perfil↔candidato.

### IRC_CMT_LAUNCHES
**Descrição:** Lançamentos de comunicação (CMT - Communication) com candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de comunicações.

### IRC_CMT_RECIPIENTS
**Descrição:** Destinatários de comunicações.
**Módulo:** HCM - Recruiting
**Uso típico:** Lista de destinatários.

### IRC_CX_PAGES_B
**Descrição:** Páginas de Candidate Experience (site de carreiras).
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração do site de carreiras.

### IRC_CX_PAGES_TL
**Descrição:** Traduções das páginas CX.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CX_SITES_B
**Descrição:** Sites de Candidate Experience — portais de carreiras configurados.
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de sites de carreiras.

### IRC_CX_SITES_TL
**Descrição:** Traduções dos sites CX.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CX_SITE_LANGS
**Descrição:** Idiomas habilitados nos sites de carreiras.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração multilíngue de sites.

### IRC_CX_SITE_TEMPLATES_B
**Descrição:** Templates de sites de carreiras.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração visual dos portais.

### IRC_CX_SITE_TEMPLATES_TL
**Descrição:** Traduções dos templates de sites.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_CX_SITE_THEMES
**Descrição:** Temas visuais dos sites de carreiras.
**Módulo:** HCM - Recruiting
**Uso típico:** Personalização visual.

### IRC_DESCRIPTIONS_B
**Descrição:** Descrições reutilizáveis (templates de descrição de vaga).
**Módulo:** HCM - Recruiting
**Uso típico:** Biblioteca de descrições.

### IRC_DESCRIPTIONS_TL
**Descrição:** Traduções das descrições.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_DESC_VERSIONS_B
**Descrição:** Versões das descrições de vaga.
**Módulo:** HCM - Recruiting
**Uso típico:** Versionamento de conteúdo.

### IRC_DESC_VERSIONS_TL
**Descrição:** Traduções das versões.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_DIMENSION_DEF_B
**Descrição:** Definições de dimensões de recrutamento (ex.: senioridade, localização).
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de dimensões analíticas.

### IRC_DIMENSION_DEF_TL
**Descrição:** Traduções das dimensões.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_ENDORSEMENTS
**Descrição:** Endossos/recomendações de candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Referências e recomendações.

### IRC_ESIGNATURES
**Descrição:** Assinaturas eletrônicas no processo de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Aceite digital de termos e ofertas.

### IRC_GEO_HIERARCHIES
**Descrição:** Hierarquias geográficas para recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de áreas geográficas.

### IRC_GEO_HIER_NODES
**Descrição:** Nós das hierarquias geográficas.
**Módulo:** HCM - Recruiting
**Uso típico:** Estrutura de hierarquia geográfica.

### IRC_GEO_LEVEL_MAPPINGS
**Descrição:** Mapeamentos de níveis geográficos.
**Módulo:** HCM - Recruiting
**Uso típico:** Associação de níveis geográficos.

### IRC_HIST_EVENT_B
**Descrição:** Eventos históricos de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Auditoria de eventos.

### IRC_HIST_EVENT_TL
**Descrição:** Traduções dos eventos históricos.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_IM_FEEDBACKS
**Descrição:** Feedbacks de entrevistas (Interview Management).
**Módulo:** HCM - Recruiting
**Uso típico:** Coleta de feedback de entrevistadores.

### IRC_IM_FEEDBK_PARTCPTS
**Descrição:** Participantes dos feedbacks de entrevista.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de entrevistadores.

### IRC_IM_FEEDBK_REQUESTS
**Descrição:** Solicitações de feedback de entrevista.
**Módulo:** HCM - Recruiting
**Uso típico:** Workflow de coleta de feedback.

### IRC_IM_FEEDBK_REVIEWS
**Descrição:** Revisões de feedback de entrevista.
**Módulo:** HCM - Recruiting
**Uso típico:** Consolidação de feedbacks.

### IRC_IM_REQ_QSTNRS
**Descrição:** Questionários vinculados a requisições para entrevistas.
**Módulo:** HCM - Recruiting
**Uso típico:** Guias de entrevista por vaga.

### IRC_INTERACTIONS
**Descrição:** Interações com candidatos — registro de todas as comunicações e ações.
**Módulo:** HCM - Recruiting
**Uso típico:** Histórico de interações.

### IRC_JA_LAST_INTERACTION_V
**Descrição:** View da última interação de candidaturas (job applications).
**Módulo:** HCM - Recruiting
**Uso típico:** Monitoramento de status.

### IRC_JA_SECONDARY_FLOWS
**Descrição:** Fluxos secundários de candidaturas.
**Módulo:** HCM - Recruiting
**Uso típico:** Processos adicionais de candidatura.

### IRC_JD_REQ_POSTINGS
**Descrição:** Publicações de vagas (job postings) — onde cada requisição foi publicada.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de publicações de vagas.

### IRC_JD_REQ_POST_HISTORY
**Descrição:** Histórico de publicações de vagas.
**Módulo:** HCM - Recruiting
**Uso típico:** Auditoria de publicações.

### IRC_JD_REQ_POST_RESULTS
**Descrição:** Resultados de publicações de vagas — métricas de cada canal.
**Módulo:** HCM - Recruiting
**Uso típico:** Analytics de canais de divulgação.

### IRC_LC_ACTIONS_TL
**Descrição:** Traduções de ações do lifecycle de candidatura.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_LC_ACTION_USAGES_B
**Descrição:** Usos de ações do lifecycle.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de ações.

### IRC_LC_ACTION_USAGES_TL
**Descrição:** Traduções dos usos de ações.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_LC_HISTORY
**Descrição:** Histórico do lifecycle de candidatura — registro de todas as transições de fase.
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de funil de recrutamento; tempo em cada fase.

### IRC_LC_REASONS_B
**Descrição:** Motivos de ações no lifecycle (ex.: motivo de rejeição, desistência).
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de motivos de perda.

### IRC_LC_REASONS_TL
**Descrição:** Traduções dos motivos.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_LC_REASON_GROUPS_TL
**Descrição:** Traduções dos grupos de motivos.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_LC_SETTING_ITEMS
**Descrição:** Itens de configuração do lifecycle de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Setup de fases e regras.

### IRC_MEDIA_LINKS_B
**Descrição:** Links de mídia para vagas (vídeos, imagens, documentos).
**Módulo:** HCM - Recruiting
**Uso típico:** Enriquecimento de anúncios de vaga.

### IRC_MEDIA_LINKS_TL
**Descrição:** Traduções dos links de mídia.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_MEDIA_LINK_LANGUAGES
**Descrição:** Idiomas dos links de mídia.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração multilíngue.

### IRC_OFFERS
**Descrição:** **Ofertas de emprego** — tabela principal de ofertas feitas a candidatos, com salário, data de início, status e condições.
**Módulo:** HCM - Recruiting
**Uso típico:** Extração de ofertas; análise de acceptance rate; relatórios de compensação de contratação.

### IRC_PHASES_B
**Descrição:** Fases do processo seletivo (triagem, entrevista, oferta, etc.).
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de fases do pipeline.

### IRC_PHASES_TL
**Descrição:** Traduções das fases.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_POOLMEM_LAST_INTERACTION_V
**Descrição:** View da última interação de membros de pools.
**Módulo:** HCM - Recruiting
**Uso típico:** Engajamento de talent pools.

### IRC_PROCESSES_B
**Descrição:** Processos de recrutamento — define fluxos de seleção.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de processos seletivos.

### IRC_PROCESSES_TL
**Descrição:** Traduções dos processos.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_PROSPECTS
**Descrição:** Prospects — candidatos em potencial identificados mas não candidatados.
**Módulo:** HCM - Recruiting
**Uso típico:** Sourcing proativo.

### IRC_PRSPT_LAST_INTERACTION_V
**Descrição:** View da última interação com prospects.
**Módulo:** HCM - Recruiting
**Uso típico:** Engajamento de prospects.

### IRC_REGULATORY_RESPONSES
**Descrição:** Respostas regulatórias de candidatos (ex.: EEO, diversidade).
**Módulo:** HCM - Recruiting
**Uso típico:** Compliance regulatório e relatórios de diversidade.

### IRC_REQUISITIONS_B
**Descrição:** **Requisições de vaga** — tabela principal de requisições de pessoal, com cargo, departamento, headcount, status e datas.
**Módulo:** HCM - Recruiting
**Uso típico:** Extração de vagas abertas/fechadas; dashboards de recrutamento; análise de time-to-fill.

### IRC_REQUISITIONS_TL
**Descrição:** Traduções das requisições (título da vaga em múltiplos idiomas).
**Módulo:** HCM - Recruiting
**Uso típico:** Publicação multilíngue de vagas.

### IRC_REQ_LANGUAGES
**Descrição:** Idiomas requeridos pela requisição.
**Módulo:** HCM - Recruiting
**Uso típico:** Requisitos linguísticos de vagas.

### IRC_REQ_LOCATIONS
**Descrição:** Localizações das requisições — onde a vaga está disponível.
**Módulo:** HCM - Recruiting
**Uso típico:** Vagas por localização.

### IRC_REQ_MEDIA_LINKS
**Descrição:** Links de mídia vinculados a requisições.
**Módulo:** HCM - Recruiting
**Uso típico:** Materiais de divulgação por vaga.

### IRC_REQ_WORK_LOCATIONS
**Descrição:** Locais de trabalho das requisições (presencial, remoto, híbrido).
**Módulo:** HCM - Recruiting
**Uso típico:** Modalidade de trabalho por vaga.

### IRC_RF_REFERRALS
**Descrição:** Indicações (referrals) — candidatos indicados por colaboradores.
**Módulo:** HCM - Recruiting
**Uso típico:** Programa de indicações; análise de fonte de contratação.

### IRC_RF_REQ_HITS
**Descrição:** Acessos a requisições via programa de indicação.
**Módulo:** HCM - Recruiting
**Uso típico:** Métricas de engajamento de referral.

### IRC_RF_SHARES
**Descrição:** Compartilhamentos de vagas por colaboradores.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de compartilhamentos.

### IRC_ROUTING_STEPS_B
**Descrição:** Etapas de roteamento de candidaturas.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de fluxo de encaminhamento.

### IRC_SEARCHES
**Descrição:** Buscas realizadas no sistema de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Analytics de busca.

### IRC_SEARCHES_DN
**Descrição:** Buscas denormalizadas para reporting.
**Módulo:** HCM - Recruiting
**Uso típico:** Relatórios de busca.

### IRC_SEARCH_ACTIONS
**Descrição:** Ações realizadas a partir de buscas.
**Módulo:** HCM - Recruiting
**Uso típico:** Rastreamento de ações pós-busca.

### IRC_SEARCH_ACTION_DETAILS
**Descrição:** Detalhes das ações de busca.
**Módulo:** HCM - Recruiting
**Uso típico:** Detalhamento de ações.

### IRC_SEARCH_RESULTS
**Descrição:** Resultados de buscas de candidatos.
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de resultados de pesquisa.

### IRC_SOURCE_TRACKING
**Descrição:** Rastreamento de fontes de candidatos — de onde cada candidato veio (site, LinkedIn, indicação, etc.).
**Módulo:** HCM - Recruiting
**Uso típico:** Análise de efetividade de canais de recrutamento.

### IRC_STATES_B
**Descrição:** Estados/fases do processo seletivo.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de estados do pipeline.

### IRC_STATES_TL
**Descrição:** Traduções dos estados.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_SUBMISSIONS
**Descrição:** **Candidaturas (submissions)** — tabela principal de candidaturas, vinculando candidatos a requisições com status, fase e histórico.
**Módulo:** HCM - Recruiting
**Uso típico:** Extração de pipeline de candidaturas; funil de recrutamento; análise de conversão.

### IRC_TEAM_MEMBERS
**Descrição:** Membros da equipe de recrutamento por requisição (hiring manager, recruiter, entrevistadores).
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão da equipe de seleção.

### IRC_TP_CATEGORIES_B
**Descrição:** Categorias de parceiros de recrutamento (talent partners).
**Módulo:** HCM - Recruiting
**Uso típico:** Classificação de parceiros.

### IRC_TP_CATEGORIES_TL
**Descrição:** Traduções das categorias de parceiros.
**Módulo:** HCM - Recruiting
**Uso típico:** Suporte multilíngue.

### IRC_TP_PARTNERS
**Descrição:** Parceiros de recrutamento (agências, job boards, etc.).
**Módulo:** HCM - Recruiting
**Uso típico:** Gestão de parceiros.

### IRC_TP_PARTNER_ACCOUNTS
**Descrição:** Contas de parceiros de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de contas.

### IRC_TP_PARTNER_PROVISNGS
**Descrição:** Provisionamentos de parceiros de recrutamento.
**Módulo:** HCM - Recruiting
**Uso típico:** Setup de integrações.

### IRC_WFMODEL_REQUISITIONS
**Descrição:** Modelos de workflow vinculados a requisições.
**Módulo:** HCM - Recruiting
**Uso típico:** Configuração de workflows de aprovação.

---

## 26. Recursos e Gerentes (JTF)

### JTF_RS_REP_MANAGERS
**Descrição:** Gerentes de reporting — hierarquia de gestores para representantes.
**Módulo:** Foundation / Resources
**Uso típico:** Hierarquia de gestão.

### JTF_RS_RESOURCE_PROFILES
**Descrição:** Perfis de recursos — dados de recursos/representantes do sistema.
**Módulo:** Foundation / Resources
**Uso típico:** Referência de perfis de recursos.

---

## 27. Folha de Pagamento (PAY)

Tabelas do módulo **Payroll** — processamento de folha, elementos salariais, pagamentos e resultados de cálculo.

### PAY_ALL_PAYROLLS_F
**Descrição:** **Tabela principal de folhas de pagamento** — define cada folha (payroll) com frequência, calendário, moeda e data efetiva.
**Módulo:** HCM - Payroll
**Uso típico:** Referência de folhas de pagamento; segmentação de colaboradores por payroll.

### PAY_ASSIGNED_PAYROLLS_DN
**Descrição:** View denormalizada de atribuições de folha de pagamento.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta rápida de atribuições.

### PAY_ASSIGNED_PAYROLLS_F
**Descrição:** Atribuições de colaboradores a folhas de pagamento com data efetiva.
**Módulo:** HCM - Payroll
**Uso típico:** Histórico de vinculação a payrolls.

### PAY_BALANCE_CATEGORIES_F
**Descrição:** Categorias de saldos de folha (ex.: statutory, voluntary).
**Módulo:** HCM - Payroll
**Uso típico:** Classificação de saldos.

### PAY_BALANCE_CATEGORIES_TL
**Descrição:** Traduções das categorias de saldos.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_BALANCE_CATEGORIES_VL
**Descrição:** View de categorias de saldos com tradução.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta consolidada.

### PAY_BALANCE_DIMENSIONS
**Descrição:** Dimensões de saldos de folha (ex.: período, YTD, MTD, QTD).
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de dimensões temporais de saldos.

### PAY_BALANCE_TYPES_TL
**Descrição:** Traduções dos tipos de saldos.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_BALANCE_TYPES_VL
**Descrição:** View de tipos de saldos com tradução — define o que cada saldo acumula (ex.: INSS, IRRF, salário bruto).
**Módulo:** HCM - Payroll
**Uso típico:** Referência de tipos de saldo; extração de acumuladores.

### PAY_BALANCE_VALIDATION
**Descrição:** Validações de saldos — regras de consistência de acumuladores.
**Módulo:** HCM - Payroll
**Uso típico:** Controle de qualidade de saldos.

### PAY_CONSOLIDATION_SETS
**Descrição:** Conjuntos de consolidação — define agrupamentos para processamento de folha.
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de processamento de folha.

### PAY_COSTS
**Descrição:** Custos da folha de pagamento — distribuição contábil de custos de pessoal.
**Módulo:** HCM - Payroll
**Uso típico:** Extração de custos para contabilidade; rateio de custos.

### PAY_DEDUCTION_GROUPS_VL
**Descrição:** View de grupos de deduções.
**Módulo:** HCM - Payroll
**Uso típico:** Agrupamento de deduções.

### PAY_DEDUCTION_TYPES
**Descrição:** Tipos de deduções (INSS, IRRF, pensão, empréstimo, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Referência de tipos de desconto.

### PAY_DEDUCTION_TYPES_TL
**Descrição:** Traduções dos tipos de deduções.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_DIR_CARDS_F
**Descrição:** Cartões de informação direta (direct cards) — cartões de dados de folha por colaborador.
**Módulo:** HCM - Payroll
**Uso típico:** Dados de entrada para cálculo de folha.

### PAY_DIR_CARD_COMPONENTS_F
**Descrição:** Componentes de cartões diretos.
**Módulo:** HCM - Payroll
**Uso típico:** Detalhamento de componentes.

### PAY_DIR_CARD_COMP_DEFS_F
**Descrição:** Definições de componentes de cartões diretos.
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de definições.

### PAY_DIR_CARD_COMP_DEFS_VL
**Descrição:** View de definições de componentes com tradução.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta consolidada.

### PAY_DIR_CARD_DEFINITIONS_VL
**Descrição:** View de definições de cartões diretos.
**Módulo:** HCM - Payroll
**Uso típico:** Referência de definições.

### PAY_DIR_COMP_DETAILS_F
**Descrição:** Detalhes de componentes de cartões diretos.
**Módulo:** HCM - Payroll
**Uso típico:** Dados granulares.

### PAY_ELEMENT_CRITERIA
**Descrição:** Critérios de elegibilidade de elementos de folha.
**Módulo:** HCM - Payroll
**Uso típico:** Regras de atribuição de elementos.

### PAY_ELEMENT_ENTRIES_F
**Descrição:** **Lançamentos de elementos por colaborador** — registra cada elemento atribuído a um colaborador (salário, benefício, dedução) com valores e datas.
**Módulo:** HCM - Payroll
**Uso típico:** Extração de todos os lançamentos de folha por pessoa; base para cálculo de folha.

### PAY_ELEMENT_ENTRIES_VL
**Descrição:** View de lançamentos de elementos com tradução.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta consolidada.

### PAY_ELEMENT_ENTRY_VALUES_F
**Descrição:** Valores dos lançamentos de elementos — valores de input de cada element entry.
**Módulo:** HCM - Payroll
**Uso típico:** Valores individuais de cada componente de folha.

### PAY_ELEMENT_TYPES_F
**Descrição:** **Tipos de elementos de folha** — define todos os componentes de remuneração (salário, horas extras, benefícios, deduções) com regras de processamento.
**Módulo:** HCM - Payroll
**Uso típico:** Referência de componentes de folha; configuração de remuneração.

### PAY_ELEMENT_TYPES_TL
**Descrição:** Traduções dos tipos de elementos.
**Módulo:** HCM - Payroll
**Uso típico:** Nomes de elementos em múltiplos idiomas.

### PAY_ELE_CLASSIFICATIONS
**Descrição:** Classificações de elementos de folha (earnings, deductions, employer charges, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Categorização de elementos.

### PAY_ELE_CLASSIFICATIONS_TL
**Descrição:** Traduções das classificações de elementos.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_ENTRY_USAGES
**Descrição:** Usos de lançamentos de elementos.
**Módulo:** HCM - Payroll
**Uso típico:** Referência de onde os lançamentos são utilizados.

### PAY_FLOW_TASK_INSTANCES
**Descrição:** Instâncias de tarefas de fluxo de payroll — etapas de processamento da folha.
**Módulo:** HCM - Payroll
**Uso típico:** Monitoramento de processamento de folha.

### PAY_INPUT_VALUES_F
**Descrição:** Valores de input de elementos de folha — define os campos de entrada de cada tipo de elemento.
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de campos de entrada.

### PAY_INPUT_VALUES_TL
**Descrição:** Traduções dos valores de input.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_ORG_PAY_METHODS_F
**Descrição:** Métodos de pagamento organizacionais — define como a organização efetua pagamentos (transferência, cheque, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de métodos de pagamento.

### PAY_ORG_PAY_METHODS_TL
**Descrição:** Traduções dos métodos de pagamento organizacionais.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_ORG_PAY_METHODS_VL
**Descrição:** View de métodos de pagamento organizacionais com tradução.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta consolidada.

### PAY_ORG_PAY_METHOD_USAGES_F
**Descrição:** Usos de métodos de pagamento organizacionais.
**Módulo:** HCM - Payroll
**Uso típico:** Vinculação de métodos a payrolls.

### PAY_PAYMENT_COSTS
**Descrição:** Custos de pagamentos — distribuição contábil por pagamento.
**Módulo:** HCM - Payroll
**Uso típico:** Contabilização de pagamentos.

### PAY_PAYMENT_TYPES
**Descrição:** Tipos de pagamento (crédito em conta, cheque, cash, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Referência de tipos de pagamento.

### PAY_PAYMENT_TYPES_TL
**Descrição:** Traduções dos tipos de pagamento.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_PAYROLL_ACTIONS
**Descrição:** **Ações de folha de pagamento** — cada execução de processamento de folha (cálculo, retro, reversal, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Rastreamento de processamentos de folha; auditoria de execuções.

### PAY_PAYROLL_REL_ACTIONS
**Descrição:** Ações de folha por payroll relationship — resultado do processamento por relação de trabalho.
**Módulo:** HCM - Payroll
**Uso típico:** Resultado de processamento por colaborador.

### PAY_PAY_RELATIONSHIPS_DN
**Descrição:** View denormalizada de payroll relationships.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta rápida.

### PAY_PAY_RELATIONSHIPS_F
**Descrição:** **Relações de folha de pagamento** — vincula pessoas a contextos de folha (um pessoa pode ter múltiplos payroll relationships).
**Módulo:** HCM - Payroll
**Uso típico:** Base para processamento de folha; segmentação de vínculos.

### PAY_PERSON_PAY_METHODS_F
**Descrição:** Métodos de pagamento pessoais — como cada colaborador recebe (conta bancária, split de pagamento).
**Módulo:** HCM - Payroll
**Uso típico:** Dados bancários para pagamento; split de salário.

### PAY_PRE_PAYMENTS
**Descrição:** Pré-pagamentos — valores calculados antes da efetivação do pagamento.
**Módulo:** HCM - Payroll
**Uso típico:** Verificação de valores antes do pagamento.

### PAY_REL_GROUPS_DN
**Descrição:** View denormalizada de grupos de relação de folha.
**Módulo:** HCM - Payroll
**Uso típico:** Consulta rápida.

### PAY_REL_GROUPS_F
**Descrição:** Grupos de relação de folha — agrupamentos de payroll relationships.
**Módulo:** HCM - Payroll
**Uso típico:** Segmentação para processamento.

### PAY_REQUESTS
**Descrição:** Requisições de processamento de folha.
**Módulo:** HCM - Payroll
**Uso típico:** Monitoramento de requisições de processamento.

### PAY_RUN_RESULTS
**Descrição:** **Resultados de processamento de folha** — valores calculados por elemento por colaborador em cada execução. Tabela essencial para extração de contracheques.
**Módulo:** HCM - Payroll
**Uso típico:** Extração de holerites; relatórios de folha; análise de custos de pessoal.

### PAY_RUN_TYPES_F
**Descrição:** Tipos de execução de folha (regular, suplementar, bônus, etc.).
**Módulo:** HCM - Payroll
**Uso típico:** Classificação de tipos de processamento.

### PAY_RUN_TYPES_TL
**Descrição:** Traduções dos tipos de execução.
**Módulo:** HCM - Payroll
**Uso típico:** Suporte multilíngue.

### PAY_TIME_PERIODS
**Descrição:** Períodos de folha de pagamento — define cada período (mês, quinzena, semana) com datas de início e fim.
**Módulo:** HCM - Payroll
**Uso típico:** Referência de períodos para processamento; dimensão temporal.

### PAY_TIME_PERIOD_TYPES
**Descrição:** Tipos de período de folha (mensal, quinzenal, semanal).
**Módulo:** HCM - Payroll
**Uso típico:** Configuração de frequências de pagamento.

---

## 28. Pessoa e Dados Básicos (PER)

Tabelas centrais do **Core HR** — dados pessoais, atribuições, cargos, grades, localizações, ausências e todos os dados fundamentais de pessoas.

### PER_ABSENCE_ATTENDANCES
**Descrição:** Registros de ausência e presença — lançamentos de ausências por colaborador (tabela legada, complementa ANC).
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Extração de ausências.

### PER_ABSENCE_ATTENDANCE_TYPES_B
**Descrição:** Tipos de ausência/presença (legado).
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Referência de tipos.

### PER_ABS_ATTENDANCE_REASONS
**Descrição:** Motivos de ausência/presença.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Justificativas.

### PER_ABS_ATTENDANCE_TYPES_TL
**Descrição:** Traduções dos tipos de ausência/presença.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Suporte multilíngue.

### PER_ACCRUAL_BANDS
**Descrição:** Faixas de acúmulo de ausência.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Progressão de direitos por tempo de serviço.

### PER_ACCRUAL_CALC_RULES
**Descrição:** Regras de cálculo de acúmulo de ausências.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Configuração de regras.

### PER_ACCRUAL_PLANS_B
**Descrição:** Planos de acúmulo de ausências.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Definição de planos.

### PER_ACCRUAL_PLANS_TL
**Descrição:** Traduções dos planos de acúmulo.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Suporte multilíngue.

### PER_ACTIONS_B
**Descrição:** Ações de HR — tipos de transação (admissão, promoção, transferência, desligamento, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Referência de ações; auditoria de transações.

### PER_ACTIONS_TL
**Descrição:** Traduções das ações.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_ACTION_OCCURRENCES
**Descrição:** Ocorrências de ações — registro de cada execução de uma ação de HR.
**Módulo:** HCM - Core HR
**Uso típico:** Auditoria de transações.

### PER_ACTION_REASONS_B
**Descrição:** Motivos de ações de HR (ex.: motivo de desligamento, motivo de transferência).
**Módulo:** HCM - Core HR
**Uso típico:** Análise de motivos de movimentações.

### PER_ACTION_REASONS_TL
**Descrição:** Traduções dos motivos de ações.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_ACTION_REASON_USAGES
**Descrição:** Usos de motivos de ações — quais motivos são válidos para quais ações.
**Módulo:** HCM - Core HR
**Uso típico:** Configuração de validações.

### PER_ACTION_TYPES_B
**Descrição:** Tipos de ações (admissão, promoção, transferência, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Classificação de ações.

### PER_ACTION_TYPES_TL
**Descrição:** Traduções dos tipos de ações.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_ADDRESSES_F
**Descrição:** **Endereços de pessoas** — endereços residenciais e correspondência com data efetiva. Contém rua, cidade, estado, CEP, país.
**Módulo:** HCM - Core HR
**Uso típico:** Extração de endereços; relatórios demográficos; validação de dados cadastrais.

### PER_ALLOCATED_CHECKLISTS
**Descrição:** Checklists alocados a colaboradores (onboarding, offboarding, etc.).
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Acompanhamento de processos de onboarding.

### PER_ALLOCATED_CHECKLISTS_TL
**Descrição:** Traduções dos checklists alocados.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Suporte multilíngue.

### PER_ALLOCATED_TASKS
**Descrição:** Tarefas alocadas dentro de checklists por colaborador.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Rastreamento de tarefas de onboarding.

### PER_ALLOCATED_TASKS_TL
**Descrição:** Traduções das tarefas alocadas.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Suporte multilíngue.

### PER_ALLOC_CHKLST_CONTACTS
**Descrição:** Contatos vinculados a checklists alocados.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Responsáveis por tarefas.

### PER_ALLOC_CHKLST_CONTENTS
**Descrição:** Conteúdo de checklists alocados.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Detalhes de checklists.

### PER_ALLOC_TASK_NOTIFS
**Descrição:** Notificações de tarefas alocadas.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Rastreamento de notificações.

### PER_ALL_ASSIGNMENTS_M
**Descrição:** **Tabela principal de atribuições (assignments)** — registra todos os vínculos de trabalho com cargo, departamento, posição, localização, grade, status e data efetiva. Tabela materializada (\_M) com histórico completo. Essencial para qualquer relatório de HR.
**Módulo:** HCM - Core HR
**Uso típico:** Base para praticamente todos os relatórios de HR; headcount; movimentações; estrutura organizacional.

### PER_ALL_PEOPLE_F
**Descrição:** **Tabela principal de pessoas** — dados de todas as pessoas no sistema HR (colaboradores, candidatos, dependentes, contatos) com data efetiva. Contém person_id, person_number e dados biográficos fundamentais.
**Módulo:** HCM - Core HR
**Uso típico:** Base para qualquer extração de dados de pessoas; chave principal para joins com outras tabelas HR.

### PER_ASG_ABSENCE_RECORDING
**Descrição:** Registro de ausências por assignment.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Ausências por vínculo de trabalho.

### PER_ASG_RESPONSIBILITIES
**Descrição:** Responsabilidades atribuídas a assignments.
**Módulo:** HCM - Core HR
**Uso típico:** Gestão de responsabilidades.

### PER_ASSIGNMENT_DAY_ABSENCES
**Descrição:** Ausências diárias por assignment.
**Módulo:** HCM - Core HR / Absences
**Uso típico:** Detalhamento diário de ausências.

### PER_ASSIGNMENT_EXTRA_INFO_M
**Descrição:** Informações extras de assignments — campos adicionais configuráveis (Extra Information Types / EIT).
**Módulo:** HCM - Core HR
**Uso típico:** Extração de campos customizados de assignments.

### PER_ASSIGNMENT_STATUS_TYPES
**Descrição:** Tipos de status de assignment (ativo, suspenso, terminado).
**Módulo:** HCM - Core HR
**Uso típico:** Referência de status.

### PER_ASSIGNMENT_STATUS_TYPES_TL
**Descrição:** Traduções dos tipos de status de assignment.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_ASSIGNMENT_SUPERVISORS_F
**Descrição:** Supervisores de assignments — define quem é o gestor de cada vínculo de trabalho.
**Módulo:** HCM - Core HR
**Uso típico:** Construção de hierarquias de gestão.

### PER_ASSIGN_GRADE_STEPS_F
**Descrição:** Steps de grade atribuídos a assignments — progressão dentro de uma faixa salarial.
**Módulo:** HCM - Core HR
**Uso típico:** Análise de progressão salarial.

### PER_ASSIGN_WORK_MEASURES_F
**Descrição:** Medidas de trabalho por assignment (FTE, headcount, horas).
**Módulo:** HCM - Core HR
**Uso típico:** Cálculo de FTE e headcount.

### PER_CALENDAR_EVENTS
**Descrição:** Eventos de calendário de HR (feriados, datas especiais).
**Módulo:** HCM - Core HR
**Uso típico:** Calendário corporativo.

### PER_CALENDAR_EVENTS_TL
**Descrição:** Traduções dos eventos de calendário.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_CHECKLISTS_B
**Descrição:** Definições de checklists (onboarding, offboarding, transferência).
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Configuração de checklists.

### PER_CHECKLISTS_TL
**Descrição:** Traduções dos checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Suporte multilíngue.

### PER_CHECKLIST_CONTACTS
**Descrição:** Contatos definidos em checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Responsáveis padrão.

### PER_CHECKLIST_CONTENTS
**Descrição:** Conteúdo/itens dos checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Definição de itens.

### PER_CHK_CONTENT_DEFNS_B
**Descrição:** Definições de conteúdo de checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Configuração de templates.

### PER_CHK_CONTENT_DEFNS_TL
**Descrição:** Traduções das definições de conteúdo.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Suporte multilíngue.

### PER_CITIZENSHIPS
**Descrição:** Cidadanias/nacionalidades dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Dados de nacionalidade; compliance de visto.

### PER_COL_AGREEMENTS_F
**Descrição:** Acordos coletivos (convenções coletivas de trabalho).
**Módulo:** HCM - Core HR
**Uso típico:** Vinculação de colaboradores a convenções coletivas.

### PER_COL_AGREEMENTS_F_TL
**Descrição:** Traduções dos acordos coletivos.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_CONTACT_RELSHIPS_F
**Descrição:** **Relacionamentos de contato** — dependentes, cônjuges, contatos de emergência e beneficiários vinculados a colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Extração de dependentes; benefícios; contatos de emergência.

### PER_CONTRACTS_F
**Descrição:** **Contratos de trabalho** — define termos contratuais (tipo, duração, data início/fim, renovações).
**Módulo:** HCM - Core HR
**Uso típico:** Gestão de contratos; relatórios de vencimento; compliance trabalhista.

### PER_DEPT_TREE_NODE
**Descrição:** Nós da árvore departamental — hierarquia de departamentos.
**Módulo:** HCM - Core HR
**Uso típico:** Construção de organogramas.

### PER_DEPT_TREE_NODE_CF
**Descrição:** Versão cross-functional da árvore departamental.
**Módulo:** HCM - Core HR
**Uso típico:** Hierarquia departamental entre BUs.

### PER_DEPT_TREE_NODE_RF
**Descrição:** Versão row-flattened da árvore departamental.
**Módulo:** HCM - Core HR
**Uso típico:** Navegação de hierarquia departamental.

### PER_DISABILITIES_F
**Descrição:** Registro de deficiências/necessidades especiais dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Compliance de acessibilidade; cotas de PcD.

### PER_DRIVERS_LICENSES
**Descrição:** Carteiras de habilitação dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Gestão de documentos; requisitos de cargo.

### PER_DRIVERS_LICENSE_TYPES
**Descrição:** Tipos de carteira de habilitação.
**Módulo:** HCM - Core HR
**Uso típico:** Referência de tipos de CNH.

### PER_EMAIL_ADDRESSES
**Descrição:** **Endereços de e-mail** dos colaboradores (corporativo, pessoal).
**Módulo:** HCM - Core HR
**Uso típico:** Comunicação; diretório de colaboradores.

### PER_ETHNICITIES
**Descrição:** Dados de etnia/raça dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Relatórios de diversidade; compliance regulatório.

### PER_EXT_APP_IDENTIFIERS
**Descrição:** Identificadores de aplicações externas — IDs em sistemas externos vinculados a pessoas.
**Módulo:** HCM - Core HR
**Uso típico:** Integração com sistemas externos.

### PER_GRADES_F
**Descrição:** **Grades (níveis/faixas salariais)** — define faixas de remuneração aplicáveis a cargos e posições.
**Módulo:** HCM - Core HR
**Uso típico:** Referência de grades para análise salarial; estrutura de remuneração.

### PER_GRADES_F_TL
**Descrição:** Traduções dos nomes de grades.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_GRADES_IN_LADDERS_F
**Descrição:** Grades dentro de escadas de progressão (grade ladders).
**Módulo:** HCM - Core HR
**Uso típico:** Configuração de progressão salarial.

### PER_GRADE_LADDERS_F
**Descrição:** Escadas de progressão de grades — define sequências de grades para progressão de carreira.
**Módulo:** HCM - Core HR
**Uso típico:** Planos de carreira e progressão salarial.

### PER_GRADE_LADDERS_F_TL
**Descrição:** Traduções das escadas de progressão.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_GRADE_STEPS_F
**Descrição:** Steps dentro de grades — subdivisões de uma grade para progressão incremental.
**Módulo:** HCM - Core HR
**Uso típico:** Progressão step-by-step dentro de faixas.

### PER_GRADE_STEPS_F_TL
**Descrição:** Traduções dos steps de grade.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_JOBS_F
**Descrição:** **Tabela principal de cargos (jobs)** — define todos os cargos da organização com família de cargo, código e atributos. Cargo é genérico (ex.: "Analista de Sistemas") vs. posição que é específica.
**Módulo:** HCM - Core HR
**Uso típico:** Referência de cargos; dimensão de cargo em relatórios; estrutura organizacional.

### PER_JOBS_F_TL
**Descrição:** Traduções dos nomes de cargos.
**Módulo:** HCM - Core HR
**Uso típico:** Nomes de cargos em múltiplos idiomas.

### PER_JOB_EVALUATIONS
**Descrição:** Avaliações de cargos — pontuação e classificação de cargos para fins de remuneração.
**Módulo:** HCM - Core HR
**Uso típico:** Job evaluation (Hay, Mercer, etc.).

### PER_JOB_EXTRA_INFO_F
**Descrição:** Informações extras de cargos — campos customizados (EIT) de cargos.
**Módulo:** HCM - Core HR
**Uso típico:** Atributos adicionais de cargos.

### PER_JOB_FAMILY_F
**Descrição:** **Famílias de cargo** — agrupamento de cargos similares (ex.: TI, Finanças, Operações).
**Módulo:** HCM - Core HR
**Uso típico:** Classificação funcional de cargos; relatórios por família.

### PER_JOB_FAMILY_F_TL
**Descrição:** Traduções das famílias de cargo.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_JOB_LEG_F
**Descrição:** Dados legislativos de cargos — informações específicas por legislação (CBO, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Compliance legislativo de cargos.

### PER_LEGISLATIVE_DATA_GROUPS
**Descrição:** **Grupos de dados legislativos (LDG)** — define o contexto legislativo/legal para processamento de dados de pessoas (país, moeda, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Segmentação por legislação; fundamental para payroll.

### PER_LEGISLATIVE_DATA_GROUPS_TL
**Descrição:** Traduções dos LDGs.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_LOCATIONS
**Descrição:** **Localizações** — tabela principal de locais de trabalho (escritórios, fábricas, filiais) com endereço completo.
**Módulo:** HCM - Core HR
**Uso típico:** Referência de localização; dimensão geográfica em relatórios.

### PER_LOCATION_DETAILS_F
**Descrição:** Detalhes de localizações com data efetiva.
**Módulo:** HCM - Core HR
**Uso típico:** Atributos adicionais de locais.

### PER_LOCATION_DETAILS_F_TL
**Descrição:** Traduções dos detalhes de localizações.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_LOCATION_DETAILS_F_VL
**Descrição:** View de detalhes de localizações com tradução.
**Módulo:** HCM - Core HR
**Uso típico:** Consulta consolidada.

### PER_LOC_ADDRESS_USAGES_F
**Descrição:** Usos de endereço de localizações.
**Módulo:** HCM - Core HR
**Uso típico:** Tipos de endereço por localização.

### PER_MANAGER_HRCHY_CF
**Descrição:** Hierarquia de gestores — versão cross-functional com todos os níveis de gestão.
**Módulo:** HCM - Core HR
**Uso típico:** Construção de árvores de gestão; aprovações em cadeia.

### PER_MANAGER_HRCHY_DN
**Descrição:** Hierarquia de gestores denormalizada — facilita consultas de subordinados em todos os níveis.
**Módulo:** HCM - Core HR
**Uso típico:** Relatórios de hierarquia; contagem de subordinados.

### PER_MANAGER_HRCHY_REPORTEES_DN
**Descrição:** Reportees da hierarquia de gestores denormalizada — lista de todos os subordinados diretos e indiretos.
**Módulo:** HCM - Core HR
**Uso típico:** Extração de equipes completas.

### PER_NATIONAL_IDENTIFIERS
**Descrição:** **Identificadores nacionais** — CPF, RG, NIS/PIS e outros documentos de identificação por país.
**Módulo:** HCM - Core HR
**Uso típico:** Identificação legal; compliance; integração com governo.

### PER_ORG_TREE_NODE_CF
**Descrição:** Nós da árvore organizacional — versão cross-functional.
**Módulo:** HCM - Core HR
**Uso típico:** Hierarquia organizacional.

### PER_ORG_TREE_NODE_RF
**Descrição:** Nós da árvore organizacional — versão row-flattened.
**Módulo:** HCM - Core HR
**Uso típico:** Navegação de hierarquia.

### PER_PASSPORTS
**Descrição:** Passaportes dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Gestão de documentos de viagem; compliance de expatriados.

### PER_PEOPLE_LEGISLATIVE_F
**Descrição:** Dados legislativos por pessoa — informações específicas de legislação (raça, deficiência, veterano, etc. conforme país).
**Módulo:** HCM - Core HR
**Uso típico:** Compliance regulatório; relatórios legais.

### PER_PERIODS_OF_SERVICE
**Descrição:** **Períodos de serviço** — registra cada vínculo de emprego (data de admissão, data de desligamento, status). Pessoa pode ter múltiplos períodos.
**Módulo:** HCM - Core HR
**Uso típico:** Cálculo de tempo de casa; relatórios de turnover; histórico de vínculos.

### PER_PERSONS
**Descrição:** **Pessoas (tabela core)** — dados fundamentais da pessoa (person_id, data de nascimento, sexo, start_date).
**Módulo:** HCM - Core HR
**Uso típico:** Dados demográficos; chave para joins.

### PER_PERSON_ADDR_USAGES_F
**Descrição:** Usos de endereços por pessoa (residencial, correspondência, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Tipos de endereço por pessoa.

### PER_PERSON_DLVRY_METHODS
**Descrição:** Métodos de entrega de comunicação por pessoa (e-mail, correio, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Preferências de comunicação.

### PER_PERSON_NAMES_F
**Descrição:** **Nomes de pessoas** — nome completo com data efetiva, incluindo primeiro nome, sobrenome, nome do meio, title. Suporta múltiplos tipos de nome (legal, display, preferred).
**Módulo:** HCM - Core HR
**Uso típico:** Extração de nomes; diretório de colaboradores; relatórios de pessoas.

### PER_PERSON_NAMES_F_V
**Descrição:** View de nomes de pessoas — facilita consulta de nomes com formatação.
**Módulo:** HCM - Core HR
**Uso típico:** Consulta rápida de nomes.

### PER_PERSON_TYPES
**Descrição:** Tipos de pessoa (empregado, contingente, candidato, contato, etc.).
**Módulo:** HCM - Core HR
**Uso típico:** Classificação de pessoas.

### PER_PERSON_TYPES_TL
**Descrição:** Traduções dos tipos de pessoa.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_PERSON_TYPE_USAGES_M
**Descrição:** Usos de tipos de pessoa — materializada; registra quais tipos estão ativos para cada pessoa ao longo do tempo.
**Módulo:** HCM - Core HR
**Uso típico:** Segmentação de pessoas por tipo ativo.

### PER_PHONES
**Descrição:** **Telefones** dos colaboradores (celular, residencial, comercial).
**Módulo:** HCM - Core HR
**Uso típico:** Dados de contato; diretório.

### PER_POSITION_HIERARCHY_F
**Descrição:** Hierarquia de posições — define subordinação entre posições.
**Módulo:** HCM - Core HR
**Uso típico:** Organograma por posição.

### PER_POSITION_HRCHY_RF
**Descrição:** Hierarquia de posições — versão row-flattened.
**Módulo:** HCM - Core HR
**Uso típico:** Navegação de hierarquia.

### PER_POSITION_LEG_F
**Descrição:** Dados legislativos de posições.
**Módulo:** HCM - Core HR
**Uso típico:** Compliance legislativo.

### PER_POS_FUNDING_POSITIONS_F
**Descrição:** Funding de posições — orçamento aprovado por posição.
**Módulo:** HCM - Core HR
**Uso típico:** Controle orçamentário de headcount.

### PER_POS_HRCHY_TOPDOWN_RF_CF_V
**Descrição:** View de hierarquia de posições top-down (row-flattened, cross-functional).
**Módulo:** HCM - Core HR
**Uso típico:** Navegação completa de hierarquia.

### PER_POS_TREE_NODE_CF
**Descrição:** Nós da árvore de posições — versão cross-functional.
**Módulo:** HCM - Core HR
**Uso típico:** Hierarquia de posições.

### PER_RATES_F
**Descrição:** Taxas/valores de referência — define rates associados a grades, steps ou cargos.
**Módulo:** HCM - Core HR
**Uso típico:** Valores de referência salarial.

### PER_RATES_F_TL
**Descrição:** Traduções das taxas.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_RATE_VALUES_F
**Descrição:** Valores das taxas — amounts efetivos por rate.
**Módulo:** HCM - Core HR
**Uso típico:** Valores de referência salarial.

### PER_RELIGIONS
**Descrição:** Religião/crença dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Dados demográficos opcionais.

### PER_REQUISITIONS_INTERFACE_B
**Descrição:** Interface de requisições de pessoal — dados de requisições importados via integração.
**Módulo:** HCM - Core HR
**Uso típico:** Integração de requisições.

### PER_REQUISITIONS_INTERFACE_TL
**Descrição:** Traduções da interface de requisições.
**Módulo:** HCM - Core HR
**Uso típico:** Suporte multilíngue.

### PER_RESOURCE_EXCEPTIONS
**Descrição:** Exceções de recursos — exceções ao calendário padrão de trabalho.
**Módulo:** HCM - Core HR
**Uso típico:** Feriados e exceções de calendário.

### PER_ROLES_DN_VL
**Descrição:** View denormalizada de roles/papéis de pessoa.
**Módulo:** HCM - Core HR
**Uso típico:** Consulta de papéis atribuídos.

### PER_SCHEDULE_ASSIGNMENTS
**Descrição:** Atribuições de escalas de trabalho a colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Vinculação de escalas a pessoas.

### PER_SCHEDULE_EXCEPTIONS
**Descrição:** Exceções a escalas de trabalho.
**Módulo:** HCM - Core HR
**Uso típico:** Alterações pontuais em escalas.

### PER_TASKS_IN_CHECKLIST_B
**Descrição:** Tarefas definidas em checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Definição de tarefas.

### PER_TASKS_IN_CHECKLIST_TL
**Descrição:** Traduções das tarefas de checklist.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Suporte multilíngue.

### PER_TASK_DEPENDENCIES
**Descrição:** Dependências entre tarefas de checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Sequenciamento de tarefas.

### PER_TASK_NOTIFICATIONS
**Descrição:** Notificações de tarefas de checklists.
**Módulo:** HCM - Core HR / Checklists
**Uso típico:** Configuração de alertas.

### PER_USERS
**Descrição:** Usuários do sistema HR — vincula pessoa a conta de usuário.
**Módulo:** HCM - Core HR / Security
**Uso típico:** Gestão de acessos; auditoria.

### PER_USER_HISTORY
**Descrição:** Histórico de usuários — log de alterações em contas de usuário.
**Módulo:** HCM - Core HR / Security
**Uso típico:** Auditoria de acessos.

### PER_USER_ROLES
**Descrição:** Papéis/roles atribuídos a usuários — permissões de segurança.
**Módulo:** HCM - Core HR / Security
**Uso típico:** Gestão de permissões; auditoria de acessos.

### PER_VALID_GRADES_F
**Descrição:** Grades válidas por cargo/posição — define quais grades são permitidas para cada combinação.
**Módulo:** HCM - Core HR
**Uso típico:** Validação de atribuição de grade.

### PER_VISAS_PERMITS_F
**Descrição:** Vistos e permissões de trabalho dos colaboradores.
**Módulo:** HCM - Core HR
**Uso típico:** Gestão de expatriados; compliance de imigração.

### PER_WORKING_HOUR_PATTERNS_F
**Descrição:** Padrões de horário de trabalho — define jornadas (ex.: 8h/dia, 40h/semana, escalas alternadas).
**Módulo:** HCM - Core HR
**Uso típico:** Configuração de jornadas; cálculo de FTE.

---

## 29. Aprendizado / Learning (WLF)

Tabelas do módulo **Learning (Oracle Learning Cloud)** — cursos, planos de aprendizado, inscrições e conteúdo.

### WLF_AR_RELATIONS_F
**Descrição:** Relações de registros de atribuição no módulo de Learning.
**Módulo:** HCM - Learning
**Uso típico:** Vinculação entre objetos de aprendizado.

### WLF_ASSIGNMENT_DESTINATIONS_F
**Descrição:** Destinos de atribuições de aprendizado — onde os resultados são registrados.
**Módulo:** HCM - Learning
**Uso típico:** Configuração de destinos.

### WLF_ASSIGNMENT_RECORDS_F
**Descrição:** Registros de atribuições de aprendizado por colaborador.
**Módulo:** HCM - Learning
**Uso típico:** Extração de inscrições em treinamentos.

### WLF_ASSIGNMENT_RULES
**Descrição:** Regras de atribuição automática de treinamentos.
**Módulo:** HCM - Learning
**Uso típico:** Configuração de treinamentos obrigatórios.

### WLF_ASSIGNMENT_TASKS_F
**Descrição:** Tarefas de atribuição de aprendizado.
**Módulo:** HCM - Learning
**Uso típico:** Acompanhamento de tarefas.

### WLF_BI_ANALYSIS_DESTINATIONS
**Descrição:** Destinos de análise BI para Learning.
**Módulo:** HCM - Learning
**Uso típico:** Configuração de analytics.

### WLF_EVENT_ASSIGNMENTS_F
**Descrição:** Atribuições de eventos de aprendizado — inscrição de colaboradores em eventos/turmas.
**Módulo:** HCM - Learning
**Uso típico:** Gestão de inscrições.

### WLF_EVENT_ASSIGNMENTS_F_TL
**Descrição:** Traduções das atribuições de eventos.
**Módulo:** HCM - Learning
**Uso típico:** Suporte multilíngue.

### WLF_EVENT_ATTEMPTS
**Descrição:** Tentativas de eventos de aprendizado — registra cada tentativa de conclusão.
**Módulo:** HCM - Learning
**Uso típico:** Rastreamento de progresso.

### WLF_EVENT_INCIDENTS
**Descrição:** Incidentes em eventos de aprendizado.
**Módulo:** HCM - Learning
**Uso típico:** Registro de ocorrências.

### WLF_EVENT_SOCIAL
**Descrição:** Interações sociais em eventos de aprendizado (comentários, curtidas).
**Módulo:** HCM - Learning
**Uso típico:** Engajamento social.

### WLF_LEARNING_ITEMS_F
**Descrição:** **Itens de aprendizado** — tabela principal de conteúdo de aprendizado (cursos, certificações, programas).
**Módulo:** HCM - Learning
**Uso típico:** Catálogo de treinamentos; relatórios de oferta de L&D.

### WLF_LEARNING_ITEMS_F_TL
**Descrição:** Traduções dos itens de aprendizado.
**Módulo:** HCM - Learning
**Uso típico:** Catálogo multilíngue.

### WLF_LEARNING_PLANS_F
**Descrição:** **Planos de aprendizado** — trilhas/programas estruturados de desenvolvimento com sequência de cursos.
**Módulo:** HCM - Learning
**Uso típico:** Gestão de trilhas de desenvolvimento.

### WLF_LI_ACTIVITIES_F
**Descrição:** Atividades de itens de aprendizado.
**Módulo:** HCM - Learning
**Uso típico:** Componentes de cursos.

### WLF_LI_CLASSES_F
**Descrição:** Classes/turmas de itens de aprendizado — sessões específicas (presencial com data/local).
**Módulo:** HCM - Learning
**Uso típico:** Gestão de turmas; calendário de treinamentos.

### WLF_LI_CONTENT_F
**Descrição:** Conteúdo de itens de aprendizado — materiais, links, documentos associados.
**Módulo:** HCM - Learning
**Uso típico:** Gestão de conteúdo de cursos.

### WLF_LI_COURSES_F
**Descrição:** Cursos — detalhes específicos de cursos dentro dos itens de aprendizado.
**Módulo:** HCM - Learning
**Uso típico:** Catálogo de cursos.

### WLF_LI_ELEARNINGS_F
**Descrição:** E-learnings — conteúdo online/digital.
**Módulo:** HCM - Learning
**Uso típico:** Gestão de conteúdo digital.

### WLF_LI_HIERARCHIES_F
**Descrição:** Hierarquias de itens de aprendizado — relações entre cursos e programas.
**Módulo:** HCM - Learning
**Uso típico:** Estrutura de programas de treinamento.

### WLF_PLAN_PROFILES_F
**Descrição:** Perfis de planos de aprendizado — critérios de elegibilidade.
**Módulo:** HCM - Learning
**Uso típico:** Configuração de elegibilidade.

### WLF_PLAN_RECORDS_F
**Descrição:** Registros de planos de aprendizado por colaborador — progresso em trilhas.
**Módulo:** HCM - Learning
**Uso típico:** Acompanhamento de progresso em trilhas.

### WLF_PRICING_COMPONENTS_F
**Descrição:** Componentes de preço de treinamentos.
**Módulo:** HCM - Learning
**Uso típico:** Gestão de custos de treinamento.

### WLF_PRICING_RULES_F
**Descrição:** Regras de precificação de treinamentos.
**Módulo:** HCM - Learning
**Uso típico:** Configuração de preços.

### WLF_REQUEST_DETAILS
**Descrição:** Detalhes de solicitações de treinamento.
**Módulo:** HCM - Learning
**Uso típico:** Workflow de solicitação de treinamento.

### WLF_RESOURCES_B
**Descrição:** Recursos de treinamento (instrutores, salas, equipamentos).
**Módulo:** HCM - Learning
**Uso típico:** Gestão de recursos de L&D.

### WLF_RESOURCES_TL
**Descrição:** Traduções dos recursos de treinamento.
**Módulo:** HCM - Learning
**Uso típico:** Suporte multilíngue.

---

## 30. Entidades Legais (XLE)

### XLE_ENTITY_PROFILES
**Descrição:** Perfis de entidades legais — dados de pessoas jurídicas (CNPJ, registro, endereço legal).
**Módulo:** Foundation / Legal Entity
**Uso típico:** Referência de entidades legais; relatórios legais e fiscais.

---

## 31. Escalas e Padrões de Trabalho (ZMM)

Tabelas de **Schedule/Shift Management** — definição de padrões e escalas de trabalho.

### ZMM_SR_PATTERNS_B
**Descrição:** Padrões de escala de trabalho — define sequências de turnos (ex.: 5x2, 6x1, 12x36).
**Módulo:** HCM - Scheduling
**Uso típico:** Configuração de padrões de escala.

### ZMM_SR_PATTERNS_TL
**Descrição:** Traduções dos padrões de escala.
**Módulo:** HCM - Scheduling
**Uso típico:** Suporte multilíngue.

### ZMM_SR_PATTERN_DTLS
**Descrição:** Detalhes dos padrões de escala — dias e turnos específicos dentro de cada padrão.
**Módulo:** HCM - Scheduling
**Uso típico:** Configuração detalhada de escalas.

### ZMM_SR_SCHEDULES_B
**Descrição:** Escalas de trabalho — definição de schedules que utilizam os padrões.
**Módulo:** HCM - Scheduling
**Uso típico:** Cadastro de escalas de trabalho.

### ZMM_SR_SCHEDULES_TL
**Descrição:** Traduções das escalas de trabalho.
**Módulo:** HCM - Scheduling
**Uso típico:** Suporte multilíngue.

---

## Referência Rápida — Tabelas Mais Importantes

| Tabela | Área | Descrição Resumida |
|--------|------|--------------------|
| `PER_ALL_PEOPLE_F` | Core HR | Todas as pessoas (empregados, candidatos, contatos) |
| `PER_ALL_ASSIGNMENTS_M` | Core HR | Todos os vínculos de trabalho (assignments) |
| `PER_PERSON_NAMES_F` | Core HR | Nomes das pessoas (legal, display, preferred) |
| `PER_PERSONS` | Core HR | Dados fundamentais da pessoa |
| `PER_PERIODS_OF_SERVICE` | Core HR | Períodos de emprego (admissão/desligamento) |
| `PER_ADDRESSES_F` | Core HR | Endereços residenciais |
| `PER_EMAIL_ADDRESSES` | Core HR | E-mails dos colaboradores |
| `PER_PHONES` | Core HR | Telefones dos colaboradores |
| `PER_NATIONAL_IDENTIFIERS` | Core HR | CPF, RG e documentos nacionais |
| `PER_CONTACT_RELSHIPS_F` | Core HR | Dependentes e contatos |
| `PER_JOBS_F` | Core HR | Cargos (jobs) |
| `PER_JOB_FAMILY_F` | Core HR | Famílias de cargo |
| `PER_GRADES_F` | Core HR | Grades/faixas salariais |
| `PER_LOCATIONS` | Core HR | Localizações/locais de trabalho |
| `PER_CONTRACTS_F` | Core HR | Contratos de trabalho |
| `HR_ALL_ORGANIZATION_UNITS_F` | Organizations | Estrutura organizacional |
| `HR_ALL_POSITIONS_F` | Positions | Posições |
| `CMP_SALARY` | Compensation | Salários |
| `PAY_ALL_PAYROLLS_F` | Payroll | Folhas de pagamento |
| `PAY_ELEMENT_ENTRIES_F` | Payroll | Lançamentos de elementos de folha |
| `PAY_RUN_RESULTS` | Payroll | Resultados de processamento de folha |
| `PAY_PAY_RELATIONSHIPS_F` | Payroll | Relações de folha de pagamento |
| `IRC_REQUISITIONS_B` | Recruiting | Requisições de vaga |
| `IRC_CANDIDATES` | Recruiting | Candidatos |
| `IRC_SUBMISSIONS` | Recruiting | Candidaturas |
| `IRC_OFFERS` | Recruiting | Ofertas de emprego |
| `BEN_PL_F` | Benefits | Planos de benefícios |
| `BEN_PRTT_ENRT_RSLT` | Benefits | Enrollment de benefícios |
| `ANC_PER_ABS_ENTRIES` | Absences | Registros de ausência |
| `HRA_EVALUATIONS` | Performance | Avaliações de desempenho |
| `HRG_GOALS` | Goals | Metas |
| `WLF_LEARNING_ITEMS_F` | Learning | Itens de aprendizado |
| `HRT_PROFILES_B` | Talent | Perfis de talento |

---

> **Nota:** Tabelas com sufixo `_TL` contêm traduções multilíngues; `_VL` são views com tradução; `_B` são tabelas base; `_F` são date-effective (data efetiva); `_M` são materializadas; `_DN` são denormalizadas para performance; `_CF` são cross-functional; `_RF` são row-flattened.
