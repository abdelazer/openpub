# Information Document : Pure HTTP Acquisition #
20/07/2010 v0.1

## Status of this document ##

This document is an information document, which are meant to be a proposed common solution to peripheral issues related to OPDS Spec usage. This document is non-normative; implementing the OPDS spec is not a requirement to use it nor is its implementation required to implement the OPDS protocol.

## Goals ##

The OPDS Specification defines a way to list and discover publications leaving aside issues related to the acquisition flow. Currently, after browsing
through an OPDS Catalog, customers are often redirected to a general-purpose Internet browser to complete an acquisition.
The scenarios proposed by this document should enable customers to perform acquisitions without having to leave the application.

## Environment ##

This document is tailored toward services that provide OPDS endpoints for acquisition but require users to be registered and store their payment information. This is not always the case but seems to applies to the vast majority of services found on the Web.

## Primary Scenario : Acquisition for registered users ##

The primary scenario is nothing more than an HTTP authentication request before acquiring the requested file.

**Prerequisite:** The user already has a valid account set up (including payment information).

**Steps:**
  1. Browsing the store’s OPDS Catalog, the user follows an acquisition URL.
  1. The application sends a GET request to the URL
  1. The store server replies with a 401 (Unauthorized) response with WWW-Authenticate header to enable HTTP authentication.
  1. The application SHOULD ask the user to confirm its credentials to authorize the acquisition
  1. The application resends the GET request with credentials set.
  1. The store performs the acquisition and sends the requested file (200 OK response).


## Scenario 2: Registered, but missing payment information ##

In this scenario, the user’s identity has been confirmed but the store is missing the payment’s information (as with a new user, for example, or invalid or outdated credit card) to perform the acquisition.

**Prerequisite:** The user already has a valid account set up but the payment’s information is either missing or invalid.

**Steps:** (1-5 are the same as the primary case)
> 6. The store sends a 402 response (Payment required) with a Location header set towards a web page where the user can add the missing information.

> 7. The user fills in the required information and sends it back to the server

> 8. The store registers the new info, performs the acquisition and sends the requested file (200 OK response)


## Scenario 3: Unregistered users ##

Registration is a mandatory step for any acquisition.

**Prerequisite:** none

**Steps:** (1-2 are the same as the primary case)
> 3. The store replies with a 401 (Unauthorized) response with WWW-Authenticate header to enable HTTP authentication. An X-OPDS-Register header provides the location of a registration form.

This document doesn’t specify the end of this scenario. The Client could either finish the acquisition in a browser or continue with the steps defined in the primary or secondary scenarios.