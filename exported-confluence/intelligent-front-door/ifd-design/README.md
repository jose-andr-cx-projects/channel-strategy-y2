---
title: "IFD - Design"
source_system: confluence
confluence_page_id: "1348370437"
confluence_space_id: "68452354"
confluence_status: "current"
confluence_url: "https://jira-cityofmelbourne.atlassian.net/spaces/cex/pages/1348370437/IFD+-+Design"
confluence_version: "1"
repository_path: "intelligent-front-door/ifd-design/README.md"
generated: true
---

> **Source note:** Generated from Confluence. Do not edit directly while Confluence remains the source of truth.

# IFD - Design

## Page status

| Field | Details |
| --- | --- |
| Parent page | Intelligent Front Door |
| Workstream | Intelligent Front Door |
| Phase | Design |
| Status | In progress |
| Owner | Jose Andrade |
| Contributors | Relevant CX, Parking, Contact Centre, service design, digital, content and service stakeholders |
| Related Y2 outcome | Connected Interactions Framework and service information architecture foundations |

---

## 1. Purpose of this phase

The Design phase turns the agreed Intelligent Front Door problem into a practical, testable future-state approach.

The first Design iteration uses the **parking-infringement journey** as the container for testing how City of Melbourne can move from fragmented interactions toward a more connected customer experience.

The work is not starting from a technology solution.

It is starting from the customer problem, the context in which that problem occurs, and the capabilities a connected experience may need to provide.

The phase should progressively answer:

> **What should a connected parking-infringement experience enable so customers can understand what applies to them, move confidently into the right pathway and receive the right level of support?**

---

## 2. Design North Star

> **Create and test a connected experience that begins wherever the customer begins, recognises their intent and relevant context, and guides them toward the right information, pathway and support while respecting operational and statutory constraints.**

The first iteration is intended to help the project move from:

> **fragmented interactions**

to:

> **a connected customer experience**

without assuming that every customer should receive the same pathway or that every interaction should become self-service.

---

## 3. Inputs from Define

### 3.1. Problem statement

> **People dealing with a parking infringement can experience a fragmented journey across information, payment, review and support pathways.**
>
> That journey may begin before they reach a City of Melbourne channel — through Google, AI search, information on the infringement notice or another source — as they try to understand what happened and what they should do next.
>
> As they move through the experience, they may need to understand the rule, identify which options apply to their circumstances, determine what information or evidence is required, decide whether to pay, nominate or request a review, and understand what happens next.
>
> The experience does not always recognise their intent or circumstances early enough to connect these interactions into a clear pathway. This can create unnecessary searching, uncertainty, channel switching and repeated contact, while customers with materially different circumstances may encounter similar pathways even when their needs differ.
>
> **The opportunity is to move from fragmented interactions to a connected compliance experience that begins wherever the customer begins and guides them appropriately through to resolution.**

### 3.2. How Might We

> **How might we create a connected experience for people dealing with a parking infringement — beginning with how they discover and understand their options through search, AI and City of Melbourne information — that recognises their intent and relevant circumstances early enough to guide them confidently into the right pathway and level of support?**

### 3.3. So that

> **So that customers can understand what applies to them, know what to do next and resolve their situation with less unnecessary effort and channel switching, while people with complex or exceptional circumstances can access appropriate guidance or human support.**
>
> **And so that City of Melbourne can reduce avoidable repeat contact and staff effort by connecting interactions more effectively, rather than relying on the Contact Centre to repair a fragmented experience.**

### 3.4. Evidence position

**Partially validated — suitable to progress into Design with explicit evidence gaps.**

The broad problem is supported by Discovery and Define work.

Specific customer circumstances, service rules and operational constraints remain at different levels of evidence maturity and should be tested rather than silently converted into requirements.

---

## 4. Design posture

### 4.1. Journey as the container

The parking-infringement journey is the container for Design.

It allows the team to examine a connected customer need rather than treating individual forms, webpages, teams or service offerings as separate experiences.

### 4.2. Modes as quality lenses

Interaction modes help define what good should look like at different moments within the journey.

The first Design iteration will use **Comply** as the primary quality lens.

For Comply, the current ambition is:

> **Fair, transparent and easy to resolve.**

**Transact** and **Apply** become relevant where the customer's interaction changes, for example when they move into payment or review.

The intent is not to design separate mode experiences.

The intent is to test whether the journey remains coherent as the customer's needs and interaction mode change.

### 4.3. Connected does not mean one pathway for everyone

A connected experience should not force materially different customer circumstances into one standard flow.

For this work:

