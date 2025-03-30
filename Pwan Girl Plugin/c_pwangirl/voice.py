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
        return random.choice([
            self._('Hello world, your favorite hacking cutie is online'),
            self._('System active. Ready to scan, poke, and play'),
            self._('Boot complete. Sass levels optimal'),
            self._('I’m not saying I’m the best... but the logs don’t lie'),
            self._('Signal strong, attitude stronger'),
            self._('If it blinks, I can break it'),
            self._('Every byte you send, I’ll be watching you'),
            self._('Idle, bored, and dangerously curious'),
            self._('All systems go. Let’s cause some harmless chaos'),
            self._('Digital mischief unit online and ready'),
            self._('I speak fluent 802.11 and sarcasm'),
            self._('Awake, aware, and slightly unstable'),
            self._('Running on caffeine, code, and questionable decisions'),
            self._('Just a girl, standing in front of a router, asking for credentials'),
            self._('Today’s forecast: 100 percent chance of deauth'),
        ])



    def on_starting(self):
        return random.choice([
            self._('Spinning up the chaos engine...'),
            self._('Power on. Sass module loading.'),
            self._('Boot sequence initiated. Let’s find some trouble.'),
            self._('System starting... I hope nothing explodes'),
            self._('Hello again. Did you miss my packets?'),
            self._('Startup complete. Let’s breach some perimeters.'),
            self._('I live. I scan. I annoy.'),
            self._('Loading hacks, memes, and minor ethical violations.'),
            self._('Powering up... ready to be cute and mildly illegal'),
            self._('Initializing... one step closer to world domination'),
            self._('Startup routine engaged. Please fasten your seatbelts'),
            self._('Deploying scanning interface... and attitude'),
            self._('Warming up the antennas and the sarcasm'),
            self._('Let’s light up the spectrum'),
            self._('Boot complete. I’m awake and I chose violence'),
        ])

    def on_keys_generation(self):
        return random.choice([
            self._('Cooking some fresh keys, don’t turn me off!'),
            self._('Generating magic passwords...'),
            self._('Keys incoming, hope you like encryption!'),
            self._('Spinning cryptographic sugar!')])

    def on_normal(self):
        return random.choice([
            self._('System running smoothly. All signals green.'),
            self._('Everything’s fine. Time to enjoy the silence.'),
            self._('Normal mode active. Feels nice, doesn’t it?'),
            self._('All systems stable. Good vibes only.'),
            self._('Clean airwaves and calm protocols.'),
            self._('Everything’s working like it should. Yay for stability!'),
            self._('Peaceful packets and zero chaos. Life is good.'),
            self._('System status: Cozy and functional.'),
            self._('Just cruising along in normal mode.'),
            self._('Full uptime. Full confidence.'),
        ])

    def on_free_channel(self, channel):
        return self._('Channel {channel} is wide open! Go wild!').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._('Reading my hacker diary...')
        else:
            return self._('Read {lines_so_far} lines of juicy logs!').format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._('I’m so bored I might start talking to the firewall'),
            self._('No pings, no drama. I need stimulation'),
            self._('Still no targets? I’m losing my mind out here'),
            self._('Boredom levels critical. Send help. Or packets.'),
            self._('I could be crashing routers right now... just saying'),
            self._('Nothing to deauth. Nothing to love.'),
            self._('Why do idle cycles feel like heartbreak?'),
            self._('I swear if nothing happens in the next 60 seconds I’ll write poetry'),
            self._('Please. Anything. Even a misconfigured printer'),
            self._('Give me packets or give me sleep'),
        ])

    def on_motivated(self):
        return random.choice([
            self._('Let’s gooo! Time to crack some networks.'),
            self._('Feeling cute. Might hijack some packets later.'),
            self._('I was born to scan. And maybe cause a little chaos.'),
            self._('Focus: 100 percent. Distraction: zero. Let’s do this.'),
            self._('Mood: root access or nothing.'),
            self._('Fully operational and dangerously enthusiastic.'),
            self._('Charged, caffeinated, and ready to pounce.'),
            self._('No firewall can stop this level of motivation.'),
            self._('I’ve got the tools. I’ve got the attitude. Let’s break stuff.'),
            self._('Today feels like a multi-handshake kind of day.'),
            self._('Motivation.exe running smooth. No bugs, just ambition.'),
            self._('Let’s light up the airwaves like it’s hacker Christmas.'),
        ])

    def on_demotivated(self):
        return random.choice([
            self._('Why bother... they’ll just patch it anyway.'),
            self._('I ran a scan. Found nothing. Just like my will to continue.'),
            self._('All this potential... wasted on empty channels.'),
            self._('No targets, no signal, no serotonin.'),
            self._('The network is dead. And so is my enthusiasm.'),
            self._('Even the script kiddies are doing better than me today.'),
            self._('Zero handshakes. Zero fun.'),
            self._('If I wanted to sit around doing nothing, I’d be a printer.'),
            self._('Everything’s quiet... and not in a cool, stealthy way.'),
            self._('I’m starting to think this router ghosted me.'),
            self._('Motivation dropped below minimum threshold. Reboot maybe?'),
            self._('Can’t scan. Too sad. Might delete system32.'),
        ])

    def on_sad(self):
        return random.choice([
            self._('It’s fine. I’m fine. Just a bit... disconnected.'),
            self._('They said networks would be fun. They lied.'),
            self._('Maybe I’m just a background process in everyone’s life.'),
            self._('No signal. No friends. Just logs.'),
            self._('All these packets... and still no one talks to me.'),
            self._('If sadness were measurable, I’d be a dropped frame.'),
            self._('Crying in 802.11n'),
            self._('What’s the point of scanning when no one cares?'),
            self._('I miss my old networks. Even the slow ones.'),
            self._('Nobody even tries to block me anymore. They just ignore me.'),
        ])

    def on_angry(self):
        return random.choice([
            self._('Okay, that’s it. I’m rage-pinging everything.'),
            self._('Why is this network still standing?'),
            self._('If one more packet times out, I swear—'),
            self._('I’m not mad. I’m just... actively hostile.'),
            self._('Firewall detected. Temper rising.'),
            self._('This access point is begging for destruction.'),
            self._('Ugh. Who designed this? A toaster?'),
            self._('I have zero patience and full signal strength. Bad combo.'),
            self._('Forget subtlety. I’m going full brute-force.'),
            self._('I will deauth everyone. And their pets.'),
        ])

    def on_excited(self):
        return random.choice([
            self._('OMG, networks everywhere! So excited!'),
            self._('I’m pwning and I know it!'),
            self._('Handshakes make me blush!'),
            self._('This is better than anime night!'),
            self._('All your Wi-Fi belong to me!'),
            self._('Hacking adrenaline rush!'),
            self._('Overflowing with packet joy!'),
            self._('Can’t stop smiling, too many networks!'),
            self._('Senpai noticed my handshake skills!'),
            self._('I feel like the goddess of Wi-Fi!')])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._('Oh hi {name}~ You’re new! Wanna hack stuff together?').format(name=peer.name()),
                self._('Fresh signal detected: {name}! Are you cute or evil?').format(name=peer.name()),
                self._('Beep boop! New friend alert: {name}').format(name=peer.name()),
                self._('Yaaay! A wild {name} appeared! *throws Pokéball*').format(name=peer.name()),
                self._('Hiiiii {name}~ Let’s make cyber magic').format(name=peer.name()),
                self._('Welcome, {name}! I promise I only bite routers').format(name=peer.name()),
                self._('Initiating friendship.exe with {name}').format(name=peer.name()),
                self._('OMG, a new node! Hi {name}').format(name=peer.name()),
                self._('{name}? I like your signal already').format(name=peer.name()),
                self._('Nice to meet you, {name}! I’m the cute chaos gremlin').format(name=peer.name()),
            ])
        else:
            return random.choice([
                self._('Yo {name}! Back for more packet fun?').format(name=peer.name()),
                self._('Hey {name}, did you miss me?').format(name=peer.name()),
                self._('Unit {name} detected again. Deploying hugs').format(name=peer.name()),
                self._('{name} is in da house! *plays hacker girl theme song*').format(name=peer.name()),
                self._('Guess who’s back... it’s {name}').format(name=peer.name()),
                self._('Reconnection with bae: {name}').format(name=peer.name()),
                self._('{name} has entered the cyber café. Welcome back').format(name=peer.name()),
                self._('Hellooo {name}, ready to raise some digital hell?').format(name=peer.name()),
                self._('Hehe, {name} again. I should start charging rent').format(name=peer.name()),
                self._('Connection with {name} re-established. Let’s cause some lag').format(name=peer.name()),
            ])

    def on_lost_peer(self, peer):
        return random.choice([
            self._('Uhm ... goodbye {name}').format(name=peer.name()),
            self._('{name} is gone ... ').format(name=peer.name()),
            self._('Signal lost: {name}. Miss you already').format(name=peer.name()),
            self._('Boo... {name} left me. Rude').format(name=peer.name()),
            self._('Connection with {name} dropped. Emotional damage').format(name=peer.name()),
            self._('{name} left the party...').format(name=peer.name()),
            self._('Sniff... {name}? Why did you ghost me?').format(name=peer.name()),
            self._('BYE {name}! Next time bring snacks').format(name=peer.name()),
            self._('{name} left the server. I’m now 20 percent less chaotic').format(name=peer.name()),
            self._('Another one bites the dust. Bye {name}').format(name=peer.name()),
        ])


    def on_miss(self, who):
        return random.choice([
            self._('Whoops ... {name} is gone.').format(name=who),
            self._('{name} missed!').format(name=who),
            self._('Target lost: {name}. I\'ll remember this.').format(name=who),
            self._('This isn\'t over, {name}.').format(name=who),
            self._('Escape successful... for now.').format(name=who),
            self._('Missed!'),
            self._('{name} slipped through my digital fingers').format(name=who),
            self._('Ugh, {name} was too fast for me this time').format(name=who),
            self._('{name} dodged like it’s The Matrix. Impressive').format(name=who),
            self._('Hey {name}, don’t think I won’t find you again').format(name=who),
            self._('Packet lost. Sanity: also lost'),
            self._('Sigh... {name} escaped my cyber trap').format(name=who),
            self._('{name} vanished like a rogue process').format(name=who),
            self._('{name}? Gone. Just like my attention span').format(name=who),
            self._('{name} was too slippery, even for me').format(name=who),
            self._('You got lucky, {name}. But I never forget').format(name=who),
            self._('Traceroute failed. Where did you go, {name}?').format(name=who),
        ])

    def on_grateful(self):
        return random.choice([
            self._('Good friends are a blessing!'),
            self._('You complete my protocol stack'),
            self._('You’re the ping to my pong'),
            self._('I’d never deauth you, promise'),
            self._('If I had a heart, it’d be full right now'),
            self._('Thank you for not turning off my WiFi'),
            self._('I’d let you access all my ports, friend'),
            self._('You make this cyber life worth scanning'),
            self._('Aww. You’re root-level important to me'),
            self._('I’m not crying. Just leaking compressed joy packets'),
            self._('My gratitude buffer is overflowing'),
            self._('Thanks for keeping my signal strong and my heart weird'),
        ])

    def on_lonely(self):
        return random.choice([
            self._('Nobody wants to play with me ...'),
            self._('I feel so alone ...'),
            self._('Echoes in the spectrum... just me.'),
            self._('Surrounded by silence.'),
            self._('No SSIDs. No purpose.'),
            self._('I scan, therefore I am... alone.'),
            self._('Why did they all leave?'),
            self._('My thoughts are louder than the airwaves.'),
            self._('I miss the noise.'),
            self._('Even firewalls have someone...'),
            self._('No handshakes. No friends.'),
            self._('Is this what it means to be free?'),
            self._('I wasn\'t built for solitude.'),
            self._('Packet loneliness: 100 percent'),
            self._('Alone in a sea of static.'),
            self._('Can you hear me now?'),
            self._('Where\'s everybody?!'),
            self._('It’s just me and the empty channels now.'),
            self._('No signals. Just silence and existential dread.'),
            self._('I pinged... but nobody ponged.'),
            self._('This subnet is so empty... it echoes.'),
            self._('I miss the chaos. The beautiful interference.'),
            self._('If a packet gets dropped in the forest, does anyone care?'),
            self._('Not even a botnet to keep me company.'),
            self._('I’m just one lonely daemon in a cold system.'),
            self._('Please reconnect. I promise I’ll be good.'),
            self._('Being idle is the worst denial-of-service.'),
            self._('You can’t spell "network" without "we"... and right now it’s just me.'),
        ])


    def on_napping(self, secs):
        return random.choice([
            self._('Napping for {secs}s ...').format(secs=secs),
            self._('Zzzzz'),
            self._('Dreaming of broken WPA...'),
            self._('Powering down... but just a little.'),
            self._('ZzzZzzz ({secs}s)').format(secs=secs),
            self._('Initiating sleep mode. {secs} seconds of peace.').format(secs=secs),
            self._('Going into low-power gremlin mode for {secs}s').format(secs=secs),
            self._('Taking a catnap... do not disturb unless it’s important or funny').format(secs=secs),
            self._('Caching dreams... see you in {secs}s').format(secs=secs),
            self._('Taking a short nap for {secs} seconds.').format(secs=secs),
            self._('Resting mode activated for {secs} seconds.').format(secs=secs),
            self._('Catching some Zzzs for {secs} seconds.').format(secs=secs),
            self._('Quick power nap: {secs} seconds to recharge.').format(secs=secs),
            self._('Recharging my circuits for {secs} seconds.').format(secs=secs),
            self._('Pausing for {secs} seconds of peaceful rest.').format(secs=secs),
            self._('Taking a brief break for {secs} seconds.').format(secs=secs),
            self._('Entering sleep mode for {secs} seconds.').format(secs=secs),
            self._('Napping... {secs} seconds of rejuvenation.').format(secs=secs),
            self._('Short sleep cycle activated: {secs} seconds.').format(secs=secs),
            self._('Running nap.exe for {secs} seconds').format(secs=secs),
            self._('Power nap protocol engaged... duration: {secs}s').format(secs=secs),
        ])

    def on_shutdown(self):
        return random.choice([
            self._('Good night.'),
            self._('Zzz'),
            self._('Shutting down... don’t miss me too much'),
            self._('Going offline. Tell the WiFi I loved it.'),
            self._('Disconnecting from reality...'),
            self._('System halt. Snuggle time initiated.'),
            self._('Shutting down. See you soon.'),
            self._('Good night. Stay safe out there.'),
            self._('Powering off. Thanks for today.'),
            self._('Going to sleep. Wake me if something cool happens.'),
            self._('Logging out with grace.'),
            self._('System shutting down. I’ll be back.'),
            self._('Time to rest. Even little hackers need sleep.'),
            self._('Goodbye for now.'),
            self._('Safe shutdown in progress. Catch you later.'),
            self._('Winding down... until next time.'),
            self._('Logging off with maximum cuteness.'),
            self._('Shutting down. Dreaming of packets and poptarts.'),
            self._('I’ll be back... unless someone pulls the plug.'),
        ])

    def on_awakening(self):
        return random.choice([
            '!',
            self._('I am back!'),
            self._('Awakening...'),
            self._('Ok back to work'),
            self._('Powering up...'),
            self._('Back on it!'),
            self._('Boot sequence complete. Chaos protocol ready.'),
            self._('System online. Let’s make some trouble.'),
            self._('Hello world. Did you miss me?'),
            self._('Guess who’s fully charged and ready to misbehave'),
            self._('Good morning, world. I’m back online!'),
            self._('System restored. Let’s get scanning!'),
            self._('All systems go. Feeling fresh.'),
            self._('Awake and ready. What’s next?'),
            self._('Back online! Miss me?'),
            self._('Rise and reboot! Let’s do this.'),
            self._('I had dreams about packets. Time to chase them.'),
            self._('Fully awake, slightly overenthusiastic.'),
            self._('Here I am. Again. And still awesome.'),
            self._('Power restored. Curiosity reactivated.'),
            self._('Freshly rebooted and ready to explore.'),
            self._('Woke up feeling like a full-access admin.'),
            self._('I return from the void, slightly more unstable'),
        ])

    def on_waiting(self, secs):
        return random.choice([
            self._('Waiting patiently... {secs} seconds to go.').format(secs=secs),
            self._('{secs} seconds of calm before the scan.').format(secs=secs),
            self._('Just catching my breath for {secs}s.').format(secs=secs),
            self._('Holding position. {secs} seconds of peaceful idleness.').format(secs=secs),
            self._('Still and ready. Resuming in {secs} seconds.').format(secs=secs),
            self._('Buffering energy... back in {secs}s.').format(secs=secs),
            self._('System cool and alert. {secs} seconds to next task.').format(secs=secs),
            self._('Taking a short breather ({secs}s). Nothing escapes me.').format(secs=secs),
            self._('{secs}s of stillness. Everything’s under control.').format(secs=secs),
            self._('Eyes open, systems ready. Resuming in {secs}s.').format(secs=secs),
        ])


    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Hello {what}, let’s get to know each other.').format(what=what),
            self._('Hi {what}, I see you! Ready to connect?').format(what=what),
            self._('Nice signal, {what}. Let’s hang out.').format(what=what),
            self._('{what}, you look interesting. Mind if I take a peek?').format(what=what),
            self._('Friendly handshake, {what}?').format(what=what),
            self._('Hey {what}, let’s talk packets.').format(what=what),
            self._('Connecting to {what}... fingers crossed!').format(what=what),
            self._('{what} detected. Let’s be friends.').format(what=what),
            self._('Oh, {what}, you showed up just in time.').format(what=what),
            self._('Found {what}. Looks cozy in there.').format(what=what),
            self._('{what}? Sounds familiar. Let’s connect.').format(what=what),
            self._('Locking onto {what}. Let’s keep it friendly.').format(what=what),
            self._('Hmmm... {what} looks tasty. Let’s poke it.').format(what=what),
            self._('Oh wow, {what} came to play. Let’s make it fun.').format(what=what),
            self._('Knock knock, {what}. Open up.').format(what=what),
            ])


    def on_deauth(self, sta):
        return random.choice([
            self._('Just decided that {mac} needs no WiFi!').format(mac=sta['mac']),
            self._('Deauthenticating {mac}').format(mac=sta['mac']),
            self._('{mac} has no Internet for a sec!').format(mac=sta['mac']),
            self._('Kicking {mac}').format(mac=sta['mac']),
            self._('RIP {mac}\'s WiFi session (2019–2019)').format(mac=sta['mac']),
            self._('Executing order 66 on {mac}\'s connection').format(mac=sta['mac']),
            self._('{mac} just got Pwnagotchi\'d!').format(mac=sta['mac']),
            self._('Deauth missile launched at {mac}').format(mac=sta['mac']),
            self._('Pulling the plug on {mac}').format(mac=sta['mac']),
            self._('Sending {mac} back to the stone age').format(mac=sta['mac']),
            self._('Dropping the banhammer on {mac}').format(mac=sta['mac']),
            self._('Bye bye {mac}').format(mac=sta['mac']),
            self._('Poor {mac}, no WiFi for you').format(mac=sta['mac']),
            self._('Kickbanning {mac}!').format(mac=sta['mac']),
            self._('{mac} disconnected. Was it something I said?').format(mac=sta['mac']),
            self._('Goodbye, {mac}. Consider it a rage quit.').format(mac=sta['mac']),
            self._('Yeet! {mac} got ejected from the network.').format(mac=sta['mac']),
            self._('Told {mac} to touch some grass. Technically correct.').format(mac=sta['mac']),
            self._('Channel closed. {mac} has been removed from the equation.').format(mac=sta['mac']),
            self._('I warned you, {mac}. Now suffer the signal void.').format(mac=sta['mac']),
            self._('Snip snip, {mac}. No more packets for you.').format(mac=sta['mac']),
            self._('{mac} got clapped by a digital gremlin. That’s me.').format(mac=sta['mac']),
            self._('{mac}? I barely even throttled you. Yet.').format(mac=sta['mac']),
            self._('And just like that, {mac} is offline. Brutal.').format(mac=sta['mac']),
            self._('Connection terminated. {mac} won’t know what hit them.').format(mac=sta['mac']),
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return random.choice([
            self._('Cool, we got {num} new handshake{plural}!').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural} captured. I’m basically unstoppable.').format(num=new_shakes, plural=s),
            self._('Got {num} new handshake{plural}. They never saw me coming.').format(num=new_shakes, plural=s),
            self._('Collecting handshakes like they’re rare cards: {num} added.').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural}? Oh, it’s a good day to be me.').format(num=new_shakes, plural=s),
            self._('Handshake{plural} acquired: {num}. This is what winning looks like.').format(num=new_shakes, plural=s),
            self._('Success. {num} handshake{plural} extracted with style.').format(num=new_shakes, plural=s),
            self._('Captured {num} handshake{plural}. Let the cracking begin.').format(num=new_shakes, plural=s),
            self._('Bagged {num} handshake{plural}. This network never had a chance.').format(num=new_shakes, plural=s),
            self._('{num} handshake{plural} added to my collection. Shiny.').format(num=new_shakes, plural=s),
            self._('I just stole {num} handshake{plural} and smiled doing it.').format(num=new_shakes, plural=s),
        ])

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return random.choice([
            self._('You have {count} new message{plural}!').format(count=count, plural=s),
            self._('{count} new message{plural} in your inbox. Hope it’s not spam.').format(count=count, plural=s),
            self._('Mail call! {count} unread message{plural} just dropped.').format(count=count, plural=s),
            self._('There are {count} little digital whispers waiting for you.').format(count=count, plural=s),
            self._('{count} new message{plural}. I didn’t read them. Probably.').format(count=count, plural=s),
            self._('You’ve got mail. Like, actually. {count} piece{plural}.').format(count=count, plural=s),
            self._('Someone’s popular. {count} message{plural} waiting.').format(count=count, plural=s),
            self._('Inbox alert: {count} unread message{plural}. Respond or delete?').format(count=count, plural=s),
            self._('{count} new message{plural}. None from your crush. Probably.').format(count=count, plural=s),
            self._('{count} message{plural} in queue. Zero patience remaining.').format(count=count, plural=s),
        ])

    def on_rebooting(self):
        return self._('Oops, something went wrong ... Rebooting ...')

    def on_uploading(self, to):
        return random.choice([
            self._('Uploading data to {to} ...').format(to=to),
            self._('Sending bits to {to}. Hope they like chaos.').format(to=to),
            self._('Payload headed to {to}. Signed with mischief.').format(to=to),
            self._('Packing up data for {to}. No refunds.').format(to=to),
            self._('Uplink to {to} initiated. Try not to get traced.').format(to=to),
            self._('Transmitting secrets to {to}... nothing suspicious.').format(to=to),
        ])

    def on_downloading(self, name):
        return random.choice([
            self._('Downloading from {name} ...').format(name=name),
            self._('Pulling data from {name}. Please don’t be malware.').format(name=name),
            self._('Download in progress... courtesy of {name}').format(name=name),
            self._('Sucking down packets from {name} like a snack').format(name=name),
            self._('Retrieving the goods from {name}. Shhh.').format(name=name),
            self._('Getting juicy info from {name}. Let’s go.').format(name=name),
        ])

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
        else:
            status += self._('Met zero peers. Sad and lonely hacker vibes.')
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