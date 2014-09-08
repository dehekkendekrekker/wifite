import datetime
import copy
import stations


class Targeter:
    wnd_opportunity = 300
    attack_attempts = 3
    attacked_targets = None
    targets = None

    def __init__(self, config):
        self.wnd_opportunity = int(config.get("main", "wnd_opportunity"))
        self.attack_attempts = int(config.get("main", "attack_attempts"))
        self.attacked_targets = stations.APs()
        self.targets = stations.APs()

    def set_possible_targets(self, aps):
        self.targets = copy.deepcopy(aps)
        self.create_target_list()

    def create_target_list(self):
        self.targets = self.get_relevant_aps()
        self.targets = self.targets.get_by_privacy("WPA")
        self.targets = self.targets.get_aps_with_associations()
        self.targets.sort_by_average_power("desc")

    def get_relevant_aps(self):
        aps = stations.APs()
        now = datetime.datetime.now()

        for ap in self.targets:
            delta = now - ap.last_time_seen
            if delta.seconds < self.wnd_opportunity:
                aps.append(ap)

        return aps


    def request_target(self):
        for ap in self.targets:
            attacked_ap = self.attacked_targets.get_by_mac(ap.mac)
            if attacked_ap:
                if attacked_ap.attack_attempts < self.attack_attempts:
                    return ap
                else:
                    continue
            else:
                return ap

        return None






