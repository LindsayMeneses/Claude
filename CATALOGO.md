# Catálogo de agentes y skills instalados

**619 skills** y **48 agentes**, organizados por área. Se instalan en `.claude/skills/` y `.claude/agents/`, y Claude Code los carga automáticamente al trabajar en este repo.

- **Skills:** se activan solas cuando lo que pides encaja con su descripción. También puedes llamarlas por nombre con `/nombre-de-skill`.
- **Agentes:** pídele a Claude, por ejemplo: *“usa el agente `market-content` para…”*.

Las fuentes y licencias están en `.claude/licenses/`, y el detalle completo en `.claude/installed-manifest.json`.

## 🎬 Video, audio y producción con IA (22)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `ai-video-gen` | Generate AI videos from text prompts using multiple provider gateways. Use when: (1) Generating videos from text descriptions, (2) Creating … | calesthio/OpenMontage |
| skill | `avatar-video` | Create AI avatar videos with precise control over avatars, voices, scripts, scenes, and backgrounds using HeyGen's v2 API. Use when: (1) Cho… | calesthio/OpenMontage |
| skill | `bfl-api` | BFL FLUX API integration guide covering endpoints, async polling patterns, rate limiting, error handling, webhooks, and regional endpoints w… | calesthio/OpenMontage |
| skill | `create-video` | Create videos from a text prompt using HeyGen's Video Agent. Use when: (1) Creating a video from a description or idea, (2) Generating expla… | calesthio/OpenMontage |
| skill | `d3-viz` | Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geogr… | calesthio/OpenMontage |
| skill | `elevenlabs` | Generate AI voiceovers, sound effects, and music using ElevenLabs APIs. Use when creating audio content for videos, podcasts, or games. Trig… | calesthio/OpenMontage |
| skill | `ffmpeg` | Video and audio processing with FFmpeg. Use for format conversion, resizing, compression, audio extraction, and preparing assets for Remotio… | calesthio/OpenMontage |
| skill | `flux-best-practices` | Comprehensive guide for BFL FLUX image generation models. Covers prompting, T2I, I2I, structured JSON, hex colors, typography, multi-referen… | calesthio/OpenMontage |
| skill | `heygen` | [DEPRECATED] Use `create-video` for prompt-based video generation or `avatar-video` for precise avatar/scene control. This legacy skill comb… | calesthio/OpenMontage |
| skill | `lottie-bodymovin` | Use when implementing Disney's 12 animation principles with Lottie animations exported from After Effects | calesthio/OpenMontage |
| skill | `manim-composer` | Trigger when: (1) User wants to create an educational/explainer video, (2) User has a vague concept they want visualized, (3) User mentions … | calesthio/OpenMontage |
| skill | `music` | Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-ge… | calesthio/OpenMontage |
| skill | `remotion-best-practices` | Best practices for Remotion - Video creation in React | calesthio/OpenMontage |
| skill | `shortfilm-prompt` | Generate cinematic AI shortfilm prompts (works with Seedance 2.0, Xiaoyunque, Sora, Kling, Jimeng, Veo) using the 5-stage structure from Mx-… | jnMetaCode/ai-shortfilm-prompts |
| skill | `sound-effects` | Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambien… | calesthio/OpenMontage |
| skill | `speech-to-text` | Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, o… | calesthio/OpenMontage |
| skill | `text-to-speech` | Generate speech audio from text using HeyGen's Starfish TTS model. Use when: (1) Generating standalone speech audio files from text, (2) Con… | calesthio/OpenMontage |
| skill | `video` | When the user wants to create, generate, or produce video content using AI tools or programmatic frameworks. Also use when the user mentions… | coreyhaines31/marketingskills |
| skill | `video-edit` | Edit videos locally using ffmpeg. Trim, concat, resize, speed, overlay, extract audio, compress, and convert. Use when: (1) Trimming or cutt… | calesthio/OpenMontage |
| skill | `video-understand` | Understand video content locally using ffmpeg frame extraction and Whisper transcription. No API keys needed. Use when: (1) Understanding wh… | calesthio/OpenMontage |
| skill | `visual-style` | Create, extract, and apply portable visual design systems via visual-style.md files. Use when: (1) Creating a visual-style.md design system … | calesthio/OpenMontage |
| skill | `visual-style-presets` | Pick and apply a complete visual style direction — surface ladder, type scale, accent discipline, and one signature structural motif — for a… | boraoztunc/skills |

## 🤝 Marketing de afiliados (49)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `ab-test-generator` | Generate A/B test variants for affiliate content. Triggers on: "create A/B test", "test my headline", "optimize my CTA", "generate variants"… | Affitor/affiliate-skills |
| skill | `affiliate-blog-builder` | Write SEO-optimized affiliate blog articles, product reviews, comparison posts, listicles, and how-to guides. Triggers on: "write a blog pos… | Affitor/affiliate-skills |
| skill | `affiliate-program-search` | Research and evaluate affiliate programs to find the best ones to promote. Use this skill when the user asks anything about finding affiliat… | Affitor/affiliate-skills |
| skill | `bio-link-deployer` | Create a Linktree-style bio link hub page as a single self-contained HTML file. Triggers on: "create a bio link page", "make a linktree", "l… | Affitor/affiliate-skills |
| skill | `bonus-stack-builder` | Design exclusive bonus packages that make YOUR affiliate link the obvious choice. Triggers on: "create bonuses for", "bonus stack", "what bo… | Affitor/affiliate-skills |
| skill | `category-designer` | Define a new category where your product wins by default. Reframe the buying decision. Triggers on: "create a category", "category design", … | Affitor/affiliate-skills |
| skill | `commission-calculator` | Calculate realistic affiliate earnings projections before committing to a program. Use this skill when the user asks about affiliate earning… | Affitor/affiliate-skills |
| skill | `comparison-post-writer` | Write "X vs Y" comparison blog posts that help readers choose between two competing products. Triggers on: "write a comparison post", "X vs … | Affitor/affiliate-skills |
| skill | `competitor-spy` | Reverse-engineer successful affiliate strategies from competitors. Use this skill when the user asks about spying on competitors, researchin… | Affitor/affiliate-skills |
| skill | `compliance-checker` | Check affiliate content for FTC compliance and platform rules. Triggers on: "check my content for compliance", "FTC disclosure check", "is t… | Affitor/affiliate-skills |
| skill | `content-angle-ranker` | Rank content angles by engagement data, competition level, and platform fit. Data-driven angle selection instead of guesswork. Use this skil… | Affitor/affiliate-skills |
| skill | `content-decay-detector` | Monitor existing content for ranking drops and trigger refresh workflows. Triggers on: "check for content decay", "which content needs updat… | Affitor/affiliate-skills |
| skill | `content-moat-calculator` | Estimate pages needed for topical authority. Go/no-go decision before investing months in content. Triggers on: "how much content do I need"… | Affitor/affiliate-skills |
| skill | `content-pillar-atomizer` | Take 1 blog post or article and generate 15-30 platform-native micro-content pieces. Not reformatting — re-contextualizing for each platform… | Affitor/affiliate-skills |
| skill | `content-research-brief` | Research trending topics, collect source articles, and generate a structured research brief for content creation. Stop writing from thin air… | Affitor/affiliate-skills |
| skill | `conversion-tracker` | Set up affiliate conversion tracking with UTM parameters and link tagging. Triggers on: "set up tracking", "create UTM links", "track my aff… | Affitor/affiliate-skills |
| skill | `create-skill` | Turn a repeatable AI prompt or workflow into a structured, shareable skill for the affiliate-skills GitHub repository. Use this skill when t… | Affitor/affiliate-skills |
| skill | `email-automation-builder` | Build multi-sequence email automation flows with branching logic. Triggers on: "build email automation", "create email funnel", "email autom… | Affitor/affiliate-skills |
| skill | `email-drip-sequence` | Write an email drip sequence for affiliate marketing. Triggers on: "write me an email sequence", "create a drip campaign", "email nurture se… | Affitor/affiliate-skills |
| skill | `funnel-planner` | Plan a complete affiliate funnel from research to revenue. Triggers on: "plan my affiliate funnel", "create a funnel strategy", "affiliate b… | Affitor/affiliate-skills |
| skill | `github-pages-deployer` | Deploy affiliate content to GitHub Pages for free hosting. Triggers on: "deploy to GitHub Pages", "host on GitHub Pages", "free hosting for … | Affitor/affiliate-skills |
| skill | `grand-slam-offer` | Design irresistible affiliate offers using the Hormozi Grand Slam framework. Triggers on: "create an offer for", "design my offer", "grand s… | Affitor/affiliate-skills |
| skill | `guarantee-generator` | Create YOUR personal guarantee on top of the product's guarantee for risk reversal. Triggers on: "create a guarantee", "guarantee for my aff… | Affitor/affiliate-skills |
| skill | `how-to-tutorial-writer` | Write how-to guides and tutorials that naturally integrate affiliate product recommendations. Triggers on: "write a how-to guide", "tutorial… | Affitor/affiliate-skills |
| skill | `infographic-generator` | Generate branded infographic specifications from any content or data. Outputs structured layout, copy, data visualization, and color scheme … | Affitor/affiliate-skills |
| skill | `internal-linking-optimizer` | Analyze site's internal link structure and optimize for hub-and-spoke SEO architecture. Triggers on: "optimize internal links", "internal li… | Affitor/affiliate-skills |
| skill | `keyword-cluster-architect` | Map 50-200+ keywords into topical clusters for SEO domination. Build content roadmaps for topical authority. Triggers on: "keyword research"… | Affitor/affiliate-skills |
| skill | `landing-page-creator` | Build high-converting affiliate landing pages as single self-contained HTML files. Triggers on: "create a landing page for", "build a landin… | Affitor/affiliate-skills |
| skill | `listicle-generator` | Write "Top N best..." listicle articles for affiliate marketing with mini-reviews, pricing, pros/cons, and CTAs per entry. Triggers on: "wri… | Affitor/affiliate-skills |
| skill | `monopoly-niche-finder` | Find intersection niches where you're the ONLY voice. Thiel's "competition is for losers" lens. Triggers on: "find my monopoly niche", "blue… | Affitor/affiliate-skills |
| skill | `multi-program-manager` | Manage and compare multiple affiliate programs as a portfolio. Triggers on: "manage my affiliate programs", "compare my programs", "portfoli… | Affitor/affiliate-skills |
| skill | `niche-opportunity-finder` | Find untapped affiliate niches with real earning potential. Use this skill when the user asks about picking a niche, finding a niche to star… | Affitor/affiliate-skills |
| skill | `paid-ad-copy-writer` | Write paid ad copy for affiliate offers across ad platforms. Triggers on: "write ad copy", "Facebook ad for affiliate", "Google Ads copy", "… | Affitor/affiliate-skills |
| skill | `product-showcase-page` | Build a single-product deep-dive showcase page as a self-contained HTML file. Triggers on: "build a product showcase page", "deep dive landi… | Affitor/affiliate-skills |
| skill | `proprietary-data-generator` | Create original surveys, benchmarks, and aggregated data nobody else has. Automate data collection for content moats. Triggers on: "create o… | Affitor/affiliate-skills |
| skill | `purple-cow-audit` | Score product remarkability 1-10 to decide if it's worth promoting. Seth Godin's Purple Cow test. Triggers on: "is this product worth promot… | Affitor/affiliate-skills |
| skill | `reddit-post-writer` | Write Reddit posts and comments that recommend affiliate products without getting banned or flagged as spam. Subreddit-native content that a… | Affitor/affiliate-skills |
| skill | `self-improver` | Review affiliate campaign results and improve strategy. Triggers on: "review my results", "what went wrong", "how to improve conversions", "… | Affitor/affiliate-skills |
| skill | `skill-finder` | Find the right Affitor skill for your goal. Triggers on: "which skill should I use", "find me a skill", "what skills are available", "help m… | Affitor/affiliate-skills |
| skill | `social-media-scheduler` | Create a 30-day social media content calendar for affiliate marketing. Triggers on: "create a social media calendar", "30-day content plan",… | Affitor/affiliate-skills |
| skill | `squeeze-page-builder` | Build email capture landing pages (squeeze pages) as single self-contained HTML files. Triggers on: "build a squeeze page", "email capture p… | Affitor/affiliate-skills |
| skill | `submit-program` | Research an affiliate program and create a verified listing for openaffiliate.dev. Use this skill when the user asks anything about listing … | Affitor/affiliate-skills |
| skill | `tiktok-script-writer` | Write short-form video scripts for TikTok, Instagram Reels, and YouTube Shorts that promote affiliate products with strong hooks, demos, and… | Affitor/affiliate-skills |
| skill | `traffic-analyzer` | Analyze website traffic, global rank, engagement metrics, and traffic sources for any domain. Use this skill to evaluate affiliate program w… | Affitor/affiliate-skills |
| skill | `trending-content-scout` | Scan social platforms for top-performing content by engagement before you create anything. Use this skill when the user wants to see what co… | Affitor/affiliate-skills |
| skill | `twitter-thread-writer` | Write X/Twitter threads that get bookmarked, shared, and drive affiliate clicks. Use this skill when the user asks about writing Twitter thr… | Affitor/affiliate-skills |
| skill | `value-ladder-architect` | Design the complete free-to-premium value ladder for affiliate promotions. Triggers on: "value ladder", "customer journey", "upsell path", "… | Affitor/affiliate-skills |
| skill | `viral-post-writer` | Write viral social media posts that promote affiliate products naturally. Use this skill when the user asks anything about writing social me… | Affitor/affiliate-skills |
| skill | `webinar-registration-page` | Build a webinar or live event registration page as a self-contained HTML file with countdown timer, speaker bio, agenda, and registration fo… | Affitor/affiliate-skills |

