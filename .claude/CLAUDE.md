# data-centered Project Guide

## Session Startup

1. Run `bd list` to see open beads
2. If ingesting resources: read `AGENTS.md` first for schema requirements

## Resource Ingestion Workflow

When adding resources to the knowledge base:

### Step 1: Check for Duplicates
```bash
python ingest.py batch intake-queue.md --dry-run
```

### Step 2: For Each URL

**Extraction** (free, local):
```bash
summarize "<url>" --extract-only --json
```

**Classification** - Use exact taxonomy from `ingestion/classifiers.py`:

| Domain | Categories |
|--------|------------|
| `knowledge-engineering` | Core Architecture, Semantic Layer, Knowledge Graphs, Semantic Foundations, Agentic Analytics, Process Knowledge, Context Engineering, Knowledge Quality |
| `ai-llms` | LLM Foundations, Agent Memory, AI Evaluation, Prompt Engineering |
| `ai-tools` | Agent Infrastructure, Development Tools |
| `analytics-engineering` | dbt Practices, Data Modeling, Transformation Tools |
| `data-visualization` | Chart Design, Dashboard Exemplars, UI/UX Principles |
| `data-storytelling` | Process Guides, Scrollytelling, Data Journalism |
| `career-development` | Portfolio Building, Career Strategy |

**Required fields** (see `AGENTS.md` for full schema):
- `id`, `url`, `preferredLabel`, `definition`
- `author` (create new author entry if needed)
- `domain`, `category`, `granularity`
- `contentType`: essay | blog | video | podcast | documentation | paper
- `granularity`: foundational | conceptual | implementation | advanced
- `dateAdded`: today's date

### Step 3: Author Research
For new authors, research demographics per `AGENTS.md`:
- Location, job title, affiliation
- `perspectiveType`: practitioner | academic | vendor | journalist | researcher
- Use `~` for unknown fields, don't guess

### Step 4: Append to YAML Files
- Resources → `resources.yaml`
- Authors → `authors.yaml`

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Full schema, relationship types, ontology mappings |
| `ingestion/classifiers.py` | Exact taxonomy with domain colors |
| `docs/ingestion-pipeline-update.md` | Pipeline status and capabilities |
| `intake-queue.md` | URLs pending ingestion |

## API Note

The automated pipeline (`python ingest.py add`) requires `ANTHROPIC_API_KEY`.

For Claude Max users (no API): use `summarize.sh` for extraction + Claude Code for classification directly, following the taxonomy above.

## Beads

View open work:
```bash
bd list --status open
```

Current phases:
- Phase 1 (dei): Complete - extraction, duplicates, batch, scoring
- Phase 2 (0hv): Open - context compression, parallel search, author enrichment
- Phase 3 (i13): Open - KB testing, experiential learning, Skill packaging
