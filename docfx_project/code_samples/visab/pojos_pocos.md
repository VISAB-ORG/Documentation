# Creating POCOs and POJOs

All information sent from games to VISAB is using JSON as its data format.
To enable the respective game to have automated serialization from C# into JSON,
we need POCOS that represent the information to be sent to VISAB.

To correctly deserialize this information, VISAB needs **equivalent** POJOS within its own code.
By **equivalent** it is meant, that these classes need to resemble the exact same attributes and names for them.
Otherwise deserialization on the VISAB file will fail because of unknown attributes.

It is also possible to nest further classes in the POCOS / POJOS, they only need their respective implementation.

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

        public TetrisBoard Board { get; set; }
    }
}
```
##### TetrisBoard POCO
```csharp
using UnityEngine;

namespace VISABConnector.Example.Tetris
{
    public class TetrisBoard
    {
        public Color[,] Board { get; } = new Color[20, 10];
    }
}
```

### Code Samples for Fictive Implementation of Tetris game (VISAB - POJOs)