# Passo 04 — Gerar Descricoes de Negocio para PVOs

## Objetivo

Usar LLM (Claude Opus) para preencher o campo `meta.description` dos arquivos .json de PVO com descricoes de negocio contextualizadas.

## DOR (Definition of Ready)

- Passo 02 concluido: arquivos .json de PVO existem em `{MODULE}/pvos/`
- Variavel `ANTHROPIC_API_KEY` configurada

## DOD (Definition of Done)

- Todo .json tem `meta.description` preenchido (nao null)
- Descricoes sao em pt-BR, claras e com contexto de negocio Oracle Fusion
- Atributos dos PVOs com descricoes preenchidas quando possivel

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.json`

## Saida

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.json` (atualizado)

## Requer LLM

Sim — Claude Opus (Anthropic API).

## Uso

```bash
python scripts/04-generate-pvo-descriptions/update_pvo_descriptions.py --batch src/kb/oracle-fusion-data-dictionary/docs/GL/pvos/
python scripts/04-generate-pvo-descriptions/update_pvo_descriptions.py src/kb/.../GL/pvos/GlBalancePVO.json
python scripts/04-generate-pvo-descriptions/update_pvo_descriptions.py --module AP --limit 3
```

## Notas

- Custo estimado: ~0.01 USD por PVO (prompt ~2K tokens + resposta ~500 tokens)
- O script pula PVOs que ja possuem `meta.description` preenchido
- Use `--force` para regenerar descricoes existentes
- Sempre testar com 1-3 arquivos antes de rodar batch
- Inclui retry com backoff exponencial para rate limiting
