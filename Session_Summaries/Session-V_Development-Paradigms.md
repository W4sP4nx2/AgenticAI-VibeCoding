# Development Paradigms - Theoretical and Practical

**📅 Date & Time:** November 7, 2026 at 09:00 (9:00 AM UTC)  
**👨‍🏫 Presenter:** Akshi Rao  
**🎯 Session Type:** Comprehensive Theory + Hands-On Application (4-hour session with breaks)

---

## Overview

This session bridges the gap between understanding Vibe Coding concepts and implementing them in production-level applications. Participants learn that "Vibe Coding" isn't just about typing prompts—it requires understanding **system design principles, business requirements, and software development lifecycle** before engaging AI as a tool. The session emphasizes that **system design is a founding principle** of responsible AI development.

---

## Key Learning Outcomes

1. **System Design First** - Understand why proper planning prevents AI hallucination and wasted tokens
2. **Spec-Driven Workflow** - Learn the five-component system specification framework
3. **Production-Level Coding** - Build applications ready for real-world use, not just demos
4. **Avoid Blind AI Trust** - Understand limitations and when to stop prompting
5. **End-to-End Deployment** - From concept to hosted application

---

## Main Topics Covered

### 1. **Why System Design is Fundamental**

**Historical Context:**
- Google and Amazon interviews require mastery of **system design** for software engineers
- System design addresses: scalability, reliability, performance, security, maintainability
- Building Facebook or Amazon requires complex system architecture across multiple data centers
- **Traditional development:** Months or years to launch a production system

**Current Vibe Coding Challenge:**
- People often launch applications without proper system design thinking
- Result: Applications that work initially but fail under scale, security, or complexity
- AI makes it *easy* to build something—but easy ≠ production-ready
- **Without system design, you waste tokens and create technical debt**

**The Principle:**
> Don't just say "build a dashboard." Say "build a scalable, secure dashboard with these specific requirements, this architecture, and these constraints."

### 2. **The Problem with Random Prompting**

**Anti-Pattern: Vague Requests**
```
❌ "Build a dashboard"
❌ "Create a website"
❌ "Make a chatbot"
```

**Why This Fails:**
- AI must guess what you want (token waste, hallucination)
- Result likely doesn't match your actual needs
- May have security or architectural problems
- You burn tokens before getting something usable

**Better Pattern: Structured Specification**
```
✅ Functional requirements clearly listed
✅ Non-functional requirements defined
✅ Interface design described
✅ Acceptance criteria specified
✅ Constraints and limitations noted
```

### 3. **The Five-Component Specification Framework**

Every system should be defined by:

#### **Component 1: Functional Requirements**
- **Definition:** What MUST the system do?
- **Question:** What is the core purpose and capability?
- **Example (Job Search App):**
  - Search across 3 job websites
  - Filter by city and job title
  - Display results matching user skills

#### **Component 2: Non-Functional Requirements**
- **Definition:** What qualities must it have? (Not "what does it do" but "how well does it do it?")
- **Examples:**
  - Performance: Response time < 2 seconds
  - Security: Comply with OWASP Top 10
  - Usability: Mobile-responsive, intuitive UI
  - Reliability: 99.9% uptime
  - Scalability: Handle 10,000 concurrent users

#### **Component 3: Constraints**
- **Definition:** What are the LIMITS and RESTRICTIONS?
- **Examples:**
  - "No hardcoded credentials"
  - "No external LLM API calls (cost control)"
  - "No complex authentication for MVP"
  - "HTML/CSS/JavaScript only"
  - "Deployable offline"

#### **Component 4: Interface Description**
- **Definition:** How do users interact with it?
- **Examples:**
  - Design language (colors, typography)
  - Layout structure (one-page vs. multi-page)
  - Interaction patterns (scroll vs. click)
  - Accessibility requirements
  - Responsiveness targets (mobile-first? tablet-optimized?)

#### **Component 5: Acceptance Criteria**
- **Definition:** How do we measure SUCCESS?
- **Rule:** Must be testable and measurable
- **Examples:**
  - "Job matching accuracy: ≥ 90% based on keyword matching"
  - "Load time: < 1.5 seconds"
  - "No security warnings from Bandit/TruffleHog"
  - "All features documented and tested"

### 4. **System Design Thinking Exercise**

**Example: Photo Sharing App (Like Instagram)**

