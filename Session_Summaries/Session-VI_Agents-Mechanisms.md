# Agents Mechanisms - Understanding Agentic AI

**📅 Date & Time:** November 14, 2026 at 17:00 (5:00 PM)  
**👨‍🏫 Presenter:** Alan Al Jammoor 
**🎯 Session Type:** Live Demonstration + Interactive Problem Solving 

* * *

## Overview

This foundational session explores the core mechanics of AI agents: how they differ from traditional LLMs, the anatomy of an agentic loop, the concept of tools, and planning strategies. Alan emphasizes that understanding these mechanisms is critical before attempting to build with agents. This is a deep conceptual session laying groundwork for the practical session tomorrow.

* * *
## Slides and Presentation

The first session, Alan presented a well-informative manner of how Agents works. All the slides presented in class can be access at:

[Deck](../materials/deck-Alan-Al-Jammoor.pdf){.btn .btn-primary target="_blank"}


[How Agent Works](../materials/agent-step-by-step.html){.btn .btn-primary target="_blank"}

[Agents at Work](../materials/agent-at-work-Alan-Al-Jammoor.html){.btn .btn-primary target="_blank"}


## Reading List

Alan gave us a very informative reading list! Keep your reading list full and slowly digest these contents.

[Reading List](../materials/reading-list-Alan-Al-Jammoor.html){.btn .btn-primary target="_blank"}


## Key Learning Outcomes

1. **Understand Five Levels of AI Configuration** - Identify when agents are truly needed
2. **Master the Agentic Loop** - Understand how agents think, plan, and execute
3. **Recognize Tool Capabilities** - Know what enables agent action
4. **Grasp Planning Patterns** - Learn how agents break down complex problems
5. **Apply Cost-Benefit Analysis** - Know when agents are overkill

* * *

## Main Topics Covered

### 1. **Five Levels of AI Configuration**

Alan introduces a framework for understanding different AI capabilities:

#### **Level 1: Naked LLM** (2022-2023)
- **Example:** ChatGPT interface on web
- **Capability:** Text input for Text output
- **Limitation:** No external tools, often gives outdated information
- **Use Case:** Creative writing, brainstorming, explanations
- **Cost:** Cheapest
- **Latency:** Fastest
- **Complexity:** Simplest

**Example in Work:**
- "Polish this email draft" → LLM rewrites it → Done

* * *

#### **Level 2: Augmented LLM** (2023-2024)

- **Definition:** LLM with access to 1-3 tools (search, files, memory)
- **Capability:** Can access external information or perform limited actions
- **Limitation:** Still requires human orchestration of steps
- **Use Case:** Answering current-events questions, accessing company documents

**Example in Work:**
- Q: "What time is the last bus?" 
- LLM: "I don't know, let me check the bus schedule [tool] → 8:45 PM"
- You still coordinate what comes next

* * *

#### **Level 3: Workflow** (Multi-step, pre-planned)
- **Definition:** Multiple AI steps connected in sequence; steps are pre-defined
- **Capability:** "Every Monday, summarize feedback → sort by topic → draft report"
- **Automation Level:** Repeats same steps automatically
- **Limitation:** If something unexpected happens, it fails; no adaptation
- **Use Case:** Scheduled, repetitive processes

**Example in Work:**
- Monday morning → AI runs same process → Report auto-generated
- BUT: If feedback format changes, process breaks

* * *

#### **Level 4: Agent** (Adaptive decision-making loop)
- **Definition:** LLM + Tools + Memory + Loop that decides its own next steps
- **Key Innovation:** **AI decides the steps, not humans**
- **Capability:** "Book a room for 30 people Thursday, adapt if usual room is full"
- **Automation Level:** High—AI plans and executes in real-time
- **Adaptability:** Handles unexpected situations
- **Use Case:** Complex, unpredictable tasks

**Example in Work:**
- "Book a room" → AI plans steps → Checks availability → Finds usual room full → Automatically books alternative → Success

