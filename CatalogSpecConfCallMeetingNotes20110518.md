# Agenda #

Discussion about the current proposals for facets and indirect acquisition.


# Attending #

Hadrien Gardeur, Peter Brantley, Patrick Thompson, Daihei Shiohama, Chris Rowan, Tim Jones


# Discussion #

> ## Facets ##

Hadrien mentioned that a first draft was recently posted on the mailing list since everyone seems to agree on the way facets should be handled.

The target is to have a first proposal implemented in the working draft of the full spec for the next call.

Commitments from Tim Jones (Bluefire) and Patrick Thompson (Inkstone) on support in OPDS clients.
For catalog providers, Peter Brantley (Internet Archive) and Hadrien Gardeur (Feedbooks) made a similar commitment.

> ## Indirect Acquisition ##

Tim seems happy with the proposal (important point, since Bluefire is the only app who really tried to deal with this problem so far).
Indirect acquisition is seen as a good trade-off between simplicity (single term, inlined several times) and the kind of information that we need to represent in an OPDS feeds.

Several examples and explanations were posted on the mailing list by Hadrien.

Next step is to write a new draft for the spec.

> ## Mixed feeds ##

Hadrien mentioned that it might be a good idea to add a media parameter to identify if a feed is a Navigation or an Acquisition feed.

This started a discussion about mixed feeds (Navigation + Acquisition) with Tim.

Tim mentioned that some of their content partners previously used mixed feeds in order to speed things up (navigation and featured titles in the same feed).

Hadrien answered that this is not allowed in the current (1.0) spec and that even from a pure latency/speed issue, a separate feed for featured/new/popular titles wouldn't be an issue.

After a fairly long discussion, Tim agreed but mentioned that it'll take some effort to move their content partners (Books-A-Million for example) to a more OPDS 1.0 correct syntax in those feeds.

Patrick and Chris agreed that making sure that we don't have too much fragmentation is the highest priority at this point.

# Conclusion #

The group felt that the current proposals for facets and indirect acquisition are good enough and we should now focus on spec language.

Fragmentation is still a major issue and the group will reach out to a maximum number of clients/catalogs to make sure that we can avoid fragmentation as much as possible.

_End_