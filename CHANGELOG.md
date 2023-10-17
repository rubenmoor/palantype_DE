Changelog
========================

All version updates imply changes in one or more of the dictionaries
that come with the plugin.
In order to have the dictionaries updated, you have to remove the dictionaries
from your plover before you update the plugin.
This can be achieved by editing/deleting your Plover config file `plover.cfg`.

* `palantype-DE.json`
* `palantype-DE-extra.json`
* `palantype-DE-numbers.json`

1.1.4
------------------------

The anglicisms now have an extra dictionary `palantype-DE-anglicisms.json`.
And they have been removed from the biggest file `palantype-DE.json`.
This allows disabling anglicisms as a intermediate solution for steno code collisions.
The long-term solution will be the resolution of every collision by adding rules and exceptions.

1.1.3
------------------------

Moved the special mode for number input from `B+-` to `NM-`;
i.e. all steno codes from the number mode now begin with `NM-`.
This avoids a couple of collisions based on the fact that `B+-` is
the steno code for "p" and thus fairly common.
