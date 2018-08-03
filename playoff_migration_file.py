import os
from json import dump

from refactor_playoff_migration import GetPlayoffDesign, GetPlayoffData, \
    Utility


class Export(object):

    def __init__(self):
        self.base_dir = "playoff-data"
        self.proj_path = os.getcwd() + "\\" + self.base_dir + "\\"

        if not os.path.isdir(self.proj_path):
            os.mkdir(self.base_dir)

        playoff_client = Utility.get_playoff_client(
            "GAMELABNOTARGETV01_CLIENT_ID",
            "GAMELABNOTARGETV01_CLIENT_SECRET"
        )

        self.design_getter = GetPlayoffDesign(playoff_client)
        self.data_getter = GetPlayoffData(playoff_client)


class ExportRawDesign(Export):

    def __init__(self):
        super().__init__()

        self.dir_name = "design-raw"
        self.path = self.proj_path + self.dir_name + "\\"

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def export_teams(self):
        """Saves raw teams design data from the original game in a .json
        file
        """
        with open(self.path + "teams_raw_design.json", "w+") as file:
            cloned_teams_design = []
            teams_design = self.design_getter.get_teams_design()

            for team in teams_design:
                single_team_design = self.design_getter\
                    .get_single_team_design(team['id'])

                cloned_teams_design.append(single_team_design)

            dump(cloned_teams_design, file, sort_keys=True, indent=4)

    def export_metrics(self):
        """Saves raw metrics design data from the original game in a .json
        file
        """
        with open(self.path + "metrics_raw_design.json", "w+") as file:
            cloned_metrics_design = []
            metrics_design_id = self.design_getter.get_metrics_design()

            for metric in metrics_design_id:
                single_metric_design = self.design_getter\
                    .get_single_metric_design(metric['id'])

                cloned_metrics_design.append(single_metric_design)

            dump(cloned_metrics_design, file, sort_keys=True, indent=4)

    def export_actions(self):
        """Saves raw actions design data from the original game in a .json
        file
        """
        with open(self.path + "actions_raw_design.json", "w+") as file:
            cloned_actions_design = []
            actions_design = self.design_getter.get_actions_design()

            for action in actions_design:
                single_action_design = self.design_getter\
                    .get_single_action_design(action['id'])

                cloned_actions_design.append(single_action_design)

            dump(cloned_actions_design, file, sort_keys=True, indent=4)

    def export_leaderboards(self):
        """Saves raw leaderboards design data from the original game in a .json
        file
        """
        with open(self.path + "leadboards_raw_design.json", "w+") as file:
            cloned_leaderboards_design = []
            leaderboards_id = self.design_getter.get_leaderboards_design()

            for board in leaderboards_id:
                single_design = self.design_getter\
                    .get_single_leaderboard_design(board['id'])

                cloned_leaderboards_design.append(single_design)

            dump(cloned_leaderboards_design, file, sort_keys=True, indent=4)


class ExportRawData(Export):

    def __init__(self):
        super().__init__()

        self.dir_name = "data-raw"
        self.path = self.proj_path + self.dir_name + "\\"

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def export_teams(self):
        """Saves raw instances of all teams from the original game in a .json
        format
        """
        with open(self.path + "teams_raw.json", "w+") as file:
            cloned_teams_instances = []
            teams_by_id = self.data_getter.get_teams_by_id()

            for team in teams_by_id:
                team_instance_info = self.data_getter.get_team_info(team)

                cloned_teams_instances.append(team_instance_info)

            dump(cloned_teams_instances, file, sort_keys=True, indent=4)

    def export_players(self):
        """Saves raw profile data of all players from the original game in a
        .json format
        """
        with open(self.path + "players_raw.json", "w+") as file:
            cloned_players = []
            players_by_id = self.data_getter.get_players_by_id()

            for player in players_by_id:
                player_instance_info = self.data_getter\
                    .get_player_profile(player)

                cloned_players.append(player_instance_info)

            dump(cloned_players, file, sort_keys=True, indent=4)

    def export_players_feed(self):
        """Saves raw feed data of all players from the original game in a
        .json format
        """
        with open(self.path + "players_feed_raw.json", "w+") as file:
            cloned_feed = {}
            players_id = self.data_getter.get_players_by_id()

            for player in players_id:
                player_feed = self.data_getter.get_player_feed(player)

                cloned_feed.update({player: player_feed})

            dump(cloned_feed, file, sort_keys=True, indent=4)


