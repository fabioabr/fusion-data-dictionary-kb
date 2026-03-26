---
id: DOC-PO-099
doc_type: system-doc
title: "POZ_SUPP_RELATIONSHIP_VL — Relacionamentos de Fornecedores (Traduzida)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - supplier-relationships
  - hierarquia
  - relacionamentos
aliases:
  - POZ_SUPP_RELATIONSHIP_VL
  - poz_supp_relationship_vl
  - relacionamentos-fornecedor
  - supplier-relationships
  - hierarquia-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_RELATIONSHIP_VL

## Visão Geral

View traduzida (Value List) que apresenta os **relacionamentos entre fornecedores** no Oracle Fusion Procurement. Combina dados base (`_B`) com traduções (`_TL`) para exibir tipos de relacionamento (matriz/filial, parceiro, subcontratado, etc.) no idioma da sessão do usuário. Suporta hierarquias e vínculos comerciais entre entidades fornecedoras.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **Value List** — view que combina a tabela base (`_B`) com a tabela de traduções (`_TL`), retornando dados no idioma da sessão do usuário.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Hierarquia de fornecedores:** Definição de relacionamentos matriz/filial entre fornecedores.
- **Grupo econômico:** Identificação de fornecedores pertencentes ao mesmo grupo empresarial.
- **Subcontratação:** Registro de relacionamentos de subcontratação entre fornecedores.
- **Análise de spend consolidado:** Agrupamento de gastos por grupo econômico ou hierarquia.
- **Risk management:** Avaliação de risco considerando interdependências entre fornecedores.
- **Relatórios multilíngues:** Exibição de tipos de relacionamento traduzidos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RELATIONSHIP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do relacionamento | — | 🟡 70% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor de origem do relacionamento | [[poz_suppliers]] | 🟡 75% |
| 3 | RELATED_VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor relacionado (destino) | [[poz_suppliers]] | 🟡 75% |
| 4 | RELATIONSHIP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Código do tipo de relacionamento | — | 🟡 70% |
| 5 | RELATIONSHIP_TYPE_NAME | VARCHAR2(240) | NULL | Classificação | Nome traduzido do tipo de relacionamento | — | 🟡 70% |
| 6 | START_DATE | DATE | NULL | Vigência | Data de início do relacionamento | — | 🟡 65% |
| 7 | END_DATE | DATE | NULL | Vigência | Data de término do relacionamento | — | 🟡 65% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificação | Status: ACTIVE, INACTIVE | — | 🟡 65% |
| 9 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Observações sobre o relacionamento | — | 🟡 60% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor de origem)
- [[poz_suppliers]] — via `RELATED_VENDOR_ID` (fornecedor relacionado)

### Tabelas relacionadas

---

## Uso Típico

### Relacionamentos ativos de um fornecedor
```sql
SELECT sr.RELATED_VENDOR_ID, s.VENDOR_NAME AS related_name,
       sr.RELATIONSHIP_TYPE_NAME, sr.START_DATE
FROM   POZ_SUPP_RELATIONSHIP_VL sr
JOIN   POZ_SUPPLIERS s ON sr.RELATED_VENDOR_ID = s.VENDOR_ID
WHERE  sr.VENDOR_ID = :p_vendor_id
  AND  sr.STATUS = 'ACTIVE';
```

### Mapa de grupo econômico
```sql
SELECT sr.VENDOR_ID, s1.VENDOR_NAME AS from_name,
       sr.RELATED_VENDOR_ID, s2.VENDOR_NAME AS to_name,
       sr.RELATIONSHIP_TYPE_NAME
FROM   POZ_SUPP_RELATIONSHIP_VL sr
JOIN   POZ_SUPPLIERS s1 ON sr.VENDOR_ID = s1.VENDOR_ID
JOIN   POZ_SUPPLIERS s2 ON sr.RELATED_VENDOR_ID = s2.VENDOR_ID
WHERE  sr.RELATIONSHIP_TYPE = 'PARENT_SUBSIDIARY'
  AND  sr.STATUS = 'ACTIVE';
```

---

## Observações

- A view combina as tabelas base (`_B`) e tradução (`_TL`), retornando o `RELATIONSHIP_TYPE_NAME` no idioma da sessão.
- Os tipos de relacionamento comuns incluem: **PARENT_SUBSIDIARY** (matriz/filial), **SUBCONTRACTOR** (subcontratado), **PARTNER** (parceiro comercial).
- Relacionamentos são **bidirecionais**: se A é matriz de B, normalmente há um registro inverso (B é filial de A).
- A análise de spend consolidado por grupo econômico depende desta view para agrupar fornecedores relacionados.
- Fornecedores com `END_DATE` no passado ou `STATUS = 'INACTIVE'` representam relacionamentos encerrados.

---

## Referências

- [Oracle Docs — Supplier Relationships](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