> **Connected means enough continuity and understanding to provide the right next interaction for the customer's circumstances, within legitimate service constraints.**

### 4.4. The front door can begin off-platform

The customer may begin through:

- Google search;
- AI-enabled search;
- information on an infringement notice;
- another City of Melbourne channel; or
- another external information source.

Off-platform discovery should therefore be considered part of the Intelligent Front Door response where it helps customers reach authoritative information and the appropriate City of Melbourne pathway.

---

## 5. Context overlay

### 5.1. Purpose

The mode tells us what a good interaction should feel like.

The context overlay identifies what is materially different about the customer's situation or the service environment that may change the information, pathway, support or controls required.

The current context should be treated as a combination of:

> **customer circumstance + operational context + service constraints**

leading to:

> **an appropriate connected response**

---

### 5.2. Customer circumstances to explore

Current working circumstances include:

| Customer circumstance | Current status | Design question |
| --- | --- | --- |
| I understand the fine and want to resolve it | Working scenario | Can the routine pathway be recognised quickly and completed with minimal unnecessary effort? |
| I thought I was doing the right thing or misunderstood the rule | Reported / hypothesis to validate | Can the experience explain what happened, what rule applied and what legitimate options exist? |
| Something in the system or equipment may have failed | Working hypothesis | Can the experience recognise this situation and guide the customer toward the appropriate evidence or review pathway? |
| I faced an exceptional or unavoidable circumstance | Working hypothesis | How should exceptional circumstances be recognised and supported without implying a particular review outcome? |
| I have already contested this or I am returning again | Open — requires evidence | Is the customer returning because of unresolved need, disagreement, misunderstanding, new evidence, misuse or another reason, and what should change in the response? |

These are not confirmed customer segments or requirements.

They are design contexts to investigate.

---

### 5.3. Identity and authority

Identity and authority may be different design needs.

Some interactions may require City of Melbourne to know who a person is.

Others may require confirmation that the person has authority to act in relation to the infringement, vehicle or another person.

**Design question**

> What does City of Melbourne actually need to know about the person, the vehicle and their authority to act — and at what point?

Do not assume authentication is required before the customer has reached an action that genuinely requires it.

---

### 5.4. Identifiers and continuity

The current experience can involve different identifiers, including infringement/PIN references, issue references and internal case numbers.

Customers may also use generic language such as "reference number".

**Design question**

> What information needs to remain recognisable across channels so the customer and staff can confidently refer to the same matter?

This is a continuity issue as much as an information issue.

---

### 5.5. Repeat and returning interactions

Repeat interaction may represent a materially different context, but the cause should not be assumed.

Possible explanations include:

- unresolved need;
- misunderstanding;
- disagreement with an outcome;
- new evidence;
- uncertainty about what happens next; or
- behaviour that requires a different operational response.

**Design question**

> When someone comes back after a previous interaction or decision, what prior context should change the guidance, pathway or support they receive?

---

### 5.6. Status and follow-up

Customers naturally want to understand what happens after they act.

There may be statutory or operational limits on the status information City of Melbourne can provide for infringement reviews.

The exact limitation requires validation before being treated as a confirmed requirement.

**Design question**

> Where City of Melbourne cannot provide the status information customers naturally expect, what can it explain clearly about process, timeframe and what happens next?

---

### 5.7. Internal service structure

Internal service classifications can leak into the customer experience.

The Intelligent Front Door should not require customers to understand organisational taxonomy before they can understand what applies to them.

**Design question**

> What service structure needs to remain behind the experience, and what needs to be translated into customer language?

---

### 5.8. Emotional and complex interactions

Parking infringements can generate emotionally charged or complex interactions.

An efficient digital pathway may suit one customer while another may need human guidance or specialist support.

**Design question**

> What signals suggest the customer needs more guidance or human support rather than another self-service step?

---

## 6. Design requirement areas

### 6.1. Umbrella requirement

> **The Intelligent Front Door should help create a connected experience by recognising enough about the customer's intent and relevant context to provide the right information, pathway and level of support — while respecting service, statutory and operational constraints.**

The current requirement areas are:

| Requirement area | What the experience needs to enable | Current status |
| --- | --- | --- |
| **Information & knowledge** | Give customers the authoritative information needed to understand what happened, what applies, what options exist, what they need to provide and what happens next | Initial requirement set documented |
| **Intent & routing** | Recognise what the customer is trying to resolve and guide them toward the appropriate existing pathway without requiring knowledge of internal service structures | In development |
| **Context & continuity** | Retain or reconnect relevant context as customers move between information, digital pathways and human support | To develop |
| **Support & escalation** | Match guidance and human support to the customer's circumstances and complexity | To develop |
| **Identity, authority & authentication** | Establish identity or authority only when necessary for the action being taken | To develop |
| **Discovery & off-platform entry** | Support accurate discovery through search, AI-enabled search, notices and owned channels while guiding customers toward authoritative City of Melbourne pathways | To develop |

