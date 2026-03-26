---
id: DOC-HCM-755
doc_type: system-doc
title: "ZMM_SR_SCHEDULES_TL — Escalas de Trabalho (Traduções)"
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
  - work-schedules
  - translations
aliases:
  - ZMM_SR_SCHEDULES_TL
  - zmm_sr_schedules_tl
  - escalas-trabalho-traducao
  - work-schedules-translation
  - zmm-sr-schedules-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ZMM_SR_SCHEDULES_TL

## 📌 Visão Geral

Tabela de traduções customizada (prefixo `ZMM`) que armazena os **textos traduzidos das escalas de trabalho** em múltiplos idiomas. O sufixo `_TL` indica tabela de tradução, seguindo o padrão MLS (Multi-Language Support) do Oracle Fusion.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Permite que nomes e descrições das escalas de trabalho sejam exibidos no idioma do usuário logado.
- **Interface multilíngue:** Suporta operações em múltiplos países com idiomas distintos.
- **Relatórios localizados:** Garante que relatórios de escalas e jornada sejam gerados no idioma adequado.
- **Portal do colaborador:** Exibe informações de escala no idioma preferido do funcionário.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_ID | NUMBER(18) | NOT NULL | PK/FK | Referência à escala de trabalho base | [[zmm_sr_schedules_b]].SCHEDULE_ID | 🟡 80% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | SCHEDULE_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da escala de trabalho | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida da escala | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[zmm_sr_schedules_b]] — via `SCHEDULE_ID` (tabela base da escala)

### Tabelas-filha
- Nenhuma — tabela terminal de tradução.

---

## 📎 Uso Típico

### Obter nome da escala no idioma do usuário
```sql
SELECT b.SCHEDULE_ID, b.SCHEDULE_CODE,
       tl.SCHEDULE_NAME, tl.DESCRIPTION
FROM   ZMM_SR_SCHEDULES_B b
JOIN   ZMM_SR_SCHEDULES_TL tl
       ON tl.SCHEDULE_ID = b.SCHEDULE_ID
       AND tl.LANGUAGE = USERENV('LANG')
WHERE  b.ACTIVE_FLAG = 'Y';
```

### Listar todos os idiomas disponíveis para uma escala
```sql
SELECT tl.LANGUAGE, tl.SCHEDULE_NAME
FROM   ZMM_SR_SCHEDULES_TL tl
WHERE  tl.SCHEDULE_ID = :p_schedule_id
ORDER BY tl.LANGUAGE;
```

---

## 🔒 Observações

- Tabela customizada (prefixo `ZMM`) — não faz parte do modelo padrão Oracle Fusion. Estrutura inferida por naming convention.
- Chave primária composta: `SCHEDULE_ID` + `LANGUAGE`.
- Padrão MLS Oracle: `SOURCE_LANG` indica o idioma em que o texto foi originalmente cadastrado.
- Sempre realizar JOIN com [[zmm_sr_schedules_b]] para obter dados completos da escala.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