* * *

#### **Level 5: Multi-Agent** (Team of specialized agents)
- **Definition:** Multiple agents with different roles working toward same goal
- **Example:** Researcher Agent + Writer Agent + Fact-Checker Agent
- **Why Multiple Agents?** Context isolation—prevents bias and errors
- **Use Case:** Complex projects needing specialized expertise
- **Example Benefit:** 
  - If Researcher verifies own work, bias creeps in
  - Separate Fact-Checker agent catches errors Researcher missed

**Example in Work:**
- Task: "Produce one market research report"
- Researcher Agent: Collects data, synthesizes findings
- Writer Agent: Formats into professional document
- Fact-Checker Agent: Verifies 3 random statistics against original sources

* * *

### 2. **The Critical Decision: Which Level Do You Need?**

**Anti-Pattern: Over-engineering**

Many people jump to agents when simpler solutions suffice:

| Task | Appropriate Level | Why Not Agent? |
|------|------------------|----------------|
| Translate English → French | LLM | No loop needed, deterministic task |
| Answer questions from PDF | Augmented LLM | Just need file access + search |
| Weekly report from sign-up sheet | Workflow | Same steps every time, no adaptation |
| Book room for 30 (adapt if full) | **Agent** | Need adaptive decision-making |
| Write 20-page research with QA | **Multi-Agent** | Need separation of concerns |

**Cost Impact:**
- Each loop iteration costs tokens (plan + action + observe + repeat)
- Translation with Agent = ❌ Bankrupt in days (overkill cost)
- Translation with LLM = ✅ Pennies (simple + efficient)

**Rule:** Use simplest tool that solves the problem. Beyond that = diminishing returns.

* * *

### 3. **What Makes an Agent Different: The Agentic Loop**

#### **The Three Core Components:**

```
┌─────────────────────────────────────┐
│   Agentic Loop Components           │
├─────────────────────────────────────┤
│ 1. PLAN: Agent decides next step    │
│ 2. ACT: Agent uses a tool           │
│ 3. OBSERVE: Agent reads result      │
│ → REPEAT until goal achieved        │
└─────────────────────────────────────┘
```

#### **Definition:**
> An agent is an AI that works toward a goal by deciding the next step, using a tool, reading the result, observing the outcome, and repeating until the goal is met.

#### **What This Enables:**
- **Autonomous Planning:** "I need to calculate X, divide by Y. I'll use a calculator."
- **Tool Selection:** "This needs math → calculator tool, not guessing"
- **Error Correction:** "Result doesn't look right → try different approach → loop again"
- **Goal Achievement:** Keeps looping until success or max attempts

* * *

### 4. **The Components of an Agent System**

An agent consists of multiple interacting parts:

```
                    ┌─────────────────┐
                    │  Large Language │
                    │  Model (Claude) │
                    │  (Thinking)     │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        v                    v                    v
  ┌──────────┐         ┌──────────┐         ┌──────────┐
  │  Tools   │         │ Memory   │         │   Loop   │
  │ (Calcs,  │         │(Project  │         │(Planning,│
  │  Search, │         │ Notes)   │         │ Acting,  │
  │  Code)   │         │          │         │Observing)│
  └──────────┘         └──────────┘         └──────────┘
```

#### **Tool:** Capability the AI can request
- Calculator (math)
- Web search (current info)
- Code execution (Python, JavaScript)
- File operations (read, write)
- MCP (Model Context Protocol) - extensions

#### **Memory:** Persistent context across iterations
- Project folder with `.md` files
- Notes tracking what's been done
- Decisions made and why
- Progress toward goal

#### **Loop:** The iterative process
- Plan what to do next
- Execute/request tool
- Read result back
- Adjust plan based on result
- Repeat

* * *

### 5. **Tools: How Agents Take Action**

#### **Definition:**
> A tool is an artifact or capability the AI can ask the computer to do for it.

