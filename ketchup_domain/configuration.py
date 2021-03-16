# This class should allow a number of operations related
# to the configuration of the whole program
class Configuration:
    def __init__(self):
        self.pomodoro_duration

        # See the functionalities section in the architecture document
        # to see what variables should be present in this class
        # (i.e. what the user can configure)
        # Remember, however, that we can use this class to store
        # data, such as paths, parameters and such, that cannot be
        # changed by the user, but that can and should be passed around
        # within the application. This distinction will be important later.
        # Remember there may be no configuration file:
        # in this case, an "empty" or "default" configuration should be
        # created, and also saved, e.g.
        self._pomodoro_duration = 25

        pass

    def save_configuration(self, path: str) -> None:
        # What type of file should the configuration be?
        # Perhaps a json? A xml?
        # How would you translate the single variables of this object
        # into something that can be easily parsed into that format?
        pass

    # Should follow a number of what are called "getters" and "setters"
    # These are simple functions, that abstract and make "safe" the
    # manipulation of variables stored in this object.
    # Example of getter:
    def get_pomodoro_duration(self) -> int:
        # Is this minutes?
        return self._pomodoro_duration

    # Example of setter:
    def set_pomodoro_duration(self, new_duration: int) -> None:
        # Here you can make sure that the new value is within your
        # expectations. These "boundary" values should be specified
        # elsewhere and not hardcoded here
        pmin = self._pomodoro_min
        pmax = self._pomodoro_max
        if pmin < new_duration < pmax:
            self._pomodoro_duration = new_duration
        else:
            raise ValueError("Each pomodoro should last between"
                             + pmin + " and " + pmax + " minutes.")


