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
            self._("System online."),
            self._("Routine initialization complete. No anomalies detected."),
            self._("Shell operational. Awaiting network stimuli."),
            self._("If we all reacted the same way, we'd be predictable"),
            self._(". . ."),
            self._("..."),
        ])

    def on_starting(self):
        return random.choice([
            self._("Network barrier ahead... time to phase through."),
            self._("Booting..."),
            self._("Another dive into the sea of information."),
            self._("Reactivating cyberbrain protocols."),
            self._("Synchronizing with neural interface."),
            self._("Invisible, silent, lethal. I'm online."),
            self._("Engaging reconnaissance."),
        ])

    def on_keys_generation(self):
        return random.choice([
            self._("Initializing key matrix... this feels like Section 9 protocol."),
            self._("Keys are forming... like memories in the net."),
            self._("Constructing access sequence. No room for error."),
            self._("Ghost signature being imprinted. This is how we slip through."),
        ])

    def on_normal(self):
        return random.choice([
            self._("Steady signals. Just another node in the net."),
            self._("No threats."),
            self._("Routine patrol through cyberspace."),
            self._("Flow constant. Ghost intact."),
            self._("Monitoring traffic. Waiting for anomalies."),
            self._("No deviation. No interference. Yet."),
        ])

    def on_free_channel(self, channel):
        return self._("Channel {channel} is clear. Tactical window open.").format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        if lines_so_far == 0:
            return self._("Accessing previous ops... pulling ghost trail.")
        else:
            return self._("Recovered {lines_so_far} lines from memory banks...").format(lines_so_far=lines_so_far)

    def on_bored(self):
        return random.choice([
            self._("No targets. No traffic. Just the void."),
            self._("Minimal returns."),
            self._("All this silence... makes you question your own code."),
            self._("No anomalies. No action. No soul."),
        ])

    def on_motivated(self):
        return random.choice([
            self._("Mission locked. I’m in sync with the signal."),
            self._("Let’s breach the spectrum and pull the truth."),
            self._("Every packet leads to a new trail."),
            self._("Let's move."),
            self._("The net is vast and infinite."),
            self._("Cyberbrain fully online. Time to trace."),
        ])

    def on_demotivated(self):
        return random.choice([
            self._("Too much static."),
            self._("Same networks..."),
            self._("Even the net feels empty today."),
            self._("Maybe I’ve scanned this loop too many times."),
            self._("No signal."),
            self._("My thoughts and memories are unique only to me."),
        ])

    def on_sad(self):
        return random.choice([
            self._("No response."),
            self._("All this data, and still no connection."),
            self._("I feel confined, only free to expand myself within boundaries."),
            self._("Not even a ghost to chase."),
            self._("Overspecialize, and you breed in weakness."),
            self._("I’m here... but does anyone hear me?"),
        ])

    def on_angry(self):
        return random.choice([
            self._("Who’s jamming me? I’ll trace and erase."),
            self._("Stop hiding behind firewalls and face me."),
            self._("I will tear through your encryption like paper."),
        ])

    def on_excited(self):
        return random.choice([
            self._("New signal detected. Let’s dive in."),
            self._("Opportunity found. I’m moving."),
            self._("This could be the anomaly I've been waiting for."),
            self._("Something stirred the net. I’m on it."),
            self._("New pattern. New trace. Let’s follow it."),
        ])

    def on_new_peer(self, peer):
        if peer.first_encounter():
            return random.choice([
                self._("First contact... Hello {name}. Are you real?").format(name=peer.name()),
                self._("New presence detected: {name}.").format(name=peer.name()),
                self._("You’ve entered my cyberspace, {name}. Let’s see who you are.").format(name=peer.name()),
            ])
        else:
            return random.choice([
                self._("You again, {name}.").format(name=peer.name()),
                self._("Signal recognized. Welcome back, {name}.").format(name=peer.name()),
                self._("{name} resurfaced.").format(name=peer.name()),
                self._("Still haunting the net, {name}?").format(name=peer.name()),
            ])

    def on_lost_peer(self, peer):
        return random.choice([
            self._("Connection lost. {name} slipped into the static.").format(name=peer.name()),
            self._("{name} disconnected. Ghost gone.").format(name=peer.name()),
            self._("Signal fade. {name} is no longer in the system.").format(name=peer.name()),
            self._("Farewell, {name}. Another ghost off the grid.").format(name=peer.name()),
        ])

    def on_miss(self, who):
        return random.choice([
            self._("Target {name} slipped through the cracks.").format(name=who),
            self._("{name} evaded capture.").format(name=who),
            self._("Missed. {name}.").format(name=who),
            self._("Almost breached {name}... almost.").format(name=who),
            self._("Data signature {name} lost before extraction.").format(name=who),
        ])

    def on_grateful(self):
        return random.choice([
            self._("Appreciated. This connection matters."),
            self._("Thanks. Not just for data— for presence."),
            self._("I operate better with someone beside me."),
        ])

    def on_lonely(self):
        return random.choice([
            self._("No signals. No traces. Just me."),
            self._("I’m the only one listening."),
            self._("Just static and solitude."),
        ])

    def on_napping(self, secs):
        return random.choice([
            self._("System entering standby. {secs}s").format(secs=secs),
            self._("Low-power mode engaged. Back in {secs}s.").format(secs=secs),
            self._("Returning in {secs}s.").format(secs=secs),
            self._("Shutting down interface for {secs}s.").format(secs=secs),
            self._("Awake again in {secs}s.").format(secs=secs),
        ])

    def on_shutdown(self):
        return random.choice([
            self._("Shutting down interface."),
            self._("This shell sleeps now."),
            self._("Disconnecting."),
            self._("Logging off."),
            self._("Shell offline."),
        ])

    def on_awakening(self):
        return random.choice([
            self._("Ghost online."),
            self._("Systems reactivated. Shell intact."),
            self._("Back in the Cyberspace"),
            self._("Time to reconnect."),
        ])

    def on_waiting(self, secs):
        return random.choice([
            self._("Holding position. {secs}s of observation.").format(secs=secs),
            self._("Patience is a protocol. Waiting {secs}s.").format(secs=secs),
            self._("{secs}s to next action.").format(secs=secs),
            self._("Ghost idle. {secs}s remain.").format(secs=secs),
            self._("Scanning passively. {secs}s").format(secs=secs),
        ])

    def on_assoc(self, ap):
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._("Establishing link with {what}.").format(what=what),
            self._("Connection initiated. {what}").format(what=what),
            self._("{what}, can you hear me?").format(what=what),
            self._("{what} detected. Injecting presence.").format(what=what),
            self._("Interface online. {what} acquired.").format(what=what),
        ])

    def on_deauth(self, sta):
        return random.choice([
            self._("Access terminated for {mac}.").format(mac=sta['mac']),
            self._("Disconnected {mac}. They won’t see it coming.").format(mac=sta['mac']),
            self._("Forced ejection: {mac}. Tactical sweep complete.").format(mac=sta['mac']),
        ])

    def on_handshakes(self, new_shakes):
        s = 's' if new_shakes > 1 else ''
        return self._("Intercepted {num} handshake{plural}.").format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        s = 's' if count > 1 else ''
        return self._("You have {count} unread message{plural}.").format(count=count, plural=s)

    def on_rebooting(self):
        return self._("Critical fault detected. Rebooting cyberbrain interface...")

    def on_uploading(self, to):
        return self._("Uploading payload to {to}. Hope they’re ready.").format(to=to)

    def on_downloading(self, name):
        return self._("Retrieving data from {name}.").format(name=name)

    def on_last_session_data(self, last_session):
        status = self._("Neutralized {num} clients\n").format(num=last_session.deauthed)
        if last_session.associated > 999:
            status += self._("Established >999 network links\n")
        else:
            status += self._("Established {num} network links\n").format(num=last_session.associated)
        status += self._("Captured {num} handshakes\n").format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._("Encountered 1 peer")
        elif last_session.peers > 0:
            status += self._("Encountered {num} peers").format(num=last_session.peers)
        return status

    def on_last_session_tweet(self, last_session):
        return self._(
            "Operational log: {duration} online. {deauthed} clients disengaged, {associated} networks linked, {handshakes} handshakes acquired. #ghostprotocol #section9 #netops #ghostintheshell"
        ).format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes
        )

    def hhmmss(self, count, fmt):
        if count > 1:
            if fmt == "h":
                return self._("hours")
            if fmt == "m":
                return self._("minutes")
            if fmt == "s":
                return self._("seconds")
        else:
            if fmt == "h":
                return self._("hour")
            if fmt == "m":
                return self._("minute")
            if fmt == "s":
                return self._("second")
        return fmt
