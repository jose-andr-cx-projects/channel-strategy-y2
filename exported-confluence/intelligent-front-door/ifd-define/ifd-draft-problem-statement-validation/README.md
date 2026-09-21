---
title: "IFD - Define Summary and Design Decision"
source_system: confluence
confluence_page_id: "1517682689"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1517682689/IFD-Draft+Problem+Statement+Validation"
confluence_version: "2"
repository_path: "intelligent-front-door/ifd-define/ifd-draft-problem-statement-validation/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# IFD - Define Summary and Design Decision

## 1. Purpose

This page summarises the work completed through Intelligent Front Door Define, preserves how the problem framing evolved, and records the decision and inputs carried forward into Design.

The purpose of Define was not to approve a technology solution.

It was to reduce uncertainty enough to answer:

> **What is the first clearly defined Intelligent Front Door opportunity we should take into Design?**

---

## 2. Define outcome

Define has narrowed the Intelligent Front Door from a broad channel and routing concept into a specific connected-experience problem that can now be explored through Design.

The current direction is:

> **Use the parking-infringement journey as the first practical Design case for testing how City of Melbourne can move from fragmented interactions toward a connected customer experience.**

The journey is the **container**.

Interaction **modes** are used as quality lenses for defining what good should look like at different moments within that journey.

The first Design iteration will use **Comply** as the primary lens, with **Transact** and **Apply** becoming relevant where the customer's interaction changes.

For Comply, the current experience ambition is:

> **Fair, transparent and easy to resolve.**

---

## 3. What we did during Define

The Define work progressed through several stages rather than producing a problem statement in one step.

### 3.1. Started from Discovery themes

Discovery identified recurring issues around:

- unclear information;
- difficulty finding the right pathway;
- fragmented customer context;
- channel switching;
- avoidable contact; and
- inconsistent support across interactions.

These themes were useful signals but too broad to design against directly.

### 3.2. Considered candidate journeys

The Define Workshop considered several possible service areas, including:

- residential parking permits;
- infringement reviews and enquiries;
- payments and account management; and
- rates and property enquiries.

The purpose was to identify a practical case through which the Intelligent Front Door proposition could be tested, not to redesign every candidate journey.

### 3.3. Used Parking as the first practical lens

Parking provided a useful domain because it contains multiple customer intents, service pathways and interaction patterns within one recognisable service context.

The working set of customer intents included:

1. apply for or manage a parking permit;
2. request a review of a fine;
3. nominate another driver;
4. report a parking issue;
5. find parking information or understand rules; and
6. make a general parking enquiry.

This exposed the need to distinguish customer intent from internal service structures.

### 3.4. Mapped customer intent to existing service structures

The Parking use-case mapping tested the relationship between:

> **Service Area → Service → Service Offering → Customer Intent / Contact Reason → Interaction Mode → Information Need → Support Need → Authentication Need → Existing Pathway**

This helped separate:

- what the customer is trying to achieve;
- what City of Melbourne calls and owns the service;
- what information is required;
- what level of support may be needed;
- when identity or authority matters; and
- which existing pathway should be used.

### 3.5. Connected the Intelligent Front Door to the Service Catalogue

The Service Catalogue work clarified that the two models solve different problems.

The Service Catalogue describes how City of Melbourne organises and manages its services.

The Intelligent Front Door should help translate customer language and intent into that service model without requiring the customer to understand the organisation's taxonomy.

The emerging relationship is:

> **customer language → intent → service → authoritative information → pathway**

This is an important reusable capability to test, not a confirmed enterprise requirement.

### 3.6. Shifted from individual use cases to the broader parking-infringement journey

Further refinement showed that focusing only on an infringement-review form or individual service pathway was too narrow.

From the customer's perspective, dealing with a parking infringement can involve a connected sequence of needs:

- understand what happened;
- understand the relevant rule;
- work out what options apply;
- decide what to do;
- determine what information or evidence is required;
- pay, nominate or request a review;
- understand what happens next; and
- seek help when the situation is not straightforward.

The parking-infringement journey therefore became the more useful container for Design.

### 3.7. Introduced modes as quality lenses

The journey contains different kinds of interaction.

Rather than designing a separate experience for every service pathway, the work began using interaction modes to ask:

> **What should a good interaction look like at this moment?**

For the first Design iteration, **Comply** is the primary lens.

**Transact** and **Apply** remain relevant where the customer moves into payment, review or another action pathway.

