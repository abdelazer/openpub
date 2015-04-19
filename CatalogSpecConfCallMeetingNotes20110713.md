# Agenda #

  * OPDS 1.1 adoption & documentation
  * spec reorganization: http://groups.google.com/group/openpub/browse_thread/thread/55a755a1114a5e74
  * opds:// scheme: http://groups.google.com/group/openpub/browse_thread/thread/79a64d4890c79683
  * callbacks: http://groups.google.com/group/openpub/browse_thread/thread/fffa62a5ca3134db
  * (if we have enough time) JSON serialization


# Attending #

Hadrien Gardeur, Tim Jones, Patrick Thompson

# OPDS 1.1 Adoption & Documentation #

Hadrien said that Feedbooks already supports both facets & indirect acquisition.

Tim expect Bluefire Reader to support indirect acquisition in the next 2-4 weeks, and BFR already support facets.

Patrick will most likely update his apps (MegaReader, QuickReader) in September-October.

# Spec Reorganization #

Tim & Patrick agree on the overall reorganization but they haven't read the mail about it in details.

Hadrien will contact Keith who did most of the work on the 1.0 spec to gather his thoughts about it.

# opds:// scheme #

Hadrien mentioned that Feedbooks already added support for this new scheme on a new page: https://www.feedbooks.com/catalog

Both Tim & Patrick are excited about this and will add support for the opds:// scheme in their apps.

Patrick mentioned an issue on iOS when multiple applications register the same scheme, but based on Tim experience, this shouldn't be a problem and he's aware of other applications who do the same thing.

To kickstart things, Hadrien would like to create a new page on the official OPDS website linking to valid OPDS 1.0 catalogs using the new scheme. Tim will provide links to various international retailers' OPDS catalogs, while Patrick will help with free catalogs.

The big picture here, is that we could create a real directory & search engine for OPDS catalogs that would be hosted by the IA in the future.
Such a website would encourage more diversity in the ecosystem.

# Callbacks #

Multiple questions from Tim & Patrick.

Tim thought that the callback would be a simple URL with all the information in it. Hadrien replied that the callback would be a URL to an OPDS catalog entry rather than just a URL. Tim is slightly worried that this would be an issue for the retailers that they support since they all use static files. Hadrien replied that this should be fairly easy: a single endpoint generating a dynamic callback would be good enough, no need to generate entirely a dynamic catalog.

Patrick asked Hadrien if the entry returned in the callback would provide metadata such as cover etc. Hadrien replied that the entry returned in the callback would be a normal OPDS entry including all the expected metadata. The only requirement will be a direct link to the publication without any kind of authentication (Basic Auth or OAuth). A hash will be required to avoid multiple authentications.

Hadrien mentioned that it'll be up to the client to decide how exactly things are handled, post-callback. They can automatically start downloading the publication or ask the user which format they'd like to use if there are multiple formats.

Hadrien feels that callbacks, both for native apps and web apps should have their own spec document.

We'll have to invite devs working on web apps (Joseph Pearson, Keith Fahlgren) to move forward.