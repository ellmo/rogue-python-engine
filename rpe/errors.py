class RpeError(Exception):
  pass

class NoPlayerStartError(RpeError):
  def __str__(self):
        return repr('Loaded map has no player start.')

class MultiplePlayerStartError(RpeError):
  def __str__(self):
    return repr('Loaded map has multiple player starts.')