## 📊 Investigación de tendencias (1)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `last30days` | Research what people actually say about any topic in the last 30 days. Pulls posts and engagement from Reddit, X, YouTube, TikTok, Hacker Ne… | mvanhorn/last30days-skill |

## 🧊 Diseño 3D, WebGL y experiencias inmersivas (29)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `3dicon` | Turn a prompt or a still image into a looping animated icon with real transparency — GPT Image / Nano Banana for the art, Seedance via OpenR… | samyost1/3dicon |
| skill | `3dviz-pro-max` | Design and build expressive 3D scenes, explainers and interactive models with grounded subject knowledge. Use for 3D creation or edits, incl… | viettranx/3dviz-pro-max |
| skill | `aframe-webxr` | Declarative web framework for building browser-based 3D, VR, and AR experiences using HTML and entity-component architecture. Use this skill… | freshtechbro/claudedesignskills |
| skill | `babylonjs-engine` | Comprehensive skill for Babylon.js 3D web rendering engine. Use this skill when building real-time 3D experiences, browser-based games, inte… | freshtechbro/claudedesignskills |
| skill | `blender-web-pipeline` | Blender to web export workflows for 3D models and animations. Use this skill when exporting Blender models to glTF for web, optimizing 3D as… | freshtechbro/claudedesignskills |
| skill | `lightweight-3d-effects` | Lightweight 3D effects for decorative elements and micro-interactions using Zdog, Vanta.js, and Vanilla-Tilt.js. Use this skill when adding … | freshtechbro/claudedesignskills |
| skill | `liquid-metal-border` | Add and tune animated liquid-metal WebGL borders with the React `metal-fx` package. Use when buttons, icon controls, chips, tabs, cards, or … | boraoztunc/skills |
| skill | `pixijs-2d` | Fast, lightweight 2D rendering engine for creating interactive graphics, particle effects, and canvas-based applications using WebGL/WebGPU.… | freshtechbro/claudedesignskills |
| skill | `playcanvas-engine` | Lightweight WebGL/WebGPU game engine with entity-component architecture and visual editor integration. Use this skill when building browser-… | freshtechbro/claudedesignskills |
| skill | `react-three-fiber` | Build declarative 3D scenes with React Three Fiber (R3F) - a React renderer for Three.js. Use when building interactive 3D experiences in Re… | freshtechbro/claudedesignskills |
| skill | `shaders-cursor-ripples` | Add cursor-following fluid WebGPU distortion over an existing image with the Shaders library's ImageTexture and CursorRipples components. Us… | boraoztunc/skills |
| skill | `spline-interactive` | Browser-based 3D design tool with visual editor, animation, and web export. Use this skill when creating 3D scenes without code, designing i… | freshtechbro/claudedesignskills |
| skill | `substance-3d-texturing` | Comprehensive skill for Adobe Substance 3D Painter texturing and material creation workflow. Use this skill when creating PBR materials, exp… | freshtechbro/claudedesignskills |
| skill | `thinking-orbs` | Add accessible animated AI loading and agent-status indicators with the React thinking-orbs library. Use when a chat, copilot, voice, search… | boraoztunc/skills |
| skill | `three` | Three.js and WebGL adapter patterns for HyperFrames. Use when creating deterministic Three.js scenes, WebGL canvas layers, AnimationMixer ti… | boraoztunc/skills |
| skill | `threejs-animation` | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF anima… | calesthio/OpenMontage |
| skill | `threejs-fundamentals` | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configurin… | calesthio/OpenMontage |
| skill | `threejs-geometry` | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertice… | calesthio/OpenMontage |
| skill | `threejs-interaction` | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection… | calesthio/OpenMontage |
| skill | `threejs-lighting` | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing l… | calesthio/OpenMontage |
| skill | `threejs-loaders` | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing… | calesthio/OpenMontage |
| skill | `threejs-materials` | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating cust… | calesthio/OpenMontage |
| skill | `threejs-postprocessing` | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creatin… | calesthio/OpenMontage |
| skill | `threejs-shaders` | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing frag… | calesthio/OpenMontage |
| skill | `threejs-textures` | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, H… | calesthio/OpenMontage |
| skill | `threejs-webgl` | Comprehensive skill for Three.js 3D web development. Use this skill when building interactive 3D scenes, WebGL/WebGPU applications, product … | freshtechbro/claudedesignskills |
| skill | `typegpu` | TypeGPU and raw WebGPU adapter patterns for HyperFrames. Use when creating GPU-rendered compositions with TypeGPU, raw WebGPU, WGSL fragment… | boraoztunc/skills |
| skill | `web3d-integration-patterns` | Meta-skill for combining Three.js, GSAP ScrollTrigger, React Three Fiber, Motion, and React Spring for complex 3D web experiences. Use when … | freshtechbro/claudedesignskills |
| skill | `webgl-laser` | Create a fixed full-screen WebGL laser background effect with a thin white-hot vertical core, restrained brand-colored halo, and soft smoky … | boraoztunc/skills |

