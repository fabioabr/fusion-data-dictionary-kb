---
id: DOC-HCM-641
doc_type: system-doc
title: "PER_CHECKLIST_CONTACTS — Contatos de Template de Checklist"
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
  - workforce-management
  - checklists
  - contatos-template
aliases:
  - PER_CHECKLIST_CONTACTS
  - per_checklist_contacts
  - per-checklist-contacts
  - contatos-de-template-de-checklist
  - per-checklist-contac
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHECKLIST_CONTACTS

## 📌 Visão Geral

Armazena os **contatos padrão** definidos no template de checklist. Estes contatos são copiados para as instâncias alocadas quando o checklist é atribuído a um colaborador.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de contatos padrão** — define os contatos que serão replicados em cada instância.
- **Padronização** — garante que todo checklist alocado tenha os contatos apropriados.
- **Suporte** — identifica automaticamente os pontos de contato para o colaborador.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECKLIST_CONTACT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do contato | — | 🟢 90% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Template de checklist | PER_CHECKLISTS_B | 🟢 90% |
| 3 | CONTACT_ROLE | VARCHAR2(30) | NULL | Classificação | Papel do contato (HR, BUDDY, MANAGER) | — | 🟡 75% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (template de checklist do contato)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Contatos de um template de checklist
```sql
SELECT pcc.CONTACT_ROLE
FROM   PER_CHECKLIST_CONTACTS pcc
WHERE  pcc.CHECKLIST_ID = :p_checklist_id;
```

### Filtros comuns
- `CONTACT_ROLE = 'HR'` — Contatos de RH
---

## 🔒 Observações

- Contatos do template são copiados para PER_ALLOC_CHKLST_CONTACTS ao alocar o checklist.
- A definição no template garante consistência nos contatos de todas as instâncias.
---

## 📚 Referências

- [Oracle Docs — PER_CHECKLIST_CONTACTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchecklistcontacts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
