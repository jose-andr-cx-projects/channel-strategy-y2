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
| **Intent & routing** | Recognise what the customer is trying to resolve and guide them toward the appropriate existing pathway without requiring knowledge of internal service structures | Initial requirement set documented |
| **Context & continuity** | Retain or reconnect relevant context as customers move between information, digital pathways and human support | Initial requirement set documented |
| **Support & escalation** | Match guidance and human support to the customer's circumstances and complexity | Initial requirement set documented |
| **Identity, authority & authentication** | Establish identity or authority only when necessary for the action being taken | Initial requirement set documented |
| **Discovery & off-platform entry** | Support accurate discovery through search, AI-enabled search, notices and owned channels while guiding customers toward authoritative City of Melbourne pathways | Initial requirement set documented |

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

## 9. Requirement area 3 — Context & continuity

### 9.1. Customer need

> **Help me continue from where I am without making me repeatedly explain the same situation, rediscover what I already learned or work out how different references and channels relate to the same matter.**

A customer may move between:

- an infringement notice;
- search or AI-enabled discovery;
- City of Melbourne information;
- a payment, nomination or review pathway;
- a Contact Centre interaction;
- a specialist service interaction; and
- a later return to the same matter.

A connected experience should help those interactions feel related where they are part of the same customer need.

### 9.2. Service need

City of Melbourne needs enough relevant context to understand where the customer is in the journey and what has already happened, without collecting, retaining or exposing information that is not necessary.

Useful context may include:

- the customer's current intent;
- the infringement or matter being discussed;
- information or evidence already provided;
- a previous interaction or submission where relevant;
- the pathway already entered;
- the customer's current stage in that pathway; and
- any known constraint that materially changes what can happen next.

The exact context available will vary by channel, system, identity and service rules.

### 9.3. Working design requirement

> **The connected experience should preserve or reconnect the minimum relevant context needed for the customer and City of Melbourne to continue the same journey coherently across interactions, while respecting privacy, authority, system and statutory constraints.**

Continuity does not require every system to share every piece of information.

It requires the experience to avoid unnecessary loss of context where that loss creates customer effort, misrouting or repeated staff work.

### 9.4. Evidence status

**Partially validated — strong problem signal, detailed continuity needs still to validate.**

Define identified fragmented context, channel switching and repeated contact as part of the problem.

The current Parking work also indicates that customers and staff may encounter different identifiers, pathways and interaction histories while dealing with the same matter.

Exactly which context can or should persist across channels and systems remains open.

### 9.5. Open questions

> **What is the minimum context that must persist or be reconnectable for the customer to continue confidently without unnecessary repetition?**

Additional questions include:

- Which context can remain anonymous until the customer enters a pathway that requires identification?
- Which identifiers should be visible or translated for customers?
- What information can legitimately move between digital and assisted interactions?
- What prior interaction should be visible when a customer returns?
- When should previous context influence the next interaction, and when should it not?
- Where do current systems or statutory rules prevent continuity?
- What context should staff receive when a customer moves from digital guidance to human support?

---

### 9.6. Continuity requirement 1 — keep the same matter recognisable

A customer should be able to recognise that different interactions relate to the same infringement or matter even when City of Melbourne systems use different references.

**Working requirement**

> **The experience should maintain a clear customer-facing connection between the infringement or matter and any related pathway, interaction or case reference that the customer may encounter.**

This does not require one universal identifier.

It requires enough translation or explanation that customers and staff can establish that they are talking about the same thing.

**Evidence status:** Partially validated.

---

### 9.7. Continuity requirement 2 — avoid unnecessary repetition when the customer changes channel

Moving from information to a transaction, from digital to assisted support, or from one City of Melbourne channel to another should not automatically require the customer to reconstruct the journey from the beginning.

**Working requirement**

> **Where relevant context has already been provided and can legitimately be reused, the experience should avoid asking the customer to repeat it solely because the interaction has moved to another channel or support mode.**

Where context cannot be carried forward, the experience should make the limitation clear and minimise the amount the customer must provide again.

**Evidence status:** Strong working direction; technical and privacy feasibility to validate.

