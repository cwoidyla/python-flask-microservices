

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig:
    """Development configuration"""
    pass

class ProductionConfig(BaseConfig):
    """Production configuration"""
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
