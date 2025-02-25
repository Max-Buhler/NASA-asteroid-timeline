
class UserController:
  def __init__(self, view, model):
    self.view = view
    self.model = model
  def fetchData(self):
    return self.model.fetchData()
  def run(self):
    self.view.run()