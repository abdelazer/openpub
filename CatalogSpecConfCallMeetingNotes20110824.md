#Summary Notes from August 24 2011 conference call

# Agenda #

  * OPDS 1.1 validation tools https://github.com/zetaben/opds-validator
  * New elements for lending http://groups.google.com/group/openpub/browse_thread/thread/26131de791173572
  * Draft for OPDS Callbacks http://code.google.com/p/openpub/wiki/CallbackSpecDraft

# Attending #

Hadrien Gardeur, Daihei Shiohama, Chris Rowan, Peter Brantley, Raj Kumar

# Open Library Catalog #

Raj said that currently, Open Library supports OPDS full entries and that he would work on navigation feeds too, in order to create a full catalog.

OL will offer a catalog of titles that can be borrowed directly, using indirect acquisition. OL can also quickly support the new callback specification.

One complex issue is: how do we represent links that enable the user to read in the browser ? Since these titles can only be read in a single Web app, should we consider that this is still within the scope of OPDS ? Should we consider that reading in a browser is an "acquisition" ?

Peter & Raj replied that this is most likely the way things will be heading. Hadrien has concernes about the whole "one book, one reading app" thing, and feels that ultimately OPDS should enable "one book, multiple reading apps" instead. A major problem to really enable this is the current state of DRM support for lending.

# Elements for Lending #

Raj is OK with the proposal that Hadrien submitted on the mailing list.

Hadrien believes that we should also tackle the issue of subscription in OPDS 1.2 and that we need two extra elements for this:
  * number of issues for a subscription
  * frequency of publication

Hadrien will submit a proposal for these two elements on the mailing list.