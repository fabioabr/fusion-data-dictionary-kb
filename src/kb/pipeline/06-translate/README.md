# Passo 06 — Traduzir Conteudo I18N

## Objetivo

Traduzir os itens dos arquivos `.i18n.json` de pt-BR para EN e ES,
utilizando Ollama local (`translategemma:4b`) ou Claude Opus como fallback.

## DoR (Definition of Ready)

- Passo 05 concluido: arquivos `.i18n.json` existem com `items[].br` preenchido
- Ollama rodando em `localhost:11434` com modelo `translategemma:4b` carregado

## DoD (Definition of Done)

- Todos os `items[]` possuem campos `en` e `es` preenchidos (nao null)
- Campo `translated_at` atualizado com timestamp ISO 8601
- Traducoes sao naturais e contextualmente corretas

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.i18n.json`
- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.i18n.json`

## Saida

- Mesmos arquivos `.i18n.json`, com campos `en` e `es` preenchidos

## Requer LLM

| Motor | Tipo |
|-------|------|
| Ollama (`translategemma:4b`) | Local (preferencial) |
| Claude Opus (Anthropic API) | Fallback |

## Uso

```bash
python scripts/06-translate/translate_json.py --batch src/kb/.../GL/tables/
python scripts/06-translate/translate_json.py src/kb/.../GL/tables/GL_JE_HEADERS.i18n.json
python scripts/06-translate/batch_translate.py --module GL --lang en,es
```

## Notas

- Priorizar Ollama local para custo zero (`translategemma:4b` e rapido)
- O script traduz item a item, nao em batch, para melhor qualidade
- Itens ja traduzidos sao pulados (campo != null), use `--force` para retraduzir
- Velocidade media: ~2 seg/item no Ollama, ~0.5 seg/item no Opus
- Configuracao Ollama em `scripts/config/modules.json`
