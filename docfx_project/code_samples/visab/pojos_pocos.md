# Creating POCOs and POJOs

All information sent from games to VISAB is using JSON as its data format.
To enable the respective game to have automated serialization from C# into JSON,
we need POCOS that represent the information to be sent to VISAB.

To correctly deserialize this information, VISAB needs **equivalent** POJOS within its own code.
By **equivalent** it is meant, that these classes need to resemble the exact same attributes and names for them.
Otherwise deserialization on the VISAB file will fail because of unknown attributes.

It is also possible to nest further classes in the POCOS / POJOS, they only need their respective implementations.

*For the special case of having an attribute or method within one of these data object classes that should be exluded from serialization, you can put a `@JsonIgnore` on the VISAB side.*

### Code Samples for Fictive Implementation of Tetris (Unity Game - POCOs)

##### TetrisMetaInformation POCO
```csharp
using System.Collections.Generic;

namespace VISABConnector.Example.Tetris
{
    public class TetrisMetaInformation : IMetaInformation
    {
        public string Game => "Tetris";

        public IList<string> PlayerNames { get; set; }

        public int PlayerCount => PlayerNames.Count;
    }
}
```

##### TetrisStatistics POCO
```csharp
using System.Collections.Generic;

namespace VISABConnector.Example.Tetris
{
    public class TetrisStatistics : IStatistics
    {
        public int Turn { get; set; }

        public IDictionary<string, int> PlayerPoints { get; set; }
    }
}
```
##### Player POCO
```csharp
namespace VISABConnector.Example.Tetris
{
    public class Player
    {
        public string Name { get; set; }

        public int Score { get; set; }
    }
}
```

### Code Samples for Fictive Implementation of Tetris game (VISAB - POJOs)

##### TetrisMetaInformation POJO
```java
package org.visab.globalmodel.Tetris;

public class TetrisMetaInformation implements IMetaInformation {

    private String game;
    private List<String> playerNames;
    private int playerCount;

    public String setGame() {
        return game;
    }

    public List<String> getPlayerNames() {
        return playerNames;
    }

    public void setPlayerNames(List<String> playerNames) {
        this.playerNames = playerNames;
    }

    public Rectangle getMapRectangle() {
        return mapRectangle;
    }

    public int getPlayerCount() {
        return playerCount;
    }

    public void setPlayerCount(int playerCount) {
        this.playerCount = playerCount;
    }

    @Override
    public String getGame() {
        return game;
    }

}
```

##### TetrisStatistics POJO
```java
package org.visab.globalmodel.Tetris;

public class TetrisStatistics implements IStatistics {

    private int turn;
    private HashMap<String, int> playerPoints;

    public int getTurn() {
        return turn;
    }

    public void setTurn(int turn) {
        this.turn = turn;
    }

    public HashMap<String, int> getPlayerPoints() {
        return playerPoints;
    }

    public void setPlayerPoints(HashMap<String, int> playerPoints) {
        this.playerPoints = playerPoints;
    }
}


```
##### Player POJO
```java
package org.visab.globalmodel.Tetris;

public class Player {

    private String name;
    private int score;

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

```