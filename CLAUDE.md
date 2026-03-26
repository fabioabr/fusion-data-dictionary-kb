# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Idioma

Toda documentação e comunicação neste repositório é em **português brasileiro (pt-BR)**.

## Visão Geral do Projeto

Repositório de **arquitetura e base de conhecimento** do Banco Patria para construção de uma **base de conhecimento corporativa com GraphRAG** (Neo4j + embeddings + agentes de IA). Contém ADRs, blueprints, documentação formal, apresentações HTML e um pipeline automatizado de amadurecimento de documentos.

**Premissa central:**
- **Git** = origem da verdade (documentos Markdown com front matter estruturado)
- **Neo4j** = projeção operacional (grafo + vetor + metadados)
- **Agentes de IA** = consumidores controlados via recuperação híbrida
- **Obsidian** = ferramenta de edição e navegação da KB (wikilinks `[[...]]`)

## Estrutura do Repositório

```
├── CLAUDE.md                 # Este arquivo (raiz do projeto)
├── Visão.txt                 # Estratégia Incorta MCP (discovery de dicionário de dados)
├── c.bat                     # Atalho: claude --dangerously-skip-permissions
├── .obsidian/                # Configuração do Obsidian (raiz)
├── .claude/                  # Configuração e skills do Claude Code
│   ├── behavior/             # Diretrizes comportamentais para o Claude
│   │   ├── onboarding_information.md   # Parâmetros corporativos (preenchido 1x por org)
│   │   ├── schema_front_matter.md      # Schema de validação do front matter
│   │   ├── kb_gen/obsidian_kb_guide.md # Regras de escrita para Obsidian/IA
│   │   └── ui_ux/                      # Design system (playground.html + design_system.md)
│   ├── skills/               # Skills especializadas do pipeline
│   └── samples/              # Exemplos de referência
├── assets/                   # Logos e recursos visuais (logos, onboarding, variáveis)
├── docs/                     # Artefatos publicados (saída final)
│   ├── index.html            # Portal de navegação
│   ├── adrs/                 # ADRs em HTML (apresentações finais)
│   └── assets/               # Logos (dark/light, small/medium)
└── src/                      # Fontes e pipeline de produção
    ├── .obsidian/            # Configuração do Obsidian (workspace src)
    ├── diagrams/             # Diagramas draw.io
    ├── kb/                   # Knowledge Base (conteúdo principal)
    │   ├── rag-blueprint-adrs-draft/   # ADRs em desenvolvimento
    │   │   ├── draft/        # .txt — rascunhos, iteração livre
    │   │   └── beta/         # .beta.md — front matter leve, pré-promoção
    │   └── rag-blueprint-adrs-kb/      # ADRs formalizados
    │       ├── docs/         # .md — front matter rico, base de conhecimento
    │       └── presentation/ # .html — apresentações standalone
    └── pendings/             # Itens em aberto
        ├── human pendings/   # Pendências que requerem decisão humana
        └── planos/           # Planos de reorganização e inventários
```

## Pipeline de Amadurecimento de Documentos (4 Fases)

O pipeline é definido pelo ADR-001 e orquestrado pela skill `pipeline-master`:

```
.txt (draft) → .beta.md (front matter leve) → .md (front matter rico) → .html (apresentação)
```

| Fase | Entrada | Saída | Skills envolvidas |
|------|---------|-------|-------------------|
| 1 — Draft | Captura livre | `.txt` | `drf-writer`, `drf-reviewer` |
| 2 — Beta | `.txt` | `.beta.md` | `doc-writer` / `adr-writer` |
| 3 — Promoção | `.beta.md` | `.md` formal | `doc-writer` / `adr-writer`, `compliance-auditor` |
| 4 — Apresentação | `.md` | `.html` standalone | `prs-writer` |

Cada promoção passa por QA com scores (média atual: ~98% nos `.md`).

## Skills Disponíveis (`.claude/skills/`)

| Skill | Função |
|-------|--------|
| `pipeline-master` | Orquestra o fluxo completo de amadurecimento |
| `adr-writer` | Gera ADRs em `.md` formal |
| `adr-reviewer` | Revisa ADRs com rigor técnico |
| `doc-writer` | Converte drafts `.txt` para `.md` formal |
| `drf-writer` | Curadoria de rascunhos `.txt` |
| `drf-reviewer` | Revisão de negócio (PO) dos drafts |
| `prs-writer` | Gera HTML (standalone ou linked) a partir de `.md` |
| `translator` | Traduz conteúdo pt-BR para EN/ES via MCP ollama-local |
| `rnb-writer` | Gera runbooks operacionais |
| `gls-writer` | Gera entradas de glossário |
| `compliance-auditor` | Valida contra regras corporativas, PII, classificação |
| `link-validator` | Varre wikilinks quebrados nos `.md` |

