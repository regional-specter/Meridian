# Meridian

**Sovereign-Grade Agentic OS for UAE Energy**

Meridian is a next-generation agentic intelligence operating system, architected for national energy sovereignty in the UAE. It implements a full-stack, continuously cycling OODA (Observe, Orient, Decide, Act) loop to optimize production, logistics, pricing, and strategy—specifically designed for the UAE’s new post-OPEC reality.

---

## The Opportunity

On May 1, 2026, the UAE exited OPEC after 59 years, becoming a fully independent oil producer. This historic event enables the UAE to make sovereign decisions on production, pricing, routing, and capital—all at machine speed and without external negotiation. Meridian is built to turn this structural opportunity into sustainable national advantage.

---

## 📚 Research & Theoretical Foundations

This project is the result of an intensive 5-day research sprint into **Agentic AI**, **Decision Intelligence**, and **Energy Sovereignty**. The implementation transforms theoretical frameworks—specifically John Boyd's OODA Loop—into a functional multi-agent system tailored for the modern energy landscape.

---

### 🧠 Phase 1: The OODA Foundation
*Developing the core cognitive architecture for the system.*

* **John Boyd** — *"Destruction and Creation" (1976)*: The primary theoretical paper on mental models.
* **John Boyd** — *"A Discourse on Winning and Losing"*: Original briefing slides via Air University.
* **SwissUniversity.com (April 2026)** — *"From Fast Cycles to Intelligent Advantage"*: Reframing OODA for Agentic AI.
* **F5 (2025)** — *"AI and the OODA Loop: Reimagining Operations"*.
* **JAPCC (2022)** — *"Speeding Up the OODA Loop with AI"*.

### 🤖 Phase 2: Multi-Agent Systems (MAS) & Agentic OS
*Technical frameworks for autonomous reasoning and tool use.*

* **Wang et al.** — *"A Survey on LLM-based Autonomous Agents"* (arXiv:2308.11432).
* **Yao et al.** — *"ReAct: Synergizing Reasoning and Acting in LLMs"* (arXiv:2210.03629).
* **Microsoft Research** — *"AutoGen: Enabling Next-Gen LLM Applications"* (arXiv:2308.08155).
* **Schick et al.** — *"Toolformer: Language Models Can Teach Themselves to Use Tools"*.
* **VIGIL (2026)** — *"Towards Edge-Extended Agentic AI for Enterprise IT Support"* (arXiv:2603.16110).

### 🛢️ Phase 3: Energy Domain & Industrial AI
*Contextualizing AI within the upstream and downstream oil & gas sector.*

* **Koroteev & Tekic** — *"AI in Oil and Gas Upstream: Trends and Challenges"* (ScienceDirect 2021).
* **CrudeCast (2025)** — *"Agentic AI Systems' Potential in Upstream Oil & Gas"*.
* **XenonStack (2026)** — *"Re-Imagining the Oil and Gas Industry with Agentic AI"*.
* **AIQ ENERGYai** — Technical documentation and ADIPEC published materials.
* **ADNOC Panorama** — Command Center case studies (GITEX/ADIPEC white papers).

### 📈 Phase 4: Decision Intelligence & Uncertainty
*Designing for feedback loops, noise filtering, and predictive accuracy.*

* **Lorien Pratt** — *"Decision Intelligence: An AI Approach to Business Decision Making"*.
* **Donella Meadows** — *"Thinking in Systems"*: Critical for designing system feedback loops.
* **Nate Silver** — *"The Signal and the Noise"*: Applied to the **Observe** layer of the OODA loop.
* **Glasserman** — *"Monte Carlo Methods in Financial Engineering"*: For scenario simulation modules.
* **Tetlock & Gardner** — *"Superforecasting"*: Methods for quantitative prediction accuracy.

### ⚖️ Phase 5: Governance & Sovereign AI
*Ensuring explainability and alignment in industrial applications.*

