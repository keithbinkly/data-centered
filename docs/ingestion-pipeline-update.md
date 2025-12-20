# Ingestion Pipeline: From Manual to Automated

*December 2024 — Phase 1 Complete*

---

## The Problem We Had

Adding a resource to data-centered.com meant:

1. Find interesting article
2. Read it, decide if it fits the taxonomy
3. Open `resources.yaml`, scroll to the right section
4. Manually write 30+ lines of YAML (title, definition, domain, category, author, relationships...)
5. Look up or create author entry in `authors.yaml`
6. Think about how it relates to existing resources
7. Hope you didn't make a typo

**Time per resource:** 10-15 minutes of focused work.

**Result:** A backlog of 50+ bookmarked articles that never got added.

---

## What We Built

An automated ingestion pipeline using **summarize.sh** for content extraction and **DSPy** for LLM-powered classification.

```
URL → Extract → Classify → Score → Enrich → Generate YAML
```

**New workflow:**
```bash
python ingest.py add "https://example.com/article" --dry-run
python ingest.py batch intake-queue.md --dry-run
```

The pipeline:
- Fetches and parses URLs (including YouTube transcripts)
- Checks for duplicates before processing
- Classifies into our 7 domains and categories
- Generates and scores definitions for quality
- Extracts author information
- Logs all reasoning for debugging
- Creates ready-to-append YAML

**Time per resource:** 2-3 minutes (mostly review).

---

## Current State (Phase 1 Complete)

### What Works

```
✓ Single URL ingestion
✓ Batch ingestion from markdown files
✓ YouTube transcript extraction
✓ Duplicate URL detection
✓ Automatic domain/category classification
✓ Definition generation with quality scoring
✓ Author extraction
✓ YAML generation matching our schema
✓ Human review queue for low-confidence items
✓ Pipeline logging for debugging
✓ CLI with dry-run mode
```

### Remaining Limitations

```
✗ Truncates long articles at 4000 chars
✗ No relationship discovery
✗ Author bios require manual research
✗ No semantic similarity detection (only exact URL match)
```

---

## Phase 1: Foundation (Complete)

All tasks implemented and closed:

| Bead | Task | Status |
|------|------|--------|
| `dei.1` | Replace extraction with summarize.sh | ✅ Complete |
| `dei.2` | Add duplicate detection | ✅ Complete |
| `dei.3` | Add batch mode | ✅ Complete |
| `dei.4` | Add definition quality scoring | ✅ Complete |
| `dei.5` | Log classification reasoning | ✅ Complete |

**Epic:** `data-centered-dei` (closed)

**Commits:**
- `c24d700` feat: replace Unstructured with summarize.sh wrapper
- `c78287d` feat: add duplicate URL detection to ingestion pipeline
- `bc34e1e` feat: add batch ingestion from markdown files
- `bbde328` feat: add definition quality scoring to ingestion pipeline
- `a09bacb` feat: add ingestion pipeline logging for debugging

---

## Phase 2: Intelligence (Open)

| Bead | Task | Impact |
|------|------|--------|
| `0hv.1` | Context compression for long articles | Better classification accuracy |
| `0hv.2` | Parallel relationship search | 4x faster as KB grows |
| `0hv.3` | Author enrichment via GitHub API | Automatic bio/affiliation |
| `0hv.4` | Lazy DSPy module loading | 40-60% token reduction |

**Epic:** `data-centered-0hv` (open, depends on Phase 1)

---

## Phase 3: Advanced (Open)

| Bead | Task | Impact |
|------|------|--------|
| `i13.1` | Semiosis-style KB quality testing | Systematic quality measurement |
| `i13.2` | Experiential learning | Pipeline improves over time |
| `i13.3` | Package as Claude Skill | Seamless invocation |
| `i13.4` | CocoIndex integration | Knowledge graph visualization |

**Epic:** `data-centered-i13` (open, depends on Phase 2)

---

## CLI Reference