These are **design requirement areas**, not detailed business or technical requirements.

---

## 7. Requirement area 1 — Information & knowledge

### 7.1. Customer need

> **Help me understand what happened, what applies to my circumstances, what my legitimate options are, what I need to provide and what I should do next.**

### 7.2. Service need

Provide authoritative, consistent and customer-readable information across the places where the journey begins and continues, without requiring the customer to interpret internal service structures or reconstruct information across channels.

### 7.3. Working design requirement

> **The connected experience should provide the minimum authoritative information needed for the customer to understand their situation and make the next decision confidently, adapting the information where relevant context materially changes the options, evidence, pathway or support required.**

### 7.4. Evidence status

**Partially validated.**

The need for clearer information is established.

Exactly which information should change based on circumstance, intent, authority, previous interaction or pathway still requires validation.

### 7.5. Open question

> **What information is universal across the parking-infringement journey, and what must change based on customer circumstance, action, authority or previous interaction?**

---

### 7.6. Information requirement 1 — explain the situation before asking the customer to act

Customers should be able to understand:

- what happened;
- why they received the infringement; and
- what rule applies.

**Working requirement**

> **The experience should explain the relevant rule and situation in language the customer can understand before requiring them to choose an action.**

**Evidence status:** Partially validated.

---

### 7.7. Information requirement 2 — make legitimate options understandable

Customers should be able to distinguish between actions such as:

- pay;
- nominate;
- request a review; and
- seek information or support.

They should not need to know which internal team, form, service offering or system owns each pathway.

**Working requirement**

> **The experience should present available actions around the customer's intent and circumstances rather than requiring them to navigate City of Melbourne's internal service structure.**

**Evidence status:** Strong working direction.

---

### 7.8. Information requirement 3 — tell customers what they need before they start

Before entering a pathway, customers may need clarity about:

- information;
- evidence;
- authority;
- identity or authentication;
- deadlines; and
- prerequisites.

**Working requirement**

> **Before a customer enters a pathway, the experience should make clear what information, evidence, authority or authentication will be required so they can make an informed decision about proceeding.**

**Evidence status:** Customer need validated; exact pathway rules remain open.

---

### 7.9. Information requirement 4 — explain what happens after the action

The connected experience should not end at submission.

Customers may need to understand:

- confirmation;
- expected timeframe;
- what happens next;
- what follow-up is possible; and
- when escalation or further support is appropriate.

**Working requirement**

> **The experience should clearly explain what happens after an action, including expected process and timeframe, and transparently explain any limits on status or follow-up information.**

**Evidence status:** Need established; specific constraints require validation.

---

### 7.10. Information requirement 5 — keep authoritative information coherent wherever the journey starts

The customer may encounter information before reaching the City of Melbourne website.

City of Melbourne cannot control every external search or AI response.

The Design opportunity is to ensure that authoritative City of Melbourne information is clear, structured and consistent enough to support reliable discovery and guide customers toward the appropriate pathway.

**Working requirement**

> **Authoritative customer information should be sufficiently clear, structured and consistent that customers can receive useful guidance whether they begin through an infringement notice, search, AI-enabled discovery, City of Melbourne web content or assisted support.**

**Evidence status:** Working Design hypothesis to test through Off-Platform Search and Design.

---

### 7.11. What good looks like for Information & knowledge

A connected Comply experience should allow a customer to say:

> **I understand what happened.**  
> **I understand what applies to me.**  
> **I know my legitimate options.**  
> **I know what I need before I choose one.**  
> **I know what will happen next.**

Better information is not the end goal.

It creates value when it helps the customer make the **right next decision with less unnecessary searching, uncertainty, channel switching or staff intervention**.

---

## 8. Requirement area 2 — Intent & routing

### 8.1. Customer need

> **Help me quickly work out what I am trying to do and get me to the right place without making me understand City of Melbourne's service structure first.**

Customers may arrive with language such as:

- "I just want to pay this";
- "I think this fine is wrong";
- "someone else was driving";
- "I do not understand why I got this";
- "I need help because my situation is different"; or
- a broader parking question that does not yet map cleanly to a service pathway.

The experience should help translate that customer language into an appropriate next action.

