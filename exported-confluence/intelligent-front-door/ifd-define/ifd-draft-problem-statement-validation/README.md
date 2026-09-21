---
title: "IFD-Draft Problem Statement Validation"
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

# IFD-Draft Problem Statement Validation

## 1.1. Purpose

This page brings the current Intelligent Front Door problem statement into **Define** for stakeholder review and validation.

The intent is not to approve a solution or technical architecture.

The purpose of this playback is to test whether we have:

- framed the right customer problem;
- understood where the problem occurs;
- set an appropriate initial boundary for the Intelligent Front Door;
- identified the right questions to take forward into Design; and
- selected a useful set of Parking scenarios through which to test the proposition.

The output of stakeholder validation will be a refined problem statement and clearer Define direction.

---

## 1.2. Where we are

Discovery has moved the Intelligent Front Door away from a generic concept of creating a new "front door".

The emerging opportunity is more specific:

> Help customers recognise what they are trying to do, understand what they need, and enter the right existing service pathway with an appropriate level of support.

Parking is being used as the first practical lens because it contains several different customer intents and interaction patterns within one service domain.

This allows us to test whether a common front-door approach could work across different situations without assuming that every journey should behave in the same way.

---

# 2. Draft problem statement

> **Customers can struggle to recognise and navigate the right parking or infringement pathway because services are not always presented around the task they are trying to complete.**
>
> This can create avoidable search, navigation and support effort, particularly when customers need to understand eligibility, evidence, next steps, status or which level of support applies.
>
> **The Intelligent Front Door should help customers identify their intent, understand what they need to know, and enter the right existing pathway with the appropriate level of support and authentication — without redesigning the underlying business process in the initial phase.**

### 2.1.1. Validation status

**Draft — stakeholder validation required**

This statement is intended to provide a shared starting point for Define. It should change if stakeholder knowledge or further evidence shows that we have framed the problem incorrectly.

---

# 3. The customer problem we are trying to solve

The working hypothesis is that some customer effort occurs **before the underlying service transaction has really begun**.

Customers first need to work out:

1. what they are actually trying to do;
2. which City of Melbourne service or pathway relates to that need;
3. what applies to their situation;
4. what information or evidence they need;
5. whether they need to identify themselves;
6. whether they can continue independently or need additional support; and
7. where they should go next.

When these questions are difficult to resolve, customers may need to search, interpret organisational language, move between channels or seek staff assistance simply to find the correct starting point.

The Intelligent Front Door opportunity is therefore not just about providing another entry point.

It is about improving the **decision-making that happens before pathway entry**.

---

# 4. Define question

> **How might we help customers recognise and navigate the right parking or infringement task, understand what is required, and enter the appropriate existing pathway with the right information, support and authentication?**

This question deliberately keeps the solution open.

It does not assume:

- a chatbot;
- a new portal;
- a single digital interface;
- a new authentication platform; or
- replacement of existing service systems.

---

# 5. Proposed initial scope

For the initial phase, the Intelligent Front Door would focus on:

### 5.1.1. Findability

Help the customer recognise where their need belongs.

### 5.1.2. Intent

Understand what the customer is trying to achieve rather than requiring them to understand City of Melbourne's internal service structure.

### 5.1.3. Understanding

Provide the minimum information required for the customer to make the next decision confidently.

### 5.1.4. Routing

Direct the customer into the appropriate existing service pathway.

### 5.1.5. Support

Recognise when the customer can proceed independently and when additional guidance or human support may be required.

### 5.1.6. Authentication

Ask the customer to identify or authenticate themselves only when the task or existing service requires it.

---

# 6. What is not being proposed at this stage

The initial Intelligent Front Door work is **not** intended to:

- redesign underlying business processes;
- change service rules or policy;
- redesign back-office workflows;
- determine detailed technical architecture;
- define a final authentication solution; or
- replace existing service delivery platforms.

Those opportunities may emerge later, but they should not be assumed as requirements of the initial Define work.

The immediate question is:

> **Can we make it easier for customers to understand and enter the services we already provide?**

---

# 7. A different way of thinking about the front door

Today, services can naturally be organised around organisational structures, service offerings, webpages, forms and systems.

Customers do not necessarily begin there.

They begin with an intent:

> "I need a parking permit."

> "Someone else was driving."

> "I think this fine is wrong."

> "There is a car blocking something."

> "Can I park here?"

The emerging Intelligent Front Door model therefore introduces a customer-intent layer in front of existing service pathways.

### 7.1.1. Working model

**Service Area → Service → Service Offering → Customer Intent / Contact Reason → Interaction Mode → Information Need → Support Need → Authentication Need → Existing Pathway**

The formal service catalogue remains important.

The proposition is that customers should not need to understand that catalogue before they can successfully use it.

---

# 8. Information is required across the experience

One important Define principle is that **information need is not a separate interaction type**.

Customers need information while they:

- apply;
- comply;
- report an issue;
- transact;
- access a service;
- have a say; or
- take part.

Across these interactions they may need to know:

- what applies to them;
- what they need before starting;
- what happens next;
- what evidence is required;
- what happens after submission;
- status or progress where relevant; and
- where to get help.

This means information should be treated as a capability that supports multiple customer journeys rather than as a separate destination customers must find.

---

# 9. Parking as the first validation lens

The current working set of Parking intents is:

1. **Apply for or manage a parking permit**
2. **Request a review of a fine**
3. **Nominate another driver**
4. **Report a parking issue**
5. **Find parking information / understand rules**
6. **General parking enquiry**

