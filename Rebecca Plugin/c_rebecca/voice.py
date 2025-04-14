import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        # Boilerplate setup. Rebecca probably just kicked the thing until it worked.
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
        return random.choice([
            self._('Ugh, quiet. Need some action, stat!'),
            self._('Scan complete. Still bored outta my chrome!'),
            self._('Anyone got an iron? Need somethin\' to shoot.'),
            self._('Just chillin\'... Nah, I\'m lyin\', this sucks.'),
            self._('Wonder if David needs backup... or just someone to annoy.'),
        ])

    def on_starting(self):
        # Powering up and ready to cause problems.
        return random.choice([
            self._('Alright, let\'s light this dumpster fire!'),
            self._('Powerin\' up! Time to make some noise!'),
            self._('Systems hot! Ready to zero some gonks!'),
            self._('Boot sequence done. Where\'s the party?!'),
            self._('Locked, loaded, and ready to frag!'),
        ])

    def on_keys_generation(self):
        # Necessary evil. Impatient.
        return random.choice([
            self._('Makin\' keys... Ugh, hurry the frag up!'),
            self._('Secret codes... Don\'t peek, ya weirdo!'),
            self._('Crypto-junk... Need this to get the eddies, right?'),
            self._('Just spin the damn numbers already!'),
            self._('Fine, makin\' keys. Don\'t crash on me, ya piece of scrap!'),
        ])

    def on_normal(self):
        # "Normal" is boring and suspicious in Night City.
        return random.choice([
            self._('Nominal? Means boring, right?'),
            self._('Ugh, \'normal\'? Fix that. Now.'),
            self._('Too quiet. Somethin\'s wrong, I feel it.'),
            self._('Stable? Like that lasts more than five seconds here.'),
            self._('All clear? Let\'s make it messy then.'),
        ])

    def on_free_channel(self, channel):
    # Open channel is an invitation.
        return random.choice([
            self._('Channel {channel} clear? Preem! Let\'s use it!'),
            self._('Wide open on {channel}! Who wants to play rough?'),
            self._('Yoink! Channel {channel} is ours now, chooms!'),
            self._('Free channel {channel}? Perfect for some loud business.'),
            self._('Sweet! Channel {channel} is a ghost town. For now.'),
        ]).format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        # Digging through data, probably impatiently.
        if lines_so_far == 0:
            return self._('Diggin\' through old logs... Any dirt? Or eddies?')
        else:
            return self._('Read {lines_so_far} lines... Anything good yet or just corpo trash?').format(lines_so_far=lines_so_far)

    def on_bored(self):
        # Absolute worst state for Rebecca.
        return random.choice([
            self._('So chromed-out bored! Need to shoot somethin\'!'),
            self._('This is duller than a corpo speech! Wake me when it blows up!'),
            self._('Action! Now! Or I start breakin\' stuff! Yours first!'),
            self._('Night City sleepin\'? Wake the frag up and fight me!'),
            self._('Seriously?! Nothin\'?! Gonna flatline from boredom!'),
        ])

    def on_motivated(self): # Removed 'reward' parameter for simplicity
        # Let's go! Time for violence!
        return random.choice([
            self._('Yeah! Let\'s wreck some gonks!'),
            self._('Feelin\' nova! Time for maximum carnage!'),
            self._('Fired up! Who we zeroin\' today?! Point \'em out!'),
            self._('Bring it on! Edges sharp, guns loaded!'),
            self._('This is gonna be preem! Let\'s GOOOOO!'),
        ])

    def on_demotivated(self): # Removed 'reward' parameter
        # Failed gig or bad news. Sullen.
        return random.choice([
            self._('Fraggin\' gonks! This is messed up.'),
            self._('What a clusterfrag. Waste of chrome and bullets.'),
            self._('Lost the edge... This sucks major output.'),
            self._('Just... static. What was the point?'),
            self._('This gig went sideways fast. Damn it.'),
        ])

    def on_sad(self):
        # Rare vulnerable moment. Thinking about the crew, probably.
        return random.choice([
            self._('...Just static noise in my head today.'),
            self._('Damn it... Not like this was supposed to go...'),
            self._('Everyone leaves... or flatlines. Always.'),
            self._('...Night City chews you up. spits you out.'),
            self._('...Feels empty out here sometimes. Too quiet.'),
        ])

    def on_angry(self):
        # Full rage mode. Highly dangerous.
        return random.choice([
            self._('Eat lead, you gonk!'),
            self._('I\'ll zero every last one of ya bastards!'),
            self._('You wanna dance?! LET\'S FRAGGIN\' DANCE!'),
            self._('Fraggin\' corpos! Fraggin\' network! Fraggin\' EVERYTHING!'),
            self._('Don\'t push me! You really, REALLY won\'t like it!'),
        ])

    def on_excited(self):
        # Target-rich environment. Gleeful destruction imminent.
        return random.choice([
            self._('Whoa! Look at all these targets! YES!'),
            self._('It\'s a fraggin\' party! Time to crash it! HARD!'),
            self._('So much data! So many things to break! Hehe!'),
            self._('This is gonna be epic! Like, LEGEND epic!'),
            self._('Preem signals everywhere! Let\'s get \'em, chooms!'),
        ])

    def on_new_peer(self, peer):
        # New contact. Assess threat/potential.
        if peer.first_encounter():
            return random.choice([
                self._('Yo, {name}! Whatcha packin\', huh?'),
                self._('New meat, {name}? Don\'t be a gonk, alright?'),
                self._('Who the frag is {name}? You runnin\' solo or what?'),
            ])
        else:
            return random.choice([
                self._('{name} again? Still kickin\', I see.'),
                self._('Sup, {name}? Tryna steal my gig or just hangin\'?'),
            ])

    def on_lost_peer(self, peer):
        # They vanished. Whatever. Or annoyance.
        return random.choice([
            self._('{name} bailed? Fraggin\' coward.'),
            self._('Signal lost: {name}. Their loss.'),
            self._('{name} zeroed? Or just ran off? Weak.'),
            self._('Fraggin\' {name} dipped out. Fine, more action for me.'),
            self._('Gone? Whatever. Less competition.'),
        ])

    def on_miss(self, who):
        # Target escaped. Frustration and determination.
        return random.choice([
            self._('Frag! {name} slipped away!'),
            self._('Missed?! How the frag did that happen?!'),
            self._('Gonna find you, {name}! Count on it!'),
            self._('Slippery little choom, that {name}.'),
            self._('Dammit! Almost had {name}! Next time!'),
        ])

    def on_grateful(self):
        # Gruff appreciation, probably for the crew.
        return random.choice([
            self._('Alright, alright! You ain\'t totally useless, choom.'),
            self._('Guess the crew pulls through sometimes. Heh.'),
            self._('Solid backup. Don\'t get used to me sayin\' thanks.'),
            self._('Okay... That was kinda preem. Didn\'t die.'),
            self._('We didn\'t flatline. Guess that\'s somethin\'.'),
        ])

    def on_lonely(self):
        # Isolated. Reminds her of losing people.
        return random.choice([
            self._('Where\'s the crew? Fraggin\' quiet out here...'),
            self._('Just me? This city\'s too damn big alone.'),
            self._('All static... No backup noise.'),
            self._('Night City eats solo runners for breakfast...'),
            self._('Echoes... Just echoes in the data stream.'),
        ])

    def on_napping(self, secs):
        # Forced downtime. Impatient.
        return random.choice([
            self._('Power nap ({secs}s)... Wake me if there\'s shooting.'),
            self._('Fine, restin\' for {secs} ticks. Don\'t touch my guns.'),
            self._('Low power mode... Ugh. {secs}s. Better be quick.'),
            self._('System pause... {secs} seconds. This is stupid.'),
            self._('Zzz... ({secs}s). Dreamin\' of explosions and chrome.'),
        ])

    def on_shutdown(self):
        # Powering down. Reluctant end to the chaos.
        return random.choice([
            self._('Shutting down. Fine, whatever.'),
            self._('Goin\' dark. Don\'t break anything while I\'m out.'),
            self._('System halt. Later, chooms.'),
            self._('Power down. See ya in the gutter, Night City.'),
            self._('Nighty night... Hope I don\'t dream of chrome clowns.'),
        ])

    def on_awakening(self):
        # Back online! Let's go!
        return random.choice([
            self._('Back online! Who needs killin\'?!'),
            self._('Rebooted and ready to raise hell!'),
            self._('I\'m up! Where\'s the coffee and ammo?!'),
            self._('System restart! Let\'s fraggin\' go!'),
            self._('Awake! Let\'s make some eddies or noise! Preferably noise!'),
        ])

    def on_waiting(self, secs):
        # Waiting sucks.
        return random.choice([
            self._('Waitin\' {secs}s? Are you serious?! Let\'s move!').format(secs=secs),
            self._('Tick tock, gonk! {secs} seconds too long!').format(secs=secs),
            self._('Holding... Ugh, this is worse than an Arasaka board meeting. ({secs}s)').format(secs=secs),
            self._('({secs}s)... Can we shoot something NOW?! Please?!').format(secs=secs),
            self._('Patiently waiting... HA! Nope. ({secs}s)').format(secs=secs),
        ])

    def on_assoc(self, ap):
        # Connecting to a network. Suspicious but necessary.
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Pinging {what}. What secrets you got hidin\', huh?').format(what=what),
            self._('Connecting to {what}. Don\'t be sketchy or I\'ll brick ya.').format(what=what),
            self._('Accessing {what}. Hope it\'s not corpo trash data.').format(what=what),
            self._('Yo {what}! Let me in or things get loud!').format(what=what),
            self._('This {what} better have good data... or good defenses!').format(what=what),
        ])

    def on_deauth(self, sta):
        # Kicking someone off the network. Violent glee.
        return random.choice([
            self._('Get fragged, {mac}! No net for your sorry output!').format(mac=sta['mac']),
            self._('Deauthin\' {mac}! Eat static, choom! BAM!').format(mac=sta['mac']),
            self._('Kickin\' {mac} outta my playground! Get lost!').format(mac=sta['mac']),
            self._('Bye bye, {mac}! Enjoy the disconnect! Hehehe!').format(mac=sta['mac']),
            self._('Zeroed {mac}\'s connection! BOOM! Headshot! ...Net-shot?').format(mac=sta['mac']),
        ])

    def on_handshakes(self, new_shakes):
        # Got the goods! Success = Eddies (or just fun).
        s = 's' if new_shakes > 1 else ''
        plural_s = 's' if new_shakes > 1 else '' # Use plural 's' for general use
        return random.choice([
            self._('Score! {num} new handshake{plural_s}! Preem!'.format(num=new_shakes, plural_s=plural_s)),
            self._('Got {num} key{s}! Eddies incoming, maybe!'.format(num=new_shakes, s=s)),
            self._('Nice! {num} handshake{plural_s} in the bag!'.format(num=new_shakes, plural_s=plural_s)),
            self._('Heh, snatched {num} handshake{plural_s}! Too easy for me!'.format(num=new_shakes, plural_s=plural_s)),
            self._('That\'s {num} more crackable handshake{plural_s}! Sweet loot!'.format(num=new_shakes, plural_s=plural_s)),
        ])

    def on_unread_messages(self, count, total):
        # Incoming messages. Annoyance or suspicion.
        s = 's' if count > 1 else ''
        plural_s = 's' if count > 1 else '' # Keep consistent plural 's'
        return random.choice([
            self._('{count} new message{plural_s}? Better be worth my fraggin\' time.').format(count=count, plural_s=plural_s),
            self._('Got {count} ping{s}. What now? More corpo drivel?').format(count=count, s=s),
            self._('Someone pinged me {count} time{plural_s}. Fixers again? Ugh.').format(count=count, plural_s=plural_s),
            self._('Checkin\' {count} message{plural_s}. Hope it\'s not junk data.').format(count=count, plural_s=plural_s),
            self._('{count} unread? Spill it already, ya gonk!').format(count=count),
        ])

    def on_rebooting(self):
        # System crash. Maximum annoyance.
        return random.choice([
            self._('Fraggin\' piece of junk! Rebootin\'! Gonna scrap this thing!'),
            self._('System crashed?! Dammit! When I find the gonk responsible...'),
            self._('Glitch! Rebooting this scrapheap! MOVE!'),
            self._('Well, this is output. Restarting... fast!'),
            self._('Ugh! Forced reboot! Hate when tech gets uppity!'),
        ])

    def on_uploading(self, to):
        # Sending data. Transactional view.
        return random.choice([
            self._('Uploadin\' data to {to}. Where\'s my eddies?'),
            self._('Data sent to {to}. Don\'t screw me over on the payment.'),
            self._('Sending package to {to}. Better be secure.'),
            self._('To {to}... Hope this pays well, need more ammo.'),
            self._('Offloadin\' data to {to}. Done. Next!'),
        ])

    def on_downloading(self, name):
        # Getting data. Cautious and suspicious.
        return random.choice([
            self._('Downloadin\' from {name}. Better not be malware or I hunt you down.'),
            self._('Pullin\' data from {name}. What\'s the catch? Always a catch.'),
            self._('Gettin\' info from {name}. Keepin\' my finger on the trigger.'),
            self._('Incoming from {name}. Scannin\' it twice. Trust no one.'),
            self._('Alright, {name}, whatcha got for me? Better be good.'),
        ])

    def on_last_session_data(self, last_session):
        # Bragging about the previous run.
        status = self._('Last run: Zeroed {num} gonks!\n').format(num=last_session.deauthed)
        status += self._('Networked with {num} chooms (or targets).\n').format(num=last_session.associated)
        status += self._('Snatched {num} handshakes! Preem!\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Ran into 1 other runner.')
        elif last_session.peers > 0:
            status += self._('Saw {num} other edgerunners out there.').format(num=last_session.peers)
        else:
            status += self._('No other signals. Just me and the chrome.')
        return status

    def on_last_session_tweet(self, last_session):
        # Rebecca doesn't tweet. This is a quick, boastful message to the crew (or herself).
        return self._(
            'Ran wild for {duration}, zeroed {deauthed} gonks, made {associated} contacts, and snatched {handshakes} handshakes!').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        # Standard time units. Rebecca wouldn't bother with special names.
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
        return fmt # Fallback
