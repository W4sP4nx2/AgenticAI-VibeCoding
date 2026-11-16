# Introduction to Vibe Coding II - Practical Session

**📅 Date & Time:** November 3, 2026 at 18:30 (6:30 PM)  
**👨‍🏫 Presenter:** Phyo Ko Ko (Senior Cybersecurity Analyst, Thailand)  
**🎯 Session Type:** Hands-On Lab + Security Demonstration

---

## Overview

This practical follow-up session demonstrates real-world application of Vibe Coding concepts. Participants see live demonstrations of security scanning tools, then engage in hands-on building of an actual application using Claude Code while implementing security best practices.

---

## Key Learning Outcomes

1. **Demonstrate Security Scanning Tools** - Understand practical security verification
2. **Practical Vibe Coding Workflow** - Build real applications in real-time
3. **Cost-Effective AI Usage** - Manage tokens efficiently with plan mode
4. **Multi-Agent Security Architecture** - Implement automated security checks in development pipeline
5. **GitHub & Deployment** - Deploy applications securely to production

---

## Main Topics Covered

### 1. **Security Scanning Tools Demonstration**

Three primary open-source tools for detecting vulnerabilities in AI-generated code:

#### **Bandit** (Python-focused)
- **Purpose:** Scans Python code for security issues
- **Detection:** SQL injection, path traversal, dangerous functions
- **Example Finding:** Hardcoded passwords, weak cryptography
- **Limitation:** Python-only; Semgrep is language-agnostic alternative
- **Usage:** `bandit <filename.py>` or `bandit -r .` (recursive)

#### **TruffleHog** (Credential Scanning)
- **Purpose:** Detects hardcoded credentials in source code
- **Detection:** API keys, tokens, passwords embedded in code
- **Why Critical:** Exposed credentials on public GitHub = instant compromise
- **Cost Impact:** One leaked API key can drain your budget rapidly if used by malicious actors
- **Usage:** Direct scan from CLI or via their website

#### **Synk** (Dependency Vulnerability Scanner)
- **Purpose:** Checks installed libraries for known vulnerabilities
- **Why Important:** Third-party dependencies often contain outdated/vulnerable versions
- **Process:** Scans `requirements.txt` or similar dependency files
- **Output:** Shows which packages are outdated and have security vulnerabilities
- **Action:** Update vulnerable libraries or consult documentation for patches

### 2. **System Design with Spec-Driven Approach**

Before building anything, establish **five key specifications:**

#### **Five-Star Formula for System Requirements**

```
1. Functional Requirements
   - What MUST the system do?
   - Core features and operations
   - Example: "Search job listings across 3 websites for specific cities and roles"

2. Non-Functional Requirements
   - What else does it need? (Performance, security, usability)
   - Example: "Security compliant with OWASP Top 10", "Load under 2 seconds"
   - Example: "Scroll-worthy design, one-page read-only interface"

3. Constraints
   - What are the LIMITS?
   - Example: "No hardcoded credentials", "No LLM integration required"
   - Example: "HTML/CSS/JavaScript only"

4. Interface Description
   - How does the user interact?
   - Visual design, layout, interaction patterns
   - Example: "Pink color scheme with dark mode support"

5. Acceptance Criteria
   - How do we know it's DONE?
   - Measurable success metrics
   - Example: "Job matches must be 90% accurate based on keyword matching"
```

### 3. **Practical Build Example: Job Search Application**

**Project Brief:**
- **Goal:** Create a web application that searches job listings and matches them to user CV
- **Users:** Job seekers (non-technical to semi-technical)
- **Key Feature:** Curated, relevant job suggestions delivered daily

**System Design Decisions:**
- **Frontend:** HTML/CSS/JavaScript (no complex backend initially)
- **Data Source:** Web scraping + simple keyword matching
- **Database:** Simple local storage initially (optional backend upgrade)
- **Security:** No authentication/OAuth required for MVP
- **Cost:** Minimize API calls; use free tier services where possible

### 4. **Using Claude Code Effectively**

**Three Interaction Modes:**

| Mode | Use Case | Token Cost | Control |
|------|----------|-----------|---------|
| **Auto** | Let AI do everything | Highest | Lowest |
| **Plan Mode** | AI shows plan first, then executes | Medium | Medium |
| **Manual Mode** | You control each step | Lowest | Highest |

**Best Practice:** Use **Plan Mode** to review AI's approach before execution

**Prompt Structure (Markdown format):**
```markdown
# Job Search Application

## Functional Requirements
- Search job listings across Indeed, LinkedIn, FlexJobs
- Filter by role, location, experience level
- Match jobs to user skills with keyword matching

## Non-Functional Requirements
- Secure, no hardcoded API keys
- Fast search (< 2 seconds)
- Mobile-responsive design

## Constraints
- No paid APIs initially (use free tier)
- No complex authentication
- Deployable offline or as static site

## Interface
- Simple, clean design
- Display job cards with key info
- One-click apply buttons

## Acceptance Criteria
- Successfully displays 10+ jobs per search
- Filtering works correctly
- No security warnings from scanning tools
```

### 5. **Live Development Walkthrough**

**Step-by-Step Process:**

