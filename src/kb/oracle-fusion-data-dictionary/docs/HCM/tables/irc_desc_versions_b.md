---
id: DOC-HCM-480
doc_type: system-doc
title: "IRC_DESC_VERSIONS_B — Versoes de Descricoes (Base)"
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
  - desc-versions
  - irc-recruiting
aliases:
  - IRC_DESC_VERSIONS_B
  - irc_desc_versions_b
  - desc-versions-b
  - desc-versions-hcm
  - irc-desc-versions-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_DESC_VERSIONS_B

## Visao Geral

**Versoes** de descricoes de recrutamento. Tabela base (`_B`) com historico versionado.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Versionamento:** Historico de alteracoes em descricoes.
- **Auditoria:** Rastreabilidade por versao.
- **Rollback:** Reverter para versoes anteriores.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DESC_VERSION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | DESCRIPTION_ID | NUMBER(18) | NOT NULL | FK | Descricao | IRC_DESCRIPTIONS_B | 🟢 85% |
| 3 | VERSION_NUMBER | NUMBER | NOT NULL | Dados | Numero da versao | — | 🟡 80% |
| 4 | VERSION_STATUS | VARCHAR2(30) | NULL | Classificacao | Status (current, archived) | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_descriptions_b]] — via `DESCRIPTION_ID` (descricao de vaga da versao)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Versoes de uma descricao
```sql
SELECT dv.VERSION_NUMBER, dv.VERSION_STATUS
FROM   IRC_DESC_VERSIONS_B dv
WHERE  dv.DESCRIPTION_ID = :p_id
ORDER BY dv.VERSION_NUMBER DESC;
```

### Filtros comuns
- `VERSION_STATUS = 'CURRENT'` — Versao vigente
---

## Observacoes

- Tabela base (_B) — traducoes em IRC_DESC_VERSIONS_TL.
---

## Referencias

- [Oracle Docs -- IRC_DESC_VERSIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircdescversionsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
