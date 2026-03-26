---
id: DOC-HCM-347
doc_type: system-doc
title: "HWM_TE_ALT_NAME_VALS_TL — Valores de Nomes Alternativos de Entrada de Tempo (Traduções)"
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
  - time-entry
  - nomes-alternativos
  - valores
  - traducao
aliases:
  - HWM_TE_ALT_NAME_VALS_TL
  - hwm_te_alt_name_vals_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TE_ALT_NAME_VALS_TL

## 📌 Visão Geral

Tabela de traduções dos valores de nomes alternativos de entradas de tempo em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos por idioma. Chave composta: PK da tabela `_B` + `LANGUAGE`.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de entradas de tempo:** Captura e gestão de registros individuais de horas trabalhadas.
- **Nomes alternativos:** Suporte a múltiplas nomenclaturas para integração com diferentes interfaces.
- **Validação de entradas:** Mensagens de erro e conformidade durante o processamento.
- **Controle de versão:** Rastreamento do ciclo de vida de cada entrada de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TE_ALT_NAMEALS_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | — | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do registro | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida do registro | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.NAME, t.DESCRIPTION, t.LANGUAGE
FROM   HWM_TE_ALT_NAME_VALS_TL t
WHERE  t.LANGUAGE = USERENV('LANG')
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Tradução no idioma da sessão
- `LANGUAGE = 'PTB'` — Tradução em português brasileiro

---

## 🔒 Observações

- Tabela de traduções: não utilizar diretamente em relatórios; preferir a view `_VL` correspondente.
- Chave composta: PK do registro base + LANGUAGE.
- Área funcional: Time Entry dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TE_ALT_NAME_VALS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_te_alt_name_vals_tl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