* **Vaswani et al.** — *"Attention Is All You Need"*: The foundational Transformer architecture.
* **Anthropic (2022)** — *"Constitutional AI: Harmlessness from AI Feedback"*.
* **Zhao et al.** — *"Explainability for LLMs: A Survey"* (arXiv:2309.01029).
* **IEA (2024)** — *"Responsible AI in the Energy Sector"*.
* **Grieves (2022)** — *"Digital Twins for Industrial Applications"*.

---

### 🇦🇪 Contextual Layer: UAE Geopolitical Strategy
The project specifically addresses the technical requirements of an independent energy strategy following the **UAE's exit from OPEC in April 2026**. 

* **Market Impact:** Analyzed through reports from *Al Jazeera*, *The National*, and *The Conversation* regarding the "No More Quotas" era.
* **Technical Modernization:** Grounded in the **SLB and AIQ (2025)** deployment of Agentic AI across ADNOC’s subsurface operations and the **EnkiAI** report on ADNOC’s 2025 AI revolution.

## System Architecture Overview

Meridian’s design is structured as a four-layer OODA loop, continuously cycling with each layer feeding the next and outcomes feeding back to Observe.

```
┌─────────────────────────────────────────────────────────────┐
│                     OBSERVE LAYER                           │
│  Signal ingestion · Markets · Geopolitical · Field data ... │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      ORIENT LAYER                           │
│  Multi-agent intelligence fusion · 7 specialist agents      │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      DECIDE LAYER                           │
│  Monte Carlo scenario engine · Simulation & ranking         │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                       ACT LAYER                             │
│  Physical + commercial + strategic execution & feedback     │
└───────────────────────┬─────────────────────────────────────┘
                        │ outcome telemetry → back to Observe
                        └──────────────────────────────────────
```
**Full OODA cycle target: under 30 minutes.**

## System Architecture Overview

### Layer 1: Observe

<img src="https://github.com/user-attachments/assets/5768499b-2391-4083-9141-2892ef09ac8d" align="right" width="400" hspace="20" alt="Layer 1 Observe">

**Description:** This layer acts as the high-speed sensory intake or "nervous system" of the platform. It is designed to ingest and normalize a massive volume of disparate data streams, capturing raw "signals" from both the global energy landscape and local field operations. By processing these inputs with a sub-5 second latency, the system ensures that the subsequent layers are operating on the most current reality possible.

* **Diverse Signal Ingestion:** The layer captures and normalizes specialized data types including Industrial IoT/SCADA (sensor data from ADNOC pipelines), Market Data (Brent, Murban, WTI), Satellite Intelligence (AIS vessel tracking in the Strait of Hormuz), and Digital Intelligence (OSINT and news wires).
* **Canonical Normalization:** To ensure interoperability, the system converts vastly different data formats—such as a geopolitical tweet versus a high-pressure reservoir sensor—into a unified, queryable schema.
* **Infrastructure & Denoising:** Powered by Apache Kafka for high-volume streaming, the layer includes "Signal Denoising" to filter out market volatility and "Anomaly Detection" to trigger instant alerts for sensor failures or unexpected geopolitical shifts.

<br clear="right"/>

---

### Layer 2: Orient

<img src="https://github.com/user-attachments/assets/9f3d1505-aa28-4167-a79b-975af1aa8272" align="right" width="400" hspace="20" alt="Layer 2 Orient">

**Description:** The "Orient" layer is the cognitive core where multi-agent fusion occurs. It transforms the normalized data into an interpretable market structure. By contextualizing real-time signals against 70 years of historical data, it builds a "living mental model" of the world, allowing the system to understand not just what is happening, but why it matters in a historical and strategic context.

