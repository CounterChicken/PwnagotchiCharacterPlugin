Every character plugin consists of a plugin file and a character folder.

Example for the Motoko plugin:
Plugin file -> motoko.py
Character folder -> c_motoko


Save the plugin file motoko.py in the plugin folder:
/usr/local/share/pwnagotchi/custom-plugins/

And the character folder in the root directory:
/c_motoko

For this i use FileZilla. You can do this with all character plugins.


Activate the plugin in your browser under:
http://10.0.0.2:8080/plugins
or in your config.toml:
main.plugins.motoko.enabled = true

Restart your Pwnagotchi and the face and voice should be changed.

