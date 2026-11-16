# Practical Lab: Agents Mechanisms - Building Real Applications

**📅 Date & Time:** November 15, 2026 at 17:00 (5:00 PM)  
**👨‍🏫 Presenter:** Alan Al Jammoor  
**🎯 Session Type:** Live Demonstration + Interactive Problem Solving (1 hour 4 minutes)

---

## Overview

This practical session brings yesterday's theoretical foundations to life. Participants watch real applications built by agents, observe the loop in action with actual tools, and participate in interactive exercises. The focus is on seeing tools execute, understanding cost implications, and recognizing when agents are truly valuable. Alan demonstrates multiple real-world examples from simple to complex.

---

## Key Learning Outcomes

1. **See Agents in Action** - Observe the loop executing with real tools
2. **Understand Tool Usage** - Watch different tools solve different problems
3. **Learn Effective Prompting** - See how structure reduces token waste
4. **Manage Risk** - Know where to put human oversight ("Keep a human in charge")
5. **Apply to Real Work** - Leave with templates you can use immediately

---

## Main Topics Covered

### 1. **The Five Core Rules for Strong Prompts**

Before demonstrating agents, Alan emphasizes prompt structure:

#### **Why Structure Matters**
- Reduces hallucination by 80%+
- AI understands exactly what you want
- Saves tokens by avoiding rework
- Tells AI which tools to use (critical!)

#### **Five Components of Strong Prompts**

```markdown
1. GOAL
   - What is the end outcome?
   - Be crystal clear

2. CONTEXT
   - What background info does AI need?
   - What files/resources are relevant?
   - Provide exact examples

3. RULES (Constraints)
   - What can it NOT do?
   - Security/compliance requirements
   - Format requirements

4. OUTPUT
   - Exactly what format do you want?
   - 6 slides? 1 page? Code file?
   - Be specific

5. CHECKS
   - What verification should happen?
   - Random sampling? Spot checks?
   - Security verification?
```

#### **Example: Good vs. Bad Prompts**

**❌ BAD Prompt:**
```
"Make a presentation about my sales data"
```
- AI must guess: Which file? Which format? Who's the audience? How many slides?
- Result: Maybe 50% right, needs rework

**✅ GOOD Prompt:**
```markdown
# Sales Analysis Presentation

## Goal
Create a presentation to help decide next month's menu and opening hours

## Context
Use the clean sales file from Step 1
Summarize past 3 months
Target audience: Owner and business partner

## Rules
- Every number must come from the clean data
- Use plain language (not jargon)
- Include at least two charts

## Output
Exactly 6 slides, named in order:
1. Executive Summary
2. Monthly Trends
3. Best Sellers
4. Worst Sellers
5. Recommendations
6. Next Steps

## Checks
- Look at every slide as an image
- Confirm 3 random numbers against original data
- Ensure no errors before delivery
```

**Result:** 95%+ likely to be right first try

#### **Connection to Agent Mechanics**

Notice the prompt also includes **tool permissions**:
- "Use the clean file from Step 1" = Telling agent which file to access
- "Create charts" = Telling agent to use visualization tools
- "Plain language" = Telling agent not to get too technical

**Key Insight:** Your prompt implicitly tells agents which tools to use and how to verify their work.

---

### 2. **Example 1: Data Cleaning (Simple Agent Loop)**

**Real Example:** 3 months of café sales data (messy)

#### **The Messy Data Problem**
```
Date formats: Sometimes "Nov 2", sometimes "2 Nov", sometimes "11/02/2024"
Amounts: Sometimes "$100", sometimes "100 dollars", sometimes "100"
Rows: 979 total, manually fixing is impossible
```

#### **The Agentic Process (Observed Step-by-Step)**

**Step 1: Plan**
```
Agent thinks: "I need to clean 979 rows of data. I cannot fix these one by one manually.
I will use Python to write a script that restructures and cleans everything systematically."
```