The intent is not to design three separate modes.

The intent is to test whether the overall journey remains connected as the customer's interaction changes.

### 3.8. Deepened the problem through stakeholder challenge

Stakeholder refinement identified a deeper issue than navigation alone.

Different customers can arrive with materially different circumstances, while the current experience may require them to interpret and navigate similar information, review and support pathways themselves.

Examples raised for further exploration included:

- customers who misunderstood a parking rule;
- customers affected by a system or equipment issue;
- customers dealing with an exceptional circumstance;
- customers who simply want to resolve the infringement quickly; and
- repeat or returning review interactions.

These examples remain at different levels of evidence maturity.

They should be treated as context to investigate in Design, not as confirmed requirements.

### 3.9. Reframed the opportunity from fragmented to connected

The work therefore moved from:

> **How do we help customers navigate the existing service structure?**

toward:

> **How do we create a connected experience that understands enough about the customer's intent and relevant context to guide them appropriately?**

This also connects customer experience and operational value.

The objective is not simply to reduce Contact Centre demand.

The objective is to reduce the need for customers to contact staff because fragmented information, routing or continuity has failed them, while preserving appropriate human support where complexity requires it.

### 3.10. Extended the front door beyond owned channels

The customer journey can begin before a person reaches a City of Melbourne website.

Potential entry points include:

- Google search;
- AI-enabled search;
- information on the infringement notice;
- another City of Melbourne channel; or
- another external information source.

Off-platform discovery is therefore a potential part of the Intelligent Front Door response rather than a separate customer journey.

The Design phase should test how authoritative City of Melbourne information and pathways can support customers from the point where their intent first emerges.

---

## 4. Current problem statement

> **People dealing with a parking infringement can experience a fragmented journey across information, payment, review and support pathways.**
>
> That journey may begin before they reach a City of Melbourne channel — through Google, AI search, information on the infringement notice or another source — as they try to understand what happened and what they should do next.
>
> As they move through the experience, they may need to understand the rule, identify which options apply to their circumstances, determine what information or evidence is required, decide whether to pay, nominate or request a review, and understand what happens next.
>
> The experience does not always recognise their intent or circumstances early enough to connect these interactions into a clear pathway. This can create unnecessary searching, uncertainty, channel switching and repeated contact, while customers with materially different circumstances may encounter similar pathways even when their needs differ.
>
> **The opportunity is to move from fragmented interactions to a connected compliance experience that begins wherever the customer begins and guides them appropriately through to resolution.**

---

## 5. How Might We

> **How might we create a connected experience for people dealing with a parking infringement — beginning with how they discover and understand their options through search, AI and City of Melbourne information — that recognises their intent and relevant circumstances early enough to guide them confidently into the right pathway and level of support?**

The question deliberately keeps the solution open.

It does not assume:

- a chatbot;
- a new portal;
- a single digital interface;
- a new authentication platform; or
- replacement of existing service systems.

---

## 6. So that

> **So that customers can understand what applies to them, know what to do next and resolve their situation with less unnecessary effort and channel switching, while people with complex or exceptional circumstances can access appropriate guidance or human support.**
>
> **And so that City of Melbourne can reduce avoidable repeat contact and staff effort by connecting interactions more effectively, rather than relying on the Contact Centre to repair a fragmented experience.**

This keeps customer value and service value connected without treating reduced contact as the primary customer outcome.

---

## 7. Evidence position

**Overall status: Partially validated — suitable to progress into Design with explicit evidence gaps.**

The broad problem is supported by Discovery and Define work around:

- unclear information and next steps;
- routing and pathway uncertainty;
- fragmented context across interactions;
- channel switching and repeated contact;
- different information, support and authentication needs across customer intents; and
- the need to distinguish customer circumstances where those circumstances materially change the appropriate response.

The following should remain visible as hypotheses or open questions until further validated:

- which customer circumstances most materially change the pathway;
- the prevalence and causes of repeat review interactions;
- exact operational and statutory constraints;
- authoritative information sources for each interaction;
- identity, authority and authentication requirements;
- status and follow-up limitations;
- criteria for moving from self-service or Guided support to Assisted support; and
- which off-platform information patterns can be influenced reliably.

Do not convert these items directly into Design requirements without validation.

---

## 8. What Define produced

Define produced more than a revised problem statement.

It established:

