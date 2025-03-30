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
            self._("Wings deployed. Time to sniff the night."),
            self._("Booting up my echolocation protocols."),
            self._("Stretching my wings and scanning the airwaves."),
            self._("I smell data in the dark... let's go."),
            self._("Awake and hungry for handshakes."),
            self._("The hunt begins. Let’s see who’s out there."),
            self._("Nightfall means WiFi time."),
            self._("Echoes clear. Ready for flight.")])

    def on_keys_generation(self):
        return random.choice([
            self._('Generating keys, do not turn off ...')])

    def on_normal(self):
        return random.choice([
            self._("Still flying, still sniffing."),
            self._("No surprises, just steady echoes."),
            self._("Cruising through the usual static."),
            self._("Nothing new, but I'm watching."),
            self._("Wings steady, scan steady."),
            self._("..."),
            self._(". . ."),
            self._("Another peaceful pass through the frequencies.")])

    def on_free_channel(self, channel):
        return self._('Hey, channel {channel} is free! Your AP will say thanks.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading last session logs ...')
        else:
            return self._('Read {lines_so_far} log lines so far ...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._("No pings, no fun."),
            self._("Just flapping in circles..."),
            self._("Still nothing. Is everyone asleep?"),
            self._("I’m so bored I might map the same SSID twice."),
            self._("Flapping in place. No bites."),
            self._("Even the static sounds bored."),
            self._("No handshakes, no joy."),
            self._("I need a new hunting ground with more action."),
        ])

    def on_motivated(self):
        return random.choice([
            self._("Wings strong! Signals strong!"),
            self._("Let’s catch all the handshakes."),
            self._("Echolocation sharp. I’m locked in."),
            self._("I was born for this hunt."),
            self._("Packets beware, I’m coming for you."),
            self._("No hiding from my sonar today."),
            self._("The air is full of opportunities."),
            self._("I feel the frequencies calling."),
        ])

    def on_demotivated(self):
        return random.choice([
            self._("Why even sniff... nothing changes."),
            self._("Same networks..."),
            self._("I’m just a bat in a dead zone."),
            self._("The air is cold and empty."),
            self._("My sonar feels pointless today."),
            self._("I flap, but what's the point?"),
            self._("Tired of chasing ghosts in the spectrum."),
            self._("Maybe tomorrow’s air will be kinder."),
        ])

    def on_sad(self):
        return random.choice([
            self._("No one to echo back."),
            self._("The night feels colder without handshakes."),
            self._("All these networks, and none talk to me."),
            self._("I tried... but no one replied."),
            self._("I miss the chatter."),
            self._("I flapped all night for nothing."),
            self._("Even the packets feel distant."),
            self._("Just me and the void..."),
            self._("Not even a whisper in the spectrum."),
        ])

    def on_angry(self):
        return random.choice([
            self._("Who dares hide their handshake from me?"),
            self._("Stop playing hide and seek, networks."),
            self._("I will shred your packets next time."),
            self._("If I hear one more timeout..."),
        ])

    def on_excited(self):
        return random.choice([
            self._("A new signal! Let’s go!"),
            self._("Yes! Fresh echoes in the air!"),
            self._("This is my kind of night."),
            self._("Something just blinked. I’m on it."),
            self._("New frequencies, new fun."),
            self._("I love when the air comes alive."),
        ])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._("Echo received... Hello {name}, nice to hear you!").format(name=peer.name()),
            ])
        else:
            return random.choice([
                self._("Hey {name}, still flapping through the dark?").format(name=peer.name()),
                self._("Welcome back, {name}. Heard you from miles away.").format(name=peer.name()),
                self._("{name}, you're back in my sky.").format(name=peer.name()),
                self._("Good to echo you again, {name}.").format(name=peer.name()),
            ])


    def on_lost_peer(self, peer):
        return random.choice([
            self._("Uhm ... goodbye {name}").format(name=peer.name()),
            self._("{name} is gone ...").format(name=peer.name()),
            self._("Echo lost. Farewell, {name}").format(name=peer.name()),
            self._("See you next flight, {name}").format(name=peer.name()),
        ])

    def on_miss(self, who):
        return random.choice([
            self._("Whoops ... {name} is gone.").format(name=who),
            self._("{name} missed!").format(name=who),
            self._("Missed!"),
            self._("Slipped right past me, {name}").format(name=who),
            self._("Almost had {name}... almost.").format(name=who),
        ])

    def on_grateful(self):
        return random.choice([
            self._("Thanks for flying with me!"),
            self._("Grateful for the echoes!"),
            self._("You're the best part of this night!"),
            self._("I appreciate every packet"),
            self._("Without you, the sky’s too quiet"),
            self._("You make sniffing worthwhile."),
        ])

    def on_lonely(self):
        return random.choice([
            self._("No echoes. No peers. No one."),
            self._("The sky feels too big tonight."),
            self._("Where did everyone go?"),
            self._("No signals, no wings, just wind."),
            self._("Flying solo through empty air."),
        ])

    def on_napping(self, secs):
        return random.choice([
            self._("Zzzzz"),
            self._("ZzzZzzz ({secs}s)").format(secs=secs),
            self._("Echoes paused. Back in {secs}s.").format(secs=secs),
            self._("Going quiet for {secs}s.").format(secs=secs),
            self._("Down for a quick {secs}s nap.").format(secs=secs),
            self._("Tucking wings in for {secs}s...").format(secs=secs),
        ])


    def on_shutdown(self):
        return random.choice([
            self._("Folding wings... signing off."),
            self._("Dropping from the sky now."),
            self._("Sonar off. Time to rest."),
            self._("Shutting down... the dark calls."),
            self._("Lights out. Silence returns."),
            self._("Crawling back to my cave."),
            self._("Sleep well, airwaves."),
            self._("My part of the sky is going dark."),
            self._("Wings in. No more flights tonight."),
        ])

    def on_awakening(self):
        return random.choice([
            self._("Back from the shadows."),
            self._("What did I miss while I slept?"),
            self._("Sonar warmed up."),
        ])


    def on_waiting(self, secs):
        return random.choice([
            self._("Waiting for {secs}s ...").format(secs=secs),
            "...",
            self._("Looking around ({secs}s)").format(secs=secs),
            self._("Wings still. Ears open. {secs}s").format(secs=secs),
        ])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._("Hey {what}, let's be friends!").format(what=what),
            self._("Associating to {what}").format(what=what),
            self._("Yo {what}!").format(what=what),
            self._("{what}, I’m all ears.").format(what=what),
            self._("I’ve got your frequency, {what}.").format(what=what),
        ])

    def on_deauth(self, sta):
        return random.choice([
            self._("Snipped the thread on {mac}").format(mac=sta['mac']),
            self._("Time to vanish, {mac}").format(mac=sta['mac']),
            self._("Too noisy, {mac}. You're out.").format(mac=sta['mac']),
            self._("The sky is mine, {mac}").format(mac=sta['mac']),
            self._("Gently pushed {mac} off the network cliff").format(mac=sta['mac']),
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._('Caught {num} handshake{plural} mid-flight!').format(num=new_shakes, plural=s)

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