---

### 9.8. Continuity requirement 3 — preserve progress when the interaction changes

A customer may begin by seeking information and then decide to pay, nominate, request a review or seek human help.

That change should not unnecessarily discard the understanding already established.

**Working requirement**

> **When the customer's next action changes, the experience should preserve relevant progress and context so they can move into the new pathway without restarting unrelated parts of the journey.**

This is the continuity counterpart to the routing requirement that allows customers to change direction.

**Evidence status:** Working Design hypothesis.

---

### 9.9. Continuity requirement 4 — use previous interactions carefully when the customer returns

A returning customer may have:

- an unresolved need;
- a previous decision;
- new evidence;
- a misunderstanding;
- an incomplete action; or
- a different reason for returning.

Previous interaction should therefore inform the next response without predetermining it.

**Working requirement**

> **Where a previous interaction is relevant and legitimately available, the experience should use that context to help understand what has already occurred and what the customer needs now, without assuming that every repeat interaction has the same cause.**

**Evidence status:** Partially validated; reasons for repeat interaction require further evidence.

---

### 9.10. Continuity requirement 5 — support a meaningful handoff to people

Human support is part of the connected experience, not a failure state.

When the customer reaches assisted or specialist support, staff should receive enough relevant context to continue the interaction rather than begin a separate journey.

**Working requirement**

> **When a customer moves into human support, the handoff should provide the minimum relevant context needed for staff to understand the customer's intent, current stage and prior interaction where appropriate.**

The objective is to reduce avoidable repetition while preserving the opportunity for staff to confirm or correct the customer's situation.

**Evidence status:** Strong working direction; specific handoff data remains to define.

---

### 9.11. Continuity requirement 6 — continuity must be proportionate

More retained context is not automatically a better experience.

Some interactions should remain anonymous or low-context, and some information should not be reused beyond the purpose for which it was collected.

**Working requirement**

> **The experience should retain, reconnect or expose only the context necessary for the current customer need and legitimate service purpose.**

Privacy, authority, records, security and statutory requirements remain constraints on what continuity can mean in practice.

**Evidence status:** Design principle; exact controls require specialist validation.

---

### 9.12. What good looks like for Context & continuity

A connected Comply experience should allow a customer to say:

> **City of Melbourne understands which matter I am dealing with.**  
> **I do not have to repeatedly explain information that is already relevant and available.**  
> **When I move to another pathway or person, I can continue rather than unnecessarily start again.**  
> **If City of Melbourne cannot carry something forward, I understand what I need to provide and why.**  
> **When I return later, the experience can recognise relevant prior context without making assumptions about what I need now.**

Better continuity creates value when the journey feels connected across interactions while the organisation uses only the context that is necessary, legitimate and useful.

---

## 10. Requirement area 4 — Support & escalation

### 10.1. Customer need

> **Help me complete the task independently when my situation is straightforward, but make it clear how I can get more guidance or human support when the situation becomes difficult, uncertain or exceptional.**

A connected experience should not assume that every customer needs the same level of support.

Some customers may be able to understand the infringement and complete the next action with minimal guidance.

Others may need more support because:

- they cannot confidently determine which option applies;
- their circumstances do not appear to fit the standard pathway;
- they are unsure what evidence or information is required;
- they are returning after an earlier interaction or decision;
- the available digital pathway does not resolve their need; or
- the interaction has become complex or emotionally difficult.

### 10.2. Service need

City of Melbourne needs a support model that helps routine interactions remain simple while recognising when additional guidance or human assistance adds value.

The support model should:

- avoid forcing customers into assisted channels when self-service is sufficient;
- avoid forcing customers to remain in self-service when it is no longer sufficient;
- provide a clear progression from routine to guided to assisted support;
- preserve relevant context when support level changes;
- help staff understand why the customer has reached them; and
- distinguish customer need from channel cost or operational convenience.

### 10.3. Working design requirement

> **The connected experience should provide the lowest level of support that is sufficient for the customer's current need, while making it easy to move into additional guidance or appropriate human support when complexity, uncertainty or service constraints mean self-service is no longer enough.**