#### **Why Tools Matter:**
- **LLM Limitation:** Cannot calculate 15% of 4,750 accurately (would guess)
- **With Calculator Tool:** Calculates exactly, returns to AI
- **Result:** AI reads answer, can build on it

#### **Tool Anatomy:**

```markdown
# Calculator Tool
- **Name:** calculator
- **Description:** "Do exact arithmetic when user asks for calculation"
- **Input:** Expression (e.g., "18% of 4750")
- **Output:** Numerical result (e.g., 855)
```

#### **Tools AI Can Request:**

| Tool Type | Example | Benefit |
|-----------|---------|---------|
| Calculator | 18% × 4,750 | Exact math (not guessing) |
| Code Runner | Execute Python script | Complex logic, data processing |
| Web Search | "Current weather in Bangkok" | Real-time, current data |
| File Access | Read project files | Context about project |
| Browser | Auto-browse web for info | Autonomous research |
| Email | Send notification | Autonomous communication |

* * *

### 6. **Practical Loop Example: School Trip Bus Calculation**

**Scenario:**
- 4,750 students going on trip
- 18% will take the bus
- Each bus holds 52 seats
- **Question:** How many buses needed?

#### **If LLM Guesses (No Tools):**
```
Human: "How many buses?"
LLM Output: "About 16 buses"
Result: ❌ WRONG (actual: 17)
```

#### **If LLM Uses Calculator Tool (Agentic):**

**Step 1: Plan**
```
LLM thinks: "I need 18% of 4,750. I should not guess math. I will use the calculator."
```

**Step 2: Act (Use Tool)**
```
LLM calls: calculator(18% of 4750)
Tool returns: 855
```

**Step 3: Observe**
```
LLM reads: "855 students will take the bus."
```

**Step 4: Plan Next**
```
LLM thinks: "Now I need 855 ÷ 52. Using calculator again."
```

**Step 5: Act (Use Tool Again)**
```
LLM calls: calculator(855 ÷ 52)
Tool returns: 16.44
```

**Step 6: Observe & Reason**
```
LLM reads: "16.44 buses. Can't have 0.44 buses. 16 would leave students behind."
LLM reasons: "Must round UP to 17."
```

**Step 7: Final Answer**
```
LLM: "Need 17 buses. 855 students. 17 buses × 52 seats = 884 seats total."
```

**Key Insight:** Each tool use loops back to LLM for interpretation, not just mechanical computation.

* * *

### 7. **Memory in Agents**

**Definition:** How agents remember context across iterations

#### **Two Types of Memory:**

1. **Context Window (Short-term)**
   - What fits in current LLM conversation
   - Lost when conversation ends
   - Limited by token count

2. **Project Memory (Long-term)**
   - Files in project folder (like `memory.md`)
   - Persists across sessions
   - Loaded into context when agent deploys

**Example Memory File:**
```markdown
# Project Progress Log

## Decision 1: Architecture
- Chose: Database + Backend + Frontend
- Why: Need to store user data
- Status: ✓ Decided

## Decision 2: Security
- Chose: OAuth2 + JWT tokens
- Why: Enterprise requirement
- Status: ✓ Implemented

## Errors Found & Fixed
- Bug 1: Password reset failing
  - Cause: Email not configured
  - Fix: Added SendGrid integration
  - Status: ✓ Fixed

## Next Steps
- [ ] Add two-factor authentication
- [ ] Scale database to multi-region
```

* * *

### 8. **Four Planning Patterns Agents Use**

Agents choose strategies based on problem type. Alan provides four named patterns:

#### **Pattern 1: Think Step-By-Step (Chain of Thought)**

**Problem:** Problems needing logical breakdown
**Example:** "On what date is the last Friday of a 30-day month starting on Tuesday?"

**AI Process:**
```
"Day 1 is Tuesday. 
Days 4, 11, 18, 25 are Fridays.
Day 32 would be next Friday but exceeds month.
Answer: 25th"
```