### 8.2. Service need

City of Melbourne needs a consistent way to distinguish customer intents that lead to materially different information, pathways, controls or support.

The routing logic should:

- recognise customer intent before exposing internal service classifications;
- ask only enough questions to distinguish the next appropriate action;
- use relevant context where it changes the pathway or level of support;
- connect the customer to an existing service pathway where one already exists;
- preserve appropriate human support as a valid destination; and
- allow the route to change when new information shows that the original interpretation was wrong.

### 8.3. Working design requirement

> **The connected experience should identify the customer's intended action with the minimum necessary questions, distinguish intents that require materially different pathways, and guide the customer to the appropriate existing pathway or level of support without requiring them to understand City of Melbourne's internal service structure.**

### 8.4. Evidence status

**Partially validated — strong working direction.**

Define established that Parking contains multiple customer intents that do not map neatly to one customer-facing pathway.

The use-case work also showed that "general enquiry" is better treated as an ambiguous starting point that should be resolved into a clearer intent, rather than as the destination itself.

The exact routing questions, service rules and escalation conditions still require validation.

### 8.5. Open questions

> **What is the minimum information needed to distinguish the customer's intended action confidently enough to guide the next step?**

Additional questions include:

- Which intents can be recognised without identity or authentication?
- Which customer circumstances materially change the route?
- When should the experience provide information first rather than send the customer directly into a form or transaction?
- When should ambiguity trigger Guided or Assisted support?
- Which existing pathways are appropriate once the customer's intent is understood?
- Where is the underlying pathway itself the problem rather than the routing into it?

---

### 8.6. Routing requirement 1 — recognise customer intent before service structure

The customer should not need to select an internal service name before City of Melbourne can help.

**Working requirement**

> **The experience should begin from the customer's goal or situation and translate that into the relevant City of Melbourne service or pathway behind the experience.**

This preserves the distinction established in Define:

> **Customer intent describes what the customer is trying to achieve. The Service Catalogue describes what City of Melbourne delivers.**

The Intelligent Front Door provides the translation layer between them.

**Evidence status:** Strong working direction.

---

### 8.7. Routing requirement 2 — distinguish materially different actions early

Several parking-infringement actions can begin from the same event but require different pathways.

Examples include:

- pay the infringement;
- request a review;
- nominate another driver;
- understand the rule or infringement;
- seek help because the customer's situation does not fit the standard path; or
- raise another issue that initially appears related.

**Working requirement**

> **The experience should distinguish materially different customer actions early enough to avoid sending customers into an inappropriate pathway and requiring them to recover later.**

This is the practical expression of the Define principle:

> **Intent disambiguation before pathway selection.**

**Evidence status:** Partially validated.

---

### 8.8. Routing requirement 3 — use context only where it changes the response

A connected experience should not interrogate every customer simply because some customers have complex circumstances.

Context is useful when it materially changes:

- the information presented;
- the pathway;
- evidence requirements;
- authority or authentication requirements; or
- the level of support.

**Working requirement**

> **The experience should ask for additional context only when that context is needed to change or confirm the next appropriate interaction.**

This supports a simpler routine experience while still allowing more complex circumstances to be recognised.

**Evidence status:** Working Design hypothesis.

---

### 8.9. Routing requirement 4 — connect clearly into the existing pathway

The Intelligent Front Door is not intended to replace every underlying service process in the first iteration.

Where an appropriate pathway already exists, the customer should understand:

- why this pathway applies;
- what they need before entering it;
- what will happen when they continue; and
- whether they are moving into a different interaction mode.

**Working requirement**

> **When routing a customer into an existing pathway, the experience should make the transition understandable and preserve the information needed for the customer to continue confidently.**

**Evidence status:** Strong working direction; continuity details remain to develop.

---

### 8.10. Routing requirement 5 — allow the route to recover when the situation changes

Customer intent may be ambiguous at first or change as the customer learns more.

For example, a person may begin by trying to understand a fine, then decide to pay, nominate another driver or request a review.

**Working requirement**

> **The connected experience should allow customers to change direction without unnecessarily restarting the journey when new information changes the action they need to take.**

Where the experience cannot confidently determine the right path, uncertainty should trigger additional guidance or appropriate human support rather than a forced routing decision.

**Evidence status:** Working Design hypothesis.

---

### 8.11. Routing is not channel deflection

Routing should not be optimised solely to reduce Contact Centre demand.

A successful route may be:

- self-service;
- a guided digital pathway;
- a transaction;
- a review process;
- an assisted interaction; or
- specialist human support.

