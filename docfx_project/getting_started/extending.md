# Extending VISAB for a New Game

The underlying code base of VISAB is designed to be easily extensible. This article will guide you through 
all relevant changes you need to perform, if you desire to make VISAB capable of supporting a new game.
As the below order already indicates, we advise you to start with the modifications in your game, because 
then you will have a fixed basis, of what shall be processed within VISAB.

### Step by Step Guidance

1. [Setup your environment](https://visab-org.github.io/getting_started/setup.html)
2. [Deploy the <code>VISABConnector</code> in your (Unity-) game](https://github.com/VISAB-ORG/VISABConnector)
3. [Create necessary POCOs in the game](https://visab-org.github.io/code_samples/visab/pojos_pocos.html)
4. [Implement a <code>VISABHelper</code> in your (Unity-) game to extract data and send it with the <code>VISABConnector</code>](https://visab-org.github.io/code_samples/old/connector.html)
5. [**[OPTIONAL]** Use the <code>VISABConnector.Unity</code> to perform snapshots](https://visab-org.github.io/code_samples/visabconnector_unity/images.html)
6. [Create a new <code>SessionListener</code> in VISAB](https://visab-org.github.io/code_samples/visab/listener.html)
7. [Create necessary POJOs in VISAB](https://visab-org.github.io/code_samples/visab/pojos_pocos.html)
8. [Create a <code>VISABFile</code> in VISAB](https://visab-org.github.io/code_samples/visab/file.html)
9. [Implement desired visualizers (at least one) for your (Unity-) game](https://visab-org.github.io/documentation/visualizer/index.html)
10. [Add respective classes to the <code>classMapping.json</code>](https://visab-org.github.io/code_samples/visab/class_mapping.html)