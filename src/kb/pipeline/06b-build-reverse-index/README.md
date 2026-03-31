# Passo 06b — Gerar Indice Reverso Tabela → PVOs

## Objetivo

Gerar um mapa reverso que, para cada tabela, lista todos os atributos de PVOs
que a referenciam como fonte de dados. Este indice alimenta a aba
"PVOs Relacionados" nos HTMLs de tabelas (passo 07).

## DoR (Definition of Ready)

- Passo 02 concluido: JSONs de PVOs extraidos em `docs/{MODULE}/pvos/`
- Passo 04 concluido: descricoes de PVOs geradas (`meta.description` preenchido)
- Passo 06 concluido: `.i18n.json` com traducoes EN/ES dos PVOs

## DoD (Definition of Done)

- Arquivo `scripts/config/table_to_pvos_map.json` gerado
- Cada tabela contem lista de atributos de PVO mapeados (coluna, pvo_name, pvo_attr, module_code, bicc)
- PVOs duplicados entre modulos deduplicados (prioriza modulo nativo da tabela)
- Ordenado por pvo_name + column

## Entrada

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO}.json`
- `src/kb/oracle-fusion-data-dictionary/docs/table-mappings.txt` (para deduplicacao)

## Saida

- `scripts/config/table_to_pvos_map.json`

Estrutura do JSON:

```json
{
  "PER_ALL_PEOPLE_F": [
    {
      "column": "PERSON_ID",
      "pvo_name": "PersonPVO",
      "pvo_attr": "PersonId",
      "module_code": "HCM",
      "bicc": true
    }
  ]
}
```

## Requer LLM

Nao.

## Uso

```bash
python scripts/06b-build-reverse-index/build_reverse_index.py
python scripts/06b-build-reverse-index/build_reverse_index.py --src-dir <docs_dir> --output <path>
```

## Notas

- Processa ~4.200 PVO JSONs em ~6 segundos
- Gera ~390.000 mapeamentos de atributos para ~2.900 tabelas
- Deduplicacao: PVOs identicos em modulos diferentes (ex: HCM + OTHER) sao mantidos apenas uma vez, priorizando o modulo nativo da tabela (via `table-mappings.txt`)
- So precisa ser re-executado quando PVO JSONs mudam (passos 02 ou 04)
- O passo 07 (BUILD-TABLE-HTML) carrega este arquivo automaticamente via auto-discovery em `scripts/config/`