The objective is not to minimise human contact.

The objective is to use human support where it adds value and reduce contact that exists only because the experience failed to explain, route or connect the journey effectively.

### 10.4. Evidence status

**Partially validated — support patterns are established, escalation triggers still require validation.**

Define already used Routine, Guided and Assisted support patterns across Parking use cases.

The parking-infringement work also identified complex, exceptional, returning and emotionally difficult interactions as contexts where different support may be required.

The exact signals for changing support level have not yet been validated.

### 10.5. Open questions

> **What signals tell us that the current level of support is no longer sufficient and that the customer should receive additional guidance or human assistance?**

Additional questions include:

- Which customer needs can be completed confidently through routine self-service?
- Which conditions should trigger Guided support?
- Which conditions genuinely require Assisted or specialist support?
- How should repeated failed attempts affect the support offered?
- What service or statutory constraints require staff involvement?
- What context should be passed to staff so escalation does not become a restart?
- Where are staff currently compensating for information, routing or continuity problems that Design should remove upstream?

---

### 10.6. Support requirement 1 — use the minimum sufficient level of support

**Working requirement**

> **The experience should begin with the minimum level of support sufficient for the customer's need and add guidance only when it materially improves the customer's ability to proceed confidently.**

**Evidence status:** Strong working direction.

---

### 10.7. Support requirement 2 — make additional help visible before failure

**Working requirement**

> **The experience should make the next available level of support visible at points where customers may reasonably need additional guidance, rather than waiting until the interaction has failed.**

The appropriate support may be clearer information, guided decision support, assisted digital support, Contact Centre support or specialist service support.

**Evidence status:** Working Design hypothesis.

---

### 10.8. Support requirement 3 — escalate based on need, not persistence

**Working requirement**

> **Escalation should be based on the customer's current need, complexity and unresolved issue rather than the number of times they have contacted City of Melbourne alone.**

Previous interactions can inform the decision, but should not predetermine why the customer has returned.

**Evidence status:** Working Design hypothesis; repeat-contact causes require further evidence.

---

### 10.9. Support requirement 4 — escalate when uncertainty materially affects the next action

**Working requirement**

> **Where the experience cannot determine an appropriate next step with sufficient confidence, it should provide additional guidance or escalate to appropriate human support rather than forcing the customer into a potentially incorrect pathway.**

This is particularly relevant where intent remains ambiguous, customer circumstances may materially change the pathway, authority or evidence requirements are unclear, or the standard pathway does not appear to fit.

**Evidence status:** Strong working direction; exact thresholds remain to define.

---

### 10.10. Support requirement 5 — human handoff should add value

**Working requirement**

> **When the customer moves into assisted support, the interaction should use relevant available context and enable staff to provide judgement, clarification or action that the previous support level could not provide.**

The purpose of escalation is to increase the usefulness of the interaction, not merely change channel.

**Evidence status:** Strong working direction; exact handoff information remains to validate.

---

### 10.11. Support requirement 6 — preserve access to human support for legitimate complexity

**Working requirement**

> **Where a customer's circumstances genuinely require human judgement, explanation or exception handling, the experience should provide a clear and proportionate route to the appropriate assisted or specialist support.**

This does not imply that human support changes statutory rules or guarantees a different service outcome.

**Evidence status:** Partially validated; service-specific escalation rules require validation.

---

### 10.12. What good looks like for Support & escalation

A connected Comply experience should allow a customer to say:

> **I can resolve a straightforward situation without unnecessary help.**  
> **I can see where to get more guidance before I become stuck.**  
> **I am not forced to stay in self-service when it cannot resolve my need.**  
> **If I move to human support, I do not have to unnecessarily start again.**  
> **The person helping me can add something the previous interaction could not.**

Better support creates value when customers receive enough help to make progress without unnecessary escalation, while human effort is focused on interactions where judgement, clarification or specialist support genuinely adds value.

---

## 11. Requirement area 5 — Identity, authority & authentication

### 11.1. Customer need

> **Let me understand and explore my options before asking me to prove who I am, and only ask for identity or authority when it is genuinely required for the action I want to take.**

