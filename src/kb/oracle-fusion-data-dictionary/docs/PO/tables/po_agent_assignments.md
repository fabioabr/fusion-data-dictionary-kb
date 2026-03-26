---
id: DOC-PO-110
doc_type: system-doc
title: "PO_AGENT_ASSIGNMENTS — Atribuicoes de Categorias por Comprador"
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
  - compradores
  - buyers
  - agents
aliases:
  - PO_AGENT_ASSIGNMENTS
  - po_agent_assignments
  - po-agent-assignments
  - po-agent
  - atribuicoes-de-categorias-por-compr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_AGENT_ASSIGNMENTS

## 📌 Visão Geral

Armazena as **atribuicoes de categorias de compras a compradores** (agents). Define quais categorias cada comprador esta autorizado a comprar.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Segregacao:** Especializacao por categoria de produto/servico.
- **Roteamento automatico:** Direciona requisicoes ao comprador correto.
- **Controle de alcada:** Restricoes por categoria alem do limite financeiro.
- **Relatorios de carga:** Distribuicao de trabalho entre compradores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | ID da atribuicao | — | 🟡 80% |
| 2 | AGENT_ID | NUMBER(18) | NOT NULL | FK | Comprador | [[po_agents_v]] | 🟢 95% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[egp_categories_b]] | 🟢 90% |
| 4 | ITEM_ID | NUMBER(18) | NULL | FK | Item especifico (opcional) | [[egp_system_items_b]] | 🟡 75% |
| 5 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_agents_v]] — via `AGENT_ID` (comprador atribuído à designação)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de item atribuída ao comprador)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da atribuição do comprador)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Categorias de um comprador
```sql
SELECT AGENT_ID, CATEGORY_ID
FROM   PO_AGENT_ASSIGNMENTS
WHERE  AGENT_ID = :p_agent_id;
```


---

## 🔒 Observações

- Atribuicao por categoria ou item especifico.
- Sem atribuicao, comprador pode ter acesso irrestrito (depende da config).
- Utilizada pelo AutoCreate para roteamento.

---

## 📚 Referências

- [Oracle Docs — PO_AGENT_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
