---
name: Lumina Storytelling
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#474554'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#787586'
  outline-variant: '#c8c4d7'
  surface-tint: '#5546d8'
  primary: '#3318b8'
  on-primary: '#ffffff'
  primary-container: '#4c3bcf'
  on-primary-container: '#cac5ff'
  inverse-primary: '#c5c0ff'
  secondary: '#585f6c'
  on-secondary: '#ffffff'
  secondary-container: '#dce2f3'
  on-secondary-container: '#5e6572'
  tertiary: '#6d2900'
  on-tertiary: '#ffffff'
  tertiary-container: '#923a00'
  on-tertiary-container: '#ffbb9c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4dfff'
  primary-fixed-dim: '#c5c0ff'
  on-primary-fixed: '#140067'
  on-primary-fixed-variant: '#3c27c0'
  secondary-fixed: '#dce2f3'
  secondary-fixed-dim: '#c0c7d6'
  on-secondary-fixed: '#151c27'
  on-secondary-fixed-variant: '#404754'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb693'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7a2f00'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  ui-button:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 4rem
  container-max: 1120px
  reading-width: 680px
---

## Brand & Style

The design system is anchored in the concept of "Editorial Quietude." It prioritizes the author's voice and the reader's immersion, positioning the platform as a premium sanctuary for long-form thought and creative expression. The brand personality is intellectual, sophisticated, and deeply intentional.

The visual style is **Minimalist** with a focus on high-end editorial layouts. By utilizing generous white space and a restrained color palette, the UI recedes to allow the content to take center stage. The emotional response should be one of calm focus—evoking the feeling of reading a beautifully typeset physical journal or a high-end digital magazine.

## Colors

The palette centers on a deep, intellectual Indigo that acts as a signal for interaction and brand presence. 

- **Primary:** A vibrant yet deep Indigo (#4C3BCF) used for primary actions, active states, and brand moments.
- **Neutrals:** A sophisticated range of greys. In light mode, surfaces use a soft off-white (#F9FAFB) to reduce glare, while text utilizes a high-contrast charcoal for maximum legibility.
- **Dark Mode:** Transitions to a deep navy-tinted black (#111827) for surfaces, with typography shifting to soft whites and muted greys to maintain the premium, low-strain reading experience.
- **Semantic Colors:** Success, Warning, and Error colors should be desaturated to maintain the sophisticated aesthetic.

## Typography

Typography is the cornerstone of this design system. We use a dual-font strategy to balance classic literary elegance with modern functional clarity.

- **The Serif (Noto Serif):** Reserved for storytelling elements—titles, pull quotes, and chapter headings. It provides the "premium" feel and signals to the user that they are in a reading environment.
- **The Sans (Inter):** Used for all UI chrome, navigation, and body text. While the titles are serif, the body text remains sans-serif to ensure high legibility across all device types and screen resolutions, particularly for long-form reading.

**Note on Body Text:** Line height for body text is intentionally generous (1.6x - 1.8x) to prevent eye fatigue during extended reading sessions.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for content and a fluid approach for containers.

1. **The Reading Column:** All story content is constrained to a 680px centered column. This optimal line length prevents reader fatigue.
2. **The Grid:** A 12-column grid is used for discovery pages and dashboards, with wide 32px gutters to maintain a sense of "air."
3. **The Rhythm:** Spacing follows a strict 4px/8px scale. Large vertical gaps (xl) are encouraged between major sections to emphasize the minimalist aesthetic.
4. **Margins:** Generous page margins (minimum 24px on mobile, up to 80px on desktop) ensure the content never feels cramped against the viewport edges.

## Elevation & Depth

To maintain a sophisticated feel, this design system avoids heavy shadows and garish depth. Hierarchy is established through:

- **Ambient Shadows:** We use very soft, diffused shadows with a slight indigo tint in the shadow color (e.g., `rgba(49, 46, 129, 0.05)`). This makes cards feel like they are floating slightly above the surface rather than sitting on it.
- **Tonal Layers:** In both light and dark modes, depth is primarily communicated by shifting the background color slightly (e.g., a card being slightly lighter/darker than the base canvas).
- **Backdrop Blurs:** For navigation bars and modals, a light backdrop blur (12px) creates a sense of translucency and "glass," maintaining the context of the content beneath.

## Shapes

The shape language is "Softly Geometric." All interactive elements and containers utilize rounded corners to soften the professional typography and make the platform feel approachable.

- **Standard Radius:** 0.5rem (8px) for buttons and inputs.
- **Large Radius:** 1rem (16px) for cards and featured story modules.
- **Extra Large Radius:** 1.5rem (24px) for modals and large surface containers.

Buttons should never be fully pill-shaped unless they are small "tags" or "chips." The 8px radius provides a modern, architectural feel that aligns with the editorial aesthetic.

## Components

### Buttons
- **Primary:** Solid Indigo background with white text. No border. Soft shadow on hover.
- **Secondary:** Transparent background with an Indigo border (1px) or a soft grey background.
- **Text:** No background or border. High-weight sans-serif text.

### Cards
Cards are the primary vehicle for story discovery. They should feature:
- A subtle 1px border (`#E5E7EB`) in light mode.
- A soft ambient shadow.
- Large padding (`2rem`) to give the typography room to breathe.

### Input Fields
- Understated design: A subtle grey border that thickens and changes to Indigo only on focus.
- Backgrounds should be slightly darker than the surface in light mode to provide a clear target.

### Story Modules
Specialized components for the reading experience:
- **Progress Indicator:** A thin Indigo line at the top of the viewport.
- **Floating Action Bar:** A minimalist, translucent bar at the bottom for liking, commenting, or sharing, utilizing the backdrop blur effect.
- **Author Chips:** Small, rounded-full components for tags or author names, using a low-contrast grey background.

### Navigation
Global navigation should be minimalist, using `label-sm` typography for links and maximizing white space to prevent distraction from the main feed.