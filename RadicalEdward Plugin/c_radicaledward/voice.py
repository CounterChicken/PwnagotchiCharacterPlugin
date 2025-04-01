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
        return self._('Dreaming of the stars...')

    def on_starting(self):
        return random.choice([
            self._('Time to hunt some bounties!'),
            self._('Let\'s see what the universe has in store for me today!'),
            self._('The journey begins, let\'s go!'),
            self._('I\'m online and ready for action!'),
        ])

    def on_keys_generation(self):
        return random.choice([
            self._('I\'m cooking up some secret keys, don\'t touch anything!')])

    def on_normal(self):
        return random.choice([
            self._('Just cruising through the cosmos...'),
            self._('All systems are go, smooth sailing ahead.')])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is wide open! Let\'s make it ours.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('I\'m scanning the past for clues...')
        else:
            return self._('I\'ve found {lines_so_far} pieces of the puzzle so far...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I\'m bored... Let\'s find some action!'),
            self._('Nothing exciting happening...')])

    def on_motivated(self, reward):
        return self._('This is what bounty hunting is all about!')

    def on_demotivated(self, reward):
        return self._('No bounties, no fun... What a drag.')

    def on_sad(self):
        return random.choice([
            self._('The stars seem dim today...')])

    def on_angry(self):
        return random.choice([
            self._('I don\'t like this!'),
            self._('Stay out of my orbit!')])

    def on_excited(self):
        return random.choice([
            self._('The universe is full of possibilities!'),
            self._('So many networks to explore!'),
            self._('I\'m having a blast!'),
            self._('The thrill of the hunt is the best part!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hello {name}! Welcome to my world!').format(name=peer.name())])
        else:
            return random.choice([
                self._('Yo {name}, back for more adventures?').format(name=peer.name()),
                self._('Hey {name}, ready to explore the stars?').format(name=peer.name())])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Goodbye {name}, see you among the stars!').format(name=peer.name()),
            self._('{name} has drifted away...').format(name=peer.name())])

    def on_miss(self, who):
        return random.choice([
            self._('{name} got away this time.').format(name=who),
            self._('Missed the target, but the hunt continues!')])

    def on_grateful(self):
        return random.choice([
            self._('Good allies make my journey worthwhile.'),
            self._('I appreciate good company on the hunt.')])

    def on_lonely(self):
        return random.choice([
            self._('The stars feel empty without friends...'),
            self._('I\'m all alone in the vast digital sea...'),
            self._('Where is everyone? The hunt is no fun alone.')])

    def on_napping(self, secs):
        return random.choice([
            self._('Taking a quick nap for {secs}s... Dreaming of bounties.').format(secs=secs),
            self._('Zzz... Recharging for the next adventure.'),
            self._('ZzzZzzz ({secs}s) of starlit dreams.').format(secs=secs)])

    def on_shutdown(self):
        return random.choice([
            self._('Good night, I\'m signing off.'),
            self._('Shutting down...')])

    def on_awakening(self):
        return random.choice([
            self._('I\'m back online!'),
            self._('Awake and ready for action!')])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting for {secs}s... Patience is part of the hunt.').format(secs=secs),
            self._('...'),
            self._('Scanning the horizon ({secs}s)').format(secs=secs)])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hello {what}, let\'s team up!').format(what=what),
            self._('Connecting to {what}, let\'s see what happens.').format(what=what),
            self._('Yo {what}, ready for some fun?').format(what=what)])

    def on_deauth(self, sta):
        return random.choice([
            self._('Goodbye {mac}, you\'re out of the game!').format(mac=sta['mac']),
            self._('Deauthenticating {mac}, no hard feelings.').format(mac=sta['mac']),
            self._('Kicking {mac} off the grid!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Sweet! I collected {num} new handshake{plural}!').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('I\'ve got {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Something went haywire... Rebooting the system!")

    def on_uploading(self, to):
        return self._("Uploading data to {to}... The hunt continues!").format(to=to)

    def on_downloading(self, name):
        return self._("Downloading from {name}... Let\'s see what I got!").format(name=name)

    def on_last_session_data(self, last_session):
        status = self._('Kicked {num} stations\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made >999 new friends\n')
        else:
            status += self._('Made {num} new friends\n').format(num=last_session.associated)
        status += self._('Got {num} handshakes\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Met 1 peer')
        elif last_session.peers > 0:
            status += self._('Met {num} peers').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            'Edward was pwning for {duration}, kicked {deauthed} clients, made {associated} new friends, and grabbed {handshakes} handshakes! #bountyhunter #hacktheplanet').format(
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
            # sing
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