**Brainstorming Round (What Matters?):**
- **Authentication:** How do users log in? Security level needed?
- **Security:** Is this public? Data privacy requirements? GDPR/compliance?
- **Scroll Design:** Is it infinitely scrolling (mobile) or paginated (desktop)?
- **UI/UX:** What makes it "addictive" (intentional design)?
- **Functional Requirements:** Upload, download, share, comment, like?
- **Non-Functional Requirements:** Handle 1M users? Global scalability? Real-time notifications?
- **Back-end Storage:** Need database? Cloud? CDN for images?
- **Performance:** How fast must image loading be?

**This exercise prevents:** Building something cool but impractical

### 5. **The Development Lifecycle (QA → Dev → Test → Prod)**

Traditional software development follows this flow:

```
Business Analyst (BA)  →  Developer  →  QA Tester  →  Production
    ↓                        ↓              ↓
Define Requirements     Implement       Verify Quality
What to build?          How to build?   Does it work?
                                        Is it secure?
```

**The Vibe Coding Risk:**
- Many people skip from "What to build?" directly to "Build it with AI"
- Bypassing design, testing, and security reviews
- **Result:** Features that don't match business needs, security vulnerabilities, poor user experience

**Recommended Vibe Coding Process:**
1. **Business Requirements** - Define spec using five components
2. **AI Development** - Generate code based on spec
3. **Testing & Review** - Verify code quality, security, functionality
4. **QA Sign-off** - Confirm acceptance criteria met
5. **Production Deployment** - Release with confidence

### 6. **Real Application: Building a Job Search App**

**User Need:** Daily curated job listings matching my CV and skills

**Specification Using Five Components:**

```
# Job Search Application Specification

## Functional Requirements
1. Search job listings across multiple job boards
2. Filter by: location (cities), job title, experience level
3. Store user preferences and CV information
4. Provide daily curated matches
5. Display job card with: title, company, salary, link

## Non-Functional Requirements
1. Load within 2 seconds
2. Mobile-responsive design (primary mobile use)
3. No authentication required for MVP
4. Scroll-based infinite or pagination-based interface
5. Pink color scheme with modern aesthetics

## Constraints
1. No LLM integration (cost control)
2. No complex backend; static deployment possible
3. No hardcoded credentials
4. No paid APIs (use free tier only)
5. Keyword matching only (no ML/complex algorithm initially)

## Interface Description
- Single-page application (one-page read-only view)
- Scroll through job cards
- One-click apply buttons
- Search filters at top
- Responsive to mobile screen sizes

## Acceptance Criteria
1. Successfully displays 10+ jobs per search
2. Filtering works correctly (location, title, experience)
3. Job matches meet 90% accuracy vs. user CV skills
4. No security warnings from Bandit/TruffleHog/Synk
5. Deployment successful on free tier (Render/Netlify)
6. Mobile loads within 2 seconds
```

### 7. **Practical Implementation with Claude Code**

**Three Critical Decisions Before Prompting:**

1. **Which AI Tool?** (Claude Code, Cursor, ChatGPT, Gemini)
2. **Which Model?** (Claude Opus/Sonnet, GPT-4/3.5, Gemini Pro/Flash)
3. **Which Mode?** (Auto, Plan, Manual)

**Recommended Approach: Plan Mode**
- Shows AI's approach before executing
- Allows review of architecture decisions
- Reduces token waste from wrong approaches
- Enables course-correction early

**Prompt to AI (in Markdown):**

```markdown
# Job Search Application

## Functional Requirements
- Search across 3 websites (Indeed, LinkedIn, FlexJobs)
- Filter by: 3 cities, job titles A/B/C
- Simple search engine, no API needed
- Display results in responsive layout

## Non-Functional Requirements
- Load time < 2 seconds
- Mobile-first responsive design
- Pink and purple color scheme
- Accessible to non-technical users

## Constraints
- No LLM integration
- No authentication/OAuth
- Simple keyword matching only
- Deployable as static site

## Interface
- Single page, scroll design
- HTML/CSS/JavaScript only
- Job cards with apply buttons

## Acceptance Criteria
- 90% keyword match accuracy
- All jobs from latest daily refresh
- No security vulnerabilities
- Mobile load time < 1.5 seconds
- Successfully deployed to Render/Netlify
```

**Key Advantage:** This specification makes AI's job much easier and more accurate

### 8. **Download → Customize → Deploy Workflow**

**Step 1: Generate with Claude Code**
- AI creates initial artifact (HTML/CSS/JavaScript)
- Download as ZIP file

