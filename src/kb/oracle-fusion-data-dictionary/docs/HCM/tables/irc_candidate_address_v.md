---
id: DOC-HCM-460
doc_type: system-doc
title: "IRC_CANDIDATE_ADDRESS_V — Enderecos de Candidatos (View)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - candidate-address
  - irc-recruiting
aliases:
  - IRC_CANDIDATE_ADDRESS_V
  - irc_candidate_address_v
  - candidate-address-v
  - candidate-address-hcm
  - irc-candidate-address-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CANDIDATE_ADDRESS_V

## Visao Geral

**View** que consolida **enderecos** dos candidatos. Dados de localizacao normalizados.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto de consulta que consolida dados de multiplas tabelas. Pode ter restricoes em operacoes DML.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta simplificada:** Agrega enderecos em formato acessivel.
- **Localizacao geografica:** Filtros por regiao/cidade.
- **Diversidade geografica:** Distribuicao por localidade.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Referencia ao candidato | IRC_CANDIDATES | 🟢 90% |
| 2 | ADDRESS_ID | NUMBER(18) | NOT NULL | PK | Identificador do endereco | — | 🟢 85% |
| 3 | ADDRESS_LINE_1 | VARCHAR2(240) | NULL | Dados | Linha 1 do endereco | — | 🟢 85% |
| 4 | CITY | VARCHAR2(100) | NULL | Dados | Cidade | — | 🟢 85% |
| 5 | STATE | VARCHAR2(100) | NULL | Dados | Estado | — | 🟢 85% |
| 6 | POSTAL_CODE | VARCHAR2(30) | NULL | Dados | CEP | — | 🟢 85% |
| 7 | COUNTRY | VARCHAR2(60) | NULL | Dados | Pais | — | 🟢 85% |
| 8 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Classificacao | Endereco principal (Y/N) | — | 🟡 75% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_candidates]] — via `CANDIDATE_ID` (candidato titular do endereco)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Endereco principal
```sql
SELECT ca.CANDIDATE_ID, ca.CITY, ca.STATE, ca.COUNTRY
FROM   IRC_CANDIDATE_ADDRESS_V ca
WHERE  ca.PRIMARY_FLAG = 'Y'
  AND  ca.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `PRIMARY_FLAG = 'Y'` — Principal
- `COUNTRY = 'BR'` — Brasil
---

## Observacoes

- View (_V) — pode ter restricoes DML.
- Dados sensiveis — LGPD.
---

## Referencias

- [Oracle Docs -- IRC_CANDIDATE_ADDRESS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandidateaddressv.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
