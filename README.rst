====================
plonetheme.imioapps
====================

Plone 6.1 Classic UI theme for the iMio applications (iA.Délib, GED).

The theme is a Barceloneta child theme. It keeps Bootstrap 5 and adds one
layer of iMio design tokens on top. Bootstrap gives the grid, the modals,
the dropdowns and the tables. The theme does not replace them.


Architecture
============

One distribution holds a base and one skin per application.

``profiles/default``
    The base. It enables the Diazo theme and the compiled base CSS. All
    applications share it.

``profiles/iadelib``, ``profiles/ged``
    One skin per application. A skin adds a small CSS bundle on top of the
    base. Install the base profile and exactly one skin profile per site.

Each skin also has its own browser layer. Use it to register a viewlet or
a template for one application only.


What a skin may change
======================

A skin only redefines CSS custom properties. It cannot recompile
Bootstrap, because the base CSS is compiled once.

A skin owns:

- the accent color and its hover shade;
- the logo and the application icon;
- the workflow state colors;
- the advice colors.

Everything else belongs to the base. If a design needs a skin to change
something outside this list, the change belongs in the base.

**Limit to know.** Bootstrap 5.3 bakes the Sass value of ``$primary``
into components such as ``.btn-primary``. A skin that overrides
``--imio-accent`` therefore reskins the chrome and the parts this theme
writes itself, but not every Bootstrap component. If an application needs
a different accent across all Bootstrap components, that skin needs its
own full compilation of ``theme.scss``. Add a build script for it.


Build
=====

The SCSS sources live in ``src/plonetheme/imioapps/theme/scss``. The
compiled CSS is committed, because Plone serves it directly.

.. code-block:: shell

    cd src/plonetheme/imioapps/theme
    npm install
    npm run build      # compile the base and every skin
    npm run watch      # recompile the base on each change

``scss/theme.scss`` sets the import order. Do not change it. Bootstrap
needs the variables and the maps before the Barceloneta base.

Keep the npm pin of ``@plone/plonetheme-barceloneta-base`` at the same
version as the ``plonetheme.barceloneta`` egg. The two ship the same
markup, and a mismatch gives CSS that does not fit the page.


Diazo files
===========

``theme/index.html`` and ``theme/rules.xml`` are a copy of
plonetheme.barceloneta 3.3.4, with the resource paths changed to
``++theme++imioapps``. The theme owns them so that ``production-css`` in
``manifest.cfg`` serves the iMio stylesheet in place of the Barceloneta
one.

Resync both files when the ``plonetheme.barceloneta`` egg moves to a new
version. A Diazo theme needs its own rules: a ``<theme>`` element on its
own copies no content and renders an empty page.


Fonts
=====

The fonts are self-hosted, not loaded from Google Fonts. Belgian public
sector sites must not send visitor IP addresses to a third party font
service. Drop the font files in ``theme/fonts``. See the README there.


Design source
=============

The tokens come from the iMio design system. Keep ``scss/_tokens.scss``
as the single source of truth and derive every Bootstrap variable from
it in ``scss/_variables.scss``.
