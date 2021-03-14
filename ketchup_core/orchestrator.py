from ketchup_domain.configuration import Configuration
from motivator import Motivator
from pomodoro import Pomodoro


# An orchestrator is a component (e.g. context)
# with the purpose (responsibility) of creating and storing
# other components and mediating the interaction among them
class KetchupOrchestrator:
    def __init__(self):
        # Do some initialization
        # 1. What are the components that this class should store?
        #    Create them as self.component
        #    These are usually components that store a *state*,
        #    that is, something that needs to be remembered
        #    (e.g. the progress of the pomodoro), or that it's
        #    too cumbersome to load every time (e.g. sentences)
        # 2. What things should be instead processed and then let go?

        # E.g.:
        self.config = Configuration()
        self.motivator = Motivator(self.config)  # E.g. of use of config
        self.pomodoro = Pomodoro()
        # ...

    # The following method runs the main loop of the app
    # Its name is important because it is related to the idea of
    # a Thread/Process object. If the orchestrator becomes
    # a subclass of these classes, the run method is usually central
    def run(self):
        pass
        # Usually a loop goes like this:
        # 1. Initialize whatever needed (e.g. listeners objects)
        # 2. Listen to (user) input
        # 3. Parse input (i.e. decide what to do based on input)
        # 4. Execute associated function
        #   where are these functions stored?
        #   how are they selected?
        #   where are they implemented?
        # 5. Provide output
        # 6. Go to 2, unless some (exit) condition is met
        # These steps usually need to be guarded for exceptions (try-except)
