# meetventure.ca — Website Files

Split from the single-file build into a standard structure for GitHub:

```
index.html
style.css
script.js
images/
  meet-patel-headshot.jpg
```

## Publishing with GitHub Pages

1. Create a new repository (or use an existing one) and add these four items to the **root** of the repo — don't nest them in a subfolder unless you're prepared to adjust the Pages settings for it.
2. Commit and push.
3. In the repo, go to **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to `Deploy from a branch`, pick your default branch (usually `main`) and `/ (root)` as the folder.
5. Save. GitHub will give you a URL like `https://yourusername.github.io/your-repo-name/` within a minute or two.

## Using your own domain (meetventure.ca)

If you want the site to load at `meetventure.ca` instead of the github.io URL:

1. In the same **Settings → Pages** screen, enter `meetventure.ca` under **Custom domain** and save. GitHub will add a `CNAME` file to your repo automatically.
2. At your domain registrar, add a `CNAME` DNS record pointing `meetventure.ca` (or `www`) to `yourusername.github.io`.
3. DNS changes can take a few hours to propagate. Once they do, tick **Enforce HTTPS** back in the Pages settings.

## Before you publish

- Replace the placeholder Calendly link in `index.html` — search for `YOUR-LINK-HERE`.
- Market/rate figures embedded in `script.js` (`MARKET_DATA`, `GROWTH_RATES`, `BOC_MEETINGS`, `BOND_YIELDS`) should be refreshed periodically — they were current as of when this build was made, but real estate and rate data move.
- This is marketing material for a mortgage agent — have it reviewed by your Principal Broker before it goes live, per FSRA requirements.