Identity, authority and authentication are related but different.

A customer may be able to:

- understand a rule;
- explore options;
- learn what evidence is required; or
- identify the correct pathway

without being authenticated.

A later action may require City of Melbourne to establish:

- who the person is;
- which infringement or matter they are acting on;
- whether they are authorised to act; or
- whether a higher level of identity assurance is required.

### 11.2. Service need

City of Melbourne needs to apply identity, authority and authentication proportionately to the risk and requirements of the customer's intended action.

The experience should distinguish between:

- **identity** — who the person is;
- **authority** — whether they are entitled to act in relation to the matter;
- **authentication** — how identity or access is verified; and
- **matter matching** — confirming which infringement, vehicle or case the interaction relates to.

These should not be treated as one generic login requirement.

### 11.3. Working design requirement

> **The connected experience should ask for identity, authority or authentication only when the intended action requires it, using the minimum level of assurance necessary to proceed safely and lawfully.**

The design should avoid using authentication as a prerequisite for general information or early intent recognition where it is not required.

### 11.4. Evidence status

**Partially validated — the distinction is important, exact service rules require authoritative validation.**

The Parking work indicates that different pathways may have different identity, authority and reference requirements.

Exact rules for owner, nominated-driver, business, representative and other scenarios must be confirmed with authoritative service owners and relevant policy or statutory sources.

### 11.5. Open questions

> **At what point in each pathway does City of Melbourne genuinely need to know who the customer is, whether they have authority to act, and how strongly that must be verified?**

Additional questions include:

- Which interactions can remain anonymous?
- Which interactions require matter matching but not full authentication?
- Which actions require proof of authority rather than proof of identity alone?
- Can authentication occur only when the customer commits to an action?
- What information can be reused once identity or authority has been established?
- How should representatives, organisations or nominated drivers be handled?
- What controls are required for privacy, records, security and statutory compliance?

---

### 11.6. Identity requirement 1 — do not authenticate before it adds value

**Working requirement**

> **The experience should allow customers to access general information, understand options and identify the appropriate pathway without authentication where the service does not require identity at that stage.**

**Evidence status:** Strong Design principle; exact exceptions require validation.

---

### 11.7. Identity requirement 2 — distinguish identity from authority

Knowing who a person is does not necessarily establish that they are entitled to act.

**Working requirement**

> **Where an action depends on authority, the experience should confirm the customer's authority to act separately from simply establishing identity.**

**Evidence status:** Strong working direction; authority rules require service validation.

---

### 11.8. Identity requirement 3 — use proportionate assurance

Different actions may carry different risks.

**Working requirement**

> **The level of identity or authentication assurance should be proportionate to the action, information being accessed and service risk rather than applying the highest level of assurance to every interaction.**

**Evidence status:** Design principle; risk thresholds require specialist validation.

---

### 11.9. Identity requirement 4 — make verification understandable

Customers should know why information is being requested.

**Working requirement**

> **When identity, authority or authentication is required, the experience should explain what is needed, why it is needed and what the customer can do if they cannot provide it through the standard method.**

**Evidence status:** Strong working direction.

---

### 11.10. Identity requirement 5 — avoid repeated verification where it is legitimately reusable

**Working requirement**

> **Where identity or authority has already been established and can legitimately be relied upon, the experience should avoid requiring the customer to repeat verification solely because they move between connected interactions.**

This depends on privacy, security, records, system and statutory constraints.

**Evidence status:** Working Design hypothesis.

---

### 11.11. What good looks like for Identity, authority & authentication

A connected Comply experience should allow a customer to say:

> **I can understand my options before being asked to identify myself unnecessarily.**  
> **When City of Melbourne asks who I am, I understand why.**  
> **If I need authority to act, that is explained clearly.**  
> **The level of verification feels proportionate to what I am trying to do.**  
> **I do not repeatedly prove the same thing without a legitimate reason.**

---

## 12. Requirement area 6 — Discovery & off-platform entry

### 12.1. Customer need

> **Help me find accurate, understandable information and the right next action wherever I begin — even if I start with Google, an AI-enabled search experience, an infringement notice or another external source.**

