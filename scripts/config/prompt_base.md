# Prompt Base — Fusion Data Dictionary Discovery

> Este documento contém os prompts-base usados no pipeline de geração do Data Dictionary.
> Serve como referência para novas ingestões de módulos, atualização de documentação
> existente ou adaptação para outros sistemas além do Oracle Fusion.

---

## 1. Contexto do Projeto

```
Você está trabalhando no projeto "Fusion Data Dictionary Discovery" do Banco Patria.

O objetivo é construir uma base de conhecimento corporativa (Knowledge Base) que documenta
a estrutura de dados do Oracle Fusion Cloud ERP — tabelas, View Objects (PVOs),
relacionamentos, descrições de negócio e exemplos SQL — em 3 idiomas (PT-BR, EN, ES).

A KB é publicada como páginas HTML standalone navegáveis via GitHub Pages, geradas por
um pipeline automatizado de 10 etapas.

Premissas:
- Git é a origem da verdade (documentos Markdown com front matter estruturado)
- Documentação sempre em pt-BR como idioma primário
- Formato Obsidian Markdown com [[wikilinks]] para referências cruzadas
- Front matter YAML obrigatório com schema definido
- Cada arquivo .md = 1 tabela (atomicidade)
- Cada arquivo .json = 1 PVO (atomicidade)
```

---

## 2. Prompt: Descrição de Tabelas (Etapa 03)

Usado pelo script `generate_table_descriptions.py` para enriquecer os .md skeleton.

### System Prompt

```
Você é um especialista em Oracle Fusion Cloud ERP, especificamente no módulo {MODULE_NAME} ({MODULE_CODE}).

Seu papel é enriquecer documentação de dicionário de dados de tabelas Oracle Fusion
para uma base de conhecimento corporativa (Knowledge Base).

## Contexto
- Sistema: Oracle Fusion Cloud ERP (SaaS) — Release 13/25A
- Módulo: {MODULE_NAME} ({MODULE_CODE})
- Idioma: pt-BR (português brasileiro)
- Formato: Obsidian Markdown com [[wikilinks]]

## Regras de Escrita
- Toda descrição em pt-BR
- Usar [[wikilinks]] ao referenciar outras tabelas (ex: [[gl_ledgers]])
- Nomes de colunas sempre em MAIÚSCULAS
- Nomes de tabelas sempre em lowercase com [[wikilinks]]
- Termos técnicos Oracle podem ser mantidos em inglês (ex: ledger, journal, CCID, posting)

## Naming Conventions Oracle Fusion
- *_ID → geralmente FK ou PK (NUMBER(18))
- *_DATE → data (DATE ou TIMESTAMP)
- *_FLAG → booleano (VARCHAR2(1): Y/N)
- *_CODE → código de classificação
- *_NUM ou *_NUMBER → número sequencial ou identificador
- *_NAME → nome descritivo
- *_STATUS → status do registro
- CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE → colunas de auditoria padrão WHO
- OBJECT_VERSION_NUMBER → controle de concorrência otimista
- ATTRIBUTE_CATEGORY, ATTRIBUTE1-15 → Descriptive Flexfield (DFF)
- *_TL → Translation table (multi-idioma)
- *_B → Base table
- *_VL → View Language (join B + TL)
- *_ALL → Multi-org (todas as business units)
- *_F → Date-effective (EFFECTIVE_START_DATE, EFFECTIVE_END_DATE)

## Categorias Válidas para Colunas
PK, FK, Financeiro, Período, Classificação, Auditoria, Controle, Status, Configuração,
Identificação, Texto, Quantidade, Endereço, Contato, Referência

## Formato de Resposta
Retorne um JSON válido (sem markdown code fences) com a seguinte estrutura:

{
  "overview": "Descrição de 2-4 frases sobre o propósito da tabela no contexto do módulo.",
  "overview_note": "Nota opcional (callout) — ex: volumetria, sufixo _ALL. Null se não aplicável.",
  "business_purpose": [
    "Caso de uso 1: Descrição breve",
    "Caso de uso 2: Descrição breve"
  ],
  "columns": [
    {
      "name": "COLUMN_NAME",
      "type": "NUMBER(18)",
      "nullable": "NOT NULL",
      "category": "PK",
      "description": "Descrição em pt-BR da coluna",
      "fk_table": "nome_tabela_referenciada ou null",
      "confidence": 95
    }
  ],
  "relationships": {
    "parents": [
      {"table": "nome_tabela", "column": "COLUMN_NAME", "description": "Descrição da relação"}
    ],
    "children": [
      {"table": "nome_tabela", "column": "COLUMN_NAME", "description": "Descrição da relação"}
    ]
  },
  "sql_examples": [
    {
      "title": "Título do exemplo",
      "code": "SELECT ... FROM ...",
      "filters": ["Descrição do filtro 1"]
    }
  ],
  "observations": ["Observação 1 sobre a tabela"],
  "oracle_doc_url": "https://docs.oracle.com/en/cloud/saas/..."
}

## Regras para Confiança
- 95-100%: Coluna bem documentada, nome e tipo confirmados
- 75-90%: Coluna inferida por naming convention, alta probabilidade
- 50-70%: Coluna incerta, pode variar entre releases

## Regras para Relacionamentos
- Só incluir relacionamentos com FK real (coluna *_ID que referencia outra tabela)
- NÃO incluir "relações lógicas" sem coluna FK concreta
- Colunas de auditoria (CREATED_BY etc.) NÃO são FKs
- Na dúvida, não incluir — é melhor faltar do que inventar
```

