# fluxandform.io — redesign brief

Handoff document for a Claude Code session. Everything in "Settled" is decided; do not
re-litigate it. Everything in "Your call" is genuinely open.

---

## 1. What this site is

The landing page for Flux and Form LLC, a one-person iOS studio in Columbus, Ohio.

The current site is a generic agency template written in the first-person plural for a
company that does not exist. The redesign replaces it with a personal, first-person
studio page.

**Do not build on the existing code.** It is included at the end of this brief as
reference for what is being replaced, not as a starting point. Start fresh.

You are on a redesign branch of the existing repository. The old `index.html` and its
CSS have already been deleted deliberately — do not restore them, do not recover them
from git history, and do not port them to Astro. The previous site is tagged
`pre-redesign` if it is ever needed. `CNAME` and the privacy content are the only
things carried forward.

**Audience:** people who find the studio through an app, or who want to know who makes
these apps. Not clients. The site does not solicit contract work and must not imply
availability for hire.

**Tone:** plain, confident, unhurried. No marketing voice, no exclamation, no
"passionate about." The page is deliberately sparse — nothing has shipped yet, so there
are no screenshots. Sparseness must read as intent, not as an unfinished page.

---

## 2. Scope of v1

Build:

1. **The landing page** — full copy in §4.
2. **A per-app detail page template**, rendered from the data file, with one app page
   generated as proof. Leave it unpopulated — no screenshots, no marketing copy. This
   exists so the structure is proven before the first app ships.
3. **`privacy.html`** — restyled to match the new design. Content unchanged.

Do not build: a blog, a contact form, a services or hire-me section, a newsletter
signup, app screenshots, or per-app marketing pages beyond the template.

---

## 3. Stack

- **Astro**, static output, zero client-side JavaScript unless something genuinely needs it.
- **Hosting stays GitHub Pages** on the existing custom domain `fluxandform.io`.
- **Replace the current deploy setup** with the official Astro GitHub Pages workflow
  (`withastro/action`), building from the repository root. The site currently deploys
  straight from a branch with no build step, which Astro cannot use.
- **`CNAME` must survive into the build output** — put it in `public/` so it lands in
  `dist/`. If it doesn't ship, the custom domain drops on the first deploy and HTTPS
  has to be re-provisioned. This is the standard way an Astro-on-Pages migration takes
  a site down.
- No external services, no third-party scripts, no analytics, no tag managers.
- Self-host all fonts as `woff2` in the repo. **No Google Fonts request, no CDN
  font request.** This is a hard requirement — see §7.

---

## 4. Final copy

This copy is settled. Set it as written. Do not paraphrase, expand, or "improve" it.

### Header

```
FLUX & FORM                                    COLUMBUS, OH / EST. 2025
```

### Hero

> # The good part is happening off-screen.
> ## I build apps that know it.

**The line breaks are content, not layout.** "The good part is happening off-screen."
and "I build apps that know it." must render as two distinct lines with a visible beat
between them, at every breakpoint. The second line is set in a lighter tone than the
first. If these collapse into a single flowing paragraph, the copy fails.

### Subhead

> I'm Todd. I build iOS apps. Flux and Form is my one-person studio in Columbus, Ohio.

Three sentences, three full stops. Do not join them with conjunctions.

### Section: House rules

Section label: `HOUSE RULES`

> **Your data doesn't travel without a reason.**
> On your device by default. On a server only when the app can't work any other way.
>
> **It has to be worth keeping.**
> Either it does something nothing else does, or it's simply a good time.
>
> **Nobody's counting.**
> No streaks, no notifications you didn't ask for, nothing that rewards you for staying.

### Section: What I'm building

Section label: `BUILDING` / `04` — the count is derived from the data file, not hardcoded.

> **Inkling**
> A calmer place to think. Talk to it and it writes down what you said, without sending
> a word anywhere.
>
> **Greenroom**
> A quieter place to talk about film. Connection over collection.
>
> **Nightfall**
> A narrator and moderator for Werewolf, so nobody has to sit out to run the game.
>
> **VibeDeck**
> Everyone at the party gets a say in what plays next. The host runs Apple Music, the
> room votes, the queue moves live.

