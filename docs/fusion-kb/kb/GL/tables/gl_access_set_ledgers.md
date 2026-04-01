---
id: DOC-GL-005
doc_type: system-doc
title: "GL_ACCESS_SET_LEDGERS — Ledgers Associados a Conjuntos de Acesso"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - acesso
  - ledger
  - seguranca
aliases:
  - GL_ACCESS_SET_LEDGERS
  - gl_access_set_ledgers
  - ledgers-acesso-gl
  - access-set-ledgers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ACCESS_SET_LEDGERS

## Visao Geral

Armazena a **associação entre conjuntos de acesso e ledgers** no General Ledger. Cada registro indica que um determinado ledger faz parte de um Data Access Set, podendo incluir restrições por segmento de valor (balancing segment, management segment). É a tabela que define o escopo detalhado de ledgers acessíveis por conjunto.

> [!note] Granularidade de acesso
> Além de incluir o ledger no conjunto, esta tabela permite restringir o acesso a valores específicos de segmentos contábeis — por exemplo, permitir acesso ao ledger apenas para a empresa "01" ou centro de custo "100".

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Definição de escopo de ledgers:** Especifica quais ledgers estão incluídos em cada Data Access Set.
- **Restrição por segmento:** Permite limitar o acesso a valores específicos do balancing segment ou management segment dentro de um ledger.
- **Configuração multi-entidade:** Suporta cenários onde um usuário precisa acessar múltiplos ledgers com diferentes restrições.
- **Auditoria de configuração:** Permite revisar quais ledgers e segmentos estão acessíveis por conjunto.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCESS_SET_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do conjunto de acesso | [[gl_access_sets]] | 🟢 95% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger incluído | [[gl_ledgers]] | 🟢 95% |
| 3 | ACCESS_PRIVILEGE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Nível de acesso ao ledger: READ_ONLY, READ_AND_WRITE | — | 🟢 90% |
| 4 | SEGMENT_VALUE_FROM | VARCHAR2(25) | NULL | Filtro | Valor inicial do segmento para restrição (range) | — | 🟡 75% |
| 5 | SEGMENT_VALUE_TO | VARCHAR2(25) | NULL | Filtro | Valor final do segmento para restrição (range) | — | 🟡 75% |
| 6 | ALL_SEGMENT_VALUES_FLAG | VARCHAR2(1) | NULL | Controle | Indica se todos os valores do segmento são acessíveis (Y/N) | — | 🟡 75% |
| 7 | LEDGER_SET_ID | NUMBER(18) | NULL | FK | ID do ledger set, quando aplicável | [[gl_ledgers]] | 🟡 70% |
| 8 | LINK_ID | NUMBER(18) | NULL | Sistema | ID de vínculo interno para agrupamento | — | 🟡 65% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_access_sets]] — via `ACCESS_SET_ID` (conjunto de acesso)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger incluído)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de interseção (leaf table).

---

## Uso Tipico

### Ledgers em um conjunto de acesso
```sql
SELECT asl.ACCESS_SET_ID, das.NAME AS access_set,
       asl.LEDGER_ID, gl.NAME AS ledger,
       asl.ACCESS_PRIVILEGE_CODE,
       asl.ALL_SEGMENT_VALUES_FLAG,
       asl.SEGMENT_VALUE_FROM, asl.SEGMENT_VALUE_TO
FROM   GL_ACCESS_SET_LEDGERS asl
JOIN   GL_ACCESS_SETS das ON das.ACCESS_SET_ID = asl.ACCESS_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = asl.LEDGER_ID
WHERE  asl.ACCESS_SET_ID = :p_access_set_id
ORDER BY gl.NAME;
```

### Conjuntos com acesso restrito por segmento
```sql
SELECT das.NAME AS access_set, gl.NAME AS ledger,
       asl.SEGMENT_VALUE_FROM, asl.SEGMENT_VALUE_TO
FROM   GL_ACCESS_SET_LEDGERS asl
JOIN   GL_ACCESS_SETS das ON das.ACCESS_SET_ID = asl.ACCESS_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = asl.LEDGER_ID
WHERE  asl.ALL_SEGMENT_VALUES_FLAG = 'N';
```

### Filtros comuns
- `ALL_SEGMENT_VALUES_FLAG = 'Y'` — Acesso a todos os valores do segmento
- `ALL_SEGMENT_VALUES_FLAG = 'N'` — Acesso restrito a faixa de valores
- `ACCESS_PRIVILEGE_CODE = 'READ_AND_WRITE'` — Permissão de escrita

---

## Observacoes

- Quando `ALL_SEGMENT_VALUES_FLAG = 'Y'`, os campos `SEGMENT_VALUE_FROM` e `SEGMENT_VALUE_TO` são ignorados — o acesso abrange todos os valores do segmento.
- Quando `ALL_SEGMENT_VALUES_FLAG = 'N'`, a faixa definida por `SEGMENT_VALUE_FROM` e `SEGMENT_VALUE_TO` restringe quais valores do segmento de segurança são acessíveis.
- A mesma combinação `ACCESS_SET_ID` + `LEDGER_ID` pode ter múltiplas linhas se houver diferentes faixas de segmento definidas.
- O `LEDGER_SET_ID` é preenchido quando o acesso é concedido via ledger set (agrupamento de ledgers) em vez de ledger individual.

---

## Referencias

- [Oracle Docs — GL_ACCESS_SET_LEDGERS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glaccesssetledgers-25068.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL

---

## 🔗 PVOs Relacionados

### [[dataaccesssetledgerpvo|DataAccessSetLedgerPVO]] (GL · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_PRIVILEGE_CODE | DasLedgerAccessPrivilegeCode | — |
| ACCESS_SET_ID | AccessSetId | ✅ |
| CREATED_BY | DasLedgerCreatedBy | — |
| CREATION_DATE | DasLedgerCreationDate | — |
| END_DATE | DasLedgerEndDate | — |
| LAST_UPDATE_DATE | DasLedgerLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DasLedgerLastUpdateLogin | — |
| LAST_UPDATED_BY | DasLedgerLastUpdatedBy | — |
| LEDGER_ID | LedgerId | ✅ |
| START_DATE | DasLedgerStartDate | — |