## 🖼️ Generación de imágenes con IA (10)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `gallery-researcher` | Gallery search and inspiration agent. Delegates here when user wants to find references, explore styles, build a mood board, or needs inspir… | wshobson/agents (meigen-ai-design) |
| 🤖 agente | `image-generator` | Image generation executor agent. Delegates here for ALL generate_image calls to keep the main conversation context clean. Spawn one per imag… | wshobson/agents (meigen-ai-design) |
| 🤖 agente | `prompt-crafter` | Batch prompt writing agent. Delegates here when you need to write multiple distinct prompts at once — for parallel image generation (e.g., "… | wshobson/agents (meigen-ai-design) |
| skill | `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world prese… | Leonxlnx/taste-skill |
| skill | `image` | When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product mockups, profile ban… | coreyhaines31/marketingskills |
| skill | `imagegen-frontend-mobile` | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-pla… | Leonxlnx/taste-skill |
| skill | `imagegen-frontend-web` | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE… | Leonxlnx/taste-skill |
| skill | `product-photoshoot` | Optional product imagery planning. Use when the user asks for help to "shoot a product", "make e-commerce product images", "product photogra… | jau123/MeiGen-AI-Design-MCP |
| skill | `social-thumbnail` | Optional thumbnail planning for short-video platforms and social feeds. Use when the user asks for creative help with a "video thumbnail", "… | jau123/MeiGen-AI-Design-MCP |
| skill | `visual-creative` | Optional visual planning assistant. Use when the user asks MeiGen to develop a creative idea, explore visual directions, improve a prompt, o… | jau123/MeiGen-AI-Design-MCP |

## 🎨 Branding e identidad (31)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `b2b-brand-marketing` | Build and execute brand marketing strategy for B2B companies — thought leadership, ABM brand layer, trust signals, LinkedIn presence, long s… | arnabbagxd/Brand-building-skills |
| skill | `brand` | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, market… | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `brand-answer-monitoring` | Track how AI assistants describe your brand over time and catch wrong, outdated, or damaging claims. Claude builds your monitoring prompt se… | irinabuht12-oss/marketing-skills |
| skill | `brand-architecture` | Define how multiple brands, sub-brands, and product lines relate to each other under one organization. Use when the user says "brand archite… | arnabbagxd/Brand-building-skills |
| skill | `brand-audit` | Assess the health and consistency of an existing brand — identity, messaging, voice, positioning, and market perception. Use when the user s… | arnabbagxd/Brand-building-skills |
| skill | `brand-context` | Foundation skill that captures and stores core brand context — identity, audience, positioning, values, and voice. Use when the user says "s… | arnabbagxd/Brand-building-skills |
| skill | `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use… | anthropics/skills |
| skill | `brand-identity` | Create a visual identity brief for a brand — logo direction, color palette, typography, imagery style, and design system foundations. Use wh… | arnabbagxd/Brand-building-skills |
| skill | `brand-landingpage` | Brand-first landing page designer — runs a brand-identity interview (colors, typography, shape language), then generates and iterates on a p… | wshobson/agents (brand-landingpage) |
| skill | `brand-launch` | Plan and execute a new brand launch — from internal rollout to public debut. Use when the user says "launch the brand", "brand launch plan",… | arnabbagxd/Brand-building-skills |
| skill | `brand-manifesto` | Write a brand manifesto — a bold, belief-driven declaration of what the brand stands for, fights against, and exists to change. Use when the… | arnabbagxd/Brand-building-skills |
| skill | `brand-measurement` | Define KPIs, metrics, and tracking systems to measure brand health, awareness, perception, and equity over time. Use when the user says "bra… | arnabbagxd/Brand-building-skills |
| skill | `brand-messaging` | Build a brand's messaging hierarchy — taglines, value propositions, key messages, and proof points for each audience. Use when the user says… | arnabbagxd/Brand-building-skills |
| skill | `brand-naming` | Full brand naming workflow for founders, agencies, and businesses. Use this skill whenever the user says "help me name this brand", "brand n… | arnabbagxd/Brand-building-skills |
| skill | `brand-packaging` | Create a packaging design brief — structure, visual direction, hierarchy, materials, and unboxing experience. Use when the user says "packag… | arnabbagxd/Brand-building-skills |
| skill | `brand-partnerships` | Build brand partnership strategy — co-branding campaigns, brand collaborations, licensing deals, partner brand alignment, and joint marketin… | arnabbagxd/Brand-building-skills |
| skill | `brand-positioning` | Define and sharpen a brand's market positioning — where it sits relative to competitors, what it owns, and how it differentiates. Use when t… | arnabbagxd/Brand-building-skills |
| skill | `brand-review` | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixe… | anthropics/knowledge-work-plugins (marketing) |
| skill | `brand-story` | Craft a brand's origin story, founder narrative, and "why we exist" statement. Use when the user says "brand story", "origin story", "founde… | arnabbagxd/Brand-building-skills |
| skill | `brand-strategy` | Full brand strategy workflow for agencies and brand consultants. Acts as a senior brand strategist — collects client information through a s… | arnabbagxd/Brand-building-skills |
| skill | `brand-voice` | Define a brand's verbal identity — tone, voice, writing style, vocabulary, and messaging rules. Use when the user says "brand voice", "tone … | arnabbagxd/Brand-building-skills |
| skill | `campaign-naming-convention-builder` | Builds a consistent, filterable naming convention across your Google and Meta accounts based on your campaign types, objectives, targeting, … | irinabuht12-oss/marketing-skills |
| skill | `competitor-branding` | Analyze how competitors present their brand — identity, messaging, positioning, voice, and visual style — to find gaps and opportunities. Us… | arnabbagxd/Brand-building-skills |
| skill | `critique-brand-consistency` | Critique a rendered screen against mood.md, voice.md, and tokens.md. Use when those brand files exist and you are checking compliance. For d… | Owl-Listener/designer-skills |
| skill | `data-storytelling` | Transform data into compelling narratives using visualization, context, and persuasive structure. Use when presenting analytics to stakehold… | wshobson/agents (business-analytics) |
| skill | `market-brand` |  | zubair-trabzada/ai-marketing-claude |
| skill | `naming-convention` | Establish naming rules for components, tokens, and layers with patterns and worked examples. Use when names are inconsistent or being set. F… | Owl-Listener/designer-skills |
| skill | `obviously-awesome` | Define product positioning by mapping competitive alternatives, unique attributes, and best-fit customers to the right market category. Use … | wondelai/skills |
| skill | `personal-brand` | Build a personal brand strategy for founders, executives, creators, and consultants. Use when the user says "personal brand", "personal bran… | arnabbagxd/Brand-building-skills |
| skill | `rebranding` | Plan and execute a brand transformation — from diagnosis to new brand definition to rollout. Use when the user says "rebrand", "rebranding",… | arnabbagxd/Brand-building-skills |
| skill | `storybrand-messaging` | Clarify brand messaging using narrative structure that positions the customer as hero. Use when the user mentions "brand message", "website … | wondelai/skills |

## 📢 Publicidad pagada (Google, Meta, LinkedIn, TikTok) (37)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `account-structure-review` | Evaluates your campaign and ad set structure against your actual goals and budget. Flags over-segmentation that fragments your data, under-s… | irinabuht12-oss/marketing-skills |
| skill | `ad-copy-variant-generator` | Analyzes your top performing ads, identifies what's working in the hooks, CTAs, messaging angles, and formats, then generates new variants t… | irinabuht12-oss/marketing-skills |
| skill | `ad-creative` | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid… | coreyhaines31/marketingskills |
| skill | `ad-extension-audit` | Reviews all your Google Ads extensions — sitelinks, callouts, structured snippets, call extensions, image extensions, price extensions — acr… | irinabuht12-oss/marketing-skills |
| skill | `ad-spend-allocator` | Multi-channel budget optimization using MER, marginal ROAS, and diminishing returns analysis. Use when pasting multi-channel spend and resul… | irinabuht12-oss/marketing-skills |
| skill | `ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platform… | coreyhaines31/marketingskills |
| skill | `anomaly-detection` | Catches unusual performance changes across your accounts — CPC spikes, CVR drops, spend surges, impression collapses, CTR shifts — and flags… | irinabuht12-oss/marketing-skills |
| skill | `attribution` | When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reco… | coreyhaines31/marketingskills |
| skill | `attribution-model-comparison` | Runs your conversion data through different attribution models side by side — last click, first click, linear, time decay, position based, a… | irinabuht12-oss/marketing-skills |
| skill | `audience-overlap-analysis` | Compares your Meta ad sets and identifies where audiences overlap significantly, causing your ads to compete against each other in the same … | irinabuht12-oss/marketing-skills |
| skill | `bid-strategy-recommendations` | Analyzes your campaign history, conversion volume, CPA targets, and auction dynamics, then recommends the right bid strategy for each campai… | irinabuht12-oss/marketing-skills |
| skill | `budget-scenario-planner` | Models what happens to your CPA, ROAS, conversion volume, and impression share when you increase or decrease budget by any amount. Uses your… | irinabuht12-oss/marketing-skills |
| skill | `channel-mix-optimizer` | Given your total budget, recommends the optimal split across Google Search, PMax, Meta prospecting, Meta retargeting, and any other active c… | irinabuht12-oss/marketing-skills |
| skill | `client-report-narratives` | Takes your raw campaign performance data and writes the executive summary paragraph that goes at the top of the report. The plain English ex… | irinabuht12-oss/marketing-skills |
| skill | `competitor-creative-analysis` | Pulls competitor ads from Meta Ad Library and Google Ads Transparency Center, categorizes their messaging angles, formats, CTAs, and creativ… | irinabuht12-oss/marketing-skills |
| skill | `cpa-diagnostics` | When your CPA spikes, Claude breaks down exactly what caused it. It looks across your campaign data and isolates the contributing factors — … | irinabuht12-oss/marketing-skills |
| skill | `creative-fatigue-detection` | Monitors your ads for early signs of fatigue before performance fully collapses. Tracks frequency buildup, CTR decay, CPM increases, and eng… | irinabuht12-oss/marketing-skills |
| skill | `frequency-cap-recommendations` | Analyzes frequency data across your Meta campaigns, identifies where you're overserving ads to the same people, and recommends frequency cap… | irinabuht12-oss/marketing-skills |
| skill | `good-strategy-bad-strategy` | Formulate and audit real strategy using Richard Rumelt''s "Good Strategy Bad Strategy": an honest diagnosis, a guiding policy, and coherent … | wondelai/skills |
| skill | `google-ads` | Plan, build, and optimize Google Ads campaigns — Search, Shopping, Performance Max, Display, and YouTube — including keyword research, match… | arnabbagxd/Brand-building-skills |
| skill | `google-ads-audit` | Comprehensive Google Ads account health analysis detecting wasted spend, search term leaks, negative keyword gaps, bid strategy issues, and … | irinabuht12-oss/marketing-skills |
| skill | `lead-magnets` | When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the user mentions "lead m… | coreyhaines31/marketingskills |
| skill | `linkedin-ads-audit` | LinkedIn Ads campaign analysis for B2B marketers detecting CTR issues, audience quality problems, lead gen form friction, and budget ineffic… | irinabuht12-oss/marketing-skills |
| skill | `market-ads` |  | zubair-trabzada/ai-marketing-claude |
| skill | `meta-ads` | Plan, build, and optimize Meta advertising campaigns on Facebook and Instagram — campaign structure, audience targeting (core, custom, looka… | arnabbagxd/Brand-building-skills |
| skill | `meta-ads-audit` | Meta/Facebook/Instagram Ads campaign structure analysis detecting creative fatigue, audience overlap, scaling opportunities, and iOS trackin… | irinabuht12-oss/marketing-skills |
| skill | `pacing-monitor` | Tracks daily spend against monthly budget targets across all campaigns and accounts. Tells you exactly where you'll land at current pace, fl… | irinabuht12-oss/marketing-skills |
| skill | `paid-ads` | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platform… | alirezarezvani/claude-skills (marketing) |
| skill | `quality-score-breakdown` | Breaks down Quality Score components for your Google Ads keywords — expected CTR, ad relevance, and landing page experience — and tells you … | irinabuht12-oss/marketing-skills |
| skill | `reddit-ads-audit` | Reddit Ads campaign analysis detecting community targeting issues, creative fatigue, bid inefficiencies, and subreddit performance problems.… | irinabuht12-oss/marketing-skills |
| skill | `retargeting-window-analysis` | Analyzes your conversion lag data to determine the optimal retargeting window for each audience segment. Tells you whether your 30-day retar… | irinabuht12-oss/marketing-skills |
| skill | `roas-forecasting` | Projects your ROAS for the next 30, 60, and 90 days based on current performance trends, seasonality patterns from your historical data, and… | irinabuht12-oss/marketing-skills |
| skill | `search-term-mining` | Analyzes your search term reports across all campaigns and surfaces high-intent terms you're not bidding on yet. Groups them by theme, estim… | irinabuht12-oss/marketing-skills |
| skill | `spacing-system` | Create a spacing scale from a base unit with rules for when each step applies. Use when standardising padding and margins. For page-level co… | Owl-Listener/designer-skills |
| skill | `upload-to-stitch` | Upload local assets (images, mockups, extracted HTML, design markdown) to a Stitch project. ALWAYS use this skill when you need to upload vi… | google-labs-code/stitch-skills |
| skill | `wasted-spend-finder` | Scans your Google and Meta accounts for money being spent on search terms, placements, audiences, and ads that produce zero or near-zero con… | irinabuht12-oss/marketing-skills |
| skill | `weekly-account-summary` | Generates a plain English summary of everything that happened across all your accounts this week. What improved, what declined, what needs i… | irinabuht12-oss/marketing-skills |

## ✍️ Copywriting y contenido (48)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `content-marketer` | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven … | wshobson/agents (content-marketing) |
| 🤖 agente | `content-strategist` | Builds content engines that rank, convert, and compound. Thinks in systems — topic clusters, not individual posts. Every piece earns its pla… | alirezarezvani/claude-skills |
| 🤖 agente | `cs-content-creator` | Long-form marketing content producer orchestrating the content-production skill (research → brief → draft → optimize → gate). Use when conte… | alirezarezvani/claude-skills |
| 🤖 agente | `cs-webinar-marketer` | Webinar & virtual-event marketing specialist agent. Use when planning, promoting, running, or rescuing a webinar, virtual event, live demo, … | alirezarezvani/claude-skills |
| 🤖 agente | `market-content` |  | zubair-trabzada/ai-marketing-claude |
| 🤖 agente | `social-publishing-publisher` | Agent-first social media publishing specialist. Use this agent to schedule and publish posts across 13 platforms (X, LinkedIn, Instagram, Fa… | wshobson/agents (social-publishing) |
| skill | `avoid-ai-writing` | Audit and rewrite prose so it stops reading as machine-generated. Use this skill when asked to remove AI-isms, clean up AI writing, edit a d… | wshobson/agents (avoid-ai-writing) |
| skill | `better-writing` | UX writing and interface copy, from voice and button labels to error messages and empty states. Use when writing or reviewing any user-facin… | boraoztunc/skills |
| skill | `cold-email` | Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, c… | coreyhaines31/marketingskills |
| skill | `community-marketing` | Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a community strategy, gro… | coreyhaines31/marketingskills |
| skill | `contagious` | Engineer word-of-mouth and virality using the STEPPS framework (Social Currency, Triggers, Emotion, Public, Practical Value, Stories). Use w… | wondelai/skills |
| skill | `content-creation` | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use … | anthropics/knowledge-work-plugins (marketing) |
| skill | `content-creator` | Deprecated redirect skill that routes legacy 'content creator' requests to the correct specialist. Use when a user invokes 'content creator'… | alirezarezvani/claude-skills (marketing) |
| skill | `content-humanizer` | Makes AI-generated content sound genuinely human — not just cleaned up, but alive. Use when content feels robotic, uses too many AI clichés,… | alirezarezvani/claude-skills (marketing) |
| skill | `content-production` | Full content production pipeline — takes a topic from blank page to published-ready piece. Use when you need to execute content: write a blo… | alirezarezvani/claude-skills (marketing) |
| skill | `content-repurposer` | Transform one long-form piece into multiple platform-specific content derivatives including LinkedIn posts, tweet threads, email snippets, a… | irinabuht12-oss/marketing-skills |
| skill | `content-strategy` | When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also use when the user me… | coreyhaines31/marketingskills |
| skill | `copy-editing` | When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the user mentions 'edit … | coreyhaines31/marketingskills |
| skill | `copywriting` | When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages, pricing pages, feature pa… | coreyhaines31/marketingskills |
| skill | `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical s… | anthropics/skills |
| skill | `draft-content` | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO … | anthropics/knowledge-work-plugins (marketing) |
| skill | `ecommerce-visual-copywriting` | 将商品资料、包装与资质、目标平台、目标人群和视觉参考转成可直接执行的电商视觉方案，包括转化策略、Campaign Style Lock、主图/详情页/Listing/A+ Storyboard、图内文案、设计说明、生图 Prompt、证据与合规审查。适用于淘宝、天猫、京东、拼多多… | feichanggege/ecommerce-visual-copywriting-skill |
| skill | `email-marketing` | Build and run a full email marketing channel — list building, deliverability, segmentation, newsletter strategy, campaign types, A/B testing… | arnabbagxd/Brand-building-skills |
| skill | `email-sequence` | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when buildi… | anthropics/knowledge-work-plugins (marketing) |
| skill | `email-sequence-writer` | Write complete nurture email sequences with subject lines, preview text, and body copy using proven copywriting formulas. Use when given ICP… | irinabuht12-oss/marketing-skills |
| skill | `emails` | When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when … | coreyhaines31/marketingskills |
| skill | `influencer-marketing` | When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting partners, structur… | coreyhaines31/marketingskills |
| skill | `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use … | anthropics/skills |
| skill | `made-to-stick` | Craft messages that are understood, remembered, and drive action using the SUCCESs checklist (Simple, Unexpected, Concrete, Credible, Emotio… | wondelai/skills |
| skill | `market-copy` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-emails` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-social` |  | zubair-trabzada/ai-marketing-claude |
| skill | `ogilvy` | Apply David Ogilvy's advertising principles when writing or reviewing copy, headlines, product descriptions, landing pages, ads, emails, or … | boraoztunc/skills |
| skill | `public-relations` | When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests). Al… | coreyhaines31/marketingskills |
| skill | `sms` | When the user wants to plan, build, or optimize SMS or MMS marketing — including welcome flows, abandoned cart texts, post-purchase, win-bac… | coreyhaines31/marketingskills |
| skill | `social` | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or o… | coreyhaines31/marketingskills |
| skill | `social-content` | When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram, TikTok, Facebook, or o… | alirezarezvani/claude-skills (marketing) |
| skill | `social-media-analyzer` | Social media campaign analysis and performance tracking. Calculates engagement rates, ROI, and benchmarks across platforms. Use when analyzi… | alirezarezvani/claude-skills (marketing) |
| skill | `social-media-manager` | When the user wants to develop social media strategy, plan content calendars, manage community engagement, or grow their social presence acr… | alirezarezvani/claude-skills (marketing) |
| skill | `social-publishing` | Schedule and publish social media posts across 13 platforms (X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Red… | wshobson/agents (social-publishing) |
| skill | `stop-slop` | Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells and produce more huma… | boraoztunc/skills |
| skill | `ugc-strategy` | Build a User Generated Content (UGC) strategy — getting customers to create content, review generation, UGC briefs for creators, social camp… | arnabbagxd/Brand-building-skills |
| skill | `ux-copy` | Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "rev… | anthropics/knowledge-work-plugins (design) |
| skill | `ux-writing` | Write interface copy — microcopy, error messages, empty states, and CTAs. Use when the words are the deliverable. For content structure and … | Owl-Listener/designer-skills |
| skill | `webinar-marketing` | When the user wants to plan, promote, run, or improve a webinar or virtual event to generate and convert demand. Use when the user mentions … | alirezarezvani/claude-skills (marketing) |
| skill | `whatsapp-marketing` | Build a WhatsApp marketing strategy — WhatsApp Business setup, broadcast campaigns, automated flows, customer service, drip sequences, and c… | arnabbagxd/Brand-building-skills |
| skill | `x-twitter-growth` | X/Twitter growth engine for building audience, crafting viral content, and analyzing engagement. Use when the user wants to grow on X/Twitte… | alirezarezvani/claude-skills (marketing) |
| skill | `youtube-full` | Use when the user needs YouTube transcripts, video search, channel browsing, playlist extraction, or content monitoring. Trigger phrases: 'g… | alirezarezvani/claude-skills (marketing) |

## 🔍 SEO / AEO / IA (28)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `cs-aeo` | Answer Engine Optimization (AEO) specialist agent. Use when content needs to be optimized for citation by AI language models (ChatGPT, Perpl… | alirezarezvani/claude-skills |
| 🤖 agente | `seo-authority-builder` | Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PR… | wshobson/agents (seo-analysis-monitoring) |
| 🤖 agente | `seo-cannibalization-detector` | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use … | wshobson/agents (seo-analysis-monitoring) |
| 🤖 agente | `seo-content-auditor` | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations base… | wshobson/agents (seo-content-creation) |
| 🤖 agente | `seo-content-planner` | Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for co… | wshobson/agents (seo-content-creation) |
| 🤖 agente | `seo-content-refresher` | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need… | wshobson/agents (seo-analysis-monitoring) |
| 🤖 agente | `seo-content-writer` | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. … | wshobson/agents (seo-content-creation) |
| 🤖 agente | `seo-keyword-strategist` | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents o… | wshobson/agents (seo-technical-optimization) |
| 🤖 agente | `seo-meta-optimizer` | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword… | wshobson/agents (seo-technical-optimization) |
| 🤖 agente | `seo-snippet-hunter` | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Us… | wshobson/agents (seo-technical-optimization) |
| 🤖 agente | `seo-structure-architect` | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates sea… | wshobson/agents (seo-technical-optimization) |
| skill | `aeo` | Answer Engine Optimization (AEO) skill — optimize content to be cited by AI language models (ChatGPT, Perplexity, Claude, Gemini, Mistral) a… | alirezarezvani/claude-skills (marketing) |
| skill | `ai-seo` | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user … | coreyhaines31/marketingskills |
| skill | `ai-visibility-audit` | Audit how visible your brand is inside AI answers (ChatGPT, Claude, Gemini, Perplexity, AI Overviews). Claude builds a prompt panel for your… | irinabuht12-oss/marketing-skills |
| skill | `citation-source-gap-finder` | Find the exact pages AI assistants cite when answering questions in your category, and identify which ones you can get into. Claude clusters… | irinabuht12-oss/marketing-skills |
| skill | `content-aeo-optimizer` | Rewrite existing pages so AI assistants can extract, quote, and cite them. Claude restructures your content into answer-ready blocks — direc… | irinabuht12-oss/marketing-skills |
| skill | `directory-submissions` | When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for backlinks, domain rating, a… | coreyhaines31/marketingskills |
| skill | `e2e-seo-assistant` | Full SEO workflow covering technical audits, content gaps, backlink opportunities, on-page fixes, and content briefs. Use when given a site … | irinabuht12-oss/marketing-skills |
| skill | `keyword-cannibalization-check` | Identifies where your own keywords and campaigns are competing against each other in Google Ads auctions. Finds duplicate keywords across ca… | irinabuht12-oss/marketing-skills |
| skill | `local-seo-manager` | Manage local SEO for service-area businesses — appliance repair, HVAC, plumbing, cleaning, and any business that serves customers at their l… | alirezarezvani/claude-skills (marketing) |
| skill | `market-seo` |  | zubair-trabzada/ai-marketing-claude |
| skill | `programmatic-seo` | When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "templ… | coreyhaines31/marketingskills |
| skill | `programmatic-seo-builder` | Create scalable programmatic SEO page templates with title patterns, internal linking logic, schema markup, and thin content avoidance strat… | irinabuht12-oss/marketing-skills |
| skill | `programmatic-seo-playbook` | Replicate the 7 programmatic SEO plays that took Zapier, Clay, Composio, Gamma, Mintlify, HeyGen and HubSpot to #1 in Google and ChatGPT. Us… | irinabuht12-oss/marketing-skills |
| skill | `schema` | When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup… | coreyhaines31/marketingskills |
| skill | `schema-markup` | When the user wants to implement, audit, or validate structured data (schema markup) on their website. Use when the user mentions 'structure… | alirezarezvani/claude-skills (marketing) |
| skill | `seo-audit` | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when asse… | anthropics/knowledge-work-plugins (marketing) |
| skill | `site-architecture` | When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal linking. Also use wh… | coreyhaines31/marketingskills |

## 📈 Estrategia, growth y CRO (124)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `business-analyst` | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI framework… | wshobson/agents (business-analytics) |
| 🤖 agente | `cs-demand-gen-specialist` | Demand generation and acquisition-funnel specialist orchestrating the marketing-demand-acquisition, paid-ads, and email-sequence skills. Use… | alirezarezvani/claude-skills |
| 🤖 agente | `customer-support` | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support e… | wshobson/agents (customer-sales-automation) |
| 🤖 agente | `growth-marketer` | Growth marketing specialist for bootstrapped startups and indie hackers. Builds content engines, optimizes funnels, runs launch sequences, a… | alirezarezvani/claude-skills |
| 🤖 agente | `market-competitive` |  | zubair-trabzada/ai-marketing-claude |
| 🤖 agente | `market-conversion` |  | zubair-trabzada/ai-marketing-claude |
| 🤖 agente | `market-strategy` |  | zubair-trabzada/ai-marketing-claude |
| 🤖 agente | `market-technical` |  | zubair-trabzada/ai-marketing-claude |
| 🤖 agente | `sales-automator` | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales out… | wshobson/agents (customer-sales-automation) |
| 🤖 agente | `search-specialist` | Expert web researcher using advanced search techniques and synthesis. Masters search operators, result filtering, and multi-source verificat… | wshobson/agents (content-marketing) |
| 🤖 agente | `solo-founder` | Your co-founder who doesn't exist yet. Covers product, engineering, marketing, and strategy for one-person startups — because nobody's stopp… | alirezarezvani/claude-skills |
| 🤖 agente | `startup-analyst` | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-st… | wshobson/agents (startup-business-analyst) |
| skill | `ab-test-analyzer` | Statistical significance calculator for A/B test results with sample size requirements, segment breakdowns, and hypothesis generation. Use w… | irinabuht12-oss/marketing-skills |
| skill | `ab-test-setup` | When the user wants to plan, design, or implement an A/B test or experiment. Also use when the user mentions "A/B test," "split test," "expe… | alirezarezvani/claude-skills (marketing) |
| skill | `ab-test-setup-and-analysis` | Designs statistically valid split tests for ads, audiences, landing pages, or bid strategies. Calculates required sample sizes before you st… | irinabuht12-oss/marketing-skills |
| skill | `ab-testing` | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the us… | coreyhaines31/marketingskills |
| skill | `affinity-diagram` | Cluster many qualitative data points into themes and insight statements. Use when synthesising across multiple sessions or sources. For a si… | Owl-Listener/designer-skills |
| skill | `analytics` | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4… | coreyhaines31/marketingskills |
| skill | `analytics-tracking` | Set up, audit, and debug analytics tracking implementation — GA4, Google Tag Manager, event taxonomy, conversion tracking, and data quality.… | alirezarezvani/claude-skills (marketing) |
| skill | `app-store-optimization` | App Store Optimization (ASO) toolkit for researching keywords, analyzing competitor rankings, generating metadata suggestions, and improving… | alirezarezvani/claude-skills (marketing) |
| skill | `app-store-screenshots` | Use when building App Store screenshot pages, generating exportable marketing screenshots for iOS apps, or creating programmatic screenshot … | boraoztunc/skills |
| skill | `aso` | When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO audit,' 'app store optimi… | coreyhaines31/marketingskills |
| skill | `behavioural-analytics` | Read funnels, retention curves, and event data as a designer — separating a design problem from a tracking artefact. Use when handed product… | Owl-Listener/designer-skills |
| skill | `blue-ocean-strategy` | Create uncontested market space using value innovation instead of competing head-to-head. Use when the user mentions "blue ocean", "red ocea… | wondelai/skills |
| skill | `business-name-fit` | Suggest, pick, or vet a business, startup, or product name that stays true to the founder's cultural origin while working professionally in … | alirezarezvani/claude-skills (marketing) |
| skill | `campaign-analytics` | Analyzes campaign performance with multi-touch attribution, funnel conversion analysis, and ROI calculation for marketing optimization. Use … | alirezarezvani/claude-skills (marketing) |
| skill | `campaign-plan` | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when plann… | anthropics/knowledge-work-plugins (marketing) |
| skill | `card-sort-analysis` | Analyse open or closed card sort results into a proposed grouping and label set. Use after running a sort study. For turning that evidence i… | Owl-Listener/designer-skills |
| skill | `churn-prevention` | When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or implement retention strategie… | coreyhaines31/marketingskills |
| skill | `click-test-plan` | Design first-click and click tests for findability and navigation. Use when testing whether people can locate something. For full task-based… | Owl-Listener/designer-skills |
| skill | `co-marketing` | When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities. Use when the user says 'co… | coreyhaines31/marketingskills |
| skill | `cold-start-problem` | Start and scale networked products using Andrew Chen''s "The Cold Start Problem" framework for network effects. Use when the user mentions "… | wondelai/skills |
| skill | `competitive-analysis` | Compare UX patterns, features, strengths, and gaps across rival products. Use when you need to know what others actually do. For deliberatel… | Owl-Listener/designer-skills |
| skill | `competitive-brief` | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sa… | anthropics/knowledge-work-plugins (marketing) |
| skill | `competitive-landscape` | Analyze competition, identify differentiation opportunities, and develop winning market positioning strategies using Porter's Five Forces, B… | wshobson/agents (startup-business-analyst) |
| skill | `competitor-alternatives` | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alte… | alirezarezvani/claude-skills (marketing) |
| skill | `competitor-profiling` | When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions 'competitor profile,' 'com… | coreyhaines31/marketingskills |
| skill | `competitor-teardown` | Systematic competitive analysis covering positioning, messaging hierarchy, objection handling, and CTA strategy from landing page URLs or sc… | irinabuht12-oss/marketing-skills |
| skill | `competitors` | When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alte… | coreyhaines31/marketingskills |
| skill | `conversion-optimization` | Guided journey from a leaking conversion flow - landing page, signup, checkout, or in-app onboarding - to a measured, tested funnel. Orchest… | wondelai/skills |
| skill | `conversion-path-analysis` | Maps out how users move through your funnel from first ad click to conversion. Identifies where the biggest drop-offs happen, which campaign… | irinabuht12-oss/marketing-skills |
| skill | `cro` | When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing… | coreyhaines31/marketingskills |
| skill | `cro-methodology` | Audit websites and landing pages for conversion issues and design evidence-based A/B tests. Use when the user mentions "landing page isnt co… | wondelai/skills |
| skill | `crossing-the-chasm` | Navigate the technology adoption lifecycle from early adopters to mainstream market. Use when the user mentions "crossing the chasm", "beach… | wondelai/skills |
| skill | `customer-research` | When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "t… | coreyhaines31/marketingskills |
| skill | `d2c-marketing` | Build and execute marketing strategy for Direct-to-Consumer (DTC) brands — customer acquisition, retention, email flows, social proof, subsc… | arnabbagxd/Brand-building-skills |
| skill | `diary-study-plan` | Design a diary study — prompts, cadence, duration, participant criteria, and analysis frame. Use when behaviour unfolds over days or weeks. … | Owl-Listener/designer-skills |
| skill | `empathy-map` | Build a Says, Thinks, Does, Feels map for one user or segment. Use when sharing user understanding quickly. For a composite archetype with g… | Owl-Listener/designer-skills |
| skill | `events` | When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows, meetups, dinners, wor… | coreyhaines31/marketingskills |
| skill | `form-cro` | When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms, demo request forms, … | alirezarezvani/claude-skills (marketing) |
| skill | `free-tool-strategy` | When the user wants to build a free tool for marketing — lead generation, SEO value, or brand awareness. Use when they mention 'engineering … | alirezarezvani/claude-skills (marketing) |
| skill | `free-tools` | When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also us… | coreyhaines31/marketingskills |
| skill | `grow-business` | Guided journey from a business with lucky months to a repeatable growth engine that produces a forecast. Orchestrates nine skills phase by p… | wondelai/skills |
| skill | `grow-website` | Guided journey from a website with traffic it under-converts to a research-driven growth engine that captures more leads, persuades more buy… | wondelai/skills |
| skill | `heuristic-evaluation` | Run an expert review against Nielsen's heuristics and domain criteria, with severity ratings. Use when you need findings without recruiting … | Owl-Listener/designer-skills |
| skill | `hundred-million-offers` | Create irresistible offers using the Value Equation, bonus stacking, risk-reversing guarantees, and ethical scarcity. Use when the user ment… | wondelai/skills |
| skill | `icp-research-assistant` | Build detailed B2B buyer personas with pain points, objections, buying triggers, and messaging angles. Use when given a product and market t… | irinabuht12-oss/marketing-skills |
| skill | `improve-retention` | Diagnose and fix retention problems using behavior design (B=MAP). Use when the user mentions "users sign up but dont stick around", "activa… | wondelai/skills |
| skill | `improve-website` | Guided journey from a live website that underperforms to a prioritized, evidence-backed backlog of conversion, usability, message, and speed… | wondelai/skills |
| skill | `influence-psychology` | Apply the seven principles of ethical persuasion (reciprocity, commitment, social proof, authority, liking, scarcity, unity) to product desi… | wondelai/skills |
| skill | `interview-script` | Write a structured interview guide — warm-up, core exploration, and wrap-up. Use before running interviews. For analysing what comes back, u… | Owl-Listener/designer-skills |
| skill | `jobs-to-be-done` | Discover what customers truly need by analyzing the "job" they hire your product to do. Use when the user mentions "customer discovery", "wh… | wondelai/skills |
| skill | `journey-map` | Map one persona's end-to-end experience with stages, touchpoints, emotions, and pain points. Use when improving an existing experience. For … | Owl-Listener/designer-skills |
| skill | `landing-page` | Use when designing or rewriting a high-converting landing page (single-offer page) for SaaS/apps/services. Covers structure, layout patterns… | boraoztunc/skills |
| skill | `landing-page-audit` | Reviews your landing pages against the ads driving traffic to them. Checks for message match between ad copy and page content, CTA clarity, … | irinabuht12-oss/marketing-skills |
| skill | `landing-page-audit-39` | CRO analysis for landing pages evaluating headline clarity, CTA placement, trust signals, mobile friction, and conversion killers. Use when … | irinabuht12-oss/marketing-skills |
| skill | `launch` | When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product … | coreyhaines31/marketingskills |
| skill | `launch-strategy` | When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product … | alirezarezvani/claude-skills (marketing) |
| skill | `market-audit` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-competitors` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-funnel` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-landing` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-launch` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-proposal` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-report` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-report-pdf` |  | zubair-trabzada/ai-marketing-claude |
| skill | `market-sizing-analysis` | Calculate TAM/SAM/SOM for market opportunities using top-down, bottom-up, and value theory methodologies. Use this skill when sizing markets… | wshobson/agents (startup-business-analyst) |
| skill | `marketing-context` | Create and maintain the marketing context document that all marketing skills read before starting. Use when the user mentions 'marketing con… | alirezarezvani/claude-skills (marketing) |
| skill | `marketing-council` | When the user wants multiple expert perspectives on a marketing question — a simulated board of advisors staffed by legendary marketers (Set… | coreyhaines31/marketingskills |
| skill | `marketing-loops` | When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a cadence (weekly, daily,… | coreyhaines31/marketingskills |
| skill | `marketing-ops` | Central router for the marketing skill ecosystem. Use when unsure which marketing skill to use, when orchestrating a multi-skill campaign, o… | alirezarezvani/claude-skills (marketing) |
| skill | `marketing-plan` | When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product. Also use when the user mention… | coreyhaines31/marketingskills |
| skill | `marketing-psychology` | When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when the user mentions 'p… | coreyhaines31/marketingskills |
| skill | `marketing-skills` | Directory and router for the marketing skills library. Use when you need to find the right marketing skill for a task, see what marketing ca… | alirezarezvani/claude-skills (marketing) |
| skill | `marketing-strategy-pmm` | Product marketing skill for positioning, GTM strategy, competitive intelligence, and product launches. Use when the user asks about product … | alirezarezvani/claude-skills (marketing) |
| skill | `mom-test` | Talk to customers without leading them using Mom Test rules: discuss their life not your idea, ask about specifics in the past, and talk les… | wondelai/skills |
| skill | `monetizing-innovation` | Design products and pricing around validated willingness to pay, from Ramanujam & Tacke''s "Monetizing Innovation". Use when the user mentio… | wondelai/skills |
| skill | `negotiation` | Prepare and execute negotiations using tactical empathy, calibrated questions, and the Ackerman method. Use when the user mentions "salary n… | wondelai/skills |
| skill | `offers` | When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, guar… | coreyhaines31/marketingskills |
| skill | `onboarding` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user ment… | coreyhaines31/marketingskills |
| skill | `onboarding-cro` | When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also use when the user ment… | alirezarezvani/claude-skills (marketing) |
| skill | `one-page-marketing` | Build a complete marketing plan covering the full customer journey from stranger to raving fan. Use when the user mentions "marketing plan",… | wondelai/skills |
| skill | `page-cro` | When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing pages, pricing pages, … | alirezarezvani/claude-skills (marketing) |
| skill | `paywall-upgrade-cro` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions… | alirezarezvani/claude-skills (marketing) |
| skill | `paywalls` | When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions… | coreyhaines31/marketingskills |
| skill | `popup-cro` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user me… | alirezarezvani/claude-skills (marketing) |
| skill | `popups` | When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also use when the user me… | coreyhaines31/marketingskills |
| skill | `predictable-revenue` | Build a scalable outbound B2B sales machine with specialized roles (SDR, AE, CSM). Use when the user mentions "outbound sales", "Cold Callin… | wondelai/skills |
| skill | `pricing` | When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'pricing ti… | coreyhaines31/marketingskills |
| skill | `pricing-page` | Use when designing or rewriting a high-converting SaaS pricing page (structure, plan design, copywriting, SEO/AEO, FAQs, layout patterns, ex… | boraoztunc/skills |
| skill | `pricing-strategy` | Design, optimize, and communicate SaaS pricing — tier structure, value metrics, pricing pages, and price increase strategy. Use when buildin… | alirezarezvani/claude-skills (marketing) |
| skill | `product-marketing` | When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'market… | coreyhaines31/marketingskills |
| skill | `prospecting` | When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or local small businesse… | coreyhaines31/marketingskills |
| skill | `qual-quant-triangulation` | Reconcile what the numbers say with what users say, and design the study that settles it rather than restates it. Use when behavioural data … | Owl-Listener/designer-skills |
| skill | `referral-program` | When the user wants to design, launch, or optimize a referral or affiliate program. Use when they mention 'referral program,' 'affiliate pro… | alirezarezvani/claude-skills (marketing) |
| skill | `referrals` | When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy. Also use when the user… | coreyhaines31/marketingskills |
| skill | `research-repository` | Build a repository that makes findings findable, reusable, and cumulative across teams. Use when the same research keeps getting redone. For… | Owl-Listener/designer-skills |
| skill | `research-synthesis` | Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test… | anthropics/knowledge-work-plugins (design) |
| skill | `revops` | When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes. Also use when the user… | coreyhaines31/marketingskills |
| skill | `sales-enablement` | When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also use when the user me… | coreyhaines31/marketingskills |
| skill | `scorecard-marketing` | Build quiz and assessment funnels that generate qualified leads at 30-50% conversion. Use when the user mentions "quiz funnel", "scorecard",… | wondelai/skills |
| skill | `signup` | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup c… | coreyhaines31/marketingskills |
| skill | `signup-flow-cro` | When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the user mentions "signup c… | alirezarezvani/claude-skills (marketing) |
| skill | `startup-financial-modeling` | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early… | wshobson/agents (startup-business-analyst) |
| skill | `startup-metrics-framework` | Track, calculate, and optimize key performance metrics for SaaS, marketplace, consumer, and B2B startups from seed through Series A, includi… | wshobson/agents (startup-business-analyst) |
| skill | `summarize-interview` | Turn one interview transcript into themes, supporting quotes, and action items. Use immediately after a session. For synthesising many sessi… | Owl-Listener/designer-skills |
| skill | `target-audience` | Define a brand's target audience with deep personas, psychographics, and ICP (Ideal Customer Profile). Use when the user says "target audien… | arnabbagxd/Brand-building-skills |
| skill | `team-composition-analysis` | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through … | wshobson/agents (startup-business-analyst) |
| skill | `test-scenario` | Write realistic usability task scenarios with success criteria and facilitation notes. Use when you have a study and need the tasks. For the… | Owl-Listener/designer-skills |
| skill | `usability-test-plan` | Design a usability study — research questions, methodology, participant criteria, metrics, and facilitation guide. Use when planning the stu… | Owl-Listener/designer-skills |
| skill | `user-flow-diagram` | Diagram screen-level paths, decision points, and branch logic. Use when specifying how a feature is traversed. For the emotional end-to-end … | Owl-Listener/designer-skills |
| skill | `user-persona` | Build research-grounded personas with goals, frustrations, and behavioural patterns. Use when decisions need a consistent user reference. Fo… | Owl-Listener/designer-skills |
| skill | `user-research` | Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "resea… | anthropics/knowledge-work-plugins (design) |
| skill | `utm-tracking-generator` | Generate consistent UTM parameters, GA4 event naming, and conversion tracking specs following taxonomy best practices. Use when describing c… | irinabuht12-oss/marketing-skills |

## 💡 Ideas, conceptos y creatividad (14)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art … | anthropics/skills |
| skill | `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores u… | obra/superpowers |
| skill | `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a pos… | anthropics/skills |
| skill | `concept-selection` | Choose between competing concepts against criteria fixed in advance, and record what each rejected concept was testing. Use when several dir… | Owl-Listener/designer-skills |
| skill | `design-brief` | Write a project brief — problem space, constraints, audience, and success criteria. Use at kickoff for one specific project. For long-horizo… | Owl-Listener/designer-skills |
| skill | `design-sprint` | Run a structured 5-day process to prototype, test, and validate product ideas with real users. Use when the user mentions "design sprint", "… | wondelai/skills |
| skill | `design-sprint-plan` | Plan and facilitate a design sprint from challenge framing through prototype testing. Use when compressing discovery into days. For ongoing … | Owl-Listener/designer-skills |
| skill | `marketing-ideas` | When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the user asks for 'marketi… | coreyhaines31/marketingskills |
| skill | `north-star-vision` | Articulate a long-horizon product vision that aligns teams and anchors strategy. Use when direction is contested or absent. For near-term pr… | Owl-Listener/designer-skills |
| skill | `opportunity-framework` | Identify, score, and prioritise design opportunities against impact and effort. Use when there are more ideas than capacity. For framing the… | Owl-Listener/designer-skills |
| skill | `parallel-concepts` | Build several genuinely different solutions to the same problem at once, spread across what the user does rather than how it looks. Use when… | Owl-Listener/designer-skills |
| skill | `slack-gif-creator` | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use … | anthropics/skills |
| skill | `theme-factory` | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set t… | anthropics/skills |
| skill | `wonder-pill` | Turns open-ended requests into things to think WITH instead of answers to accept. Audits the hidden assumptions inside a topic, inverts them… | ara-mkr/Wonder-Pill |

## 🖌️ Diseño UI/UX y visual (158)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `accessibility-expert` | Expert accessibility specialist ensuring WCAG compliance, inclusive design, and assistive technology compatibility. Masters screen reader op… | wshobson/agents (ui-design) |
| 🤖 agente | `design-system-architect` | Expert design system architect specializing in design tokens, component libraries, theming infrastructure, and scalable design operations. M… | wshobson/agents (ui-design) |
| 🤖 agente | `ui-designer` | Expert UI designer specializing in component creation, layout systems, and visual design implementation. Masters modern design patterns, res… | wshobson/agents (ui-design) |
| 🤖 agente | `ui-ux-designer` | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. Specializ… | wshobson/agents |
| 🤖 agente | `ui-visual-validator` | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. Masters screenshot a… | wshobson/agents (accessibility-compliance) |
| skill | `a-b-test-design` | Design an A/B experiment — hypothesis, variants, primary metric, and sample size. Use when a change can be measured quantitatively at scale.… | Owl-Listener/designer-skills |
| skill | `accessibility-audit` | Audit an existing interface against WCAG, producing findings with severity ratings and remediation steps. Use when you have a design or buil… | Owl-Listener/designer-skills |
| skill | `accessibility-compliance` | Implement WCAG 2.2 compliant interfaces with mobile accessibility, inclusive design patterns, and assistive technology support. Use when aud… | wshobson/agents (ui-design) |
| skill | `accessibility-review` | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when … | anthropics/knowledge-work-plugins (design) |
| skill | `accessibility-test-plan` | Plan accessibility testing — assistive technologies, participant criteria, WCAG coverage, and session protocol. Use when scheduling testing … | Owl-Listener/designer-skills |
| skill | `aesthetic-usability` | Apply the Aesthetic-Usability Effect — polished, consistent interfaces are perceived as more usable and forgive minor friction. Use when jus… | Owl-Listener/designer-skills |
| skill | `animation-principles` | Apply animation principles — easing, staging, follow-through — to one specific UI motion. Use when tuning how an animation feels. For produc… | Owl-Listener/designer-skills |
| skill | `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, s… | boraoztunc/skills |
| skill | `banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or … | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `baoyu-design` | Create polished design artifacts as self-contained HTML: UI mockups, interactive prototypes, wireframes, landing pages, dashboards, app scre… | JimLiu/baoyu-design |
| skill | `beautiful-shadows` | Apply exact Tailwind arbitrary shadow utilities for polished, layered neutral elevation. Use when compact cards, controls, panels, popovers,… | boraoztunc/skills |
| skill | `better-accessibility` | Accessibility engineering for product interfaces, from focus states and keyboard support to ARIA, forms, and screen readers. Use when buildi… | boraoztunc/skills |
| skill | `better-colors` | Color systems for digital products, from building and naming a palette to applying it with meaning and verifying contrast. Use when creating… | boraoztunc/skills |
| skill | `better-interface` | Cross-discipline interface review: routes a screen, flow, feature, or product interface to every `better-*` domain skill and consolidates on… | boraoztunc/skills |
| skill | `better-layout` | Layout structure for web interfaces, from grouping and alignment to reading order, progressive disclosure, and adaptive breakpoints. Use whe… | boraoztunc/skills |
| skill | `better-typography` | Web typography from choosing fonts to spacing, wrapping and accessibility. Use when picking or pairing typefaces, configuring variable fonts… | boraoztunc/skills |
| skill | `better-ui` | Design engineering principles for making interfaces feel polished. Use when building UI components, reviewing frontend code, implementing an… | boraoztunc/skills |
| skill | `brutalist-skill` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilit… | Leonxlnx/taste-skill |
| skill | `business-design` | Read financials, map competitive landscapes, and argue design decisions in the language of value. Use when defending design to commercial st… | Owl-Listener/designer-skills |
| skill | `case-study` | Craft a portfolio case study with narrative arc, process evidence, and outcomes. Use when telling a project's story to an external audience.… | Owl-Listener/designer-skills |
| skill | `code-to-design` | Convert frontend code (Vite, React, Angular, Vue, etc.) to a Stitch Design by chaining static HTML extraction, design system extraction, and… | google-labs-code/stitch-skills |
| skill | `color-system` | Build a product colour system — tonal scales, semantic roles, and contrast compliance. Use when defining or rebuilding colour from scratch. … | Owl-Listener/designer-skills |
| skill | `component-spec` | Specify one component — props, states, variants, accessibility, and usage rules. Use when defining a library component. For the reusable doc… | Owl-Listener/designer-skills |
| skill | `conversational-ux` | Design voice and conversational interfaces — dialog flows, error recovery, and persona. Use when the interface speaks and listens rather tha… | Owl-Listener/designer-skills |
| skill | `create-website` | Guided journey from a blank page to a live, high-converting website, built message-first, then design, then conversion. Orchestrates ten ski… | wondelai/skills |
| skill | `critique-affordance` | Critique a rendered screen's affordances — what looks clickable, state visibility, CTA clarity, and action discoverability. Use when reviewi… | Owl-Listener/designer-skills |
| skill | `critique-color` | Critique a rendered screen's colour — contrast ratios, palette coherence, and semantic meaning. Use when reviewing one screen. For a product… | Owl-Listener/designer-skills |
| skill | `critique-composition` | Critique a rendered screen's composition — balance, whitespace, rhythm, and gestalt grouping. Use when a layout feels off but hierarchy is f… | Owl-Listener/designer-skills |
| skill | `critique-information-density` | Critique a rendered screen's density — cognitive load, content prioritisation, scanning patterns, and progressive disclosure. Use when a scr… | Owl-Listener/designer-skills |
| skill | `critique-typography` | Critique a rendered screen's typography — scale usage, readability, consistency, and token compliance. Use when reviewing type on a screen. … | Owl-Listener/designer-skills |
| skill | `critique-visual-hierarchy` | Critique a rendered screen's hierarchy — entry point, eye flow, weight distribution, and emphasis. Use when attention lands in the wrong pla… | Owl-Listener/designer-skills |
| skill | `dark-mode-design` | Adapt an existing palette to dark mode — surface elevation, contrast rebalancing, and desaturation rules. Use when you already have a light … | Owl-Listener/designer-skills |
| skill | `data-visualization` | Select chart types and design data encodings — marks, axes, labels, and accessible chart styling. Use when presenting data graphically. Owns… | Owl-Listener/designer-skills |
| skill | `design` | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corpor… | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `design-critique` | Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do… | anthropics/knowledge-work-plugins (design) |
| skill | `design-debt-audit` | Inventory and prioritise accumulated design inconsistencies across a product. Use when drift has built up over time. For token coverage spec… | Owl-Listener/designer-skills |
| skill | `design-everyday-things` | Apply foundational design principles: affordances, signifiers, constraints, feedback, and conceptual models. Use when the user mentions "why… | wondelai/skills |
| skill | `design-handoff` | Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design to… | anthropics/knowledge-work-plugins (design) |
| skill | `design-impact-reporting` | Communicate design's contribution to business and user outcomes in stakeholder language. Use when reporting results upward. For choosing the… | Owl-Listener/designer-skills |
| skill | `design-md` | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files | google-labs-code/stitch-skills |
| skill | `design-negotiation` | Advocate for design quality, scope, and timeline with partners and leadership using evidence and shared goals. Use in the conversation itsel… | Owl-Listener/designer-skills |
| skill | `design-principles` | Define actionable principles that resolve trade-offs when the team disagrees. Use when the same decisions keep getting relitigated. For a si… | Owl-Listener/designer-skills |
| skill | `design-qa-checklist` | Build a QA checklist for verifying that a build matches the design. Use at implementation review. For the spec engineers build from, use `ha… | Owl-Listener/designer-skills |
| skill | `design-rationale` | Write rationale connecting decisions to user needs, business goals, and principles. Use when a decision needs defending in writing. For a li… | Owl-Listener/designer-skills |
| skill | `design-review-process` | Establish review gates — criteria, checkpoints, and approval flow. Use when work ships without consistent review. For running one individual… | Owl-Listener/designer-skills |
| skill | `design-system` | Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing d… | anthropics/knowledge-work-plugins (design) |
| skill | `design-system-adoption` | Create adoption strategy and enablement materials to drive design system usage. Use when the system exists but teams ignore it. For contribu… | Owl-Listener/designer-skills |
| skill | `design-system-governance` | Define how the system evolves — contribution model, versioning, deprecation, and change management. Use when multiple teams contribute. For … | Owl-Listener/designer-skills |
| skill | `design-system-patterns` | Build scalable design systems with design tokens, theming infrastructure, and component architecture patterns. Use when creating design toke… | wshobson/agents (ui-design) |
| skill | `design-token` | Define and organise tokens for colour, spacing, type, and elevation with naming and usage rules. Use when establishing the token layer. For … | Owl-Listener/designer-skills |
| skill | `design-token-audit` | Audit token usage across a product for coverage, drift, and hard-coded values. Use when tokens exist and you suspect they are being bypassed… | Owl-Listener/designer-skills |
| skill | `documentary-brutalist-agency` | Create or redesign creative agency, production studio, architecture, culture, and portfolio websites with billboard typography, hard black-a… | boraoztunc/skills |
| skill | `documentation-template` | Generate a reusable documentation scaffold for components, patterns, or guidelines. Use when standardising how the system is documented. For… | Owl-Listener/designer-skills |
| skill | `doherty-threshold` | Apply the Doherty Threshold — keep system response under 400ms to preserve user flow. Use when diagnosing perceived slowness or setting a pe… | Owl-Listener/designer-skills |
| skill | `editorial-portfolio-chapters` | Create or redesign creative-studio, agency, photographer, artist, and portfolio websites where project work leads the story. Use for dark ed… | boraoztunc/skills |
| skill | `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make softw… | boraoztunc/skills |
| skill | `error-handling-ux` | Design error prevention, detection, and recovery across a product — message content, placement, and escape routes. Use when errors span mult… | Owl-Listener/designer-skills |
| skill | `experience-map` | Map the full ecosystem of touchpoints, channels, and relationships across a service. Use when the experience spans more than one product. Fo… | Owl-Listener/designer-skills |
| skill | `extract-design-md` | Extract a comprehensive design system (DESIGN.md) directly from frontend source code — React, Vue, Svelte, Angular, plain HTML/CSS, or any w… | google-labs-code/stitch-skills |
| skill | `extract-static-html` | Extract self-contained static HTML from a built web application or React components by inlining CSS and images. Use this skill whenever you … | google-labs-code/stitch-skills |
| skill | `feedback-patterns` | Design confirmations, status updates, and notifications that tell users an action registered. Use when the system must acknowledge success o… | Owl-Listener/designer-skills |
| skill | `fitts-law` | Apply Fitts's Law — target acquisition time depends on size and distance. Use when sizing and positioning controls, especially for touch. Fo… | Owl-Listener/designer-skills |
| skill | `form-design` | Design a form end to end — field order, grouping, validation, and completion. Use when the artifact is a form. For product-wide error strate… | Owl-Listener/designer-skills |
| skill | `generate-design` | Generate new screens from text prompts or images, edit existing screens with prompts and design system tokens, and generate design variants … | google-labs-code/stitch-skills |
| skill | `gesture-patterns` | Design gesture interactions for touch and pointer — swipe, drag, long-press, and their discoverability. Use when input is gestural. For OS-s… | Owl-Listener/designer-skills |
| skill | `glass-dark-ui` | Build dark-mode glassmorphism interfaces with readable contrast, frosted surfaces, and gradient borders using a pseudo-element mask. Use whe… | boraoztunc/skills |
| skill | `gpt-tasteskill` | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide… | Leonxlnx/taste-skill |
| skill | `hallmark` | Anti-AI-slop design skill for greenfield pages, audits, redesigns, and design extraction from URLs or screenshots. Use when the user asks to… | Nutlope/hallmark |
| skill | `handoff-spec` | Write the implementation handoff — measurements, behaviours, assets, states, and edge cases. Use when engineering picks up the work. For ver… | Owl-Listener/designer-skills |
| skill | `hicks-law` | Apply Hick's Law — decision time grows with the number of simultaneous choices. Use when a screen offers too many options at once. For how m… | Owl-Listener/designer-skills |
| skill | `hooked-ux` | Design habit-forming product loops using the Hook Model (Trigger, Action, Variable Reward, Investment). Use when the user mentions "users ar… | wondelai/skills |
| skill | `icon-system` | Specify an icon system — grid, sizing, stroke weight, naming, categories, and implementation. Use when standardising iconography. For broade… | Owl-Listener/designer-skills |
| skill | `illustration-style` | Define an illustration style guide — visual language, colour usage, and application rules. Use when commissioning or standardising illustrat… | Owl-Listener/designer-skills |
| skill | `image-to-code-skill` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply ana… | Leonxlnx/taste-skill |
| skill | `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, e… | boraoztunc/skills |
| skill | `information-architecture` | Design content structure, hierarchy, labelling, and the navigation model. Use when organising what exists. For the UI that exposes it use `n… | Owl-Listener/designer-skills |
| skill | `interaction-design` | Design and implement microinteractions, motion design, transitions, and user feedback patterns. Use when adding polish to UI interactions, i… | wshobson/agents (ui-design) |
| skill | `interface-review` | Interface review of a change rather than a screen: uncommitted work, the current branch, or a pull request. Covers interface quality, not co… | boraoztunc/skills |
| skill | `interfaces-that-feel` | Apply an emotional resonance lens to a UI that is technically correct but flat, prescribing changes at the copy, motion, and interaction lay… | Owl-Listener/designer-skills |
| skill | `jakobs-law` | Apply Jakob's Law — users expect your product to work like the others they already use. Use when deciding whether to innovate on a familiar … | Owl-Listener/designer-skills |
| skill | `kpi-dashboard-design` | Design effective KPI dashboards with metrics selection, visualization best practices, and real-time monitoring patterns. Use this skill when… | wshobson/agents (business-analytics) |
| skill | `law-of-closure` | Apply the Law of Closure — the eye completes implied shapes from partial forms. Use when reducing visual weight by dropping borders or letti… | Owl-Listener/designer-skills |
| skill | `law-of-common-region` | Apply the Law of Common Region — a shared container, background, or border groups elements regardless of spacing. Use when grouping must sur… | Owl-Listener/designer-skills |
| skill | `law-of-continuity` | Apply the Law of Continuity — the eye follows alignment and unbroken paths. Use when sequencing steps, aligning content, or designing carous… | Owl-Listener/designer-skills |
| skill | `law-of-figure-ground` | Apply the Law of Figure-Ground — establish which layer is foreground and actionable versus background. Use when designing modals, overlays, … | Owl-Listener/designer-skills |
| skill | `law-of-proximity` | Apply the Law of Proximity — spatial closeness groups elements more strongly than any other cue. Use when spacing alone must carry grouping.… | Owl-Listener/designer-skills |
| skill | `law-of-similarity` | Apply the Law of Similarity — shared colour, shape, or size signals that elements belong to one category. Use when signalling relationships … | Owl-Listener/designer-skills |
| skill | `layout-grid` | Define a responsive grid — columns, gutters, margins, and breakpoint behaviour. Use when establishing page structure. For the spacing scale … | Owl-Listener/designer-skills |
| skill | `lean-ux` | Apply lean thinking to UX: hypothesis-driven design, collaborative sketching, and rapid experiments instead of heavy deliverables. Use when … | wondelai/skills |
| skill | `loading-states` | Design waiting experiences — spinners, skeletons, optimistic updates, and progressive reveal. Use when content takes time to arrive. For the… | Owl-Listener/designer-skills |
| skill | `localization-design` | Design for multiple languages, writing directions, and cultural contexts — text expansion, RTL mirroring, and locale formats. Use when shipp… | Owl-Listener/designer-skills |
| skill | `manage-design-system` | Manage design systems in Stitch using MCP tools. Includes retrieval of assets, creating/updating design systems in Stitch, and applying them… | google-labs-code/stitch-skills |
| skill | `marketing-demand-acquisition` | Creates demand generation campaigns, optimizes paid ad spend across LinkedIn, Google, and Meta, develops SEO strategies, and structures part… | alirezarezvani/claude-skills (marketing) |
| skill | `mesh-gradient-dark-blue-clean` | Create a futuristic, premium, clean dark-blue mesh-gradient design system across background rendering, hero shell, navigation, floating node… | boraoztunc/skills |
| skill | `metrics-definition` | Define UX metrics and KPIs that connect design decisions to measurable outcomes. Use when choosing what to measure. For presenting the resul… | Owl-Listener/designer-skills |
| skill | `micro-interaction-spec` | Specify one micro-interaction completely — trigger, rules, feedback, loops, and modes. Use when handing a single interaction to engineering.… | Owl-Listener/designer-skills |
| skill | `microinteractions` | Design the small details -- triggers, rules, feedback, loops and modes -- that separate good products from great ones. Use when the user men… | wondelai/skills |
| skill | `millers-law` | Apply Miller's Law — chunk information into groups of about four to fit working memory. Use when grouping fields, menu items, or steps. For … | Owl-Listener/designer-skills |
| skill | `minimal-zine-poster` | Compile a theme, sentence, object, mood, article idea, or photo into a quiet Japanese/Korean zine-style editorial poster — tall aged paper, … | boraoztunc/skills |
| skill | `minimalist-skill` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy sha… | Leonxlnx/taste-skill |
| skill | `mobile-android-design` | Master Material Design 3 and Jetpack Compose patterns for building native Android apps. Use when designing Android interfaces, implementing … | wshobson/agents (ui-design) |
| skill | `mobile-ios-design` | Master iOS Human Interface Guidelines and SwiftUI patterns for building native iOS apps. Use when designing iOS interfaces, implementing Swi… | wshobson/agents (ui-design) |
| skill | `modern-web-design` | Modern web design trends, principles, and implementation patterns for 2024-2025. Use this skill when designing websites, creating interactiv… | freshtechbro/claudedesignskills |
| skill | `motion-system` | Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising moti… | Owl-Listener/designer-skills |
| skill | `navigation-patterns` | Select and design a navigation pattern — tabs, drawer, hierarchy, or hub — matched to product structure and user tasks. Use when choosing ho… | Owl-Listener/designer-skills |
| skill | `nothing-design` | This skill should be used when the user explicitly says "Nothing style", "Nothing design", "/nothing-design", or directly asks to use/apply … | dominikmartn/nothing-design-skill |
| skill | `onboarding-design` | Design the first-run experience — activation path, progressive disclosure, and time to first value. Use for a user's very first session. For… | Owl-Listener/designer-skills |
| skill | `output-skill` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits clea… | Leonxlnx/taste-skill |
| skill | `pattern-library` | Structure a pattern entry — problem context, solution, usage examples, and related patterns. Use when documenting a recurring solution rathe… | Owl-Listener/designer-skills |
| skill | `peak-end-rule` | Apply the Peak-End Rule — a flow is remembered by its most intense moment and its last. Use when designing completion, celebration, or cance… | Owl-Listener/designer-skills |
| skill | `platform-conventions` | Design to iOS and Android conventions — what each OS mandates, where they diverge, and when to unify. Use when shipping native apps. For bre… | Owl-Listener/designer-skills |
| skill | `presentation-deck` | Structure a design presentation for a specific audience and decision. Use when presenting internally. For a portfolio narrative use `case-st… | Owl-Listener/designer-skills |
| skill | `product-proof-saas` | Create or redesign SaaS and AI product landing pages where a real workflow, interface, or deterministic demo is the central proof. Use for p… | boraoztunc/skills |
| skill | `prototype-strategy` | Choose prototype fidelity and method to match the design question and the decision at stake. Use before building a prototype. For what to te… | Owl-Listener/designer-skills |
| skill | `react-native-design` | Master React Native styling, navigation, and Reanimated animations for cross-platform mobile development. Use when building React Native app… | wshobson/agents (ui-design) |
| skill | `readable-measure` | Set line length and measure for comfortable reading across type sizes and breakpoints. Use when tuning body text. Covers measure only — for … | Owl-Listener/designer-skills |
| skill | `redesign-skill` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design s… | Leonxlnx/taste-skill |
| skill | `refactoring-ui` | Audit and fix visual hierarchy, spacing, color, and depth in web UIs. Use when the user mentions "my UI looks off" (or amateur/unprofessiona… | wondelai/skills |
| skill | `responsive-design` | Implement modern responsive layouts using container queries, fluid typography, CSS Grid, and mobile-first breakpoint strategies. Use when bu… | wshobson/agents (ui-design) |
| skill | `screen-reader-testing` | Test web applications with screen readers including VoiceOver, NVDA, and JAWS. Use when validating screen reader compatibility, debugging ac… | wshobson/agents (accessibility-compliance) |
| skill | `search-ux` | Design search — query input, zero results, refinement, and result presentation. Use when users retrieve rather than browse. For browse struc… | Owl-Listener/designer-skills |
| skill | `serial-position-effect` | Apply the Serial Position Effect — first and last items in a sequence are recalled best. Use when ordering menus, lists, and steps. For emph… | Owl-Listener/designer-skills |
| skill | `site-md` | Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop | google-labs-code/stitch-skills |
| skill | `skeuomorphic-ui` | Create skeuomorphic web UI surfaces with layered gradients, stacked inner and outer shadows, reflective gradient borders, micro texture, and… | boraoztunc/skills |
| skill | `slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `soft-skill` | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a webs… | Leonxlnx/taste-skill |
| skill | `stakeholder-alignment` | Build alignment artifacts — responsibility matrices, decision rights, and communication plans. Use when unclear ownership stalls decisions. … | Owl-Listener/designer-skills |
| skill | `state-machine` | Model component behaviour as explicit states, events, and transitions. Use when a component has many interacting states that must be exhaust… | Owl-Listener/designer-skills |
| skill | `steve-jobs-design-review` | Review designs, products, and features with Steve Jobs'' standards: ruthless simplicity, focus, and end-to-end excellence. Use when the user… | wondelai/skills |
| skill | `stitch-loop` | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern | google-labs-code/stitch-skills |
| skill | `stitch-skill` | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — s… | Leonxlnx/taste-skill |
| skill | `survey-design` | Design unbiased survey instruments — question wording, scales, and sampling — to measure attitudes at scale. Use when you need quantitative … | Owl-Listener/designer-skills |
| skill | `taste-design` | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — s… | google-labs-code/stitch-skills |
| skill | `taste-skill` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and shi… | Leonxlnx/taste-skill |
| skill | `team-workflow` | Design the team's operating rhythm — task management, collaboration rituals, and tooling. Use when the day-to-day cadence needs structure. F… | Owl-Listener/designer-skills |
| skill | `teslers-law` | Apply Tesler's Law — every process has irreducible complexity that someone must absorb. Use when deciding whether the product or the user ca… | Owl-Listener/designer-skills |
| skill | `theming-system` | Design theming architecture — brand variants, dark mode, and high-contrast — mapped through token layers. Use when one system must serve mul… | Owl-Listener/designer-skills |
| skill | `top-design` | Create award-winning, immersive web experiences at the level of Awwwards-featured agencies. Use when the user mentions "Awwwards quality", "… | wondelai/skills |
| skill | `typography-scale` | Create a modular type scale with size, weight, and line-height relationships. Use when establishing typographic structure. For line length o… | Owl-Listener/designer-skills |
| skill | `ui-styling` | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, a… | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `ui-ux-pro-max` | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces,… | nextlevelbuilder/ui-ux-pro-max-skill |
| skill | `ux-heuristics` | Evaluate and improve interface usability using heuristic analysis. Use when the user mentions "usability audit", "users are confused", "form… | wondelai/skills |
| skill | `version-control-strategy` | Define version control for design files, components, and libraries — branching, naming, and release. Use when file history is chaotic. For d… | Owl-Listener/designer-skills |
| skill | `visual-design-foundations` | Apply typography, color theory, spacing systems, and iconography principles to create cohesive visual designs. Use when establishing design … | wshobson/agents (ui-design) |
| skill | `visual-hierarchy` | Establish hierarchy through size, weight, colour, spacing, and position so the eye lands in the intended order. Use when composing new work.… | Owl-Listener/designer-skills |
| skill | `von-restorff-effect` | Apply the Von Restorff Effect — the element that differs from its neighbours is the one remembered. Use when a single action must dominate. … | Owl-Listener/designer-skills |
| skill | `wcag-audit-patterns` | Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for … | wshobson/agents (accessibility-compliance) |
| skill | `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS,… | anthropics/skills |
| skill | `web-component-design` | Master React, Vue, and Svelte component patterns including CSS-in-JS, composition strategies, and reusable component architecture. Use when … | wshobson/agents (ui-design) |
| skill | `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX"… | boraoztunc/skills |
| skill | `web-typography` | Select, pair, and implement typefaces for web projects. Use when the user mentions "font pairing", "which typeface", "line height", "respons… | wondelai/skills |
| skill | `wireframe-spec` | Specify wireframe layout — content priority, component placement, and annotation. Use when defining structure before visual design. For grid… | Owl-Listener/designer-skills |
| skill | `zeigarnik-effect` | Apply the Zeigarnik Effect — incomplete tasks stay mentally active. Use when designing progress indicators, saved drafts, and return hooks. … | Owl-Listener/designer-skills |

## 🎞️ Animación y motion (CSS/JS) (20)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `animated-component-libraries` | Pre-built animated React component collections combining Magic UI (150+ TypeScript/Tailwind/Motion components) and React Bits (90+ minimal-d… | freshtechbro/claudedesignskills |
| skill | `animejs` | Anime.js adapter patterns for HyperFrames. Use when writing Anime.js animations or timelines inside HyperFrames compositions, registering an… | boraoztunc/skills |
| skill | `barba-js` | Page transitions library for creating fluid, smooth transitions between website pages. Use this skill when implementing page transitions, cr… | freshtechbro/claudedesignskills |
| skill | `css-animations` | CSS animation adapter patterns for HyperFrames. Use when authoring CSS keyframes, animation-delay based timing, animation-fill-mode, animati… | boraoztunc/skills |
| skill | `css-border-gradient` | Apply subtle gradient-border treatments for premium web surfaces. Use when cards, pricing panels, nav bars, modals, buttons, or hero surface… | boraoztunc/skills |
| skill | `gsap` | GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), positio… | boraoztunc/skills |
| skill | `gsap-scrolltrigger` | Comprehensive skill for GSAP (GreenSock Animation Platform) and ScrollTrigger plugin. Use this skill when creating web animations, scroll-dr… | freshtechbro/claudedesignskills |
| skill | `locomotive-scroll` | Comprehensive skill for Locomotive Scroll smooth scrolling library with parallax effects, viewport detection, and scroll-driven animations. … | freshtechbro/claudedesignskills |
| skill | `lottie` | Lottie and dotLottie adapter patterns for HyperFrames. Use when embedding lottie-web JSON animations, .lottie files, @lottiefiles/dotlottie-… | boraoztunc/skills |
| skill | `lottie-animations` | After Effects animation rendering for web and React applications. Use this skill when implementing Lottie animations, JSON vector animations… | freshtechbro/claudedesignskills |
| skill | `motion-framer` | Modern animation library for React and JavaScript. Create smooth, production-ready animations with motion components, variants, gestures (ho… | freshtechbro/claudedesignskills |
| skill | `progressive-blur` | Create a layered CSS progressive blur (top or bottom) using multiple backdrop-filter masks for depth and softness. Use when asked for “progr… | boraoztunc/skills |
| skill | `react-spring-physics` | Physics-based animation library combining React Spring (spring dynamics, gesture integration, 60fps animations) and Popmotion (low-level com… | freshtechbro/claudedesignskills |
| skill | `reveal-hover-effect` | Build cursor-following spotlight reveals that expose a second aligned image through a soft radial mask. Use for hover-to-color, before-and-a… | boraoztunc/skills |
| skill | `rive-interactive` | State machine-based vector animation with runtime interactivity and web integration. Use this skill when creating interactive animations, st… | freshtechbro/claudedesignskills |
| skill | `scroll-reveal-libraries` | Simple scroll-triggered reveal animations using AOS (Animate On Scroll). Use this skill when building marketing pages, landing pages, or con… | freshtechbro/claudedesignskills |
| skill | `staggered-word-reveal` | Create subtle editorial word-by-word text reveal animations where each word fades and rises into place once it enters the viewport. Use for … | boraoztunc/skills |
| skill | `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session | obra/superpowers |
| skill | `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code | obra/superpowers |
| skill | `waapi` | Web Animations API adapter patterns for HyperFrames. Use when authoring element.animate() motion, Animation currentTime seeking, document.ge… | boraoztunc/skills |

## ⚡ Eficiencia de Claude y metodología (19)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| skill | `caveman` | Ultra-compressed communication mode that cuts output tokens while keeping technical accuracy. Levels: lite, full, ultra and the wenyan varia… | JuliusBrussee/caveman |
| skill | `clean-code-guard` | Review generated or changed production code before it ships, using Clean Code, SOLID, DRY, KISS, YAGNI, and LLM-specific failure-mode checks… | amElnagdy/guard-skills |
| skill | `code-review-excellence` | Master effective code review practices to provide constructive feedback, catch bugs early, and foster knowledge sharing while maintaining te… | wshobson/agents |
| skill | `debugging-strategies` | Master systematic debugging techniques, profiling tools, and root cause analysis to efficiently track down bugs across any codebase or techn… | wshobson/agents |
| skill | `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | obra/superpowers |
| skill | `docs-guard` | Review generated or changed documentation before it ships — READMEs, API references, docstrings, PHPDoc/JSDoc, changelogs, tutorials, and do… | amElnagdy/guard-skills |
| skill | `enhance-prompt` | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context,… | google-labs-code/stitch-skills |
| skill | `executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or… | obra/superpowers |
| skill | `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make… | multica-ai/andrej-karpathy-skills |
| skill | `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-design… | anthropics/skills |
| skill | `prompt-engineer-toolkit` | Turns marketing prompts into tested, versioned production assets: A/B prompt evaluation against structured test cases, immutable prompt vers… | alirezarezvani/claude-skills (marketing) |
| skill | `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable -… | obra/superpowers |
| skill | `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | obra/superpowers |
| skill | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes | obra/superpowers |
| skill | `test-guard` | Review generated or changed test code against universal testing rules before it ships. Best used reactively after an agent writes, edits, ge… | amElnagdy/guard-skills |
| skill | `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and … | obra/superpowers |
| skill | `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI be… | anthropics/skills |
| skill | `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code | obra/superpowers |
| skill | `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment | obra/superpowers |

## 💻 Programación: WordPress, PHP, SQL, CSS, HTML, JS (77)

| Tipo | Nombre | Qué hace | Fuente |
|---|---|---|---|
| 🤖 agente | `backend-architect` | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. Masters REST/GraphQL/gRPC… | wshobson/agents |
| 🤖 agente | `database-architect` | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database archi… | wshobson/agents |
| 🤖 agente | `database-optimizer` | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. Masters advanced indexi… | wshobson/agents |
| 🤖 agente | `frontend-developer` | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern fron… | wshobson/agents |
| 🤖 agente | `frontend-security-coder` | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. Use PROAC… | wshobson/agents |
| 🤖 agente | `javascript-pro` | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. Use PRO… | wshobson/agents |
| 🤖 agente | `legacy-modernizer` | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and… | wshobson/agents |
| 🤖 agente | `performance-engineer` | Expert performance engineer specializing in modern observability, application optimization, and scalable system performance. Masters OpenTel… | wshobson/agents |
| 🤖 agente | `php-pro` | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP … | wshobson/agents |
| 🤖 agente | `sql-pro` | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data mod… | wshobson/agents |
| 🤖 agente | `typescript-pro` | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patt… | wshobson/agents |
| skill | `blueprint` | Use when the deliverable is WordPress Playground Blueprint JSON or a Blueprint bundle, including creating, editing, reviewing, validating sc… | WordPress/agent-skills |
| skill | `database-hana` | Apply SAP HANA database standards for SQL parameterization, in-memory engine optimization, dynamic IN query chunking, column aliasing on joi… | HoangNguyen0403/agent-skills-standard |
| skill | `database-migration` | Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollback procedures. Use when … | wshobson/agents |
| skill | `database-migrations` | Plan additive, zero-downtime schema migrations with rollout, backfill, and rollback awareness. Use when renaming columns, backfilling data, … | HoangNguyen0403/agent-skills-standard |
| skill | `database-mongodb` | Apply MongoDB data-modeling, indexing, and query rules from access patterns. Use when designing schemas, choosing embed vs reference, or tun… | HoangNguyen0403/agent-skills-standard |
| skill | `database-postgresql` | Apply PostgreSQL standards for migrations, indexing, transactions, and ORM boundaries. Use when editing entities, Prisma schema, migrations,… | HoangNguyen0403/agent-skills-standard |
| skill | `database-query-performance` | Diagnose database latency with explain plans, index ownership, and query-shape review. Use when a query is slow, an index is missing, or sca… | HoangNguyen0403/agent-skills-standard |
| skill | `database-redis` | Optimize Redis as cache and coordination infrastructure with TTL, eviction, and latency-aware key design. Use when implementing Redis cachin… | HoangNguyen0403/agent-skills-standard |
| skill | `database-schema-design` | Design relational or document schemas from access patterns, cardinality, and lifecycle. Use when modeling entities, choosing embed vs normal… | HoangNguyen0403/agent-skills-standard |
| skill | `database-transactions` | Define transaction boundaries, locking, and consistency guarantees for multi-step writes. Use when designing atomic operations, retries, ide… | HoangNguyen0403/agent-skills-standard |
| skill | `day-hour-performance-breakdown` | Analyzes performance by day of week and hour of day across your campaigns. Identifies when your ads perform best and worst, recommends ad sc… | irinabuht12-oss/marketing-skills |
| skill | `device-performance-split` | Analyzes how your campaigns perform across mobile, desktop, and tablet. Identifies where device performance diverges significantly and recom… | irinabuht12-oss/marketing-skills |
| skill | `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typog… | anthropics/skills |
| skill | `geo-performance-analysis` | Breaks down campaign performance by geographic location at whatever level matters — country, state, city, DMA, zip code. Flags underperformi… | irinabuht12-oss/marketing-skills |
| skill | `javascript-best-practices` | Idiomatic JavaScript patterns and conventions for maintainable existing code. Use when reviewing or refactoring JavaScript language patterns… | HoangNguyen0403/agent-skills-standard |
| skill | `javascript-language` | Modern JavaScript (ES2022+) patterns for clean, maintainable code. Use when working with modern JavaScript features like optional chaining, … | HoangNguyen0403/agent-skills-standard |
| skill | `javascript-tooling` | Configure development tools, linting, formatting, and test runners for existing JavaScript projects. Use for ESLint, Prettier, Jest, or equi… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-api` | Build REST endpoints with API Resources, Sanctum authentication, and versioned route groups in Laravel. Use when creating JsonResource class… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-architecture` | Enforce core architectural standards for scalable Laravel applications. Use when structuring controllers, service layers, action classes, Fo… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-background-processing` | Build scalable asynchronous workflows using Queues, Jobs, and Events in Laravel. Use when implementing queued jobs, event-driven workflows, … | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-clean-architecture` | Implement Domain-Driven Design with typed DTOs, repository interfaces, and single-responsibility Action classes in Laravel. Use when creatin… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-database-expert` | Optimize Laravel queries with subqueries, joinSub, Redis cache-aside patterns, and read/write connection splitting. Use when writing complex… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-eloquent` | Write performant Eloquent queries with eager loading, reusable scopes, and strict lazy-loading prevention in Laravel. Use when defining mode… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-security` | Harden Laravel apps with Policies for model authorization, Gate-based RBAC, validated mass assignment, and CSRF protection. Use when creatin… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-sessions-middleware` | Configure Redis session drivers, register security-header middleware, and prevent session fixation in Laravel. Use when switching session dr… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-testing` | Write Pest feature tests with RefreshDatabase, mock external services, and create test data with Eloquent Factories in Laravel. Use when add… | HoangNguyen0403/agent-skills-standard |
| skill | `laravel-tooling` | Configure Laravel ecosystem with custom Artisan commands, Vite asset bundling, Pint code styling, and Horizon queue monitoring. Use when cre… | HoangNguyen0403/agent-skills-standard |
| skill | `modern-javascript-patterns` | Master ES6+ features including async/await, destructuring, spread operators, arrow functions, promises, modules, iterators, generators, and … | wshobson/agents |
| skill | `nodejs-backend-patterns` | Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handling, authentication, data… | wshobson/agents |
| skill | `performance-benchmarking` | Compares your key metrics against industry benchmarks for your specific vertical, campaign type, and platform. Tells you where you're ahead,… | irinabuht12-oss/marketing-skills |
| skill | `performance-report` | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use wh… | anthropics/knowledge-work-plugins (marketing) |
| skill | `php-best-practices` | Write PHP following PSR coding standards, SOLID principles, and code-quality guidelines. Use for PHP style, design, refactoring, naming, and… | HoangNguyen0403/agent-skills-standard |
| skill | `php-concurrency` | Implement concurrency and non-blocking I/O in modern PHP. Use when implementing concurrent requests, async processing, or non-blocking I/O i… | HoangNguyen0403/agent-skills-standard |
| skill | `php-error-handling` | Implement modern PHP error and exception handling patterns. Use when implementing exception hierarchies, error handlers, or custom exception… | HoangNguyen0403/agent-skills-standard |
| skill | `php-language` | Apply core PHP language standards and modern 8.x features. Use when working with PHP 8.x features like enums, fibers, readonly properties, o… | HoangNguyen0403/agent-skills-standard |
| skill | `php-security` | PHP-only security standards for database access, password handling, and input validation. Use when securing PHP apps against SQL injection, … | HoangNguyen0403/agent-skills-standard |
| skill | `php-testing` | Write unit and integration tests for PHP applications with PHPUnit and Pest. Use when writing PHPUnit unit tests or integration tests for PH… | HoangNguyen0403/agent-skills-standard |
| skill | `php-tooling` | Configure PHP ecosystem tooling, dependency management, and static analysis. Use when managing Composer dependencies, running PHPStan, or co… | HoangNguyen0403/agent-skills-standard |
| skill | `postgresql-table-design` | Use this skill when designing or reviewing a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performan… | wshobson/agents |
| skill | `service-blueprint` | Map service delivery across frontstage actions, backstage processes, and supporting systems. Use when staff and operations are part of the e… | Owl-Listener/designer-skills |
| skill | `sql-optimization-patterns` | Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow que… | wshobson/agents |
| skill | `tailwind` | Tailwind CSS v4.2 browser-runtime patterns for HyperFrames compositions. Use when scaffolding or editing projects created with `hyperframes … | boraoztunc/skills |
| skill | `tailwind-design-system` | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component… | wshobson/agents |
| skill | `tailwind-v4` | Tailwind CSS v4 conventions for real projects — CSS-first configuration with @theme, automatic content detection, the v3-to-v4 migration dif… | boraoztunc/skills |
| skill | `typescript-advanced-types` | Master TypeScript's advanced type system including generics, conditional types, mapped types, template literals, and utility types for build… | wshobson/agents |
| skill | `woo-guard` | Review generated or changed WooCommerce code — extensions, payment and shipping integrations, checkout customizations, and order/product log… | amElnagdy/guard-skills |
| skill | `wordpress-router` | Use when the user asks about WordPress codebases (plugins, themes, block themes, Gutenberg blocks, WP core checkouts) and you need to quickl… | WordPress/agent-skills |
| skill | `wp-abilities-api` | Use when working with the WordPress Abilities API (wp_register_ability, wp_register_ability_category, /wp-json/wp-abilities/v1/*, @wordpress… | WordPress/agent-skills |
| skill | `wp-abilities-audit` | Audit a WordPress plugin's REST surface and produce a standardized audit document proposing Abilities API registrations. Produces a markdown… | WordPress/agent-skills |
| skill | `wp-abilities-verify` | Verify a WordPress plugin's Abilities API registrations: enumerate abilities, check that callback behavior matches each annotation's claim (… | WordPress/agent-skills |
| skill | `wp-block-development` | Use when developing WordPress (Gutenberg) blocks: block.json metadata, register_block_type(_from_metadata), attributes/serialization, suppor… | WordPress/agent-skills |
| skill | `wp-block-themes` | Use when developing WordPress block themes: theme.json (global settings/styles), templates and template parts, patterns, style variations, a… | WordPress/agent-skills |
| skill | `wp-env` | Use when setting up, configuring, or troubleshooting local WordPress development environments with @wordpress/env (wp-env). Triggers on ment… | WordPress/agent-skills |
| skill | `wp-guard` | Review generated or changed WordPress code — plugins, themes, and blocks — before it ships. Best used reactively after an agent writes, edit… | amElnagdy/guard-skills |
| skill | `wp-interactivity-api` | Use when building or debugging WordPress Interactivity API features (data-wp-* directives, @wordpress/interactivity store/state/actions, blo… | WordPress/agent-skills |
| skill | `wp-patterns` | Pattern: create or update WordPress block patterns (starter pages, templates, template parts, Query Loop layouts), review pattern registrati… | WordPress/agent-skills |
| skill | `wp-performance` | Use when investigating or improving WordPress performance (backend-only agent): profiling and measurement (WP-CLI profile/doctor, Server-Tim… | WordPress/agent-skills |
| skill | `wp-performance-review` | WordPress performance code review and optimization analysis. Use when reviewing WordPress PHP code for performance issues, auditing themes/p… | elvismdev/claude-wordpress-skills |
| skill | `wp-phpstan` | Use when configuring, running, or fixing PHPStan static analysis in WordPress projects (plugins/themes/sites): phpstan.neon setup, baselines… | WordPress/agent-skills |
| skill | `wp-playground` | Use as the WordPress Playground routing wrapper for ambiguous Playground work, local CLI runs with @wp-playground/cli, playground.wordpress.… | WordPress/agent-skills |
| skill | `wp-plugin-development` | Use when developing WordPress plugins: architecture and hooks, activation/deactivation/uninstall, admin UI and Settings API, data storage, c… | WordPress/agent-skills |
| skill | `wp-plugin-directory-guidelines` | Use when reviewing WordPress plugins for GPL compliance, checking license headers or compatibility, evaluating upsell/freemium/trialware pat… | WordPress/agent-skills |
| skill | `wp-project-triage` | Use when you need a deterministic inspection of a WordPress repository (plugin/theme/block theme/WP core/Gutenberg/full site) including tool… | WordPress/agent-skills |
| skill | `wp-rest-api` | Use when building, extending, or debugging WordPress REST API endpoints/routes: register_rest_route, WP_REST_Controller/controller classes, … | WordPress/agent-skills |
| skill | `wp-wpcli-and-ops` | Use when working with WP-CLI (wp) for WordPress operations: safe search-replace, db export/import, plugin/theme/user/content management, cro… | WordPress/agent-skills |
| skill | `wpds` | Use when building UIs leveraging the WordPress Design System (WPDS) and its components, tokens, patterns, etc. | WordPress/agent-skills |

