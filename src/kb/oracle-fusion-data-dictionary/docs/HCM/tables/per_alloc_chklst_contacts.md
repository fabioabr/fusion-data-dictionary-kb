---
id: DOC-HCM-623
doc_type: system-doc
title: "PER_ALLOC_CHKLST_CONTACTS — Contatos de Checklists Alocados"
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
  - contatos
aliases:
  - PER_ALLOC_CHKLST_CONTACTS
  - per_alloc_chklst_contacts
  - per-alloc-chklst-contacts
  - contatos-de-checklists-alocados
  - per-alloc-chklst-con
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOC_CHKLST_CONTACTS

## 📌 Visão Geral

Armazena os **contatos** associados a checklists alocados. Define as pessoas de contato para suporte durante a execução de um checklist (ex.: buddy de onboarding, gestor, RH).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Suporte ao colaborador** — identifica pessoas de contato para dúvidas durante o checklist.
- **Programa de buddy** — associa mentores a novos colaboradores no onboarding.
- **Comunicação** — facilita o contato entre o colaborador e os responsáveis pelo processo.
- **Escalação** — define a quem recorrer em caso de problemas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOC_CHKLST_CONTACT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do contato | — | 🟢 90% |
| 2 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist associado | PER_ALLOCATED_CHECKLISTS | 🟢 90% |
| 3 | CONTACT_PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa de contato | PER_ALL_PEOPLE_F | 🟢 85% |
| 4 | CONTACT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de contato (BUDDY, MANAGER, HR_REP) | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_checklists]] — via `ALLOCATED_CHECKLIST_ID` (checklist de onboarding do contato)
- [[per_all_people_f]] — via `CONTACT_PERSON_ID` (pessoa de contato)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Contatos de um checklist
```sql
SELECT pcc.CONTACT_TYPE, ppf.FULL_NAME
FROM   PER_ALLOC_CHKLST_CONTACTS pcc
JOIN   PER_ALL_PEOPLE_F ppf ON pcc.CONTACT_PERSON_ID = ppf.PERSON_ID
WHERE  pcc.ALLOCATED_CHECKLIST_ID = :p_checklist_id
  AND  SYSDATE BETWEEN ppf.EFFECTIVE_START_DATE AND ppf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `CONTACT_TYPE = 'BUDDY'` — Mentores/Buddies
---

## 🔒 Observações

- Cada checklist pode ter múltiplos contatos de diferentes tipos.
- O programa de buddy é uma prática comum de onboarding — o buddy é registrado aqui.
- Os contatos são específicos por instância de checklist, não pelo template.
---

## 📚 Referências

- [Oracle Docs — PER_ALLOC_CHKLST_CONTACTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocchklstcontacts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
