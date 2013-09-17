class CrawlerError(Exception):
  pass

class NoPlayerStartError(CrawlerError):
  pass

class MultiplePlayerStartError(CrawlerError):
  pass