These scenarios deliberately contain different levels of complexity, information, support and authentication.

They allow us to test whether one common Intelligent Front Door model can recognise different customer needs and then adapt the pathway accordingly.

---

# 10. What the first use cases are showing us

## 10.1. Parking permits

The front door may need to:

**Identify intent → distinguish the permit task → clarify eligibility or permit type where necessary → provide minimum information → route to the existing permit pathway**

Potential support pattern:

**Routine → Guided**

Key question:

> At what point does City of Melbourne genuinely need to know who this customer is in order for the permit task to progress?

---

## 10.2. Infringement review

The front door may need to:

**Understand the customer's intended action → distinguish review from payment, nomination, information or complaint → explain requirements → enter the existing review pathway → escalate complex circumstances where appropriate**

Potential support pattern:

**Guided → Assisted**

Key question:

> What does City of Melbourne need to confirm about the infringement and the person acting before the review pathway can safely proceed?

---

## 10.3. Driver nomination

The front door may need to:

**Recognise responsibility-transfer intent → distinguish nomination from disputing the fine → explain requirements → confirm necessary information or authority → route into the existing nomination pathway**

Potential support pattern:

**Routine → Guided**

Emerging principle:

> **Intent disambiguation before pathway selection.**

---

## 10.4. Reporting a parking issue

The front door may need to:

**Classify the issue → determine City of Melbourne responsibility → determine urgency → capture minimum routing information → enter the existing Parking Enforcement pathway**

Potential support pattern:

**Routine → Guided**

Emerging pattern:

> **Classify issue → determine responsibility → determine urgency → route.**

---

# 11. Emerging proposition

The Intelligent Front Door may not need to create one universal customer journey.

Instead, it could provide a reusable decision layer that asks only enough questions to determine:

**What is the customer trying to do?**

↓

**What do they need to understand?**

↓

**Which pathway applies?**

↓

**How much support is required?**

↓

**Is authentication actually required yet?**

↓

**Enter the existing service pathway**

The value would come from making this logic consistent and reusable across services while allowing individual service pathways to retain their necessary rules and processes.

This is a proposition to test, not yet a confirmed design.

---

# 12. What we need stakeholders to validate

During the playback, we want to test five things.

### 12.1.1. Problem

**Does this describe a real and meaningful customer problem?**

What is missing, overstated or incorrectly framed?

### 12.1.2. Boundary

**Is improving findability, understanding and routing into existing pathways a useful initial boundary?**

Are we excluding something essential?

### 12.1.3. Service reality

**Does the proposed logic reflect how these Parking services actually work?**

Where does the model oversimplify the service?

### 12.1.4. Support and authentication

**Are we asking for customer information, authentication or staff intervention at the right points?**

Where are there policy, operational, privacy or risk requirements we have not yet captured?

### 12.1.5. Transferability

**If this worked for Parking, does the underlying model appear reusable for other City of Melbourne services?**

What would need to remain service-specific?

---

# 13. Specific questions still open

The following items require further validation:

- exact Service Offering alignment for driver nomination;
- authoritative sources for Parking knowledge and service information;
- authentication requirements for individual pathways;
- mandatory identity or authority checks;
- where anonymous or low-authentication interactions are appropriate;
- existing status and follow-up capabilities;
- common customer abandonment or failure points;
- criteria for moving from Guided to Assisted support;
- customer language that best represents current service offerings; and
- whether some customer intents should be combined or separated.

These should remain visible as open questions rather than being treated as confirmed requirements.

---

# 14. Decision sought from this playback

The immediate decision is **not approval of an Intelligent Front Door solution**.

We are seeking stakeholder agreement on whether:

> **This is the right problem and a useful boundary to take forward into Design.**

Following validation, we should be able to:

- refine the problem statement;
- confirm or adjust the Parking use cases;
- identify incorrect assumptions;
- confirm important operational constraints;
- prioritise remaining evidence gaps; and
- move into Design with a clearer problem and testable service logic.

---

# 15. Rovo presentation brief

Create a concise stakeholder playback presentation from this page.

The presentation should help a mixed operational, CX, service design and decision-making audience understand and challenge the proposed Define direction.

Use approximately **8–10 slides**.

Suggested story:

1. **Why we are here** — Discovery has moved us from a broad Intelligent Front Door concept to a specific problem to validate.
2. **The draft problem** — present the problem statement clearly.
3. **Where customer effort occurs** — show the decisions customers need to make before entering a service pathway.
4. **What we are proposing to focus on** — findability, intent, understanding, routing, support and authentication.
5. **What we are not proposing** — make the initial scope boundary explicit.
6. **The emerging front-door model** — show customer intent connecting to existing City of Melbourne services and pathways.
7. **Parking as the test case** — show the six priority customer intents.
8. **What the use cases are teaching us** — illustrate the different routing patterns using 2–4 examples.
9. **What remains uncertain** — highlight assumptions and open questions.
10. **What we need from stakeholders** — validate the problem, boundary, service reality, support/authentication logic and transferability.

Presentation principles:

- one clear message per slide;
- prioritise diagrams and simple flows over dense text;
- clearly distinguish **confirmed current understanding**, **working hypothesis** and **open question**;
- avoid presenting the Intelligent Front Door as a predetermined technology solution;
- keep the existing service pathways visible;
- use Parking examples to make the concept tangible;
- finish with the stakeholder validation questions rather than a solution recommendation.
