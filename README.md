# Maths — Exponential E (HTML)

This folder contains a **single static web page**, `index.html`, that explains the mathematical constant **e** and why it is so important in growth, logarithms, calculus, and complex numbers.

The page is presented as a **CJF Hal AI** branded educational note with interactive graphics, a browser favicon, and an **Apple touch icon** for iPhone and iPad home-screen use.

## What the page covers

- **What e is** — the exponential constant, approximately **2.718281828...**
- **How e arises from the limit** — **(1 + 1/n)^n** as **n → ∞**
- **Continuous compounding** — the classic **£1 at 100% interest** explanation
- **Why e is special in calculus** — the unique base for which **d/dx (e^x) = e^x**
- **Exponential comparisons** — how **2^x**, **3^x**, and **e^x** relate to their derivatives
- **Logarithmic differentiation** — worked derivations for general **a^x**, then **2^x**, **3^x**, and **e^x**
- **Euler’s formula** — **e^(iθ) = cos θ + i sin θ**
- **Natural logarithms** — why base **e** is called “natural”
- **Further appearances of e** — growth, decay, probability, and other mathematical settings

## Interactive features

- **Limit slider** showing how **(1 + 1/n)^n** approaches **e**
- **Curve toggles** for exponentials and their derivatives on shared axes
- **Animated unit-circle diagram** for **e^(iθ)**
- **Step** and **snap** controls to move around key angles on the complex plane

## How to view

Open `index.html` in any modern web browser, or publish the folder on **GitHub Pages** and open the site URL.

**iPhone / iPad:** In Safari, tap **Share → Add to Home Screen**. The file `apple-touch-icon.png` is included as a **180 × 180** Apple home-screen icon, and the mobile web app title is set to **Euler e**.

## Assets in this folder

| File | Purpose |
|------|---------|
| `index.html` | Main educational page about **e** |
| `README.md` | Project summary and usage notes |
| `header-logo.svg` | CJF Hal AI header logo used on the page |
| `favicon.svg` | Browser tab icon |
| `apple-touch-icon.png` | **180 × 180** Apple home-screen icon |
| `build_apple_icon.py` | Small helper script used to generate the Apple icon |

## Notes

- The entry file **must** be named **`index.html`** with a **lowercase** `i`. On case-sensitive web servers (typical for **GitHub Pages** and many Linux hosts), `Index.html` is a different path and may not be used as the folder’s default document.
- No build step is required to use the page.
- The page is entirely client-side HTML, CSS, SVG, canvas, and JavaScript.
- The content is intended as a clear visual explanation rather than a full formal treatment.

---

*Educational summary only — intended as an accessible introduction to the constant **e** and its mathematical significance.*
