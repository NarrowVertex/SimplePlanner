class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)

            if cls not in cls._instances:
                cls._instances[cls] = instance
        return cls._instances[cls]

    def is_initialized(cls):
        return cls in cls._instances

    @property
    def instances(self):
        return self._instances
