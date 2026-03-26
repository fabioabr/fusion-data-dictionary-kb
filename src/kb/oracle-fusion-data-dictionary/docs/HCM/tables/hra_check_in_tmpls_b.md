---
id: DOC-HCM-134
doc_type: system-doc
title: "HRA_CHECK_IN_TMPLS_B — Templates de Check-In (Base)"
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
  - performance-management
  - template
  - avaliacao
  - hra
aliases:
  - HRA_CHECK_IN_TMPLS_B
  - hra_check_in_tmpls_b
  - hra-check-in-tmpls-b
  - DOC-HCM-134
  - templates-de-check-in-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_CHECK_IN_TMPLS_B

## 📌 Visão Geral

Armazena as **definições base** de templates de check-in. Tabela _B (base language) contendo atributos não-traduzíveis como códigos, status e configurações estruturais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de templates de check-in:** Cadastro central de configurações.
- **Configuração estrutural:** Parâmetros base do registro.
- **Controle de versão:** Versionamento via `OBJECT_VERSION_NUMBER`.
- **Base para tradução:** Complementada por `HRA_CHECK_IN_TMPLS_TL`.
- **Governança:** Configurações auditáveis e rastreáveis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECK_IN_TMPL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | CODE | VARCHAR2(30) | NULL | Identificação | Código do registro | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 4 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 5 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Número de versão do objeto | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_check_in_tmpls_tl]] — via `CHECK_IN_TMPL_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Registros ativos
```sql
SELECT b.CHECK_IN_TMPL_ID, b.CODE, b.STATUS_CODE
FROM   HRA_CHECK_IN_TMPLS_B b
WHERE  b.STATUS_CODE = 'ACTIVE';
```

### Com tradução
```sql
SELECT b.CHECK_IN_TMPL_ID, b.CODE, tl.NAME
FROM   HRA_CHECK_IN_TMPLS_B b
JOIN   HRA_CHECK_IN_TMPLS_TL tl ON b.CHECK_IN_TMPL_ID = tl.CHECK_IN_TMPL_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- Para nomes traduzidos, juntar com `HRA_CHECK_IN_TMPLS_TL` via `CHECK_IN_TMPL_ID`.
- O `OBJECT_VERSION_NUMBER` é usado para controle de concorrência otimista.
- Views _VL unem _B + _TL automaticamente para o idioma da sessão.

---

## 📚 Referências

- [Oracle Docs — HRA_CHECK_IN_TMPLS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hracheckintmplsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