1. **Define Requirements** (using five-star formula)
2. **Provide to Claude Code** in markdown format with specific instructions
3. **Review Generated Code** in real-time
4. **Customize Offline** in VS Code (colors, fonts, text)
5. **Run Locally** to test functionality
6. **Execute Security Scans**
   - Run Bandit for Python code issues
   - Run TruffleHog for hardcoded credentials
   - Run Synk for dependency vulnerabilities
7. **Ask Claude to Fix Issues** (use AI to remediate security findings)
8. **Push to GitHub** via CLI commands (AI-assisted)
9. **Deploy Publicly** using Render.com or Netlify

### 6. **Token Usage in Practice**

**Real Example:**
- Building a simple job search app = ~11,000 tokens for complete generation
- Claude Pro subscription ($20/month) allows ~8 full sessions like this per week
- **Cost breakdown:** One hour session ≈ 25% of weekly Pro budget

**Optimization Strategies:**
- Use smaller models for routine tasks
- Batch similar requests together
- Cache system prompts to avoid repetition
- Break large projects into smaller pieces

### 7. **Security Best Practices During Development**

#### **Critical "Do NOTs":**
- ❌ Do NOT put API keys in code you'll push to GitHub
- ❌ Do NOT hardcode passwords or database credentials
- ❌ Do NOT blindly trust AI-generated code without review
- ❌ Do NOT deploy directly to production without testing

#### **Critical "DOs":**
- ✅ Use `.env` files for secrets (never commit them)
- ✅ Run security scanners before each commit
- ✅ Use permission restrictions (ask AI to request permission for dangerous actions)
- ✅ Implement multi-AI review for high-stakes code

#### **Multi-Agent Security Architecture:**
```
Developer  →  Claude AI (Build)  →  Security Scanners  →  Second AI Agent (Audit)  →  Production
                                        (Bandit, TruffleHog, Synk)
```

### 8. **GitHub Integration & Deployment**

**Publishing Workflow:**

```bash
1. Initialize git repository
2. Add all files and create initial commit
3. Create GitHub repository
4. Push local code to GitHub
5. Connect GitHub to Render.com or Netlify
6. Deploy automatically on each push
```

**Deployment Options:**
- **Render.com** - Free static site hosting (best for simple projects)
- **Netlify** - Drag-and-drop deployment, free tier available
- **Paid Options** - Hostinger, GoDaddy for custom domains and 24/7 uptime

**Free vs. Paid:**
- Free tier: Great for portfolio/demo projects
- Paid: Required for production systems requiring reliability

### 9. **Common Pitfalls & Solutions**

| Problem | Cause | Solution |
|---------|-------|----------|
| AI skips requirements | Unclear specification | Use five-star formula; break into steps |
| Hallucinations in output | Insufficient context | Use system prompts, provide examples |
| Expensive token usage | Sending full project repeatedly | Only send changed files; use caching |
| Security vulnerabilities | No scanning | Always run Bandit, TruffleHog, Synk |
| Rate limiting errors | Too many rapid API calls | Use local LLM (Llama, Mistral) or queue requests |

### 10. **Practical Tips from Live Demo**

- **Expect Customization Time:** Even AI-generated apps need color/style adjustments
- **Test Locally First:** Always run applications locally before deploying
- **Weather API Consideration:** If using external APIs, have demo/test keys ready
- **File Organization:** Keep security rules, prompts, and code in separate `.md` files for multi-agent setups
- **Permission Control:** Always use "Allow Once" rather than "Allow Always" for AI-performed actions

---

## Real Application Example: Job Search App

**What Was Built:**
- Registration system (username/password)
- Job search interface (location, job type)
- Database storage for user preferences
- Weather integration (bonus feature)
- Responsive, user-friendly UI

**Vulnerabilities Caught by Scanning:**
- Hardcoded API credentials (TruffleHog alert)
- Weak password validation (Bandit alert)
- Outdated dependencies (Synk alert)

**Resolution:** AI automatically fixed each issue when prompted with security tool reports

---

## Program Evolution

**Key Recognition:** 
- **Junior developers can now work like senior architects** when properly supervised
- **Speed is democratized** - but quality and security become your competitive advantage
- **Your role evolves** from "code writer" to "code reviewer and system architect"

---

## Action Items for Participants

1. **Install Tools:** Bandit, TruffleHog, Synk on your development machine
2. **Set Up Environment:** Python virtual environment, VS Code, Claude Code extension
3. **Create Simple Project:** Follow the job search app example
4. **Run Security Scans:** Practice identifying and fixing vulnerabilities
5. **Deploy:** Push to GitHub and deploy using Render/Netlify
6. **Document:** Create markdown specs for your own projects

---

## Key Takeaway

> **Vibe Coding is not about replacing developers—it's about enhancing them. Your job is to become the quality gate, the security auditor, and the architect. AI handles the mechanical coding; you handle judgment, oversight, and verification.**

---

## Resources

- **Bandit Documentation:** https://bandit.readthedocs.io/
- **TruffleHog GitHub:** https://github.com/trufflesecurity/trufflehog
- **Synk:** https://snyk.io/
- **Render.com:** https://render.com/
- **Netlify:** https://netlify.com/
- **Claude Code Documentation:** Available via trainer

---

**📞 Follow-up:** Share your project attempts; trainer and cohort available for support via WhatsApp/Signal