**Step 2: Act (Use Tool #1 - Read File)**
```
Agent: "Show me the messy data"
Result: Gets back file contents (shows the 979 rows of inconsistent data)
```

**Step 3: Observe & Replan**
```
Agent: "Now I see the problem. I need Python tool to process systematically."
```

**Step 4: Act (Use Tool #2 - Run Python)**
```
Agent writes Python script to:
- Standardize all dates to YYYY-MM-DD
- Remove currency symbols, convert to numbers
- Remove duplicates
- Output to clean CSV

Script executes, creates clean file with 946 rows (deduplicated)
```

**Step 5: Observe Result**
```
Agent: "Data is now clean and standardized. Goal achieved."
Output: Clean sales file, ready for analysis
```

**Token Cost:** ~15,000 tokens (for the entire data cleaning operation)
**Equivalent Work:** Would take human 2-3 hours manually

**Key Learning:** Agent chose Python because it was the right tool for bulk data processing

---

### 3. **Example 2: Create Presentation (Complex Multi-Step)**

**Real Example:** Transform clean data into business-ready deck

#### **The Challenge**
- Take clean sales data
- Analyze for insights
- Create professional presentation
- Verify numbers are accurate
- Format as slides

#### **The Agentic Process**

**Step 1: Plan (Agent's Internal Reasoning)**
```
"User wants a presentation. I need to:
1. Analyze the data for trends and insights
2. Create visualizations/charts
3. Format as slides (probably HTML or PDF)
4. Verify numbers match source data

What's the best order? Should I code first or see the data first?
I'll review the data first, then plan my approach."
```

**Step 2: Act (Tool: Read File)**
```
Agent reads clean sales data
Observes: Cappuccino is 1/5 of all sales
          Saturdays are busiest (15% of weekly sales)
          Matcha latte is worst performer (1 cup/day)
```

**Step 3: Decide Next Step (Replan)**
```
Agent: "I already have the data. Now I'll write Python to create slides."
```

**Step 4: Act (Tool: Run Python - Create Slides)**
```
Agent generates Python script that:
- Creates slide deck (PowerPoint or HTML format)
- Adds the insights as content
- Formats professionally
```

**Step 5: Act (Tool: Look at Image)**
```
Agent: "Render the first slide as image so I can verify it looks correct"
Result: Sees rendered slide
```

**Step 6: Observe & Check**
```
Agent: "Numbers look good, design looks professional. Let me verify accuracy.
Checking random number: Slide says Cappuccino = $11,407. 
Data says $11,407. ✓ Match"
```

**Step 7: Deliver**
```
Complete presentation deck with verified accuracy
```

**Human's Role in the Loop:**
- Define: "I want 6 slides with these requirements"
- Verify: "Does this look right?" (seeing the rendered slides)
- Approve: "Yes, deploy this"

---

### 4. **Example 3: Create Video (AI Creativity + Tools)**

**Real Example:** 30-second promo video for social media

#### **The Interesting Part**
Agent can't generate videos like Gemini can. So what does it do?

#### **Agent's Approach**

**Step 1: Plan**
```
"User wants a 30-second video. I cannot generate video directly.
But I can:
1. Create the visuals (images/graphics with code)
2. Animate them together (using Remotion or similar tool)
3. Result: Animated video"
```

**Step 2: Storyboard (Plan Phase)**
```
"30 seconds at standard frame rate = need 900 frames
Let me break it into 5 scenes × 6 seconds each = 180 frames per scene

Scene 1: Title card (frames 1-180)
Scene 2: Data visualization (frames 181-360)
Scene 3: Chart showing trends (frames 361-540)
...and so on"
```

**Step 3: Ask Humans to Verify Plan**
```
Agent to humans: "Here's my plan. Does this work for you?"
Expected: Humans approve before AI burns tokens
```

**Step 4: Act (Tool: Run Python)**
```
Agent generates Python code that:
- Creates individual frame graphics
- Sets up animation parameters
- Uses colors/design from brand guidelines
```

**Step 5: Act (Tool: Make Video)**
```
Agent uses Remotion (a tool for creating videos)
Remotion combines all frames into animated video
Result: 30-second MP4 file ready for social media
```

**Cost Analysis:**
- One session like this = 20-30 planning loops
- Many attempts if requirements unclear
- Clear requirements = fewer iterations = lower cost

---

### 5. **Example 4: Meal Planner Web App (End-to-End)**

**Real Example:** Interactive web application

#### **Requirements**
- Help families plan weekly meals
- Create shopping list based on selected dishes
- Works offline
- Accessible to non-technical users
- Includes 8 built-in dishes
- Allows adding custom dishes

#### **The Agentic Process**

**Step 1: Plan**
```
Agent: "User wants a web app. I need:
1. Frontend (HTML/CSS/JavaScript for interactivity)
2. Data structure (dish list, shopping list calculator)
3. Offline capability
4. Responsive design

Best approach: Single HTML file with embedded CSS and JavaScript = fully offline"
```

**Step 2: Specification Provided by Human**
```markdown
## Functional Requirements
- Display 7 days of week
- Show 8 built-in meals
- Allow selection per day
- Calculate shopping list automatically
- Show estimated cost
- Allow adding custom meals

## Technical Requirements
- Single HTML file (offline capable)
- Large, readable text
- Mobile-first responsive design
- Works on laptop AND phone
```

**Step 3: Act (Generate Application)**
```
Agent creates HTML file with:
- CSS styling for responsive design
- JavaScript for calculations and interactivity
- Embedded 8-meal database
```

**Step 4: Test (Observe)**
```
Agent: "Let me see if this works as a web page"
(Renders HTML in browser)
Result: Fully functional meal planner displayed
```

**Step 5: Verify Features**
```
- Select meals ✓
- Shopping list updates ✓
- Cost calculates ✓
- Mobile responsive ✓
- Can add custom meals ✓
```

**Delivery:**
```
User can:
1. Open HTML file in any browser
2. Select meals for the week
3. See shopping list automatically
4. Print shopping list
5. Take to store on phone or paper
```

**Key Insight:** No backend, no database, no deployment—just a single HTML file. Perfect for MVP.

---

### 6. **Interactive Exercise: What Tools Will the Agent Use?**

Alan engages audience by asking them to predict:

**Scenario:** "Create a report analyzing 3 months of sales data"

**Possible Tools:**
1. Read file (access the data)
2. Run Python (analyze the data)
3. Look at image (verify report looks right)

**Question to Audience:** "In what ORDER should the agent use these tools?"

**Expected Reasoning:**
```
1. Read file (can't analyze without seeing data) ✓
2. Run Python (analyze the data) ✓
3. Look at image (verify results) ✓
```

**Key Teaching:** Agent considers which tool to use in what order. Humans can guide this.

---

### 7. **The Human-in-the-Loop Principle: "Keep a Human in Charge"**

Alan emphasizes risk management:

#### **High-Risk Actions Requiring Human Approval**

| Situation | Risk | Decision |
|-----------|------|----------|
| **Reversible** | Low | Let AI decide (fix later if needed) |
| **Moderate Risk** | Medium | AI asks permission, humans decide |
| **Irreversible** | High | ALWAYS keep human in charge |
| **High Impact** | High | ALWAYS keep human in charge |

#### **Examples Requiring Human Oversight**

❌ **DON'T Let AI Decide Alone:**
- Delete files (irreversible)
- Send emails to customers (high impact)
- Modify production database (irreversible)
- Approve transactions (high impact)
- Generate public-facing content (reputational risk)
- Access private/sensitive data

✅ **CAN Let AI Decide Alone:**
- Format local files
- Create drafts (you review before sending)
- Analyze data (you verify insights)
- Modify draft code (you test before deployment)
- Run local tests (safe environment)

#### **The Pattern**
```
High-Risk Action → AI asks: "Do you approve? [Allow Once] [Allow Always]"
Human: "Let me review..."
Review: Check the action is correct
Decision: [Allow Once] ← Always choose this, not "Allow Always"
Reason: Each situation might be different
```

**Key Rule:** "Allow Once" > "Allow Always" (maintains human judgment)

---

### 8. **Cost Management in Action**

#### **Real Token Usage from Live Demo**

| Task | Tokens Used | Cost | Time |
|------|-----------|------|------|
| Clean 979 rows data | ~15,000 | ~$0.15 | 2 min |
| Create 6-slide deck | ~25,000 | ~$0.25 | 3 min |
| Generate 30-sec video | ~20,000 | ~$0.20 | 2 min |
| Build meal planner app | ~30,000 | ~$0.30 | 3 min |
| **Total Example** | **~90,000** | **~$0.90** | **~10 min** |

**Comparison:**
- Equivalent human work: 20+ hours → costs $500-2,000
- Agent work: 10 minutes → costs $0.90
- Savings: 99.95%+

**BUT:** Only if requirements are clear, tools are chosen wisely, and human oversight is maintained

---

### 9. **Practical Workflow for Using Agents**

#### **Step 1: Define Your Goal Clearly**
```
❌ "Build a dashboard"
✅ "Build a dashboard showing daily sales by product category, 
   refreshed hourly, with drill-down capability for each category"
```

#### **Step 2: Provide Context**
```
"Here's the data structure..."
"Here's the brand style guide..."
"Here are the acceptance criteria..."
```

#### **Step 3: Specify Tools You Want Used**
```
"Use Python for data processing"
"Use HTML/CSS/JavaScript for frontend (not React, to keep it simple)"
"Use chart.js for visualizations"
```

#### **Step 4: Set Human Checkpoints**
```
"Show me the plan before executing (Plan mode, not Auto)"
"Render the preview before final deployment"
"Run security scans before anything touches production"
```

#### **Step 5: Monitor the Loop**
```
Watch as agent:
- Plans next steps
- Uses tools to execute
- Observes results
- Adjusts if needed
- Loops until complete
```

#### **Step 6: Verify Output**
```
- Does it match your spec? ✓
- Is it secure? (ran scans?) ✓
- Does it perform well? ✓
- Ready to deploy? ✓
```

---

### 10. **Common Mistakes Demonstrated**

#### **Mistake 1: Unclear Requirements**
**Result:** Agent creates "something," but not what you wanted
**Solution:** Use five-component framework from yesterday's session

#### **Mistake 2: Not Using Right Tools**
**Example:** Agent tries to calculate with LLM instead of calculator
**Result:** Wrong answers, wasted tokens
**Solution:** Explicitly tell AI which tools to use

#### **Mistake 3: Too Many Loops**
**Example:** Requirements unclear, so agent keeps reworking
**Result:** Token budget blown
**Solution:** Get requirements right before starting

#### **Mistake 4: Skipping Verification**
**Example:** Deploy without checking numbers
**Result:** Wrong data in production
**Solution:** Always have verification step in plan

#### **Mistake 5: Over-Engineering**
**Example:** Use agent for task that needs simple LLM
**Result:** Expensive, slow, unnecessary complexity
**Solution:** Use simplest tool that works

---

### 11. **Deciding: When IS Agent Right Choice?**

Alan provides decision tree:

```
Task Type?
│
├─ Simple computation (1 step)
│  → Use LLM ✓
│
├─ Need current info
│  → Augmented LLM (with search) ✓
│
├─ Same steps, every time
│  → Workflow ✓
│
├─ ADAPTIVE decision-making needed
│  └─ Single role?
│     → Agent ✓
│     
│  └─ Multiple specialized roles?
│     → Multi-Agent ✓
│
└─ When in doubt?
   → Use simpler level, upgrade if needed
```

---

### 12. **The Three Most Important Lessons**

#### **Lesson 1: Speed Alone ≠ Advantage**
> "You can now describe your idea in English and get code. So can everyone else. What differentiates you is **quality, security, and reliability**."

#### **Lesson 2: Keep Humans in Charge**
> "AI is a powerful tool. But the moment you blindly trust it with critical decisions, you've lost control. Always maintain checkpoints."

#### **Lesson 3: Understand Your Tools**
> "An agent is only as good as the tools it has access to. Know what your AI can do (and cannot do). Design your workflows around those capabilities."

---

## Practical Session Output

**Live Demonstrations Completed:**
1. ✅ Data cleaning (messy → clean CSV)
2. ✅ Report generation (data → 6-slide deck)
3. ✅ Video creation (concept → 30-second video)
4. ✅ Web application (spec → fully functional app)

**All Verifiable:** Participants saw rendered outputs, verified correctness

---

## Homework: Apply Today's Learning

### **For Each of Your Own Projects:**

1. **Define it clearly** (use five-component spec)
2. **Identify tools needed** (Python? JavaScript? Database?)
3. **Plan the loop** (what are steps? In what order?)
4. **Choose right level** (LLM? Augmented LLM? Workflow? Agent? Multi-Agent?)
5. **Build with AI** (use Claude Code or similar)
6. **Verify thoroughly** (security scans, manual checks, testing)
7. **Deploy carefully** (staging first, then production)

---

## Questions Addressed (From Participants)

**Q: When I give AI a prompt, it often skips tasks or misses requirements. Why?**

A: Several reasons:
- Unclear specification (use five-component framework)
- Too many requirements at once (break into steps)
- AI doesn't have context (provide examples and templates)
- **Solution:** Use system prompts (reusable templates) + multi-agent verification

**Q: How do I ensure AI code is secure?**

A: Multiple approaches:
1. Run security scanners (Bandit, TruffleHog, Synk)
2. Have second AI agent review code
3. Use deterministic tools for sensitive operations
4. Test in safe environments before production
5. Keep humans in charge of critical operations

**Q: Can I use multiple AI models to reduce hallucination?**

A: Yes! Perfect approach:
- Model A writes the code
- Model B from different vendor audits the code
- Model A fixes issues
- Result: Much higher quality

**Q: Is AI coding faster than hiring developers?**

A: Yes, but different:
- **Speed:** 100x faster (minutes vs. months)
- **Cost:** 1000x cheaper ($ vs. $k)
- **Catch:** Requires human judgment to verify
- **Trade:** You become the architect/reviewer, not code writer

---

## Key Takeaway

> **"The age of human programmers is not ending. It's evolving. You're becoming architects, reviewers, and decision-makers. AI handles the mechanical coding. You handle judgment, oversight, verification, and strategic decisions."**

---

## Next Steps

**Before Next Session:**
- Practice building something with agents
- Experiment with different tools
- Understand your limitations and AI's limitations
- Prepare questions for future sessions

**Coming Next:**
- Multi-agent teams (coordinating specialized agents)
- Security & safety nets
- MCP (connecting AI to external systems)
- Deployment & operations at scale

---

## Resources

- **Claude Code Documentation:** Available from trainer
- **Tool Integration Guides:** Will be shared in course materials
- **Example Projects:** Available in GitHub repository
- **Template Prompts:** Share in course channel

---

**📞 Support:** Questions or stuck? Reach out to trainer or cohort.

**🎯 Goal for Next Week:** Build 1 complete application using agents, verify it thoroughly, deploy it.

---

**Session Complete!** Next session focuses on putting multiple agents together as a coordinated team.
