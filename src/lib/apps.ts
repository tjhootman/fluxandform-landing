import appsData from '../data/apps.json';

/**
 * The single source of truth for apps is src/data/apps.json (BRIEF §8).
 * Adding a shipped app is one entry there — never hand-written markup.
 */

export const STATUSES = ['concept', 'building', 'beta', 'live', 'archived'] as const;
export type Status = (typeof STATUSES)[number];

export interface App {
  slug: string;
  name: string;
  blurb: string;
  status: Status;
  accent: string;
  appStoreUrl: string | null;
  testFlightUrl: string | null;
}

/** A resolved call-to-action for a card / detail page, or null when the status has none. */
export interface Cta {
  label: string;
  href: string;
}

interface StatusMeta {
  /** Mono status badge label. */
  badge: string;
  /** Given an app, produce its CTA (or null). Derives href from the app's URL fields. */
  cta: (app: App) => Cta | null;
}

/**
 * Closed enum -> badge + CTA (BRIEF §8). Badge label and CTA both derive from status;
 * `live` and `beta` are wired now even though nothing uses them yet, so promoting an
 * app is a one-word edit to `status`.
 */
const STATUS_META: Record<Status, StatusMeta> = {
  concept: { badge: 'Concept', cta: () => null },
  building: { badge: 'In development', cta: () => null },
  beta: {
    badge: 'TestFlight beta',
    cta: (app) => (app.testFlightUrl ? { label: 'Join the beta', href: app.testFlightUrl } : null),
  },
  live: {
    badge: 'On the App Store',
    cta: (app) => (app.appStoreUrl ? { label: 'Download', href: app.appStoreUrl } : null),
  },
  archived: { badge: 'Archived', cta: () => null },
};

export function statusBadge(status: Status): string {
  return STATUS_META[status].badge;
}

export function appCta(app: App): Cta | null {
  return STATUS_META[app.status].cta(app);
}

/** All apps, in authored order. */
export const apps: App[] = appsData as App[];

/** Count for the derived section label (e.g. BUILDING / 04). Never hardcode this. */
export const appCount = apps.length;

export function getApp(slug: string): App | undefined {
  return apps.find((a) => a.slug === slug);
}
