# Passo 09 — Gerar Indice por Modulo

## Objetivo

Gerar um `index.html` por modulo contendo grid de cards com links para
todas as tabelas e PVOs do modulo, com contadores e busca.

## DoR (Definition of Ready)

- Passo 07 concluido: HTMLs de tabelas gerados
- Passo 08 concluido: HTMLs de PVOs gerados
- `scripts/config/modules.json` com metadados dos modulos

## DoD (Definition of Done)

- Um `index.html` por modulo em `docs/fusion-kb/data-dictionary/{MODULE}/`
- Grid de cards com: nome da tabela/PVO, descricao curta, link
- Contadores corretos (total tabelas, total PVOs)
- Busca/filtro funcional
- Design system consistente com HTMLs individuais

## Entrada

- `docs/fusion-kb/data-dictionary/{MODULE}/tables/*.html` (metadados)
- `docs/fusion-kb/data-dictionary/{MODULE}/pvos/*.html` (metadados)
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/*.md` (descricoes)
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/*.json` (descricoes)
- `scripts/config/modules.json`

## Saida

- `docs/fusion-kb/data-dictionary/{MODULE}/index.html`

## Requer LLM

Nao.

## Uso

```bash
python scripts/09-build-module-index/build_module_index.py --module GL
python scripts/09-build-module-index/build_module_index.py --all
```

## Notas

- O indice e regenerado do zero a cada execucao (nao incremental)
- Cards de tabelas e PVOs sao separados em secoes distintas
- Icone e cor do modulo vem de `modules.json`
- Inclui breadcrumb: Portal > Modulo
- Busca filtra por nome e descricao em tempo real (JS client-side)
