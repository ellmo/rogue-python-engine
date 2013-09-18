class CrawlerError(Exception):
  pass

class NoPlayerStartError(CrawlerError):
  def __str__(self):
        return repr('Loaded map has no player start.')

class MultiplePlayerStartError(CrawlerError):
  def __str__(self):
    return repr('Loaded map has multiple player starts.')