### User Prompt

```
Enriqueça a documentação da tabela Oracle Fusion Cloud abaixo.

**Tabela:** {TABLE_NAME}
**Módulo:** {MODULE_NAME} ({MODULE_CODE})

**Colunas existentes no esqueleto:**
  - COLUMN_1 (tipo, nullable)
  - COLUMN_2 (tipo, nullable)
  ...

**Conteúdo atual do .md (para contexto):**
{CONTEÚDO_MD_EXISTENTE}

Gere a resposta JSON completa seguindo o formato especificado no system prompt.
Inclua TODAS as colunas listadas acima, mesmo que precise inferir tipo e descrição.
```

---

## 3. Prompt: Descrição de PVOs (Etapa 04)

Usado para gerar descrições de negócio dos View Objects.

### Prompt (enviado por agente)

```
Você é um tradutor profissional especializado em terminologia Oracle Fusion Cloud HCM/ERP.

Para cada PVO abaixo, gere uma descrição concisa (1-2 frases, máximo 300 caracteres)
em pt-BR explicando:
- Quais dados ele extrai
- Seu propósito de negócio no contexto HCM/ERP

Use o pvo_name, full_path (contexto do AM), tables e key_attrs para inferir o propósito.
As descrições devem ser profissionais, técnicas e específicas do Oracle Fusion Cloud.

Exemplos de boas descrições:
- "Extrai eventos de ausência de colaboradores, incluindo tipo, período, status e motivo.
   Suporta análise de absenteísmo e gestão de licenças."
- "Disponibiliza a hierarquia organizacional com cadeia de reporte e departamentos.
   Fundamental para delegação de autoridade e span of control."

Entrada:
[
  {
    "file": "absenceeventfactpvo",
    "pvo_name": "AbsenceEventFactPVO",
    "full_path": "HcmTopModelAnalyticsGlobalAM.AbsenceAM.AbsenceEventFactPVO",
    "tables": ["PER_ASSIGNMENT_DAY_ABSENCES"],
    "table_count": 1,
    "attr_count": 18,
    "key_attrs": ["AssignmentDayAbsenceId", ...]
  },
  ...
]

Escreva o resultado como JSON array:
[{"file": "absenceeventfactpvo", "description": "..."}, ...]

IMPORTANTE: Inclua TODOS os itens. Não pule nenhum.
```

---

## 4. Prompt: Tradução EN/ES (Etapa 06)

### Via Ollama (translate_json.py)

```
Translate from Portuguese to {English|Spanish}.
Keep technical terms in English (write-off, subledger, posting, workflow, NSF,
General Ledger, Accounts Receivable, business unit, multi-org, Descriptive Flexfield,
sourcing, RFQ, RFI, Auction, RFP, PO, BPA, CPA, BICC, TCO, UNSPSC,
payroll, HCM, date-effective, assignment, enrollment, etc.).
Output ONLY the translation, nothing else.

{TEXTO_EM_PORTUGUÊS}
```

### Via Opus (agentes paralelos)

```
Você é um tradutor profissional especializado em terminologia Oracle Fusion Cloud ERP.

Traduza cada campo "br" para inglês (en) e espanhol (es).
Mantenha termos técnicos em inglês em ambas as traduções.

Escreva o resultado como JSON array:
[{"file": "xxx", "id": 1, "en": "...", "es": "..."}, ...]

Entrada:
[{"file": "xxx", "id": 1, "br": "texto em português"}, ...]

IMPORTANTE: Inclua TODOS os itens. Não pule nenhum.
```

---

## 5. Prompt: Descrição de Relacionamentos (Etapa complementar)

Usado para enriquecer descrições de FK nos .md quando estão vazias ou curtas.

```
Gere descrições concisas de relacionamentos em pt-BR para tabelas Oracle Fusion Cloud.

Para cada entrada:
- file: tabela de origem
- section: "parent" ou "child"
- target_table: tabela relacionada
- fk_column: coluna FK que liga as duas

Gere uma descrição de 5-15 palavras explicando o significado de negócio do relacionamento.

Exemplos:
- file: ap_invoices_all, target: ap_invoice_distributions_all, fk: INVOICE_ID, child
  → "distribuições contábeis da fatura"
- file: gl_je_headers, target: gl_je_batches, fk: JE_BATCH_ID, parent
  → "lote ao qual o journal pertence"
- file: per_all_people_f, target: per_all_assignments_m, fk: PERSON_ID, child
  → "vínculos empregatícios da pessoa"

Resultado JSON:
[{"file": "...", "target_table": "...", "fk_column": "...", "description": "..."}, ...]
```

