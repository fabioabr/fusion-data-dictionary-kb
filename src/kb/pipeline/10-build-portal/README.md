# Passo 10 — Atualizar Portal Principal

## Objetivo

Atualizar o portal principal (`docs/index.html`) com contadores atualizados
de tabelas, PVOs e modulos, refletindo o estado atual da documentacao.

## DoR (Definition of Ready)

- Passo 09 concluido: `index.html` por modulo gerado
- `docs/index.html` existente (template do portal)
- `scripts/config/modules.json` com metadados dos modulos

## DoD (Definition of Done)

- `docs/index.html` atualizado com:
  - Total de tabelas documentadas
  - Total de PVOs documentados
  - Numero de modulos ativos
  - Cards de modulos com contadores corretos
- Portal navegavel e funcional

## Entrada

- `docs/fusion-kb/data-dictionary/{MODULE}/tables/*.html` (contagem)
- `docs/fusion-kb/data-dictionary/{MODULE}/pvos/*.html` (contagem)
- `docs/index.html` (template existente)
- `scripts/config/modules.json` (metadados dos modulos)

## Saida

- `docs/index.html` (atualizado)

## Requer LLM

Nao.

## Uso

```bash
python scripts/10-build-portal/build_portal.py
```

## Notas

- O script apenas atualiza contadores e cards — nao altera layout/design
- Modulos sem nenhum HTML sao omitidos dos cards
- Execucao e idempotente e segura para re-execucao
- O portal e o ponto de entrada para GitHub Pages