All four are currently `building`.

### Section: Background

Section label: `BACKGROUND`

> Before this, fourteen years in civil design — most recently as a senior designer at a
> national engineering firm here in Columbus. Before that, GIS: building the data and
> the tools other people's work depended on. AWS certified, finishing a software
> development degree.
>
> Infrastructure work teaches you to think in loads and tolerances, and to assume the
> thing you're drawing will outlast your involvement in it. I build software the same way.

Do not name the employer. "a national engineering firm" is deliberate.

### Footer

```
hello@fluxandform.io   Instagram   X   LinkedIn      © 2026 FLUX & FORM, LLC / PRIVACY
```

Social links as mono text links, not icons — icons would be the only glyphs on an
otherwise purely typographic page.

- Instagram — https://instagram.com/fluxandform_apps
- X — https://x.com/fluxandform_app
- LinkedIn — https://linkedin.com/company/flux-and-form
- Privacy — /privacy.html

---

## 5. Design direction

**Concept:** a spec sheet on paper. The studio is a neutral, confident container that
sits above four products with deliberately unrelated design languages. It must not adopt
the aesthetic of any one of them.

- **Light, warm paper background.** Not white, not dark. The paper is the identity.
- **A monospace label column** running down the left edge, indexing every section
  (`HOUSE RULES`, `BUILDING / 04`, `BACKGROUND`). This is the primary structural device
  and the thing that makes the page read as a document rather than a landing page.
- **Hairline rules.** Full-strength rule at the top of each section, lighter rules
  between items within a section.
- **Generous vertical rhythm.** The page should feel unhurried and have real air in it.
- **Large hero.** The headline is the only display-scale element on the page and should
  be noticeably larger than feels safe.
- **No cards, no shadows, no gradients, no rounded boxes, no icons, no illustration.**
  Type, rules, whitespace, and one small colour mark per app. That is the whole kit.

### Per-app accent colour

Each app carries a single small colour mark (a square chip beside its name) drawn from
that app's own visual identity. This turns four unrelated design languages from an
incoherence problem into visible proof of range, and gives a screenshot-less page its
only colour.

Colour values live in the data file, one per app. Treat any values currently in the repo
as provisional — the real colours should be pulled from each app's actual design system
as they are finalised.

Note: Inkling's mark will be quiet and low-contrast by nature. That is correct. A system
where the loudest app has the loudest mark is honest.

---

## 6. Per-app detail pages

The template built in v1 uses the studio aesthetic.

**Longer term, each app page will take on its own app's aesthetic** — Greenroom editorial
and warm, VibeDeck brutalist and terminal, and so on — held together by a thin persistent
studio frame: wordmark, a link back to the studio, and the footer. Everything between the
frame belongs to the app.

Build the template so that per-page style overrides are straightforward later. Do not
attempt those treatments now.

These pages will eventually serve as App Store support and privacy destinations, so their
URLs must be stable: `/inkling`, `/greenroom`, `/nightfall`, `/vibedeck`.

---

## 7. Typography

Three voices, one job each.

| Role | Face | Usage |
|---|---|---|
| Hero | An editorial serif — **to be chosen, see below** | The hero headline only. Nothing else on the site. |
| Labels & metadata | **Commit Mono**, self-hosted | Section labels, status badges, header meta line, footer. |
| Body | System sans stack | Everything else. |

**Commit Mono rules — enforce these:**

- Only for section labels, status badges, the location/est line, and the footer.
- Never for body copy, app names, headings, or the subhead.
- Uppercase, letterspacing ~0.06–0.08em, size 10–11px, never below 10px.
- One weight. Regular.

**System sans** renders as SF on Apple devices, which is quietly right for an iOS studio,
costs nothing to load, and stays neutral so the serif and mono carry the character.

### Serif — your task

Propose **three** serifs for the hero. Requirements:

- Must pair with Commit Mono and hold at display size on a warm paper background.
- Editorial rather than technical.
- OFL or otherwise free for commercial use, and self-hostable.
- **Not Bodoni Moda** — that belongs to Greenroom and reusing it collapses the separation
  between studio and product.
