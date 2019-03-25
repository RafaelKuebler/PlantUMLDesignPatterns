# Plant UML Design Patterns

[PlantUML](http://plantuml.com/index) code for some Design Patterns.
The syntax can be looked up on [PlantUML's class diagram documentation](http://plantuml.com/class-diagram).


## Running

If you do not intend to run locally, please have a look at the alternatives found in [this overview](http://plantuml.com/running).


## Included patterns

Creational
- Abstract factory
- Builder
- Factory method
- Prototype
- Singleton

Structural
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

Behavioral
- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template method
- Visitor


### Prerequisites

To run locally, the PlantUML jar (from [PlantUML's download](http://plantuml.com/download)) site is needed.
As described on the [Getting started](http://plantuml.com/starting) site, you will also need both [Java](https://www.java.com/en/download/) and [Graphviz](https://www.graphviz.org/) installed on your machine.

### Creating the diagrams
The easiest way is to just run the included python script ([run.py](run.py)).
It checks for changes in the diagram files and only generates the new/changed/not existing ones.

´´´
python run.py
´´´

The generated diagrams are stored in the *output* folder.

To run PlantUML directly from the command line for one specific diagram, you can execute:

´´´
java -jar plantuml.jar diagram.txt
´´´


## Built With

* [PlantUML](http://plantuml.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* The pattern descriptions and overall class diagram arrangements are taken from a cheat sheet from [Jason Mcdonalds blog](http://www.mcdonaldland.info/2007/11/28/40/)