**vs. Guessing:**
```
"Probably the 30th" ❌ WRONG
```

**When Used:** Logical reasoning, math, multi-step decision

* * *

#### **Pattern 2: React (Reason → Act)**

**Problem:** Need information before deciding
**Example:** "Which rooms are free on Thursday at 10 AM for 30 people?"

**AI Process:**
```
1. Reason: "I need to know room availability. I'll search."
2. Act: Search tool → "Room A full, Room B available (35 seats), Room C (20 seats too small)"
3. Reason: "Room B is perfect. But it affects others. Should ask user first."
4. Act: Ask human → "Should I book Room B?"
5. Act: User approves
6. Act: Book Room B
```

**Key:** Intervene when outcome has human implications

* * *

#### **Pattern 3: Plan-Execute (To-Do List)**

**Problem:** Many tasks; need to track completion
**Example:** "Analyze cafe sales over 3 months, decide on menu changes"

**AI Process:**
```
To-Do:
1. ☑ Read sales file
2. ☑ Check if data is clean
3. ☑ Note: Data is messy; will clean first
4. ☑ Run cleaning process
5. ☑ Calculate sales per product
6. ☑ Analyze findings
7. ☑ Compare to business rules
8. ☑ Check every number against source
9. ☑ Write recommendation
```

**Key:** Ensures nothing is forgotten; accountability trail

* * *

#### **Pattern 4: Check & Fix (Iterative Refinement)**

**Problem:** First draft has mistakes; need verification
**Example:** "Create a report with verified numbers"

**AI Process:**
```
1. Create initial draft
2. Check: "Report says cappuccino earned $11,047"
3. Verify: Look at source data
4. Find: Source says $11,407 (2 digits swapped)
5. Fix: Correct the number
6. Output: Verified report
```

**Key:** Catches errors before output; quality gate

* * *

### 9. **Who Decides Which Pattern?**

**Question:** When does AI use which pattern?

**Answer:** Depends on problem. AI reasons about which pattern to use:

**Decision Framework:**
- **Problem needs logical breakdown?** → Think Step-By-Step
- **Missing information or external action needed?** → React (Reason → Act)
- **Multiple tasks to track?** → Plan-Execute (To-Do)
- **Accuracy critical or risk of errors?** → Check & Fix

**You Can Override:**
If you want specific pattern, tell AI:
- "Show me your plan first" → Plan-Execute
- "Think step by step" → Chain of Thought
- "Look up the answer before deciding" → React

* * *

### 10. **Tools in Claude Code (Real Example)**

Alan demonstrates Claude Code as a practical agent:

#### **What Claude Code Can Access:**
- File system (read, write, delete)
- Terminal commands (run code, install packages)
- Browser (via Chrome extension)
- Python, JavaScript, Node.js
- Databases
- APIs (with keys)

