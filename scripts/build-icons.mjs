// Rasterize the brand SVGs to PNG with sharp.
// Run from repo root:  node scripts/build-icons.mjs
import sharp from 'sharp';

const ink = '#201e1a';

// Single F — the geometric F, on a paper tile. Used for every square single-F
// slot: site favicon, apple-touch, App Store icon, avatar.
const singleFInner = `
  <rect width="32" height="32" fill="#f3efe6"/>
  <g fill="${ink}">
    <rect x="11" y="7" width="4.2" height="18"/>
    <rect x="11" y="7" width="11" height="4.2"/>
    <rect x="11" y="14.3" width="8.2" height="3.8"/>
  </g>`;

// F / F horizontal mark (transparent background) — the distinct primary mark.
const ffInner = `
  <g fill="${ink}">
    <rect x="6" y="6" width="7" height="48"/>
    <rect x="6" y="6" width="32" height="7"/>
    <rect x="6" y="28" width="29" height="7"/>
    <rect x="72" y="6" width="7" height="48"/>
    <rect x="72" y="6" width="32" height="7"/>
    <rect x="72" y="28" width="29" height="7"/>
  </g>
  <path d="M48 54 L62 6" fill="none" stroke="${ink}" stroke-width="4.2"/>`;

const doc = (w, h, viewBox, inner) =>
  `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${viewBox}">${inner}</svg>`;

const png = (w, h, viewBox, inner, out) =>
  sharp(Buffer.from(doc(w, h, viewBox, inner))).png().toFile(out).then(() => console.log('  ' + out));

const jobs = [
  // Site icons
  png(48,   48,   '0 0 32 32', singleFInner, 'public/favicon.png'),
  png(180,  180,  '0 0 32 32', singleFInner, 'public/apple-touch-icon.png'),
  // Brand kit — App Store icon / social avatar (same single F)
  png(1024, 1024, '0 0 32 32', singleFInner, 'brand/app-icon-1024.png'),
  png(512,  512,  '0 0 32 32', singleFInner, 'brand/app-icon-512.png'),
  // Brand kit — horizontal F/F mark (transparent)
  png(1100, 600,  '0 0 110 60', ffInner, 'brand/ff-mark-1100.png'),
];

await Promise.all(jobs);
console.log('icons built.');