The customer journey does not necessarily begin on a City of Melbourne webpage.

The Intelligent Front Door therefore needs to consider both:

- the quality of City of Melbourne-owned information and pathways; and
- how well that information can be discovered, interpreted and represented through external discovery surfaces.

### 12.2. Service need

City of Melbourne needs authoritative customer information that is clear, structured and consistent enough to support reliable discovery across both owned and off-platform channels.

The design should help external discovery surfaces identify:

- what the service is about;
- which customer situations or intents it applies to;
- what options exist;
- which information is authoritative;
- what the next action is; and
- where the customer must return to City of Melbourne to complete a protected, authenticated or formal action.

City of Melbourne cannot control every external answer.

The design opportunity is to improve the quality and machine-readability of the authoritative source material external systems rely on.

### 12.3. Working design requirement

> **The connected experience should make authoritative City of Melbourne information discoverable and interpretable from common customer entry points, while providing a clear path back to the appropriate City of Melbourne-owned interaction when formal action, authentication or human support is required.**

### 12.4. Evidence status

**Working Design direction — linked to the Off-Platform Search workstream and requires active testing.**

Discovery and Define identified off-platform search and AI-enabled discovery as plausible customer entry points.

The extent to which different search and AI surfaces can reliably interpret current City of Melbourne content must be established through testing rather than assumed.

### 12.5. Open questions

> **What must be true of City of Melbourne's authoritative information so that a customer starting off-platform can understand the issue, receive safe guidance and reach the right owned pathway?**

Additional questions include:

- Which parking-infringement queries are most important to test?
- Which pages or knowledge sources should be authoritative?
- Can search and AI systems distinguish payment, review, nomination and information intents reliably?
- What information should be answerable off-platform versus requiring transition to an owned pathway?
- How should City of Melbourne signal authoritative, current and service-specific information?
- What content structures improve machine interpretation without degrading human readability?
- How will off-platform performance be monitored over time?

---

### 12.6. Discovery requirement 1 — optimise the authoritative source, not the external answer

**Working requirement**

> **City of Melbourne should maintain clear, current and structured authoritative source information so external search and AI systems have a reliable basis for interpreting the service.**

The design should not depend on controlling a third-party interface or generated answer.

**Evidence status:** Strong Design principle; specific content patterns to test.

---

### 12.7. Discovery requirement 2 — support customer-language entry

Customers may search using their own description of the situation rather than formal service terminology.

**Working requirement**

> **Authoritative information should make the relationship between common customer language, customer intent and the relevant City of Melbourne service or pathway sufficiently explicit for both people and machine-mediated discovery.**

**Evidence status:** Strong working direction.

---

### 12.8. Discovery requirement 3 — make the next action explicit

External discovery is useful only if the customer can determine what to do next.

**Working requirement**

> **Authoritative information should clearly identify the legitimate next actions and provide an unambiguous route to the relevant City of Melbourne-owned pathway where action is required.**

**Evidence status:** Strong working direction.

---

### 12.9. Discovery requirement 4 — distinguish information from formal action

Some information can be safely understood off-platform.

Payment, nomination, review submission, identity verification and other formal actions may need to occur in controlled City of Melbourne pathways.

**Working requirement**

> **The experience should make clear when information can be consumed off-platform and when the customer must transition to an owned City of Melbourne interaction to act, authenticate or obtain appropriate support.**

**Evidence status:** Strong working direction; exact boundaries require service validation.

---

### 12.10. Discovery requirement 5 — design for human and machine readability together

**Working requirement**

> **Customer-facing information should use clear structure, terminology and relationships that improve machine interpretation without creating a separate or degraded experience for human readers.**

This connects IFD Design to the Off-Platform Search AI-readability work without making AI optimisation a separate customer experience.

**Evidence status:** Working hypothesis to test.

---

### 12.11. Discovery requirement 6 — monitor external interpretation rather than assume it remains correct

External search and AI behaviour can change independently of City of Melbourne.

**Working requirement**

> **The future operating model should include a lightweight way to test whether priority customer intents continue to be represented accurately through important off-platform discovery surfaces.**

