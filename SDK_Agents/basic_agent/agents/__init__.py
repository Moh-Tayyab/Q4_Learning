# agents/__init__.py

class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class Runner:
    @staticmethod
    def run_sync(agent, query):
        class Result:
            final_output = f"Simulated answer for: '{query}' (from agent '{agent.name}')"
        return Result()
    