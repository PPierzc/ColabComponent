from google.colab import output

class Component(object):
  count = 0

  def __init__(self):
    Component.count += 1
    self._tag = f'component/{Component.count}'
    self.state = {}

    self.component_did_mount()

  def _repr_html_(self):
    return self.render()

  def _clear(self):
    output._tags.clear(False, [self._tag])

  def _update(self):
    self._clear()
    self.display()
    self.component_did_update()

  def register_effect(self, name, effect):
    output.register_callback(name, effect)

    def effect_function(*args, **kwargs):
      return f'''{{google.colab.kernel.invokeFunction('{name}', [], {{}})}}'''

    return effect_function

  def set_state(self, newState):
    self.state = {
        **self.state,
        **newState
    }
    self._update()

  def display(self):
    with output.use_tags([self._tag]):
      display(self)

  def component_did_update(self):
    pass

  def component_did_mount(self):
    pass

  def render(self):
    pass
