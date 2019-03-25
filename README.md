# Plant UML Design Patterns

[PlantUML](http://plantuml.com/index) code for some Design Patterns.
The syntax can be looked up on [PlantUML's class diagram documentation](http://plantuml.com/class-diagram).


## Example
![abstract_factory](https://user-images.githubusercontent.com/9216979/54890891-b84dee80-4eab-11e9-9cca-7318506eb934.png)

## Included patterns

| Creational       | Structural | Behavioral              |
| ---------------- | ---------- | ----------------------- |
| Abstract factory | Adapter    | Chain of Responsibility |
| Builder          | Bridge     | Command                 |
| Factory method   | Composite  | Interpreter             |
| Prototype        | Decorator  | Iterator                |
| Singleton        | Facade     | Mediator                |
| &nbsp;           | Flyweight  | Memento                 |
| &nbsp;           | Proxy      | Observer                |
| &nbsp;           | &nbsp;     | State                   |
| &nbsp;           | &nbsp;     | Strategy                |
| &nbsp;           | &nbsp;     | Template method         |
| &nbsp;           | &nbsp;     | Visitor                 |


## Running

If you do not intend to run locally, please have a look at the alternatives found in [this overview](http://plantuml.com/running).

### Prerequisites

To run locally, the PlantUML jar (from [PlantUML's download](http://plantuml.com/download)) site is needed.
As described on the [Getting started](http://plantuml.com/starting) site, you will also need both [Java](https://www.java.com/en/download/) and [Graphviz](https://www.graphviz.org/) installed on your machine.

### Creating the diagrams
The easiest way is to just run the included python script ([run.py](run.py)).
It checks for changes in the diagram files and only generates the new/changed/not existing ones.

```
python run.py
```

The generated diagrams are stored in the *output* folder.

To run PlantUML directly from the command line for one specific diagram, you can execute:

```
java -jar plantuml.jar diagram.txt
```


## Built With

* [PlantUML](http://plantuml.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* The pattern descriptions and overall class diagram arrangements are taken from a cheat sheet from [Jason Mcdonalds blog](http://www.mcdonaldland.info/2007/11/28/40/)
