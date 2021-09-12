class Logger():
  def __init__(self, **params):
    self.report_level = params.get("level", 0)
    pass

  def info(self, msg):
    if self.report_level > 0:
      print(msg)

  def debug(self, msg):
    if self.report_level > 1:
      print(msg)