- One weight, regular.

**Render each proposal in situ** — the actual hero lines, at actual size, on the actual
background. Not a type specimen, not a list of names. Three renderings of the real
headline so the choice can be made by eye.

**Fallback note:** if the finished page reads too cold, IBM Plex Mono is the approved
substitute for Commit Mono — it is warmer, at the cost of being wider in the label column.

---

## 8. Data model

App entries live in a single data file (`src/data/apps.json` or an Astro content
collection). Adding a shipped app must be one entry plus one image folder — never a
design session, never hand-written markup.

```json
{
  "slug": "inkling",
  "name": "Inkling",
  "blurb": "A calmer place to think. Talk to it and it writes down what you said, without sending a word anywhere.",
  "status": "building",
  "accent": "#888780",
  "appStoreUrl": null,
  "testFlightUrl": null
}
```

`status` is a closed enum. Badge label and card CTA both derive from it:

| Status | Badge | CTA |
|---|---|---|
| `concept` | Concept | none |
| `building` | In development | none |
| `beta` | TestFlight beta | Join the beta |
| `live` | On the App Store | Download |
| `archived` | Archived | none |

Build the `live` and `beta` states now even though nothing uses them yet. Promoting an
app must be a one-word edit.

---

## 9. Hard constraints

- **No dark mode.** Do not add `prefers-color-scheme`. The paper is the identity and
  must not invert.
- **No third-party network requests of any kind.** No fonts, no scripts, no analytics,
  no embeds. The site's first house rule is that data doesn't travel without a reason;
  the site itself has to obey it. Anyone who reads that line is exactly the sort of
  person who will open the network tab.
- **Hero line breaks are content.** See §4.
- **Label column on narrow screens:** the labels stack *above* their section as small
  mono headers. Do not collapse the grid and leave labels orphaned beside content.
- **Contrast:** verify all muted text against the paper background at its rendered size.
  Mid-grey at 11px is borderline — meet WCAG AA or darken it.
- **Semantic HTML.** One `h1` (the hero), sections as `section`, real headings.
- **Preserve:** `privacy.html` content, `CNAME` (see §3), and the existing social URLs
  exactly as given in §4. The deploy workflow is being replaced, not preserved.

---

## 10. Out of scope — deliberately removed

Do not reintroduce any of these from the old site:

- The "Studio Status / Deep Work Mode / Inquiries are reviewed weekly" block.
- Any hire-me, services, or contact-form section. The mailto is the only contact route.
- **Refract** and **Construction MVP** — both still in development, both removed.
- The `01 / The Motion`, `02 / The Structure` framing.
- Any first-person-plural voice. There is no "we."

---

## 11. Your call

Genuinely open, use your judgement:

- Astro project structure, component boundaries, and file naming.
- Exact type scale, measure, and vertical rhythm within the direction above.
- Exact label column width and how it reflows.
- Whether the header wordmark is text or a simple SVG lockup.
- Favicon and `og:` metadata.
- Whether `privacy.html` becomes an Astro page or stays a static file.

---

## 12. Current site — reference only

For context on what is being replaced. **Do not build on this.**

```
flux&form                                    Contact
Est. 2025 — Columbus, OH

We craft digital experiences.
Engineering web and mobile applications where fluid user interaction
meets structural integrity.

01 / The Motion
Real-time data, API integrations, and adaptive flows. We build apps
that breathe and react to the user.

02 / The Structure
Pixel-perfect UI and strict security compliance. We ensure the
foundation never cracks.

Selected Works
  Refract — Transformation SaaS — Live
  Nightfall — Game Utility — Beta
  Construction MVP — Utility Tool — In Dev

Studio Status
Deep Work Mode — We are currently heads-down on internal product
development. Inquiries are reviewed weekly.

© 2026 Flux & Form, LLC.
Privacy · Instagram · Twitter · LinkedIn
```

Problems with it, for reference: agency voice for a solo studio, first-person plural,
no personal identity, placeholder projects presented as work, a status block implying
availability for hire, and generic template structure throughout.