```bash
# Single URL
python ingest.py add "https://example.com/article"
python ingest.py add "https://example.com/article" --dry-run

# Batch from markdown
python ingest.py batch intake-queue.md --dry-run
python ingest.py batch intake-queue.md --auto-approve

# Review pending
python ingest.py review
```

**Current intake queue status:**
- 90 total links in `intake-queue.md`
- 33 already in KB (duplicates)
- 57 ready to process

---

## End State Vision

After completing all phases:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  $ ingest "https://example.com/article"                             │
│                                                                     │
│  📥 Fetching...                                                     │
│  ✓ Extracted: "Context Engineering for AI Agents" (2,847 words)    │
│                                                                     │
│  🔍 Checking for duplicates...                                      │
│  ✓ No duplicates found                                              │
│  ℹ Similar: context-engineering-weaviate (0.72 similarity)          │
│                                                                     │
│  🧠 Classifying...                                                  │
│  ✓ Domain: knowledge-engineering → Context Engineering              │
│  ✓ Confidence: 94% (auto-approved)                                  │
│                                                                     │
│  📝 Generating definition...                                        │
│  ✓ Quality score: 0.91                                              │
│                                                                     │
│  👤 Author: Cory Doctorow                                           │
│  ✓ Found on GitHub: cory@eff.org, EFF                               │
│                                                                     │
│  🔗 Suggested relationships:                                        │
│  • related → context-engineering-weaviate                           │
│  • broader → ai-context-gap                                         │
│                                                                     │
│  ✅ Added to knowledge base                                          │
│  ✅ Author enriched                                                  │
│  ✅ Relationships created                                            │
│                                                                     │
│  📊 Session stats: 3 resources added, 0 duplicates, $0.02 spent    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Capabilities Summary

| Capability | Before | After Phase 1 | After Phase 3 |
|------------|--------|---------------|---------------|
| Time per resource | 10-15 min | 2-3 min | 30 sec |
| Batch processing | No | **Yes** | Yes |
| Duplicate detection | No | **Yes** | Yes |
| YouTube support | No | **Yes** | Yes |
| Definition scoring | No | **Yes** | Yes |
| Pipeline logging | No | **Yes** | Yes |
| Author enrichment | Manual | Manual | Automatic |
| Relationship discovery | Manual | Manual | Automatic |
| Quality measurement | None | **Basic** | Systematic |
| Learning over time | No | No | Yes |
| Knowledge graph | No | No | Yes |

---

## Key Insights from Research

These findings shaped our roadmap:

> **"87.5% of agent failures are context problems, not model capability."**
> — Weaviate Context Engineering

We're adding context compression and selection for long articles.

> **"Small models benefit most from shared memory (+0.66 pts)."**
> — Spark: Shared Memory for Coding Agents

We're adding experiential learning from successful classifications.

> **"Tool Search reduces tokens by 85%."**
> — Anthropic Advanced Tool Use

We're adding lazy DSPy module loading.

> **"Quality is the production killer."**
> — LangChain State of Agent Engineering 2025

We added definition quality scoring and will add KB testing.

---

## Resources Informing This Work

- [summarize.sh](https://summarize.sh/) - Robust content extraction CLI
- [Semiosis](https://github.com/AnswerLayer/semiosis) - KB quality testing framework
- [CocoIndex](https://cocoindex.io/) - Incremental indexing to graphs
- [LangChain Context Engineering](https://blog.langchain.com/context-engineering-for-agents/) - 4 context strategies
- [Relace Fast Agentic Search](https://www.relace.ai/blog/fast-agentic-search) - Parallel search patterns
- [Anthropic Advanced Tool Use](https://www.anthropic.com/engineering/advanced-tool-use) - Tool Search Tool
- [Agent Skills](https://agentskills.io/) - Skills packaging format

---

## Next Steps

View remaining tasks:

```bash
bd list --status open
```

Phase 2 priority: Context compression (`0hv.1`) for better classification of long articles.

---

*Built with Claude Code + DSPy + summarize.sh*
