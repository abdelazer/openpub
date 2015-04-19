# Summary #

During this meeting we concentrated on two main issues: payments and search.

**Action points:**
  * Keith will post his latest snippet of (paymentgateway) code to the mailing list.
  * Keith will write the description of the shopping cart flow to the actual body of the spec, will write to the mailing list accordingly.
  * Raj to post to the mailing list about labels that would be most useful.
  * Tim to work with Raj on client/aggregator interop.


# Attendees #

  * Raj
  * Tim
  * Keith
  * Paul
  * Steph

# Notes #

## Payment ##

Raj: getting pretty close where we need to show interop. would like to finalise the tags, not enough people on the call to do that.

Keith describes problem: if you intend to give someone an epub doc, you have to say that in a feed, so the client can only read epub knows what it's going to get. the common case as it exists today, if you follow the link the first thing you get is not an epub, but a series of HTML pages until they find the epub, after putting in their credit card info.

Raj: require more feedback from everyone.

Keith: this is the complex case, would like more simpler case - e.g. no one does paypal today but agreed/assume this would be a simpler process.

Raj: should we set a deadline - say, by the end of the week- that we should have the payment gateway info?

Keith: make sure we capture the most common cases today. we describe how that process happens in text, if you want to reference other scenarios, if we want to implement paypal, we talk to paypal about how we can do it.

Tim: what do we do if it's generic html we land on?
Keith: steps would be: the client visits the HTML page, doesn't give money, but links to epub bites
Tim: or gives them money through their proprietary system, end up with epub bites.

Keith: stanza starts you off on this road, will eventually give you the content you need of this content type. We could have a link: this is how it comes at you, it'll come at you in epub. You'd have to look at the content-type. The link may say epub, but the server may serve you html.

At least, three cases:
1) you could just have the epub (it's free)
2) you can pay for this via paypal, if clever enough, do that without a browser
3) this is a shopping cart, let the user walk through it, eventually they'll click on something that gives them the content

Tim: referring to the 3rd case.  Wondering about the case where there may be DRM?

Keith: we should show a second link, but this is a very high burden for catalog implementers. If we are talking about the case where you have to go through the shopping cart - the child element indicates we're going to be a HTML shopping cart.

**Keith will post his latest snippet of code from the chat yesterday to the mailing list.**

Keith: I feel like we go back/forth whether the DRM should be expressed as part of the content type or the mime-type of the link or not, it'll either be a child or an attribute(?)

Raj: the latest suggestion was that the DRM is expressed in the child element, a child of atom:link in OPDS namespace.

Keith: absence of any DRM elements asserts it's DRM free, a presence of a DRM element will have a URI that describes what kind of DRM.

Raj: why is it an attribute rather than a child(?)?

Keith: it's a reference to a resource, to use an attribute rather than a child, but doesn't matter either way.

Raj asks about consistency with DRM and paymentgateway.

Keith: Let's use attributes for both.

Raj: do we need to specify the protocol?

Keith: I think we should write a description of the shopping cart workflow is. Hopefully we have a more generic one that a client can handle. My preference is not to say whether its' http or https.

**Keith will write the description of the shopping cart flow to the actual body of the spec, will write to the mailing list accordingly.**

## Search ##

Keith wants to raise - will raise again on the mailing list - using the catalog to maximise our sales buy-in.  Wonders if there's any thought on what we might want to do to at least allow catalog providers to suggest some UI components? We would enable client to search etc, should there be a bucket for anything stronger. There should be a way of expressing a series of titles, using Atom. If you want to recombine them in a different order, we provide enough metadata for you to do that.

Raj: the order of entries in the atom feed, doesn't have to be sorted in  any particular way, right? Would suggest order by updated date, otherwise aggregators have to look through the whole catalog again everytime there's an update. Would it help if there was an open source viewer for opds feeds -maybe through a proxy, to be able to sort the feed in different ways?

Keith: Yes. if we have a main feed, and a sort - the sort may or may not be interesting. e.g. we gave you the first 25 hot sellers, but a client may want to sort this differently.

Tim: this may be tricky once we introduce pagination.

Keith: I can imagine that's the client's job if they want to do second order sorting. most of these things to do with hierarchy is to give them tiny subset filters. e.g. 15 best sellers, but not all best sellers. Could be the feed that tells this is the set information you can ask for, or it's up to the client to consume everything and deal with it

Raj: This would be hard for a big catalog. how would the client say "i want this in bestseller order"?

Keith: we can describe a few unambiguously, e.g. sorted by dc:issue, atom:updated, title, creator ..
then there are just going to be a few, maybe just best sellers? featured? that we just define: here's the key/value. These are in the existing catalog, we should cater for it.

Raj: since we're not going to have the stanza hierarchy, would this be rel links in the feed?

Keith: this is the crux of the problem. how does the sophisticated publisher indicate other ways you can slice/dice the feed?

Tim: can do it in a similar way that google search handle suggested subjects.

[discusison around how google search does this](missed.md)

Keith: i'm interested in order and grouping.

Raj: Too bad open search hasn't got anything to handle search order.

Keith: there are extensions that do about 80%.

Raj: we can write our own.

keith: if we have had another month, that's probably what we would have done.

Raj: maybe we should send the email around.

Keith: if you had to abandon the hierarchy, how would you want to express/get people to show your catalog?

Raj: probably the most useful way, if a client has a good interface, author/title - we have both most downloaded, the recents. we put this up for crawlers. being able to sort by tag, by category  or by subject. this is hard to do, most publishers use different subject heading.

Keith: the client could know the most common cases and do some consistent UI in the labelling. if we can agree on a consistent way of labelling them ...

Raj: maybe there should be some rel links, by title (alphabetical), by author (alphabetical), publication date.

Keith: would love another take on this.

**Raj to post to the mailing list about labels that would be most useful.**

## Miscellaneous ##

Tim: what is it about the spec that prohibits us from setting up multi-level feeds ala Lexcycle.

Keith: that was documented as a consensus: hierarchy was attractive but had too many costs, we'll try to make this into a single consolidated feed. Consolidated feeds makes it easier for catalog providers, but end up in more sophisticated clients.

Tim: would be difficult if you implement the pagination part but not the search part.

Raj is looking for an client to work with as an aggregator. Will have discussion with Tim offline.

Keith will be publishing feeds soon that's closer to OPDS spec. Will have to leave the current Stanza feeds.

We should document the IDs don't change.

Raj: another suggested sort order would be by publisher.

Keith: this should be in the list.

Tim: are we suggest a predesigned set that everyone would use?

Keith: suggest we go live with a set, and a mechanism for defining more.