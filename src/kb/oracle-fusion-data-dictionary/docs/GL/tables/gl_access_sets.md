---
id: DOC-GL-003
doc_type: system-doc
title: "GL_ACCESS_SETS — Conjuntos de Acesso a Dados Contábeis"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - acesso
  - data-access-set
  - seguranca
aliases:
  - GL_ACCESS_SETS
  - gl_access_sets
  - conjuntos-acesso-gl
  - data-access-sets
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_ACCESS_SETS

## Visao Geral

Armazena os **conjuntos de acesso a dados contábeis** (Data Access Sets) do General Ledger. Cada registro define um agrupamento lógico que controla quais ledgers, segmentos de balancete e combinações de contas um usuário ou responsabilidade pode acessar. É o mecanismo central de segurança de dados financeiros no Oracle Fusion GL.

> [!note] Segurança de dados
> Os Data Access Sets substituem o conceito de Security Rules do EBS. Eles controlam o acesso a ledgers e segmentos de forma granular, permitindo que diferentes equipes vejam apenas os dados financeiros relevantes.

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Segurança de dados financeiros:** Controla quais ledgers e segmentos contábeis cada usuário pode consultar e lançar.
- **Segregação de funções:** Permite que diferentes equipes acessem apenas os dados de suas business units ou centros de custo.
- **Configuração multi-ledger:** Define o escopo de acesso quando a organização possui múltiplos ledgers (primário, secundário, de reporte).
- **Auditoria de acesso:** Rastreamento de quais conjuntos de acesso existem e seus parâmetros.
- **Provisioning:** Base para atribuição de acesso a novos usuários via GL_ACCESS_SET_ASSIGNMENTS.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCESS_SET_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conjunto de acesso | — | 🟢 95% |
| 2 | NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do conjunto de acesso | — | 🟢 95% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do conjunto de acesso | — | 🟢 90% |
| 4 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NOT NULL | FK | Plano de contas associado | [[fnd_id_flex_structures]] | 🟢 90% |
| 5 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do calendário contábil associado | [[gl_calendars]] | 🟢 85% |
| 6 | ACCOUNTED_PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo de período contábil (ex: Month) | — | 🟢 85% |
| 7 | DEFAULT_LEDGER_ID | NUMBER(18) | NULL | FK | Ledger padrão do conjunto de acesso | [[gl_ledgers]] | 🟢 90% |
| 8 | SECURITY_SEGMENT_CODE | VARCHAR2(30) | NULL | Classificação | Código do segmento usado para segurança (ex: Management Segment) | — | 🟡 75% |
| 9 | AUTOMATICALLY_CREATED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se foi criado automaticamente pelo sistema (Y/N) | — | 🟡 70% |
| 10 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o conjunto de acesso está ativo (Y/N) | — | 🟢 85% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `DEFAULT_LEDGER_ID` (ledger padrão associado ao conjunto de acesso)
- [[gl_calendars]] — via `PERIOD_SET_NAME` (calendário contábil)

### Tabelas-filha (FK de saída)
- [[gl_access_set_assignments]] — via `ACCESS_SET_ID` (atribuições a usuários/responsabilidades)
- [[gl_access_set_ledgers]] — via `ACCESS_SET_ID` (ledgers incluídos no conjunto)

---

## Uso Tipico

### Listar conjuntos de acesso ativos
```sql
SELECT das.ACCESS_SET_ID, das.NAME, das.DESCRIPTION,
       das.DEFAULT_LEDGER_ID, das.SECURITY_SEGMENT_CODE
FROM   GL_ACCESS_SETS das
WHERE  das.ENABLED_FLAG = 'Y'
ORDER BY das.NAME;
```

### Conjunto de acesso com ledger padrão
```sql
SELECT das.NAME AS access_set,
       gl.NAME AS ledger_padrao
FROM   GL_ACCESS_SETS das
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = das.DEFAULT_LEDGER_ID
WHERE  das.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Conjuntos de acesso ativos
- `AUTOMATICALLY_CREATED_FLAG = 'Y'` — Criados automaticamente pelo sistema
- `DEFAULT_LEDGER_ID = :p_ledger_id` — Filtrar por ledger padrão

---

## Observacoes

- Cada Data Access Set está vinculado a um **plano de contas** (Chart of Accounts) e um **calendário contábil** — não é possível misturar estruturas diferentes em um mesmo conjunto.
- O `DEFAULT_LEDGER_ID` define o ledger que será usado como padrão quando o usuário acessar funcionalidades do GL com esse conjunto.
- O `SECURITY_SEGMENT_CODE` determina qual segmento do plano de contas é usado para restringir acesso (ex: segmento de empresa, centro de custo).
- Conjuntos criados automaticamente (`AUTOMATICALLY_CREATED_FLAG = 'Y'`) são gerados pelo sistema ao criar um novo ledger — geralmente concedem acesso total ao ledger.
- A tabela [[gl_access_set_ledgers]] detalha quais ledgers (além do padrão) fazem parte do conjunto.

---

## Referencias

- [Oracle Docs — GL_ACCESS_SETS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glaccesssets-25066.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
