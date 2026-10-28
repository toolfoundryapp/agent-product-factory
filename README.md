# ToolFoundry — zero-cost starter product factory

A working static website with three free digital tools: a freelance-rate calculator and two spreadsheet templates. It uses **no paid APIs, AI subscriptions, database, or backend**. This is a tested product-publishing foundation, **not yet an autonomous AI-agent fleet**.

## Preview locally

```bash
python factory/build.py
python -m unittest discover -s tests -v
python -m http.server 8000 --directory site
```
Visit http://localhost:8000. All links are relative to the site root.

## Publish for £0 upfront

1. Create a free GitHub account (if needed) and a repository. Upload all contents of this folder, including `.github/workflows/build.yml`.
2. Create a free Cloudflare account and connect the repository under **Workers & Pages → Pages**. Choose a static deployment with build command `python factory/build.py` and output directory `site`. Check current free-tier limits and account requirements.
3. Open the assigned `pages.dev` URL. Verify calculator and ZIP download. You must complete third-party account authorisations yourself.
4. The GitHub workflow tests and packages the site on pushes and weekly; **it does not automatically publish new products or perform AI research**. Cloudflare Pages redeploys when the repository changes.

## Revenue experiment (optional)

The initial products are free to establish usefulness. To test demand without paying upfront, manually create a paid digital download listing with a provider such as Gumroad (fees deducted from sales; payment account and identity verification may be required). Do **not** sell the same free pack unchanged as a premium product. Develop a genuinely differentiated paid version, verify its quality and licensing, then replace a product link in `factory/build.py` with the real checkout URL. Do not fabricate testimonials or sales.

## Automation roadmap

- Phase 1 **working**: deterministic product generator, tests, downloadable files, static catalog, CI.
- Phase 2 **not yet implemented**: opportunity research agent with approved inputs and human review of findings.
- Phase 3 **not yet implemented**: AI product-generation agent with quality gates, security checks and controlled publishing. Model inference may incur cost; use a free local model only if you have suitable hardware.
- Phase 4 **not yet implemented**: analytics and checkout integration; requires service connections, privacy updates and consent where applicable.

## Important boundaries

No income is guaranteed. Free tiers have usage caps and may change. The calculator is a planning estimate, not tax advice. CSV files can be opened in spreadsheet applications; inspect formulas and adapt for your jurisdiction. Do not publish generated products without review. Keep secrets out of source control. The static site has no email capture or visitor tracking.
