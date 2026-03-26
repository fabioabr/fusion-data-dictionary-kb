---
id: DOC-HCM-710
doc_type: system-doc
title: "PER_ROLES_DN_VL — View de Papéis Desnormalizados com Tradução"
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
  - papeis
  - roles
  - view
  - denormalized
  - seguranca
aliases:
  - PER_ROLES_DN_VL
  - per_roles_dn_vl
  - view-papeis-denormalizados
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_ROLES_DN_VL

## Visão Geral

**View** desnormalizada com tradução que apresenta os **papéis** (roles) atribuídos a pessoas no sistema HCM. Combina dados de atribuição de papéis com informações descritivas traduzidas, facilitando consultas de segurança e relatórios.

> [!note] Sufixos _DN_VL
> `_DN` indica dados **Denormalized**; `_VL` indica **View com Language** — dados desnormalizados com tradução automática no idioma da sessão.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Gestão de segurança** — consultar papéis atribuídos a cada colaborador
- **Auditoria de acessos** — verificar quem possui quais papéis
- **Relatórios de compliance** — listar papéis para auditorias internas
- **Provisionamento de acessos** — base para concessão/revogação de papéis
- **Segregação de funções** — identificar conflitos de papéis

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa com o papel atribuído | PER_PERSONS | 🟡 80% |
| 2 | ROLE_ID | NUMBER(18) | NOT NULL | FK | Identificador do papel | — | 🟡 80% |
| 3 | ROLE_NAME | VARCHAR2(240) | NULL | Tradução | Nome traduzido do papel | — | 🟡 75% |
| 4 | ROLE_CODE | VARCHAR2(30) | NULL | Identificação | Código do papel | — | 🟡 75% |
| 5 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do papel (JOB, ABSTRACT, DATA) | — | 🟡 70% |
| 6 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo associado | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da atribuição | — | 🟡 75% |
| 8 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da atribuição | — | 🟡 75% |
| 9 | PERSON_NAME | VARCHAR2(360) | NULL | Descritivo | Nome da pessoa | — | 🟡 70% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa com papel/funÃ§Ã£o atribuÃ­do)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vÃ­nculo do papel/funÃ§Ã£o atribuÃ­do)

### Tabelas-filha (FK de saída)
- Nenhuma — views não possuem FKs diretas.

---

## Uso Típico

### Papéis atribuídos a uma pessoa
```sql
SELECT vl.ROLE_NAME, vl.ROLE_CODE, vl.ROLE_TYPE
FROM   PER_ROLES_DN_VL vl
WHERE  vl.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## Observações

- Por ser uma view desnormalizada, contém dados descritivos para evitar joins.
- `ROLE_TYPE` distingue papéis de cargo (JOB), abstratos (ABSTRACT) e de dados (DATA).
- Tradução automática no idioma da sessão (`USERENV('LANG')`).
- Útil para auditorias de segurança e compliance.

---

## Referências

- [Oracle Docs — PER_ROLES_DN_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perrolesdnvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
