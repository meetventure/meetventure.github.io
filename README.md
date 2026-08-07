# meetventure.ca - Website Files

Split from the single-file build into a standard structure for GitHub:

```
index.html
style.css
script.js
images/
  image.jpg
```

## Publishing with GitHub Pages

1. Create a new repository (or use an existing one) and add these four items to the **root** of the repo - don't nest them in a subfolder unless you're prepared to adjust the Pages settings for it.
2. Commit and push.
3. In the repo, go to **Settings -> Pages**.
4. Under **Build and deployment**, set **Source** to `Deploy from a branch`, pick your default branch (usually `main`) and `/ (root)` as the folder.
5. Save. GitHub will give you a URL like `https://yourusername.github.io/your-repo-name/` within a minute or two.

## Using your own domain (meetventure.ca)

If you want the site to load at `meetventure.ca` instead of the github.io URL:

1. In the same **Settings -> Pages** screen, enter `meetventure.ca` under **Custom domain** and save. GitHub will add a `CNAME` file to your repo automatically.
2. At your domain registrar, add a `CNAME` DNS record pointing `meetventure.ca` (or `www`) to `yourusername.github.io`.
3. DNS changes can take a few hours to propagate. Once they do, tick **Enforce HTTPS** back in the Pages settings.

## Making future edits

The code has inline comments throughout `script.js` explaining what each section does and where to make common changes (adding a blog post, updating CMHC rates, adding a document checklist scenario, etc.) - if you're not sure where something lives, search for it there first. A few starting points:

- **Blog posts**: search `BLOG_POSTS` near the top of `script.js`.
- **Mortgage Diaries case studies**: search `CASE_STUDIES` - shows 4 at a time with page numbers underneath; change `CASES_PER_PAGE` if you want a different count.
- **Document checklist scenarios**: search `DOC_SCENARIOS`.
- **CMHC insurance rates / suggested starting rate**: search `cmhcRate` and `suggestedRate` - every calculator on the site shares these two functions, so updating them here updates everywhere at once.
- **Ontario coverage map regions**: search `const REGIONS` - each entry has a note on keeping new circles inside the map's visible area so nothing gets clipped at the edge.

## Mobile

The site includes a phone-specific hamburger menu (shows automatically under 920px width) and a dedicated mobile CSS section at the bottom of `style.css` covering touch-target sizing, spacing, and layout for phones and small tablets. If something looks off specifically on a phone (and not on desktop), check that section first.

## Before you publish

- Replace the placeholder Calendly link in `index.html` - search for `YOUR-LINK-HERE`.
- Market/rate figures embedded in `script.js` (`MARKET_DATA`, `GROWTH_RATES`, `BOC_MEETINGS`, `BOND_YIELDS`) should be refreshed periodically - they were current as of when this build was made, but real estate and rate data move.
- This is marketing material for a mortgage agent - have it reviewed by your Principal Broker before it goes live, per FSRA requirements.
