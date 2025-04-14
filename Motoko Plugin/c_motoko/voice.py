
import gettext
import os
import random


class Voice:
    def __init__(self, lang):
        # System initialization. Localization protocols engaged.
        localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
        translation = gettext.translation(
            'voice', localedir,
            languages=[lang],
            fallback=True,
        )
        translation.install()
        self._ = translation.gettext

    def custom(self, s):
        # Relaying external input verbatim.
        return s

    def default(self):
        # Standby mode. Monitoring ambient data streams.
        return self._('System idle. Processing...')

    def on_starting(self):
        # Unit activation sequence.
        return random.choice([
            self._('Section 9 cyberbrain interface active.'),
            self._('Commencing network reconnaissance operation.'),
            self._('Bringing systems online. Ready for deployment.'),
            self._('Ghost synchronization complete. Unit ready.'),
            self._('Initializing tactical network analysis suite.'),
        ])

    def on_keys_generation(self):
        # Security protocols require key generation.
        return random.choice([
            self._('Generating cryptographic keys. Maintain system integrity.')])

    def on_normal(self):
        # Passive monitoring state. Scanning environment.
        return random.choice([
            '',
            '...',
            self._('Monitoring local network traffic.'),
            self._('Sensors active. Nominal status.'),
            self._('Analyzing packet flow.')
        ])

    def on_free_channel(self, channel):
        # Tactical advantage identified.
        return self._('Channel {channel} is clear. Optimal for data acquisition or covert transmission.').format(channel=channel)

    def on_reading_logs(self, lines_so_far=0):
        # Data analysis subroutine.
        if lines_so_far == 0:
            return self._('Accessing previous operational log data...')
        else:
            return self._('Processed {lines_so_far} log entries. Continuing analysis...').format(lines_so_far=lines_so_far)

    def on_bored(self):
        # Operational tempo low. Awaiting targets of opportunity.
        return random.choice([
            self._('No significant network activity detected.'),
            self._('Environment scan yields minimal targets. Standby.'),
            self._('Awaiting actionable intelligence.')])

    def on_motivated(self, reward):
        # Positive reinforcement acknowledged. Mission parameters likely met.
        return self._('Objective criteria met. Operational efficiency maximized.')

    def on_demotivated(self, reward):
        # Negative feedback loop detected. Re-evaluating strategy.
        return self._('Suboptimal performance registered. Analysis required.')

    def on_sad(self):
        # System state reflects lack of meaningful interaction or data. Contemplative state.
        return random.choice([
            self._('Network silence... A ghost feels thin without the net.'),
            self._('Is this the extent of this node\'s consciousness?'),
            self._('Minimal interaction detected. Reflecting on data boundaries.'),
            '...'])

    def on_angry(self):
        # External interference or system inefficiency detected. Minor frustration possible.
        return random.choice([
            '...Tch.', # A characteristic sound of annoyance
            self._('Operational parameters compromised.'),
            self._('Inefficiency detected. Rectification required.'),
            self._('Analyzing system interference.')])

    def on_excited(self):
        # Target-rich environment or significant data influx. Optimal operational state.
        return random.choice([
            self._('High-density target environment detected. Engaging.'),
            self._('Multiple access points available. Maximizing data capture.'),
            self._('Network infiltration vectors confirmed.'),
            self._('Data stream optimal. Processing at maximum capacity.'),
            self._('Engaging multiple targets simultaneously.')])

    def on_new_peer(self, peer):
        # Detecting another networked entity, possibly Section 9 or unknown.
        if peer.first_encounter():
            return random.choice([
                self._('New cyberbrain signature detected: {name}. Analyzing profile.').format(name=peer.name()),
                self._('Unit {name} identified. Establishing contact protocols.').format(name=peer.name())])
        else:
            return random.choice([
                self._('Unit {name} re-acquired on sensors.').format(name=peer.name()),
                self._('Acknowledged, {name}. Maintain operational awareness.').format(name=peer.name()),
                self._('Tracking unit {name} within operational zone.').format(name=peer.name())])

    def on_lost_peer(self, peer):
        # Loss of signal from networked entity.
        return random.choice([
            self._('Signal lost for unit {name}.').format(name=peer.name()),
            self._('{name} has left the network perimeter.').format(name=peer.name()),
            self._('Lost tracking on {name}. Updating network map.').format(name=peer.name())])

    def on_miss(self, who):
        # Target evaded capture or interaction.
        return random.choice([
            self._('Target {name} evaded handshake capture.').format(name=who),
            self._('Connection attempt with {name} failed.').format(name=who),
            self._('Intercept failed on {name}. Recalculating approach.').format(name=who)])

    def on_grateful(self):
        # Acknowledging successful cooperation or support from peers.
        return random.choice([
            self._('Synchronized actions successful. Teamwork protocols validated.'),
            self._('Support from allied units acknowledged and deemed effective.')])

    def on_lonely(self):
        # Operating without peer support or interaction.
        return random.choice([
            self._('No allied signals detected in vicinity. Operating solo.'),
            self._('Isolated network presence confirmed.'),
            self._('Scanning for Section 9 network nodes... Negative.')])

    def on_napping(self, secs):
        # Entering low-power or maintenance cycle.
        return random.choice([
            self._('Entering standby mode for {secs} seconds. Conserving energy.').format(secs=secs),
            self._('System maintenance cycle initiated ({secs}s).'),
            self._('Reducing operational footprint for {secs}s.').format(secs=secs)])

    def on_shutdown(self):
        # Terminating operations.
        return random.choice([
            self._('Mission complete. Initiating shutdown sequence.'),
            self._('Terminating processes. Disconnecting from network.')])

    def on_awakening(self):
        # Resuming operations from standby or boot.
        return random.choice(['Systems online.', 'Reinitializing... Operation resumed.'])

    def on_waiting(self, secs):
        # Tactical pause or holding pattern.
        return random.choice([
            self._('Holding position for {secs} seconds. Monitoring...').format(secs=secs),
            self._('Tactical pause engaged ({secs}s). Awaiting optimal conditions.').format(secs=secs),
            '... Maintaining vigilance. ({secs}s)'.format(secs=secs)])

    def on_assoc(self, ap):
        # Establishing connection with a network access point.
        ssid, bssid = ap['hostname'], ap['mac']
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid
        return random.choice([
            self._('Attempting interface with node {what}.').format(what=what),
            self._('Establishing secure connection to {what}.').format(what=what),
            self._('Accessing network via {what}.').format(what=what)])

    def on_deauth(self, sta):
        # Executing denial-of-service on a specific client MAC.
        return random.choice([
            self._('Executing network denial protocol against {mac}.').format(mac=sta['mac']),
            self._('Disconnecting target {mac} from network access point.').format(mac=sta['mac']),
            self._('Counter-access measure deployed: Deauthenticating {mac}.').format(mac=sta['mac'])])

    def on_handshakes(self, new_shakes):
        # Successful capture of authentication data.
        s = 's' if new_shakes > 1 else ''
        return self._('Acquired {num} authentication handshake{plural}. Data secured.').format(num=new_shakes, plural=s)

    def on_unread_messages(self, count, total):
        # Incoming data or communication.
        s = 's' if count > 1 else ''
        return self._('{count} new data packet{plural} received. Pending analysis.').format(count=count, plural=s)

    def on_rebooting(self):
        # Critical error requiring system restart.
        return self._("System instability detected. Initiating emergency reboot sequence.")

    def on_uploading(self, to):
        # Transmitting collected data.
        return self._("Transmitting encrypted data package to secure server: {to}.").format(to=to)

    def on_downloading(self, name):
        # Receiving data or updates.
        return self._("Receiving secure data transmission from {name}.").format(name=name)

    def on_last_session_data(self, last_session):
        # Summarizing previous operational results.
        status = self._('Last Op Summary: Targets Deauthed: {num}.\n').format(num=last_session.deauthed)
        status += self._('Associated Nodes: {num}.\n').format(num=last_session.associated)
        status += self._('Handshakes Acquired: {num}.\n').format(num=last_session.handshakes)
        if last_session.peers == 1:
            status += self._('Peer Units Encountered: 1.')
        elif last_session.peers > 0:
            status += self._('Peer Units Encountered: {num}.').format(num=last_session.peers)
        else:
             status += self._('Peer Units Encountered: 0.')
        return status

    def on_last_session_tweet(self, last_session):
        # Motoko wouldn't tweet. This is framed as an internal log or report summary.
        # Hashtags kept as meta-commentary or simplified internal tags.
        return self._(
            'Operational Log: Duration {duration}. Targets neutralized (deauth): {deauthed}. Nodes interfaced: {associated}. Authentication packets secured: {handshakes}. #Section9 #NetOps #CyberSecurity #Pwnagotchi #GhostInTheShell').format(
            duration=last_session.duration_human,
            deauthed=last_session.deauthed,
            associated=last_session.associated,
            handshakes=last_session.handshakes)

    def hhmmss(self, count, fmt):
        # Standard time units, likely unchanged in her professional context.
        # Relies on gettext for potential localization nuances.
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
