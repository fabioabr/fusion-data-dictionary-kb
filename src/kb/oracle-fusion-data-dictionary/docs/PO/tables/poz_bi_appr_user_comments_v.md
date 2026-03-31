---
id: DOC-PO-072
doc_type: system-doc
title: "POZ_BI_APPR_USER_COMMENTS_V — View BI de Comentários de Aprovação de Fornecedores"
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
  - fornecedores
  - aprovacao
  - bi
  - view
aliases:
  - POZ_BI_APPR_USER_COMMENTS_V
  - poz_bi_appr_user_comments_v
  - bi-comentarios-aprovacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BI_APPR_USER_COMMENTS_V

## 📌 Visão Geral

View otimizada para **Business Intelligence** que expõe os comentários e ações dos aprovadores no workflow de cadastro e manutenção de fornecedores. Desnormaliza dados de `POZ_APPROVAL_HISTORY` com informações do usuário e do objeto aprovado para facilitar análises em OTBI e ferramentas de BI.

> [!note] Prefixo BI
> Views com prefixo `_BI_` são projetadas para consumo por ferramentas de BI (OTBI, BICC) e não devem ser usadas em lógica transacional.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Relatórios OTBI:** Análise de comentários e decisões de aprovação em dashboards.
- **Auditoria de compliance:** Evidência de revisão e aprovação de cadastros de fornecedores.
- **Análise de ciclo de aprovação:** Tempo médio entre submissão e aprovação.
- **Extração BICC:** Publicação de dados de aprovação para data warehouse corporativo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPROVAL_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador do registro de aprovação | [[poz_approval_history]] | 🟡 80% |
| 2 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do objeto aprovado | — | 🟡 75% |
| 3 | OBJECT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do objeto aprovado | — | 🟡 75% |
| 4 | ACTION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Ação: APPROVE, REJECT, RETURN, SUBMIT | — | 🟡 80% |
| 5 | ACTION_DATE | DATE | NOT NULL | Data | Data/hora da ação | — | 🟡 80% |
| 6 | APPROVER_NAME | VARCHAR2(360) | NULL | Descrição | Nome do aprovador | — | 🟡 75% |
| 7 | USER_COMMENT | VARCHAR2(4000) | NULL | Texto livre | Comentário do aprovador | — | 🟡 75% |
| 8 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor (desnormalizado) | — | 🟡 70% |
| 9 | SUPPLIER_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do fornecedor | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_approval_history]] — via `APPROVAL_HISTORY_ID` (histórico de aprovação)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta BI)

---

## 📎 Uso Típico

### Comentários de aprovação para relatórios
```sql
SELECT bac.SUPPLIER_NAME, bac.SUPPLIER_NUMBER,
       bac.ACTION_CODE, bac.ACTION_DATE,
       bac.APPROVER_NAME, bac.USER_COMMENT
FROM   POZ_BI_APPR_USER_COMMENTS_V bac
WHERE  bac.ACTION_DATE BETWEEN :start_date AND :end_date
ORDER BY bac.ACTION_DATE DESC;
```

### Rejeições com comentários
```sql
SELECT bac.SUPPLIER_NAME, bac.APPROVER_NAME,
       bac.USER_COMMENT, bac.ACTION_DATE
FROM   POZ_BI_APPR_USER_COMMENTS_V bac
WHERE  bac.ACTION_CODE = 'REJECT'
  AND  bac.USER_COMMENT IS NOT NULL;
```

---

## 🔒 Observações

- Esta é uma **view BI**, não uma tabela física — não aceita DML direto.
- Projetada para OTBI e BICC; pode ter performance inferior em queries transacionais de alto volume.
- Campos desnormalizados (ex: `SUPPLIER_NAME`) podem ficar desatualizados se a view não for refreshed.
- Para queries transacionais, use diretamente [[poz_approval_history]].

---

## 🔗 PVOs Relacionados

### [[supplierapprovalhistorypvo|SupplierApprovalHistoryPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_SEQ_NUM | SuppApprUserCommentsActionSeqNum | — |
| AMX_IDENTIFICATION_KEY | SuppApprUserCommentsAmxIdentificationKey | — |
| LATEST_COMMENT | SuppApprUserCommentsLatestComment | — |
| PERFORMER_ID | SuppApprUserCommentsPerformerId | — |

### [[supplierprofilechangeapprovalhistorypvo|SupplierProfileChangeApprovalHistoryPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_SEQ_NUM | ApprovalUserCommentPEOActionSeqNum | — |
| AMX_IDENTIFICATION_KEY | ApprovalUserCommentPEOAmxIdentificationKey | — |
| LATEST_COMMENT | ApprovalUserCommentPEOLatestComment | — |
| PERFORMER_ID | ApprovalUserCommentPEOPerformerId | — |

---

## 📚 Referências

- [Oracle Docs — POZ BI Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
