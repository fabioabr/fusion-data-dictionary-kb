# Oracle Fusion — Purchasing (PO) — Database Tables

> Referência de tabelas do módulo PO extraídas do BICC Database Mapping (Release 13/25A).
> Fonte: documentação oficial Oracle Fusion Cloud ERP.
> Total: **201 tabelas** mapeadas.

---

## Índice de Grupos

1. [Pedidos de Compra (PO Core)](#1-pedidos-de-compra-po-core)
2. [Linhas e Distribuições de PO](#2-linhas-e-distribuições-de-po)
3. [PO Draft (Rascunhos)](#3-po-draft-rascunhos)
4. [PO Archive e Versionamento](#4-po-archive-e-versionamento)
5. [Tipos de Documento e Estilos de PO](#5-tipos-de-documento-e-estilos-de-po)
6. [Configurações e Parâmetros de PO](#6-configurações-e-parâmetros-de-po)
7. [Approved Supplier List (ASL)](#7-approved-supplier-list-asl)
8. [Agentes de Compra e Atribuições](#8-agentes-de-compra-e-atribuições)
9. [Histórico de Ações de PO](#9-histórico-de-ações-de-po)
10. [Requisições (POR)](#10-requisições-por)
11. [Negociações e Sourcing (PON)](#11-negociações-e-sourcing-pon)
12. [Qualificação de Fornecedores (POQ)](#12-qualificação-de-fornecedores-poq)
13. [Fornecedores (POZ)](#13-fornecedores-poz)
14. [Registros e Solicitações de Fornecedores (POZ)](#14-registros-e-solicitações-de-fornecedores-poz)
15. [Acesso de Fornecedores (POS)](#15-acesso-de-fornecedores-pos)
16. [Contas a Pagar — Referência Cruzada (AP)](#16-contas-a-pagar--referência-cruzada-ap)
17. [Catálogo de Produtos (EGP)](#17-catálogo-de-produtos-egp)
18. [Idiomas e Territórios (FND)](#18-idiomas-e-territórios-fnd)
19. [Acordos e Business Units (FOS/FUN)](#19-acordos-e-business-units-fosfun)
20. [Contabilidade e Ledger (GL)](#20-contabilidade-e-ledger-gl)
21. [Organizações e Locais (HR)](#21-organizações-e-locais-hr)
22. [Terceiros e Endereços (HZ — TCA)](#22-terceiros-e-endereços-hz--tca)
23. [Pagamentos (IBY)](#23-pagamentos-iby)
24. [Inventário e Unidades de Medida (INV)](#24-inventário-e-unidades-de-medida-inv)
25. [Pessoas e Atribuições (PER)](#25-pessoas-e-atribuições-per)
26. [Tributação (ZX)](#26-tributação-zx)

---

## 1. Pedidos de Compra (PO Core)

### PO_HEADERS_ALL
**Descrição:** Tabela principal de cabeçalhos de pedidos de compra (Purchase Orders). Armazena informações como número do PO, fornecedor, moeda, termos de pagamento, status de aprovação, tipo de documento (standard, blanket, contract, planned) e datas de criação/aprovação.
**Módulo:** Purchasing
**Uso típico:** Extração de todos os pedidos de compra para análise de spend, relatórios de compras e integração com sistemas externos.

### PO_GA_ORG_ASSIGNMENTS
**Descrição:** Armazena as atribuições de organizações autorizadas a utilizar um Global Agreement (contrato blanket global). Define quais business units podem fazer releases contra um contrato corporativo.
**Módulo:** Purchasing
**Uso típico:** Análise de contratos globais e quais organizações estão habilitadas para utilizá-los.

### PO_NOTIFICATION_CONTROLS
**Descrição:** Define as regras de controle de notificações para processos de compras, como alertas de aprovação, expiração de contratos e recebimento pendente.
**Módulo:** Purchasing
**Uso típico:** Configuração e auditoria de notificações automáticas do módulo de compras.

### PO_SYSTEM_PARAMETERS_ALL
**Descrição:** Armazena os parâmetros de sistema do módulo de Purchasing por business unit, incluindo configurações de numeração automática, regras de aprovação, tolerâncias de recebimento e políticas de matching.
**Módulo:** Purchasing
**Uso típico:** Consulta de configurações operacionais do módulo PO por unidade de negócio.

---

## 2. Linhas e Distribuições de PO

### PO_LINES_ALL
**Descrição:** Contém as linhas dos pedidos de compra, com detalhes de item, descrição, quantidade, preço unitário, categoria e tipo de linha. Cada linha está vinculada a um cabeçalho em PO_HEADERS_ALL.
**Módulo:** Purchasing
**Uso típico:** Análise detalhada de itens comprados, volumes, preços e categorias de gasto.

### PO_LINE_LOCATIONS_ALL
**Descrição:** Armazena os schedules (programações de entrega) das linhas de PO, incluindo local de entrega (ship-to), data prometida, quantidade solicitada vs. recebida, e informações de matching para faturamento.
**Módulo:** Purchasing
**Uso típico:** Rastreamento de entregas, análise de on-time delivery e conciliação com recebimentos.

### PO_DISTRIBUTIONS_ALL
**Descrição:** Contém as distribuições contábeis das linhas de PO, com informações de centro de custo, projeto, conta contábil (charge account), quantidade distribuída e valores encumbrados.
**Módulo:** Purchasing
**Uso típico:** Integração contábil, análise de encumbrances e rastreamento de alocação orçamentária.

### PO_ORIG_LINE_LOCATIONS_ALL_V
**Descrição:** View que apresenta os dados originais dos schedules de linha de PO antes de alterações/revisões, útil para rastreamento de mudanças.
**Módulo:** Purchasing
**Uso típico:** Auditoria de alterações em schedules e comparação entre versão original e versão atual do pedido.

---

## 3. PO Draft (Rascunhos)

### PO_HEADERS_DRAFT_ALL
**Descrição:** Armazena cabeçalhos de pedidos de compra em estado de rascunho (draft), antes da submissão para aprovação. Estrutura idêntica a PO_HEADERS_ALL, porém para documentos ainda não finalizados.
**Módulo:** Purchasing
**Uso típico:** Monitoramento de POs em elaboração e pipeline de compras pendentes de aprovação.

### PO_LINES_DRAFT_ALL
**Descrição:** Contém as linhas de pedidos de compra em rascunho, vinculadas aos cabeçalhos em PO_HEADERS_DRAFT_ALL.
**Módulo:** Purchasing
**Uso típico:** Análise de itens em processo de compra ainda não aprovados.

### PO_LINE_LOCATIONS_DRAFT_ALL
**Descrição:** Schedules de entrega dos POs em rascunho, com locais de entrega e quantidades planejadas.
**Módulo:** Purchasing
**Uso típico:** Visibilidade de entregas planejadas em pedidos ainda não finalizados.

### PO_DISTRIBUTIONS_DRAFT_ALL
**Descrição:** Distribuições contábeis de POs em rascunho, incluindo contas de encargo e alocação orçamentária provisória.
**Módulo:** Purchasing
**Uso típico:** Planejamento orçamentário de compras em elaboração.

---

## 4. PO Archive e Versionamento

### PO_HEADERS_ARCHIVE_ALL
**Descrição:** Armazena versões arquivadas dos cabeçalhos de PO. Cada revisão ou alteração significativa gera um registro de arquivo para manter o histórico completo de mudanças.
**Módulo:** Purchasing
**Uso típico:** Auditoria de versões anteriores de pedidos de compra e rastreamento de alterações contratuais.

### PO_VERSIONS
**Descrição:** Registra as versões de documentos de compra, incluindo número da versão, data de criação e status de cada revisão.
**Módulo:** Purchasing
**Uso típico:** Controle de versionamento de POs e contratos, auditoria de histórico de revisões.

### PO_VERSIONS_INIT_SEQUENCE_V
**Descrição:** View que exibe a sequência inicial de versionamento dos documentos de compra, facilitando a identificação da primeira versão.
**Módulo:** Purchasing
**Uso típico:** Consulta da versão original de um documento de compra.

### PO_VERSIONS_UNPROCESSED_V
**Descrição:** View que lista versões de PO que ainda não foram processadas, útil para identificar documentos pendentes de sincronização ou workflow.
**Módulo:** Purchasing
**Uso típico:** Monitoramento de versões pendentes de processamento em integrações.

---

## 5. Tipos de Documento e Estilos de PO

### PO_DOCUMENT_TYPES_ALL_B
**Descrição:** Tabela base que define os tipos de documento de compra (Standard PO, Blanket Purchase Agreement, Contract Purchase Agreement, Planned PO) por business unit.
**Módulo:** Purchasing
**Uso típico:** Configuração e consulta dos tipos de documento habilitados por organização.

### PO_DOCUMENT_TYPES_ALL_TL
**Descrição:** Tabela de tradução dos tipos de documento de compra, com nomes e descrições em múltiplos idiomas.
**Módulo:** Purchasing
**Uso típico:** Suporte multilíngue para tipos de documento de PO.

### PO_DOCUMENT_TYPES_VL
**Descrição:** View combinada (base + tradução) dos tipos de documento de compra, retornando dados no idioma da sessão do usuário.
**Módulo:** Purchasing
**Uso típico:** Consulta simplificada dos tipos de documento com descrições traduzidas.

### PO_DOC_STYLE_HEADERS
**Descrição:** Define os estilos de documento de compra (Document Styles), que controlam o comportamento e os campos disponíveis em cada tipo de PO (ex.: estilo para compras de serviço vs. materiais).
**Módulo:** Purchasing
**Uso típico:** Configuração de estilos personalizados de documentos de compra.

### PO_DOC_STYLE_LINES_B
**Descrição:** Tabela base que define os estilos de linha de documento, controlando quais campos e comportamentos são habilitados no nível de linha para cada estilo de documento.
**Módulo:** Purchasing
**Uso típico:** Personalização granular de linhas de PO por estilo.

### PO_DOC_STYLE_LINES_TL
**Descrição:** Tradução dos estilos de linha de documento de compra.
**Módulo:** Purchasing
**Uso típico:** Suporte multilíngue para estilos de linha.

### PO_DOC_STYLE_LINES_VL
**Descrição:** View combinada dos estilos de linha de documento (base + tradução).
**Módulo:** Purchasing
**Uso típico:** Consulta de estilos de linha com descrições traduzidas.

### PO_LINE_TYPES_B
**Descrição:** Tabela base que define os tipos de linha de PO (Goods, Services, Fixed Price, Amount, Rate), controlando o comportamento de cada tipo quanto a recebimento, matching e faturamento.
**Módulo:** Purchasing
**Uso típico:** Configuração de tipos de linha e suas regras de processamento.

### PO_LINE_TYPES_TL
**Descrição:** Tradução dos tipos de linha de PO em múltiplos idiomas.
**Módulo:** Purchasing
**Uso típico:** Suporte multilíngue para tipos de linha de compra.

### PO_LOOKUP_CODES
**Descrição:** Tabela de códigos de lookup específicos do módulo Purchasing, contendo listas de valores usadas em campos como status, tipo de documento, condições de pagamento, etc.
**Módulo:** Purchasing
**Uso típico:** Decodificação de campos codificados em tabelas de PO.

---

## 6. Configurações e Parâmetros de PO

### PO_ATTRIBUTE_VALUES
**Descrição:** Armazena valores de atributos descritivos flexíveis (DFF — Descriptive Flexfields) associados a entidades de compra. Permite extensão de dados customizados.
**Módulo:** Purchasing
**Uso típico:** Extração de campos customizados adicionados a POs, linhas ou distribuições.

### PO_ATTRIBUTE_VALUES_TLP
**Descrição:** Armazena traduções dos valores de atributos descritivos flexíveis de compra, permitindo valores multilíngues para campos customizados.
**Módulo:** Purchasing
**Uso típico:** Suporte multilíngue para campos customizados de PO.

### PO_HAZARD_CLASSES_B
**Descrição:** Tabela base que define classes de periculosidade (hazard classes) para itens comprados, conforme regulamentações de transporte e armazenamento.
**Módulo:** Purchasing
**Uso típico:** Classificação de materiais perigosos em pedidos de compra.

### PO_HAZARD_CLASSES_TL
**Descrição:** Tradução das classes de periculosidade em múltiplos idiomas.
**Módulo:** Purchasing
**Uso típico:** Suporte multilíngue para classes de periculosidade.

### PO_HAZARD_CLASSES_VL
**Descrição:** View combinada das classes de periculosidade (base + tradução).
**Módulo:** Purchasing
**Uso típico:** Consulta de classes de periculosidade com descrições traduzidas.

### PO_UN_NUMBERS_VL
**Descrição:** View que lista os números UN (United Nations) de classificação de materiais perigosos, utilizados em conformidade com regulamentações internacionais de transporte.
**Módulo:** Purchasing
**Uso típico:** Classificação de itens perigosos conforme padrão ONU.

---

## 7. Approved Supplier List (ASL)

### PO_APPROVED_SUPPLIER_LIST
**Descrição:** Lista de fornecedores aprovados (ASL) por item ou categoria, definindo quais fornecedores estão autorizados a fornecer determinados produtos ou serviços.
**Módulo:** Purchasing
**Uso típico:** Controle de sourcing — verificação de quais fornecedores estão homologados por item/categoria.

### PO_ASL_ATTRIBUTES
**Descrição:** Atributos detalhados da lista de fornecedores aprovados, incluindo regras de sourcing (ex.: business unit habilitada, tipo de release autorizado, faixa de preço acordada).
**Módulo:** Purchasing
**Uso típico:** Configuração de regras de sourcing automático e restrições de fornecimento.

### PO_ASL_STATUSES
**Descrição:** Define os possíveis status da lista de fornecedores aprovados (Approved, Debarred, New, etc.).
**Módulo:** Purchasing
**Uso típico:** Consulta e gestão do ciclo de vida de homologação de fornecedores.

---

## 8. Agentes de Compra e Atribuições

### PO_AGENTS_V
**Descrição:** View que lista os agentes de compra (buyers) cadastrados no sistema, com informações de nome, e-mail e organização.
**Módulo:** Purchasing
**Uso típico:** Identificação de compradores responsáveis por pedidos e contratos.

### PO_AGENT_ASSIGNMENTS
**Descrição:** Armazena as atribuições de agentes de compra a categorias de item ou commodities, definindo a responsabilidade de cada comprador.
**Módulo:** Purchasing
**Uso típico:** Gestão de responsabilidades de compra por categoria e análise de carga de trabalho dos compradores.

---

## 9. Histórico de Ações de PO

### PO_ACTION_HISTORY
**Descrição:** Registra o histórico completo de ações realizadas em documentos de compra, incluindo aprovações, rejeições, devoluções, cancelamentos e revisões, com data, usuário e comentários.
**Módulo:** Purchasing
**Uso típico:** Auditoria de workflow de aprovação, rastreamento de quem aprovou/rejeitou cada PO e quando.

---

## 10. Requisições (POR)

> Tabelas com prefixo **POR_** pertencem ao módulo de Self-Service Procurement / Requisitions, referenciadas no contexto de Purchasing.

### POR_REQUISITION_HEADERS_ALL
**Descrição:** Cabeçalhos de requisições de compra, contendo número da requisição, solicitante, status de aprovação, business unit e datas. A requisição é o documento de solicitação interna que pode originar um PO.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Análise de demanda interna, ciclo requisição-to-PO e tempo de atendimento.

### POR_REQUISITION_LINES_ALL
**Descrição:** Linhas de requisição de compra, com detalhes de item solicitado, quantidade, preço estimado, categoria e fornecedor sugerido.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Detalhamento de itens requisitados, análise de demanda por categoria.

### POR_REQ_DISTRIBUTIONS_ALL
**Descrição:** Distribuições contábeis das linhas de requisição, incluindo centro de custo, projeto e conta de encargo para cada linha requisitada.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Rastreamento de alocação orçamentária de requisições e integração contábil.

### POR_LINE_LOCATIONS_SUM_V
**Descrição:** View sumarizada das localizações de entrega das linhas de requisição, consolidando quantidades e valores por local de destino.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Análise de demanda por local de entrega.

### POR_BROWSE_CATEGORIES_TL
**Descrição:** Tradução das categorias de navegação do catálogo de compras self-service, permitindo browsing hierárquico de itens.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Suporte multilíngue para catálogo de compras.

### POR_BROWSE_CATEGORIES_VL
**Descrição:** View combinada das categorias de navegação do catálogo (base + tradução).
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Consulta de categorias de catálogo com descrições traduzidas.

### POR_ITEM_CAT_PARENT_LEVELS
**Descrição:** Define os níveis hierárquicos pai das categorias de item no catálogo de compras, permitindo navegação em árvore.
**Módulo:** Procurement (Self-Service Requisitions)
**Uso típico:** Construção de hierarquia de categorias para browsing e relatórios.

---

## 11. Negociações e Sourcing (PON)

> Tabelas com prefixo **PON_** pertencem ao módulo de Sourcing/Negotiations, referenciadas no contexto de Purchasing.

### PON_AUCTION_HEADERS_ALL
**Descrição:** Cabeçalhos de negociações (RFQ, RFI, Auction, Reverse Auction), contendo tipo de negociação, datas de abertura/encerramento, moeda, regras de licitação e status.
**Módulo:** Sourcing
**Uso típico:** Análise de eventos de sourcing, volume de negociações e ciclo de compras estratégicas.

### PON_AUCTION_ITEM_PRICES_ALL
**Descrição:** Itens/linhas das negociações com preços-alvo, quantidades, especificações e categorias. Cada linha representa um item sendo negociado.
**Módulo:** Sourcing
**Uso típico:** Detalhamento de itens em negociação, análise de preços-alvo vs. propostas.

### PON_AUCTION_ATTRIBUTES
**Descrição:** Atributos customizados definidos para linhas de negociação, permitindo solicitar informações adicionais dos fornecedores (ex.: prazo de garantia, certificações).
**Módulo:** Sourcing
**Uso típico:** Análise de requisitos técnicos e comerciais em negociações.

### PON_AUCTION_SECTIONS
**Descrição:** Define as seções de uma negociação, organizando os itens e atributos em grupos lógicos.
**Módulo:** Sourcing
**Uso típico:** Estruturação de negociações complexas com múltiplas seções.

### PON_ACKNOWLEDGEMENTS
**Descrição:** Registra os acknowledgements (confirmações de recebimento) enviados por fornecedores convidados para participar de negociações.
**Módulo:** Sourcing
**Uso típico:** Rastreamento de confirmações de participação em eventos de sourcing.

### PON_ACTION_HISTORY
**Descrição:** Histórico de ações em negociações, incluindo criação, publicação, extensão de prazo, adjudicação e cancelamento.
**Módulo:** Sourcing
**Uso típico:** Auditoria de workflow de negociações de sourcing.

### PON_BIDDING_PARTIES
**Descrição:** Lista de fornecedores convidados para participar de uma negociação, com status de convite e participação.
**Módulo:** Sourcing
**Uso típico:** Análise de participação de fornecedores em eventos de sourcing.

### PON_BID_HEADERS
**Descrição:** Cabeçalhos das propostas (bids/respostas) submetidas por fornecedores em negociações, com data de submissão, status e valores totais.
**Módulo:** Sourcing
**Uso típico:** Análise comparativa de propostas recebidas em negociações.

### PON_BID_ITEM_PRICES
**Descrição:** Preços propostos por fornecedores para cada item/linha de uma negociação, incluindo preço unitário, quantidade ofertada e condições.
**Módulo:** Sourcing
**Uso típico:** Comparação detalhada de preços entre fornecedores concorrentes.

### PON_BID_ATTRIBUTE_VALUES
**Descrição:** Valores dos atributos customizados informados pelos fornecedores em suas propostas (ex.: prazo de entrega, garantia).
**Módulo:** Sourcing
**Uso típico:** Avaliação técnica e comercial de propostas por atributo.

### PON_BID_PO_LINES
**Descrição:** Vinculação entre linhas de proposta adjudicada e linhas de PO geradas a partir da negociação.
**Módulo:** Sourcing
**Uso típico:** Rastreamento de award-to-PO, verificação de quais propostas geraram pedidos.

### PON_BID_PO_NUMBERS
**Descrição:** Números de PO gerados a partir de propostas adjudicadas em negociações.
**Módulo:** Sourcing
**Uso típico:** Vinculação direta entre negociação e pedido de compra resultante.

### PON_BID_REQUIREMENTS
**Descrição:** Requisitos obrigatórios definidos na negociação que devem ser atendidos pelos fornecedores em suas propostas.
**Módulo:** Sourcing
**Uso típico:** Gestão de requisitos mandatórios em processos de sourcing.

### PON_BID_REQUIREMENT_VALUES
**Descrição:** Respostas dos fornecedores aos requisitos obrigatórios definidos na negociação.
**Módulo:** Sourcing
**Uso típico:** Avaliação de conformidade dos fornecedores com requisitos mandatórios.

### PON_BID_SECTIONS
**Descrição:** Seções das propostas dos fornecedores, organizadas conforme a estrutura definida na negociação.
**Módulo:** Sourcing
**Uso típico:** Análise estruturada de propostas por seção.

### PON_NEG_TEAM_MEMBERS
**Descrição:** Membros da equipe de negociação, com papéis atribuídos (owner, collaborator, approver) e permissões de acesso.
**Módulo:** Sourcing
**Uso típico:** Gestão de equipe de sourcing e controle de acesso a negociações.

### PON_REQUIREMENTS
**Descrição:** Definição de requisitos em negociações (ex.: certificações, capacidade produtiva), usados para qualificar fornecedores.
**Módulo:** Sourcing
**Uso típico:** Configuração de critérios de qualificação em eventos de sourcing.

### PON_REQUIREMENT_SCORES
**Descrição:** Pontuações atribuídas às respostas dos fornecedores para requisitos de negociação, usadas na avaliação e ranking.
**Módulo:** Sourcing
**Uso típico:** Scoring e ranking de fornecedores em processos de licitação.

### PON_REQUIREMENT_SECTIONS
**Descrição:** Organização dos requisitos em seções dentro de uma negociação.
**Módulo:** Sourcing
**Uso típico:** Estruturação de requisitos em categorias lógicas.

### PON_SUPPLIER_ACTIVITIES
**Descrição:** Registra atividades dos fornecedores no contexto de negociações (visualização, download de anexos, submissão de propostas).
**Módulo:** Sourcing
**Uso típico:** Monitoramento de engajamento de fornecedores em eventos de sourcing.

### PON_AUC_DOCTYPES_B
**Descrição:** Tabela base que define os tipos de documento de negociação (RFQ, RFI, Auction, Buyer's Auction, etc.).
**Módulo:** Sourcing
**Uso típico:** Configuração de tipos de negociação disponíveis.

### PON_AUC_DOCTYPES_TL
**Descrição:** Tradução dos tipos de documento de negociação em múltiplos idiomas.
**Módulo:** Sourcing
**Uso típico:** Suporte multilíngue para tipos de negociação.

### PON_AUC_DOCTYPES_VL
**Descrição:** View combinada dos tipos de documento de negociação (base + tradução).
**Módulo:** Sourcing
**Uso típico:** Consulta de tipos de negociação com descrições traduzidas.

### PON_DOCTYPE_STYLES_B
**Descrição:** Tabela base que define os estilos de documento de negociação, controlando comportamento e campos disponíveis por tipo.
**Módulo:** Sourcing
**Uso típico:** Personalização de estilos de negociação.

### PON_DOCTYPE_STYLES_TL
**Descrição:** Tradução dos estilos de documento de negociação.
**Módulo:** Sourcing
**Uso típico:** Suporte multilíngue para estilos de negociação.

### PON_DOCTYPE_STYLES_VL
**Descrição:** View combinada dos estilos de documento de negociação (base + tradução).
**Módulo:** Sourcing
**Uso típico:** Consulta de estilos de negociação com descrições traduzidas.

### PON_NEGOTIATION_STYLES_B
**Descrição:** Tabela base que define estilos de negociação, incluindo regras de pricing, visibilidade de propostas e critérios de adjudicação.
**Módulo:** Sourcing
**Uso típico:** Configuração de regras de negociação (sealed bid, multi-round, etc.).

### PON_NEGOTIATION_STYLES_TL
**Descrição:** Tradução dos estilos de negociação em múltiplos idiomas.
**Módulo:** Sourcing
**Uso típico:** Suporte multilíngue para estilos de negociação.

### PON_PROGRAM_HEADERS
**Descrição:** Cabeçalhos de programas de sourcing, que agrupam múltiplas negociações sob uma estratégia de compras de longo prazo.
**Módulo:** Sourcing
**Uso típico:** Gestão de programas estratégicos de sourcing.

### PON_PROGRAM_OBJECTIVES
**Descrição:** Objetivos definidos para programas de sourcing (ex.: redução de custo, diversificação de fornecedores, melhoria de qualidade).
**Módulo:** Sourcing
**Uso típico:** Definição e rastreamento de metas estratégicas de sourcing.

### PON_PROGRAM_TEAM_MEMBERS
**Descrição:** Membros da equipe designados para programas de sourcing, com papéis e responsabilidades.
**Módulo:** Sourcing
**Uso típico:** Gestão de equipes em programas estratégicos de compras.

### PON_OBJECTIVE_NEGOTIATIONS
**Descrição:** Vinculação entre objetivos de programa e negociações individuais, rastreando quais negociações atendem a quais objetivos.
**Módulo:** Sourcing
**Uso típico:** Alinhamento de negociações com objetivos estratégicos do programa.

### PON_NEG_AGG_TO_OBJ_OTBI_V
**Descrição:** View OTBI (Oracle Transactional BI) que agrega dados de negociações por objetivo, para análise em relatórios de Business Intelligence.
**Módulo:** Sourcing
**Uso típico:** Relatórios analíticos de negociações agregadas por objetivo de programa.

### PON_NEG_AGG_TO_PROG_OTBI_V
**Descrição:** View OTBI que agrega dados de negociações por programa de sourcing.
**Módulo:** Sourcing
**Uso típico:** Relatórios analíticos de desempenho de programas de sourcing.

### PON_OBJ_AGG_TO_PROG_OTBI_V
**Descrição:** View OTBI que agrega dados de objetivos por programa de sourcing.
**Módulo:** Sourcing
**Uso típico:** Relatórios analíticos de progresso de objetivos dentro de programas.

---

## 12. Qualificação de Fornecedores (POQ)

> Tabelas com prefixo **POQ_** pertencem ao módulo de Supplier Qualification Management, referenciadas no contexto de Purchasing.

### POQ_QUAL_MODELS
**Descrição:** Define modelos de qualificação de fornecedores, que agrupam áreas de qualificação, critérios e pesos para avaliação estruturada.
**Módulo:** Supplier Qualification Management
**Uso típico:** Configuração de modelos de avaliação de fornecedores.

### POQ_QUAL_MODEL_AREAS
**Descrição:** Áreas de qualificação vinculadas a modelos, como qualidade, capacidade financeira, sustentabilidade, compliance.
**Módulo:** Supplier Qualification Management
**Uso típico:** Definição de dimensões de avaliação dentro de cada modelo.

### POQ_QUAL_MODEL_OUTCOMES
**Descrição:** Resultados possíveis (outcomes) para modelos de qualificação (ex.: Qualificado, Não Qualificado, Qualificado com Restrições).
**Módulo:** Supplier Qualification Management
**Uso típico:** Configuração de resultados finais do processo de qualificação.

### POQ_QUAL_AREAS_VL
**Descrição:** View combinada das áreas de qualificação com descrições traduzidas.
**Módulo:** Supplier Qualification Management
**Uso típico:** Consulta de áreas de qualificação de fornecedores.

### POQ_QUAL_AREA_QUESTIONS
**Descrição:** Perguntas associadas a cada área de qualificação, usadas em questionários de avaliação de fornecedores.
**Módulo:** Supplier Qualification Management
**Uso típico:** Definição de critérios de avaliação por área de qualificação.

### POQ_QUAL_AREA_ALL_QUESTIONS_V
**Descrição:** View que consolida todas as perguntas de todas as áreas de qualificação.
**Módulo:** Supplier Qualification Management
**Uso típico:** Visão completa do questionário de qualificação.

### POQ_QUAL_AREA_OUTCOMES
**Descrição:** Resultados possíveis definidos por área de qualificação específica.
**Módulo:** Supplier Qualification Management
**Uso típico:** Configuração de outcomes por dimensão de avaliação.

### POQ_QUAL_RESPONSES
**Descrição:** Respostas às perguntas de qualificação fornecidas por fornecedores ou avaliadores internos.
**Módulo:** Supplier Qualification Management
**Uso típico:** Coleta e análise de respostas de qualificação.

### POQ_QUAL_ASMT_INIT_V
**Descrição:** View que apresenta a relação entre avaliações (assessments) e iniciativas de qualificação.
**Módulo:** Supplier Qualification Management
**Uso típico:** Rastreamento de avaliações vinculadas a iniciativas.

### POQ_ASSESSMENTS
**Descrição:** Avaliações de qualificação de fornecedores, registrando o processo de avaliação, data, avaliador e resultado.
**Módulo:** Supplier Qualification Management
**Uso típico:** Gestão do ciclo de avaliação de fornecedores.

### POQ_ASSESSMENT_QUALS
**Descrição:** Qualificações resultantes de avaliações, vinculando o resultado da avaliação ao status de qualificação do fornecedor.
**Módulo:** Supplier Qualification Management
**Uso típico:** Registro de qualificações concedidas a fornecedores.

### POQ_EVALUATION_TEAM
**Descrição:** Membros da equipe de avaliação de qualificação de fornecedores.
**Módulo:** Supplier Qualification Management
**Uso típico:** Gestão de avaliadores designados para processos de qualificação.

### POQ_INITIATIVES
**Descrição:** Iniciativas de qualificação de fornecedores, que representam campanhas ou programas de avaliação (ex.: requalificação anual, onboarding).
**Módulo:** Supplier Qualification Management
**Uso típico:** Gestão de programas de qualificação e requalificação.

### POQ_INITIATIVE_SUPPLIERS
**Descrição:** Fornecedores vinculados a iniciativas de qualificação, com status de participação e progresso.
**Módulo:** Supplier Qualification Management
**Uso típico:** Rastreamento de quais fornecedores estão em cada iniciativa.

### POQ_QUESTIONS_VL
**Descrição:** View de perguntas de qualificação com descrições traduzidas.
**Módulo:** Supplier Qualification Management
**Uso típico:** Consulta de perguntas disponíveis para questionários.

### POQ_QUESTION_SCORES
**Descrição:** Pontuações atribuídas a respostas de perguntas de qualificação, usadas no cálculo de score final.
**Módulo:** Supplier Qualification Management
**Uso típico:** Scoring de respostas de fornecedores.

### POQ_QUESTION_STRUCTURE_V
**Descrição:** View que apresenta a estrutura hierárquica de perguntas (perguntas pai/filho, dependências condicionais).
**Módulo:** Supplier Qualification Management
**Uso típico:** Visualização da árvore de perguntas de qualificação.

### POQ_QUESTNAIRES_VL
**Descrição:** View de questionários de qualificação com descrições traduzidas.
**Módulo:** Supplier Qualification Management
**Uso típico:** Consulta de questionários disponíveis.

### POQ_QUESTNAIRE_RESPONSES
**Descrição:** Respostas completas a questionários de qualificação, agregando todas as respostas de um fornecedor a um questionário específico.
**Módulo:** Supplier Qualification Management
**Uso típico:** Análise consolidada de respostas por questionário.

### POQ_QUESTNAIRE_RESP_HEADERS
**Descrição:** Cabeçalhos das respostas a questionários, com informações de fornecedor, data de submissão e status.
**Módulo:** Supplier Qualification Management
**Uso típico:** Controle de submissões de questionários.

### POQ_QUESTNAIRE_RESP_SECTIONS
**Descrição:** Seções das respostas a questionários, organizando respostas por grupo temático.
**Módulo:** Supplier Qualification Management
**Uso típico:** Análise de respostas por seção do questionário.

### POQ_ALL_QNAIRE_RESP_VALUES_V
**Descrição:** View consolidada de todos os valores de respostas a questionários de qualificação.
**Módulo:** Supplier Qualification Management
**Uso típico:** Extração completa de respostas para análise.

### POQ_ALL_RESP_REPOS_VALUES_V
**Descrição:** View consolidada de todos os valores de respostas armazenados no repositório de respostas.
**Módulo:** Supplier Qualification Management
**Uso típico:** Análise histórica de respostas de qualificação.

### POQ_QUES_ACC_RESPONSES_VL
**Descrição:** View que exibe respostas aceitas/acumuladas para perguntas de qualificação, com traduções.
**Módulo:** Supplier Qualification Management
**Uso típico:** Consulta de respostas válidas para scoring.

### POQ_RESPONSE_REPOSITORY
**Descrição:** Repositório central de respostas de qualificação, armazenando respostas reutilizáveis de fornecedores para uso em múltiplas avaliações.
**Módulo:** Supplier Qualification Management
**Uso típico:** Reaproveitamento de respostas de fornecedores entre avaliações.

---

## 13. Fornecedores (POZ)

> Tabelas com prefixo **POZ_** pertencem ao módulo de Supplier Management, referenciadas no contexto de Purchasing.

### POZ_SUPPLIERS
**Descrição:** Tabela principal de fornecedores, contendo dados cadastrais como razão social, CNPJ/Tax ID, status (ativo, inativo, prospectivo), tipo de organização e data de criação.
**Módulo:** Supplier Management
**Uso típico:** Base cadastral de fornecedores para compras, pagamentos e análise de spend.

### POZ_SUPPLIERS_V
**Descrição:** View de fornecedores com dados consolidados para consulta simplificada.
**Módulo:** Supplier Management
**Uso típico:** Consultas de fornecedores com informações agregadas.

### POZ_SUPPLIERS_PII
**Descrição:** Dados pessoais sensíveis (PII — Personally Identifiable Information) de fornecedores pessoa física, como CPF, data de nascimento e informações protegidas por LGPD/GDPR.
**Módulo:** Supplier Management
**Uso típico:** Acesso controlado a dados sensíveis de fornecedores — requer atenção especial à privacidade.

### POZ_SUPPLIER_SITES_ALL_M
**Descrição:** Sites (endereços operacionais) dos fornecedores por business unit, contendo informações de endereço, termos de pagamento, moeda padrão, e configurações de faturamento e remessa.
**Módulo:** Supplier Management
**Uso típico:** Gestão de múltiplos sites de fornecedores e suas configurações por organização.

### POZ_SUPPLIER_SITES_PII
**Descrição:** Dados pessoais sensíveis associados a sites de fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Acesso controlado a dados PII de sites de fornecedores.

### POZ_SUPPLIER_ADDRESS_V
**Descrição:** View consolidada de endereços de fornecedores, combinando dados de sites com informações de localização.
**Módulo:** Supplier Management
**Uso típico:** Consulta simplificada de endereços de fornecedores.

### POZ_SUPPLIER_CONTACTS
**Descrição:** Contatos de fornecedores (nome, e-mail, telefone, cargo), vinculados a sites específicos ou ao fornecedor como um todo.
**Módulo:** Supplier Management
**Uso típico:** Gestão de contatos de fornecedores para comunicação e notificações.

### POZ_ALL_SUPPLIER_CONTACTS_V
**Descrição:** View consolidada de todos os contatos de fornecedores, incluindo dados de contato e site associado.
**Módulo:** Supplier Management
**Uso típico:** Consulta abrangente de contatos de fornecedores.

### POZ_SUPP_SITES_CONTACTS_V
**Descrição:** View que relaciona contatos de fornecedores com seus respectivos sites.
**Módulo:** Supplier Management
**Uso típico:** Identificação de contatos por site de fornecedor.

### POZ_SUPPLIER_MAPPINGS
**Descrição:** Mapeamentos de fornecedores entre diferentes sistemas ou entidades, utilizado em cenários de migração, consolidação ou integração entre business units.
**Módulo:** Supplier Management
**Uso típico:** Reconciliação de fornecedores entre sistemas legados e Oracle Fusion.

### POZ_SITE_ASSIGNMENTS_ALL_M
**Descrição:** Atribuições de sites de fornecedores a business units e funções (purchasing, payment, procurement), controlando quais sites podem ser usados em cada contexto.
**Módulo:** Supplier Management
**Uso típico:** Configuração de quais sites estão habilitados para compras e pagamentos por BU.

### POZ_BUS_CLASSIFICATIONS
**Descrição:** Classificações empresariais de fornecedores (ex.: pequena empresa, empresa de propriedade feminina, empresa minoritária), usadas para programas de diversidade.
**Módulo:** Supplier Management
**Uso típico:** Relatórios de diversidade de fornecedores e conformidade regulatória.

### POZ_BUSINESS_CLASSIFICATIONS_V
**Descrição:** View de classificações empresariais com dados consolidados.
**Módulo:** Supplier Management
**Uso típico:** Consulta simplificada de classificações de fornecedores.

### POZ_CERTIFYING_AGENCIES
**Descrição:** Agências certificadoras que validam classificações empresariais de fornecedores (ex.: órgãos que certificam status de pequena empresa).
**Módulo:** Supplier Management
**Uso típico:** Gestão de certificações e agências validadoras.

### POZ_SUP_PRODUCTS_SERVICES
**Descrição:** Produtos e serviços oferecidos por cada fornecedor, categorizados por UNSPSC ou outro sistema de classificação.
**Módulo:** Supplier Management
**Uso típico:** Busca de fornecedores por produto/serviço oferecido.

### POZ_SUPP_PROD_SERVICES_ATTR_V
**Descrição:** View com atributos detalhados dos produtos e serviços oferecidos por fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Análise detalhada de capacidades dos fornecedores.

### POZ_SUPP_RELATIONSHIP_VL
**Descrição:** View que exibe relacionamentos entre fornecedores (ex.: subsidiárias, parceiros, consórcio), com descrições traduzidas.
**Módulo:** Supplier Management
**Uso típico:** Análise de estrutura corporativa e relacionamentos entre fornecedores.

### POZ_SUP_THIRDPARTY_PAYMENT_REL
**Descrição:** Relacionamentos de pagamento a terceiros, onde o pagamento de um fornecedor é direcionado a outro (third-party payment).
**Módulo:** Supplier Management
**Uso típico:** Configuração de pagamentos a terceiros e gestão de relações de pagamento indireto.

### POZ_EXT_BANK_ACCOUNTS_V
**Descrição:** View de contas bancárias externas de fornecedores, consolidando dados de IBY com informações do fornecedor.
**Módulo:** Supplier Management (referência cruzada com IBY)
**Uso típico:** Consulta de dados bancários de fornecedores para pagamentos.

---

## 14. Registros e Solicitações de Fornecedores (POZ)

### POZ_SUPPLIER_REGISTRATIONS
**Descrição:** Registros de processos de cadastro (registration) de novos fornecedores, incluindo status, data de submissão e informações do processo de aprovação.
**Módulo:** Supplier Management
**Uso típico:** Rastreamento do processo de onboarding de novos fornecedores.

### POZ_SUP_REG_PII
**Descrição:** Dados pessoais sensíveis associados a registros de fornecedores em processo de cadastro.
**Módulo:** Supplier Management
**Uso típico:** Acesso controlado a dados PII durante o processo de registro.

### POZ_SUPP_REQUESTS
**Descrição:** Solicitações de alteração ou inclusão de fornecedores, submetidas por usuários internos ou pelo próprio fornecedor via portal.
**Módulo:** Supplier Management
**Uso típico:** Gestão de solicitações de manutenção cadastral de fornecedores.

### POZ_ADDRESS_REQUESTS
**Descrição:** Solicitações de inclusão ou alteração de endereços de fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Workflow de aprovação de novos endereços de fornecedores.

### POZ_CONTACT_REQUESTS
**Descrição:** Solicitações de inclusão ou alteração de contatos de fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Workflow de aprovação de novos contatos.

### POZ_PRODUCT_SERVICE_REQUESTS
**Descrição:** Solicitações de inclusão ou alteração de produtos/serviços oferecidos por fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Manutenção do catálogo de capacidades dos fornecedores.

### POZ_BUS_CLASS_REQS
**Descrição:** Solicitações de inclusão ou alteração de classificações empresariais de fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Workflow de classificações de diversidade de fornecedores.

### POZ_SPEND_AUTH_REQUESTS
**Descrição:** Solicitações de autorização de gasto (spend authorization) com fornecedores, usadas para aprovar limites de compra ou contratos.
**Módulo:** Supplier Management
**Uso típico:** Controle de autorizações de gasto com fornecedores.

### POZ_UP_REQUESTS
**Descrição:** Solicitações de atualização de perfil de fornecedor, submetidas via portal do fornecedor.
**Módulo:** Supplier Management
**Uso típico:** Self-service de atualização cadastral por fornecedores.

### POZ_UP_ROLE_REQUESTS
**Descrição:** Solicitações de atribuição ou alteração de roles/papéis para usuários de fornecedores no portal.
**Módulo:** Supplier Management
**Uso típico:** Gestão de permissões de acesso de usuários de fornecedores.

### POZ_APPROVAL_HISTORY
**Descrição:** Histórico de aprovações de solicitações de fornecedores, incluindo aprovador, data e comentários.
**Módulo:** Supplier Management
**Uso típico:** Auditoria de processos de aprovação de fornecedores.

### POZ_BI_APPR_USER_COMMENTS_V
**Descrição:** View BI que exibe comentários de aprovadores em processos de fornecedores.
**Módulo:** Supplier Management
**Uso típico:** Relatórios de auditoria com comentários de aprovação.

### POZ_PROVISIONABLE_ROLES
**Descrição:** Roles/papéis que podem ser provisionados (atribuídos) a contatos de fornecedores para acesso ao portal.
**Módulo:** Supplier Management
**Uso típico:** Configuração de papéis disponíveis para fornecedores no portal.

### POZ_CONTACT_ACT_DATA_ACCESS_V
**Descrição:** View que exibe o acesso a dados ativos de contatos de fornecedores, incluindo permissões e escopo.
**Módulo:** Supplier Management
**Uso típico:** Auditoria de acessos de contatos de fornecedores.

### POZ_SUPP_ACCESS_SITES_V
**Descrição:** View que relaciona fornecedores aos sites que seus contatos podem acessar.
**Módulo:** Supplier Management
**Uso típico:** Controle de acesso de fornecedores por site.

### POZ_SUPP_ROLE_ASSIGNMENTS_V
**Descrição:** View que exibe as atribuições de roles/papéis a fornecedores e seus contatos.
**Módulo:** Supplier Management
**Uso típico:** Consulta de permissões atribuídas a fornecedores.

### POZ_BI_HIERARCHY_AP_INV_DIST_V
**Descrição:** View BI que apresenta dados hierárquicos de fornecedores com distribuições de faturas de Contas a Pagar, para análise de spend hierárquica.
**Módulo:** Supplier Management (referência cruzada com AP)
**Uso típico:** Relatórios de spend por hierarquia de fornecedores.

### POZ_BI_SUPP_AP_INV_DIST_V
**Descrição:** View BI que relaciona fornecedores com distribuições de faturas AP, para análise de gastos por fornecedor.
**Módulo:** Supplier Management (referência cruzada com AP)
**Uso típico:** Relatórios de spend analysis por fornecedor.

### POZ_BI_SUP_SITES_AP_INV_DIST_V
**Descrição:** View BI que relaciona sites de fornecedores com distribuições de faturas AP.
**Módulo:** Supplier Management (referência cruzada com AP)
**Uso típico:** Análise de gastos por site de fornecedor.

### POZ_BI_SUPP_REG_BANK_ACCOUNT_V
**Descrição:** View BI que relaciona registros de fornecedores com contas bancárias, para análise e auditoria.
**Módulo:** Supplier Management (referência cruzada com IBY)
**Uso típico:** Relatórios de dados bancários associados a registros de fornecedores.

---

## 15. Acesso de Fornecedores (POS)

### POS_USER_ACCESS_VALUES
**Descrição:** Define os valores de acesso de usuários de fornecedores, controlando quais dados e funcionalidades cada usuário do portal de fornecedores pode acessar.
**Módulo:** Supplier Portal
**Uso típico:** Controle granular de acesso de usuários de fornecedores no portal self-service.

---

## 16. Contas a Pagar — Referência Cruzada (AP)

> Tabelas com prefixo **AP_** pertencem ao módulo de Accounts Payable, referenciadas no contexto de Purchasing para configuração de tolerâncias e distribuições.

### AP_DISTRIBUTION_SETS_ALL
**Descrição:** Conjuntos de distribuição contábil padrão para faturas de Contas a Pagar, definindo como valores são automaticamente distribuídos entre contas contábeis.
**Módulo:** Accounts Payable (referência cruzada)
**Uso típico:** Automação de distribuição contábil em faturas vinculadas a POs.

### AP_INCOME_TAX_TYPES
**Descrição:** Tipos de imposto de renda retido na fonte para fornecedores (ex.: 1099 nos EUA, IRF no Brasil), usados no processo de pagamento.
**Módulo:** Accounts Payable (referência cruzada)
**Uso típico:** Classificação fiscal de fornecedores para retenção de impostos.

### AP_TOLERANCE_TEMPLATES
**Descrição:** Templates de tolerância para matching entre PO, recebimento e fatura, definindo percentuais e valores aceitos de variação (ex.: 5% de tolerância de preço).
**Módulo:** Accounts Payable (referência cruzada)
**Uso típico:** Configuração de regras de matching e tolerâncias de validação de faturas.

---

## 17. Catálogo de Produtos (EGP)

> Tabelas com prefixo **EGP_** pertencem ao módulo de Product Management (Engineering), referenciadas no contexto de Purchasing para catálogo de itens.

### EGP_CATEGORIES_TL
**Descrição:** Tradução de categorias de itens (purchasing categories, inventory categories) usadas para classificação de produtos e serviços.
**Módulo:** Product Management (referência cruzada)
**Uso típico:** Suporte multilíngue para categorias de compras.

### EGP_CATEGORIES_VL
**Descrição:** View combinada de categorias de itens com descrições traduzidas.
**Módulo:** Product Management (referência cruzada)
**Uso típico:** Consulta de categorias para classificação de linhas de PO e requisição.

### EGP_SYSTEM_ITEMS_VL
**Descrição:** View principal de itens do sistema (master items), com descrição, UOM, categoria, status e atributos de compra. É a referência central de itens compráveis.
**Módulo:** Product Management (referência cruzada)
**Uso típico:** Consulta de catálogo de itens para compras, validação de itens em POs e requisições.

---

## 18. Idiomas e Territórios (FND)

> Tabelas com prefixo **FND_** pertencem à Foundation (infraestrutura base), referenciadas no contexto de Purchasing para lookups e localização.

### FND_LANGUAGES_VL
**Descrição:** View de idiomas instalados no sistema, com código ISO, nome e status (ativo/inativo).
**Módulo:** Foundation (referência cruzada)
**Uso típico:** Suporte a traduções e localização de documentos de compras.

### FND_LOOKUPS
**Descrição:** Tabela central de lookups (listas de valores) do sistema, usada por todos os módulos para decodificação de campos codificados.
**Módulo:** Foundation (referência cruzada)
**Uso típico:** Decodificação de campos como status, tipo de documento, condições de pagamento, etc.

### FND_TERRITORIES_VL
**Descrição:** View de territórios/países com descrições traduzidas, contendo código ISO, nome do país e região.
**Módulo:** Foundation (referência cruzada)
**Uso típico:** Classificação geográfica de fornecedores e endereços de entrega.

---

## 19. Acordos e Business Units (FOS/FUN)

### FOS_AGREEMENT_PTR_F
**Descrição:** Tabela de fatos de acordos (agreements) no modelo de dados OTBI, contendo ponteiros para acordos de compra (Blanket/Contract Purchase Agreements).
**Módulo:** Fusion OTBI (referência cruzada)
**Uso típico:** Análise de acordos de compra em relatórios OTBI/BI Publisher.

### FUN_ALL_BUSINESS_UNITS_V
**Descrição:** View que lista todas as business units configuradas no sistema, com nome, status e informações organizacionais.
**Módulo:** Financials Common (referência cruzada)
**Uso típico:** Filtro de dados de compras por business unit.

### FUN_BU_USAGES_V
**Descrição:** View que exibe os usos (usages) de cada business unit — quais módulos estão habilitados (Purchasing, Payables, Receivables, etc.).
**Módulo:** Financials Common (referência cruzada)
**Uso típico:** Identificação de quais BUs têm o módulo Purchasing habilitado.

### FUN_SERVICE_PROVIDER_BU_V
**Descrição:** View que identifica business units que atuam como service providers (centros de serviço compartilhados), processando transações em nome de outras BUs.
**Módulo:** Financials Common (referência cruzada)
**Uso típico:** Configuração de shared services em compras centralizadas.

---

## 20. Contabilidade e Ledger (GL)

> Tabelas com prefixo **GL_** pertencem ao módulo de General Ledger, referenciadas no contexto de Purchasing para contabilização.

### GL_DAILY_CONVERSION_TYPES
**Descrição:** Tipos de conversão cambial diária (Spot, Corporate, User Defined), usados para converter valores de POs em moedas diferentes da moeda do ledger.
**Módulo:** General Ledger (referência cruzada)
**Uso típico:** Definição de taxa de câmbio para POs em moeda estrangeira.

### GL_LEDGERS
**Descrição:** Cadastro de ledgers (livros contábeis), contendo plano de contas, moeda, calendário contábil e método de subledger accounting.
**Módulo:** General Ledger (referência cruzada)
**Uso típico:** Vinculação de distribuições de PO ao ledger contábil correspondente.

---

## 21. Organizações e Locais (HR)

> Tabelas com prefixo **HR_** pertencem ao módulo de Human Resources, referenciadas no contexto de Purchasing para estrutura organizacional.

### HR_ALL_ORGANIZATION_UNITS_F
**Descrição:** Tabela de organizações (departamentos, divisões, centros de custo) com versionamento temporal (date-effective), contendo hierarquia organizacional.
**Módulo:** Human Resources (referência cruzada)
**Uso típico:** Vinculação de compras a departamentos e centros de custo.

### HR_ALL_ORGANIZATION_UNITS_F_VL
**Descrição:** View de organizações com descrições traduzidas e dados consolidados.
**Módulo:** Human Resources (referência cruzada)
**Uso típico:** Consulta de nomes de organizações para relatórios de compras.

### HR_ORGANIZATION_UNITS_F_TL
**Descrição:** Tradução dos nomes de organizações em múltiplos idiomas.
**Módulo:** Human Resources (referência cruzada)
**Uso típico:** Suporte multilíngue para nomes de organizações.

### HR_LOCATIONS_ALL_F_VL
**Descrição:** View de locais (locations) com dados consolidados e traduzidos, contendo endereço, país, região e status.
**Módulo:** Human Resources (referência cruzada)
**Uso típico:** Identificação de locais ship-to e bill-to em pedidos de compra.

---

## 22. Terceiros e Endereços (HZ — TCA)

> Tabelas com prefixo **HZ_** pertencem ao Trading Community Architecture (TCA), referenciadas no contexto de Purchasing para dados de terceiros (fornecedores, clientes, contatos).

### HZ_PARTIES
**Descrição:** Tabela central de parties (entidades) do TCA, contendo organizações, pessoas e grupos. Todo fornecedor tem um registro correspondente em HZ_PARTIES.
**Módulo:** TCA (referência cruzada)
**Uso típico:** Dados master de entidades — vinculação entre fornecedores e parties.

### HZ_ORGANIZATION_PROFILES
**Descrição:** Perfis de organizações no TCA, com dados como DUNS number, SIC code, número de funcionários, faturamento anual e informações corporativas.
**Módulo:** TCA (referência cruzada)
**Uso típico:** Enriquecimento de dados de fornecedores com informações corporativas.

### HZ_LOCATIONS
**Descrição:** Endereços físicos no TCA, com rua, cidade, estado, país e CEP. Compartilhada entre múltiplas entidades.
**Módulo:** TCA (referência cruzada)
**Uso típico:** Dados de endereço de fornecedores, locais de entrega e faturamento.

### HZ_PARTY_SITES
**Descrição:** Vinculação entre parties e locations, definindo os endereços associados a cada entidade e seus usos (ship-to, bill-to, remit-to).
**Módulo:** TCA (referência cruzada)
**Uso típico:** Gestão de endereços de fornecedores e seus usos.

### HZ_ORG_CONTACTS
**Descrição:** Contatos de organizações no TCA, contendo informações de cargo, departamento e dados de contato.
**Módulo:** TCA (referência cruzada)
**Uso típico:** Dados de contatos associados a fornecedores.

### HZ_ORG_CONTACT_ROLES
**Descrição:** Papéis atribuídos a contatos de organizações (ex.: comercial, financeiro, logística).
**Módulo:** TCA (referência cruzada)
**Uso típico:** Classificação de contatos por função/papel.

### HZ_ADDTNL_PARTY_NAMES
**Descrição:** Nomes adicionais de parties (aliases, nomes comerciais, razões sociais anteriores).
**Módulo:** TCA (referência cruzada)
**Uso típico:** Busca de fornecedores por nomes alternativos ou trade names.

---

## 23. Pagamentos (IBY)

> Tabelas com prefixo **IBY_** pertencem ao módulo de Payments (Oracle Payments), referenciadas no contexto de Purchasing para dados bancários e métodos de pagamento de fornecedores.

### IBY_EXTERNAL_PAYEES_ALL
**Descrição:** Cadastro de beneficiários de pagamento externos (payees), vinculando fornecedores/sites a configurações de pagamento.
**Módulo:** Oracle Payments (referência cruzada)
**Uso típico:** Configuração de dados de pagamento por fornecedor e site.

### IBY_EXT_BANK_ACCOUNTS
**Descrição:** Contas bancárias externas cadastradas para fornecedores, contendo banco, agência, número da conta, IBAN e SWIFT.
**Módulo:** Oracle Payments (referência cruzada)
**Uso típico:** Gestão de dados bancários para pagamentos a fornecedores.

### IBY_EXT_PARTY_PMT_MTHDS
**Descrição:** Métodos de pagamento configurados para parties externas (fornecedores), definindo como cada fornecedor prefere receber pagamentos.
**Módulo:** Oracle Payments (referência cruzada)
**Uso típico:** Configuração de métodos de pagamento por fornecedor.

### IBY_PAYMENT_METHODS_VL
**Descrição:** View de métodos de pagamento disponíveis (transferência bancária, cheque, boleto, etc.) com descrições traduzidas.
**Módulo:** Oracle Payments (referência cruzada)
**Uso típico:** Consulta de métodos de pagamento para configuração de fornecedores.

### IBY_PMT_INSTR_USES_ALL
**Descrição:** Usos de instrumentos de pagamento (payment instrument uses), vinculando contas bancárias a payees e definindo prioridade de uso.
**Módulo:** Oracle Payments (referência cruzada)
**Uso típico:** Configuração de qual conta bancária usar para cada fornecedor/site.

---

## 24. Inventário e Unidades de Medida (INV)

> Tabelas com prefixo **INV_** pertencem ao módulo de Inventory Management, referenciadas no contexto de Purchasing para organizações de inventário e UOM.

### INV_ORGANIZATION_DEFINITIONS_V
**Descrição:** View de definições de organizações de inventário, com nome, código, endereço e business unit associada. Utilizada para identificar organizações de recebimento.
**Módulo:** Inventory Management (referência cruzada)
**Uso típico:** Identificação de organizações de destino para recebimento de materiais.

### INV_UNITS_OF_MEASURE_VL
**Descrição:** View de unidades de medida (UOM) com descrições traduzidas, incluindo código, nome e classe (peso, volume, comprimento, etc.).
**Módulo:** Inventory Management (referência cruzada)
**Uso típico:** Decodificação de unidades de medida em linhas de PO e requisição.

---

## 25. Pessoas e Atribuições (PER)

> Tabelas com prefixo **PER_** pertencem ao módulo de Human Resources / HCM, referenciadas no contexto de Purchasing para dados de pessoas (requisitantes, aprovadores, compradores).

### PER_ALL_PEOPLE_F
**Descrição:** Tabela principal de pessoas com versionamento temporal, contendo dados de funcionários, contingentes e outros trabalhadores.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Identificação de requisitantes, aprovadores e compradores em documentos de compras.

### PER_PERSON_NAMES_F_V
**Descrição:** View de nomes de pessoas com formato por cultura/idioma, incluindo nome completo, primeiro nome e sobrenome.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Exibição de nomes de pessoas em relatórios de compras.

### PER_ALL_ASSIGNMENTS_M
**Descrição:** Atribuições de trabalho (assignments) de pessoas, contendo cargo, departamento, business unit, manager, grade e localização. Tabela date-effective.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Vinculação de requisitantes/aprovadores a departamentos e hierarquias.

### PER_ASSIGNMENT_SUPERVISORS_F
**Descrição:** Hierarquia de supervisão (manager chain) para atribuições de trabalho, com versionamento temporal.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Determinação de cadeia de aprovação para requisições e POs.

### PER_ADDRESSES_F
**Descrição:** Endereços de pessoas (residencial, correspondência) com versionamento temporal.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Endereços de entrega para requisições de compra de material pessoal (ex.: home office).

### PER_EMAIL_ADDRESSES
**Descrição:** Endereços de e-mail de pessoas (corporativo, pessoal), vinculados a person_id.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Notificações de aprovação e comunicação com requisitantes.

### PER_PHONES
**Descrição:** Números de telefone de pessoas (trabalho, celular, fax).
**Módulo:** HCM (referência cruzada)
**Uso típico:** Dados de contato de requisitantes e aprovadores.

### PER_JOBS_F
**Descrição:** Cadastro de cargos (jobs) com versionamento temporal, incluindo família de cargo e nível.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Classificação de cargos de requisitantes para regras de aprovação.

### PER_JOBS_F_TL
**Descrição:** Tradução de nomes de cargos em múltiplos idiomas.
**Módulo:** HCM (referência cruzada)
**Uso típico:** Exibição de nomes de cargos em relatórios multilíngues.

### PER_USERS
**Descrição:** Cadastro de usuários do sistema, vinculando person_id a user_id, com dados de login e status.
**Módulo:** HCM / Security (referência cruzada)
**Uso típico:** Identificação de usuários que criaram, aprovaram ou modificaram documentos de compras.

### PER_ROLES_DN_VL
**Descrição:** View de roles (papéis de segurança) atribuídos a usuários, com nomes distinguidos e descrições traduzidas.
**Módulo:** HCM / Security (referência cruzada)
**Uso típico:** Auditoria de permissões de usuários no módulo de compras.

---

## 26. Tributação (ZX)

> Tabelas com prefixo **ZX_** pertencem ao módulo de Tax (E-Business Tax / Oracle Tax), referenciadas no contexto de Purchasing para classificações fiscais.

### ZX_PARTY_TAX_PROFILE
**Descrição:** Perfis fiscais de parties (fornecedores, clientes, organizações), contendo regime tributário, status de contribuinte e configurações de cálculo de imposto.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Determinação de regime fiscal de fornecedores para cálculo de impostos em POs.

### ZX_REGISTRATIONS
**Descrição:** Registros fiscais (tax registrations) de parties, contendo número de inscrição fiscal (CNPJ, VAT number, Tax ID) e jurisdição.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Validação de inscrições fiscais de fornecedores.

### ZX_INPUT_CLASSIFICATIONS_V
**Descrição:** View de classificações de entrada fiscal (input tax classifications), usadas para determinar o tratamento tributário de itens comprados.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificação fiscal de linhas de PO para cálculo de impostos recuperáveis.

### ZX_FC_BUSINESS_CATEGORIES_V
**Descrição:** View de categorias fiscais de negócio (fiscal business categories), usadas como critério de determinação de impostos.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificação fiscal para determinação automática de impostos em transações de compra.

### ZX_FC_DOCUMENT_FISCAL_V
**Descrição:** View de classificações fiscais de documento, usadas para categorizar documentos fiscais (NF-e, invoice, etc.) no cálculo de impostos.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificação fiscal de documentos de compra para localizações que exigem documento fiscal.

### ZX_FC_INTENDED_USE_V
**Descrição:** View de classificações de uso pretendido (intended use), que define a finalidade do item comprado para fins fiscais (ex.: revenda, consumo, ativo fixo).
**Módulo:** Tax (referência cruzada)
**Uso típico:** Determinação de alíquota e recuperabilidade de imposto baseada no uso do item.

### ZX_FC_PRODUCT_CATEGORIES_V
**Descrição:** View de categorias fiscais de produto, usadas para classificação tributária de itens comprados (ex.: NCM no Brasil, HSN na Índia).
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificação tributária de itens para determinação de alíquotas.

### ZX_FC_PRODUCT_FISCAL_V
**Descrição:** View de classificações fiscais de produto, combinando categorias e atributos fiscais para determinação completa de impostos.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Determinação de tratamento fiscal completo por produto.

### ZX_FC_USER_DEFINED_V
**Descrição:** View de classificações fiscais definidas pelo usuário, permitindo extensão do modelo fiscal com critérios customizados.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificações fiscais específicas da empresa para regras tributárias customizadas.

### ZX_PRODUCT_TYPES_V
**Descrição:** View de tipos de produto para fins fiscais (Goods, Services), usada como critério na determinação de impostos.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Diferenciação fiscal entre bens e serviços em compras.

### ZX_WHT_TAX_CLASSIFICATION_V
**Descrição:** View de classificações de retenção na fonte (Withholding Tax), definindo regras de retenção de impostos sobre pagamentos a fornecedores.
**Módulo:** Tax (referência cruzada)
**Uso típico:** Classificação de retenção fiscal para pagamentos a fornecedores (IRF, PIS, COFINS, CSLL, ISS no Brasil).

---

> **Nota:** Tabelas com sufixo `_B` são tabelas base, `_TL` são tabelas de tradução, `_VL` são views que combinam base + tradução no idioma da sessão, `_V` são views genéricas, `_ALL` indica multi-org (todas as business units), `_M` indica tabela com versionamento date-effective, e `_F` indica tabela date-effective do HCM.
