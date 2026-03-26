---
id: DOC-HCM-088
doc_type: system-doc
title: "CMP_SALARY_BASES_TL — Bases Salariais (Tradução)"
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
  - compensation
  - base-salarial
  - traducao
  - translation
aliases:
  - CMP_SALARY_BASES_TL
  - cmp_salary_bases_tl
  - cmp-salary-bases-tl
  - DOC-HCM-088
  - bases-salariais-(tradução)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY_BASES_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições das bases salariais. Tabela _TL (translation) que complementa `CMP_SALARY_BASES` com conteúdo multilíngue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multilinguismo:** Nomes de bases salariais em múltiplos idiomas.
- **Interface do usuário:** Exibição traduzida conforme idioma da sessão.
- **Relatórios localizados:** Labels traduzidos em relatórios de compensação.
- **Integração:** Base para views _VL que unificam _B + _TL.
- **Governança:** Controle centralizado de traduções.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SALARY_BASIS_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da base salarial | [[cmp_salary_bases]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome da base salarial no idioma | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição no idioma | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_salary_bases]] — via `SALARY_BASIS_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Nome da base salarial em português
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   CMP_SALARY_BASES_TL tl
WHERE  tl.SALARY_BASIS_ID = :p_salary_basis_id
  AND  tl.LANGUAGE = 'PTBR';
```

### Todas as bases com tradução
```sql
SELECT b.SALARY_BASIS_CODE, tl.NAME, tl.LANGUAGE
FROM   CMP_SALARY_BASES b
JOIN   CMP_SALARY_BASES_TL tl ON b.SALARY_BASIS_ID = tl.SALARY_BASIS_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `SALARY_BASIS_ID` + `LANGUAGE`.
- O campo `SOURCE_LANG` indica o idioma original da tradução.
- Padrão Oracle _TL: um registro por idioma instalado.
- Para consultas na UI, utilizar views _VL que resolvem o idioma automaticamente.

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY_BASES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalarybasestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
