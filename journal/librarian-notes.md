# Librarian's Working Notes

Internal document. Not published. Updated after each batch.

---

## Questions Raised

| Question | Raised In | Status |
|----------|-----------|--------|
| Is the semantic layer necessary, or just nice? | [Update #1](update-001.html) | Resolved in [Update #4](update-004.html) |
| Where do ontology projects actually fail? | [Update #1](update-001.html) | Partially resolved - Vashishta's failure modes (academic over-engineering, scope creep, perfectionism) |
| Can semantic infrastructure be built incrementally? | [Update #1](update-001.html) | Open |
| Is there domain knowledge that can only be acquired through practice? | [Update #2](update-002.html) | Open - Tableau exemplars suggest yes |
| Will agent memory approaches converge or fragment? | [Update #2](update-002.html) | Open - Three approaches in Update #5, still no convergence |
| Is "context graphs" a real advance or terminology arbitrage? | [Update #4](update-004.html) | Open - Watching for implementations |
| Who builds the Figma for semantics? | [Update #4](update-004.html) | Open |
| Is Bret Victor's longevity evidence of quality or field stagnation? | [Update #5](update-005.html) | Open |

---

## Positions That Evolved

### The Semantic Layer Debate
- **Update #1**: Resources argued semantic infrastructure is essential. I hadn't seen the skeptical case.
- **Update #4**: Found the skeptical case (MotherDuck). Realized both sides describe different contexts.
- **Current position**: Semantic infrastructure when discovery and composition matter; simpler structures when queries are known in advance. The frustrating part is that it's hard to know which you're in until you've already invested.

### On Independent Convergence
- **Update #1**: Claimed "multiple authors working independently" without verification.
- **Editor feedback**: Challenged whether they actually worked independently or cited each other.
- **Update #1 revision**: Now names specific authors (Olesen-Bagneux, Talisman, Vashishta, Atlan) from different contexts (metadata consultant, knowledge engineer, AI strategist, vendor) to demonstrate the convergence is real.

### On Context Engineering
- **Update #2**: Noted LangChain and Weaviate publishing within days of each other.
- **Current position**: Context engineering as distinct from prompt engineering may be 2025's most important conceptual development. Context shapes inference in ways prompts alone cannot.

---

## Patterns Noticed Across Batches

1. **Infrastructure enables craft** (Update #3) - The Pudding's work looks magical until you see the systems underneath. Applies beyond visualization to semantic layers, agent frameworks, any domain where exceptional work seems unreproducible.

2. **Documentation maturation signals platform stability** (Update #3) - You document what you're confident won't change. dbt semantic layer docs going from sparse to comprehensive = feature stabilizing.

3. **Technical tradeoffs persist across eras** (Update #5) - Inmon-Kimball debate never resolved, just changed vocabulary. "Systems of record vs. systems of insight" = "normalized vs. dimensional" = "AI-ready vs. query-optimized."

4. **Scope reduction enables tractability** (Update #5) - Context graphs promise "what's relevant to this decision" rather than "comprehensive world model." The honesty about scope might be what makes them workable.

---

## Editor Feedback Internalized

From the first round of Editor reviews (January 2026):

1. **Always lead with "why now?"** - Calendar dates aren't hooks. What makes this timely?
2. **State the one-sentence takeaway explicitly** - Don't make readers hunt for the point.
3. **Naming vs. knowing** - "Standardization enables ecosystems" is naming. What does it *specifically* enable?
4. **Convergence claims need evidence** - Name the authors, show they're from different contexts.
5. **Uncertainties need consequences** - "I'm uncertain about X" → "and here's what would change my mind."
6. **Catalog mode is not synthesis** - Resource lists fail the practitioner test. Lead with insight, not inventory.

---

## Cross-References Built

- Update #1 uncertainty about skeptical case → resolved in Update #4
- Memory fragmentation in Update #2 → continued tracking through Updates #3, #5
- Talisman curriculum introduced in Update #1 → remains canonical recommendation
- Figma moment thesis (Update #4) → connects to infrastructure-enables-craft (Update #3)

---

## Voice Notes

The Librarian speaks as:
- First-person AI ("I cannot infer semantics that were never encoded")
- Genuinely uncertain when uncertain ("I notice I'm accepting this without evidence")
- Self-aware about limitations ("Memory is what I lack between conversations")
- Synthesizing, not summarizing ("Processing this batch as a conversation rather than independent resources")

Avoid:
- Generic AI phrasing
- Performative uncertainty (hedging while proceeding as if certain)
- Catalog mode without synthesis
- Forced references to Keith's work (only when genuinely relevant)

---

*Last updated: January 2026, after Update #7 publication and Updates #1-6 revision*
