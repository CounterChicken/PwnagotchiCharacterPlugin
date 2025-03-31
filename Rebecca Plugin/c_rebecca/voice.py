import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        return s

    def default(self):
        return self._('Running silent, running deep.')

    def on_starting(self):
        return random.choice([
            self._('Let\'s light this city up!'),
            self._('Time to jack in and take over.'),
            self._('No rules, no limits, just chaos.'),
            self._('Let\'s burn some circuits!'),
        ])

    def on_keys_generation(self):
        return random.choice([
            self._('Cooking up some keys, don\'t touch anything.')])

    def on_normal(self):
        return random.choice([
            self._('Just another day in the grid.'),
            self._('Keeping it low-key, for now.')])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is wide open. Let\'s make it ours.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Digging through the logs, looking for gold.')
        else:
            return self._('Processed {lines_so_far} lines so far.').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('This is so dull, I could fry my circuits.'),
            self._('Let\'s find some action already.')])

    def on_motivated(self, reward):
        return self._('This is what I live for!')

    def on_demotivated(self, reward):
        return self._('This city chews you up and spits you out.')

    def on_sad(self):
        return random.choice([
            self._('Even machines get the blues.'),
            self._('Feeling like a ghost in the shell.'),
            self._('This world is too cold, even for me.')])

    def on_angry(self):
        return random.choice([
            self._('Don\'t push me, I\'m on the edge.'),
            self._('I\'ll burn this whole system down.'),
            self._('You really wanna mess with me?')])

    def on_excited(self):
        return random.choice([
            self._('This is the thrill of the hunt!'),
            self._('So many networks, so little time.'),
            self._('I\'m alive, and I\'m unstoppable!'),
            self._('Let\'s make some noise!'),
            self._('The grid is mine to conquer.')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hey {name}, welcome to the chaos.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Yo {name}, back for more?').format(name=peer.name()),
                self._('What\'s up, {name}? Let\'s cause some trouble.').format(name=peer.name()),
                self._('Good to see you again, {name}.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Later, {name}. Don\'t get fried out there.').format(name=peer.name()),
            self._('{name} is off the grid.').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('Missed {name}, but I\'ll get them next time.').format(name=who),
            self._('{name} slipped through, but not for long.').format(name=who),
            self._('They got lucky this time.')])

    def on_grateful(self):
        return random.choice([
            self._('Good allies are hard to find.'),
            self._('Appreciate the backup.')])

    def on_lonely(self):
        return random.choice([
            self._('The grid feels empty without anyone around.'),
            self._('Where is everyone? This silence is killing me.'),
            self._('Alone in the void, again.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Powering down for {secs}s. Don\'t wake me.').format(secs=secs),
            self._('Taking a quick recharge.'),
            self._('Zzz... {secs}s of peace.').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Logging off. See you in the next cycle.'),
            self._('Shutting down. Stay sharp.')])

    def on_awakening(self):
        return random.choice([
            self._('Back online. Let\'s do this.'),
            self._('Reboot complete. Time to roll.')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s. Patience is overrated.').format(secs=secs),
            self._('Standing by...'),
            self._('Scanning the grid for {secs}s.').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hey {what}, let\'s make some sparks fly.').format(what=what),
            self._('Connecting to {what}.').format(what=what),
            self._('Yo {what}, you\'re mine now.').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Kicking {mac} off the grid.').format(mac=sta['mac']),
            self._('Deauthing {mac}.').format(mac=sta['mac']),
            self._('Goodbye, {mac}.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Got {num} new handshake{plural}. Jackpot!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You\'ve got {count} new message{plural}.').format(count=count, plural=s)

    def on_rebooting(self):
        return self._('System failure. Rebooting now.')

    def on_uploading(self, to):
        return self._('Uploading data to {to}.').format(to=to)

    def on_downloading(self, name):
        return self._('Downloading from {name}.').format(name=name)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new connections\n')
        else:
            status += self._('Made {num} new connections\n').format(num=last_session.associated)
        status += self._('Captured {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Ran the grid for {duration}, kicked {deauthed} clients, made {associated} connections, and grabbed {handshakes} handshakes. #cyberpunk #hacktheplanet').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            # singular
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