This is a monitoring requirement, not a commitment to control third-party outputs.

**Evidence status:** Working Design direction.

---

### 12.12. What good looks like for Discovery & off-platform entry

A connected Comply experience should allow a customer to say:

> **I can begin in the place I naturally search.**  
> **The information I find helps me understand what applies to my situation.**  
> **I can tell which City of Melbourne information is authoritative.**  
> **I know when I can keep reading and when I need to move into an official pathway.**  
> **The transition into City of Melbourne feels like a continuation of the same task.**

Better off-platform discovery creates value when customers reach accurate information and the appropriate City of Melbourne interaction earlier, reducing unnecessary searching, misdirection and avoidable contact.

---

## 13. Evidence discipline

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

## 14. Current scope

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

## 15. Design principles

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

## 16. Current Design sequence

The current working sequence is:

1. **Problem** — established through Define.
2. **Context** — identify customer circumstances, operational context and service constraints.
3. **Requirement areas** — define what a connected experience needs to enable.
4. **Detailed requirements** — develop each requirement area from evidence.
5. **Future-state concepts** — explore multiple responses without prematurely selecting technology.
6. **Prototype and test** — test usefulness, clarity, fairness, feasibility and reusability.
7. **Decision** — determine what is strong enough to progress into Deliver.

### Requirement-set status

The six initial Design requirement areas are now documented:

1. Information & knowledge
2. Intent & routing
3. Context & continuity
4. Support & escalation
5. Identity, authority & authentication
6. Discovery & off-platform entry

These remain working Design requirements rather than approved business or technical requirements.

### Next Design task

**Agree the Design approach with the core stakeholder group.**

The current Design brief provides the starting point for that conversation.

The immediate task is not to select a future-state concept or technology. It is to validate the brief, confirm the most important questions to answer, and agree the most useful Design activities for the next three weeks.

---

## 17. Design phase planning and stakeholder validation

### 17.1. Planning intent

The current IFD Design page will act as the **Design brief and phase anchor**.

Over the next three weeks, the brief will be reviewed and refined with the core stakeholder group:

- Gavin;
- Tom;
- Jasmine;
- Margot; and
- Dennis.

The purpose of the validation period is to ensure that the Design phase is shaped by the people who understand the customer experience, service reality, operational constraints and wider design context.

The Design method should therefore **not be fixed in advance**.

The approach will be agreed with stakeholders based on:

- which parts of the brief they confirm or challenge;
- which evidence gaps matter most;
- which service constraints require deeper validation;
- which capabilities need specialist input;
- what can realistically be tested within the available time; and
- what decision the Design phase needs to support next.

---

### 17.2. Three-week planning window

The three-week period should be treated as a structured validation and planning window rather than a predetermined workshop sequence.

| Period | Primary purpose | Expected outcome |
| --- | --- | --- |
| **Week 1 — Validate the brief** | Review the problem, HMW, So That, context and six requirement areas with the core stakeholder group | Confirm what is sound, what needs refinement, what remains uncertain and what must be tested |
| **Week 2 — Agree the Design approach** | Use stakeholder input to determine the most useful combination of design activities, participants and evidence | Agreed Design approach, priority questions, required contributors and practical sequence |
| **Week 3 — Prepare the Design work** | Close material gaps needed to begin the agreed approach and establish the first testable Design focus | Updated Design brief, visible assumptions and constraints, agreed first Design activity and clear next decision |

This sequence describes the **decision progression**, not mandatory meeting formats.

The work may use workshops, one-to-one conversations, service walkthroughs, journey mapping, concept sketching, prototyping, evidence review or asynchronous input depending on what stakeholders determine will provide the strongest evidence.

---

### 17.3. What stakeholders are being asked to validate

The brief should be used to test whether there is sufficient agreement on:

