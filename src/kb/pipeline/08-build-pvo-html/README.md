# Passo 08 — Gerar HTML de PVOs

## Objetivo

Gerar arquivos HTML standalone a partir dos `.json` de PVOs,
incorporando traducoes i18n e seguindo o design system do projeto.

## DoR (Definition of Ready)

- Passo 06 concluido: `.i18n.json` com traducoes EN/ES preenchidas
- Template HTML disponivel: `scripts/08-build-pvo-html/template_pvo.html`
- Playground de referencia: `.claude/behavior/ui_ux/playground.html`

## DoD (Definition of Done)

- Um `.html` por PVO em `docs/fusion-kb/data-dictionary/{MODULE}/pvos/`
- HTML e self-contained (CSS+JS inline, sem dependencias externas)
- Seletor de idioma funcional (PT-BR / EN / ES)
- Toggle tema claro/escuro funcional
- Minimo 2 abas: Visao Geral, Atributos

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.json`
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.i18n.json`
- `scripts/08-build-pvo-html/template_pvo.html`

## Saida

- `docs/fusion-kb/data-dictionary/{MODULE}/pvos/{PVO_NAME}.html`

## Requer LLM

Nao.

## Uso

```bash
python scripts/08-build-pvo-html/build_pvo_html.py --batch src/kb/.../GL/pvos/
python scripts/08-build-pvo-html/build_pvo_html.py src/kb/.../GL/pvos/GlBalancePVO.json
python scripts/08-build-pvo-html/build_pvo_html.py --module AP
```

## Notas

- O template usa design tokens do playground (`var(--*)`)
- Header e footer sempre em gradiente escuro, independente do tema
- Logo dark sempre visivel (header e sempre escuro)
- Tipografia: Poppins (Google Fonts), icones: Remix Icon (CDN)
- i18n via atributo `data-i18n` + dicionario JS embutido
- Re-execucao sobrescreve HTMLs existentes
