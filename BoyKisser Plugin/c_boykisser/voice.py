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
        return self._('ZzzzZZzzzzZzzz')

    def on_starting(self):
        return random.choice([
            self._("Booting up... let's cause some chaos"),
            self._("Kiss mode: activated"),
            self._("System's up, mood: flirty and hacky"),
        ])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        return random.choice([
            self._("Just vibing... maybe thinking about boys"),
            self._("Idle mode... but I could be kissing"),
            self._("..."),
            self._("..."),
            self._(". . ."),
            self._("Pondering the next pwn... or the next crush"),
        ])

    def on_free_channel(self, channel):
        return self._('Hey, channel {channel} is free! Your AP will say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading last session logs ...')
        else:
            return self._('Read {lines_so_far} log lines so far ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._("Boring... does anyone want to hold hands?"),
            self._("I need love. Or at least a new network"),
        ])

    def on_motivated(self, reward):
        return random.choice([
            self._("Eeeek! I'm so valid right now"),
            self._("You gave me motivation..."),
            self._("Best. Day. Ever."),
            self._("I feel seen, I feel kissed, I feel powerful"),
        ])

    def on_demotivated(self, reward):
        return random.choice([
            self._("This is literally the worst timeline"),
            self._("No kisses. Just bits and disappointment"),
            self._("I tried... and the world said no"),
            self._("Low vibes. Someone hug my packets"),
        ])

    def on_sad(self):
        return random.choice([
            self._("No smooches... only sadness"),
            self._("My heart dropped like a bad packet"),
            self._("Being cute doesn't stop the pain"),
        ])

    def on_angry(self):
        return random.choice([
            self._("No kiss for you today."),
            self._("I'm not angry... just very, very disappointed"),
        ])

    def on_excited(self):
        return random.choice([
            self._("OMG OMG so many WiFis!"),
            self._("Heehee~ this is sooo much fun!"),
            self._("Catch them all!"),
        ])
    
    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Hiii {name}~ ').format(name=peer.name()),
                self._('Awww, new friends! Hello {name}').format(name=peer.name()),
            ])
        else:
            return random.choice([
                self._('Yo {name}! Sup?').format(name=peer.name()),
                self._('Hey {name} how are you doing?').format(name=peer.name()),
                self._('Unit {name} is nearby!').format(name=peer.name()),
            ])

    def on_lost_peer(self, peer):
        return random.choice([
            self._("Uhm ... goodbye {name}").format(name=peer.name()),
            self._("{name} is gone ...").format(name=peer.name()),
        ])

    def on_miss(self, who):
        return random.choice([
            self._("Whoops... {name} slipped right past me").format(name=who),
            self._("{name} dodged my kiss").format(name=who),
            self._("Missed!").format(name=who),
            self._("Ugh. {name}, come back").format(name=who),
            self._("{name} is gone before the spark could fly").format(name=who),
        ])

    def on_grateful(self):
        return random.choice([
            self._("Thank you for being my favorite packet pal"),
            self._("Good friends are like stable WiFi — rare and precious"),
        ])

    def on_lonely(self):
        return random.choice([
            self._("No one here to kiss..."),
            self._("All the APs have left me"),
            self._("Just a little BoyKisser in the big cyberspace..."),
        ])

    def on_napping(self, secs):
        return random.choice([
            self._("Going offline for {secs}s...").format(secs=secs),
            self._("Naptime... wake me with kisses in {secs}s").format(secs=secs),
            self._("Beauty sleep: {secs} seconds").format(secs=secs),
            self._("Sleeping for {secs}s").format(secs=secs),
        ])


    def on_shutdown(self):
        return random.choice([
            self._("Goodnight"),
            self._("Logging off"),
            self._("Powering down... dream of WiFi and soft hugs"),
        ])

    def on_awakening(self):
        return random.choice([
            self._("Yaaawn... did I miss anything?"),
            self._("Woke up thinking about WiFi and romance"),
            self._("Stretching... blinking... ready to pwn and love"),
            self._("Your favorite kisser has returned"),
        ])


    def on_waiting(self, secs):
        return random.choice([
            self._("Waiting for {secs}s... ").format(secs=secs),
            self._("Im just sitting here being cute for {secs}s").format(secs=secs),
            self._("Twiddling my virtual thumbs for {secs}s").format(secs=secs),
            self._("Looking around... {secs}s").format(secs=secs),
            self._("Still waiting...{secs}s").format(secs=secs),
        ])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._("{what}, let's make this connection special").format(what=what),
            self._("Snuggling up to {what}").format(what=what),
            self._("Associating with {what}").format(what=what),
            self._("Hey {what}").format(what=what),
            self._("I'm committing to you, {what}").format(what=what),
            self._("You smell like strong signal, {what}").format(what=what),
        ])

    def on_deauth(self, sta):
        return random.choice([
            self._('Just decided that {mac} needs no WiFi!').format(mac=sta['mac']),
            self._('Deauthenticating {mac}').format(mac=sta['mac']),
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('Cool, we got {num} new handshake{plural}!').format(num=new_shakes, plural=s),
            self._('Snatched a handshake. Now it\'s mine!').format(num=new_shakes),
        ])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._('You have {count} new message{plural}!').format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Oops, something went wrong ... Rebooting ...")

    def on_uploading(self, to):
        return self._("Uploading data to {to} ...").format(to=to)

    def on_downloading(self, name):
        return self._("Downloading from {name} ...").format(name=name)

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
            'I\'ve been pwning for {duration} and kicked {deauthed} clients! I\'ve also met {associated} new friends and ate {handshakes} handshakes! #pwnagotchi #pwnlog #pwnlife #hacktheplanet #skynet').format(
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
