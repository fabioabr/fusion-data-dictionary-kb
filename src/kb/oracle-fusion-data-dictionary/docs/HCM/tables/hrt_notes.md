---
id: DOC-HCM-239
doc_type: system-doc
title: "HRT_NOTES — Notas de Perfil de Talento"
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
  - notas
  - talent
  - perfil
aliases:
  - HRT_NOTES
  - hrt_notes
  - hrt-notes
  - talent-notes
  - notas-talento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_NOTES

## 📌 Visao Geral

Armazena **notas e anotacoes** associadas a perfis de talento, processos de talent review e atividades de gestao de talentos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Registrar observacoes durante reunioes de calibracao.
- **Gestao de talentos:** Documentar feedback e comentarios sobre colaboradores.
- **Auditoria:** Manter historico de anotacoes para compliance.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | NOTE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da nota | — | 🟢 95% |
| 2 | PROFILE_ID | NUMBER(18) | NULL | FK | Perfil de talento associado | [[hrt_profiles_b]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador associado | [[per_all_people_f]] | 🟢 90% |
| 4 | NOTE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da nota | — | 🟡 80% |
| 5 | NOTE_TEXT | CLOB | NULL | Dados | Texto da nota | — | 🟢 90% |
| 6 | NOTE_VISIBILITY | VARCHAR2(30) | NULL | Classificacao | Visibilidade (PRIVATE, PUBLIC, MANAGER) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento associado a anotacao)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa associada a anotacao de talento)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Notas de um perfil
```sql
SELECT n.NOTE_ID, n.NOTE_TYPE, n.NOTE_TEXT,
       n.CREATION_DATE
FROM   HRT_NOTES n
WHERE  n.PROFILE_ID = :p_profile_id
ORDER BY n.CREATION_DATE DESC;
```

---

## 🔒 Observacoes

- O campo NOTE_VISIBILITY controla quem pode ver a nota.
- Notas podem conter informacoes sensiveis — aplicar filtro de confidencialidade.

---

## 📚 Referencias

- [Oracle Docs — HRT_NOTES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtnotes.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