class ExportDesign(Export):

    def __init__(self):
        super().__init__()

        self.dir_name = "design"
        self.path = self.proj_path + self.dir_name + "\\"

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def export_teams(self):
        """ Create json file containing each team design of the original
        game
        """
        with open(self.path + "teams_design.json", "w+") as file:
            teams_design_clone = []
            teams_design = self.design_getter.get_teams_design()

            for team in teams_design:
                single_team_design = self.design_getter.get_single_team_design(
                    team['id'])

                team_design_data = {
                    'name': single_team_design['name'],
                    'id': single_team_design['id'],
                    'permissions': single_team_design['permissions'],
                    'creator_roles': single_team_design['creator_roles'],
                    'settings': single_team_design['settings'],
                    '_hues': single_team_design['_hues']
                }

                if 'description' in single_team_design.keys():
                    team_design_data.update(
                        {'description': single_team_design['description']})

                teams_design_clone.append(team_design_data)

            dump(teams_design_clone, file, sort_keys=True, indent=4)

    def export_metrics(self):
        """ Create json file containing each metric design of the original
        game
        """
        with open(self.path + "metric_design.json", "w+") as file:
            cloned_metrics = []
            metrics_design = self.design_getter.get_metrics_design()

            for metric in metrics_design:
                single_metric_design = self.design_getter\
                    .get_single_metric_design(metric['id'])

                metric_design_data = {
                    "id": single_metric_design['id'],
                    "name": single_metric_design['name'],
                    "type": single_metric_design['type'],
                    "constraints": single_metric_design['constraints']
                }

                if "description" in single_metric_design.keys():
                    metric_design_data.update(
                        {"description": single_metric_design["description"]})

                cloned_metrics.append(metric_design_data)

            dump(cloned_metrics, file, sort_keys=True, indent=4)

    def export_actions(self):
        """ Create json file containing each action design of the original
        game
        """
        with open(self.path + "actions_design.json", "w+") as file:
            cloned_actions = []
            actions_design = self.design_getter.get_actions_design()

            for action in actions_design:
                single_action_design = self.design_getter\
                    .get_single_action_design(action['id'])

                cloned_actions.append(single_action_design)

            dump(cloned_actions, file, sort_keys=True, indent=4)

    def export_leaderboards(self):
        """ Create json file containing each leaderboard design of the original
        game
        """
        with open(self.path + "leaderboards_design.json", "w+") as file:
            cloned_leaderboards = []
            leaderboards = self.design_getter.get_leaderboards_design()

            for board in leaderboards:
                single_board = self.design_getter\
                    .get_single_leaderboard_design(board['id'])

                board_data = {
                    "id": single_board['id'],
                    "name": single_board['name'],
                    "entity_type": single_board['entity_type'],
                    "scope": single_board['scope'],
                    "metric": single_board['metric'],
                    "cycles": single_board['cycles']
                }

                if "description" in single_board.keys():
                    board_data.update(
                        {"description": single_board["description"]})

                cloned_leaderboards.append(board_data)

            dump(cloned_leaderboards, file, sort_keys=True, indent=4)


class ExportData(Export):

    def __init__(self):
        super().__init__()

        self.dir_name = "data"
        self.path = self.proj_path + self.dir_name + "\\"

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    def export_teams(self):
        """ Create json file containing each team instance of the original
        game
        """
        with open(self.path + "teams.json", "w+") as file:
            cloned_teams_instances = []
            teams_by_id = self.data_getter.get_teams_by_id()

            for team in teams_by_id:
                team_data = self.data_getter.get_team_info(team)

                cloned_team_data = {
                    'id': team_data['id'],
                    'name': team_data['name'],
                    'access': team_data['access'],
                    'definition': team_data['definition']['id']
                }

                cloned_teams_instances.append(cloned_team_data)

            dump(cloned_teams_instances, file, sort_keys=True, indent=4)

    def export_players(self):
        """ Create json file containing id and alias of each player of the
        original game
        """
        with open(self.path + "players.json", "w+") as file:
            cloned_players = []
            players_by_id = self.data_getter.get_players_by_id()

            for player in players_by_id:
                player_data = self.data_getter.get_player_profile(player)

                cloned_player_data = {
                    'id': player_data['id'],
                    'alias': player_data['alias']
                }

                cloned_players.append(cloned_player_data)

            dump(cloned_players, file, sort_keys=True, indent=4)

    def export_players_in_team(self):
        """ Create json file containing the team of each player of the
        original game
        """
        with open(self.path + "players_in_team.json", "w+") as file:
            cloned_players_in_team = {}
            players_by_id = self.data_getter.get_players_by_id()

            for player in players_by_id:
                player_profile = self.data_getter.get_player_profile(player)

                for team in player_profile['teams']:

                    cloned_team_player = {
                        "requested_roles": {
                            team['roles'][0]: True
                        },
                        "player_id": player
                    }

                    team_id = team['id']

                    if not (team_id in cloned_players_in_team.keys()):
                        cloned_players_in_team.update({team_id: []})
                        cloned_players_in_team[team_id]\
                            .append(cloned_team_player)
                    else:
                        cloned_players_in_team[team_id]\
                            .append(cloned_team_player)

            dump(cloned_players_in_team, file, sort_keys=True, indent=4)

    def export_players_feed(self):
        """ Create json file containing the activity feed of each player of the
        original game
        """
        with open(self.path + "players_feed.json", "w+") as file:
            cloned_players_feed = {}
            players_id = self.data_getter.get_players_by_id()

            for player in players_id:
                player_feed = self.data_getter.get_player_feed(player)

                for feed in player_feed:
                    player_single_feed = {}

                    if feed['event'] == 'action':
                        player_single_feed.update({"id": feed['action']['id']})
                        player_single_feed.update(
                            {"variables": feed['action']['vars']})
                        player_single_feed.update({"scopes": feed['scopes']})

                        if not (player in cloned_players_feed.keys()):
                            cloned_players_feed.update({player: []})
                            cloned_players_feed[player]\
                                .append(player_single_feed)
                        else:
                            cloned_players_feed[player]\
                                .append(player_single_feed)

            dump(cloned_players_feed, file, sort_keys=True, indent=4)


