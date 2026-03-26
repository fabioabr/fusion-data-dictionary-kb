# Passo 03 — Gerar Descricoes Ricas para Tabelas

## Objetivo

Usar LLM (Claude Opus) para enriquecer os esqueletos .md com descricoes de negocio: visao geral, descricao de colunas, relacionamentos e SQL de exemplo.

## DOR (Definition of Ready)

- Passo 01 concluido: esqueletos .md existem em `{MODULE}/tables/`
- Variavel `ANTHROPIC_API_KEY` configurada
- Arquivo de variaveis corporativas disponivel (`docs/assets/variaveis.md`)

## DOD (Definition of Done)

- Cada .md contem secoes: Visao Geral, Descricao de Colunas (tabela), Relacionamentos, SQL de Exemplo
- Descricoes sao em pt-BR, contextualizadas para Oracle Fusion
- Nenhuma coluna ficou sem descricao (campo "Descricao" preenchido)
- Front matter atualizado com status: in-review

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.md` (esqueleto)
- `docs/assets/variaveis.md` (contexto corporativo)

## Saida

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE}.md` (enriquecido)

## Requer LLM

Sim — Claude Opus (Anthropic API).

## Uso

```bash
python scripts/03-generate-table-descriptions/generate_table_descriptions.py --batch src/kb/oracle-fusion-data-dictionary/docs/GL/tables/
python scripts/03-generate-table-descriptions/generate_table_descriptions.py src/kb/.../GL/tables/GL_JE_HEADERS.md
python scripts/03-generate-table-descriptions/generate_table_descriptions.py --module GL --limit 5
```

## Notas

- Custo estimado: ~0.02 USD por tabela (prompt ~3K tokens + resposta ~2K tokens)
- O script inclui retry com backoff exponencial para rate limiting
- Sempre testar com 1-3 arquivos antes de rodar batch (validacao iterativa)
- O LLM recebe contexto de tabelas relacionadas para gerar relacionamentos
- Re-execucao pula arquivos que ja possuem secao "Visao Geral" preenchida
