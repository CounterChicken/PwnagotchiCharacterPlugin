# Pwnagotchi Character Switcher Plugin

This plugin lets you easily switch your Pwnagotchi's **character** — including **face** and **voice** — with a single click through the web interface.

## Features

- Switch between different character personalities directly from the web UI.
- Simple plugin and character folder structure for easy setup.

## Character Preview

<table>
  <tr>
    <td align="center"><strong>Pwan Girl</strong></td>
    <td align="center"><strong>BoyKisser</strong></td>
    <td align="center"><strong>Bat Trinity</strong></td>
    <td align="center"><strong>Motoko</strong></td>
    <td align="center"><strong>Rebecca</strong></td>
  </tr>
  <tr>
    <td><img src="Pwan%20Girl%20Plugin/c_pwangirl/AWAKE.png" alt="Pwan Girl Preview" width="120"/></td>
    <td><img src="BoyKisser%20Plugin/c_boykisser/AWAKE.png" alt="BoyKisser Preview" width="120"/></td>
    <td><img src="Bat%20Trinity%20Plugin/c_battrinity/AWAKE.png" alt="Bat Trinity Preview" width="120"/></td>
    <td><img src="Motoko%20Plugin/c_motoko/AWAKE.png" alt="Motoko Preview" width="120"/></td>
    <td>
      <img src="Rebecca%20Plugin/c_rebecca/AWAKE.png" alt="Rebecca Preview" width="120"/><br/>
      <sub>Character by <a href="https://github.com/Zerodya" target="_blank">Zerodya</a></sub>
    </td>
  </tr>
</table>

## Structure

Each character consists of:

- **Plugin file** (e.g., `motoko.py`)
- **Character folder** (e.g., `c_motoko`)

## Installation Guide


[Youtube Video!](https://youtu.be/TjxbPM8c2LU)

I made this "scrappy" tutorial that explains how to install and use the character switcher plugin.

Please note: English is not my native language, thanks for your understanding.

## In short:

1. **Save the plugin file**

   Copy your plugin file (e.g., `motoko.py`) to the Pwnagotchi plugin directory:

   ```bash
   /usr/local/share/pwnagotchi/custom-plugins/

2. **Add the character folder**

   Save the character folder in the root directory:

   ```
   /c_motoko
   ```

   You can use FileZilla or any other SCP/SFTP tool to transfer the files.

3. **Enable the plugin**

   Either via the web UI:

   ```
   http://10.0.0.2:8080/plugins
   ```

   Or by editing your `config.toml`:

   ```
   main.plugins.motoko.enabled = true
   ```

4. **Restart your Pwnagotchi**

   After a reboot, the new face and voice should be active.


   ## Notes

This setup works for all character plugins that follow the same structure. You can create your own characters by providing a plugin file and a matching folder with images and voice files.

## Alternative Usage Without This Plugin

If you want to use the characters (face) without this plugin, you can manually apply the faces using the Face Plugin from this repository:

[https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)

## Credits

- **Rebecca** by [Zerodya](https://github.com/Zerodya) !


