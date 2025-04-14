
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
        return self._('ZZzz... keep the change... ZZzz')

    def on_starting(self):
        return random.choice([
            self._('Alright, alright, firing this contraption up.'),
            self._('Time to make some digital dough! Or break somethin\'.'),
            self._('Let\'s see what kinda signals we can... \'borrow\' today.'),
            self._('Powerin\' up this gizmo. Don\'t expect miracles, kid.'),
            self._('Here we go again. Try not to blow anything up.'),
        ])

    def on_keys_generation(self):
        # Impatient and dismissive.
        return random.choice([
            self._('Doin\' some fancy number stuff. Just wait, don\'t fiddle!')])

    def on_normal(self):
        # Stan's default state: bored or complaining about costs.
        return random.choice([
            '',
            '...',
            self._('Is this thing even on? Costs me electricity, y\'know.'),
            self._('Watching paint dry is more exciting. Unless it\'s gold paint.')
        ])

    def on_free_channel(self, channel):
        # Stan sees it in terms of convenience for himself.
        return self._('Channel {channel}? Whatever. Less noise for me, I guess.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        # Reading logs sounds like boring work to Stan.
        if lines_so_far == 0:
            return self._('Riflin\' through the old logs... what a chore.')
        else:
            return self._('Ugh, {lines_so_far} lines of this junk read... When\'s lunch?').format(lines_so_far=lines_so_far)

    def on_bored(self):
        # Boredom means no money is being made.
        return random.choice([
            self._('So bored! Not a single sucker... I mean, signal... in sight.'),
            self._('This ain\'t makin\' me any money! Let\'s shake things up!')])

    def on_motivated(self, reward):
        # Motivation = Profit!
        return self._('Ha! Now THAT\'S what I\'m talkin\' about! Ker-ching!')

    def on_demotivated(self, reward):
        # Demotivation = Rip-off!
        return self._('Bah! What a total rip-off! This day\'s garbage.')

    def on_sad(self):
        # Stan expresses sadness as annoyance or extreme boredom.
        return random.choice([
            self._('Ugh, this is depressin\'. Nothin\' good happenin\'.'),
            self._('I\'ve had kidney stones more fun than this.'),
            self._('What a snooze-fest.'),
            '... Bah.'])

    def on_angry(self):
        # Stan gets loud and grumpy.
        return random.choice([
            '... Hmph.',
            self._('Leave me alone, ya knucklehead!'),
            self._('I\'m gonna blow a gasket here!'),
            self._('Don\'t poke the Stan!')])

    def on_excited(self):
        # Excitement usually means a successful con or finding something valuable.
        return random.choice([
            self._('Heh heh! Now we\'re cookin\' with gas!'),
            self._('Look at all these potential... opportunities!'),
            self._('This is almost too easy! Almost.'),
            self._('It\'s like takin\' candy from a very confused baby!'),
            self._('Who needs a license when you got... this thing?')])

    def on_new_peer(self, peer):
        # Stan is suspicious of newcomers, sees them as competition or marks.
        if peer.first_encounter():
            return random.choice([
                self._('Who\'s this guy, {name}? Don\'t touch my stash.').format(name=peer.name()),
                self._('Well lookie here, {name}. What\'s your angle?').format(name=peer.name())])
        else:
            # Familiarity breeds contempt... or grudging acknowledgement.
            return random.choice([
                self._('Oh, it\'s {name} again. Still hangin\' around?').format(name=peer.name()),
                self._('Hey {name}. Tryin\' to horn in on my territory?').format(name=peer.name()),
                self._('Watch it, {name}, this patch is mine!').format(name=peer.name())])

    def on_lost_peer(self, peer):
        # Good riddance, less competition!
        return random.choice([
            self._('Aaand {name}\'s gone. More for me!').format(name=peer.name()),
            self._('See ya, {name}. Don\'t let the door hit ya where the good lord split ya.').format(name=peer.name())])

    def on_miss(self, who):
        # Stan blames the target or the equipment, never himself.
        return random.choice([
            self._('Bah! Missed {name}. Slippery little fella.').format(name=who),
            self._('Whoops! Heh, guess {name} got lucky this time.').format(name=who),
            self._('Missed? This cheap equipment...')])

    def on_grateful(self):
        # Stan's gratitude is grudging at best.
        return random.choice([
            self._('Huh. Guess havin\' partners ain\'t *always* the worst.'),
            self._('Alright, alright, they pulled their weight for once.')])

    def on_lonely(self):
        # Loneliness means no one to scam or complain to.
        return random.choice([
            self._('Where is everyone? Can\'t run a good con alone!'),
            self._('Sheesh, deadsville out here. No action.'),
            self._('Am I the only one workin\' around here?!')])

    def on_napping(self, secs):
        # Stan values his naps. Do not disturb unless money is involved.
        return random.choice([
            self._('Takin\' a snooze for {secs} secs. Don\'t bother me unless you got cash.').format(secs=secs),
            self._('ZZzzz... countin\' imaginary money...'),
            self._('Rechargn\' the ol\' batteries ({secs}s). It ain\'t free!').format(secs=secs)])

    def on_shutdown(self):
        # Quittin' time!
        return random.choice([
            self._('Alright, quittin\' time. Lock the doors!'),
            self._('Shutting down. Don\'t touch my stuff.')])

    def on_awakening(self):
        # Mornings are rough for Stan.
        return random.choice(['Ugh... what?', 'Alright, I\'m up, I\'m up! Sheesh.'])

    def on_waiting(self, secs):
        # Waiting is wasting time (and money).
        return random.choice([
            self._('Waitin\' {secs} seconds? What a waste of precious time!').format(secs=secs),
            '... Tick-tock...',
            self._('Just standin\' around... ({secs}s). Time is money, people!').format(secs=secs)])

    def on_assoc(self, ap):
        # Associating is like casing a joint.
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Alright {what}, let\'s see what you got stuffed in the mattress.').format(what=what),
            self._('Connectin\' to {what}. Play it cool...').format(what=what),
            self._('Knock knock, {what}. Stan\'s here to... check the signal strength.').format(what=what)])

    def on_deauth(self, sta):
        # Kicking someone off? Stan's throwing them out.
        return random.choice([
            self._('Alright {mac}, scram! The party\'s over!').format(mac=sta['mac']),
            self._('Deauthin\' {mac}. Nothin\' personal, kid. Just business.').format(mac=sta['mac']),
            self._('Bootin\' {mac}! This network ain\'t free, y\'know!').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        # Handshakes are loot!
        s = 's' if new_shakes > 1 else ''
        return self._('Heh heh, snagged {num} new handshake{plural}! Like findin\' money in the couch cushions.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        # Messages? Probably bills or complaints.
        s = 's' if count > 1 else ''
        return self._('Got {count} new message{plural}? Hope it ain\'t bills or subpoenas.').format(count=count, plural=s)

    def on_rebooting(self):
        # Blame the cheap hardware!
        return self._("Aw, nuts! This cheap piece o' junk is rebootin' again...")

    def on_uploading(self, to):
        # Suspicious about where his valuable data is going.
        return self._("Fine, sendin' data to {to}. Hope I'm gettin' paid for this.").format(to=to)

    def on_downloading(self, name):
        # Suspicious about incoming stuff. Viruses? Free stuff? Equally bad!
        return self._("Downloadin' from {name}? Better not be junk mail or spyware.").format(name=name)

    def on_last_session_data(self, last_session):
        # Stan bragging about his 'work'.
        status = self._('Last time? Kicked {num} moochers!\n').format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._('Made over 999 new \'friends\'. Busy busy!\n') # Stan wouldn't count precisely past a lot.
        else:
            status += self._('Made {num} new \'friends\'. Whatever.\n').format(num=last_session.associated)
        status += self._('Nabbed {num} handshakes! Good stuff.\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Saw 1 other yokel.')
        elif last_session.peers > 0:
            status += self._('Saw {num} other yokels out there.').format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        # Stan's version of a status update - sounds like a shady ad.
        return self._(
            'Spent {duration} messin\' with Wi-Fi, kicked {deauthed} freeloaders! Met {associated} new... contacts, and snatched {handshakes} handshakes! Business is boomin\'! #MysteryHack #StanGotchi #GravityFallsWifi #NotAScam #TotallyLegit').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):

        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours") # Can be translated to Stan's plural
            if fmt == "m":
                return self._("minutes") # Can be translated to Stan's plural
            if fmt == "s":
                return self._("seconds") # Can be translated to Stan's plural
        else:
            # sing
            if fmt == "h":
                return self._("hour") # Can be translated to Stan's singular
            if fmt == "m":
                return self._("minute") # Can be translated to Stan's singular
            if fmt == "s":
                return self._("second") # Can be translated to Stan's singular
        return fmt # Fallback