**Step 2: Open in VS Code**
- Extract ZIP in local directory
- Open with VS Code
- Integrate Claude Code extension in "Manual" mode

**Step 3: Customize Offline**
- Change colors in CSS
- Modify fonts and styling
- Update copy/text
- All without burning tokens

**Step 4: Test Locally**
- Run Python: `python3 -m http.server 8080`
- Test in browser at `localhost:8080`
- Verify all features work

**Step 5: Push to GitHub**
- `git init` in project folder
- `git add .`
- `git commit -m "Initial job search app"`
- Create repo on GitHub
- `git remote add origin <repo-url>`
- `git push -u origin main`

**Step 6: Deploy to Render/Netlify**
- Connect GitHub repo
- Select branch (usually `main`)
- Deploy (automatic on each push)
- Get public URL

**Step 7: Share & Monitor**
- Test deployed version on mobile/desktop
- Share portfolio URL with employers
- Monitor for any issues

### 9. **Common Mistakes & Solutions**

| Mistake | Impact | Prevention |
|---------|--------|-----------|
| No spec before prompting | Wasted tokens, wrong features | Write five-component spec first |
| Trusting AI blindly | Security issues, bugs | Always review, test, scan |
| Using only 1 AI model | Limited perspective | Have 2nd AI audit the code |
| Hardcoding secrets | Credential theft | Use `.env` files, never commit |
| Deploying without testing | Public-facing bugs | Always test locally first |
| Ignoring security warnings | Vulnerabilities in production | Run Bandit/TruffleHog/Synk |
| Over-engineering MVP | Wasted time, high cost | Simplify, iterate later |
| Assuming free tier === forever | Sudden cost increase | Plan upgrade path early |

### 10. **When to Stop Using AI & Switch to Manual Coding**

**Decision Framework:**

```
If AI Output = What You Want  →  Use It
If AI is Looping (same answer 3x)  →  Stop, Debug Manually
If AI Hallucinating Heavily  →  Provide More Context
If Simple Problem  →  Maybe just code it yourself
If Your Cost > Outcome Value  →  Manual is faster/cheaper
If Security-Critical  →  Always verify, never trust completely
```

---

## Key Business Insight

### **The Real Cost of Vibe Coding**

- **Traditional Development:** $100k+ salary × 1 engineer × 6 months = Expensive
- **Vibe Coding:** $20/month subscription × 1 person × 1 month = Cheap
- **The Catch:** Only works if you:
  1. Know what you want (good spec)
  2. Can verify it's correct (technical understanding)
  3. Can secure it (security review)
  4. Can deploy it (DevOps knowledge)
  5. Can maintain it (ongoing support)

**Therefore:** Vibe Coding is not a replacement for software engineering—it's an **accelerant for people who understand software engineering**.

---

## Action Items for Participants

1. **Define Your Problem:** Choose an application you want to build
2. **Write Five-Component Spec:** Don't skip this step
3. **Prompt Claude Code:** Use the spec as your prompt
4. **Test Locally:** Verify all features work on your machine
5. **Run Security Scans:** Bandit, TruffleHog, Synk
6. **Deploy to Free Tier:** Get it on the internet
7. **Share and Iterate:** Get feedback, improve

---

## Homework (Optional but Recommended)

**Personal Portfolio/Job Search App Build:**
- Use this exact framework
- Share your deployed URL
- Cohort can provide feedback
- Builds portfolio for interviews/job applications

---

## Key Takeaway

> **"The biggest drawback of Vibe-based coding is failing to scale. Start with the basics and always remember: speed is now available to everyone. Your advantage is ensuring fast code is also safe, strong, and professional."**

**The mindset shift:**
- **Old:** "Can I code this?"  →  **New:** "Should I build this? And how do I verify it's right?"
- From **code writer** → to **system architect and quality gate**

---

## Resources & References

- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **System Design Interview Prep:** Books like "System Design Interview" by Alex Xu
- **Render.com Deployment:** https://render.com/docs
- **Netlify Deployment:** https://docs.netlify.com/
- **GitHub Basics:** https://docs.github.com/en

---

**💡 Instructor Note:** This session emphasizes that **Vibe Coding is not a shortcut around software engineering—it's a tool for those who understand software engineering to move faster.**

---

**📞 Support:** Questions? Reach out to trainer via WhatsApp, Signal, or course communication channels.