The design objective is:

> **the right next interaction for the customer's need**

rather than:

> **the lowest-cost channel regardless of circumstance**

This keeps the customer-experience ambition and operational-efficiency objective aligned.

---

### 8.12. What good looks like for Intent & routing

A connected Comply experience should allow a customer to say:

> **I do not need to know what City of Melbourne calls the service.**  
> **I can explain what I am trying to do in terms that make sense to me.**  
> **I am only asked questions that help determine my next step.**  
> **I understand why I am being directed to this pathway.**  
> **If my situation changes, I can change direction without starting over unnecessarily.**

Better routing creates value when customers reach the **appropriate next interaction with less searching, misdirection, channel switching or recovery effort**, while staff receive customers whose needs genuinely require assisted support.

---

## 9. Evidence discipline

During Design, distinguish:

- **Confirmed direction**
- **Partially validated evidence**
- **Reported observation**
- **Working hypothesis**
- **Open question**

Do not convert:

- a stakeholder comment;
- an operational workaround;
- an assumed statutory constraint; or
- a proposed technology response

directly into a confirmed Design requirement.

Requirements should remain traceable to a customer need, service need, validated constraint or explicit testable hypothesis.

---

## 10. Current scope

### In scope

- parking-infringement journey;
- Comply as the primary mode lens;
- transitions into Transact and Apply where relevant;
- information and knowledge;
- customer intent and routing;
- context and continuity;
- support and escalation;
- identity, authority and authentication;
- off-platform discovery;
- existing service pathways;
- future-state concepts and prototypes;
- validation with relevant customer, frontline, service and design perspectives.

### Out of scope for the first iteration

- redesign of the entire Parking service;
- changing infringement policy or statutory rules;
- redesigning all back-office workflows;
- selecting a final enterprise technology architecture;
- assuming a chatbot or AI assistant as the solution;
- replacing existing service delivery platforms; and
- eliminating human support.

---

## 11. Design principles

| Principle | What it means for this work |
| --- | --- |
| Connected interactions over channel optimisation | Design the experience across discovery, information, pathways and support rather than fixing one channel in isolation |
| Customer intent before organisational structure | Customers should not need to understand City of Melbourne taxonomy before taking the right action |
| Different circumstances can require different responses | Do not force all customers through the same experience where context materially changes the appropriate response |
| Minimum necessary information and authentication | Ask only for what is required at that point in the journey |
| Human support remains visible | Do not optimise self-service by hiding appropriate Assisted support |
| Existing pathways remain visible | Test how the IFD improves entry and continuity before assuming underlying services must be replaced |
| Evidence before requirements | Preserve uncertainty and validate material assumptions |
| Reuse beyond one journey | Look for patterns that can contribute to the Connected Interactions Framework |

---

## 12. Current Design sequence

The current working sequence is:

1. **Problem** — established through Define.
2. **Context** — identify customer circumstances, operational context and service constraints.
3. **Requirement areas** — define what a connected experience needs to enable.
4. **Detailed requirements** — develop each requirement area from evidence.
5. **Future-state concepts** — explore multiple responses without prematurely selecting technology.
6. **Prototype and test** — test usefulness, clarity, fairness, feasibility and reusability.
7. **Decision** — determine what is strong enough to progress into Deliver.

### Next requirement area

**Context & continuity**

The next step is to define:

- customer need;
- service need;
- working design requirement;
- evidence status;
- open questions; and
- what context needs to persist or be reconnected as customers move between information, pathways and human support.

---

## 13. Design exit criteria

Design can move into Deliver when:

- the future-state concept is clearly linked to the defined problem;
- the connected customer journey or interaction flow is documented;
- the role of modes within the journey is clear;
- customer context and material constraints are understood;
- the six requirement areas are sufficiently defined;
- channel and off-platform roles are clear;
- staff, service team and operational impacts are visible;
- content, knowledge and data needs are documented;
- key assumptions have been tested or remain explicitly caveated;
- privacy, records, accessibility, security and operational risks are visible;
- success measures are clear enough to test; and
- there is enough evidence to make a decision on whether to pilot, implement, refine or stop.

---

## 14. Final Design outcome

By the end of Design, the team should have a practical and testable future-state approach for the first Intelligent Front Door use case.

Most importantly, the team should be able to answer:

> **Does this connected experience materially improve how customers understand, navigate and resolve their situation while also reducing avoidable service effort and preserving appropriate human support?**

If the answer is yes, the work can progress toward Deliver.

If the answer is partial or no, the specific design, evidence or service constraint should be identified before further investment.
