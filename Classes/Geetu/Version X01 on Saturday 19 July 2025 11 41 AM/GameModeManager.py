GAME_MODES = {
    "beginner": {
        "description": "Practice tables with help and skip allowed",
        "allow_skip": True,
        "allow_pause": True,
        "show_timer": False,
        "max_questions": 10,
        "badge_criteria": {
            "consistency_days": 3
        }
    },
    "intermediate": {
        "description": "Practice with timer, no skip",
        "allow_skip": False,
        "allow_pause": True,
        "show_timer": True,
        "max_questions": 15,
    },
    "challenge": {
        "description": "Speed round with timer and no pause",
        "allow_skip": False,
        "allow_pause": False,
        "show_timer": True,
        "max_questions": 20,
        "response_time_thresholds": {
            "slow": 6,
            "very_slow": 10
        }
    }
}


class GameModeManager:
    def __init__(self, player_name):
        self.player_name = player_name
        self.current_mode = "beginner"  # default
        self.available_modes = GAME_MODES

    def set_mode(self, mode_name):
        if mode_name in self.available_modes:
            self.current_mode = mode_name
            print(f"🔁 Game mode set to: {mode_name}")
        else:
            print(f"❌ Invalid mode: {mode_name}. Defaulting to Beginner.")
            self.current_mode = "beginner"

    def get_current_mode_config(self):
        return self.available_modes[self.current_mode]

    def can_skip(self):
        return self.get_current_mode_config().get("allow_skip", False)

    def can_pause(self):
        return self.get_current_mode_config().get("allow_pause", False)

    def get_max_questions(self):
        return self.get_current_mode_config().get("max_questions", 10)

    def show_timer(self):
        return self.get_current_mode_config().get("show_timer", False)

    def get_response_time_thresholds(self):
        return self.get_current_mode_config().get("response_time_thresholds", {"slow": 8, "very_slow": 12})


# Example usage
manager = GameModeManager("Geetu")
manager.set_mode("challenge")

if manager.can_pause():
    print("⏸️ Pause allowed")
else:
    print("🚫 No pausing in this mode")

print(f"Max Questions: {manager.get_max_questions()}")