## Regras de Geração de Materiais

### Relatórios HTML — OBRIGATÓRIO

Ao gerar qualquer arquivo HTML, **SEMPRE** consultar o playground em `.claude/behavior/ui_ux/playground.html` como referência única de componentes e design tokens. O playground é a **fonte de verdade** — copiar HTML/CSS de componentes diretamente dele.

**Regras invioláveis:**
- Tema escuro padrão com toggle para claro
- Tipografia: **Poppins** (Google Fonts) — nenhuma outra
- Ícones: **Remix Icon** (CDN) — nenhuma outra biblioteca
- CSS e JS **inline** no modo standalone (self-contained, sem frameworks)
- Usar **exclusivamente design tokens** do playground (`var(--*)`)
- **Mínimo 2 abas** por documento (layout por `doc_type` definido na skill `prs-writer`)
- **Seletor de idioma** (PT-BR / EN / ES) com bandeiras SVG quando `.i18n.md` existir
- **i18n via `data-i18n`** + dicionário JS (não blocos duplicados)
- **Botão back-to-top** flutuante
- **Header e Footer fixos** — gradiente escuro (`#1a2332 → #15202e → #1a2838`) em ambos os temas, nunca muda
- **Logo dark sempre visível** — como header é sempre escuro, usar apenas logo-dark
- **Aba ativa** usa `var(--bg)` como background (acompanha o tema da página)
- Estrutura: Header (gradiente fixo + logo dark + badges + bandeiras + toggle) → Tabs → Conteúdo → Footer (gradiente fixo)

**Componentes disponíveis** (ver playground):
- Header com logo, título, subtítulo, badges, seletor de idioma, toggle tema
- Tabs com `tab-count` badges
- Stats grid (KPIs com ícone colorido)
- Cards com `card-header-icon` + `card-title` + `card-badge`
- Intro text (borda esquerda accent)
- Alerts (info, warning, danger, success)
- Pills (inline badges)
- Tabelas com `table-wrapper`
- Busca/filtro com `search-input`
- Group cards com collapse
- Phase flow (diagrama horizontal)
- Footer (avatar + autor + doc info + selo)
- Back-to-top flutuante

**Componentes removidos** (NÃO usar):
- ~~delivery-card/delivery-item~~ → usar cards + pills
- ~~milestone/roadmap~~ → usar phase-flow
- ~~progress-bar~~ → usar stats ou pills
- ~~area-card~~ → usar cards genéricos
- ~~badge-footer (antigo)~~ → usar footer novo
- ~~JointJS/ELK diagramas~~ → removido do design system
- ~~legend-dot~~ → usar pills

### Front Matter Obrigatório (`.md` em `docs/`)

Validado pelo schema em `.claude/behavior/schema_front_matter.md`. Campos-chave:

```yaml
---
id: ADR-001               # Prefixos: ADR-NNN, GLS-NNN, RNB-NNN, DOC-NNNNNN, RAG-BNN
doc_type: adr              # system-doc | adr | runbook | glossary | task-doc | architecture-doc | review
status: approved           # draft | in-review | approved | deprecated
confidentiality: internal  # public | internal | restricted | confidential
# + title, system, module, domain, owner, team, tags, created_at, updated_at
---
```

### Documentos Obsidian

Seguir regras de `.claude/behavior/kb_gen/obsidian_kb_guide.md`:
- **Atomicidade** — um conceito por arquivo
- **Wikilinks** — todo conceito referenciado deve usar `[[link]]`
- Nomes em lowercase com `_` (underscore)

## Convenções

- Documentos sempre em pt-BR
- Nenhum pipeline roda sem `onboarding_information.md` preenchido
- Front matter com valores fora do schema é **bloqueante** — não gerar o arquivo
- Confidencialidade aplicada como filtro pré-retrieval (nunca confiar só em prompt)
- ADRs respondem "O QUE decidimos, POR QUE, e alternativas descartadas" — procedimentos vão em runbooks, schemas em specs

## Contexto: Incorta MCP Discovery

O arquivo `Visão.txt` descreve a estratégia para discovery do Incorta via MCP:

```
LLM / Agente → MCP Server → Conector Incorta (SQL / API) → Incorta Engine
```

Objetivo: extrair dicionário de dados (tabelas, views, colunas, tipos). Pós-discovery: classificação → regras de negócio → migração → reconstrução no BigQuery.
