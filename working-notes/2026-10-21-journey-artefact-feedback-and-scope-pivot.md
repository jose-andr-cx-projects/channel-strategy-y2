# Journey artefact critique and proposed scope pivot — 21 October 2026

**Workstream:** Channel Strategy Y2 / Intelligent Front Door (IFD)  
**Status:** Workshop feedback and proposed response — **not an endorsed design decision**  
**Evidence:** Mindy's critique of the Modes and Segments Journey Artefact; working sketches exploring a family life moment and "Moving to Melbourne → help and guidance → get orientated"; current Channel Strategy Y2 IFD Design and Define summaries.  
**Authority boundary:** This is a working interpretation in the GitHub project mirror. Confluence remains authoritative for endorsed project decisions. Do not alter Confluence-generated exports directly.

## 1. What the critique identified

The existing parking-infringement design artefact appears to be attempting several jobs at once:

- documenting a customer journey;
- applying demographic Segments and Interaction Modes;
- surfacing pain points, needs and possible branches;
- sketching future Intelligent Front Door capabilities (knowledge, information architecture, context, authentication and routing).

Stakeholder questions highlight five unresolved distinctions:

1. **Purpose and output:** Is this current-state analysis, a design challenge, or a proposed future experience? What specific decision should using it enable?
2. **Primary organising logic:** Customer situations and intent (e.g. pay a fine, nominate a driver, request review) may explain meaningful journey differences better than parallel demographic segment lanes.
3. **Segments and Modes:** Use these to challenge a core journey and test experience expectations, not as competing structures. Only differentiate segments when evidence demonstrates a meaningful need.
4. **Path versus Mode:** Pay / Nominate / Review may be different pathways within a wider **Comply** experience. Do not infer a Mode transition merely from an action label; validate against the agreed Mode definitions.
5. **Meaning of 'intelligent':** Identify the customer problem first, then test whether intent recognition, authoritative guidance, relevant context, continuity, or routing would address it. Avoid assuming a technology solution.

These are questions and interpretation, not validated customer findings.

## 2. Pivot hypothesis: one customer situation, one Job to Be Done, one bounded outcome

**Proposed method:** Life Transition / Situation → Customer Need → Job to Be Done → Bounded Experience → Evidence of friction → Segment and Mode checks → Candidate IFD enablers.

The handwritten workshop exploration offers one candidate:

- **Life transition:** Moving to Melbourne.
- **Need:** Help and guidance.
- **Job to Be Done:** Get orientated.
- **Working experience boundary:** Discover what matters → Understand what applies → Find the right next step.
- **Possible validation context:** A new arrival or young family needing local information and relevant services; this is illustrative, not a confirmed Segment or customer insight.

Do **not** attempt to map all services, life events, channels, or family activities associated with moving. Focus on the initial orientation need. Keep customer demographics and family circumstances as secondary lenses.

## 3. Preserve the current baseline; do not silently replace it

The existing Confluence-derived Define and Design documentation identifies **parking infringement** as the first chosen IFD Design container. This feedback does **not** supersede that documented position.

Two pilot directions remain available for team decision:

| Option | What it tests | Main scope risk |
| --- | --- | --- |
| Retain parking infringements, simplify artefact around one intent | Validates the intent → information → correct pathway model against a bounded operational domain | Continuing to mix many actions and lenses in one view |
| Test Moving to Melbourne → Get orientated | Validates how a connected front door can support a cross-service life transition | Expanding into an unbounded life-stage/service inventory |

**Working recommendation:** If demonstrating connected cross-service experiences is the immediate objective, explore the orientation pilot **only after** confirming its evidence availability and tight entry/exit boundary. If speed of operational validation matters more, retain parking infringements and simplify the artefact first. Ask the team to confirm the test objective before choosing.

## 4. Lean proposed sequence (three weeks, subject to team capacity)

**Week 1 — Scope.** Confirm the pilot choice, decision it should enable, customer situation, entry/exit boundary, one JTBD and evidence inventory. Output: one-page experience brief.

**Week 2 — Examine.** Map one core current-state experience, backed by available customer/service evidence. Annotate meaningful changes from Segments, Modes and specific customer circumstances; leave unsupported differences as hypotheses. Output: compact journey plus evidence and gaps.

**Week 3 — Test implications.** Select one friction point and formulate the minimum front-door response, with knowledge, IA, routing and context requirements derived only where needed. Validate with service, digital and operational stakeholders. Output: one evidence-linked opportunity and recommendation for further testing.

## 5. Artefact design rules for the next iteration

- Lead with **what the customer is trying to achieve**, not demographic lanes or technology components.
- One visual = one question and one intended decision.
- Show **current evidence**, **assumptions**, and **future opportunities** distinctly.
- Keep **Comply / Transact / Apply** as governed Mode lenses; don't redefine them from the diagram.
- Only branch journeys where customer intent or circumstance changes the steps or outcome.
- Keep supporting capabilities as a short requirements register rather than adding full-length layers to the map.
- Stop when the next useful design decision can be made; do not complete every empty box.

## 6. Decisions to seek and handoff

1. Which specific decision must the next artefact enable?
2. Is the first contained pilot **parking fine** or **moving-to-Melbourne orientation**, and why?
3. What existing evidence supports the chosen customer need?
4. Who will review the compact journey, and what would count as useful proof?
5. What is explicitly deferred?

Once agreed, record the decision and its rationale in **Confluence** under IFD Design, then follow the established Confluence-to-GitHub sync process. Track implementation tasks in Jira, not this note.

## Source pointers

- Current mirrored IFD Design: `exported-confluence/intelligent-front-door/ifd-design/README.md`
- Current mirrored IFD Define decision: `exported-confluence/intelligent-front-door/ifd-define/ifd-define-summary-and-design-decision/README.md`
- Workshop inputs: `Modes and Segments Journey Artefact.pdf`; `Channel Strategy Y2-IFD Design Artefact(1).pdf`; two handwritten workshop images supplied 21 October 2026 (not stored in this repository).
