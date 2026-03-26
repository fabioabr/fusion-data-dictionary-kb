---
id: DOC-HCM-695
doc_type: system-doc
title: "PER_PERSON_TYPE_USAGES_M — Usos de Tipo de Pessoa"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - tipo-pessoa-uso
  - person-type-usage
  - classificacao
aliases:
  - PER_PERSON_TYPE_USAGES_M
  - per_person_type_usages_m
  - usos-tipo-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_TYPE_USAGES_M

## Visão Geral

Armazena a **associação entre pessoas e seus tipos** ao longo do tempo. Permite que uma mesma pessoa possua múltiplos tipos simultaneamente (ex: empregado e contato de emergência) e rastreia mudanças de tipo (ex: candidato promovido a empregado).

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **Master** — tabela principal que armazena dados transacionais com histórico.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Ciclo de vida do colaborador** — registrar transições (candidato → empregado → desligado)
- **Classificação simultânea** — pessoa pode ser empregado e contato ao mesmo tempo
- **Relatórios de headcount** — contabilizar pessoas por tipo ativo
- **Segurança por tipo** — conceder permissões baseadas no tipo de pessoa vigente
- **Auditoria de transições** — rastrear mudanças de tipo ao longo do tempo

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_TYPE_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso de tipo | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | PERSON_TYPE_ID | NUMBER(18) | NOT NULL | FK | Referência ao tipo de pessoa | PER_PERSON_TYPES | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início do uso do tipo | — | 🟢 90% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim do uso do tipo | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa do uso de tipo de pessoa)
- [[per_person_types]] — via `PERSON_TYPE_ID` (tipo de pessoa utilizado)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Tipo atual de uma pessoa
```sql
SELECT ptu.PERSON_TYPE_ID, pt.SYSTEM_PERSON_TYPE
FROM   PER_PERSON_TYPE_USAGES_M ptu
JOIN   PER_PERSON_TYPES pt ON pt.PERSON_TYPE_ID = ptu.PERSON_TYPE_ID
WHERE  ptu.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN ptu.EFFECTIVE_START_DATE AND ptu.EFFECTIVE_END_DATE;
```

---

## Observações

- Uma pessoa pode ter múltiplos tipos ativos simultaneamente.
- A vigência (`EFFECTIVE_START_DATE` / `EFFECTIVE_END_DATE`) controla quando cada tipo é válido.
- Transições de tipo (ex: candidato → empregado) geram novos registros.

---

## Referências

- [Oracle Docs — PER_PERSON_TYPE_USAGES_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersontypeusagesm.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
