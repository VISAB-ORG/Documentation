# Using VISABConnector

We are concerned with transmitting the data of our Tetris game to VISAB so that we can use our visualizers.

Our player implementation could look like the following.
```csharp
public class Player
{
    public string Name { get; set; }

    public int Score { get; set; }

    public TetrisBoard Board { get; set; }
}
```
with `TetrisBoard` looking like this
```csharp
public class TetrisBoard
{
    public Color[,] Board { get; } = new Color[20, 10];

    public int CalculateScore()
    {
        // Some logic to calculate the score.
    }
}
```
The game controller of our Unity game has a method for incrementing a players score, switching the player and ending the game.
```csharp
public class TetrisGameController : MonoBehaviour
{
    private void IncrementPlayerPoints(Player player)
    {
        player.Score += player.Board.CalculateScore();
    }
    
    private async void SwitchPlayer(Player current) {
        // Determine the next player.
    }

    private async void OnGameEnded() {
        // Show a victory screen.
    }
}
```
We now want to supply our visualizers designed in TODO: link with statistics after every turn. To achieve this, we will use the `VISABConnector` library.

# Initializing a transmission session
We start by creating a `VISABApi` instance.
```csharp
public class TetrisGameController : MonoBehaviour
{
    ...

    private void Awake() {
        var api = new VISABApi("http://localhost", 2673, 1);
    }
}
```
The first parameter of `VISABApi`s constructor take the base adress of the machine that VISAB is running on. If VISAB is running on the same machine as the game, this will be `"http://localhost"`. The second parameter is the port and the third parameter the request timeout (in seconds). If VISAB is running on the same machine, 1 second is more than enough here. If VISAB is running on a machine that isnt in your local network, you'll have to figure out a suitable request timeout.

By creating the `VISABApi` instance, we have not made a call to VISAB yet. Lets now open a transmission session for our game by calling `api.InitiateSessionAsync`. 

# TODO
