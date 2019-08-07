# ColabComponent
A React.js inspired Component for building a simple reactive UI in Google Colaboratory.

### Why?
Sometimes there is some manual work that has to be done with your data. Instead of building a custom desktop app, why not do so in Colab?

I built this component inspired by the react framework, which provides in my opinion the best tools for quick prototype-like development ideal for custom data exploring and data analysis tools.

### How?
The `google.colab` package offers an interface to run python functions in the `output`. Combine that with the fact that python notebooks can render full on HTML and you can build UIs using python, HTML, css and javascript!

## Install
In a cell run:

```bash
!pip3 install ColabComponent
```

All the required dependencies are installed in the enviroment provided by google.

## How to use?
The package utilises Object-Oriented inheritance and is based around the basic class `Component`.

### Component API
| property name | type | description | overridable |
|---|---|---|---|
| render | method | the basic method, where the ui and effects are defined | &#x2611; |
| component_did_mount | method | a hook that is called, when the component is mounted | &#x2611; |
| component_did_update | method | a hook that is called, when the component is updated | &#x2611; |
| display | method | run to display the component | &#x2612; |
| register_effect | method | registers a python function such that it can be used within the HTML code | &#x2612; |
| state | dict | holds the info about the state of the component | &#x2612; |
| set_state | method | the preferred way of updating the component state | &#x2612; |

## Example
```python
from ColabComponent import Component

class Counter(Component):
  def __init__(self):
    super().__init__()
    self.state = {
        'number': 1
    }

    self.use_add = self.register_effect('add', self.add)

  def render(self):
    return f'''
      <h1>{self.state['number']}</h1>
      <button onclick="{self.use_add()}">+1</button>
    '''

  def component_did_mount(self):
    print('mounted')

  def component_did_update(self):
    print('updated')

  def add(self):
    self.set_state({
        'number': self.state['number'] + 1
    })

Counter().display()
```

#### Effect
![clicker_example](https://i.imgur.com/ejCkrpV.gif)
