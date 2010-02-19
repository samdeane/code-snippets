READ ME
=======

The Autolink module saves users from having to manually enter links for commonly used URLs.

The module scans posts for a set of terms. Any term found is optionally replaced with some
other text, and then automatically linked to its corresponding URL.

The module uses Drupal's built in taxonomy feature, so you can organize your terms in a Drupal
vocabulary. Autolink terms are represented with the taxonomy terms in the autolink vocabulary.
The descriptions are used to provide the URL that the term should link to.

Requirements
------------

This module has been tested with the 4.6.x version of Drupal. It will probably work with older
versions - please let me know how you get on if you try it, so that I can update this documentation.


Installation
------------

1.  Copy the autolink folder to the Drupal modules/ directory. Drupal should automatically
    detect the module. Enable the module on the modules' administration page.

2.  Autolink terms are managed as vocabularies within the categories module.

    To get started with Autolink, create a new vocabulary on the
    categories administration page. The vocabulary need not be associated
    with any modules.

3.  Next, you have to setup the input formats you want to use Autolink with.
    At the input formats page select an input format to configure. Select the
    Autolink filter checkbox and press Save configuration. Now select the
    configure filters tab and select the vocabulary and apply other settings.


Usage
-----

This module uses a vocabulary to define a list of terms. When any of these
terms occurs in some node text, a link is added. 

You create autolink items by adding terms to the vocabulary that you created
in step (2) of the installation instructions.

For each term:

-    the title of the term should be the text that should be linked
-    the first line of the description should be the URL to link to
-    an optional second line can contain text to replace the entry with
-    an optional third line can contain text to insert into a rel attribute
-    you can add synonyms - these will be replaced in the same way as the term's title would be

The first line of the taxonomy term's description field is used to define
the URL to link to.

If a second line exists in the description field, it is used as text to
replace the actual term. This allows you to use long terms in the text
(to avoid accidental matching), but have the long term replaced by a shorter
one in the actual rendered output, to make it more readable.

As an example of why replacement text is useful, say we defined a term "Apple", to
be linked to "http://www.apple.com". The danger with this is that an article 
containing the word "Apple" in another context might inappropriately be linked to
the Apple website. We could use a less ambiguous term, like "Apple Computer Inc.", 
but we don't want that text to have to actually appear in all of our articles,
because it is unnecessarily formal. The solution is do match for "Apple Computer Inc."
in the article, but provide a replacement that converts it to "Apple" in the
final output. Now it's unlikely to be matched incorrectly, but the text will still read ok.

Any text placed on the third line will be inserted into a rel="" tag inside the link.
This allows you, for example, to add XFN support to your autolinks.

Notes
-----

I generally use this module to automatically link to names of people, companies and products
that I often refer to in my blog posts.

Linking _every_ instance of a particular word to the same place is obviously a bit of
a blunt tool, and can lead to unexpected results. Many words obviously have more than
one meaning or context, so something that is a product name might also be a company name,
a band name, and a perfectly normal english word!

There are a few ways to get round this problem. One is obviously to only define autolinks for
terms that are totally unambiguous - e.g. Drupal. That's fine, but not that useful.

Another is to use the replacement feature (see the example above in USAGE) so that the actual
terms defined are quite unambigous, but the text that appears to readers still looks normal. So
I might define a term for my friend Kevin Marks, which links to his website, but also define a replacement
which replaces "Kevin Marks" with "Kevin" in the text. Clearly this has a down side too, since I now can't
actually get the text "Kevin Marks" to appear anywhere, it will always be replaced with "Kevin"!

Perhaps the safest solution is to use a prefix (or postfix) for every term which isn't likely to crop up
accidentally. For example, if I make the search term "Alink Kevin Marks", and the replacement "Kevin" then
I still get behaviour that I want, but I can also manually insert the text "Kevin Marks" if I want to - it
won't be replaced by autolink because it doesn't include the prefix. The downside of this approach is that 
the unfiltered text starts looking a bit weird!


Authors
-------

Written by Sam Deane <sam@elegantchaos.com>.
Originally based on a subset of the glossary module by Frodo Looijaard, Gabor Hojtsy, Al Maw, Moshe Weitzman et al.

The latest information on this module can always be found at <http://www.elegantchaos.com/projects/autolink>.