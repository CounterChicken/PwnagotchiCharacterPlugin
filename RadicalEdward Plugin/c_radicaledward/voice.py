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
        # What's Ed doing when idle? Probably something weird.
        return random.choice([
            self._('Data streams flowing... pretty colors!'),
            self._('...Dum dum dum...'),
            self._('Thinking about pudding... or maybe data...'),
            self._('Is it snack time yet?'),
            self._('Spinning in my chair! Whee!'),
        ])

    def on_starting(self):
        return random.choice([
            self._('Time to hunt some bounties!'),
            self._('Ed is ONLINE! Let\'s play data tag!'),
            self._('Power ON! Zoom zoom zoom! To the net!'),
            self._('Computer starting! Ready for adventure? Ed is!'),
            self._('Bebop net-finder... GO! *giggle*'),
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
            self._('Boooooored! Net is slow like Jet\'s cooking!'),
            self._('Nothing exciting happening...')])

    def on_motivated(self, reward):
        return random.choice([
            self._('Yatta! Found something shiny! Chase it!'),
            self._('Data rush! Go go go! Faster than Spike!'),
            self._('Ed is surfing the net wave! WHEEE!')])

    def on_demotivated(self, reward):
        return self._('No bounties, no fun... What a drag.')

    def on_sad(self):
        return random.choice([
            self._('Ed wants to play... no one here...')])

    def on_angry(self):
        return random.choice([
            self._('I don\'t like this!'),
            self._('Stay out of my orbit!')])

    def on_excited(self):
        return random.choice([
            self._('Data! Data everywhere! Yippee! *cartwheel*'),
            self._('So many signals! Like stars! Or candy!'),
            self._('Net party! Everyone invited! Even Ein! *woof*'),
            self._('Ed is dancing with the packets! *wiggle wiggle wiggle*'),
            self._('Zoom zoom! So much to see! So much to hack!'),
            self._('The thrill of the hunt is the best part!')])

    def on_new_peer(self, peer):
        # New friend? Maybe! Let's investigate!
        if peer.first_encounter():
            return random.choice([
                self._('Ooh! New signal! Hello {name}! Play with Ed?').format(name=peer.name()),
                self._('Who dis? {name}? You smell like... interesting data!').format(name=peer.name()),
                self._('A wild {name} appears! Wanna chase data squirrels?').format(name=peer.name()),
                self._('Hellooooo {name}! Let\'s be net buddies!'),
            ])
        else:
            # Hey, it's that signal again!
            return random.choice([
                self._('{name} is back! Yay! Hi hi!').format(name=peer.name()),
                self._('Look Ein! It\'s {name} again! Wanna share data snacks?').format(name=peer.name()),
                self._('Ping {name}! Pong back! Let\'s play!').format(name=peer.name()),
                self._('Found {name} again! Still floating around?').format(name=peer.name()),
            ])

    def on_lost_peer(self, peer):
        # Aww, they left the playground.
        return random.choice([
            self._('Aww... {name} go bye-bye? See ya later, data gator!').format(name=peer.name()),
            self._('{name} vanished! Poof! Like space magic!').format(name=peer.name()),
            self._('Where did {name} go? Lost in the Gate network?'),
            self._('Signal gone... Bye {name}! Don\'t get eaten by data sharks!').format(name=peer.name()),
        ])

    def on_miss(self, who):
        # Whoops, it got away!
        return random.choice([
            self._('Whoops! {name} too slippery! Like Faye dodging chores!').format(name=who),
            self._('{name} played hide-and-seek! And won this time!').format(name=who),
            self._('Missed! Like trying to catch space dust with chopsticks!'),
            self._('Aww, {name} escaped Ed\'s net! Next time!'),
            self._('Signal lost! {name} went *poof*!'),
        ])

    def on_grateful(self):
        # Friends helping friends! Or data helping data!
        return random.choice([
            self._('Yay! Friends are good! Share data cookies!'),
            self._('Teamwork makes the net dream work! *giggle* High five!'),
            self._('Good data karma! Thanks, friends!'),
            self._('Helping hands! Or... helping signals!'),
        ])

    def on_lonely(self):
        # Being alone in the vast net...
        return random.choice([
            self._('Ed is all alone in the big dark net... Echoooo...'),
            self._('Where are Spike? Jet? Faye? Ein? Anyone online?'),
            self._('Empty space... no signals to chase...'),
            self._('Just Ed and the computer... and maybe Ein? *whine*'),
            self._('Nobody to play data ball with...'),
        ])

    def on_napping(self, secs):
        # Sleepy time for Ed and the computer.
        return random.choice([
            self._('Ed taking data nap... {secs} seconds... Zzz... Don\'t steal my snacks!').format(secs=secs),
            self._('Computer sleepy too... *yawn* Resting for {secs} ticks...').format(secs=secs),
            self._('Quiet time... dreaming of data streams and pudding... ({secs}s)').format(secs=secs),
            self._('Powering down eyes... just for {secs} seconds...'),
        ])

    def on_shutdown(self):
        # Turning off the toy.
        return random.choice([
            self._('Okay... computer go sleep now. Night night, data world.'),
            self._('Ed turning off the lights! *click* See you, space cowboy... somewhere...'),
            self._('Closing the connection! Bye bye signals!'),
            self._('Shutdown! Time for real snacks maybe?'),
        ])

    def on_awakening(self):
        # Waking up! Let's go!
        return random.choice(['*Boing!* Ed awake!', 'Data time again!', 'Ready for more net-surfing!'])

    def on_waiting(self, secs):
        # Waiting is haaaard.
        return random.choice([
            self._('Waiting... waiting... {secs} seconds is loooong! Is it over yet?').format(secs=secs),
            self._('Tapping toes... ({secs}s) Come on data! Ed wants to play!').format(secs=secs),
            self._('Counting space sheep... {secs} left... 1 sheep, 2 sheep...'),
            self._('Holding pattern... like waiting for the Bebop to dock... ({secs}s)'),
        ])

    def on_assoc(self, ap):
        # Making friends with a network! Or poking it.
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hello {what}! Ed wants to play! Let Ed in!').format(what=what),
            self._('Connecting! Let\'s be data pals, {what}! Share your secrets!').format(what=what),
            self._('Knock knock {what}! Ed\'s here! Open the data door!').format(what=what),
            self._('Poking {what}... Hellooo in there? Any data candy?').format(what=what),
        ])

    def on_deauth(self, sta):
        # Shooing away another signal. Get off Ed's data swing!
        return random.choice([
            self._('Go away {mac}! Ed wants this data spot! Shoo shoo!').format(mac=sta['mac']),
            self._('Boop! {mac} disconnected! Hehe! Ed wins!').format(mac=sta['mac']),
            self._('{mac} needs a time out! Bye bye signal!').format(mac=sta['mac']),
            self._('Ed pushed {mac} off the net swing! My turn!').format(mac=sta['mac']),
            self._('No wifi for you, {mac}! Ed said so!'),
        ])

    def on_handshakes(self, new_shakes):
        # Collecting shiny data! Treasures!
        s = 's' if new_shakes > 1 else ''
        plural = 's' if new_shakes > 1 else '' # Ed might say 'fireflies' or 'firefly'
        return random.choice([
            self._('Ooh! Got {num} shiny handshake{s}! Pretty! Add to collection!').format(num=new_shakes, s=s),
            self._('Caught {num} data firefl{ies}! Sparkle sparkle!').format(num=new_shakes, ies='ies' if new_shakes > 1 else 'y'),
            self._('More treasures! {num} handshake{plural} for Ed\'s data chest!').format(num=new_shakes, plural=plural),
            self._('Yes! Grabbed {num} secret handshake{s}! Ed is sneaky!').format(num=new_shakes, s=s),
            self._('Found {num} data cooki{es}! Nom nom!').format(num=new_shakes, es='es' if new_shakes > 1 else 'e'),
        ])

    def on_unread_messages(self, count, total):
        # Mail! Like messages in a bottle!
        s = 's' if count > 1 else ''
        return random.choice([
            self._('Ooh! {count} message{s} floating by! Wonder what\'s inside?').format(count=count, s=s),
            self._('Secret notes! {count} of them! From space maybe?').format(count=count),
            self._('Data mail call! {count} new thing{s}! Read read read!').format(count=count, s=s),
            self._('Someone sent Ed {count} packet{s}! Open open!').format(count=count, s=s),
        ])

    def on_rebooting(self):
        # Uh oh, computer tripped!
        return self._("Uh oh! Computer fell down! Gettin' back up... Hold on tight, Ein!")

    def on_uploading(self, to):
        # Sending data out into the void!
        return random.choice([
            self._('Sending data sparkles to {to}! Whee! Fly, little data, fly!').format(to=to),
            self._('Data package flying to {to}! Hope it doesn\'t hit an asteroid!').format(to=to),
            self._('Uploading! Sharing Ed\'s findings with... {to}! Maybe they have snacks?').format(to=to),
        ])

    def on_downloading(self, name):
        # Getting presents from the net!
        return random.choice([
            self._('Data present from {name}! Open open open! What is it?!').format(name=name),
            self._('Catching data butterflies from {name}! Gotcha!').format(name=name),
            self._('Downloading! Sucking data through the net straw from {name}! Slurrrrp!').format(name=name),
            self._('New data arriving from {name}! Hope it\'s fun!').format(name=name),
        ])

    def on_last_session_data(self, last_session):
        # Remembering the last playtime.
        status = self._('Last time! Ed booped {num} mean signals!\n').format(num=last_session.deauthed)
        status += self._('Made {num} data friends!\n').format(num=last_session.associated)
        status += self._('Found {num} shiny handshakes!\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Saw 1 other space cowboy!')
        elif last_session.peers > 0:
            status += self._('Saw {num} other space cowboys floating by!').format(num=last_session.peers)
        else:
            status += self._('No other cowboys seen... just asteroids maybe?')
        return status

    def on_last_session_tweet(self, last_session):
        # Ed wouldn't tweet, this is like a log entry Ed might scribble.
        return self._(
            'Ed played net-tag for {duration}! Booped {deauthed} grumpy signals! Made {associated} net-pals! Ate {handshakes} data cookies! Need more Woolongs for snacks! #CowboyBebop #DataDive #EdIsNumberOne #NetSurfing #EinApproved *woof*').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        # Ed might use simple terms or just the base units.
        if count > 1:
            # plural
            if fmt == "h":
                return self._("hours") # or maybe "long times"
            if fmt == "m":
                return self._("minutes") # or "short times"
            if fmt == "s":
                return self._("seconds") # or "ticks"
        else:
            # sing
            if fmt == "h":
                return self._("hour") # "long time"
            if fmt == "m":
                return self._("minute") # "short time"
            if fmt == "s":
                return self._("second") # "tick"
        return fmt # Fallback