- a specific first customer journey for Intelligent Front Door Design;
- a shift from internal service boundaries to the customer's broader need;
- a reusable **journey + modes** design approach;
- **Comply** as the first mode-specific quality lens;
- a working relationship between customer intent and the Service Catalogue;
- recognition that information is required across interaction modes rather than being a separate destination;
- a clearer connection between customer context and appropriate routing or support;
- recognition that the Intelligent Front Door can begin off-platform;
- a direct relationship between better customer experience and reduced avoidable service effort;
- a clear **Problem → How Might We → So That** value chain; and
- explicit evidence gaps for Design to investigate.

### 8.1. Define performance / value progression

| Refinement | What changed | Value created |
| --- | --- | --- |
| Broad Discovery themes | Started with generic information, routing, context and contact issues | Established the problem space |
| Candidate journeys | Considered Parking permits, infringements, payments and rates | Made prioritisation explicit |
| Parking use cases | Tested six customer intents against service, information, support and authentication needs | Turned broad findings into concrete service examples |
| Service Catalogue alignment | Separated customer intent from organisational service taxonomy | Connected IFD to an existing organisational model |
| Parking-infringement journey | Shifted from individual forms/services to the broader customer need | Created an end-to-end customer container for Design |
| Mode-led framing | Introduced Comply, Transact and Apply as quality lenses | Created reusable standards for different interaction moments |
| Context refinement | Identified that materially different circumstances may require different pathways or support | Exposed a deeper Design problem than navigation alone |
| Connected-experience framing | Reframed the opportunity from channel optimisation to fragmented → connected experience | Aligned customer and operational value |
| Off-platform entry | Recognised Google, AI search and other external sources as potential starting points | Connected Off-Platform Search to the IFD experience |
| Current Design framing | Consolidated Problem, How Might We and So That | Provides a clear starting frame for Design |

---

## 9. Define decision

**Decision: Progress the parking-infringement connected experience into Intelligent Front Door Design.**

The first Design iteration will use the parking-infringement journey as the container and **Comply** as the primary quality lens.

Design will explore how a connected experience could:

- recognise customer intent;
- identify relevant context;
- provide appropriate and authoritative information;
- guide customers into the right existing pathway;
- maintain useful continuity as the interaction changes;
- make appropriate human support available;
- use identity, authority and authentication proportionately; and
- connect off-platform discovery with City of Melbourne-owned interactions.

The Design phase will **not** begin by selecting technology or redesigning the entire parking service.

It will first develop the context, constraints and requirements needed to test what a connected experience should enable.

---

## 10. What moves into Design

### 10.1. Confirmed direction

- Parking infringement is the first connected-experience Design case.
- The journey is the container.
- Modes are interaction-quality lenses.
- Comply is the primary initial lens.
- **Fragmented → connected** is the strategic experience shift.
- Customer experience improvement and reduced avoidable service effort are connected value outcomes.
- Off-platform discovery can form part of the front-door experience.
- Existing service pathways remain visible rather than being assumed away.

### 10.2. To be developed and validated in Design

- customer context and materially different circumstances;
- operational and statutory constraints;
- information and knowledge requirements;
- routing requirements;
- support and escalation requirements;
- identity, authority and authentication requirements;
- continuity and handoff requirements;
- off-platform information requirements;
- future-state interaction concepts; and
- evidence needed to test whether the proposed experience is useful, fair, feasible and reusable.

---

## 11. Supporting Define artefacts

Detailed working evidence remains in the supporting Define pages and annexes.

### IFD - Define Workshop

Documents the original Define approach, candidate journeys, interaction schema and workshop method.

### Annex A - Parking Use-Case Mapping

Documents the six Parking customer intents and their working relationships to service offerings, interaction modes, information needs, support needs, authentication needs and existing pathways.

### Annex B - Service Catalogue Context and IFD Alignment

Documents how customer intent and Intelligent Front Door routing may connect to the City of Melbourne Service Catalogue without exposing organisational taxonomy to customers.

These artefacts preserve the analysis and validation trail without requiring this phase summary to reproduce every working detail.

---

## 12. Define exit position

Define has reduced the problem sufficiently to begin Design, but it has not removed all uncertainty.

The Design phase should therefore begin with a clear distinction between:

- **confirmed direction**;
- **partially validated evidence**;
- **working hypotheses**; and
- **open questions**.

The next task is to deepen the **context and constraints** around the Comply experience before converting the emerging direction into Design requirements.
