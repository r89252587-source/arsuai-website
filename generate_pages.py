import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — ArsuAI</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --white:#ffffff;
  --off-white:#f8f8f6;
  --light-gray:#f0efeb;
  --border:#e5e4e0;
  --text-dark:#111110;
  --text-muted:#6b6a66;
  --text-light:#9b9a96;
  --green:#22c55e;
  --green-light:#dcfce7;
  --green-dark:#15803d;
  --wa-green:#25d366;
  --wa-dark:#128c7e;
  --brand-color: {brand_color};
  --brand-light: {brand_light};
}}
body{{font-family:'DM Sans',sans-serif;background:var(--white);color:var(--text-dark);overflow-x:hidden;line-height:1.6}}
h1,h2,h3,h4,.brand{{font-family:'Syne',sans-serif}}

/* NAV */
nav{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(255,255,255,0.95);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 5%;height:64px;display:flex;align-items:center;justify-content:space-between}}
.nav-brand{{font-family:'Syne',sans-serif;font-weight:800;font-size:1.3rem;letter-spacing:-0.02em;text-decoration:none;color:var(--text-dark);}}
.nav-brand span{{color:var(--wa-dark)}}
.nav-links{{display:flex;gap:2rem;align-items:center}}
.nav-links a{{text-decoration:none;color:var(--text-muted);font-size:0.9rem;font-weight:500;transition:color 0.2s}}
.nav-links a:hover{{color:var(--text-dark)}}
.nav-cta{{background:var(--text-dark);color:var(--white)!important;padding:0.5rem 1.2rem;border-radius:8px;font-weight:500!important;font-size:0.85rem!important}}

/* INNER HERO */
.inner-hero {{
  padding: 140px 5% 80px;
  background: linear-gradient(135deg, var(--brand-light) 0%, var(--off-white) 100%);
  text-align: center;
  position: relative;
}}
.inner-hero h1 {{
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 1.2rem;
  color: var(--text-dark);
}}
.inner-hero h1 span {{
  color: var(--brand-color);
}}
.inner-hero p {{
  font-size: 1.1rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto 2rem;
  line-height: 1.7;
}}

/* CONTENT SECTIONS */
.section-pad {{ padding: 100px 5%; }}
.section-header {{ text-align: center; margin-bottom: 4rem; }}
.section-label {{ font-size: 0.85rem; font-weight: 700; color: var(--brand-color); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem; }}
.section-title {{ font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 800; letter-spacing: -0.02em; }}

/* SERVICES OFFERED */
.services-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}}
.service-box {{
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 2.5rem 2rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}}
.service-box:hover {{
  border-color: var(--brand-color);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
}}
.service-box .icon {{
  width: 56px;
  height: 56px;
  background: var(--brand-light);
  color: var(--brand-color);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}}
.service-box h3 {{
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
}}
.service-box p {{
  font-size: 0.9rem;
  color: var(--text-muted);
  line-height: 1.6;
}}

