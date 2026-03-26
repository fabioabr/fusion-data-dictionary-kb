---
id: DOC-PO-108
doc_type: system-doc
title: "PO_ACTION_HISTORY — Historico de Acoes em Documentos de Compras"
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
  - historico-acoes
  - workflow
  - approval
aliases:
  - PO_ACTION_HISTORY
  - po_action_history
  - po-action-history
  - po-action
  - historico-de-acoes-em-documentos-de
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ACTION_HISTORY

## 📌 Visão Geral

Armazena o **historico de acoes realizadas em documentos de compras** (POs, requisicoes, agreements). Cada registro representa uma acao de workflow — submissao, aprovacao, rejeicao, cancelamento — com timestamp, usuario e comentario.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de aprovacoes:** Rastreamento completo de aprovacoes/rejeicoes.
- **Workflow tracking:** Analise de tempo de ciclo e gargalos.
- **Compliance (SoD):** Segregacao de funcoes em compras.
- **Relatorios:** Tempo medio de aprovacao por tipo de documento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do documento (PO_HEADER_ID, etc.) | [[po_headers_all]] | 🟢 95% |
| 2 | OBJECT_TYPE_CODE | VARCHAR2(25) | NOT NULL | Classificacao | Tipo: PO, PA, RELEASE, REQUISITION | — | 🟢 95% |
| 3 | OBJECT_SUB_TYPE_CODE | VARCHAR2(25) | NULL | Classificacao | Subtipo do objeto | — | 🟢 90% |
| 4 | SEQUENCE_NUM | NUMBER | NOT NULL | PK | Sequencia da acao | — | 🟢 95% |
| 5 | ACTION_CODE | VARCHAR2(25) | NULL | Classificacao | SUBMIT, APPROVE, REJECT, RETURN, CANCEL | — | 🟢 95% |
| 6 | ACTION_DATE | DATE | NULL | Data | Data da acao | — | 🟢 95% |
| 7 | EMPLOYEE_ID | NUMBER(18) | NULL | FK | Funcionario executor | [[per_all_people_f]] | 🟢 90% |
| 8 | NOTE | VARCHAR2(4000) | NULL | Texto livre | Comentario/justificativa | — | 🟢 90% |
| 9 | OBJECT_REVISION_NUM | NUMBER | NULL | Versionamento | Revisao do documento | — | 🟢 85% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `OBJECT_ID` (pedido de compra associado à ação registrada)
- [[per_all_people_f]] — via `EMPLOYEE_ID` (funcionário que executou a ação no PO)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Historico de acoes de um PO
```sql
SELECT SEQUENCE_NUM, ACTION_CODE, ACTION_DATE, EMPLOYEE_ID, NOTE
FROM   PO_ACTION_HISTORY
WHERE  OBJECT_ID = :p_po_header_id
  AND  OBJECT_TYPE_CODE = 'PO'
ORDER BY SEQUENCE_NUM;
```


---

## 🔒 Observações

- PK composta: `OBJECT_ID` + `OBJECT_TYPE_CODE` + `SEQUENCE_NUM`.
- O `OBJECT_TYPE_CODE` determina a tabela-pai (PO, REQUISITION, etc.).
- Acoes automaticas podem ter `EMPLOYEE_ID` nulo.
- Campo `NOTE` contem justificativas obrigatorias em rejeicoes.

---

## 📚 Referências

- [Oracle Docs — PO_ACTION_HISTORY](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poactionhistory-25428.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