* **Multi-Agent Reasoning:** Seven specialist agents (Market, Geopolitical, Reservoir, Logistics, etc.) analyze the world from their specific domain perspectives. This allows for specialized deep-dives into topics like Hormuz risk indices or peak demand curves.
* **Intelligence Fusion & World-State Synthesis:** The system resolves conflicting signals—for example, reconciling high field pressure with low market demand—to update a central vector representing the current "state" of the global energy market.
* **Proprietary Knowledge Base:** Utilizes RAG (Retrieval-Augmented Generation) to access decades of ADNOC-specific seismic reports and historical data, assigning a "Confidence Weighting" score to the accuracy of the current world model.

<br clear="right"/>

---

### Layer 3: Decide

**Description:** This is the simulation layer where the "World-State" is stress-tested against thousands of potential futures to turn beliefs into intent. It serves as a bridge between intelligence and action, providing a human-in-the-loop interface for high-level strategic oversight while automating complex computational trade-offs.

* **Monte Carlo Simulation Engine:** To determine the optimal path, the engine runs over 10,000 "What-if" scenarios per 30-minute cycle. This tests responses to critical events found in Scenario Libraries, such as price wars or regional ceasefires.
* **Strategic Optimization:** The system calculates the best mix of production volume, pricing, and routing to maximize sovereign interest. Each recommendation includes an "Audit Trail" to provide full explainability for human leadership.
* **Autonomy Gating:** Decisions are automatically routed based on confidence levels. High-confidence actions can be set to autonomous execution, while lower-confidence or high-impact scenarios are escalated for executive approval via "Executive Directives."

---

### Layer 4: Act

**Description:** The final execution layer converts digital directives into physical reality, commercial orders, and strategic communications. It closes the loop of the OODA cycle by monitoring the immediate outcome of every action and feeding that telemetry back into the Observe layer for the next iteration.

* **Physical & Commercial Execution:** The system interfaces directly with "RoboWell" to adjust field-level wellheads and flow rates. Simultaneously, it executes spot market trades and manages hedging instruments through commercial placement platforms.
* **Logistics Orchestration:** Beyond the field, the system dynamically reroutes tankers and optimizes port berth schedules at hubs like Fujairah to ensure the supply chain remains fluid and responsive to market shifts.
* **Loop Closure & Speed Moat:** By targeting a full cycle completion in under 30 minutes, the system maintains a competitive "speed moat," allowing the organization to react to global shifts faster than traditional market participants.


### Key Features

- Real-time multi-source signal ingestion (market, geopolitical, field, demand, competition, ESG)
- Multi-agent world modeling (Reservoir, Market, Geopolitical, Demand, Logistics, Competitor, Master Orchestrator)
- Decision-making via simulation, with confidence gating and explainable audit trail
- Autonomous execution across physical systems, commercial flows, and strategic levers
- Continuous loop closure: outcome telemetry triggers re-observation and re-orientation
- Built for sub-5s latency, regulatory compliance, UAE sovereign security standards

---

## Differentiators

- **Speed Asymmetry:** Full OODA cycle in under 30 minutes—weeks faster than collective decision processes.
- **Sovereignty:** No external quotas, total independent optimization.
- **Explainability:** Every decision is fully auditable and regulator-ready.
- **Integration:** Orchestrates existing AI/ML tools (e.g., ENERGYai, RoboWell, Emission X, Panorama), serving as the national intelligence backbone.

---

## Ambition

Meridian is not just another AI tool—it is an operating system for national energy sovereignty. The system’s architecture fuses cutting-edge agentic AI, sovereign-grade security, and domain-specific expertise to redefine how a nation runs its energy sector in the age of rapid demand shifts and geopolitical uncertainty.

---

## Getting Started

*Meridian is in research & architecture phase. For the latest project file and technical schematics, see:*
- [`uae-oil-ooda-project.md`](uae-oil-ooda-project.md)

---

*Architecture: OODA Sovereign Energy Intelligence OS*  
*Context: UAE OPEC exit, Hormuz closure, post-ADNOC AI programme*