/* CTA */
.cta-section{{padding:80px 5%;background:var(--text-dark);color:var(--white);text-align:center}}
.cta-section h2{{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:800;letter-spacing:-0.03em;margin-bottom:1rem}}
.cta-sub{{color:#999;font-size:1rem;margin-bottom:2rem;font-weight:300}}
.btn-wa{{background:var(--brand-color);color:white;padding:0.85rem 2rem;border-radius:10px;border:none;font-family:'DM Sans',sans-serif;font-size:0.95rem;font-weight:600;cursor:pointer;display:inline-flex;align-items:center;gap:0.5rem;text-decoration:none;transition:opacity 0.2s}}
.btn-wa:hover{{opacity:0.9}}

/* FOOTER */
footer{{background:#0d0d0c;color:#666;padding:2.5rem 5%;display:flex;align-items:center;justify-content:space-between;font-size:0.82rem;flex-wrap:wrap;gap:1rem}}
.footer-brand{{font-family:'Syne',sans-serif;font-weight:800;color:#999}}

/* RESPONSIVE DESIGN */
@media (max-width: 1024px) {{
  .services-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 768px) {{
  .nav-links {{ display: none; }}
  .services-grid {{ grid-template-columns: 1fr; }}
  footer {{ flex-direction: column; text-align: center; justify-content: center; }}
}}

/* DEMO STYLES */
{demo_styles}

</style>
</head>
<body>

<nav>
  <a href="index.html" class="nav-brand">Auto<span>Flow</span></a>
  <div class="nav-links">
    <a href="index.html#services">Services</a>
    <a href="index.html#pricing">Pricing</a>
    <a href="index.html#process">How It Works</a>
    <a href="index.html#contact" class="nav-cta">Get Started</a>
  </div>
</nav>

<header class="inner-hero">
  <h1><span>{highlight}</span> {title_rest}</h1>
  <p>{hero_desc}</p>
  <a href="#demo" class="btn-wa" style="margin-top: 1rem;">See Live Demo ↓</a>
</header>

<section class="section-pad">
  <div class="section-header">
    <div class="section-label">Features</div>
    <h2 class="section-title">What We Build For You</h2>
  </div>
  <div class="services-grid">
    {features_html}
  </div>
</section>

<section class="section-pad" id="demo" style="background:var(--off-white)">
  {demo_html}
</section>

<section class="cta-section">
  <h2>Ready to Scale Automatically?</h2>
  <p class="cta-sub">Stop doing manual work. Let AI handle the heavy lifting.</p>
  <a href="index.html#contact" class="btn-wa">
    Book a Strategy Call
  </a>
</section>

<footer>
  <div class="footer-brand">ArsuAI</div>
  <div>AI Automation Agency · Patna, Bihar · India</div>
  <div>© 2025 ArsuAI. All rights reserved.</div>
</footer>

<script>
{script}
</script>
</body>
</html>
"""

pages = {
    "instagram": {
        "file": "instagram-management.html",
        "title": "Instagram Management",
        "highlight": "Instagram",
        "title_rest": "Management",
        "brand_color": "#e1306c",
        "brand_light": "#fce8ef",
        "hero_desc": "Auto-respond to DMs and comments, capture leads from Instagram ads, schedule posts, and manage your brand presence 24/7.",
        "features": [
            ("💬", "DM Automation", "Instantly reply to every direct message with intelligent AI bots that guide users down the funnel."),
            ("🗣️", "Comment Auto-Reply", "Turn commenters into customers. Automatically reply to comments and send a DM to capture leads."),
            ("🎯", "Ad Lead Capture", "Link your IG ads to automated chat flows so you instantly engage leads when they are most interested."),
            ("📈", "Unified Dashboard", "Manage all your Instagram interactions in one place alongside WhatsApp and Email.")
        ],
        "demo_styles": '''
.ig-mockup { width: 320px; margin: 0 auto; background: #fff; border: 8px solid #111; border-radius: 40px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.1); display:flex; flex-direction:column; height: 500px;}
.ig-header { padding: 15px; border-bottom: 1px solid #eee; display: flex; align-items: center; gap: 10px; font-weight: 600;}
.ig-avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); }
.ig-body { flex: 1; background: #fafafa; padding: 15px; overflow-y: auto; display:flex; flex-direction:column; gap:12px; }
.ig-msg { padding: 10px 14px; border-radius: 20px; font-size: 0.85rem; max-width: 80%; opacity:0; transform:translateY(10px); transition: all 0.4s;}
.ig-msg.show { opacity:1; transform:translateY(0); }
.ig-in { background: #efefef; align-self: flex-start; color: #262626; border-bottom-left-radius: 4px; }
.ig-out { background: #3797f0; align-self: flex-end; color: #fff; border-bottom-right-radius: 4px; }
.demo-section { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; max-width: 1000px; margin: 0 auto; }
@media (max-width: 768px) { .demo-section { grid-template-columns: 1fr; } }
        ''',
        "demo_html": '''
  <div class="demo-section">
    <div>
      <div class="section-label">Live Demo</div>
      <h3 class="section-title" style="margin-bottom:1rem; font-size:2.2rem;">DM Automation</h3>
      <p style="color:var(--text-muted); margin-bottom:1.5rem;">See how our AI agent instantly responds to a lead inquiring via Instagram DM.</p>
      <ul style="list-style:none; line-height:2;">
        <li>✅ 24/7 Instant Responses</li>
        <li>✅ Automated Link Sharing</li>
        <li>✅ Seamless CRM integration</li>
      </ul>
    </div>
    <div class="ig-mockup">
      <div class="ig-header">
        <div class="ig-avatar"></div>
        <div>ArsuAI_AI</div>
      </div>
      <div class="ig-body">
        <div class="ig-msg ig-in" id="d1">Hey! Saw your reel about automation. Can you help my agency?</div>
        <div class="ig-msg ig-out" id="d2">Hi! 👋 Absolutely. We help agencies scale by automating their client acquisition.</div>
        <div class="ig-msg ig-out" id="d3">Are you currently doing outbound or running ads?</div>
        <div class="ig-msg ig-in" id="d4">Mostly running Meta ads.</div>
        <div class="ig-msg ig-out" id="d5">Perfect! We can connect your Meta ads directly to WhatsApp/IG DMs for instant qualification. 🚀</div>
        <div class="ig-msg ig-out" id="d6">Here is a link to book a quick demo with our team: ArsuAI.in/book</div>
      </div>
    </div>
  </div>
        ''',
        "script": '''
const seq = [
  {id:'d1', delay:500},
  {id:'d2', delay:1500},
  {id:'d3', delay:2500},
  {id:'d4', delay:4500},
  {id:'d5', delay:5500},
  {id:'d6', delay:6500},
];
function runAnim() {
  document.querySelectorAll('.ig-msg').forEach(el => el.classList.remove('show'));
  seq.forEach(s => {
    setTimeout(() => {
      const el = document.getElementById(s.id);
      if (el) el.classList.add('show');
    }, s.delay);
  });
}
runAnim();
setInterval(runAnim, 9000);
        '''
    },
    "email": {
        "file": "email-automation.html",
        "title": "Email Automation",
        "highlight": "Email",
        "title_rest": "Automation",
        "brand_color": "#0ea5e9",
        "brand_light": "#e0f2fe",
        "hero_desc": "Cold outreach campaigns, inbound reply handling, lead nurturing sequences, and CRM sync — fully automated.",
        "features": [
            ("📤", "Cold Outreach", "Automate personalized cold emails at scale without landing in spam."),
            ("🤖", "Reply Handling", "AI reads replies, categorizes them (Positive, OOO, Not Interested), and responds accordingly."),
            ("💧", "Drip Sequences", "Nurture your leads with timed sequences that provide value and drive conversions."),
            ("🔄", "CRM Sync", "Automatically update your CRM records when a lead opens, clicks, or replies to your emails.")
        ],
        "demo_styles": '''
.em-mockup { max-width: 600px; margin: 0 auto; background: #fff; border: 1px solid #ddd; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
.em-header { background: #f9f9f9; padding: 15px 20px; border-bottom: 1px solid #ddd; font-weight: 600; display:flex; justify-content: space-between;}
.em-body { padding: 20px; display:flex; flex-direction:column; gap:15px; }
.em-row { padding: 15px; border: 1px solid #eee; border-radius: 8px; display:flex; gap:15px; opacity:0; transform:translateX(-20px); transition: all 0.5s; background:#fff;}
.em-row.show { opacity:1; transform:translateX(0); }
.em-avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--brand-light); color: var(--brand-color); display:flex; align-items:center; justify-content:center; font-weight:bold;}
.em-content h4 { font-size: 0.95rem; margin-bottom: 5px;}
.em-content p { font-size: 0.85rem; color: #666;}
.em-tag { display:inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight:bold; margin-top: 8px;}
.tag-pos { background: #dcfce7; color: #15803d; }
.tag-ooo { background: #fef08a; color: #854d0e; }
.demo-section { text-align: center; max-width: 800px; margin: 0 auto; }
        ''',
        "demo_html": '''
  <div class="demo-section">
    <div class="section-label">Live Demo</div>
    <h3 class="section-title" style="margin-bottom:1rem; font-size:2.2rem;">AI Inbox Manager</h3>
    <p style="color:var(--text-muted); margin-bottom:2.5rem;">Our AI reads incoming replies, tags them intelligently, and syncs to your CRM instantly.</p>
    
    <div class="em-mockup">
      <div class="em-header">
        <div>Inbox</div>
        <div style="color:var(--brand-color)">AI Active ✨</div>
      </div>
      <div class="em-body">
        <div class="em-row" id="e1">
          <div class="em-avatar">S</div>
          <div class="em-content" style="text-align:left;">
            <h4>Sarah Jenkins</h4>
            <p>"Yes, I'd love to learn more about your services. Can we speak next Tuesday?"</p>
            <span class="em-tag tag-pos">HOT LEAD</span>
            <span class="em-tag" style="background:#e0f2fe; color:#0369a1;">Syncing to CRM...</span>
          </div>
        </div>
        <div class="em-row" id="e2">
          <div class="em-avatar">M</div>
          <div class="em-content" style="text-align:left;">
            <h4>Michael Scott</h4>
            <p>"I am currently out of the office until the 15th."</p>
            <span class="em-tag tag-ooo">OUT OF OFFICE</span>
            <span class="em-tag" style="background:#f3f4f6; color:#374151;">Rescheduling...</span>
          </div>
        </div>
      </div>
    </div>
  </div>
        ''',
        "script": '''
const seq = [
  {id:'e1', delay:500},
  {id:'e2', delay:1500},
];
function runAnim() {
  document.querySelectorAll('.em-row').forEach(el => el.classList.remove('show'));
  seq.forEach(s => {
    setTimeout(() => {
      const el = document.getElementById(s.id);
      if (el) el.classList.add('show');
    }, s.delay);
  });
}
runAnim();
setInterval(runAnim, 5000);
        '''
    },
    "call": {
        "file": "ai-call-agent.html",
        "title": "AI Call Agent",
        "highlight": "AI Call",
        "title_rest": "Agent",
        "brand_color": "#8b5cf6",
        "brand_light": "#ede9fe",
        "hero_desc": "Voice AI agents that call leads, handle inbound calls, qualify prospects, and speak natural Hindi/English.",
        "features": [
            ("📞", "Inbound Call Handling", "Never miss a call again. AI answers inbound calls, resolves queries, or routes them to the right person."),
            ("🚀", "Outbound Dialer", "Automatically call new leads within 5 minutes of sign-up to qualify them while they are still hot."),
            ("🗣️", "Multilingual Support", "Agents converse naturally in Hindi, English, and regional languages with local accents."),
            ("📊", "Call Transcripts", "Every call is recorded, transcribed, and summarized automatically in your CRM.")
        ],
        "demo_styles": '''
.call-mockup { max-width: 500px; margin: 0 auto; background: #fff; border: 1px solid #ddd; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
.call-header { background: var(--brand-color); color: #fff; padding: 25px 20px; text-align: center; }
.call-avatar { width: 70px; height: 70px; border-radius: 50%; background: #fff; margin: 0 auto 10px; display:flex; align-items:center; justify-content:center; font-size: 2rem;}
.call-body { padding: 20px; display:flex; flex-direction:column; gap:15px; height: 350px; overflow-y:auto; background: #f8fafc;}
.call-bubble { padding: 12px 16px; border-radius: 16px; font-size: 0.9rem; max-width: 85%; opacity:0; transform:translateY(10px); transition: all 0.4s; line-height: 1.5;}
.call-bubble.show { opacity:1; transform:translateY(0); }
.cb-ai { background: #fff; align-self: flex-start; color: #333; border: 1px solid #e2e8f0; border-bottom-left-radius: 4px; }
.cb-user { background: var(--brand-light); align-self: flex-end; color: var(--brand-color); border-bottom-right-radius: 4px; }
.demo-section { text-align: center; max-width: 800px; margin: 0 auto; }
        ''',
        "demo_html": '''
  <div class="demo-section">
    <div class="section-label">Live Demo</div>
    <h3 class="section-title" style="margin-bottom:1rem; font-size:2.2rem;">Live Call Transcription</h3>
    <p style="color:var(--text-muted); margin-bottom:2.5rem;">Experience a natural conversation where AI qualifies a lead over the phone.</p>
    
    <div class="call-mockup">
      <div class="call-header">
        <div class="call-avatar">🤖</div>
        <h3 style="font-size: 1.2rem;">Calling Lead...</h3>
        <p style="font-size: 0.85rem; opacity: 0.8;">00:45</p>
      </div>
      <div class="call-body">
        <div class="call-bubble cb-ai" id="c1">"Hi, am I speaking with Rahul?"</div>
        <div class="call-bubble cb-user" id="c2">"Yes, speaking."</div>
        <div class="call-bubble cb-ai" id="c3">"Hi Rahul, this is ArsuAI AI. I saw you just downloaded our e-book on automation. I'm calling to see if you have any questions?"</div>
        <div class="call-bubble cb-user" id="c4">"Yeah, actually I was wondering if this works for real estate?"</div>
        <div class="call-bubble cb-ai" id="c5">"Absolutely! We have great workflows for real estate lead qualification. Would you be open to a 10-minute demo tomorrow at 2 PM?"</div>
        <div class="call-bubble cb-user" id="c6">"Sure, 2 PM works."</div>
      </div>
    </div>
  </div>
        ''',
        "script": '''
const seq = [
  {id:'c1', delay:500},
  {id:'c2', delay:2000},
  {id:'c3', delay:3500},
  {id:'c4', delay:6000},
  {id:'c5', delay:8000},
  {id:'c6', delay:11000},
];
function runAnim() {
  document.querySelectorAll('.call-bubble').forEach(el => el.classList.remove('show'));
  seq.forEach(s => {
    setTimeout(() => {
      const el = document.getElementById(s.id);
      if (el) el.classList.add('show');
    }, s.delay);
  });
}
runAnim();
setInterval(runAnim, 14000);
        '''
    },
    "workflow": {
        "file": "workflow-automation.html",
        "title": "Workflow Automation",
        "highlight": "Workflow",
        "title_rest": "Automation",
        "brand_color": "#f97316",
        "brand_light": "#ffedd5",
        "hero_desc": "Connect your tools — CRM, sheets, WhatsApp, email — into smart n8n workflows that eliminate manual work.",
        "features": [
            ("🔗", "App Integration", "Connect over 1000+ apps seamlessly without writing custom API code."),
            ("⚡", "Real-Time Triggers", "Trigger actions instantly. When a new lead hits your sheet, text them within 1 second."),
            ("🛠️", "Custom Logic", "Build complex if/then branching, formatting, and data manipulation inside workflows."),
            ("🔒", "Self-Hosted or Cloud", "We can deploy your automation infrastructure (like n8n) on your own secure servers.")
        ],
        "demo_styles": '''
.wf-mockup { max-width: 700px; margin: 0 auto; background: #fff; border: 1px solid #ddd; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 40px; }
.wf-node { display:inline-flex; align-items:center; gap: 10px; padding: 12px 20px; background: #fff; border: 2px solid var(--brand-light); border-radius: 8px; font-weight: 600; font-size:0.9rem; position:relative; z-index:2; opacity:0; transform:scale(0.9); transition:all 0.5s;}
.wf-node.show { opacity:1; transform:scale(1); border-color: var(--brand-color);}
.wf-icon { font-size: 1.5rem; }
.wf-arrow { font-size: 2rem; color: #cbd5e1; margin: 0 15px; opacity:0; transition:all 0.5s;}
.wf-arrow.show { opacity:1; color: var(--brand-color);}
.wf-container { display:flex; align-items:center; justify-content:center; flex-wrap: wrap; gap: 10px;}
.demo-section { text-align: center; max-width: 800px; margin: 0 auto; }
        ''',
        "demo_html": '''
  <div class="demo-section">
    <div class="section-label">Live Demo</div>
    <h3 class="section-title" style="margin-bottom:1rem; font-size:2.2rem;">Visual Automation Builder</h3>
    <p style="color:var(--text-muted); margin-bottom:2.5rem;">See how a simple lead trigger can cascade into a full business operation automatically.</p>
    
    <div class="wf-mockup">
      <div class="wf-container">
        <div class="wf-node" id="w1"><span class="wf-icon">📝</span> Facebook Lead Ad</div>
        <div class="wf-arrow" id="a1">→</div>
        <div class="wf-node" id="w2"><span class="wf-icon">📊</span> Google Sheets Sync</div>
        <div class="wf-arrow" id="a2">→</div>
        <div class="wf-node" id="w3"><span class="wf-icon">💬</span> WhatsApp Welcome Msg</div>
      </div>
    </div>
  </div>
        ''',
        "script": '''
const seq = [
  {id:'w1', delay:500},
  {id:'a1', delay:1500},
  {id:'w2', delay:2000},
  {id:'a2', delay:3000},
  {id:'w3', delay:3500},
];
function runAnim() {
  document.querySelectorAll('.wf-node, .wf-arrow').forEach(el => {
    el.classList.remove('show');
  });
  seq.forEach(s => {
    setTimeout(() => {
      const el = document.getElementById(s.id);
      if (el) el.classList.add('show');
    }, s.delay);
  });
}
runAnim();
setInterval(runAnim, 6000);
        '''
    },
    "lead": {
        "file": "lead-generation.html",
        "title": "Lead Generation",
        "highlight": "Lead",
        "title_rest": "Generation",
        "brand_color": "#ef4444",
        "brand_light": "#fee2e2",
        "hero_desc": "End-to-end lead gen — from Meta Ads to WhatsApp follow-up, AI classification (HOT/WARM/COLD), and auto-booking.",
        "features": [
            ("🎯", "Targeted Meta Ads", "We create and manage highly targeted ad campaigns on Facebook and Instagram."),
            ("🤖", "Instant Qualification", "Leads are instantly met with an AI chat that asks qualifying questions to determine intent."),
            ("🔥", "AI Lead Scoring", "AI automatically categorizes leads as Hot, Warm, or Cold based on their responses."),
            ("📅", "Auto-Booking", "Hot leads are automatically sent a Calendly link to book a sales call with your team.")
        ],
        "demo_styles": '''
.lead-mockup { max-width: 600px; margin: 0 auto; display:flex; flex-direction:column; gap: 20px;}
.lead-step { background: #fff; padding: 20px; border-radius: 12px; border: 1px solid #eee; display:flex; align-items:center; gap: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); opacity:0; transform:translateY(20px); transition: all 0.5s; text-align:left;}
.lead-step.show { opacity:1; transform:translateY(0); border-left: 4px solid var(--brand-color); }
.ls-num { width: 40px; height: 40px; background: var(--brand-light); color: var(--brand-color); border-radius: 8px; display:flex; align-items:center; justify-content:center; font-weight:bold; font-size:1.2rem; flex-shrink:0;}
.ls-text h4 { margin-bottom: 5px; font-size:1.05rem;}
.ls-text p { font-size: 0.85rem; color: #666;}
.demo-section { text-align: center; max-width: 800px; margin: 0 auto; }
        ''',
        "demo_html": '''
  <div class="demo-section">
    <div class="section-label">Live Demo</div>
    <h3 class="section-title" style="margin-bottom:1rem; font-size:2.2rem;">The Automated Funnel</h3>
    <p style="color:var(--text-muted); margin-bottom:2.5rem;">Watch how we turn a stranger into a booked appointment seamlessly.</p>
    
    <div class="lead-mockup">
      <div class="lead-step" id="l1">
        <div class="ls-num">1</div>
        <div class="ls-text">
          <h4>User sees Meta Ad</h4>
          <p>Targeted prospect clicks on a "Learn More" button on Instagram.</p>
        </div>
      </div>
      <div class="lead-step" id="l2">
        <div class="ls-num">2</div>
        <div class="ls-text">
          <h4>WhatsApp AI Opens</h4>
          <p>User is instantly greeted by AI. AI asks 3 qualifying questions.</p>
        </div>
      </div>
      <div class="lead-step" id="l3">
        <div class="ls-num">3</div>
        <div class="ls-text">
          <h4>Lead Scored as "HOT"</h4>
          <p>User matches criteria. AI updates CRM and labels lead as HOT.</p>
        </div>
      </div>
      <div class="lead-step" id="l4">
        <div class="ls-num">4</div>
        <div class="ls-text">
          <h4>Meeting Booked</h4>
          <p>AI provides calendar link. User books a call for tomorrow at 10 AM.</p>
        </div>
      </div>
    </div>
  </div>
        ''',
        "script": '''
const seq = [
  {id:'l1', delay:500},
  {id:'l2', delay:1500},
  {id:'l3', delay:2500},
  {id:'l4', delay:3500},
];
function runAnim() {
  document.querySelectorAll('.lead-step').forEach(el => el.classList.remove('show'));
  seq.forEach(s => {
    setTimeout(() => {
      const el = document.getElementById(s.id);
      if (el) el.classList.add('show');
    }, s.delay);
  });
}
runAnim();
setInterval(runAnim, 6000);
        '''
    }
}

for key, data in pages.items():
    features_html = ""
    for icon, title, desc in data["features"]:
        features_html += f'''
    <div class="service-box">
      <div class="icon">{icon}</div>
      <h3>{title}</h3>
      <p>{desc}</p>
    </div>'''
    
    content = TEMPLATE.format(
        title=data["title"],
        highlight=data["highlight"],
        title_rest=data["title_rest"],
        brand_color=data["brand_color"],
        brand_light=data["brand_light"],
        hero_desc=data["hero_desc"],
        features_html=features_html,
        demo_styles=data["demo_styles"],
        demo_html=data["demo_html"],
        script=data["script"]
    )
    
    filepath = os.path.join(r"d:\Materials\Worksapce\Automation\WebSite", data["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {data['file']}")

print("All files created.")