1. **The problem** — does the fragmented-to-connected framing describe a meaningful customer and service problem?
2. **The journey boundary** — is the parking-infringement journey the right container for the first Design iteration?
3. **The mode lens** — is Comply an appropriate primary lens, with Transact and Apply used where the interaction changes?
4. **The context** — are the current customer circumstances, operational considerations and constraints credible?
5. **The requirement areas** — do the six requirement areas capture what a connected experience needs to enable?
6. **The evidence gaps** — which assumptions or service rules need validation before concept work?
7. **The Design approach** — what is the smallest useful set of activities that will produce enough evidence to make the next decision?

Stakeholder review is intended to **improve the brief**, not merely approve it.

Material disagreement, missing evidence or service constraints should be recorded and used to adjust the Design approach.

---

### 17.4. Approach-selection principles

When choosing the Design approach, prioritise:

| Principle | Planning implication |
| --- | --- |
| **Decision first** | Start with the decision or uncertainty the activity needs to resolve |
| **Use the smallest useful test** | Do not run a workshop, prototype or research activity unless it changes what we can decide |
| **Match method to uncertainty** | Use service-owner validation for service rules, customer evidence for customer needs, and design exploration for future-state interaction questions |
| **Keep the journey connected** | Avoid splitting the work back into isolated channel improvements |
| **Preserve evidence status** | Keep confirmed evidence, hypotheses and open questions visibly separate |
| **Human support stays in scope** | Include assisted and specialist support when exploring the future state |
| **Technology remains open** | Select technology only after the interaction need is sufficiently understood |
| **Design for reuse** | Capture patterns that could contribute to the Connected Interactions Framework beyond Parking |

---

### 17.5. Candidate Design activities

The following are **options to choose from with stakeholders**, not a committed delivery plan:

- validate the current journey and service constraints with service and operational stakeholders;
- walk priority customer circumstances through the six requirement areas;
- identify which moments in the journey require different information, routing, continuity or support;
- map the transition between Comply, Transact and Apply;
- define the minimum connected context required at key handoffs;
- test where identity, authority or authentication genuinely becomes necessary;
- examine where off-platform discovery should connect into owned pathways;
- develop multiple future-state interaction concepts;
- prototype only the moments needed to test the most important assumptions;
- test concepts with relevant customer, frontline and service perspectives; and
- identify reusable patterns for the Connected Interactions Framework.

The selected activities should remain proportionate to the evidence needed for the next decision.

---

### 17.6. Evidence and decision capture

The **IFD - Design README remains the anchor** for the phase.

Do not create additional Design pages simply to record activity.

Update this page when stakeholder work materially changes:

- the problem or journey boundary;
- a requirement;
- an evidence status;
- a confirmed service constraint;
- a Design principle;
- the agreed Design approach; or
- the next decision.

Use the existing project Decision Log for material project decisions and the existing RAID mechanisms for risks, assumptions, issues or dependencies where those need project-level visibility.

Working notes, meeting records and exploratory artefacts can remain in their appropriate working locations rather than being duplicated into the phase anchor.

---

### 17.7. End-of-window planning outcome

At the end of the three-week validation period, the project should be able to state:

> **We have a sufficiently validated Design brief, we know which uncertainties matter most, and stakeholders have agreed the most useful approach for turning the brief into a testable future-state concept.**

The expected planning outputs are:

- a validated or explicitly revised problem, HMW and So That;
- a validated or refined set of Design requirement areas;
- confirmed service constraints and clearly labelled remaining assumptions;
- an agreed Design method and participant mix;
- an agreed first future-state Design focus;
- clear evidence or test questions;
- a practical next sequence; and
- the next decision the Design work needs to support.

The objective is not to complete the future-state design within the planning window unless stakeholder validation shows that the evidence is already sufficient.

The objective is to enter the next Design activity with a **shared problem, shared constraints and a deliberate method**.

---

## 18. Design exit criteria

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

## 19. Final Design outcome

By the end of Design, the team should have a practical and testable future-state approach for the first Intelligent Front Door use case.

Most importantly, the team should be able to answer:

> **Does this connected experience materially improve how customers understand, navigate and resolve their situation while also reducing avoidable service effort and preserving appropriate human support?**

If the answer is yes, the work can progress toward Deliver.

If the answer is partial or no, the specific design, evidence or service constraint should be identified before further investment.