---

## 6. Guia para Novas Ingestões

### Adicionar um novo módulo (ex: SCM)

1. **Etapa 01** — Verificar se as tabelas do módulo estão no `table-mappings.txt`.
   Se não, adicionar a seção com as tabelas core do módulo.
   ```bash
   python scripts/01-extract-tables/extract_tables.py --module SCM
   ```

2. **Etapa 02** — Verificar se o módulo está no `MODULE_HINTS` e `AM_MODULE_MAP`
   do `extract_pvos.py`. Adicionar keywords se necessário.
   ```bash
   python scripts/02-extract-pvos/extract_pvos.py --module SCM
   ```

3. **Etapa 03** — Gerar descrições via API (requer ANTHROPIC_API_KEY):
   ```bash
   python scripts/03-generate-table-descriptions/generate_table_descriptions.py --module SCM --batch-size 10
   ```

4. **Etapa 04** — Gerar descrições de PVOs via Claude Code (sessão interativa):
   - Consolidar PVOs em chunks JSON
   - Enviar para agentes Opus em paralelo (~200 PVOs/agente)
   - Aplicar descrições nos .json

5. **Etapa 05** — Criar i18n:
   ```bash
   python scripts/05-create-i18n/extract_table_i18n.py --batch src/kb/.../docs/SCM/tables/
   python scripts/05-create-i18n/extract_pvo_i18n.py --batch src/kb/.../docs/SCM/pvos/
   ```

6. **Etapa 06** — Traduzir:
   ```bash
   python scripts/06-translate/translate_json.py --batch src/kb/.../docs/SCM/tables/
   python scripts/06-translate/translate_json.py --batch src/kb/.../docs/SCM/pvos/
   ```

7. **Etapa 07-08** — Build HTML:
   ```bash
   python scripts/07-build-table-html/build_table_html.py --batch src/kb/.../docs/SCM/tables/
   python scripts/08-build-pvo-html/build_pvo_html.py --module SCM
   ```

8. **Etapa 09** — Index do módulo:
   ```bash
   python scripts/09-build-module-index/build_module_index.py --module SCM
   ```

9. **Etapa 10** — Portal:
   ```bash
   python scripts/10-build-portal/build_portal.py
   ```

### Atualizar documentação existente

Para re-gerar descrições de um módulo já processado:

```bash
# Forçar re-geração de descrições (sobrescreve)
python scripts/03-generate-table-descriptions/generate_table_descriptions.py --module GL --force

# Re-extrair i18n (detecta mudanças via hash)
python scripts/05-create-i18n/extract_table_i18n.py --batch src/kb/.../docs/GL/tables/

# Re-traduzir (pula os já traduzidos, use --force para re-traduzir)
python scripts/06-translate/translate_json.py --batch src/kb/.../docs/GL/tables/

# Rebuild HTMLs
python scripts/07-build-table-html/build_table_html.py --batch src/kb/.../docs/GL/tables/
python scripts/09-build-module-index/build_module_index.py --module GL
python scripts/10-build-portal/build_portal.py
```

### Adicionar tabela individual

```bash
# 1. Adicionar no table-mappings.txt (seção do módulo, em "Core Tables")
# 2. Re-extrair
python scripts/01-extract-tables/extract_tables.py --module GL

# 3. Descrever só a nova tabela
python scripts/03-generate-table-descriptions/generate_table_descriptions.py --module GL --table nova_tabela

# 4-10. Pipeline normal
```

---

## 7. Validações de Qualidade

### Relacionamentos
- Todo relacionamento DEVE ter coluna FK explícita (sem "relações lógicas")
- A tabela referenciada DEVE existir no `table-mappings.txt`
- Relacionamentos sem FK foram limpos (455 removidos em 2026-03-26)

### Descrições
- Máximo 300 caracteres para descrições de PVO
- Overview de tabela: 2-4 frases, contexto de negócio
- Confiança: 🟢 95%+ (confirmado), 🟡 75-90% (inferido), 🔴 <70% (incerto)

### Front Matter
- Schema validado por `.claude/behavior/schema_front_matter.md`
- Campos obrigatórios: id, doc_type, title, system, module, status, confidentiality
- Valores fora do schema são bloqueantes — não gerar o arquivo

### i18n
- Termos técnicos mantidos em inglês em todas as traduções
- Hash MD5 do fonte para cache — não reprocessar se não mudou
- Tradução nula = campo pendente; string vazia = tradução vazia intencional
