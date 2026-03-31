---
id: DOC-HCM-639
doc_type: system-doc
title: "PER_CHECKLISTS_B — Templates de Checklist (Base)"
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
  - templates
aliases:
  - PER_CHECKLISTS_B
  - per_checklists_b
  - per-checklists-b
  - templates-de-checklist-(base)
  - per-checklists-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHECKLISTS_B

## 📌 Visão Geral

Armazena os **templates (modelos) de checklist** disponíveis no sistema. Define a estrutura base de checklists para processos como onboarding, offboarding e transferências.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Padronização** — define templates reutilizáveis de checklist.
- **Onboarding/Offboarding** — modelos específicos para cada processo de RH.
- **Configuração** — define a estrutura, tarefas e regras de cada checklist.
- **Compliance** — garante que processos obrigatórios sejam seguidos consistentemente.
- **Automação** — base para alocação automática de checklists em eventos de RH.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template de checklist | — | 🟢 95% |
| 2 | CHECKLIST_CATEGORY | VARCHAR2(30) | NOT NULL | Classificação | Categoria (ONBOARDING, OFFBOARDING, TRANSFER) | — | 🟢 90% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se o template está ativo (Y/N) | — | 🟢 85% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de templates de checklist.

### Tabelas-filha (FK de saída)
- [[per_checklists_tl]] — via `CHECKLIST_ID` (traduções do template de checklist)
- [[per_checklist_contacts]] — via `CHECKLIST_ID` (contatos do template)
- [[per_checklist_contents]] — via `CHECKLIST_ID` (conteúdos do template)
- [[per_allocated_checklists]] — via `CHECKLIST_ID` (instâncias alocadas)

---

## 📎 Uso Típico

### Templates de checklist ativos
```sql
SELECT pcb.CHECKLIST_ID, pcb.CHECKLIST_CATEGORY, pcb.LEGISLATION_CODE
FROM   PER_CHECKLISTS_B pcb
WHERE  pcb.ACTIVE_FLAG = 'Y'
ORDER BY pcb.CHECKLIST_CATEGORY;
```

### Filtros comuns
- `CHECKLIST_CATEGORY = 'ONBOARDING'` — Checklists de onboarding
- `ACTIVE_FLAG = 'Y'` — Templates ativos
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Cada template define a estrutura do checklist — as instâncias ficam em PER_ALLOCATED_CHECKLISTS.
- Templates podem ser específicos por legislação (país).
- A categoria determina quando o checklist é acionado automaticamente.
---

## 📚 Referências

- [Oracle Docs — PER_CHECKLISTS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchecklistsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
