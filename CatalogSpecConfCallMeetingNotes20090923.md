# Summary #

During this meeting we concentrated on interoperability issues. Keith plans to devote more time to OPDS and resolving interop issues over the next few weeks, and Hadrien will initiate a conversation on authentication. Keith and Peter will be demo'ing in Frankfurt the week before SF meeting. There will be an additional call next week on Sept 30th.

# Attendees #

  * Keith
  * Hadrien
  * Peter
  * Steph
  * Liza
  * Tim Jones (Bluefire)
  * Roger Sperberg

# Notes #

Keith:
  * If goal is interop for October, what do we need to address?
  * catalogs are providing something useful, readers can consume
  * Liza can already read Hadrien's feeds

Liza:
  * What i'm consuming is basically stanza style feeds, difficult to switch to new changes
  * would like a feed that doesn't have stanza historical items (?)

Hadrien:
  * feedbooks feed works with OPDS feed and also pre-OPDS
  * we need the right list of metadata for OPDS and link relations
  * even for acquisition, I can do something that would work. It won't support paypal or google checkout

Keith:
  * for O'Reilly's catalog, pre-OPDS catalog would be up, but will develop a new OPDS one
  * won't figure out a middle ground

Hadrien:
  * Is using content negotation, if you ask for Atom, you will get the Atom rather than the XHTML.
  * will render different layout based on user-agent
  * A normal agent will only get OPDS, if stanza, you'll get both: OPDS + legacy

Liza: I won't have to worry about dealing with legacy information.

Keith:
  * (to Hadrien) When you feels that there is consensus is growing, if you implement it, people will follow you.
  * Hadrien's choices are appropriate first-cut for the group.

Hadrien:
  * need to define how we are going to use the most common properties
  * do we use the media type to identify OPDS or not?

Keith:  Is your preference to use the profile?

Hadrien: My preference is to use media type rather than invent something new

Tim seconds this.

Keith: not clear on alternative to the profile

Hadrien:
  * We can use profile if no one is against it, but would have problem with versioning
  * Atom community is against versioning
  * you get request a version from the HTTP header

Keith: Tim, are you in process of implementing catalog reader right now?

Tim:
  * We have a catalog reader that reads Lexcycle feeds. Tricky part is dealing with extra things - acquisition with CRM
  * We could use baseline description that's text only, secondary description in HTML

Keith: Lexcycle catalog are supposed to paginated, should have rel/next

Hadrien:
  * We provided an answer
  * Search results no feedbooks: total number of items etc
  * In the current wiki on metadata, we are talking about atom:summary and dc:description - shoudln't be a problem, dc:description is in text.
  * Use new link relation + new metadata for extensions

Keith: Client implementers may choose to poll the complete entry from its particular URI rather than in a short entry in the feeds. Are there particular things the group should be doing, to inhibit DRM acquisition thing?

Tim: we just need the link would specify what type of DRM and

Keith: here's an epub, it'll cost you 20 dollars and it uses this DRM scheme from Adobe (in the form of the URI)

Hadrien: we haven't decided if we need a link or a new mimetype

Keith: I think it should be a child

Peter: We are thinking the same at IA

Roger: When we're talking DRM, we're saying the book has this particualr version/DRM, but not talking about any aspect of transmission, security & tagging? It's just a description?

Keith: Intention of that link is a refinement based on what you'll eventually going to get. If you succeed in acquiring this, this is what you're going to get

Hadrien: recommends a new mime-type(?)

Keith: we can't implement mime-types ... [missed this bit](I.md)

Tim:it can also be hiding behind an acquisition stream.

Hadrien:agreed.

Keith: We'll need to figure out the correct approach.

Peter: Still committed on doing a lending scenario

Keith: IA should express what they feel what's the cleanest approach

Peter: Long term, we'll not be doing ACS-type lending.

Hadrien: Might want to express DRM free content in the different way

Liza: My reading system isn't going to care, it just needs to know: "can i consume it or not"

Roger: we're using this to distinguish different types of DRM, but not using it to say format?

Keith: We are using the type attribute to describe format.

Roger: mobi comes in non-encrypted, but also secure format. the fact that it's not encrypted, is only part of what we need to consume.

Keith: We might need to be more nuanced in how we describe mobi files

Steph: is it worth listing?

Keith: Hadrien's mobi's are unencrypted and DRM free, so are O'Reilly. We won't do this before October.

Hadrien: not too much of a problem if well described

Tim: Selfishly, we would love to have DRM notation clarified, and price.

Keith: we just specify country code, numeric float/decimal.

Hadrien: It would be up to the reading system to interpret?

Keith: Reading system should interpret this.

Roger: We don't have to solve this issue, it's a currency+code issue.

Keith: ISO4217. Person holding the content expect to be paying in a single currency, this is the one that should be exposed.

Peter: Good first try, we'll see if we run into any problems.

Keith: We are assuming that there aren't any right restrictions for paid content.

Peter: Rights issues in terms of territorial issues?

Hadrien: It should be up to the catalog provider using the user+agent + IP to switch to different listing. This will be complicated when dealing with aggregators.

Keith: we don't need to solve this today, this is currently handled in a complex way today.

Keith: **we are going to have a price element in an OPDS namespace, that's going to have the ISO4217, 3 letter country code as an attribute and the decimal as the value (0.00 or 0,00 is a valid value).**

Hadrien: because we have a single-type attribute, we can't express what's behind the HTML.

Keith: don't know what the right solution is

Liza: my reading system wants to know when I step through that there's epub I can only consuming

Keith: what else is going to make a interop work in October?

Keith and Peter will be talking about this in Frankfurt a week before the meeting.

Hadrien: I can get something ready by then.

Keith: We can get a dev binary too.

Tim: We can have a mobi delivery available through the web interface from the Kindle, but this is not a preferred demo.

Keith: this will be a significantly less techie audience.

Keith hopes to dedicate about an hour a day to OPDS for as long as he can.

Hadrien: one thing we haven't talked about a lot: authentication. We will support basic HTTP Auth, but that's not going to be enough to support feedbooks. Need to have this discussion with other stakeholders, about more advanced authentication methods.

Keith: start an exploratory conversation on the implementers' list?

Hadrien: also working on other extensions, but may be not relevant.

Peter: IA is also interested in auth because of lending profile problem, no solutions yet.

Hadrien: we should probably have a discussion about this.

Peter, Hadrien and Raj will have a conversation on how to handle it.

Keith wants to know why this is important - not a highly critical issue for O'Reilly, need to understand better for other people - hence suggested private list, in case people can't talk about this publicly.

Hadrien: doesn't mind if it's private or not. Have interesting examples that other catalog providers may not have to deal with. **Hadrien will start a conversation on the implementers' list.**

Keith: other important issues to resolve?

Let's meet next week for a touch-base.

Steph will post notes/also a reminder on Monday.