#### **Safety Mechanisms:**
- Asks permission before dangerous actions
- Restricted context (can't access whole machine unless granted)
- Checks work before returning results
- Error handling and recovery

#### **Example Flow:**
```
User: "Clean up this messy CSV data and create a chart"

Claude Code:
1. Plans: "Need to read file, check format, clean, analyze"
2. Reads: CSV file (messy format)
3. Observes: "Dates inconsistent, amounts have symbols, duplicates"
4. Plans: "Will write Python script to standardize"
5. Acts: Runs Python script
6. Checks: Verifies output looks clean
7. Plans: "Will create chart visualization"
8. Acts: Generates chart
9. Outputs: Clean data + chart
```

* * *

### 11. **Interactive Quiz: Which Level Do You Need?**

Alan engages audience with real-world scenarios:

#### **Scenario 1: Translate paragraph into French**
- ❓ Which AI level?
- ✅ **LLM** (single task, no adaptation needed)
- ❌ Not Workflow, not Agent

#### **Scenario 2: Answer questions about bus timetable (PDF file)**
- ❓ Which AI level?
- ✅ **Augmented LLM** (need file access)
- ❌ Not Workflow, not Agent

#### **Scenario 3: Every Friday, turn sign-up sheet into summary email**
- ❓ Which AI level?
- ✅ **Workflow** (repeating same steps)
- ❌ Not Agent (no adaptation)

#### **Scenario 4: Find venue, caterer, date for 50 people under budget (adapt if options fall through)**
- ❓ Which AI level?
- ✅ **Agent** (need adaptive decision-making)
- ❌ Not Workflow (can't pre-plan all scenarios)

#### **Scenario 5: Write 20-page market study (research + writing + fact-checking by specialists)**
- ❓ Which AI level?
- ✅ **Multi-Agent** (need separated specialist roles)
- ❌ Not single Agent (bias if same agent researches AND verifies)

* * *

### 12. **Preventing Hallucination**

**What is Hallucination?**
- AI states something false with confidence
- Not lying (not intentional); confidently wrong

**Example:**
- "What's 2+2?" → AI outputs "5" (hallucination)
- "Who is the CEO of Google?" → AI outputs fake name (hallucination)

**Prevention Strategies:**

1. **Give Right Context:** More context = less hallucination
2. **Use Tools:** Let tools handle exact data (not AI guessing)
3. **System Prompts:** Provide standards at top (cached, cheap)
4. **Multi-Agent Verification:** Have 2nd AI fact-check
5. **Lower Temperature:** More deterministic (less creative, fewer errors)
6. **Multiple LLMs:** Different models catch different errors

**Key Rule:** Never trust AI for exact information without verification.

* * *

### 13. **Cost-Benefit Analysis**

**When NOT to Use Agents:**

```
Scenario: Translate 1,000,000 items daily

LLM: 1 token per item = 1M tokens/day = ~$0.01 ✅ CHEAP
Agent: Every iteration through loop = 10-100 tokens per item
        = 10-100M tokens/day = $0.10-$1.00 per day ❌ EXPENSIVE

Conclusion: Use Agent = Company bankrupt in days
            Use LLM = Perfect, tiny cost
```

**Rule:** Avoid agents for high-volume, deterministic tasks.

* * *

## Key Concepts Summary

### **Five Levels**
1. Naked LLM - Simple
2. Augmented LLM - With tools
3. Workflow - Repeating steps
4. **Agent** - Adaptive loop
5. Multi-Agent - Specialized teams

### **Agentic Loop**
Plan → Act (use tool) → Observe → Repeat

### **Tools**
Enable exact computation, real-time data, autonomous action

### **Four Planning Patterns**
1. Think step-by-step
2. React (reason + act)
3. Plan-execute (to-do list)
4. Check & fix

### **Memory**
Short-term (context window) + Long-term (project files)

* * *

## Action Items

1. **Assess Your Tasks:** Categorize into five levels
2. **Avoid Over-Engineering:** Use simplest level that works
3. **Understand Your Tools:** Know what your AI can access
4. **Cost Justify Agents:** Confirm benefits outweigh tokens
5. **Test Patterns:** See different approaches in action tomorrow

* * *

## Homework (Before Tomorrow's Practical Session)

- Think of a task you want to automate
- Determine which level it truly needs (don't jump to agent)
- Understand what tools it would need
- Consider what memories/context it needs

* * *

## Key Takeaway

> **"An agent is not better than an LLM. It's just more complex and expensive. Use agents only when the task truly requires adaptive decision-making. Otherwise, you're wasting tokens and time."**

* * *

## Connection to Tomorrow

Tomorrow's practical session (Session VII) will show these mechanisms in action:
- Building an application with agents
- Seeing tools execute in real-time
- Understanding cost implications
- Creating practical prompts that leverage these patterns

* * *

**📞 Questions:** Reach out to trainer or cohort; clarify concepts before tomorrow's practical session.

**🔗 Prerequisite:** Understand these concepts before Session VII practical lab.
